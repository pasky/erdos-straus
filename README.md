# Erdős–Straus campaign (Claude)

An AI-run research campaign on the **Erdős–Straus conjecture**: for every n ≥ 2, 4/n = 1/x + 1/y + 1/z has a solution in
positive integers. It ran from September to November 2026, with orchestrated Claude agents, cross-lab review by GPT
models, and advisory boards.

**ES is still open.** The campaign did not prove or disprove it. It produced the following.
* **Theorems near ES:**
  * the exceptional-set bound E(N) ≪ N·exp(−c(log N)^{3/4});
  * ES on infinite families beyond every finite Elsholtz–Tao covering (e.g. all 3·2^s + 1);
  * unconditional main terms ≍ log²p at every prime.
* **A precise map of why ES is hard:** every route ends at one divisor event at a single integer ("B2").
* **Weak-arithmetic models** in which ES fails.

All proofs have internal review only and are not externally refereed.

## Where to look
| you want | read |
|---|---|
| the current results, in ten minutes | **[`STATUS.md`](STATUS.md)** |
| the expert deep-dive: the reduction, barriers as theorems, a checklist for proof ideas, open problems | [`FRONTIER.md`](FRONTIER.md) |
| what happened when | [`WAVES.md`](WAVES.md), then [`STATUS_HISTORY.md`](STATUS_HISTORY.md) for earlier waves |
| the write-ups (LaTeX notes and their status) | [`paper/README.md`](paper/README.md) |
| rules for agents and contributors, including where new results go | [`AGENTS.md`](AGENTS.md) |
| orchestration directives, and the pause and resume state | [`OPERATIONS.md`](OPERATIONS.md) |

## Layout
* `*.md` at the root holds about 500 per-task research notes from waves up to z74; new notes go in `notes/zNN/`. Each note
  is the master for its own result, and `STATUS.md` and `FRONTIER.md` point into them.
* `paper/` holds the LaTeX write-ups. `reviews/` holds the hostile reviews and referee reports.
* `scripts/` holds the Python and C engines for the censuses and certificates. `data/` holds their outputs.
* `lean/ES/` holds Lean 4 formalisations (e.g. ES for all 3·2^s + 1).
* `sources/` holds archived literature. `BRAINSTORM/` and `logs/` hold raw material.

Python is run with `uv`, for example: `uv run --offline --no-project python scripts/divisor_shift_certificate.py`.
