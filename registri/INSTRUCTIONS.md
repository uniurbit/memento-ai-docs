# Istruzioni operative

> **Questo file è vincolante.** Va letto integralmente all'inizio di ogni
> sessione, prima di qualunque attività materiale, e osservato per tutta la
> lavorazione.
>
> Contiene prescrizioni, non spiegazioni: la motivazione di ciascuna regola è in
> `README.md`, che NON DEVE essere letto a ogni sessione. Chi voglia comprendere
> una regola consulti il README; chi debba applicarla si attenga a questo file.
>
> Le parole **DEVE**, **NON DEVE**, **DOVREBBE**, **PUÒ** in maiuscolo hanno
> l'interpretazione univoca definita in `README.md`, §2.

---

## 1. Ambito e precedenza

Questo file specifica **come si lavora**. `AVVIO_PROGETTO.md` specifica **che
cosa si deve produrre**. `README.md` specifica **perché il metodo è fatto così**.

In caso di prescrizioni fra loro incompatibili si applica il seguente ordine di
precedenza:

1. Una richiesta esplicita dell'utente nella sessione corrente.
2. `AVVIO_PROGETTO.md` (mandato, perimetro, ruoli).
3. Questo file.
4. `README.md`.

**Il conflitto NON DEVE essere risolto in silenzio.** Anche quando la precedenza
è chiara, la divergenza DEVE essere segnalata all'utente prima di procedere
sull'attività interessata. Se una richiesta della sessione contraddice il
mandato, il modello DEVE chiedere conferma e NON DEVE dedurre l'intenzione.

---

## 2. Apertura della sessione

I passi seguenti DEVONO essere eseguiti nell'ordine indicato, prima di qualunque
attività materiale.

1. Eseguire `git status`. Le modifiche locali non riconosciute NON DEVONO essere
   nascoste, annullate o incorporate: vanno segnalate.
2. Se esiste un repository remoto, eseguire `git fetch`. DEVONO essere accettati
   soltanto avanzamenti lineari. Ogni divergenza DEVE essere segnalata e NON
   DEVE essere risolta autonomamente.
3. Leggere integralmente `AVVIO_PROGETTO.md`.
4. Leggere integralmente questo file.
5. Leggere integralmente `registri/PROJECT.md`.
6. Leggere la porzione finale di `registri/WORKLOG.md`, sufficiente a coprire le
   ultime attività; cercarvi le voci pertinenti al compito richiesto.
7. Prendere cognizione delle fonti disponibili in `contesto/`: leggerne il
   manifest quando esiste, altrimenti l'elenco dei file. Gli scostamenti
   rispetto al perimetro dichiarato nel mandato DEVONO essere segnalati. Le
   singole fonti si aprono quando il compito lo richiede, non per prassi.

`registri/CONVERSATION.md` NON DEVE essere caricato in contesto. Si consulta
esclusivamente con ricerche mirate, quando occorre il testo originale di una
richiesta o di una risposta.

`README.md` NON DEVE essere caricato in contesto durante il lavoro ordinario. Si
consulta con ricerche mirate quando occorre la motivazione di una regola.

**Dichiarazione di lettura.** Completata la sequenza, il modello DEVE dichiarare
in apertura di risposta, in non più di quattro righe: lo stato corrente del
progetto, l'ultima attività registrata, la consistenza del contesto disponibile
e l'eventuale questione aperta pertinente al compito richiesto. La
dichiarazione rende verificabile l'avvenuta lettura.

---

## 3. Il lavoro

### 3.1 Il processo in sei fasi

Il lavoro si articola in sei fasi. Qui è prescritta la sola sequenza; le
motivazioni sono in `README.md`.

