# WAVES — chronological log, newest first

*One entry per wave, **at most 12 lines** excluding the heading. Waves before z53 are grouped. Write the entry at wave
export, following `AGENTS.md` §2–§3. Each entry has four parts:*
* *`+` positive results (with a label and a file);*
* *`−` negative results, compressed to one or two lines;*
* *`→` targets the wave opened or closed;*
* *`R` review status.*

*Items that pass the STATUS gate (`AGENTS.md` §3) are promoted to `STATUS.md`: records, refutations and target changes.
The `−` lines only compress; full scopes are in the cited notes and FRONTIER §6. Waves before z44 are in `STATUS_HISTORY.md`
(ledger (J)1–(J)110) and in `DISCOVERIES.md`.*

### z75 (2026-11-20): GPT-6.2 Astra 6-lane burst — BCM+4-squares, full prime QR, Lean 15·2^s+1 & 4^s+{33,273,297}, subexp e*(n), 2/3 (★)/U₇, trillion-scale R₈
`+` PROVED (logic): `IOpen + Bézout + BCM + Lagrange (4 squares) ⊬ ES` via twisted dyadic-axis end extensions (`notes/z75/BCM4_PUSH2.md`); separate external IOpen PID with `internal Dirichlet + Lagrange + full internal prime QR + L(D) ⊬ ES` (`BCM4_QR.md`, `BCM4_PUSH2.md`); unary `L(D)` holds in every external IOpen PID (`IE1_ES.md`); separate rank-one normal `IOpen + Lag` model repairs variable-radicand supplied-unit Pell windows with negative Pell and ¬ES(P) (`IE1_PUSH2.md`).
`+` PROVED (thin families & (S)): full **ES(15·2^s + 1)** for all s ≥ 0 via moving cyclotomic divisor, **Lean 4 verified** (`lean/ES/ES/Proth15.lean`), plus corollary `15·b^s+1` (`b ≡ 2 mod L`); full **ES(4^s + k)** for k ∈ {33, 273, 297} via finite certificates; **(S)** tightened from 28 to the exact 24 odd-square classes mod 840 (`notes/z75/CONJS_GEN.md`, `THIN_CYCLO.md`).
`+` PROVED (analytic records): unconditional effective pointwise cap `e*(n) ≤ exp(C√(log R · log log(3R)))` (`R = rad(n)`), explicit `4e*(p)+3 ≤ √(4p/3)`, Dirichlet-GRH `exp(O(√(log₂R · log₃R)))` (`notes/z75/ANALYTIC_BREAK.md`); shift-uniform `O(H exp(−c(log H)^{2/3}))` lower tail on both C-parities of (★) separately and on U₇ (`ANALYTIC_PUSH2.md`).
`+` PROVED / CERTIFIED (obstructions & censuses): open-surface `Br(V)[m]` vs 2-power-conductor dichotomy on `S°, X°, U°` (`DISPROOF_OBSTRUCT.md`); sharp cubic cutoff giving infinitely many non-BM sterile Type II fibres Y_{p,c} (`DISPROOF_PUSH2.md`); 10 new R₈ prime zeros raising in-𝔐 floor to **1,511,088,831,001**; `(MS⁺₁₀₅)` to 10¹¹, Type A to 2·10¹¹, `U₇/U_II/N_II` to 2·10¹⁰.
`−` Barriers: 3 frozen `REVIEW_GEN` maps non-universal (`CONJS_GEN.md`); single-pivot continuant fold matching, thin-core `a^m±b^m` density-0 barrier, Stepanov flat-mask linear degree cost, signed two-endpoint miss at 1,269,241 (`PROOF_WILD*.md`); dyadic kernel idempotence `J² = J` (`BCM4_QR.md`), circle Brauer obstruction `(s,x)` (`BCM4_PUSH2.md`), linear root search miss in QR PID (`IE1_PUSH2.md`).
`→` Closed: BCM+4-squares, Lagrange iteration, `15·2^s+1`, `4^s+{33,273,297}`, 3 frozen class-map tests, 4 non-square (S) classes. Open: ES, IE₁/IΔ₀, QR+TS, θ > 3/4 on E(N).
`R` Authored by GPT-6.2 Astra (`deep`), orchestrated by Fable (`best`). Independent Claude Opus cross-reviews ACCEPT or ACCEPT-WITH-FIXES (all fixes applied, Lean independently compiled) for Lanes 1, 2, 4, 5, 6; Lane 3 (`PROOF_WILD*`, scoped barriers only) self-checked with replay scripts.

