# BREADTH_Z45 — nine new branches screened for ES (2026-10-19)

**ES is not solved, here or anywhere.** This wave sent nine independent deep explorers into branches that keyword
coverage showed the campaign had *not* touched. Each wrote one memo `BRAINSTORM/z45_<slug>.md`, with scripts in
`scripts/z45_*` and data in `data/z45_*`. All nine memos received one hostile review (`reviews/z45-breadth-review.md`,
GPT Astra, deep). The reviewer found no fatal errors and three minor corrections; the repairs are marked "R-z45 repair".
Labels follow DISCOVERIES.md.

## 1. Outcome table

| slug | branch | verdict | promise (post-review) | retained value |
|---|---|---|---|---|
| etale_descent | anabelian / étale π₁, integral descent, étale-Brauer on U_n | PARTIAL (obstruction side) | 2 | **PROVED:** π₁(U_n)=π₁(Ũ_n)=1 geometrically, while π₁ of the smooth locus is ℤ/2 with the explicit universal cover Y_d : 4dABC = n(A+B+C), (x,y,z)=(dBC,dAC,dAB), d = squareclass of xyz. Ordinary étale-Brauer adds nothing. **CERTIFIED:** at 3361 all 15 solutions (12 squareclasses) need twists ramified outside 2n. So "integral covering coordinates" is a false obstruction; only the image is integral. Open: compute Br(Y_d) with image-integrality. |
| critical_chaos | Harper-type critical multiplicative chaos, lower-tail models | PARTIAL | 1 (was 2) | **PROVED in the model:** the BM multiplicative field has bounded variance, not critical-chaos variance, and its zero probability is ≍ const × Poisson. "Critical ⟹ infinitely many failures" is unsupported. Summability criterion for zero laws (with the R-z45 boundary repair). |
| interlacing_stable | MSS interlacing families, real-stable / Lee–Yang | PARTIAL | 1 | All signings of the forest F_p share one characteristic polynomial (trivial switching equivalence on trees), so spectra cannot see certificates. Divisor-class projection destroys stability, with exact counterexamples at 1097 and at 2521 (`z²+z⁴`). |
| prime_t1_dual | dual certificates / "prime T1" from real failures | PARTIAL | 1 | **CERTIFIED:** at 8/131 only 6 of 33 complete fibres admit a kernel-character obstruction; the other 27 fail on exponent budget. Real sibling failures are mostly *budget* (lottery) failures, not character failures. T1's characters are not projectively compatible. New notion: an overflow distance δ, where δ=∞ is a character obstruction and δ>0 is a missing exponent budget. |
| euler_systems | Euler / Kolyvagin systems, Iwasawa towers | PARTIAL | 1 | **PROVED:** certificate levels have finite support at fixed p, so a faithful norm-compatible "certificate detector" vanishes identically. The remaining loopholes are annihilating Euler operators and non-faithful extraction. |
| siegel_dichotomy | pretentious / Siegel-zero two-worlds proof shape | PARTIAL | 1 | **CERTIFIED:** at p=31121, q=43 the divisor-ratio box has 37 of 42 residues but misses −1, although every odd character clears the separation threshold. This refutes the single-character inverse criterion. Scan of all p≡1 (4) up to 10⁷. |
| program_synthesis | machine discovery: DSL / evolutionary search for growing witness procedures | PARTIAL | 1 | A search over 924 programs found nothing better than a plain forest-parent scan. That scan succeeds on all 82 887 primes p≡1 (24) up to 10⁷ within 2(log p)² operations (CERTIFIED to 10⁶, EVIDENCE to 10⁷). Conjecture H₄(p) ≪ (log p)². CF-derived procedures did worse. |
| transfer_logic | ultraproducts, Ax–Kochen, nonstandard p, Kolmogorov complexity | PARTIAL | 1 | **PROVED:** for monic no-cancellation ES_q at fixed degree, the success proportion is O_d(q^{−k}). For quadratic P, the solvable P lie on five explicit coefficient curves. So in the large-q limit **successes are structured and failures generic**, and the function-field limit cannot be interchanged with ES. **PROVED (standard coding):** an ES-exception of bit length L has K(p\|L) ≤ L − cL^{2/3}. That is compression, not structure. |
| recent_pointwise_tools | 2019–26 pointwise factorisation tools (Pasten/Shimura heights, BHV/Zsigmondy, Koymans–Pagano, Smith, Green–Sawhney, …) | PARTIAL | 1 | **PROVED:** the literal Pasten embedding is sterile (4Cp+1=a²+1 forces C=pk², and then every divisor is ≡1 mod 4). **BHV** is the only external *pointwise* theorem found that forces a divisor into a tied class: a primitive divisor ℓ of a Lucas sequence of discriminant p at rank t that is inert has ℓ ≡ −1 (mod t). But ℓ is not forced to divide tp+1 (analogy already in TORSION_FIRING.md and y3_lucas_dickson_trace). |

