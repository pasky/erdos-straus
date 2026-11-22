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
**Owed (z81):** none owed for promoted items. Every assigned Opus review of z72–z74 (Astra) is done (2026-11-19/20; 12 reviews in `data/z74/xreview/REVIEW_*_OPUS.md`), every z75 headline/record lane (Lanes 1, 2, 4 excl. §6 full ES counts, 5, 6) passed independent Claude Opus cross-review, and **all z76 (6), z77 (5), z78 (6), z79 (7), z80 (7), and z81 (8) lanes** passed independent cross-lab review (ACCEPT or ACCEPT-WITH-FIXES, all fixes applied; z81 has **26 cross-lab reviews** in `data/z81/xreview/`: 24 Opus reviews of the 7 Astra lanes, independent second hostile Opus review `REVIEW_CAP_RECORDS_OPUS2.md` of `CAP_ZERO` I, V and `SPECIFIC_CLASS` C1, and Astra review `REVIEW_LIT_OPUS_ASTRA.md` of Claude Opus `LIT.md`). **z80 second independent review:** QB `log(1+e*)≪_ε U^ε` (`notes/z80/BEYOND_34.md` §§10–11; `REVIEW_BEYOND_34_QB_OPUS2.md`, orchestrator-commissioned, ACCEPT-WITH-FIXES, applied); its §12 refinement QR (14) and the Montgomery estimate were reviewed separately in `REVIEW_BEYOND_34_R2_OPUS.md`; `R17` z80 R1 and R2 each have a full Opus replay with independent decisive counts; `R_BELOW_619` has six Opus reviews. **z78–z79 second independent reviews:** `46/145` (`REVIEW_ANALYTIC_WILD_46145_OPUS2.md`, ACCEPT) and z79's **`6801/21497`** (`25/79`, `999/3157`, `M^{1−5θ}`; `REVIEW_ANALYTIC_PUSH_6801_OPUS2.md`, ACCEPT) each have two independent Opus reviews; `R17` z79 R1 and R2 have two full Opus replays including an independent C/Python P-endpoint search with different cutoffs. Rule: the cross-review is always by the other lab (Astra reviews Claude work; Opus `anthropic/claude-opus-5-5:high` reviews Astra work). Done (Astra retro review, fixes applied): `Z64_UNPROV.md`, `Z65_LOGIC2.md`, `Z65_LIFT.md`, `Z64_EQUIV.md`, `Z64_SDEEP.md`, `Z64_SDEEPF.md` (reviews in `data/z6{4,5}/xreview/REVIEW_*_ASTRA.md`).

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
  orbits from principal seeds, fixed-n solution-graph moves); conjecture (S) (reduced to the 24 square classes mod 840);
  U₇ (Conjecture B and six-cofactor C open, CERTIFIED to 111·10⁹ on primes `1 mod 8`; 3-exception clause refuted at `2,238,327,841` and `4,367,159,449`, `notes/z81/S_U7_FORCE.md`); (MS⁺₁₀₅) (CERTIFIED to 3·10¹¹, coverage: `STATUS.md` §1F); `IE₁`/`IE₁⁻`/`IΔ₀` (no nonstandard external PID
  satisfies `IE₁`, if ES holds in ℕ no nonstandard external PID is an `IE₁⁻` ES countermodel, and `IE₁⁻` proves Bézout, `(Sep)`/unique maximal, and unital domain-landing exclusion with `0≠ker e⊆2R∩3R`; z81 `T*` has full supplied-unit PW, factorial strings over every non-initial PA subring, Bézout, (Sep), Lag, Dirichlet and ¬ES(P), but fails `L(Div)`; the separate `T_g` has unary Boolean affine-divisibility least search, full `L(Div)` unknown there; PROVED `notes/z81/FAREY_PROOF.md`). `r=17` Mordell point: PROVED positive sterile measure on the r-generic line at every prime `r≥83` and at `r=73`; 15 primes `17≤r≤79`, `r≠73`, remain, next charge P₁₃ at 79. CERTIFIED `5,1/5` survive P depth 16, Q odd level 39 (`notes/z80/R17_CRUSH.md`, `R17_WALK.md`). Proth core for all h; all exponents for `m>30` (PROVED ES off `P₉|s`, `P₉=497,943,285,840`, for `m≥11, m≡11 mod τ`; on a selected infinite subset good words have relative density one even inside that class, `notes/z80/PROTH_CORE.md` §6).
  Full Farey / prime short vectors / variable-discriminant reduction for an `IE₁⁻` candidate (for `n≥0`, `Th(n)` iff `n∈C` in z81's power-cut Dirichlet-line models, and power cuts about infinite generators in discretely ordered Bézout rings with integer division never carry BCM, `notes/z81/FAREY_PROOF.md` §§8,14–15); `L(Div)` with BCM+TS; `θ>3/4` on `E(N)`; breaking `6/19` on `R(n)` toward `3/10`; bounded cap `e*=O(1)` (now prime-power root at all three z80 QR rates, cap-1 saving `4/5` and prime-or-1-root `(3/4,1/4)`, `STATUS.md` §1B); unconditional normal order `R(p)∼M₀(p)` (Assessment: equilateral sieve-weighted error budget `X^{19/12+o(1)}` vs power saving `O(X^{1−δ})` needed on interior boxes, `notes/z80/R_BELOW_619.md` §5.6); unconditional `g≥11` i.o. (z81 `GAP_ES.md` §11 proves `g=11` on `≍ X/log²X` primes CONDITIONAL on prime AP level `0.9908` (EH suffices); growing tail, `L=log X`, `#{p≤X:g(p)>log X}≪X exp(−c L^{0.665}/(log L)^{3/2})`, §8); CONJECTURE `g(p)=O(log p)` on 𝔐, CERTIFIED max 127 on 𝔐-primes to 5·10¹² (`notes/z80/EXTREME.md` §§7,12).
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
  (`PROOF_WILD*.md`).
* **z76 (2026-11-20, GPT-6.2 Astra `deep` 6-lane burst orchestrated by Claude Fable `best`, all 6 lanes Opus cross-reviewed):**
  unified `IOpen + external PID + Dirichlet + Lag + full prime QR + universal TS + L(D) ⊬ ES` AND `IOpen + Bézout + BCM + Lag + full prime QR ⊬ ES` (`QR_TS_BCM.md`); proved external-PID barrier for `IE₁`/`IE₁⁻` + unique-`P` least-QNR QR PID + filtered Pell minima + twisted Pell PID (`IE1_BREAK.md`); new pointwise upper bound `R(n) ≪_ε n^{8/25+ε}` / `n^{7955/24966+ε}` (`ANALYTIC_34.md`); 16× sterile Mordell threshold drop to `r ≥ 177,505` + dense `x²+Dy²` core escape (`PROOF_LIFT.md`); Dirichlet-GRH `M_gen ∼ M₀` + `(PC)` `c_η√y` bridge + `alpo.ge/remark.pdf` transfer barriers (`ALPO_TRANSFER.md`); Vieta sterile fibres at `c = ⌊√n⌋` + sub-`n^{2/3}` counting + square-cover BM + new `R₈` floor `1,590,284,203,561` (`DISPROOF_DEEP.md`, `DISPROOF_COMP.md`).
* **z77 (2026-11-20, GPT-6.2 Astra `deep` 5-lane burst orchestrated by Claude Fable `best`, all 5 lanes Opus cross-reviewed):**
  slashed sterile Mordell threshold to **`r ≥ 7,219`** and closed the level-1 survival gap (`17 ≤ r ≤ 181,391` CERTIFIED + z76 tail, `R17_F3.md`); proved full ES on `(4^m−1)2^s+1` (`m=4,5,6`) and infinitely many non-ET-coverable `c_J·2^s+d_J` (`PROOF_S_WILD.md`); proved bounded-exponent étale-Brauer blindness `Br(W)[M]` upstairs on `S°, X°, U°` (`mM | E` sharp for the specified repair on the coordinate cover, `DISPROOF_KUMMER.md`); constructed PA-cut `C ⊊ D ⊊ R` BCM+Lag+QR model + separate multiquadratic unit-height criterion `H(A*) = Γ⁰[G]` + BCM+TS obstructions (`IE1_NONPID.md`); proved primorial-fibre short-witness sharpness + Assessment of `n^{1/20}` deficit at `θ = 3/10` for the hypothetical `W^{1/2}` kernel model (`ANALYTIC_413.md`); orientation-A `deg M ≥ ⌈(N+1)/2⌉` for `𝔽₃[T]` Conj. 0.2 (`F3_TARGET.md`).
* **z78 (2026-11-20, GPT-6.2 Astra `deep` 6-lane burst orchestrated by Claude, 2–4 steering rounds per lane).** Results,
  scopes and review status: `WAVES.md`, z78; open reviews: §Cross-model reviews above. Literature side lanes: the
  Alpöge–Buckmaster(–Coiculescu) Euler/Navier–Stokes releases were mined for method only (endpoint selection, certified
  numerics, generic-theorem + certificate Lean pattern); Masullo's unrefereed GRH announcement was graded NULL for ES transfer
  (`notes/z78/MASULLO_GRH_TRANSFER.md`). A research-mode skim is not an authoritative grading — use smart/deep for verdicts.
  Process notes (orchestrator-reported session observations): (i) one transient provider connection reset on one Astra lane
  (`upstream connect error … terminated`), cleared by a "continue" nudge and flagged to the user; no auth/quota error; Codex
  week ≈ 43% used at export, Anthropic week ≈ 74% (Opus reviews). (ii) A nested child agent fast-forwarded its commits into
  `main` instead of its parent branch (lane files only) — check `git log main` before reading lane diffs. (iii) Stale
  side-agent worktrees with stray files block slot reuse; leftovers were moved to
  `../erdos-straus-claude-stale-wt-backup-2026-11-20/`; delete Mathlib `.lake` caches (7.8 GB each) from finished worktrees.
  (iv) Multi-round steering with cross-pollination paid off: the F₃ proof came from "fix W and take a third contact", and two
  lanes independently proved the Proth core theorem. (v) A reviewer subagent may commit an empty placeholder and leave its
  review text uncommitted in the working tree — check `git status` after every `review` call.
* **z79 (2026-11-21, GPT-6.2 Astra `deep` 7-lane burst orchestrated by Claude Fable `best`, 2–3 rounds per lane; zero provider/auth/quota errors).**
  Results, scopes and review status: `WAVES.md` z79; open reviews: none owed. All 7 lanes merged cleanly with **21** Opus cross-reviews total (incl. second independent Opus ACCEPT of `6801/21497` on main and independent C/Python P-endpoint re-implementation of `R17` R2 depth 14). Process notes: (i) keeping orchestrator polling sleeps ≤ 3 min preserves prompt-cache TTL; (ii) hostile cross-lab Opus review caught an AP-equivalence overclaim in `ES_ENGINE` R1 (immediately downgraded and replaced in R2 with a linear-sieve mandatory-depth theorem among divisors `A ≤ X^γ, A ≡ −1 (u)` at one selected shift) and uncovered `LOWER_TAIL`'s own strongest corollary (`Z53_PZ` Conj. B), driving a 3-round cascade through Type I `log³p`, `O_A(π/log^A)` and `9/(32π²)`; (iii) Codex week ≈ 51% used at export; user directive: ignore Anthropic Opus review quota and push via handoffs straight at solving ES.
* **z80 (2026-11-21/22, GPT-6.2 Astra `deep` 7-lane multi-round burst orchestrated by Claude; zero provider/auth/quota errors).**
  Results, scopes and review status: `WAVES.md` z80; open reviews: none owed. All 7 lanes merged cleanly with **31 Opus lane reviews** (incl. the orchestrator-commissioned independent second QB review, run as a `smart` side agent so polling stayed under the cache TTL); separate Astra export-consistency review: see `WAVES.md` z80 R. Process notes: (i) lanes self-drive several internal rounds and self-commission reviews before first reporting (first reports after 60–100 min); steering works best as numbered targets + explicit cross-lane `git show side-agent/<lane>:notes/...` pointers; (ii) merge lanes as they finish (stash the in-progress master edits, `git merge --no-ff`, pop) and `/quit` them — it frees slots and keeps the export incremental; (iii) the R17 hostile replay took ≈ 4 h of wall time for one review (independent depth-16 search) — budget for it or cap replay scope in the brief; (iv) never issue an `Edit` and a `Bash` read of the same file in one parallel tool block (race); (v) the direct-assault lane again produced scoped barriers + an export-ready "anatomy of a failure" block rather than a mechanism — the open jugular is unchanged (B2).
* **z81 (2026-11-22, 7 GPT-6.2 Astra `deep` ES-assault lanes + 1 Claude Opus `smart` literature scout, 2 rounds per lane; zero provider/auth/quota errors).**
  Results, scopes and review status: `WAVES.md` z81; open reviews: none owed. All 8 lanes merged cleanly with **26 cross-lab reviews** (`data/z81/xreview/`, incl. independent second Opus review `REVIEW_CAP_RECORDS_OPUS2.md` of `CAP_ZERO` Thms I, V & `SPECIFIC_CLASS` Thm C1, and Astra review `REVIEW_LIT_OPUS_ASTRA.md` of `LIT.md`). Process notes: (i) launching `z81-lit` (`smart` Opus) first delivered a fast 20-min Round-1 bulletin (Trybushnyi `arXiv:2611.14167` priority flag & §11 barrier, Jiang–Lau–Lü `2611.12467`, Gao et al. `2611.24775` Davenport trap) that steered the live deep lanes mid-wave; (ii) Round-2 cross-pollination (`CAP_ZERO` `r²p+4` × `SPECIFIC_CLASS` → two packet/supply derivations of the `4/5` cap-1 exceptional bound sharing the internal z79/TQ transfer; `SPECIFIC_CLASS` Thm W → `GAP_ES` §8 growing-gap `0.665` tail and `GEOM_COMB` §8 smooth-gap normal order; `S_U7` composite walks → `B2_DUALITY` double-start traps) produced the strongest breakthroughs of the wave; (iii) Codex weekly quota reached **95% used** (3d20h remaining) as Round 2 completed — keep export consistency review light and watch quota before launching z82; (iv) no pointwise ES mechanism emerged, leaving B2 unchanged as the open core.