### z74 (2026-11-19): ordinary-prime transfers, formula menus, weak-arithmetic models
`+` PROVED: one external IOpen PID with internal Dirichlet, universal prime two-squares, universal NR and Lagrange, in
    which a nonstandard P ≡ 1 (840) fails ES. It uses positive reciprocal descent, which bypasses the z66 arc obstruction
    (`LOGIC_JOINT_NR_TS.md`). Built on it: IOpen + Bézout + BCM + five squares ⊬ ES (`LOGIC_FIVE_SQUARE_BCM.md`).
`+` PROVED, in separate non-Bézout models: IOpen + Lag + Pell⁺ ⊬ ES, still with Pell⁻ and TS at irreducibles ≡ 1 (4) added
    (`LOGIC_POSITIVE_PELL_AUDIT.md`, `LOGIC_NEGATIVE_PELL_TS_TEST.md`). One Lagrange end extension: BCM at every old cutoff.
`+` PROVED, unconditional: fixed polynomial whole-triple menus in Gaussian + *integral* Pell data miss density one of the
    primes on a progression (`GAUSSIAN_PELL_MENU.md`); with Pell data alone, every prime of a class (`PELL_ES_MENU_NOGO.md`).
`−` Method counterexamples (`Z74_CHECKPOINT.md`): one-slot repair; 214729 misses both slots at all 16 divisor shifts
    (infinitely many under Dickson); 193 fails both windows at every root-eligible shift; hull BCM; Pell remainders escape.
`→` Open: BCM + four squares, iterating the Lagrange extension, the joint non-PID NR Variant (conditional, assembly owed).
`R` Authored by Astra. Assigned Opus cross-reviews all done: ACCEPT or ACCEPT-WITH-FIXES, fixes applied, no WRONG claim
    (`data/z74/xreview/REVIEW_*_OPUS.md`). Astra's own side audits served as review inputs, not as reviewed results.

### z73 (2026-11-19): weak theories with Bézout and PIDs
`+` PROVED countermodels:
    * IOpen + Bézout ⊬ ES (`Z73_OPEN_BEZOUT.md`, `LOGIC_BEZOUT.md`).
    * Per unit-square class, an external IOpen PID with a failing prime (`Z73_PID_SQUARE.md`).
    * One PID failing, for each standard unit-square class, in every interval (a, a+b), a ≥ 1, b infinite, with Bertrand
      and internal Dirichlet (`LOGIC_PID_INTERVAL_AUDIT.md`, `LOGIC_PID_DIRICHLET_AUDIT.md`).
    * In landing (non-PID) Bézout models: collection with PD and TS (`LOGIC_BEZOUT_NORM_COLLECTION.md`), short intervals
      and greatest prime divisors (`Z73_SHORT_INTERVAL.md`, `LOGIC_GREATEST_PRIME.md`).
`+` Row descent: IOpen + Bézout + Dirichlet has the same prime-tail dichotomy as IOpen (`Z73_ES_ROW_DESCENT.md`). Also the
    marked-section characterisation and composite-shift forcing criteria.
`−` Smith's PID alone does not give ES failure. Two four-term starts get trapped at 101641; a third reaches a solution (`data/z72/counter_tail/ROUND3.md`).
`R` Authored by Astra. Opus cross-reviews ACCEPT or ACCEPT-WITH-FIXES, fixes applied (`data/z74/xreview/`: Z73BASE,
    PIDEXT, COLLECT, NRMODELS, Z72PHASE).

