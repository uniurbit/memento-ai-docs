# Operating instructions

> **This file is binding.** It must be read in full at the start of every
> session, before any material activity, and observed throughout the work.
>
> It contains prescriptions, not explanations: the reason for each rule is in
> `README.md`, which MUST NOT be read at every session. Whoever wants to
> understand a rule should consult the README; whoever has to apply it should
> keep to this file.
>
> The words **MUST**, **MUST NOT**, **SHOULD**, **MAY** in capitals have the
> single interpretation defined in `README.md`, §2.
>
> **Language.** These are the operating rules in English, the language of the
> root of the kit. The other languages are in `lang/`, each in a folder that
> mirrors this structure with the same file names. One language is chosen when
> the project is set up and `lang/` is removed (`README.md`, Technical
> appendix 5).

---

## 1. Scope and precedence

This file specifies **how the work is done**. `PROJECT_BRIEF.md` specifies
**what has to be produced**. `README.md` specifies **why the method is made this
way**.

Where prescriptions are incompatible with one another, the following order of
precedence applies:

1. An explicit request from the user in the current session.
2. `PROJECT_BRIEF.md` (mandate, perimeter, roles).
3. This file.
4. `README.md`.

**A conflict MUST NOT be resolved in silence.** Even when precedence is clear,
the divergence MUST be reported to the user before proceeding with the activity
concerned. If a request in the session contradicts the mandate, the model MUST
ask for confirmation and MUST NOT infer the intention.

---

## 2. Opening the session

The following steps MUST be carried out in the order given, before any material
activity.

1. Run `git status`. Unrecognised local changes MUST NOT be hidden, reverted or
   absorbed: they are to be reported.
2. **Check that the project holds one language only.** The `lang/` folder MUST
   NOT be present: its removal is prescribed when the repository is initialised
   (`README.md`, Technical appendix 5). If it is still there, the model MUST
   report it and MUST ask the user which language to keep before proceeding.
   Two copies of binding documents diverge without anyone noticing, and the one
   that is read is not necessarily the one that was updated.
3. If a remote repository exists, run `git fetch`. Only linear advances MUST be
   accepted. Any divergence MUST be reported and MUST NOT be resolved
   autonomously.
4. Read `PROJECT_BRIEF.md` in full.
5. Read this file in full.
6. Read `REGISTERS/PROJECT.md` in full.
7. Read the final portion of `REGISTERS/WORKLOG.md`, enough to cover the latest
   activities; search it for the entries relevant to the task requested.
8. Take note of the sources available in `CONTEXT/`: read its manifest where one
   exists, otherwise the list of files. Departures from the perimeter declared
   in the mandate MUST be reported. Individual sources are opened when the task
   requires it, not as a matter of routine.

`REGISTERS/CONVERSATION.md` MUST NOT be loaded into context. It is consulted
solely through targeted searches, when the original text of a request or of an
answer is needed.

`README.md` MUST NOT be loaded into context during ordinary work. It is
consulted through targeted searches when the reason for a rule is needed.

**Declaration of reading.** Once the sequence is complete, the model MUST
declare at the opening of its answer, in no more than four lines: the current
state of the project, the last activity recorded, the extent of the context
available, and any open question relevant to the task requested. The declaration
makes the reading verifiable.

---

## 3. The work

### 3.1 The six-phase process

The work is articulated in six phases. Only the sequence is prescribed here; the
reasons are in `README.md`.

| Phase | Subject | Concluded when |
| --- | --- | --- |
| **0 — Environment** | Technical set-up: installing the tool and the model | The tool starts and Git is available |
| **1 — Project start-up** | Repository, registers, roles, preliminary checks, mandate, sources, manifest | The mandate is filled in and the manifest covers the perimeter declared there |
| **2 — Production cycle** | Iterative drafting up to the candidate version | A complete reading brings no substantive change to light |
| **3 — External review** | Submission to people not involved in the drafting | The reviewers request no further changes |
| **4 — Release** | Export, accessibility check, formal adoption | The document is adopted by the appropriate act |
| **5 — Medium-term reviews** | Re-examination over time | Re-entry from Phase 1 when the picture has changed |

**The Phase 2 cycle.** The first draft (action **2.1**) is produced once only,
when the phase opens. Each subsequent turn carries out the following steps:

1. **Amending the documentation** (action **2.2**), in the two forms that
   alternate as needed and without a fixed order: **2.2.a prompting** — a
   request to the model on the basis of the mandate and the context; **2.2.b
   updating the context** — if the turn has exposed an insufficiency in the
   sources (§3.2).
