# OPERATIONS — standing directives and how the campaign is run (read this first if you are the orchestrator)

**ES is OPEN.** The goal of the campaign is a proof (or disproof) of the Erdős–Straus conjecture. Everything else is
instrumental.

## Standing user directives
* **Papers are the campaign's own artifacts** (user, 2026-11-05). `paper/*.tex` exist for continuity and rigour, not as
  primary output. Edit them as fit — fix citations, priority wording, errors, scope — without asking. They are *not*
  the goal; finding ES is. (Posting/submitting anything externally still needs the user; do not touch PR
  plasma-ai/erdos#65.)
* Breadth and boldness; barriers are information about what a new idea must beat. False negatives are the costly error.
* Organised, concise, honest reports; be blunt when nothing turned up. The user likes "tryhard" lanes alongside
  structured ones.
* Labels on every claim: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal
  review only; nothing is externally refereed.

## Wave mechanics (z53–z58)
* Briefs: `/home/pasky/projects/math/z52bbriefs/` — `z53_depth.md` (structured lane), `z55_tryhard.md` (unprimed
  "just prove it"), `xreview_z5N.md` (cross-model hostile review), `z5N_lanes.md` (lane file), `z58_summary.md`
  (export writer brief).
* Models: Opus `anthropic/claude-opus-5-5:high` (depth), Fable `anthropic/claude-fable-5-1:high` (unprimed twins),
  Astra `openai-codex/gpt-6-astra:high` (every cross-review and FRONTIER consistency review). No OpenRouter.
* Mandatory falsifier table for every lane (since z58): F1 odd squares, F2 C-even / numerator-8 sub-line, F3 composites,
  F4 known zeros — data in `data/z58/screens/`.
* Flow: lanes → internal hostile review → Astra cross-review `data/z5N/xreview/REVIEW_<LANE>.md` → lane applies fixes and
  merges → export (summary writer → Astra FRONTIER consistency review → apply) → report.
* Resource rules: `timeout` ≤ 1800, `ulimit -v` ≤ 6000000 (Lean: 16G cgroup); ≤ 2 compute processes per lane.
* Quota footprint (z58): 16 Opus/Fable lanes + export ≈ 11 % of the Anthropic week.