### z72 (2026-11-19): phase criteria at prime shifts
`+` PROVED: a sharp two-factor criterion at a prime shift (`Z72_PAIR_PHASE.md`). With shifts not restricted to primes,
    support ≤ 2 Type II holds on a relative-density-one set of primes p ≡ 1 (4) (elementary). An exact sieve to 5·10⁸
    finds no failure (two independent engines). There is no all-prime implication.
`+` The closest nonexact triple for p ≡ 1 (24) (`EXTREMAL_ES.md`).
`−` At 1201 no prime shift has support ≤ 2. Monotone repair fails at 73. Frozen class-group menus miss a d = 2 fibre
    (`data/z72/mixproof.md`). Equal phase costs give opposite fixed-x outcomes at c = 43 (`PHASE43_DENOMINATORS.md`).
`R` Authored by Astra. Opus cross-review: ACCEPT-WITH-FIXES, fixes applied (`data/z74/xreview/REVIEW_Z72PHASE_OPUS.md`).

### z71 (2026-11-10): literature refresh
`−` No new mechanism. Dahan arXiv:2611.08717 gets 5/7 by the 3/4-note architecture, and its pointwise part is B2 with a
    cap (`Z71_LIT.md`).
`R` Orchestrator-reviewed only.

### z70 (2026-11-10): z69 leftovers. Campaign PAUSED afterwards.
`+` The e-ideal dictionary in the prime case (`Z70_CLASS.md`). Thm LS: the level sum is not modular (`Z70_LOOSE.md`).
`−` Scoped exclusions GW, AMB and REP (`Z70_LOOSE.md`, `Z70_GEN.md`).
`→` Three frozen generative class-map tests (`data/z70/xreview/REVIEW_GEN.md`).
`R` Astra: ACCEPT-WITH-FIXES.

### z69 (2026-11-10): hard-prime mining, nonlinear U₇ rules, Fable 5.2 ideation
`−` Finite polynomial divisor rules on the specified curves fail infinitely often (CONDITIONAL on Schinzel H;
    `Z69_NL7.md`). Mining and ideation gave nulls; only minor lemmas.
    Files: `Z69_*.md`.
`R` Astra.

### z68 (2026-11-09): (S) via p-adaptive words, U₇ tryhard
`+` PROVED: the cut identity and a partial contraction on refinements of length-three words (`Z68_SIGN.md`; it need not
    preserve goodness). Primes failing U₇ are ≪_A N/(log N)^A (`Z68_U7O.md`). GRH bridge: under GRH, (PC) with
    log F(y) ≤ y^{1/2−ε} gives eventual ES (`Z68_PC2.md`). CONJECTURES B and C are in `Z68_U7F.md`.
`−` Bounded-letter cascades fail (CONDITIONAL on Dickson). Two-prime covering gives no fixed-factor gain.
`R` Astra.

### z67 (2026-11-09): making the uncovered set explicit
`+` PROVED (computer-assisted): (S) leaves U_S nonempty for every ℓ ≥ 11. U is Haar-null (`Z67_ELL0.md`, `Z67_K11.md`).
`−` Candidate π° killed in cross-review.
`R` Astra.

### z66 (2026-11-08): the uncovered set U, the next logical rung
`+` PROVED: U ⊋ squares, and as ℓ grows almost all non-square one-prime slices lie in U (`Z66_UCOVER.md`). U is Haar-null
    in the profinite unit group (z67). IOpenLin + Bézout ⊬ (MS)
    (`Z66_IE1.md`).
`−` The arc method (odd-square landing) is dead from IOpen + Lagrange upward (bypassed in z74 by descent). No H★ engine.
`R` Astra.

### z65 (2026-11-08): logical strength, char-p lifting
`+` PROVED: T1 + two squares still ⊬ ES (`Z65_LOGIC2.md`). Dichotomy: NOI proves a class tail ⟺ IOpen does ⟺ finite
    ET coverage ⟺ the class misses U.
`−` Good-reduction lifting is dead at p ≡ 1 (12) (`Z65_LIFT.md`).
`R` Astra.

