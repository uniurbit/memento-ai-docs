#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Università degli Studi di Urbino Carlo Bo
# SPDX-License-Identifier: CC-BY-4.0
"""Cattura deterministica delle interazioni con il modello.

Accoda a `registri/CONVERSATION.md` il testo verbatim della richiesta e della
risposta finale di ciascun turno. È l'attuazione del modo «cattura
dall'ambiente» prescritto in `registri/INSTRUCTIONS.md`, §4.1.

REQUISITI
    Python 3.8 o successivo, sola libreria standard. Nessuna dipendenza da
    installare.

INVOCAZIONE
    Lo strumento a riga di comando deve eseguire questo script in
    corrispondenza di due eventi del proprio ciclo di vita:

        richiesta  — dopo l'invio della richiesta da parte dell'utente
        risposta   — al completamento della risposta del modello

    Lo script accetta i dati dell'evento in tre forme, nell'ordine:

        1. un oggetto JSON su standard input        (forma più diffusa)
        2. variabili d'ambiente INTERAZIONE_*       (vedi sotto)
        3. argomenti sulla riga di comando          registra_interazione.py <evento> <testo>

    Il tipo di evento può sempre essere forzato come primo argomento, utile
    quando lo strumento non lo dichiara nei dati:

        registra_interazione.py richiesta
        registra_interazione.py risposta

ADATTAMENTO A UNO STRUMENTO DIVERSO
    Va modificata la sola sezione ADATTATORE, sotto: i nomi dei campi con cui
    lo strumento in uso denomina evento, testo, identificativo di turno e
    cartella di lavoro. Tutto il resto è indipendente dal prodotto.

VINCOLI DI FUNZIONAMENTO
    - Lo script NON scrive nulla su standard output. Alcuni strumenti
      iniettano l'output degli hook nel contesto del modello: qualunque
      messaggio di servizio finirebbe nella conversazione.
    - Lo script non fallisce mai in modo visibile: in caso di errore termina
      con codice 0 senza interrompere la sessione. Un archivio incompleto è un
      problema; una sessione interrotta dallo strumento di archiviazione è un
      problema peggiore.
    - La scrittura è protetta da lock esclusivo e marcata per turno: una
      riesecuzione non produce duplicati e più sessioni concorrenti non si
      sovrascrivono.
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import fcntl
except ImportError:  # piattaforme prive di fcntl: si procede senza lock
    fcntl = None

# ─── ADATTATORE ──────────────────────────────────────────────────────────────
# Unica sezione da modificare per adottare uno strumento diverso.
# Per ciascuna voce si elencano i nomi di campo possibili, in ordine di
# preferenza: viene usato il primo presente nei dati dell'evento.

CAMPI = {
    "evento":    ("hook_event_name", "event", "event_name", "type"),
    "richiesta": ("user_input", "prompt", "user_message", "input"),
    "risposta":  ("last_assistant_message", "assistant_message", "response", "output"),
    "turno":     ("prompt_id", "turn_id", "message_id", "request_id"),
    "sessione":  ("session_id", "conversation_id", "thread_id"),
    "cartella":  ("cwd", "workspace", "project_dir"),
}

# Nomi con cui lo strumento denomina i due eventi.
EVENTI = {
    "richiesta": ("UserPromptSubmit", "user_prompt_submit", "on_user_message", "pre_request"),
    "risposta":  ("Stop", "assistant_response_complete", "on_assistant_message", "post_response"),
}

# Percorso dell'archivio, relativo alla radice del progetto.
ARCHIVIO = Path("registri") / "CONVERSATION.md"
INTESTAZIONE = "# Conversazione\n"
# ─── FINE ADATTATORE ─────────────────────────────────────────────────────────


def primo_presente(dati: dict, nomi) -> str | None:
    """Restituisce il primo campo presente e non vuoto fra quelli indicati."""
    for nome in nomi:
        valore = dati.get(nome)
        if isinstance(valore, str) and valore != "":
            return valore
    return None


def leggi_evento() -> dict:
    """Acquisisce i dati dell'evento da stdin, dall'ambiente o dagli argomenti."""
    dati: dict = {}

    if not sys.stdin.isatty():
        grezzo = sys.stdin.read()
        if grezzo.strip():
            try:
                caricato = json.loads(grezzo)
                if isinstance(caricato, dict):
                    dati = caricato
            except json.JSONDecodeError:
                pass

    # Variabili d'ambiente: INTERAZIONE_EVENTO, INTERAZIONE_TESTO, ...
    for chiave, variabile in (
        ("evento", "INTERAZIONE_EVENTO"),
        ("testo", "INTERAZIONE_TESTO"),
        ("turno", "INTERAZIONE_TURNO"),
        ("sessione", "INTERAZIONE_SESSIONE"),
    ):
        valore = os.environ.get(variabile)
        if valore and chiave not in dati:
            dati[chiave] = valore

    # Argomenti: <evento> [testo]
    if len(sys.argv) > 1:
        dati["evento_forzato"] = sys.argv[1].strip().lower()
    if len(sys.argv) > 2:
        dati.setdefault("testo", sys.argv[2])

    return dati


def classifica(dati: dict) -> str | None:
    """Determina se l'evento è una richiesta o una risposta."""
    forzato = dati.get("evento_forzato")
    if forzato in ("richiesta", "risposta"):
        return forzato

    dichiarato = primo_presente(dati, CAMPI["evento"]) or dati.get("evento") or ""
    if dichiarato.strip().lower() in ("richiesta", "risposta"):
        return dichiarato.strip().lower()

    for tipo, nomi in EVENTI.items():
        if dichiarato in nomi:
            return tipo

    # Ultimo criterio: la presenza di uno dei due campi di testo.
    if primo_presente(dati, CAMPI["richiesta"]):
        return "richiesta"
    if primo_presente(dati, CAMPI["risposta"]):
        return "risposta"
    return None