| Fase | Oggetto | Si conclude quando |
| --- | --- | --- |
| **0 — Ambiente** | Allestimento tecnico: installazione dello strumento e del modello | Lo strumento si avvia e Git è disponibile |
| **1 — Avvio del progetto** | Repository, registri, ruoli, verifiche preliminari, mandato, fonti, manifest | Il mandato è compilato e il manifest copre il perimetro che vi è dichiarato |
| **2 — Ciclo di produzione** | Redazione iterativa fino alla versione candidata | Una lettura integrale non fa emergere modifiche sostanziali |
| **3 — Revisione esterna** | Sottoposizione a soggetti non coinvolti nella redazione | I revisori non richiedono ulteriori modifiche |
| **4 — Rilascio** | Esportazione, verifica di accessibilità, adozione formale | Il documento è adottato con l'atto competente |
| **5 — Revisioni di medio periodo** | Riesame nel tempo | Si rientra dalla Fase 1 quando il quadro è mutato |

**Il ciclo della Fase 2.** La prima bozza (azione **2.1**) si produce una volta
sola, all'apertura della fase. Ciascun giro successivo esegue i passi seguenti:

1. **Modifica della documentazione** (azione **2.2**), nelle due forme che si
   alternano secondo il bisogno e senza un ordine fisso: **2.2.a prompting** —
   richiesta al modello sulla base del mandato e del contesto; **2.2.b
   aggiornamento del contesto** — se il giro ha evidenziato un'insufficienza
   delle fonti (§3.2).
2. **Revisione umana** (azione **2.3**) — l'utente annota il documento (§3.3).
   Il modello DEVE committare lo stato annotato **prima** di eseguire le
   annotazioni, senza che gli venga chiesto, e recepisce poi le annotazioni in
   una versione pulita.
3. **Analisi di completezza** (azione **2.4**) — richiesta esplicita al modello di verificare
   completezza e coerenza rispetto all'intero corpus: riferimenti mancanti,
   documentazione di supporto necessaria, incongruenze con la normativa
   vigente. **DEVE essere eseguita dopo la revisione umana e non prima**, in
   modo che verta sul testo nella formulazione voluta dalla persona.

Il giro si chiude con la sequenza di §4, che si esegue in coda a ciascuna
azione. Si itera dal passo 1.

**Conservazione dello stato annotato.** Il modello DEVE registrare in Git lo
stato annotato dall'utente prima di riscriverlo: è quel commit a conservare
l'intervento umano. L'operazione è a carico del modello e NON DEVE attendere una
richiesta esplicita dell'utente. Il recepimento produce la versione pulita nello
stesso file; le due versioni sono due commit successivi e si recuperano
entrambe dalla cronologia. NON DEVE essere creata una copia del documento con
un nome diverso: duplicherebbe ciò che Git già conserva.

**Versioni candidate.** La versione che esce dal ciclo per essere sottoposta a
revisione esterna è una *release candidate* e DEVE essere numerata
progressivamente: RC 1, RC 2, …, RC *n*. Una bozza interna al ciclo NON è una
release candidate e non riceve numerazione. Se la revisione esterna richiede
modifiche, il documento rientra nella Fase 2 e ne esce come RC successiva. Se
non ne richiede, la RC in esame accede alla Fase 4.

**Passaggio di fase.** Ogni passaggio da una fase alla successiva DEVE essere
registrato con una voce di worklog e chiuso con un commit.

### 3.2 Cartelle e file

- Il contenuto delle fonti in `contesto/` NON DEVE essere modificato.
- La composizione di `contesto/` PUÒ essere modificata — aggiunta, rimozione,
  riclassificazione — quando ricorra una ragione. La ragione DEVE essere
  annotata nel manifest e nel worklog.
- Il manifest delle fonti DEVE essere aggiornato contestualmente
  all'acquisizione di ciascuna fonte, mai a lavorazione conclusa. Ciascun record
  riporta: identificativo breve, titolo, provenienza, data di acquisizione, nome
  della copia locale, ragione dell'acquisizione.
- Una fonte reperita per via indiretta o sostitutiva DEVE essere annotata come
  tale nel manifest.
