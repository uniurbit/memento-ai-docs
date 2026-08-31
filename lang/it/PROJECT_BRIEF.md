# Avvio del progetto

> **Prima istruzione, vincolante.**
>
> Questo è il primo documento da leggere in ogni sessione di lavoro su questo
> progetto. Contiene il **mandato**: che cosa si deve produrre e con quali
> vincoli di merito.
>
> Le **regole operative** — ordine di lettura, procedure di apertura e di
> chiusura del turno, aggiornamento dei registri, interpretazione delle
> annotazioni dell'utente nei file, uso di Git — non sono qui: risiedono in
> `REGISTERS/INSTRUCTIONS.md`.
>
> **`REGISTERS/INSTRUCTIONS.md` DEVE essere letto integralmente subito dopo
> questo file, e osservato per tutta la lavorazione.** Le sue prescrizioni sono
> vincolanti e non ammettono interpretazione discrezionale. Nessuna attività
> materiale DEVE essere avviata prima di averlo letto.
>
> La sequenza di apertura prescritta da `REGISTERS/INSTRUCTIONS.md`, §2 comprende
> la lettura dei registri di stato e di attività e la ricognizione delle fonti
> presenti in `CONTEXT/`. La lettura di questo file è pertanto sufficiente ad
> avviare la sessione: non occorre elencare al modello i documenti da aprire.
>
> **Le sezioni da 1 a 6 DEVONO essere compilate prima dell'acquisizione delle
> fonti.** La compilazione del mandato è il primo atto della Fase 1 del metodo
> (§7.2.2 della specifica); la sezione 7 è fornita compilata e vale per qualunque
> progetto.
>
> **Lingua.** Questo è il mandato in italiano. L'inglese è la lingua della radice
> del kit; le altre lingue stanno in `lang/`, e `lang/` viene rimossa in fase di
> allestimento (`README.md`, Appendice tecnica 5).

---

## 1. Metadati

- **Progetto:** `[denominazione]`
- **Fonte del mandato:** `[soggetto che ha impartito le istruzioni]`
- **Data di ricezione:** `[data]`
- **Contesto di lavorazione:** `[strumento impiegato e collocazione del progetto]`

---

## 2. Scopo del progetto

`[Documento da produrre, destinatari, finalità. L'impossibilità di esprimerlo in
forma sintetica indica un perimetro non ancora definito.]`

---

## 3. Perimetro concettuale

`[Ambito di copertura del documento e distinzioni fra le categorie rilevanti.
Le definizioni informali costituiscono guida iniziale e DEVONO essere
formalizzate mediante fonti normative e documenti istituzionali.]`

---

## 4. Principi di redazione richiesti

`[Ruolo assegnato al modello; estensione della ricerca oltre il contesto locale;
convenzioni linguistiche; formato di lavoro; vincoli di neutralità tecnologica.]`

**Documenti da non impiegare come base.** `[Elenco dei documenti presenti in
`CONTEXT/` a soli fini di inquadramento. In assenza di questo elenco il modello
attribuisce loro il medesimo peso delle fonti principali.]`

---

## 5. Contenuto sostanziale da tradurre in testo

`[Decisioni di merito già assunte, elencate. È la parte specifica del singolo
progetto e non è deducibile dal modello.]`

---

## 6. Ruoli

L'attribuzione dei ruoli DEVE essere dichiarata anche in strutture di ridotte
dimensioni: il metodo distribuisce l'esecuzione fra persona e modello, mentre la
responsabilità non è distribuibile.

| Ruolo | Titolare | Responsabilità |
| --- | --- | --- |
| **Referente del progetto** | `[…]` | Definizione di obiettivi e vincoli, mantenimento di stato e istruzioni, decisione nel merito. |
| **Redattore** | `[…]` | Costruzione del contesto, conduzione del ciclo di produzione, tenuta del worklog. |
| **Validatore** | `[…]` | Verifica del risultato in assenza di partecipazione alla redazione. |
| **Responsabile del rilascio** | `[…]` | Autorizzazione all'esportazione nei formati finali e alla messa agli atti. |

La separazione fra chi redige e chi valida costituisce l'unica separazione di
ruoli obbligatoria. Il modello non esercita potere decisionale in alcun ruolo.

---

## 7. Struttura del progetto

```
progetto/
├── PROJECT_BRIEF.md   questo file: il mandato
├── README.md           il metodo e le sue motivazioni; non si legge a ogni sessione
├── CONTEXT/           documentazione di riferimento (input)
├── RELEASE/           versioni finali esportate (output)
├── TOOLS/          script di cattura delle interazioni
└── REGISTERS/
    ├── INSTRUCTIONS.md   le regole operative: vincolanti, si leggono sempre
    ├── PROJECT.md        stato del progetto
    ├── WORKLOG.md        attività svolte, con verifiche ed esito
    └── CONVERSATION.md   richieste al modello e relative risposte
```

**Aggancio allo strumento.** Gli strumenti a riga di comando di maggiore
diffusione leggono all'avvio un file di istruzioni la cui denominazione varia per
prodotto. Tale file DEVE limitarsi a rinviare a questo documento:

```markdown
All'inizio di ogni sessione leggere integralmente `PROJECT_BRIEF.md`,
quindi `REGISTERS/INSTRUCTIONS.md`, e attenersi a quest'ultimo per l'intera
lavorazione.
```

È l'unico punto di contatto fra il metodo e uno specifico prodotto. L'adozione
del metodo con uno strumento diverso comporta la sola riscrittura di questo
rinvio.