## 2. Cross-cutting reading (Assessment)

1. **B2 again, now from nine more directions (22 fields in total with B2_ACROSS_FIELDS).** Each memo, independently,
   ended at the same step: the residue class of a divisor of one prescribed integer, in a modulus tied to the
   solution, at a single p, with polylog count. No branch supplies class-sensitive control of the factors of a
   *prescribed* integer. That is now the most robust negative finding of the campaign.
2. **Pointwise ≠ class-sensitive.** Modern pointwise factorisation theorems (Pasten, Stewart–Yu) control sizes.
   Primitive-divisor theorems control classes, but only for divisors of *their own* sequence term. ES needs both
   at once, on a side integer the theorem did not choose. This "intersection problem" is the cleanest new
   formulation of what is missing.
3. **Failures look like lotteries, not obstructions.** The disproof-side probes agree on this. Real sibling failures
   are mostly exponent-budget failures (prime_t1_dual). The large-q function-field limit has generic failures and
   structured successes (transfer_logic). Integral descent has no obstruction beyond BM on the singular or resolved
   surface (etale_descent). The chaos model gives Poisson-like zero laws. So a structured ("prime T1") disproof
   looks unlikely; a disproof would have to be a finite-search accident above 10¹⁷.
4. **Longitudinal lesson.** ES-type statements hold when the height or degree is free to grow (integers, function
   fields with growing degree). They fail generically when the degree is frozen and q grows. Any proof must exploit
   the growth of the admissible heights with p, not a fixed geometric fibre. This explains why Weil-type single-fibre
   mechanisms prove only the *mute* (cap-relaxed) variants.

## 3. Candidate new theories surfaced (each with its first testable toy case)

| theory | core object | first test | source memo |
|---|---|---|---|
| Twist-decomposed integral descent | the family Y_d with image-integrality; Br(Y_d) and its evaluation on positive adeles | compute Br(Y_d) and check the 8/131, 8/241 controls | etale_descent §5 |
| Overflow-distance theory | δ = distance from the available divisor residues (under the exponent budget) to the target −1 | finite-box δ ≤ 1 on composite non-squares that fail Type II | prime_t1_dual §5 |
| Primitive-divisor intersection theory | the set of primitive divisors of Lucas(P, (P²−p)/4) at rank t that divide tp+1 and are inert | statistics of intersections vs t; is there a forcing at any t? | recent_pointwise_tools §5 |
| Group-algebra-valued stability | generating polynomials with coefficients in ℂ[(ℤ/MZ)^*], keeping all residue sectors | classify C₂ (done); C₄ toy | interlacing_stable §5 |
| Arithmetic exposure trees | reveal prime-power residues level by level; inverse-moment bounds on class occupancy | growing-order inverse-moment bound beyond the BM-only toy (solved) | critical_chaos §5 |
| Forest-endpoint bound H₄ | least larger endpoint of a bichromatic edge of F_p | adversarial square-mimicking primes against H₄ ≪ (log p)² | program_synthesis §5 |

## 4. Recommended next steps (ranked by value × tractability; Assessment)

1. **Br(Y_d) with image-integrality** (obstruction side; concrete algebraic geometry). It is the only computation left
   in the étale/descent hierarchy, it closes or opens the last "exotic integral obstruction" door for a disproof,
   and the 8/131 and 8/241 controls make it falsifiable.
2. **Primitive-divisor intersection problem.** Lucas sequences are the one known pointwise source of the class −1
   mod a tied modulus. Tabulate, at hard primes, how often the inert primitive divisor of rank t divides tp+1, and
   look for any structural coupling (TORSION_FIRING.md §≈235 has the earlier analogy).
