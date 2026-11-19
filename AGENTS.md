# AGENTS.md — how to work in this repository

**The Erdős–Straus conjecture (ES) is OPEN.** Never write or imply otherwise. Everything here has internal review only
and is not externally refereed. Do not post, submit or open PRs externally without the user.

## 1. Read first, in this order
0. If you are the orchestrator, read **`OPERATIONS.md`** first: user directives, models, quota, pause state, and the
   resume condition.
1. **`STATUS.md`**, the master summary of current results. Ten minutes.
2. **`FRONTIER.md`**: the one-paragraph summary, then §2 (the reduction), §3 (the barrier map), §4 (the screening
   checklist) and §7 (open sub-problems). Run the §4 checklist on any idea **before** working on it.
3. The source notes cited for whatever you work on. **When a summary and its source disagree, the source wins.**

## 2. Master files and how results propagate
There is exactly one master for each kind of information. Do not restate it elsewhere; point to it instead.

| information | master | notes |
|---|---|---|
| the current best results, targets and refutations | `STATUS.md` | curated, at most 250 lines, gated (§3) |
| what happened in each wave | `WAVES.md` | at most 12 lines per wave, newest first |
| barriers, records, checklist, dead ends, open problems, with exact scopes | `FRONTIER.md` | edited in place (§4) |
| the full statement and proof of any result | its note | one note per task |
| the state of the papers | `paper/README.md` | |
| process and orchestration | `OPERATIONS.md`, this file | |

**Frozen, do not append:** `DISCOVERIES.md` (ledger frozen at (J)110), `STATUS_HISTORY.md`, `CAMPAIGN_SUMMARY.md` and
`Z53_SUMMARY.md`…`Z60_SUMMARY.md`. Old notes can receive clearly marked errata (`> **Erratum (zNN):** …`) and nothing else.

**The pipeline.** Every result goes note → `WAVES.md` line → gated promotion into `STATUS.md` and/or `FRONTIER.md`.
* **Lane or sub-agents** write only their note, plus scripts and data. They **do not edit** the master files `STATUS.md`,
  `WAVES.md` and `FRONTIER.md`. Instead they put a proposed triage class and STATUS delta in their note's §0 (below).
* **The orchestrator** applies the master-file edits at wave export, in one commit. In a single-agent session you are the
  orchestrator, so do the export before you finish.
* **Errors are the exception.** A refutation, retraction, proof gap, withdrawn hypothesis or label downgrade of anything
  quoted in a master file is fixed in **every** master file (§5) immediately, by whoever finds it, in the same commit as
  the note change. The evidence is a replayable certificate or a written gap analysis in the note.

**Note format.** New notes go in `notes/zNN/NAME.md`; scripts go in `scripts/` and data in `data/zNN/`. Old notes stay at
the repository root, because hundreds of pointers depend on their paths. Every note starts with a §0 block:
```
Result: <one sentence>            Label: PROVED (rel. …) | CONDITIONAL on … | CERTIFIED | EVIDENCE | CONJECTURE | Assessment
Scope: <exactly what is and is not claimed>
Review: <none | internal hostile (file) | cross-model (file)>
Triage: HEADLINE | RECORD | REFUTATION | TARGET | BARRIER-BROAD | BARRIER-SCOPED | METHOD-CX | NULL | DATA
STATUS delta: none | <proposed replacement text for one STATUS row>
```

## 3. The STATUS gate: keeping negative results from drowning the picture
Most of what this campaign produces is scoped no-gos ("method class X cannot do it") and nulls ("this encoding ends at
B2 again"). They are worth recording, but they describe methods, not ES. **Count them and compress them by root cause.
Do not list them in STATUS.**

| triage class | goes to | condition |
|---|---|---|
| **HEADLINE / RECORD**: a new theorem about ES or a listed relaxation, or an improved bound | `STATUS.md` §1. **Replace** the superseded row; never add a second row for the same quantity | at least one independent hostile review (two for a claimed improvement of a published record); priority checked |
| **REFUTATION / correction** of anything in STATUS or FRONTIER | `STATUS.md` §4, and fix the original row **now** (§2, "Errors") | replayable certificate or written gap analysis |
| **TARGET**: a new or changed open target | `STATUS.md` §2, kept to at most 6 items; adding one means demoting one | the statement passes the FRONTIER §4 falsifier screens |
| **BARRIER-BROAD**: rules out a class of proofs not already excluded by FRONTIER §3/§4 | a FRONTIER §3 entry plus a §4 checklist line. STATUS changes only if §0's "where everything ends" paragraph changes | exact scope stated; reviewed |
| **BARRIER-SCOPED / METHOD-CX**: a no-go for one construction, or a counterexample to a proposed method | one line in FRONTIER §6. **Merge** it into an existing line if it has the same root cause | |
| **NULL / DATA**: "ends at B2", a re-encoding, a null search, a census | the `WAVES.md` line only. A census reaches STATUS §1F only if it extends a listed census or finds a new zero | |

**The test for STATUS:** would a strong number theorist who reads *only* `STATUS.md` be misled, or miss something
important, without this item? If not, it does not go in.

**Caps:**
* STATUS: at most 250 lines in total, and at most 6 lines per §1 item.
* WAVES: at most 12 lines per entry, excluding the heading.
* FRONTIER §6: one line per dead end.

When a cap would be exceeded, compress or merge older items. Do not raise a cap without the user.

**Labels** (as in `FRONTIER.md`): PROVED (possibly *rel.* named published theorems), CONDITIONAL (on what), CERTIFIED (an
exact finite computation; state the engine and the independent-check coverage), EVIDENCE, CONJECTURE, Assessment. Put a
label and a file pointer on every claim, in every master file.

## 4. Editing `FRONTIER.md`
* Edit the relevant section in place. If an update supersedes base text, **rewrite the base text**; do not stack another
  "(zNN)" paragraph under it. Tag the changed sentence with "(zNN)" and the source file.
* Never add wave blocks at the top of the file. Wave news goes to `WAVES.md`.
* After an export, a cross-model consistency review of the changed FRONTIER passages is the norm (see `OPERATIONS.md`).
  If none was possible, say so in the WAVES `R` line.

## 5. Consistency duty
When the label, scope or status of a result changes, every master file that quotes it must follow.
* **Corrections and downgrades** go immediately, in the same commit as the note change, by whoever makes them (§2,
  "Errors").
* **Upgrades** (e.g. EVIDENCE → PROVED) go through the next wave export, after review.

To find the quotes:
```
git grep -n '<NOTE_NAME>' -- README.md STATUS.md WAVES.md FRONTIER.md paper/README.md OPERATIONS.md
```
Do the same for refuted conjectures (grep their names).

## 6. Practicalities
* Python: always `uv` (for example `uv run --offline --no-project python scripts/foo.py`). C engines live in `scripts/*.c`.
* Resources: `timeout` ≤ 1800 s, `ulimit -v` ≤ 6000000, and at most 2 compute processes per lane. Plan memory before
  running large censuses.
* Lean: `cd lean/ES && systemd-run --user --scope -p MemoryMax=16G timeout 1800 sh -c 'lake exe cache get && lake build'`. Use
  the cgroup memory cap, not `ulimit -v`, which breaks Lean (`LEAN_Z1546.md`). Do not use `sorry` or `native_decide` in
  claimed theorems.
* Commit each finished change with a clear message. Stage files explicitly; do not `git add -A` (the tree contains large
  data and unrelated work).
* Flag any provider auth or quota error to the user immediately (`OPERATIONS.md`).
