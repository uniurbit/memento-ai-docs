# Languages of the kit – how this folder works

Each subfolder here is **one language of the kit**, and holds only what changes
with the language: the specification (`README.md`), the project brief, the four
registers and, where it is translated, the figure.

It is **not** a self-contained copy of the kit, and it does not need to be.
Everything that does not change with the language lives once, at the root of the
repository: the interaction-capture script in `TOOLS/`, `LICENSE`, `LICENSES/`,
`REUSE.toml`, `.gitignore`, and the two working folders `CONTEXT/` and
`RELEASE/`, which are empty because the adopting administration fills them.

The choice of language is therefore an **overlay**, not a move: the documents of
one language are laid over the root, and the folder of languages is removed.

```shell
cp -r lang/it/. .   # Italian over the root; for English, skip this line
rm -rf lang         # one language only, from here on
```

What remains is a complete project in one language. The reasons, what must stay
identical between languages, and how to add a language are in `README.md`,
Technical appendix 5.

---

# Le lingue del kit – come funziona questa cartella

Ogni sottocartella è **una lingua del kit** e contiene soltanto ciò che cambia
con la lingua: la specifica (`README.md`), il documento di avvio, i quattro
registri e, dove è tradotta, la figura.

**Non** è una copia autonoma del kit, e non deve esserlo. Tutto ciò che non
cambia con la lingua vive una volta sola, nella radice del repository: lo script
di cattura in `TOOLS/`, `LICENSE`, `LICENSES/`, `REUSE.toml`, `.gitignore` e le
due cartelle di lavoro `CONTEXT/` e `RELEASE/`, vuote perché le riempie l'ente
adottante.

La scelta della lingua è quindi una **sovrapposizione**, non uno spostamento: i
documenti di una lingua si sovrappongono alla radice, e la cartella delle lingue
viene rimossa.

```shell
cp -r lang/it/. .   # l'italiano sopra la radice; per l'inglese si salta questa riga
rm -rf lang         # da qui in avanti, una lingua sola
```

Ciò che resta è un progetto completo in una lingua sola. Le ragioni, ciò che deve
restare identico fra le lingue e il modo di aggiungerne una sono in `README.md`,
Appendice tecnica 5.
