# STATUS — the master summary of current results

*Last wave included: **z75** (2026-11-20). This file is curated, not a log, and is capped at about 250 lines. Rules for
changing it are in `AGENTS.md` §3. When this page and a source note disagree, the source wins; fix this page.
The wave-by-wave history is in `WAVES.md` (z44 onwards) and in `STATUS_HISTORY.md` (through 2026-10-19). The
expert-level deep reference is `FRONTIER.md`. Citations of "STATUS.md §…" written before 2026-11-19 refer to
`STATUS_HISTORY.md`.*

## 0. Bottom line

* **The Erdős–Straus conjecture (ES) is open.** Nothing here proves it, conditionally on any standard conjecture or
  otherwise. Nothing here disproves it either.
* All proofs are reviewed internally only: hostile reviews by other model instances, usually including one cross-lab
  review (GPT "Astra" for Claude work, and Claude Opus for Astra work). **Nothing is externally refereed.** No campaign theorem has been posted or submitted. The only
  external contribution is an audit of other people's claimed proofs, plasma-ai/erdos#65, merged 2026-11-10.
* **Where everything ends (Assessment; FRONTIER one-paragraph summary, §2–3).** About 280 tasks up to 2026-10-19 and about
  30 waves since, across every phase, several advisory boards and three labs' models, all reduce to one statement, called
  **B2**. A single integer, determined by p and the slice parameters, must have a divisor in a residue class whose
  modulus is itself part of the solution. Only polylog(p) winners are expected.
  * A single hit R(p) ≥ 1 on the c = 1 line is *sufficient* for ES(p), not necessary.
  * The counting target H⁻_BM, R(p) ≥ ε·M_BM(p), is stronger still. Like every eventual bound, it gives ES only above a
    threshold, plus a finite check below it.
  * The main term M_BM(p) ≍ log²p is an unconditional theorem (§1B).
  * No standard conjecture is known to imply the lower tail.
  * No precedent of this shape is known for any natural problem.
* **Campaign state.** The campaign runs in bursts, one per new frontier model. Between bursts it is idle. Wave **z75**
  (2026-11-20, 6-lane GPT-6.2 Astra burst orchestrated by Claude Fable) delivered Opus-reviewed breakthroughs across
  all three pillars: `IOpen + Bézout + BCM + Lagrange ⊬ ES`, full internal prime QR PID, Lean-verified full-family
  `ES(15·2^s+1)` + `4^s+{33,273,297}`, effective subexponential pointwise cap `e*(n)`, 2/3 lower-tail `(★)/U₇` bounds,
  and trillion-scale `R₈` / extended censuses (`WAVES.md`). Spending rule unchanged (`OPERATIONS.md`).