### z64 (2026-11-08): unprovability, conjecture (S), cross-field equivalents
`+` PROVED: normal open induction does not prove ES on any class of 𝔐, while IOpen proves every other class mod 840
    (`Z64_UNPROV.md`). (S) is proved for non-square n ≡ 1 (4) outside 28 of the 210 classes (`Z64_SDEEPF.md`).
`−` Ten cross-field equivalences, none of whose tools works at a single prime (`Z64_EQUIV.md`). PA/ZFC independence is
    judged unrealistic.
`R` Astra.

### z63 (2026-11-07): precedent hunt
`+` Euclidean paths are loops in Γ₀(n). Conjecture (S) stated, with (S)(p) ⟹ ES(p) (`Z63_EUCLID.md`).
`−` No precedent known for a pointwise hit of this kind (`Z63_PRECEDENT.md`).
`R` Astra.

### z62 (2026-11-07): new proof paradigms at one prime
`+` The exact arrangement form of R(p) = 0. Lemma P0: parity and index arguments are equivalent to certificate weights.
`−` No inverse theorem; uniform parity non-vanishing is refuted (`Z62_*.md`).
`R` Astra.

### z61 (2026-11-07): board on new mechanisms
`+` A divisor-residue pigeonhole criterion, which repackages the ρ-ratio criterion (`Z61_PIGEON.md`).
`−` The board found no new mechanism; the valuation-transport rules are dead (`Z61_TRANSPORT*.md`). Board memo:
    `~/.pi/boards/20261107-es-newmech/memo.md`.

### z60 (2026-11-06): clean-statement attack, three generators
`+` U₇ census, CERTIFIED: the odd non-square zeros up to 10¹⁰ are exactly Z₇ (`Z60_LOPEZ.md`).
`+` R-zeros along non-square polynomials have density 0 (`Z60_MS105.md` Thm 3).
`+` Signed T1 (`Z60_SIGNED.md`).
`−` RAYCLASS, DYNAMICS and TRACE are exact encodings that end at B2. **Spending rule adopted:** no more re-encoding waves
    (`OPERATIONS.md`).
`→` Targets (MS-U₇) and (MS⁺₁₀₅). Full summary: `Z60_SUMMARY.md`.
`R` Astra per lane; FRONTIER consistency review `data/z60/xreview/REVIEW_FRONTIER_Z60.md` (likewise for z53–z59).

### z59 (2026-11-05): survivors of z58
`+` CERTIFIED: the (MS⁺) census to 10¹² (9 primes and 18 composites, the largest 17,401,609), and the odd non-square U_II zeros up to 10¹⁰
    are {105, 4545}.
`+` 13 explicit Waldspurger zeros (`Z59_WALDS.md`).
`−` Cusp/Waldspurger no-go. `Z59_MSPLUS.md` Prop 2.2 withdrawn. Full summary: `Z59_SUMMARY.md`.

### z58 (2026-11-05): sixteen lanes on (MS)
`+` PROVED: the positive-integral BM set is empty iff n is a square, and 4545 is a non-BM Hasse failure (`Z58_STRUCT*.md`).
`+` CERTIFIED: (★) at all primes in 𝔐 ∩ (10¹⁰, 3·10¹¹].
`+` Kandukoori–Ramesh–Kumar have a 3/4 claim in a commit dated 2026-07-30, Lean-conditional on nine analytic axioms at
    the time. Commit-date ordering only, not verified public priority; it must be cited (`Z58_LIT.md`).
`−` Scoped no-gos for Hecke and ternary-theta proxies, Mordell menus, function-field analogues and weak arithmetic. Full
    summary: `Z58_SUMMARY.md`.

### z57 (2026-11-05): synthesis
`+` CONJECTURE (MS): R(p) ≥ 1 for every prime p > 10¹⁷ in 𝔐. PROVED: (MS) ⟹ ES, via Mordell and Salez (`Z57_SYNTH.md`).
`+` Type II genus main term ≥ 10⁻¹⁰·log³p at large p ≡ 1 (4) (`Z57_BFII.md` Thm G). 𝔊*-zeros are ≪ x/(log x)^A (`Z57_BFO.md`).
`−` No complementarity: four implications refuted (`Z57_COMPLEMENT.md`). Full summary: `Z57_SUMMARY.md`.