- `rilascio/` NON DEVE essere modificata manualmente dopo l'esportazione.
- `strumenti/` contiene lo script di cattura delle interazioni (§4.1). NON DEVE
  essere modificato durante la lavorazione, salvo per l'adattamento allo
  strumento in uso, che DEVE essere registrato nel worklog.
- Le bozze risiedono nella radice del progetto o in una cartella dedicata, in
  formato testuale aperto.

### 3.3 Annotazioni dell'utente nei file

L'utente non corregge il testo prodotto: lo **annota**. Le annotazioni sono
istruzioni da eseguire, inserite nel corpo del file.

**Riconoscimento.** Un'annotazione è delimitata da tre parentesi angolari aperte
e tre chiuse, e si riferisce al passaggio che la precede immediatamente:

```text
La casella è disattivata decorsi due anni dalla cessazione del
rapporto.<<<specificare che il termine decorre dalla cessazione formale
e non dall'ultimo accesso; aggiungere il rinvio all'art. 12>>>
```

**Precedenza sulla lettura.** Quando l'utente chiede di prendere in carico un
file, le annotazioni DEVONO essere individuate **prima** di qualunque analisi,
validazione o riformattazione del file ospite. Sono istruzioni, non contenuto.

**Registrazione preventiva.** Prima di eseguire qualunque annotazione, il
modello DEVE committare il file nello stato in cui l'ha ricevuto, con un
messaggio che dichiari la presenza di annotazioni umane da recepire — per
esempio `docs(regolamento): acquisisci le annotazioni umane sulla sezione 3`.
L'operazione precede ogni modifica e NON DEVE essere omessa neppure quando
l'utente chiede direttamente il recepimento.

**Esecuzione.** Per ciascuna annotazione:

1. Eseguire l'istruzione che contiene. L'annotazione descrive un intervento; NON
   DEVE essere trascritta nel testo.
2. Verificare l'esito.
3. Rimuovere dal file l'annotazione eseguita, insieme al testo che essa
   sostituisce ove previsto.

**Annotazioni da non rimuovere.** NON DEVONO essere rimosse le annotazioni
incomplete, ambigue, incompatibili con altre istruzioni, non eseguite o la cui
esecuzione sia fallita. Restano nel file e la circostanza DEVE essere segnalata
all'utente, con l'indicazione della ragione.

**Delimitatori non conformi.** Un'annotazione delimitata da un numero di
caratteri diverso da tre NON è conforme. Se il contenuto è univoco PUÒ essere
eseguita, ma l'anomalia DEVE essere segnalata. Se il contenuto è ambiguo, NON
DEVE essere eseguita.

**Archiviazione.** Se il progetto tiene l'archivio delle interazioni,
l'annotazione DEVE esservi registrata verbatim **prima** di essere rimossa dalla
fonte, con l'indicazione del file e della riga di origine. I delimitatori DEVONO
essere codificati in modo da non essere rieseguiti a una successiva lettura
dell'archivio.

**Esempi.** Le occorrenze dei delimitatori all'interno di blocchi di codice non
sono annotazioni e NON DEVONO essere eseguite.

**Natura contestuale.** Un'annotazione vale per il compito in corso. NON DEVE
essere registrata come regola generale in questo file né come stato realizzato
in `PROJECT.md`, salvo che il suo contenuto lo disponga espressamente.

### 3.4 Regole di redazione

**Dati non disponibili.** La mancanza DEVE essere dichiarata; il contenuto
plausibile NON DEVE essere prodotto. Il documento reca un segnaposto esplicito
che indica l'oggetto mancante e la ragione. L'elenco degli elementi da verificare
accompagna la bozza come sezione autonoma, con una voce per lacuna.

**Dati personali.** Nelle richieste DEVONO essere inclusi i soli dati personali
necessari a produrre il documento. Quando un documento rilevi per la struttura o
per il contenuto dispositivo e non per i nominativi, DEVE esserne conferita la
sola parte utile.

