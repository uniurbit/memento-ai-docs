# Project start-up

> **First instruction, binding.**
>
> This is the first document to be read in every working session on this
> project. It holds the **mandate**: what has to be produced and under which
> substantive constraints.
>
> The **operating rules** — order of reading, procedures for opening and closing
> a turn, updating the registers, interpreting the user's annotations in the
> files, use of Git — are not here: they reside in `REGISTERS/INSTRUCTIONS.md`.
>
> **`REGISTERS/INSTRUCTIONS.md` MUST be read in full immediately after this
> file, and observed throughout the work.** Its prescriptions are binding and
> admit of no discretionary interpretation. No material activity MUST be started
> before it has been read.
>
> The opening sequence prescribed by `REGISTERS/INSTRUCTIONS.md`, §2 includes
> reading the registers of state and of activities and surveying the sources
> present in `CONTEXT/`. Reading this file is therefore enough to start the
> session: there is no need to list for the model the documents it should open.
>
> **Sections 1 to 6 MUST be filled in before the sources are acquired.** Filling
> in the mandate is the first act of Phase 1 of the method (§7.2.2 of the
> specification); section 7 is supplied ready-written and holds for any project.
>
> **Language.** This is the project brief in English, the language of the root
> of the kit. The other languages are in `lang/`, and `lang/` is removed when
> the project is set up (`README.md`, Technical appendix 5).

---

## 1. Metadata

- **Project:** `[name]`
- **Source of the mandate:** `[who gave the instructions]`
- **Date received:** `[date]`
- **Working context:** `[tool employed and where the project sits]`

---

## 2. Purpose of the project

`[Document to be produced, addressees, aim. If it cannot be expressed concisely,
the perimeter is not yet defined.]`

---

## 3. Conceptual perimeter

`[What the document covers and the distinctions between the relevant categories.
Informal definitions serve as an initial guide and MUST be formalised through
legal sources and institutional documents.]`

---

## 4. Drafting principles required

`[Role assigned to the model; how far research may go beyond the local context;
linguistic conventions; working format; technology-neutrality constraints.]`

**Documents not to be used as a basis.** `[List of the documents held in
`CONTEXT/` for background purposes only. Without this list the model gives them
the same weight as the primary sources.]`

---

## 5. Substantive content to be turned into text

`[Decisions on the merits already taken, listed. It is the part specific to the
individual project and the model cannot infer it.]`

---

## 6. Roles

The assignment of roles MUST be declared even in small structures: the method
distributes execution between person and model, whereas responsibility cannot be
distributed.

| Role | Holder | Responsibility |
| --- | --- | --- |
| **Project lead** | `[…]` | Defining objectives and constraints, maintaining state and instructions, deciding on the merits. |
| **Drafter** | `[…]` | Building the context, running the production cycle, keeping the worklog. |
| **Validator** | `[…]` | Checking the result, having taken no part in the drafting. |
| **Release authority** | `[…]` | Authorising export to the final formats and entry into the official record. |

The separation between whoever drafts and whoever validates is the only
mandatory separation of roles. The model exercises no decision-making power in
any role.

---

## 7. Structure of the project

```
project/
├── PROJECT_BRIEF.md    this file: the mandate
├── README.md           the method and its reasons; not read at every session
├── CONTEXT/            reference documentation (input)
├── RELEASE/            final exported versions (output)
├── TOOLS/              interaction-capture script
└── REGISTERS/
    ├── INSTRUCTIONS.md   the operating rules: binding, always read
    ├── PROJECT.md        state of the project
    ├── WORKLOG.md        activities carried out, with checks and outcome
    └── CONVERSATION.md   requests to the model and its answers
```

**Hooking up to the tool.** The most widespread command-line tools read an
instruction file at start-up whose name varies from product to product. That file
MUST do nothing more than refer on to this document:

```markdown
At the start of every session read `PROJECT_BRIEF.md` in full, then
`REGISTERS/INSTRUCTIONS.md`, and keep to the latter throughout the work.
```

It is the only point of contact between the method and a specific product.
Adopting the method with a different tool means rewriting this referral and
nothing else.