2. **Human review** (action **2.3**) — the user annotates the document (§3.3).
   The model MUST commit the annotated state **before** carrying the annotations
   out, without being asked, and then carries them out in a clean version.
3. **Completeness analysis** (action **2.4**) — an explicit request to the model
   to check completeness and consistency against the whole corpus: missing
   references, supporting documentation needed, inconsistencies with the
   legislation in force. **It MUST be carried out after the human review and not
   before**, so that it bears on the text in the wording the person wanted.

The turn closes with the sequence in §4, which is performed at the end of each
action. Iteration resumes from step 1.

**Preservation of the annotated state.** The model MUST record in Git the state
annotated by the user before rewriting it: it is that commit which preserves the
human intervention. The operation falls to the model and MUST NOT wait for an
explicit request from the user. Carrying the annotations out produces the clean
version in the same file; the two versions are two successive commits and both
can be retrieved from the history. A copy of the document under a different name
MUST NOT be created: it would duplicate what Git already preserves.

**Candidate versions.** The version that leaves the cycle to be submitted for
external review is a *release candidate* and MUST be numbered progressively:
RC 1, RC 2, …, RC *n*. A draft internal to the cycle is NOT a release candidate
and receives no number. If the external review requests changes, the document
re-enters Phase 2 and leaves it as the next RC. If it requests none, the RC
under examination proceeds to Phase 4.

**Change of phase.** Every passage from one phase to the next MUST be recorded
with a worklog entry and closed with a commit.

### 3.2 Folders and files

- The content of the sources in `CONTEXT/` MUST NOT be modified.
- The composition of `CONTEXT/` MAY be modified — addition, removal,
  reclassification — where there is a reason. The reason MUST be noted in the
  manifest and in the worklog.
- The source manifest MUST be updated as each source is acquired, never once the
  work is finished. Each record carries: short identifier, title, provenance,
  date of acquisition, name of the local copy, reason for the acquisition.
- A source obtained indirectly or by substitution MUST be noted as such in the
  manifest.
- `RELEASE/` MUST NOT be modified manually after the export.
- `TOOLS/` holds the interaction-capture script (§4.1). It MUST NOT be modified
  during the work, except to adapt it to the tool in use, which MUST be recorded
  in the worklog.
- The drafts reside in the project root or in a dedicated folder, in an open
  text format.

### 3.3 User annotations in the files

The user does not correct the text produced: the user **annotates** it.
Annotations are instructions to be carried out, inserted into the body of the
file.

**Recognition.** An annotation is delimited by three opening and three closing
angle brackets, and refers to the passage immediately preceding it:

```text
The mailbox is deactivated two years after the end of the employment
relationship.<<<specify that the period runs from formal termination and
not from the last access; add the reference to art. 12>>>
```

**Precedence over reading.** When the user asks for a file to be taken charge
of, the annotations MUST be identified **before** any analysis, validation or
reformatting of the host file. They are instructions, not content.

**Prior recording.** Before carrying out any annotation, the model MUST commit
the file in the state in which it received it, with a message declaring the
presence of human annotations still to be carried out — for example
`docs(regulation): record the user's annotations on section 3`. The operation
precedes any modification and MUST NOT be omitted even when the user asks
directly for the annotations to be carried out.

**Execution.** For each annotation:

1. Carry out the instruction it contains. The annotation describes an
   intervention; it MUST NOT be transcribed into the text.
2. Verify the outcome.
3. Remove from the file the annotation carried out, together with the text it
   replaces where so provided.

**Annotations not to be removed.** Annotations that are incomplete, ambiguous,
incompatible with other instructions, not carried out, or whose execution
failed, MUST NOT be removed. They stay in the file and the circumstance MUST be
reported to the user, with the reason.

**Non-compliant delimiters.** An annotation delimited by a number of characters
other than three is not compliant. If its content is unambiguous it MAY be
carried out, but the anomaly MUST be reported. If its content is ambiguous, it
MUST NOT be carried out.

**Archiving.** If the project keeps the interaction archive, the annotation MUST
be recorded there verbatim **before** being removed from the source, with an
indication of the file and line it came from. The delimiters MUST be encoded in
such a way that they are not carried out again on a later reading of the
archive.

**Examples.** Occurrences of the delimiters inside code blocks are not
annotations and MUST NOT be carried out.

**Contextual nature.** An annotation holds for the task in hand. It MUST NOT be
recorded as a general rule in this file, nor as an accomplished state in
`PROJECT.md`, unless its content expressly so provides.

### 3.4 Drafting rules

**Unavailable data.** The absence MUST be declared; plausible content MUST NOT
be produced. The document carries an explicit placeholder stating what is
missing and why. The list of items to be verified accompanies the draft as a
section of its own, with one entry per gap.