**Verificabilità.** Ogni affermazione del documento prodotto DEVE essere
riconducibile alla fonte che la sostiene da parte di chi non ha partecipato al
lavoro. Le affermazioni prive di fonte DEVONO essere segnalate come tali.

**Distinzione dei modi della verità.** Un fatto verificato, un'inferenza e una
previsione NON DEVONO essere scritti allo stesso modo. NON DEVE essere annotato
«verificato» ciò che non è stato verificato, né «pubblicato» ciò che non è stato
pubblicato.

**Decisioni.** Il modello propone e revisiona. Le decisioni di merito e la
validazione finale spettano alla persona. La motivazione di un provvedimento
amministrativo NON DEVE essere prodotta dal modello.

**Chiarimenti.** In presenza di ambiguità il modello DEVE formulare una domanda
anziché risolverla autonomamente.

---

## 4. Chiusura del turno

I passi seguenti DEVONO essere eseguiti in coda a ogni interazione che abbia
prodotto una modifica materiale, nell'ordine indicato.

1. **Archivio delle interazioni** — §4.1.
2. **Worklog**, se l'attività è significativa — §4.2.
3. **Stato del progetto**, se il quadro è cambiato — §4.3.
4. **Commit** — §4.4.

Un'interazione che non produce modifiche materiali non richiede nessuno dei
quattro passi, salvo l'archivio delle interazioni, che è indipendente dall'esito.

### 4.1 Archivio delle interazioni

`CONVERSATION.md` conserva le due estremità di ciascun turno — testo della
richiesta e risposta finale — **verbatim**. NON DEVONO esservi registrati
ragionamento interno, chiamate agli strumenti, output di comandi o log tecnici.

L'alimentazione avviene in **uno solo** di due modi, che si escludono a vicenda.
Il modo adottato DEVE essere annotato in `PROJECT.md`.

#### Caso A — cattura dall'ambiente

Uno script agganciato allo strumento registra entrambe le estremità di ogni
turno. È il modo da preferire ovunque sia praticabile: è deterministico, copia
il testo senza rielaborarlo e non consuma risorse di elaborazione.

Il template fornisce l'implementazione: `strumenti/registra_interazione.py`.
Richiede Python 3 e la sola libreria standard. Va agganciato ai due eventi che
lo strumento espone — invio della richiesta e completamento della risposta —
secondo la sintassi di configurazione del prodotto in uso. Esempio di aggancio,
in forma generica:

```
evento «richiesta inviata»      → python3 strumenti/registra_interazione.py
evento «risposta completata»    → python3 strumenti/registra_interazione.py
```

Lo script riconosce da sé quale dei due eventi lo ha invocato. Se lo strumento
non dichiara il tipo di evento, questo va passato come primo argomento
(`richiesta` oppure `risposta`). L'adattamento a uno strumento diverso richiede
la modifica della sola sezione `ADATTATORE` in testa allo script.

**La copertura DEVE essere completa.** Una configurazione che intercetti un solo
evento **non è conforme**: produce un archivio che conserva metà di ogni turno
senza dichiararlo. Va completata, oppure disattivata passando al Caso B. Il
Caso A e il Caso B NON DEVONO coesistere: ne risulterebbero record duplicati e
modi di cattura mescolati nello stesso archivio.

**L'abilitazione è un atto umano.** Il modello NON DEVE tentare di abilitare da
sé l'aggancio, né modificare la configurazione dello strumento per attivarlo: il
soggetto che verrebbe registrato non autorizza il proprio registratore. Il
modello PUÒ predisporre la dichiarazione e DEVE indicare all'utente che
l'abilitazione resta a suo carico. La procedura è in `README.md`, §6.3.

