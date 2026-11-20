# OPERATIONS — standing directives and how the campaign is run (read this first if you are the orchestrator)

**ES is OPEN.** The goal of the campaign is a proof (or disproof) of the Erdős–Straus conjecture. Everything else is
instrumental.

**Where results go (since 2026-11-19): `AGENTS.md` §2–§4.** Each wave export writes one `WAVES.md` entry and applies
the STATUS gate to `STATUS.md`. FRONTIER edits are made in place, with no top-of-file wave blocks. The older brief
`z52bbriefs/z5N_summary.md` ("edit FRONTIER, mark additions (zNN)") is superseded where it conflicts with this.

## Standing user directives
* **Papers are the campaign's own artifacts** (user, 2026-11-05). `paper/*.tex` exist for continuity and rigour, not as
  primary output. Edit them as fit — fix citations, priority wording, errors, scope — without asking. They are *not*
  the goal; finding ES is. (Posting/submitting anything externally still needs the user; do not touch PR
  plasma-ai/erdos#65 — merged upstream 2026-11-10 20:12 UTC, per GitHub API, z71 LIT.)
* Breadth and boldness; barriers are information about what a new idea must beat. False negatives are the costly error.
* Organised, concise, honest reports; be blunt when nothing turned up. The user likes "tryhard" lanes alongside
  structured ones.
* Labels on every claim: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal
  review only; nothing is externally refereed.

## Provider failures (user, 2026-11-08)
* **Any auth / quota / provider error on a model (e.g. "authentication token has expired", "usage limit reached") must
  be flagged to the user IMMEDIATELY, in its own message, before working around it.** Do not silently substitute
  another model and mention it only in the end-of-wave report.

## Wave mechanics (z53–z58)
* Briefs: `/home/pasky/projects/math/z52bbriefs/` — `z53_depth.md` (structured lane), `z55_tryhard.md` (unprimed
  "just prove it"), `xreview_z5N.md` (cross-model hostile review), `z5N_lanes.md` (lane file), `z58_summary.md`
  (export writer brief).
* Models: Opus `anthropic/claude-opus-5-5:high` (depth), Fable `anthropic/claude-fable-5-1:high` (unprimed twins; since z69 Fable 5.2 `anthropic/claude-fable-5-2:high` = pi "best" mode, used for tryhard + ideation lanes),
  Astra `openai-codex/gpt-6-astra:high` (every cross-review and FRONTIER consistency review). No OpenRouter.
* Mandatory falsifier table for every lane (since z58): F1 odd squares, F2 C-even / numerator-8 sub-line, F3 composites,
  F4 known zeros — data in `data/z58/screens/`.
* Flow: lanes → internal hostile review → Astra cross-review `data/z5N/xreview/REVIEW_<LANE>.md` → lane applies fixes and
  merges → export (WAVES entry + gated STATUS/FRONTIER edits per `AGENTS.md` → Astra consistency review → apply) → report.
* Resource rules: `timeout` ≤ 1800, `ulimit -v` ≤ 6000000 (Lean: 16G cgroup); ≤ 2 compute processes per lane.
* Quota footprint (z58): 16 Opus/Fable lanes + export ≈ 11 % of the Anthropic week.

## Spending rule after z60 (user, agreed 2026-11-05)
Waves z58–z60 re-encoded (★) in many coordinates; every encoding ended at B2. **Do not launch further re-encoding
waves.** Spend remaining quota only on a *genuinely new* mechanism for forcing a single tied divisor event at one prime
(something not reducible to counting / equidistribution / local-global / modular-proxy arguments already scoped in
FRONTIER §3, §6). Current cleanest targets: (MS-U₇) and (MS⁺₁₀₅) (`Z60_SUMMARY.md` §5).

## Cross-model reviews
**None owed for promoted items.** Every assigned Opus review of z72–z74 (Astra) is done (2026-11-19/20; 12 reviews in `data/z74/xreview/REVIEW_*_OPUS.md`), and every z75 headline/record lane (Lanes 1, 2, 4, 5, 6) passed independent Claude Opus cross-review (ACCEPT or ACCEPT-WITH-FIXES, fixes applied, Lean independently compiled; reviews in `notes/z75/*REVIEW*`, `data/z75/ie1/`, `data/z75/obstruct/review.md`, `data/z75/push2/review.md`, `data/z75/REVIEW_ANALYTIC*_OPUS.md`, `data/z75/thin_cyclo/REVIEW_OPUS.md`). Lane 3 (`PROOF_WILD*`, scoped barriers only) was self-checked with replay scripts. Rule: the cross-review is always by the other lab (Astra reviews Claude work; Opus `anthropic/claude-opus-5-5:high` reviews Astra work). Done (Astra retro review, fixes applied): `Z64_UNPROV.md`, `Z65_LOGIC2.md`, `Z65_LIFT.md`, `Z64_EQUIV.md`, `Z64_SDEEP.md`, `Z64_SDEEPF.md` (reviews in `data/z6{4,5}/xreview/REVIEW_*_ASTRA.md`).

## Campaign status (2026-11-10): PAUSED after z70 (user: "wrap it up"); resumes per new model (see Cadence below)
Waves z67–z70 (FRONTIER blocks z67–z70) found **no mechanism**; every lane ended at the B2 atom (one tied divisor event
at a fixed prime), at a scoped no-go, or at a bounded null. All lanes Astra-cross-reviewed and merged; no reviews owed.
* Fable 5.2 (z69, informed + independent ideation): no new mechanism; the independent lane's ideas were mostly already
  in the campaign (4 narrow twists, since tested in `Z69_TWIST.md` / `Z70_*`). Its "nothing new" claim was rejected by
  Astra, so this is evidence of coverage, not proof of saturation.
* Process lessons: tryhard/ideation lanes stop well short of their time box (state a minimum duration in the brief);
  `agent-wait-any` may return a stale `waiting_user` right after a send — sleep ~30 s and re-check; Anthropic ToS
  classifier ("reverse engineering / duplicating model outputs") falsely blocked a Fable 5.2 lane twice while it read
  many AI-written memos — a plain "please continue" cleared it.
* **Open, concrete, cheap (if resuming):** `Z70_CLASS.md` open list (Rédei 4-rank, small-split-prime
  orbits from principal seeds, fixed-n solution-graph moves); conjecture (S) (now reduced to the 24 square classes mod 840);
  U₇ (Conjectures B, C in `Z68_U7F.md`); (MS⁺₁₀₅) (certified to 10¹¹); full prime QR + universal TS; `IE₁`/`IΔ₀`;
  `θ > 3/4` on `E(N)`. (The three `REVIEW_GEN.md` tests, BCM+4-squares, and `15·2^s+1`/`4^s+{33,273,297}` closed in z75.)
* **z71 literature refresh (2026-11-10, `Z71_LIT.md`; orchestrator-reviewed, no Astra review):** arXiv math.NT
  2026-09-28 … 11-10 screened in full; no new mechanism. New ES paper Dahan arXiv:2611.08717 (5/7 < 3/4 by the same
  architecture as the 3/4 note; "1 − o(1)" only on a structured subset; pointwise part ends at an open hypothesis =
  B2 with a cap). Dahan I has a v2 with shifted numbering (repo cites v1). Resume condition unchanged.
* **Cadence (user, 2026-11-19).** The campaign resumes when a new frontier model arrives: each new model gets a burst of
  waves, and the campaign is idle in between. "Paused" means waiting for the next model. It is not a decision to stop.
* **z72–z74 (2026-11-19)** was the GPT Astra burst: phase criteria, weak-arithmetic PID and BCM models, and the
  formula-menu no-go (`WAVES.md`). Its notes then had Opus cross-reviews. Four side agents covered the headline items and eight more lanes covered the
  rest. Every verdict was ACCEPT or ACCEPT-WITH-FIXES. The reviewers applied the note-level fixes,
  since the author was not running, and tagged each edit "(z74 Opus xreview fix)".
* **z75 (2026-11-20, GPT-6.2 Astra `deep` 6-lane burst orchestrated by Claude Fable `best`)** delivered major Opus-reviewed
  results across all three pillars (`WAVES.md`): `IOpen + Bézout + BCM + Lagrange ⊬ ES` (`BCM4_PUSH2.md`), full internal
  prime QR + Dirichlet + Lag + `L(D)` PID (`BCM4_QR.md`, `BCM4_PUSH2.md`), `L(D)` and variable-radicand Pell-window repair
  (`IE1_ES.md`, `IE1_PUSH2.md`), Lean-verified `ES(15·2^s+1)` plus finite certificates (not Lean) for `4^s+{33,273,297}`,
  sharp 24-class `(S)` and closure of the 3 frozen `REVIEW_GEN` tests (`CONJS_GEN.md`, `THIN_CYCLO.md`), effective
  subexponential `e*(n)` + 2/3 `(★)/U₇` prime lower tails (`ANALYTIC_BREAK.md`, `ANALYTIC_PUSH2.md`), open-surface Brauer
  exponent dichotomy + cubic sterile fibres + trillion-scale `R₈` (`1,511,088,831,001`) and extended censuses
  (`DISPROOF_OBSTRUCT.md`, `DISPROOF_PUSH2.md`; §6 full ES counts unreviewed by Opus), plus scoped proof barriers
  (`PROOF_WILD*.md`). Remaining open fronts: ES, `IE₁`/`IΔ₀`, QR + universal TS, `θ > 3/4` on `E(N)`, `e*(n)` below `L_R[1/2]`.