3. **δ ≤ 1 finite-box statement.** It is cheap, falsifiable, and gives a graded notion between "BM-allowed" and
   "certificate", which FRONTIER §7 item 3 asks for.
4. Adversarial falsification of H₄(p) ≪ (log p)² (compare X_win: a_min ≪ log p, FRONTIER §5.5; is H₄ just a restatement?).
5. **Group-algebra-valued stability** — parked. Keeping all residue sectors in ℂ[(ℤ/MZ)^*] is keeping all
   characters; the failure is at extraction of the target sector, and no invariant that survives extraction is
   proposed, so there is nothing concrete to test. M moves with the solution (a family of group algebras = B2).
   The only working toy (C₂) is the quadratic layer, already known to be free ((J)103).
6. **Arithmetic exposure trees** — modelling only. The required growing-order inverse-moment bound at one fixed p
   restates H⁻_BM; the solved toy is the BM (quadratic) layer. Use it to calibrate disproof probability, not as a
   proof route.

Low priority (each closed in its displayed form): spectral/interlacing, faithful Euler systems, the Siegel
dichotomy, ultraproduct transfer, and larger program-synthesis runs.

## 5. Depth follow-ups on steps 1–4 (z46; hostile review `reviews/z46-depth-review.md`, no fatal errors)

| step | document | outcome |
|---|---|---|
| 1 | `BRAUER_TWISTS.md` | **COLLAPSES (as an obstruction route; a successful obstruction-side result).** **PROVED:** Br(Y_d)/Br ℚ ≅ ℤ/2, or (ℤ/2)² exactly when n/(md) is a square. The extra class changes by the pulled-back base class under the deck involution, so negating the covering coordinates over the same positive real image cancels its pairing. Hence the finite étale–Brauer / descent set with image-integrality is nonempty for every n ≥ 2. It is also nonempty at the controls 8/131 and 8/241 and at all 32 numerator-15 failures, so it explains none of them. The surviving but unoccupied twist 4/3361, d = 1 shows that adelic survival is not sufficient. Scope (R-z46): X = U∖{0}, finite-place image integrality, real-image positivity; log or positive-dimensional descent and other open models are not computed. |
| 2 | `PRIMITIVE_INTERSECTION.md` | **PARTIAL, 1/5.** **PROVED:** conditional on the certificate support being nonempty, the unrestricted traces obey an exact CRT product law. **CERTIFIED:** (PI) fails at 94 primes < 10⁶ (58 of them Mordell-hard) even with unlimited traces and levels, so prime-only certificates lose more than (★). Regular rational traces cannot force support for 4 \| t > 4. Per R-z46 this no-go is narrow: proper-factor selection and growing algebraic traces are not excluded. Missing: force the support to be nonempty, which is B2. |
| 3 | `OVERFLOW_DISTANCE.md` | **PARTIAL, 1/5.** **PROVED:** δ is not a renamed cap. At (2113, 43), δ = 1 while the same-window square-denominator cap is ∞. **CERTIFIED:** min δ = 0 for all 9 732 eligible primes ≤ 10⁶ and 1 000 samples < 10⁸. Among composites, 47 have min δ = 1 and 6 have min δ = 2. The tested numerator-8 failures (11, 17, 131, 241) and the 27 budget-obstructed numerator-15 failures all have min δ = 1. So the real sibling failures sit at distance one. No δ ≤ 1 ⟹ δ = 0 transport exists, and none can be numerator-uniform. |
| 4 | `FOREST_H4.md` | **PARTIAL, 1/5.** **PROVED:** r(p) ≤ H₄, a_min ≤ 2H₄ − 1, and H₄ ≤ h(p) for almost all p whenever h → ∞. For every H, infinitely many primes have a_min = 3, λ = 2 and H₄ > H, so H₄ is distinct from the existing minima. **CERTIFIED:** 517 362 adversarial primes have max H₄/(log p)² = 1.61 (p = 1 002 125 860 849, H₄ = 1231, r = 31). Caveat (R-z46): the random hunt silently dropped draws that exhausted the 10⁶ endpoint cap, so its aggregate maximum is not certified; fix before rerunning. Residual event: an opposite-coloured candidate parent v must actually divide ⌈p/v⌉ + 1, which is B2. |