def estrai_testo(dati: dict, tipo: str) -> str | None:
    return primo_presente(dati, CAMPI[tipo]) or dati.get("testo")


def radice_progetto(dati: dict) -> Path:
    """Radice del repository, dedotta da Git o dalla posizione dello script."""
    cartella = primo_presente(dati, CAMPI["cartella"]) or os.getcwd()
    try:
        esito = subprocess.run(
            ["git", "-C", cartella, "rev-parse", "--show-toplevel"],
            check=True, capture_output=True, text=True, timeout=5,
        )
        return Path(esito.stdout.strip()).resolve()
    except (subprocess.SubprocessError, OSError):
        return Path(__file__).resolve().parent.parent


def accoda(destinazione: Path, marcatore: str, blocco: str) -> None:
    """Scrive in coda, una volta sola per marcatore, con lock esclusivo."""
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    with destinazione.open("a+", encoding="utf-8") as flusso:
        if fcntl is not None:
            fcntl.flock(flusso.fileno(), fcntl.LOCK_EX)
        flusso.seek(0)
        esistente = flusso.read()
        if marcatore in esistente:      # turno già registrato: nessun duplicato
            return
        if not esistente.strip():
            flusso.seek(0, 2)
            flusso.write(INTESTAZIONE)
        flusso.seek(0, 2)
        flusso.write(blocco)
        flusso.flush()


def main() -> int:
    dati = leggi_evento()

    tipo = classifica(dati)
    if tipo is None:
        return 0

    testo = estrai_testo(dati, tipo)
    if not isinstance(testo, str) or testo == "":
        return 0

    turno = primo_presente(dati, CAMPI["turno"]) or dati.get("turno")
    if not turno:
        # Nessun identificativo dallo strumento: se ne deriva uno dal testo.
        # Stabile per contenuto, quindi la riesecuzione non duplica e due turni
        # distinti non collidono sullo stesso marcatore.
        turno = hashlib.sha256(testo.encode("utf-8")).hexdigest()[:12]
    sessione = primo_presente(dati, CAMPI["sessione"]) or dati.get("sessione") or "sessione-ignota"
    istante = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    marcatore = f"<!-- interazione:{sessione}:{turno}:{tipo} -->"
    etichetta = "Richiesta" if tipo == "richiesta" else "Risposta"
    blocco = (
        f"\n{marcatore}\n"
        f"## {etichetta} — {istante} — cattura: ambiente\n\n"
        f"{testo}\n"
    )

    accoda(radice_progetto(dati) / ARCHIVIO, marcatore, blocco)
    return 0


if __name__ == "__main__":
    try:
        codice = main()
    except Exception:       # nessun errore deve interrompere la sessione
        codice = 0
    raise SystemExit(codice)