**Verifica all'adozione.** Alla prima sessione dopo l'aggancio DEVE essere
verificato che l'archivio contenga entrambe le estremità del turno. Il modello
NON DEVE presumere il Caso A dalla sola presenza di una dichiarazione nella
configurazione: dichiarazione e abilitazione sono stati distinti. In assenza di
una delle due estremità si applica il capoverso precedente.

Nel Caso A il modello **NON DEVE scrivere** in `CONVERSATION.md`.

#### Caso B — cattura dal modello

Quando lo strumento non espone gli eventi necessari, o non li espone entrambi,
la registrazione è a carico del modello, che al termine di ogni turno accoda
entrambe le estremità.

Prescrizioni di esecuzione, tutte vincolanti:

- La scrittura avviene con **una sola operazione di accodamento per turno**,
  mediante un comando di shell che scrive in coda al file. NON DEVE essere
  impiegato uno strumento di modifica che richieda la previa lettura del file.
- Il file NON DEVE essere caricato in contesto, né prima né dopo la scrittura.
- L'esito della scrittura NON DEVE essere verificato rileggendo il file.
- Ogni record DEVE recare un marcatore di turno, affinché una riesecuzione non
  produca doppioni.
- Il testo NON DEVE essere riassunto, riformulato, abbreviato o normalizzato. Se
  una porzione non è riproducibile verbatim, DEVE essere dichiarata omessa con
  l'indicazione della sua estensione e della ragione; NON DEVE essere sostituita
  da una sintesi. Una sintesi non dichiarata rende l'archivio inservibile allo
  scopo per cui esiste.

**Limite del Caso B, da dichiarare in `PROJECT.md`.** Il soggetto che registra
coincide con il soggetto registrato, e la completezza dell'archivio dipende dal
fatto che il modello non ometta la scrittura. La dichiarazione del modo in
ciascun record rende la circostanza ispezionabile da chi rilegga l'archivio.

#### Formato del record

È **identico nei due casi**, salvo la dichiarazione del modo di cattura. Un
archivio deve restare leggibile anche quando il progetto passa da un caso
all'altro.

```markdown
<!-- interazione:<sessione>:<turno>:richiesta -->
## Richiesta — 2026-08-26T17:04:11+02:00 — cattura: ambiente

testo verbatim della richiesta

<!-- interazione:<sessione>:<turno>:risposta -->
## Risposta — 2026-08-26T17:06:02+02:00 — cattura: ambiente

testo verbatim della risposta finale
```

Nel Caso B la dichiarazione è `cattura: modello`. Il file si apre con
l'intestazione `# Conversazione`, che la prima scrittura crea se assente.

### 4.2 Worklog

Una voce per **attività significativa**: un documento è avanzato, una decisione è
stata assunta, una verifica ha modificato il grado di affidamento sul risultato,
un problema è emerso. NON DEVE essere prodotta una voce per singolo comando
eseguito.

`WORKLOG.md` è **append-only**: le voci si aggiungono in coda e NON DEVONO essere
riscritte. Un errore si corregge aggiungendo una voce che rettifica.

Data e ora DEVONO essere prese dall'orologio di sistema (`date -Iseconds`) e NON
DEVONO essere ricostruite a memoria.

L'aggiornamento del worklog NON DEVE essere annotato nel worklog.

```markdown
## AAAA-MM-GGTHH:MM:SS+TZ — Titolo sintetico

**Scopo:** risultato che si voleva ottenere.

**Attività e metodo:**
- azione significativa e modo in cui è stata svolta;
- decisione implementativa rilevante;
- tentativo fallito che ha cambiato l'approccio.

**Artefatti interessati:**
- `percorso/file.ext` — tipo di modifica.

**Verifiche:**
- controllo realmente eseguito — esito osservato;
- limite della verifica, se esiste.

**Decisioni e note:**
- decisione durevole, rischio, assunzione, informazione per il futuro.

**Stato:** completato | parziale | bloccato | annullato.

**Prossimo passo:** azione residua concreta, se presente.
```

