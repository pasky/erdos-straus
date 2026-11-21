# STATUS — the master summary of current results

*Last wave included: **z78** (2026-11-20). This file is curated, not a log, and is capped at about 250 lines. Rules for
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
* **Campaign state.** The campaign runs in bursts, one per new frontier model. Between bursts it is idle. Waves **z75–z78**
  (2026-11-20, GPT-6.2 Astra bursts orchestrated by Claude, all promoted items Opus cross-reviewed) proved BCM + four
  squares + full prime QR + universal TS in one Bézout model, the nonstandard-PID IE₁/IE₁⁻ barrier and norm/elliptic window
  barriers, bounded upstairs étale-BM blindness, `(4^m−1)2^s+1` (`1≤m≤10`; Lean for 3, 15, 63), subexp `e*(n)`,
  `R(n) ≪ n^{272/857+ε}`, 2/3 `(★)/U₇` tails, sterile Mordell threshold **293**, F₃[T] Conjecture 0.2, and `R₈` 1.59T.

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
* **Genus main term:** M_gen(p) ≥ (5/6 − o(1))·M₀(p) unconditionally for large p ≡ 1 (4) (PROVED rel. Burgess and
  Heath-Brown's quadratic large sieve; `Z56_FAMDESIGN.md` Thm V). **CONDITIONAL on Dirichlet GRH:** M_gen(p) ∼ M₀(p),
  including the Burgess corner and both edges (no numerical onset; Opus-reviewed, `notes/z76/ALPO_TRANSFER.md` Thm G).
* **Brauer–Manin-corrected main term:**
  * Exact L-value formula T(p) = (σ/4)E(χ_p)L(1,χ_p)² + O(p^{−1/16}log p). PROVED, cross-model reviewed; `BM_LVALUE.md`
    Thm A.
  * Hence M_BM ≥ 0.1402·log²p and M_BM ≥ 0.9225·M₀ at large p ≡ 1 (8) (Cor 3.1).
  * The odd-square obstruction T1 is built in exactly (`BM_CORRECTED_COUNT.md`).
* **Type II genus main term ≥ 10⁻¹⁰·log³p** for large p ≡ 1 (4). PROVED, genus part only; `Z57_BFII.md` Thm G.
* **Upper side:** PROVED unconditionally for every n ≥ 2: **R(n) ≪_ε n^{20/63+ε}** and **n^{272/857+ε}** (≈ 0.317386; two
  independent Opus reviews each), and n^{46/145+ε} (≈ 0.317241; one Opus review, a second is owed). Common inputs: Weil,
  uniform stationary phase, the additive large sieve and r₂ ≤ 4τ; the spacing steps use Erdős–Turán and the classical
  fourth- resp. third-derivative tests; no exponent-pair input (`notes/z78/ANALYTIC_WILD.md` §§7–8, 11–12, 14; supersedes
  z76's 8/25 and 7955/24966; uniform numerator-M bound R_M in §§13–14; external priority unverified).
* **Capped relaxation (the first pointwise positive mechanism).** 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den z = r²,
  r odd, (r, n) = 1, rad r | y, v_ℓ(r) ≤ e. **Unconditional effective:** e*(n) ≤ exp(C√(log R · log log(3R))) for n > 1,
  R = rad(n) (PROVED rel. Gallagher, Linnik, Minkowski II; explicit 4e*(p) + 3 ≤ √(4p/3) at p ≡ 1 (8)); **CONDITIONAL**
  on Dirichlet GRH alone: log(1 + e*(n)) ≤ (2√2 + o(1))√(log₂R · log₃R) as R → ∞ (2√2 is this method's constant, not a
  matching lower bound; `notes/z75/ANALYTIC_BREAK.md`, `notes/z78/ANALYTIC_WILD.md` §4, Opus-reviewed). Exceptional set ≪ X^{1−c}
  at cap (log log X)^{1+ε} (`EXSET_LINNIK_CAPS.md`). ES ⟺ e* = 0; at a fixed window, the δ_p = 0 branch of cap 0 is B2 (`CAP_DOWN.md`).

### C. ES proved on infinite thin families (computer-assisted and Lean-checked)
* **All `(4^m−1)2^s + 1` (`1 ≤ m ≤ 10`), `7·4^s + 9`, and `4^s + k`** for k ∈ {9, 33, 57, 81, 105, 129, 153, 177, 201, 225,
  249, 273, 297} (all s ≥ 0). PROVED, computer-assisted (`paper/es-exponential-families`; Opus-reviewed `notes/z75/CONJS_GEN.md`,
  `THIN_CYCLO.md`, `notes/z77/PROOF_S_WILD.md`, `notes/z78/PROTH_ALLM.md` §3 for m = 7–10). **Lean 4** (zero `sorry`/
  `native_decide`): `3·2^s+1`, `15·2^s+1`, `63·2^s+1` for every s (`Proth3`, `Proth15`, `ProthCore.proth63`). Infinitely many
  non-ET-coverable families: `15·b^s+1` (`b ≡ 2 mod L`), fixed-base-2 `c_J·2^s+d_J` (`PROOF_S_WILD.md` §3).
* **Good-word cores at fixed offset +1 (restricted exponents, not full families).** `(4^m−1)2^s+1` has good words, hence
  (S)/ES, on a core progression of exponents with square-unit closure (no finite ET/divisor cover) and on a density-one set
  in each fixed exponent progression, for 2 ≤ m ≤ 131, m = 365 (certificates) and h = 2m−1 = 4^i+1 (i ≥ 1) or 2^{12t+6}+13
  (t ≥ 0) (hand proofs; Lean `proth_four_pow_core`: ES on positive multiples of a period depending on i — neither density
  nor noncovering is formalised). For h = 7^i an explicit progression of y gives good words at `(2^{h+1}−1)y³+1` ≡ 1 (840).
  PROVED (`notes/z78/PROTH_ALLM.md`, `WILD_ES.md` §1). Open: the core for arbitrary m; all exponents for m > 10.

### D. Structure and obstruction theorems (what a proof has to beat)
* **Brauer–Manin and open-surface exponent dichotomy.** On (★) and Type II models, positive-integral BM is empty iff n is
  a square (`Z58_STRUCT*.md`, 4545 non-BM; sterile fibres Y_{p,c} down to `c = ⌊√n⌋`, `DISPROOF_DEEP.md`). On coordinate
  opens S_n°, X_n°, U_n° (kernel s ≠ 1 for k = 4, s ∉ {1, 2} for k = 8), fixed-exponent Brauer and étale-Brauer tests on
  outer-integral positive adeles fail to obstruct (`DISPROOF_OBSTRUCT.md`, `DISPROOF_KUMMER.md`, FRONTIER §3), whereas
  unbounded 2-power-conductor characters at one prime detect existence (`DISPROOF_OBSTRUCT.md`, `DISPROOF_DEEP.md` §3).
* **Finite procedures fail at trap points** (method barrier). This covers coverings, polynomial menus, and finite oracle
  programs with a finite formal tree at the trap: PROVED (`Z53_NONCRTLOGIC.md`); prime failures CONDITIONAL on Schinzel H.
  Unconditional (z74, Opus-reviewed) for polynomial whole-triple menus in Gaussian + any fixed number of *integral*
  negative-Pell witnesses: miss relative density one of primes ≡ 1 (M), 840 | M (`GAUSSIAN_PELL_MENU.md`). Sterile Mordell
  points on the r-generic line exist for every prime **r ≥ 293** (PROVED, computer-assisted rel. BBR 2012 Thm 1.2; r ≥ 919: SE/ZL/z77
  incl. inherited libm rows; [293, 919): integer/rational ledger and tails using the reduction, z76/z77 lemmas and round-1
  integer inputs; `notes/z78/R17_PUSH.md` §§7–10, two Opus replays).
* **Witness sizes are not polylog.** For fixed κ < 1/12, or κ < 1/6 with Gallagher or GRH, infinitely many p have no
  forest edge with larger endpoint in [4, exp((log p)^κ)]. Only {1,2} and {2,3} remain. This refutes Conjecture H₂.
  PROVED rel. the internal energy lemma; `H4_NOT_POLYLOG.md`. Both Type II witness moduli are ≥ the least quadratic
  non-residue at p ≡ 1 (4) (`Z57_BFII.md`).
* **All seven ET period searches can be superpolylog (z78, Opus-reviewed).** For each large prime f ≡ 3 (4) some prime p > f
  has seven-chart ET minimum H_ES(p) = f; infinitely often all seven Type I/II period searches exceed exp((log p)^κ),
  κ < 1/8 (PNT) or κ < 1/4 (Gallagher, or GRH). PROVED rel. ET, mean-value and internal energy/transfer inputs; 192 panel
  minima CERTIFIED; no such bound on every coordinate or search grammar (`notes/z78/WILD_ES.md` §6).
* **Function fields:** ES_q(T) has no finite linear covering for q = 3^r, r ≥ 2 ((J)51, (J)56, (J)67). **q = 3, A = T²
  (z78):** both designated slice points x*_c are uncovered (former Conjecture 0.2), so no finite linear covering. PROVED rel.
  the tuple/parity and minimum-level reductions and Mason–Stothers (`notes/z78/F3_CONJ.md`; Opus reviewed §§1–5, then §§6–7
  with dependencies; `F3Endpoint.lean` checks only the large-level §6 algebra under its hypotheses). CERTIFIED separately:
  brute force N = 4..15, filtered census to N = 38. Not a result for A = T or integer ES.
* **Numerator blindness:** M^□ is a theorem for every M ≡ 0 (4), while 8/n fails at n = 131 and 241 ((J)41, FRONTIER §1).
  A proof needs a 4-specific input.

### E. Logic: weak arithmetic does not prove ES (PROVED, internal; nonstandard countermodels)
In each model a nonstandard prime fails ES. The models are *separate* unless stated, so do not combine their axiom lists.
Every item has had one cross-lab review: z64–z65 Claude work by Astra, and z73–z78 Astra work by Opus
(`data/z74/xreview/`, `notes/z75/*REVIEW*`, `data/z75/ie1/`, `data/z76/`, `data/z77/`, `data/z78/xreview/`).
* **Normal open induction** (+ gcd, irreducible divisors, and all true universal ring sentences) does not prove ES on any
  class of 𝔐; IOpen proves it on every other class mod 840 (`Z64_UNPROV.md`; + T1 and two squares: `Z65_LOGIC2.md`).
* **IOpen + Bézout** does not prove ES (`Z73_OPEN_BEZOUT.md`, `LOGIC_BEZOUT.md`); a separate model adds full collection,
  PD and TS (`LOGIC_BEZOUT_NORM_COLLECTION.md`). Prime-tail dichotomy with Dirichlet: `Z73_ES_ROW_DESCENT.md`.
* **External IOpen PIDs (all satisfy unary L(D), `IE1_ES.md`; no nonstandard one satisfies IE₁, `IE1_BREAK.md`):**
  * Interval PIDs: per unit-square class, failing primes in every infinite interval with Bertrand + Dirichlet (`Z73_PID_SQUARE.md`, `LOGIC_PID_{INTERVAL,DIRICHLET}_AUDIT.md`).
  * **Unified QR + TS + Lag + Dirichlet + L(D) PID (z76, Opus-reviewed):** internal Dirichlet, Lagrange, L(D), **full internal prime QR** (both supplements, two squareclasses) and **universal TS** fail ES at P ≡ 1 (840) (`notes/z76/QR_TS_BCM.md`).
  * Separate full-QR + Dirichlet + Lag + L(D) PID where **P alone** fails least-nonresidue search (`notes/z76/IE1_BREAK.md`).
* **IOpen + Bézout + BCM + Lagrange (four squares) + full internal prime QR + universal TS ⊬ ES (z78, Opus-reviewed):**
  one countable model (recursive rotation repair of the z76 twisted dyadic-axis tower; both supplements, exactly two nonzero
  squareclasses modulo each odd prime, two squares at every prime ≡ 1 (4)) with P ≡ 1 (840) failing ES (`notes/z78/IE1_UNITS.md` §§1–3,
  strengthening `notes/z76/QR_TS_BCM.md`; not an external PID; fails `L(Div)`).
* **Variable-radicand Pell-window induction (z75–z76, Opus-reviewed):** parameter-free W₂ fails in the z74 PID, 5-square BCM
  and collection models (`IE1_ES.md`), but a separate rank-one normal `IOpen + Lag` model has ¬ES(P), negative Pell at P,
  full variable-radicand supplied-unit Pell windows and filtered least Pell-coordinate search with polynomial congruences at
  arbitrary fixed moduli (`notes/z75/IE1_PUSH2.md`, `notes/z76/IE1_BREAK.md`; not PID/Bézout/IE₁).
* **Window models (z78, Opus-reviewed; none satisfies IE₁⁻):** three separate normal `IOpen + Lag + PW` models fail ES — the
  multiquadratic-height model misses the cubic norm window C₃; the all-standard-balanced-norm model misses Ell(y² = x³ − 2);
  the third fills those norms and that elliptic window but misses Ell(y² = x³ − 36x). Separately, over any countable PA base
  a normal `IOpen + Lag` end extension has a fresh ES-failing prime with the specified pointed height windows and misses the
  √2 window (`notes/z78/IE1_UNITS.md` §§4–9, 13, 15; BARRIER-BROAD entry in FRONTIER §3).
* **Not claimed:** independence from IE₁, IE₁⁻, IΔ₀, PA or ZFC; a standard counterexample; BCM in a PID (see FRONTIER §3
  for the nonstandard external-PID barrier on IE₁ and IE₁⁻ ES countermodels).

### F. Certified computations (exact, finite; engines and ranges are in the cited files)
* (★) holds at all 355,096,166 primes in 𝔐 ∩ (10¹⁰, 3·10¹¹] (`Z58_SUMMARY.md` §3).
* The non-square zeros of R in 𝔐 up to 10¹² are exactly 9 primes and 18 composites, largest 17,401,609 (one engine;
  `Z59_MSPLUS.md`). **(MS⁺₁₀₅)** (non-square n ≡ 1 (4), gcd(n, 105) = 1, n > 29,210,401) certified to **10¹¹** (z58 LOGIC
  ≤ 10¹⁰ + two engines on (10¹⁰, 10¹¹]; `notes/z75/DISPROOF_PUSH2.md`).
* Odd non-square zeros up to **2·10¹⁰** (two engines in (10¹⁰, 2·10¹⁰], `notes/z75/DISPROOF_PUSH2.md`; earlier ≤ 10¹⁰ in
  `Z58_WILDCARD.md`, `Z59_SUMMARY.md`, `Z60_LOPEZ.md`): N_II only 4545; U_II only {105, 4545}; U₇ only the 8 composites of Z₇
  (105-multiples also checked to 5·10¹⁰).
* Among primes p ≡ 1 (4) up to **2·10¹¹**, the b = 1 line (López Type A) fails only at 193, 2521 and 66529 (two engines;
  `B1_LINE.md`, `notes/z75/DISPROOF_PUSH2.md`).
* **R₈ (C-even (★)) threshold floor:** 11 certified prime zeros across all classes in z75–z76 raise the in-𝔐 floor to
  **1,590,284,203,561** (R = 52; full 8/p passes; four checkers incl. cross-lab; earlier floors 1,511,088,831,001,
  1,218,367,081,201, 452,438,542,081; `notes/z75/DISPROOF_OBSTRUCT.md`, `DISPROOF_PUSH2.md`, `notes/z76/DISPROOF_COMP.md`).

## 2. Current open targets (statements whose proof would matter)
Ranked by the campaign (Assessment). Definitions are in the cited files.
1. **(MS-U₇)**: U₇(p) for 𝔐-primes p > 10¹⁷. **(MS⁺₁₀₅)**: R(n) ≥ 1 for non-square n ≡ 1 (4), (n, 105) = 1,
   n > 29,210,401 (certified to 10¹¹). Cleanest sufficient single-sentence targets. (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II)
   (`Z57_SYNTH.md`, `Z59_MSPLUS.md`, `Z60_LOPEZ.md` §4.2, `Z60_SUMMARY.md` §5).
2. **H⁻_BM:** R(p) ≥ ε·M_BM(p) for large p (FRONTIER §2.4). Also conjecture **(S)** (`Z63_EUCLID.md`), now PROVED for all
   non-square n ≡ 1 (4) outside the exact **24 odd-square classes mod 840** (`notes/z75/CONJS_GEN.md` Thm 2, Opus-reviewed).
3. **Structure / U₇ / class groups:** Conjectures B and C in `Z68_U7F.md`; `Z70_CLASS.md` open list (Rédei 4-rank,
   small-split-prime orbits, solution-graph moves).
4. **Logic:** IE₁, IE₁⁻, IΔ₀ and IΔ₀ + exp remain open (no nonstandard external IOpen PID satisfies IE₁, and if ES holds
   in ℕ any IE₁⁻ ES countermodel is non-PID with a nonstandard PA cut and J ≠ 0, `IE1_BREAK.md` §4; above a PA cut IE₁⁻
   forces parameter-free bounded-existential windows with true base and successor step to be witnessed — multiquadratic
   `H(A*) = Γ⁰[G]`, norm windows of standard number-field orders, elliptic duplication windows — and end extensions cannot
   repair an old bounded miss, `IE1_NONPID.md` §4, `notes/z78/IE1_UNITS.md` §§4–15; the no-lock fair-chain route stays
   open); `L(Div)` in a BCM+TS ES-countermodel; Bézout+IW₂.
5. **Coverings:** all-depth sterility for the primes 17 ≤ r ≤ 283 (each fails the current sufficient bound), above all r = 17. CERTIFIED: 5 and its
   inverse survive all seven families through depth 11 (not all-depth; `notes/z78/R17_PUSH.md` §6). At r = 17, x = 5, PROVED:
   a P hit with 17^L ≥ 10⁶ needs e ≤ 466(rN)^{1/4}; ineffectively finitely many hit levels per fixed square class of de (P)
   or d (Q); CONDITIONAL on abc: for each θ < 1/4 no sufficiently deep P hit has de ≤ N^θ (`notes/z78/R17_ENDPOINT.md`
   §§2–4). F₃[T] Conj. 0.2 is closed (§1D).
6. **Analytic sub-problems:** FRONTIER §7 (e.g. θ > 3/4 on E(N), cancellation on the height-dependent modular hyperbola,
   pushing e*(n) below L_R[1/2], R(n) from the once-reviewed 46/145 toward 3/10).

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