Notation: 𝔐 = {1, 121, 169, 289, 361, 529} mod 840 (Mordell's hard classes). R(p) = the (★)/c = 1 Type II count.
M₀(p) ∼ (3/(2π²))log²p is its expected size. It is a finite sum with an O(log p) secondary term; the exact form is in
`BM_LVALUE.md`. Definitions are in FRONTIER §2.

## 1. Headline positive results

Each item carries a label, then a pointer. "PROVED rel. X" means proved relative to the published theorems X.

### A. Exceptional set and almost-all results (averages; they say nothing about a given p)
* **E(N) ≪ N·exp(−c(log N)^{3/4})**, improving Vaughan's exponent 2/3. INTERNALLY PROVED; `paper/es-threequarter-note`.
  * Variants: short intervals; progressions, losing the smooth part q₁; numerators m ≥ 4, at a cost of m^{−1/4}
    (`paper/es-mn-short-note`). 3/4 is sharp for the audited CRT architectures (`paper/sieve-limits-note`).
  * **Priority:** Kandukoori–Ramesh–Kumar's claim predates ours by commit date (2026-07-30; Lean-conditional then). Cite
    them (`Z58_LIT.md`). Dahan, arXiv:2611.08717, gets 5/7 by the same architecture (`Z71_LIT.md`).
* **Σ_{p≤N} f_I(p) ≪ N log²N**, which removes Elsholtz–Tao's log log N. PROVED rel. the trace formulae, Weil, twisted Weil,
  Selberg 3/16 and λ₁(SL₂(ℤ)) > 1/4; it needs expert scrutiny. `paper/es-typei-heegner-note`.
* **U and ES₅ are sufficient restrictions (U ⟹ ES₅ ⟹ ES).** E_U(N) ≪ N·exp(−c(log N)^{2/3}(log log N)^{−1/3}) over
  n ≡ 1 (4). Without the log log, failures are ≪ N·exp(−c(log N)^{2/3}) at primes p ≡ 1 (4) for U, and at all primes for
  ES₅. 2/3 is sharp for the audited CRT architectures. PROVED; `EXSET_BEYOND_CRT.md`, `EXSET_I3.md` §7.3 (z50).
* **Almost all primes have R(p) ≥ (1/64 − ε)log²p.** PROVED rel. Bombieri–Vinogradov. `Z53_PZ.md`, `paper/es-count-note`
  Thm C. Akaka claims, unrefereed, a stronger almost-all bound for the *full* Type II count. It does not imply this
  result for R (FRONTIER §5.1).
* **Shift-uniform 2/3 lower tail on both C-parities of (★) and U₇:** outside ≪ H·exp(−c(log H)^{2/3}) primes per
  interval (M, M+H], both R_odd and R₈ separately have ≥ δ(log H)^{2/3} ordered witnesses (improving `Z56_FAMTRY`'s 1/2
  exponent for R(p) = 0 and `Z68_U7O`'s N/(log N)^A for U₇; unspecified c, ineffective onset). PROVED rel. BV, BT and
  Mertens; Opus-reviewed; novelty unverified; `notes/z75/ANALYTIC_PUSH2.md`.
* **Density transition for m/p:**
  * It lies at log N ≍ m^{1/3} up to a (log log N)^{1/3} factor. Thm U is PROVED rel. the internal 3/4 theorem, BV and
    Shiu; Thm L′ is PROVED rel. ET, Brun–Titchmarsh, Shiu and Pólya–Vinogradov.
  * The sharp order on both sides is CONDITIONAL on a uniform (SEL_m) (`paper/es-mn-short-note` §8–§9).

### B. Pointwise at every large prime p ≡ 1 (4): main terms and relaxations, not ES
* **Genus main term M_gen(p) ≥ (5/6 − o(1))·M₀(p)** for large p ≡ 1 (4). PROVED rel. Burgess and Heath-Brown's quadratic large sieve.
  `Z56_FAMDESIGN.md` Thm V.
* **Brauer–Manin-corrected main term:**
  * Exact L-value formula T(p) = (σ/4)E(χ_p)L(1,χ_p)² + O(p^{−1/16}log p). PROVED, cross-model reviewed; `BM_LVALUE.md`
    Thm A.
  * Hence M_BM ≥ 0.1402·log²p and M_BM ≥ 0.9225·M₀ at large p ≡ 1 (8) (Cor 3.1).
  * The odd-square obstruction T1 is built in exactly (`BM_CORRECTED_COUNT.md`).
* **Type II genus main term ≥ 10⁻¹⁰·log³p** for large p ≡ 1 (4). PROVED, genus part only; `Z57_BFII.md` Thm G.
* **Upper side:** R(n) ≪ n^{12/37+ε}, a power saving over n^{1/3} that improves the campaign's earlier 74/225. PROVED rel.
  Weil and van der Corput; external priority unverified; `Z53_SQSIEVE.md`.
* **Capped relaxation (the first pointwise positive mechanism).** 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den z = r²,
  r odd, (r, n) = 1, rad r | y, v_ℓ(r) ≤ e. **Unconditional effective subexponential bound:** e*(n) ≤ exp(C√(log R · log log(3R)))
  for every n > 1, R = rad(n) (PROVED rel. Gallagher, Linnik, Minkowski II; explicit 4e*(p) + 3 ≤ √(4p/3) at p ≡ 1 (8);
  Dirichlet GRH alone suffices for exp(O(√(log₂R · log₃R))), superseding Dedekind GRH; Opus-reviewed, `notes/z75/ANALYTIC_BREAK.md`,
  improving `CAP_POINTWISE.md` / `CAP_DOWN.md`). Exceptional set ≪ X^{1−c} at cap (log log X)^{1+ε} (`EXSET_LINNIK_CAPS.md`).
  ES ⟺ e* = 0; at a fixed window, cap 0 is the B2 divisor event.

### C. ES proved on infinite thin families (computer-assisted and Lean-checked)
* **ES holds for all 3·2^s + 1, 15·2^s + 1, 63·2^s + 1 and 7·4^s + 9**, and for **4^s + k** with k ∈ {9, 33, 57, 81,
  105, 129, 153, 177, 201, 225, 249, 273, 297} (all integers s ≥ 0). PROVED (`paper/es-exponential-families`; z75 Opus-reviewed
  `notes/z75/CONJS_GEN.md`, `notes/z75/THIN_CYCLO.md`, closing all previously open residual families via a moving
  cyclotomic divisor for 15·2^s + 1 and finite replayable certificates for k ∈ {33, 273, 297}).
  * **Lean 4 verified (zero `sorry`/`native_decide`, standard axioms):** 3·2^s + 1 (`Proth3.lean`) and **full 15·2^s + 1**
    for all s ≥ 0 (`lean/ES/ES/Proth15.lean`, `ESProth15.proth15`, Opus-compiled).
  * Corollary: ES holds for all 15·b^s + 1 with b ≡ 2 (mod L) (explicit L), with no finite ET/divisor covering (`THIN_CYCLO.md` §2).
  * 3·2^s + 1, 15·2^s + 1, 63·2^s + 1 and 7·4^s + 9 admit **no finite covering by Elsholtz–Tao and divisor classes**.

### D. Structure and obstruction theorems (what a proof has to beat)
* **Brauer–Manin sees exactly the squares; open-surface exponent dichotomy.** On the (★) surface and on the Type II
  threefold, the positive-integral BM set is empty iff n is a square; 4545 is a non-BM failure (`Z58_STRUCT*.md`), and
  sharp size cutoffs give infinitely many non-BM sterile Type II fibres Y_{p,c} at c ≈ p^{2/3} (`notes/z75/DISPROOF_PUSH2.md`).
  On the coordinate opens S_n°, X_n°, U_n°, a moving denominator defeats all Br(V)[m] and exponent-m geometric covers at
  every fixed m, whereas 2-power-conductor characters at unbounded depth at one prime detect exact integral points.
  PROVED (z75 Opus-reviewed); `notes/z75/DISPROOF_OBSTRUCT.md`.
* **Finite procedures fail at trap points** (method barrier). This covers coverings, polynomial menus, and finite oracle
  programs with a finite formal tree at the trap: PROVED (`Z53_NONCRTLOGIC.md`); prime failures CONDITIONAL on Schinzel H.
  It is unconditional (z74, Opus-reviewed) for polynomial whole-triple menus in both Gaussian coordinates and any fixed
  number of *integral* negative-Pell witnesses: they miss relative density one of the primes ≡ 1 (M), for a computable M
  with 840 | M (`GAUSSIAN_PELL_MENU.md`). Sterile Mordell points exist for all primes r ≥ 2.84·10⁶ (`STERILE_LOWER.md`).
* **Witness sizes are not polylog.** For fixed κ < 1/12, or κ < 1/6 with Gallagher or GRH, infinitely many p have no
  forest edge with larger endpoint in [4, exp((log p)^κ)]. Only {1,2} and {2,3} remain. This refutes Conjecture H₂.
  PROVED rel. the internal energy lemma; `H4_NOT_POLYLOG.md`.
  * At primes p ≡ 1 (4), both Type II witness moduli 4acd − 1 and 4bcd − 1 are at least the least quadratic non-residue
    (`Z57_BFII.md` Cor 2.4).
* **Function fields:** ES_q(T) has no finite linear covering for q = 3^r, r ≥ 2 ((J)51, (J)56, (J)67). q = 3 remains open.
* **Numerator blindness:** M^□ is a theorem for every M ≡ 0 (4), while 8/n fails at n = 131 and 241 ((J)41, FRONTIER §1).
  A proof needs a 4-specific input.

### E. Logic: weak arithmetic does not prove ES (PROVED, internal; nonstandard countermodels)
In each model a nonstandard prime fails ES. The models are *separate* unless stated, so do not combine their axiom lists.
Every item has had one cross-lab review: z64–z65 Claude work by Astra, and z73–z75 Astra work by Opus
(`data/z74/xreview/`, `notes/z75/*REVIEW*`, `data/z75/ie1/`).
* **Normal open induction** (+ gcd, irreducible divisors, and all true universal ring sentences) does not prove ES on any
  class of 𝔐. IOpen does prove it on every other class mod 840. `Z64_UNPROV.md`; adding T1 and two squares, see
  `Z65_LOGIC2.md`.
* **IOpen + Bézout** does not prove ES (`Z73_OPEN_BEZOUT.md`, `LOGIC_BEZOUT.md`); one separate model adds full collection,
  PD and TS (`LOGIC_BEZOUT_NORM_COLLECTION.md`). Prime-tail dichotomy with Dirichlet: `Z73_ES_ROW_DESCENT.md`.
* **External IOpen PIDs (automatically satisfy unary polynomial-divisibility minimization L(D), `notes/z75/IE1_ES.md`):**
  * Per unit-square class, an external PID with failing primes in every infinite interval, Bertrand and internal Dirichlet
    (`Z73_PID_SQUARE.md`, `LOGIC_PID_INTERVAL_AUDIT.md`, `LOGIC_PID_DIRICHLET_AUDIT.md`).
  * **Joint TS/NR/Lag PID:** one external IOpen PID with internal Dirichlet, universal prime TS, universal NR, Lagrange and
    L(D), where P ≡ 1 (840) fails ES (`LOGIC_JOINT_NR_TS.md`, `LOGIC_JOINT_PID_TREE_AUDIT.md`; QR_std(3) fails at P).
  * **Full internal prime QR PID (z75, Opus-reviewed):** one external IOpen PID with internal Dirichlet, Lagrange, L(D) and
    **full internal prime quadratic reciprocity** (both supplements, both odd primes universally quantified; exact order-2
    squareclass group at every odd prime), where P ≡ 1 (840) fails ES (`notes/z75/BCM4_QR.md`, `notes/z75/BCM4_PUSH2.md` §5;
    universal TS not asserted in this model; least search for v² ≡ ct (mod P) still fails, `notes/z75/IE1_PUSH2.md`).
* **IOpen + Bézout + bounded common multiples (BCM) + Lagrange (four squares) ⊬ ES (z75, Opus-reviewed):** countable model
  via twisted dyadic-axis end extensions with P ≡ 1 (840) failing ES (`notes/z75/BCM4_PUSH2.md`, superseding the five-square
  model `LOGIC_FIVE_SQUARE_BCM.md`, which has Pythagoras number 5; not an external PID).
* **Variable-radicand Pell-window induction (z75, Opus-reviewed):** parameter-free Pell-window induction W₂ fails in the
  z74 PID, 5-square BCM and collection models (`notes/z75/IE1_ES.md`), but a separate rank-one normal `IOpen + Lag` model
  has ¬ES(P), negative Pell at P and full variable-radicand supplied-unit Pell windows (`notes/z75/IE1_PUSH2.md`; not PID/IE₁).
* **Not claimed:** independence from IE₁, IE₁⁻, IΔ₀, PA or ZFC; a standard counterexample; simultaneous QR + universal TS.

### F. Certified computations (exact, finite; engines and ranges are in the cited files)
* (★) holds at all 355,096,166 primes in 𝔐 ∩ (10¹⁰, 3·10¹¹] (`Z58_SUMMARY.md` §3).
* The non-square zeros of R in 𝔐 up to 10¹² are exactly 9 primes and 18 composites, largest 17,401,609 (one engine;
  `Z59_MSPLUS.md`). **(MS⁺₁₀₅)** (all classes n ≡ 1 (4), gcd(n, 105) = 1) certified to **10¹¹** (two engines; `notes/z75/DISPROOF_PUSH2.md`).
* Odd non-square zeros up to **2·10¹⁰** (two engines in (10¹⁰, 2·10¹⁰], `notes/z75/DISPROOF_PUSH2.md`; earlier ≤ 10¹⁰ in
  `Z58_WILDCARD.md`, `Z59_SUMMARY.md`, `Z60_LOPEZ.md`): N_II only 4545; U_II only {105, 4545}; U₇ only the 8 composites of Z₇
  (105-multiples also checked to 5·10¹⁰).
* Among primes p ≡ 1 (4) up to **2·10¹¹**, the b = 1 line (López Type A) fails only at 193, 2521 and 66529 (two engines;
  `B1_LINE.md`, `notes/z75/DISPROOF_PUSH2.md`).
* **R₈ (C-even (★)) threshold floor:** 10 new certified prime zeros raise the in-𝔐 floor to **1,511,088,831,001** (R = 44;
  also 1,218,367,081,201 and 452,438,542,081; three independent checkers; `notes/z75/DISPROOF_OBSTRUCT.md`, `DISPROOF_PUSH2.md`).

## 2. Current open targets (statements whose proof would matter)
Ranked by the campaign (Assessment). Definitions are in the cited files.
1. **(MS-U₇)**: U₇(p) for 𝔐-primes p > 10¹⁷. **(MS⁺₁₀₅)**: R(n) ≥ 1 for non-square n ≡ 1 (4), (n, 105) = 1,
   n > 29,210,401 (certified to 10¹¹). Cleanest sufficient single-sentence targets. (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II)
   (`Z57_SYNTH.md`, `Z59_MSPLUS.md`, `Z60_LOPEZ.md` §4.2, `Z60_SUMMARY.md` §5).
2. **H⁻_BM:** R(p) ≥ ε·M_BM(p) for large p (FRONTIER §2.4). Also conjecture **(S)** (`Z63_EUCLID.md`), now PROVED for all
   non-square n ≡ 1 (4) outside the exact **24 odd-square classes mod 840** (`notes/z75/CONJS_GEN.md` Thm 2, Opus-reviewed).
3. **Structure / U₇ / class groups:** Conjectures B and C in `Z68_U7F.md`; `Z70_CLASS.md` open list (Rédei 4-rank,
   small-split-prime orbits, solution-graph moves). (The 3 frozen `REVIEW_GEN.md` class-map tests closed non-universal in z75.)
4. **Logic:** IE₁, IE₁⁻, IΔ₀ and IΔ₀ + exp remain open; also simultaneous full prime QR + universal TS, and combining
   Pell-window induction with Bézout/PID. (BCM + four squares and Lagrange end-extension iteration are CLOSED in z75.)
5. **Coverings and function fields:** the r = 17 Mordell point; CONJECTURE 0.2 over F₃[T]. (15·2^s + 1 and 4^s + {33,273,297} CLOSED in z75.)
6. **Analytic sub-problems:** FRONTIER §7 (e.g. θ > 3/4 on E(N), cancellation on the height-dependent modular hyperbola,
   pushing e*(n) below L_R[1/2]).

## 3. Negative results: summarised, not listed
Most of the campaign's output is scoped no-gos, meaning "method class X cannot do it". They are kept out of this page on
purpose.
* **Where they live:** the barrier map as theorems is FRONTIER §3, the proof screening checklist is FRONTIER §4, and the
  dead ends are FRONTIER §6, one line each. Every no-go, scope included, is in its own note and in `WAVES.md`.
* **The pattern:** every analytic, sieve, spectral, automorphic, geometric, algebraic, dynamical, logical and cross-field
  re-encoding tried so far ends at B2, at a non-standard hypothesis, or at evidence. So a new memo that "ends at B2 again"
  is not news.
* **Rule for new work:** before starting, run the FRONTIER §4 checklist. A barrier only changes this page if it rules out
  a *broad* class of proofs that the current text does not already rule out (`AGENTS.md` §3).

## 4. Refuted or corrected claims (do not rely on the old versions)
* **Refuted, or refuted in the checked range:**
  * Conjecture H₂ (polylog forest witnesses): `H4_NOT_POLYLOG.md`.
  * The (H⁻_𝔉) inequality fails at the checked primes with R_𝔉 = 0 < M_𝔉. M_𝔉 > 0 was replayed through the 10¹²-range
    scans, and zeros were found up to 10¹⁵. So any true version needs a large p₀, but the eventual statement is **not**
    disproved (`Z55_CROSSF.md` §4(ii)).
  * Q3 pivot universality, at p = 7,909,441: `Q3_PIVOT.md`.
  * x* sterile, at r = 13: `es-coverings-note`.
  * Former C_SQ, at 288, 336 and 4545: `espaper` v11.
* **Corrections:** the coprime form of SQ is false at 105, 345, 561 and 5985 (`Z52_BANKED.md` §1(d)).
  `Z59_MSPLUS.md` Prop 2.2 is withdrawn.
* **Priority:** Kandukoori–Ramesh–Kumar's 3/4 claim predates ours by commit date, so do not claim the bound as first.
  Public priority is unverified. Several "new" items are known (FRONTIER §1, `Z58_LIT.md`).
* **Labels:** `espaper.tex` headlines labelled CLAIMED/PROVISIONAL stay provisional unless restated above.

## 5. Map of master files
| file | role | updated |
|---|---|---|
| `README.md` | orientation for humans | rarely |
| `AGENTS.md` | rules: where results go, anti-deluge policy | when the process changes |
| **`STATUS.md`** | **this page: curated current results** | at wave export if an `AGENTS.md` §3 rule fires; corrections immediately |
| `WAVES.md` | chronological log, at most 12 lines per wave | every wave |
| `FRONTIER.md` | expert reference: reduction, barrier map, checklist, records, dead ends, open problems | at wave export, in place |
| `OPERATIONS.md` | orchestrator directives, models, quota, pause state | when they change |
| `paper/README.md` | status of the write-ups in `paper/` | when a paper changes |
| `DISCOVERIES.md` | ledger (A)–(J)110, frozen 2026-10-19 | frozen |
| `STATUS_HISTORY.md`, `CAMPAIGN_SUMMARY.md`, `Z53_SUMMARY.md`…`Z60_SUMMARY.md` | historical snapshots | frozen |