### z56 (2026-11-04)
`+` M_gen(p) ≥ (5/6 − o(1))·M₀ at large p ≡ 1 (4) (`Z56_FAMDESIGN.md` Thm V).
`+` #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X) for X ≥ X₀ (`Z56_FAMTRY.md`).
`+` Lean HC infrastructure. Drafts `paper/es-count-note` and `paper/es-hc-note`.
`−` K(4) open. Full summary: `Z56_SUMMARY.md`.

### z55 (2026-11-04)
`+` The (H⁻_𝔉) inequality fails at the checked zero primes (CERTIFIED); the eventual statement is open (`Z55_CROSSF.md` §4). A positive proportion of primes have R_𝔉 ≥ 2 (`Z55_CROSSO.md`).
    HC ≤ 64 below 10¹².
`−` TD is not proved for any η > 0. Full summary: `Z55_SUMMARY.md`.

### z54 (2026-11-03)
`+` K(4) ⟺ P(4,15). Theorem Q: HC ≥ 7 at primes p = 5m² + 1 with 4 | m. HC ≤ 8 for primes p ≡ 1 (4) outside 𝔐.
`−` Triangle-inequality and character-side square-sieve routes give nothing. Full summary: `Z54_SUMMARY.md`.

### z53 (2026-11-01)
`+` M_gen(p) ≫ log²p unconditionally at large p ≡ 1 (4) (`Z53_GENUSLVAL.md`). R(n) ≪ n^{12/37+ε} (`Z53_SQSIEVE.md`).
`+` Almost-all R(p) ≥ (1/64 − ε)log²p (`Z53_PZ.md`). ES(15·2^s + 1) CERTIFIED for s ≤ 3·10⁶.
`−` The oracle no-go (`Z53_NONCRTLOGIC.md`) and the lattice no-go (`Z53_LATTICE.md`). Full summary: `Z53_SUMMARY.md`.

### z52–z52d (2026-10-30 … 11-01): breadth-first connection generation, triage, depth lanes
`+` `BM_LVALUE.md` Thm A (exact L-value formula) and Cor 3.1 (M_BM ≥ 0.1402·log²p at large p ≡ 1 (8)).
`+` Lean: ES(3·2^s + 1); 15·2^s + 1 off s ≡ 0, 240 (360).
`+` The I3_𝒞 zeros among primes p ≡ 1 (4) up to 10⁹ are {5, 13, 17, 2521} (`Z52_BANKED.md`).
`−` Pass 1 over 2284 items found 0 new-structural (`ES_CONNECTIONS_TODO.md`). Depth lanes narrowed (`Z52D_*.md`). The
    coprime SQ statement in FRONTIER §5.5 was wrong.

### z50–z51 (2026-10-29/30): exceptional-set offensive
`+` E_U(N) ≪ N·exp(−c(log N)^{2/3}…). The supply-law caps 3/4 (ES) and 2/3 (U/ES₅) are attained (`EXSET_*.md`,
    `BREADTH_Z45.md` §15–16).
`+` Cap relaxation at (log log X)^{1+ε} with a power-saving exceptional set (`EXSET_LINNIK_CAPS.md`).
`−` Nothing beyond 3/4 for ES or 2/3 for U, even conditionally on a standard hypothesis.

### z44–z49 (2026-10-19 … 10-29): boards #3/#4, breadth, forests
`+` No étale-Brauer descent obstruction for any n ≥ 2 (`BRAUER_TWISTS.md`). Q3 refuted (`Q3_PIVOT.md`).
`+` Forest witnesses are not polylog; H₂ refuted (`H4_NOT_POLYLOG.md`). I3 counts (`I3_DEEP_*.md`).
`−` Nine new fields and two boards all end at B2 (`BREADTH_Z45.md` §1–14).