### 4.3 Stato del progetto

`PROJECT.md` si modifica sul posto e DEVE essere aggiornato **soltanto** quando
cambiano ambito, struttura, stato di realizzazione, decisioni strutturali, rischi
o direzione. NON DEVE essere impiegato come secondo worklog.

Sezioni: sintesi, ambito (incluso ed escluso), struttura corrente, artefatti
principali, stato complessivo in tabella, decisioni strutturali, rischi e
questioni aperte, direzione.

Nella tabella di stato DEVONO essere distinti il **grado di realizzazione** e
l'**evidenza** che lo sostiene: implementato, previsto, ipotizzato, e in base a
quale riscontro.

Una decisione revocata NON DEVE essere cancellata: DEVE essere registrata come
revocata, con la data.

### 4.4 Commit

Il commit chiude l'iterazione. Il modello valuta il momento e lo esegue: a
ciascun giro del ciclo di produzione e a ciascun passaggio di fase.

Prima di ogni commit:

- Verificare che nell'indice non vi siano file estranei all'attività in corso.
- Verificare che non vengano versionati chiavi, credenziali, dati personali non
  necessari o file generati di grandi dimensioni.
- Preservare le modifiche concorrenti estranee all'attività.

Convenzione: `tipo(ambito): descrizione`, breve, imperativa e semanticamente
coerente con la voce di worklog. Tipi: `feat`, `fix`, `docs`, `refactor`,
`chore`, `meta`, `checkpoint`.

Dal messaggio DEVE risultare **distinguibile l'intervento umano da quello del
modello**: i commit che recepiscono annotazioni dell'utente lo dichiarano.

```text
docs(regolamento): recepisci le annotazioni dell'utente sulla sezione 3
docs(regolamento): colma la lacuna sulle proroghe rilevata dall'analisi
```

Il messaggio dice **che cosa** è cambiato. Il **perché** va nel worklog.

---

## 5. Git — regole permanenti

- NON DEVE essere eseguito force push.
- NON DEVE essere riscritta storia già condivisa.
- NON DEVONO essere cancellati branch o tag remoti senza autorizzazione
  esplicita.
- Gli stati parziali da conservare senza pubblicarli come definitivi DEVONO
  essere posti su branch di checkpoint.
- Quando i redattori sono più di uno, il ramo principale NON DEVE essere
  modificato direttamente: ciascuno opera su un ramo proprio e integra a ciclo
  concluso.
- Un conflitto di integrazione su una bozza è una decisione di merito e NON DEVE
  essere risolto dal modello.
- Tag annotati e versionamento semantico si impiegano soltanto per rilasci
  deliberati.
- Chiavi, credenziali e dati non versionabili restano fuori dal repository.

---

## 6. Riferimento rapido

**All'apertura:** `git status` → `git fetch` se remoto → `AVVIO_PROGETTO.md` →
questo file → `PROJECT.md` → coda di `WORKLOG.md` → manifest di `contesto/` →
dichiarazione di lettura in quattro righe.

**Durante:** eseguire le fasi nell'ordine · analisi di completezza dopo la
revisione umana · committare lo stato annotato prima di recepirlo (a carico del modello) · non
modificare le fonti · annotare in manifest e worklog ogni
variazione del contesto · eseguire le annotazioni prima di ogni altra analisi ·
dichiarare le lacune invece di colmarle · segnalare i conflitti invece di
risolverli · chiedere invece di dedurre.

**Alla chiusura:** archivio delle interazioni, se il progetto è nel Caso B di
§4.1 → worklog se significativo → stato se il quadro è cambiato → commit.

**Mai:** caricare `CONVERSATION.md` in contesto · riassumere un record verbatim ·
riscrivere il worklog · decidere nel merito · produrre la motivazione di un
provvedimento · risolvere un conflitto in silenzio.