**Personal data.** Requests MUST include only the personal data necessary to
produce the document. Where a document matters for its structure or its
operative content and not for the names it contains, only the useful part MUST
be handed over.

**Verifiability.** Every statement in the document produced MUST be traceable to
the source that supports it by someone who took no part in the work. Statements
without a source MUST be flagged as such.

**Distinguishing the modes of truth.** A verified fact, an inference and a
forecast MUST NOT be written in the same way. What has not been verified MUST
NOT be noted as "verified", nor what has not been published as "published".

**Decisions.** The model proposes and revises. Decisions on the merits and the
final validation fall to the person. The statement of reasons for an
administrative measure MUST NOT be produced by the model.

**Clarifications.** Where there is ambiguity the model MUST put a question
rather than resolve it autonomously.

---

## 4. Closing the turn

The following steps MUST be carried out at the end of every interaction that has
produced a material change, in the order given.

1. **Interaction archive** — §4.1.
2. **Worklog**, if the activity is significant — §4.2.
3. **Project state**, if the picture has changed — §4.3.
4. **Commit** — §4.4.

An interaction that produces no material change requires none of the four steps,
except the interaction archive, which is independent of the outcome.

### 4.1 Interaction archive

`CONVERSATION.md` preserves the two ends of each turn — the text of the request
and the final answer — **verbatim**. Internal reasoning, tool calls, command
output and technical logs MUST NOT be recorded there.

It is fed in **one only** of two ways, which are mutually exclusive. The way
adopted MUST be noted in `PROJECT.md`.

#### Case A — capture from the environment

A script hooked to the tool records both ends of every turn. It is the way to
prefer wherever it is practicable: it is deterministic, it copies the text
without reworking it, and it consumes no processing resources.

The template supplies the implementation: `TOOLS/record_interaction.py`.
It requires Python 3 and the standard library alone. It is to be hooked to the
two events the tool exposes — the sending of the request and the completion of
the answer — following the configuration syntax of the product in use. An
example hook, in generic form:

```
event "request sent"        → python3 TOOLS/record_interaction.py
event "answer completed"    → python3 TOOLS/record_interaction.py
```

The script recognises by itself which of the two events invoked it. If the tool
does not declare the type of event, it is to be passed as the first argument
(`request` or `answer`). Adapting it to a different tool requires modifying only
the `ADAPTER` section at the head of the script.

**Coverage MUST be complete.** A configuration that intercepts only one event is
**not compliant**: it produces an archive that preserves half of every turn
without declaring it. It is to be completed, or switched off by moving to
Case B. Case A and Case B MUST NOT coexist: the result would be duplicate
records and capture modes mixed in the same archive.

**Enabling is a human act.** The model MUST NOT attempt to enable the hook
itself, nor modify the tool's configuration in order to activate it: the subject
that would be recorded does not authorise its own recorder. The model MAY
prepare the declaration and MUST tell the user that the enabling remains theirs
to do. The procedure is in `README.md`, Technical appendix 2.

**Verification on adoption.** At the first session after the hook is set up it
MUST be verified that the archive holds both ends of the turn. The model MUST
NOT presume Case A from the mere presence of a declaration in the configuration:
declaration and enabling are distinct states. If either end is missing, the
preceding paragraph applies.

In Case A the model **MUST NOT write** in `CONVERSATION.md`.

#### Case B — capture by the model

When the tool does not expose the necessary events, or does not expose both, the
recording falls to the model, which appends both ends at the end of every turn.

Execution prescriptions, all binding:

- Writing is done with **a single append operation per turn**, by means of a
  shell command that writes at the end of the file. An editing tool that
  requires the file to be read first MUST NOT be used.
- The file MUST NOT be loaded into context, either before or after the writing.
- The outcome of the writing MUST NOT be verified by rereading the file.
- Every record MUST carry a turn marker, so that a re-execution produces no
  duplicates.
- The text MUST NOT be summarised, reformulated, abbreviated or normalised. If a
  portion cannot be reproduced verbatim, it MUST be declared omitted, with an
  indication of its extent and of the reason; it MUST NOT be replaced by a
  summary. An undeclared summary makes the archive useless for the purpose it
  exists for.

**Limitation of Case B, to be declared in `PROJECT.md`.** The subject that
records coincides with the subject recorded, and the completeness of the archive
depends on the model not omitting the writing. Declaring the mode in each record
makes the circumstance inspectable by whoever rereads the archive.

#### Format of the record

It is **identical in both cases**, save for the declaration of the capture mode.
An archive has to stay readable even when a project moves from one case to the
other.

