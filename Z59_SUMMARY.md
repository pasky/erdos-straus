# Z59_SUMMARY — wave z59 "pursue the z58 survivors": five math lanes + papers housekeeping, no lead, sharper targets

**ES is OPEN; (MS), (MS⁺), (MS-II) and CONV-II are open.** Everything here is internal and unrefereed. Wave z59 (brief
`z52bbriefs/z59_lanes.md`) ran six lanes on the z58 survivors: CONV2 (Opus, structured: what the full Type II family buys),
CONVO (Opus, tryhard, unprimed: Type II at primes p ≡ 1 (24)), WALDS (Opus, structured: the cusp / Waldspurger residue left
by z58 TERNARY), MSPLUS (Opus, structured: the primality-free target (MS⁺)), MSPF (Fable, tryhard: pointwise (★) on 𝔐),
and PAPERS (housekeeping: K-R-K priority sweep and z58-vs-paper consistency, `data/z59/papers/CHANGES.md`). Memos
`Z59_<LANE>.md`; cross-model reviews `data/z59/xreview/REVIEW_<LANE>.md`. **All five cross-model verdicts were
ACCEPT-WITH-FIXES; the fixes were applied and not re-reviewed.** Each memo's own statement governs; scopes below are short.

Notation as in `Z58_SUMMARY.md`: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^×;
R₈ = C-even half of (★); N_II(n) = #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc}; (MS): R(p) ≥ 1 for primes p > 10¹⁷ in 𝔐.
New: **U := (c = 1) ∪ (a = 1)** (the (★) line and López's "Type A" line of Type II); 𝒞₁(2N) = integers that are units and
squares at every prime of 2N (⊇ 𝔐 for levels with odd primes in {3, 5, 7}).

## 0. Bottom line

* **No HOT LEAD. No lane found a mechanism forcing R(p) ≥ 1, U(p) ≥ 1 or N_II(p) ≥ 1 at a single large prime. B2 (the
  tied-modulus divisor event at one integer) did not move.** Verdicts: CONV2 "narrowed + sharper target"; WALDS "narrowed";
  MSPLUS "narrowed / strengthened (target choice)"; CONVO "NOT PROVED, no hot lead"; MSPF "not a hot lead". The two
  unprimed tryhard lanes (CONVO, MSPF) mostly rederived prior repository results (reviews give the attribution maps).
* **Sharper targets (CONJECTURE; statements, not mechanisms).**
  * **CONJECTURE U** (CONV2): every odd non-square n ∉ {105, 4545} has U(n) ≥ 1. Equivalently (Lemma 1(iii), PROVED): some
    Tn + 1 has a divisor ≡ −1 (mod L_T), L_T = T if 4 | T, else 4T — **one one-parameter line**. CERTIFIED to 10¹⁰. At
    primes it is López's Conjecture 1 (prior). U ⟹ CONV-II; (MS) ⟹ (MS-U) ⟹ (MS-II). U asks for more than CONV-II; that
    it is *harder to prove* is not claimed. In the certified range the full family beyond U is needed only at n = 105.
  * **(MS⁺₁₀₅)** (MSPLUS): R(n) ≥ 1 for non-square n ≡ 1 (4), gcd(n, 105) = 1, n > 29 210 401 (all classes); and
    **(R⁺_y)**, y ≥ 47: non-square n ≡ 1 (4) > 8 813 281 with all prime factors > y. Both CERTIFIED to 10¹⁰ (z58 LOGIC
    census). (MS⁺₁₀₅) is strictly stronger than (MS⁺); "as good a target" is an Assessment.
* **Scoped no-gos (PROVED in their scopes; none is a necessity theorem for every proof).**
  * WALDS Thm W1 (rel. Waldspurger 1981 Prop 1 / Cor 2, Shimura T(ℓ²), TERNARY Thm F): for a one-nebentypus ternary-theta
    proxy vanishing at odd squares, a Shimura eigensystem φ contributes on squarefree 𝒞₁ only if its Gaussian twist
    G_φ = φ ⊗ ψχ₋₄ has L(G_φ, ½) = 0; then at most one line (given an L-non-zero anchor or (H2)). Lemma W0: termwise
    recipe lattices represent nothing in 𝒞₁. Prop W5: for an effective proxy, validity ⟺ (MS) on its class.
  * CONV2: on a shared integer the c = 1 / a = 1 events are nested within one coordinate system (Prop 3.1); all c-line
    events on 4mn + 1 lie in the greatest event E_{r(m)} (Prop 4.2; incomparable c *can* rescue each other); equation-scaling
    transports (inheritance, numerator ladder, ET dilation) give no descent into a prime (Prop 4.1).
  * MSPLUS Thm 1: the leading class mean of R is (𝔖_Q(a)/8)log²X, Jacobi-blind (𝔐 not special at leading order); R₈ has
    exactly half (Remark 2.3). Lemma 4.1: no positive-density twisted-T1 family s·m² for (★).
* **New certified data:** (MS⁺) to **10¹²** (no zero; one engine); U to 10¹⁰ (zeros 105, 4545); U⁽⁸⁾ to 10⁸ (819 zeros);
  min-ρ ≤ 107 for all primes p ≡ 1 (24) ≤ 10⁸; a 24-level exact half-integral-weight sweep with validity certificates;
  13 explicit 𝒞₁-primes (six in 𝔐) where a single-twist central value provably vanishes (§3).
* **Papers:** K-R-K priority sweep applied to eight notes, two false "first since 1970" / "new for every m ≠ 4" claims
  removed, one BM overstatement fixed (§4). Nothing posted.

## 1. Per-lane table

Labels after review fixes. All verdicts ACCEPT-WITH-FIXES, fixes applied, not re-reviewed.

| Lane | Tried | Proved / certified (labelled, scoped) | Killed (scoped) | Survives |
|---|---|---|---|---|
| CONV2 | What c ≥ 2, d etc. buy at one p; joint failure of c = 1 and a = 1; inheritance / ladder across c | PROVED: Lemma 1 (one-line forms; U = single profile line L_T; full family = line m ↦ E(4mn + 1, 4m/r(m))); Prop 2.1 (tie relaxes from 4m to ≥ 2√(4m); τ(u) integers per modulus 4u vs min(2, τ(u)) for U, 1 for (★)); Prop 2.2 (U has Mordell's complete moduli 3, 7, 15; (★) only 3 among f ≤ 15 — explains exactly the 5 (★)-zero primes outside 𝔐); Props 3.1, 4.1, 4.2. CERTIFIED: U-zeros ≤ 10¹⁰ = {105, 4545}; U⁽⁸⁾ 819 zeros ≤ 10⁸ | rescue on a shared integer is one-directional (one coordinate system); fixed finite (T, f) menus fail on a congruence class; equation-scaling transports into primes | CONJECTURE U / (MS-U); adaptive or growing arguments across integers; non-monomial transports. Z57_BFII Thm G is genus-only; "τ(u) independent trials" is heuristic |
| CONVO | Unprimed: Type II at p ≡ 1 (24) via ρ = 4abd − p | PROVED (mostly prior: Z57_BFII, Z58_CONVF, JOINT_BUDGET): Criterion 3.1 (∃ j: (p+3)/4 + j has divisors a, b, ab \| it, a + b ≡ 0 mod 4j + 3); Identity 3.2 / Lemma 3.3 (character expansion; square cancellation); Lemma 4.1 (global colouring λ_ρ(ℓ) = (ℓ/p)); Lemmas 5.1–5.2. CONDITIONAL (Dickson suffices) Thm 7.7: no uniform bound on witnessing ρ — exact prior result DISPROOF_AVENUES §3 Prop 3.1. CERTIFIED: min ρ ≤ 107 for p ≡ 1 (24) ≤ 10⁸ | "escape ⇒ solution" (one-character implication) refuted by 4545 and by p = 8 803 369; fixed (a, b) menus, S-supported ab | other bounded-order character arguments; congruence arguments (p ≡ 73 mod 168 forces ρ = 7); §7 are failed attempts, not barriers |
| WALDS | Cusp / Waldspurger residue of TERNARY on 𝒞₁ ⊇ 𝔐 | PROVED: Thm W1, Cor W2, Lemma W1′ (anchor or (H2)), Prop W4 ((a), (d) need only Cor 2; (b), (c) need (H2) for every contributing φ), Prop W5, Lemma W0; Remark W3 (sign constant on 𝒞₁; needs (H2), else CONDITIONAL on (W-loc)). CERTIFIED: sweep of 24 levels L \| 3360, 121 (L, ψ) pairs; non-zero 𝒞₁-kernel at 15 pairs; with R-zero rows rank 0 in all 15. PROVED: L(G_φ ⊗ χ_p, ½) = 0 at 13 𝒞₁-primes (six in 𝔐: 1009, 1129, 1201, 1801, 4201, 4729) | single-eigensystem positivity *everywhere* on the class (explicit zeros); termwise recipe lattices on 𝒞₁; at each swept (L, ψ), every valid proxy vanishes on 𝒞₁ ∩ [1, B] | (E-a) many-φ levels with a validity identity; (E-b) coset thetas; (E-c) mixed ψ; (E-d) higher weight; (E-e) off-𝒞₁ / p-dependent levels (= B2). Eventual single-line effectiveness is open; false under a residue-class CKRS refinement (CONJECTURE) |
| MSPLUS | Primality-free (MS⁺): dead moduli, local means, zero law, targets | PROVED: Lemma 2.0 (hit d coprime to n); Thm 1 (σ_q = 1 + 1/q² if q ∤ a, 1 − 1/q + 1/q² if q \| a; 2-adic factor 1); Cor 1.1 (each odd q \| n multiplies the leading constant by (q² − q + 1)/(q² + 1)); Remark 2.3; Lemmas 4.1, 5.1. CERTIFIED: (MS⁺) census (10¹¹, 10¹²]; OOS census of four dead-moduli classes on [10¹⁰, 10¹¹]; exact R to 10⁹. EVIDENCE: zero law P(R = 0) ≈ e^{−0.3·m(n)} | means mechanism cannot separate R from R₈ (Assessment); unconditional product / divisor / q²-scaling closures of R ≥ 1 fail (CERTIFIED examples). Prop 2.2 (second-order class mean) **WITHDRAWN** — now only a proxy (Def 2.2) | (MS⁺), (MS⁺₁₀₅), (R⁺₄₇); the excess of 𝔐-prime zeros at 10⁶–10⁷ (≈ 6× the law, unexplained); genuine second-order term |
| MSPF | Tryhard: pointwise (★) on non-square n ∈ 𝔐 | PROVED (mostly prior: Z56_FAMTRY, Z57_SYNTH, Z58_WITNESS): Lemmas 1.1–1.8 — four bijections; (−k/d) = −1; every hit modulus has χ_n(d) = −1, so d ≥ q₁(n) ≥ 11 on 𝔐; (B/n) = −(k/n); R(n) even; Lemma 1.8: for every D, infinitely many non-square n in every 𝔐-class have no witness d ≤ D (d > (1/2 − ε)log n i.o.). CERTIFIED: 𝔐-prime census ≤ 10⁷ | bounded witness menus, fixed-modulus selectors, class-wide identities (Lemma 1.8; incremental over prior) | §3 routes are attempt records (each stops at "some n + k has a divisor ≡ −1 mod 4k"); a congruence + global non-square argument is not excluded |
| PAPERS | K-R-K sweep; z58 vs papers | see §4 | — | (D)30/(D)31-type claims kept only relative to K-R-K's *stated* theorems |

## 2. Falsifier lessons across lanes

| Lane / idea | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros |
|---|---|---|---|---|
| CONV2, U-line | every odd prime factor of Tm² + 1 lies in ker χ_{−T}, which misses −1 (PROVED) | U⁽⁸⁾: 819 odd non-square zeros ≤ 10⁸ (61 primes, last 3 869 153) | U-zeros ≤ 10¹⁰: {105, 4545}, both divisible by 15 | all 14 (★)-zero primes rescued by a = 1 (T = 2, 5, 6); 193, 2521, 66529 by (★) (T = 8, 44, 8) |
| CONVO, ρ-criterion | all residues in ker λ_ρ for coprime squares; Lemma 2.1 for the rest | full d-even family survives the 12 R₈-zeros (witnesses with c ≥ 2); its c = 1 sub-line fails; 15 vs 22 reconciled (all odd primes) | 284/285 have witnesses; 4545 none — refutes "escape ⇒ solution" | all 14 and all 38 𝔊*-zeros have full witnesses (min ρ ≤ 23) |
| WALDS, cusp proxies | **W1: T1 pins a(1) = 0; Waldspurger carries it to the square class** | all negative statements line-blind | 15/285 in 𝔐, all squarefree; enter like primes | survivors non-zero at 5569, 9601, 23929 or 1969, 2641, 5161 ⟹ invalid |
| MSPLUS, means / zero law | **square-blind** (Thm 1) — cannot be a proof route alone | identical dead-moduli structure for R₈ (half mean); R₈ zero rate ≈ 5× the R-law near 10¹⁰ | 214/285 in g3/g15/g21/g105, 51 in g5/g7/g35, 20 coprime to 105 | model under-predicts 𝔐-prime zeros at 10⁶–10⁷ ≈ 6× |
| MSPF, witness constraints | Lemma 1.3 / Cor 1.4; χ_n principal iff square | R_even = 0 at 186 𝔐-primes ≤ 10⁷ (last 9 965 881), R_odd = 0 at 118 (last 9 744 001) | 285 recomputed (15 in 𝔐) + 8 725 201, 12 538 801, 17 401 609 | 14 ⊂ 38; 11 of the 20 in-𝔐 𝔊*-zeros have R > 0 |

**Lessons** (Assessment unless labelled).
1. **T1 is always a kernel statement, and each lane rediscovered it in its own coordinates** (ker χ_{−T}, ker λ_ρ, (−k/d) = −1,
   a(1) = 0 of every Shimura component). WALDS shows it is *stronger* on the half-integral side than z58 knew: it kills
   every non-Gauss-exceptional eigensystem on squarefree 𝒞₁, not only the Eisenstein part. Conversely, MSPLUS proves the
   leading mean is square-blind: any mean/density mechanism must get its non-square input elsewhere.
2. **The composite screen for Type II is now one line deep.** U (two coordinate lines) fails only at 105, 4545 ≤ 10¹⁰;
   the full family only at 4545. 4545 also kills CONVO's one-character escape implication.
3. **Numerator 8 bites every line-level statement.** U⁽⁸⁾ has prime zeros to 3 869 153; R₈ shares MSPLUS's dead-moduli
   structure exactly; neither C-parity alone suffices for 𝔐-primes ≤ 10⁷ (MSPF). Full d-even Type II survives the 12
   R₈-zero primes only through c ≥ 2 (CONVO, CERTIFIED).
4. **Keep 𝔊* and R apart.** All 14 (★)-zero primes are among the 38 𝔊*-zeros; the other 24 have R > 0 (CONVO, MSPF, WALDS,
   MSPLUS, independently re-witnessed). 𝔊*-zeros obstruct the subfamily, not R-targets.
5. **Every pointwise attempt stops at B2** in lane-specific clothes: one line Tp + 1 (CONV2); residues mod ρ of the prime
   factors of (p + ρ)/4 (CONVO); "some n + k has a divisor ≡ −1 (mod 4k)" (MSPF); p-dependent levels (WALDS (E-e));
   "untouched" (MSPLUS).
6. **Fixed finite menus fail again** (CONV2 §3, CONVO Lemmas 5.1–5.2, MSPF Lemma 1.8, WALDS (E-e)); all prior in
   substance (Z56_FAMTRY Prop 2.2, Z57_BFII Prop 3.2, Z58_WITNESS). Unprimed lanes cost rediscovery, not novelty.

## 3. New certified data

"One engine" = one production engine; independent coverage listed. None of the large interval censuses was fully rerun by a
second engine beyond the stated ranges.

* **(MS⁺) census to 10¹² (MSPLUS §6; CERTIFIED, one engine = z58 LADDER exact decider, unchanged).** No zero among the
  1 046 544 177 primes and 5 381 870 962 non-square composites n ∈ (10¹¹, 10¹²] with n mod 840 ∈ 𝔐 (total 6 428 415 139 =
  raw 6 428 571 430 − 156 291 odd squares; 18 chunks, all exit 0). Largest least-hit modulus 1 470 759 at
  n = 475 715 523 361 (R = 12). Cross-review: all chunks reconciled, an independent-engine slice, the extremal input.
  **So the non-square R-zeros on 𝔐 up to 10¹² are exactly the 9 primes and 18 composites ending at 17 401 609.**
* **U census (CONV2 §5; CERTIFIED).** Odd non-squares ≤ 10¹⁰: U-zeros exactly 105 and 4545 (n ≡ 3 (4) by Lemma 1(vii)).
  Engine `scripts/z59_conv2_lines.c` (bitmap + exact fallback). Independent: cross-review direct-progression census to
  10⁹ (exactly {105, 4545}); internal review reran to 10⁸, [10⁹, 1.01·10⁹) and 300 random n ∈ [10⁹, 10¹⁰). Above 10⁹ one
  engine (re-executed by the reviewer, same algorithm). Prime U-zeros ≤ 10¹¹: none — inherited from B1_LINE's a = 1 census,
  not recomputed. Small counts (n ≡ 1 (4) ≤ 10⁵): c = 1 / a = 1 / U / full = 99 / 35 / 2 / 1 zeros.
* **U⁽⁸⁾ (CONV2; CERTIFIED ≤ 10⁸, independently reproduced zero by zero).** 819 odd non-square zeros: n ≡ 1 (4): 547
  (45 primes, last 3 869 153; 502 composites, last 89 530 945); n ≡ 3 (4): 272 (16 primes, last 1 226 891; 256 composites,
  last 93 398 595). All 11 366 (K = 4) and 215 858 (K = 8) LATE certificates re-verified.
* **T-mask table (CONV2 §3; EVIDENCE reading of CERTIFIED counts, ≤ 10⁷):** restricting the a = 1 part to T mod 4 ∈ {1, 2}
  gives 6 zeros, {2, 3} 9, {1, 3} 18, {2} 24, {3} 66, {1} 63 (full U: 2). No single class carries the rescue.
* **Minimal ρ (CONVO §6; CERTIFIED, independently reproduced with a different algorithm).** All 719 781 primes
  p ≡ 1 (24) ≤ 10⁸ have a working ρ ≤ 107; records 73→7, 1129→11, 1201→23, 21169→31, 67369→35, 87481→63, 1430641→71,
  8803369→107. Least-non-residue census p ≤ 2·10⁵: 30 complete absences of a solution with q | ab (e.g. 2521, q = 11).
* **Half-integral-weight sweep (WALDS §5; CERTIFIED exact ranks, pari; EVIDENCE identification).** M_{3/2}(Γ₀(L), ψ) at 24
  levels L | 3360, 121 (L, ψ) pairs, B = 10⁴ / 8000 / 16 000; 123 comparisons (118 full-space + 5 cusp-space), 121 match the
  Gauss-exceptional prediction; the 2 full-space runs (840, χ₁₀₅), (840, χ₈₄₀) at B = 8000 have rank 5 on 𝒞₁ (rank 1 in
  the cusp space at B = 16 000). With R-zero rows added: rank 0 in all 15 survivor runs ⟹ every valid proxy of each swept
  (L, ψ) vanishes on 𝒞₁ ∩ [1, B] — full space, except L = 840, ψ ∈ {1, χ₈, χ₂₁} (TERNARY class only); χ₁₀₅, χ₈₄₀ full
  space to B = 8000 only. Cross-review reproduced matrices with an independent implementation.
* **Single-twist zeros (WALDS §6.1).** PROVED unconditionally (two independent points via `ellrank` + Gross–Zagier–Kolyvagin):
  13 𝒞₁-primes, six in 𝔐. CONDITIONAL (L-value reading of exact coefficients): 57 of 238 primes of 𝒞₁(84) ≤ 4·10⁴ (36 in 𝔐)
  at (168, χ₁₆₈); 54 of 238 of 𝒞₁(280) (28 in 𝔐) at (560, χ₂₈₀).
* **Other (CERTIFIED).** MSPLUS: exact R for all n ≡ 1 (4) ≤ 10⁹ (class means); OOS zeros on [10¹⁰, 10¹¹]: 9 / 4 / 4 / 1 for
  105 | n, 15 | n 7 ∤ n, 21 | n 5 ∤ n, 3 | n only (all 18 confirmed by a second divisor-based engine); 460 000 structured-search
  lines (sm2, deadsq, dead, msq, semi; 10¹¹ < n < 4·10¹⁸) all with verified witness, least hit modulus ≤ 211 403;
  twist data s·m² ≤ 10¹⁰ (≤ 3 zeros per s). MSPF: 20 513 𝔐-primes ≤ 10⁷ (R, R_odd, R_even, d_min, q₁, R_prime, k_min) —
  reproduced byte-for-byte by an independent enumerator; R_prime = 0 at 136 (last 9 831 889); d_min = q₁ for 22.6 %;
  max q₁ = 53, max d_min = 64 255, k_min up to 410 (p = 4 160 641).
* **Targets table (MSPLUS §5.3, from z58 LOGIC census to 10¹⁰).** Non-square zeros n ≡ 1 (4) ≤ 10¹⁰: (MS) primes in 𝔐 9
  (last 8 813 281); (MS⁺) 27 (last 17 401 609); (MS⁺₁₀₅) 38 (last 29 210 401); (R⁺₁₁) 30, (R⁺₄₃) 21 (last 17 401 609);
  (R⁺₄₇) 19 (last 8 813 281); 3 ≤ y < 7 last 7 479 950 569; all non-squares 500 (last 9 919 520 121).

## 4. Papers (PAPERS lane, `data/z59/papers/CHANGES.md`; deep-subagent fidelity review applied)

* **K-R-K sweep.** Every note mentioning the 3/4 exponent now cites K-R-K (same bibitem; "unrefereed as far as known"),
  with "claimed earlier", no priority claim, and "shares this architecture but differs in its details" (independence is not
  documented). Edited: `es-threequarter-note` (+ archived v1), `es-mn-short-note`, `espaper`, `sieve-limits-note`,
  `es-subexp-note`, `vaughan-loglog-note`, `es-count-note` (LIT's qualified citation). The 3/4 note states the verified date
  ordering (K-R-K PDF 2026-07-29; campaign repository first commit 2026-08-16).
* **False claims removed.** `es-mn-short-note`: "no 3/4-type bound for m ≠ 4" / "Theorem A new for every m ≠ 4" (K-R-K Thm 2
  has fixed m ≥ 4); now only short-interval/progression forms, uniformity in m, Cor D, Thms U, L′ are claimed new relative
  to PW, Elsholtz and K-R-K's *stated* theorems. `espaper`: two "first exponent improvement since 1970" sentences and all
  "record" wording for 3/4.
* **z58 consistency.** `es-automorphic-barrier-note` Prop `prop:brauer`(b) overstated "BM never removes a Type II level":
  restricted to p ∤ d (levels with p | d are empty and obstructed by the STRUCT2 class). Akaka bib → v0.8 (pinpoints v0.7).
  Pomerance–Weingartner → *Ramanujan J.* 69 (2026), art. 31 in six notes. Other notes checked, no contradiction.

## 5. Open problems supported by the memos (none is a lead)

1. **CONJECTURE U / (MS-U)** (CONV2): a fixed-p argument for the single line T ↦ E(Tp + 1, L_T) suffices for (MS-II). The
   rescue is spread over all T mod 4 classes (mask table); adaptive/growing families are not excluded.
2. **(MS⁺), (MS⁺₁₀₅), (R⁺₄₇)** (MSPLUS; CONJECTURE). A proof of (MS) transfers to (R⁺_y) only if every use of primality
   follows from non-squareness plus the fixed-y exclusion (fixed-y roughness does not give gcd(n, u) = 1:
   n = 9 553 913 = 1093·8741 has witness (1093, 2186, 1)). Descents allowed by (MS⁺) would have to be non-scaling.
3. **Zero-law questions** (MSPLUS; EVIDENCE): the genuine second-order class mean (Prop 2.2 withdrawn); the ≈ 6× excess of
   𝔐-prime zeros at 10⁶–10⁷; the systematic ≈ 1.4× under-prediction in later decades.
4. **WALDS escapes (E-a)–(E-e)**: many-φ levels with a validity identity not reducible to validity at large primes; coset
   thetas; mixed-ψ signed combinations; higher half-integral weight; off-𝒞₁ / p-dependent levels (= B2 / n_p wall).
5. **CONVO**: an input controlling the residues mod ρ of the individual prime factors of (p + ρ)/4 beyond the quadratic
   colouring; growth of min ρ (Thm 7.7, CONDITIONAL: unbounded; EVIDENCE: ≤ 107 to 10⁸).
6. **MSPF**: prime-only or single-C-parity witness statements need thresholds above 10⁷ (counts decay, not to 0; EVIDENCE).
7. **Papers**: the analytic K-R-K proof is still not audited; finer comparison of the remaining campaign-new claims.

## 6. Caveats / do-not-export

* **ES, (MS), (MS⁺), (MS⁺₁₀₅), (R⁺_y), U, (MS-U), CONV-II and (MS-II) are open.** No lane supplies a HOT LEAD; "sharper
  target" is about statements. Do not call U "harder" or "easier" than CONV-II.
* **Finite data stay finite.** (MS⁺) to 10¹² and U above 10⁹ are one-engine censuses (spot/slice checks only). Prime U to
  10¹¹ is inherited (B1_LINE), not recomputed. Fitted laws (zero law, OOS, tail expectations) are EVIDENCE; the OOS test had
  no pre-set criterion and is **not a passed test**; finiteness of zeros is a property of the model under a uniform
  exponential-law assumption (Assessment), never a bound.
* **Withdrawn:** MSPLUS Prop 2.2 as a class-mean expansion (wrong already at Q = 4: true linear coefficient (3γ − 1)/4); c₁
  is a proxy covariate only. Mordell classes differ from other unit classes at O(log X) (PROVED), size not derived.
* **WALDS scope.** Ternary-theta class, one ψ (W0: any ψ, non-negative combinations). W1′ needs an L-non-zero anchor or (H2);
  W4(b)/(c) need (H2) for every contributing φ; W3 needs (H2) else CONDITIONAL on (W-loc). Certificates are finite (B ≤
  16 000), per (L, ψ), with the ambient space stated in §3; identification with Gauss-exceptional φ is EVIDENCE (box search,
  rational φ only). The 13 L-zeros refute only the *everywhere* version; eventual non-vanishing is unproved; its failure
  needs a residue-class CKRS refinement not stated in CKRS (CONJECTURE). "GRH does not give it" and "the cusp residue is
  heuristically worse than (MS)" are Assessments. W5 is a reformulation, not a circularity theorem.
* **CONV2 scope.** Prop 3.1 is per coordinate system and shared integer (counterexample to a stronger reading: n = 193,
  T = 8); Prop 4.1 covers equation-scaling (rational diagonal) transports only; Prop 2.2 gives positivity on its local
  classes; the count-heuristic reading and the whole-family correlation (0.483–0.548, Z57_COMPLEMENT) are EVIDENCE.
* **CONVO / MSPF are largely rederivations** (attribution maps in their memos / reviews). CONVO Thm 7.7 is prior
  (DISPROOF_AVENUES §3 Prop 3.1) and CONDITIONAL; CONVO §7 and MSPF §3 record failed attempts, not barriers; 4545 refutes
  only the one-character escape implication; Lemmas 5.1–5.2 / 1.8 exclude only finite fixed menus, fixed-modulus selectors
  and class-wide identities.
* **Literature.** K-R-K unrefereed; public priority unverified; do not call the campaign's 3/4 bound first.
* **Nothing has been posted.** Papers are internal artifacts; posting needs the user.