**Reading (Assessment).** Step 1 closes the finite descent–Brauer hierarchy: no structured obstruction of that kind exists at any n ≥ 2, so a disproof via descent of this kind is ruled out. Steps 2–4 each produce a clean new invariant (trace support, overflow distance δ, endpoint height H₄) with exact laws *conditional on support*. Each stops at the same unconditional step: forcing one prescribed integer to have a divisor in the tied class. The most informative new fact is that all real sibling failures sit at δ = 1, exactly one exponent step from success. A theorem of the shape "δ ≤ 1 at every level with a forced window ⟹ δ = 0 at some level", provable for numerator 4 and failing for 8, would be the next rung, but no mechanism for it is known.

## 6. Third wave (z47 + board #3, 2026-10-19)

* **H₄ hunt fixed (`FOREST_H4.md` §"R-z46 follow-up").** The scanner now counts draws that exhaust the endpoint cap as
  CENSORED. Rerun: zero censored draws in 4 521 959 prime evaluations. **CERTIFIED:** max H₄/(log p)² = 1.6121
  (p = 1 002 125 860 849, H₄ = 1231). The conjecture H₄ ≪ (log p)² survives the adversarial hunt.
* **δ-transport (`DELTA_TRANSPORT.md`, PARTIAL 1/5).** **PROVED:** a numerator-4 distance-one witness that overflows
  at the prime 2 with quotient a = (u+v)/m = 1 folds explicitly to a zero-distance window m′ = v < m. This
  dyadic step is automatic for 4 (b ≥ 1 ⟹ 4 | u) but needs an extra 2-adic bit for 8. That bit is missing at the
  8/131 source (u = 4, v = 9, m = 13; K′ = 35/2). Example: 4/409 = 1/105 + 1/4090 + 1/85890 (window 31 → 11). For
  a > 1, folding solves an instead of n and cannot descend. **CERTIFIED:** over p ≡ 1 (24), p ≤ 10⁴, the folding and
  re-splitting moves reach δ = 0 from 296 of 2 166 distance-one windows. 35 of the 143 primes have no move edge.
  This is a genuine 4-vs-8 separation in one dyadic face, not a global transport.
* **Board #3: sidestep B2 (`~/.pi/boards/20261019-es-sidestep/memo.md`; fable, astra, argon; 17 items + 3 forks,
  4 rounds).** Unanimous: **no proposal sidesteps B2.** Every item died in one of four ways: a re-indexing, a
  parity count whose even total includes zero, a false lemma, or a rewriting walk whose exits are B2 windows.
  Retained:
  1. A **q = 3 pivot spine on U_{3p}**. Because 4 − 3 = 1, the seed (p, 4p, 12p) has an unconditional 3-step spine.
     Its depth-4 exits are the ET windows q = 4e₁ + 3 with e₁ \| ((p+3)/4)², i.e. x = (p+3)/4 + e₁. These are
     standard windows, so the note is explanatory.
     **Q3 (CONJECTURE):** pivot components of p·U₃ in U_{3p} always reach (3ℕ)³. EVIDENCE: 83 Mordell-hard
     p < 3·10⁴ and 27 adversarial primes up to 4.4·10⁵. Q3 implies ES(p).
  2. **Trapped components (CERTIFIED by 3 independent implementations).** ES(p) holds, yet the q = 2 pivot component
     and the 4-particle collision graph are closed and miss every target. This happens for 21 primes < 10⁵
     (1321, 6121, 8641, 12241, 14281, …), sometimes with composite side numbers (14281: (p+1)/2 = 37·193).
     So fixed-q positive rewriting (q = 2, and q = 5 at 76 of 83 tested primes) is not universal.
  3. **Parity-loophole closure.** Pairing the sterile part leaves an even certifying count, which may be zero, so
     parity cannot certify existence. The square detector also fails (d₁(9) = d₁(49) = 2).
  The board does *not* claim B2 is necessary for ES. All three seats converged that the missing object is a
  **propagation law** (one exception ⟹ many, cf. AMPLIFY_EXCEPTION.md criteria) or a **single global object
  whose positivity is proved without counting**. None was produced.