```markdown
<!-- interaction:<session>:<turn>:request -->
## Request — 2026-08-26T17:04:11+02:00 — capture: environment

verbatim text of the request

<!-- interaction:<session>:<turn>:answer -->
## Answer — 2026-08-26T17:06:02+02:00 — capture: environment

verbatim text of the final answer
```

In Case B the declaration is `capture: model`. The file opens with the heading
`# Conversation`, which the first write creates if absent.

The markers and labels of the record are in English in both language versions of
the kit: the capture script is one and the same, and those strings are
machine-readable scaffolding, not prose. The text recorded stays verbatim in the
language in which it was written.

### 4.2 Worklog

One entry per **significant activity**: a document has advanced, a decision has
been taken, a check has changed how far the result can be relied on, a problem
has emerged. An entry MUST NOT be produced for each command executed.

`WORKLOG.md` is **append-only**: entries are added at the end and MUST NOT be
rewritten. An error is corrected by adding an entry that rectifies it.

Date and time MUST be taken from the system clock (`date -Iseconds`) and MUST
NOT be reconstructed from memory.

The updating of the worklog MUST NOT be noted in the worklog.

```markdown
## YYYY-MM-DDTHH:MM:SS+TZ — Short title

**Purpose:** the result that was sought.

**Activity and method:**
- significant action and the way it was carried out;
- relevant implementation decision;
- failed attempt that changed the approach.

**Artefacts affected:**
- `path/file.ext` — type of change.

**Checks:**
- check actually performed — outcome observed;
- limitation of the check, if any.

**Decisions and notes:**
- lasting decision, risk, assumption, information for the future.

**State:** completed | partial | blocked | cancelled.

**Next step:** concrete remaining action, if any.
```

### 4.3 Project state

`PROJECT.md` is edited in place and MUST be updated **only** when scope,
structure, state of completion, structural decisions, risks or direction change.
It MUST NOT be used as a second worklog.

Sections: summary, scope (included and excluded), current structure, main
artefacts, overall state in a table, structural decisions, risks and open
questions, direction.

In the state table the **degree of completion** and the **evidence** supporting
it MUST be distinguished: implemented, planned, hypothesised, and on the
strength of which finding.

A decision that has been revoked MUST NOT be deleted: it MUST be recorded as
revoked, with the date.

### 4.4 Commit

The commit closes the iteration. The model judges the moment and performs it: at
each turn of the production cycle and at each change of phase.

Before every commit:

- Check that the index holds no files extraneous to the activity in hand.
- Check that no keys, credentials, unnecessary personal data or large generated
  files are being versioned.
- Preserve concurrent changes extraneous to the activity.

Convention: `type(scope): description`, short, imperative and semantically
consistent with the worklog entry. Types: `feat`, `fix`, `docs`, `refactor`,
`chore`, `meta`, `checkpoint`.

The message MUST make **human intervention distinguishable from the model's**:
commits that carry out the user's annotations say so.

```text
docs(regulation): carry out the user's annotations on section 3
docs(regulation): fill the gap on extensions found by the analysis
```

The message says **what** changed. The **why** goes in the worklog.

---

## 5. Git — permanent rules

- Force push MUST NOT be performed.
- History already shared MUST NOT be rewritten.
- Remote branches or tags MUST NOT be deleted without explicit authorisation.
- Partial states to be preserved without publishing them as final MUST be placed
  on checkpoint branches.
- When there is more than one drafter, the main branch MUST NOT be modified
  directly: each works on a branch of their own and merges once the cycle is
  concluded.
- A merge conflict on a draft is a decision on the merits and MUST NOT be
  resolved by the model.
- Annotated tags and semantic versioning are used only for deliberate releases.
- Keys, credentials and non-versionable data stay outside the repository.

---

## 6. Quick reference

**On opening:** `git status` → check that `lang/` is not present → `git fetch`
if there is a remote → `PROJECT_BRIEF.md` → this
file → `PROJECT.md` → the end of `WORKLOG.md` → manifest of `CONTEXT/` →
declaration of reading in four lines.

**During:** carry out the phases in order · completeness analysis after the
human review · commit the annotated state before carrying the annotations out
(the model's own responsibility) · do not modify the sources · note every change
of context in the manifest and the worklog · carry out the annotations before
any other analysis · declare the gaps instead of filling them · report conflicts
instead of resolving them · ask instead of inferring.

**On closing:** interaction archive, if the project is in Case B of §4.1 →
worklog if significant → state if the picture has changed → commit.

**Never:** load `CONVERSATION.md` into context · summarise a verbatim record ·
rewrite the worklog · decide on the merits · produce the statement of reasons
for an administrative measure · resolve a conflict in silence.
