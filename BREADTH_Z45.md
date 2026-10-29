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
* **Q3 refuted (`Q3_PIVOT.md`).** **CERTIFIED:** at p = 7 909 441 and 8 604 961 the union of q = 3 pivot components
  through p·U₃ is closed: 57 and 76 vertices, and no member has all three denominators divisible by 3. Two
  implementations in Q3_PIVOT agree, and the parent re-verified with a third, from-scratch BFS
  (`/tmp/q3chk/chk.py`, not kept), which also reaches targets at 1321 and 409. ES holds at both primes, which lie
  below the verified bound 10¹⁷. Fixed-q pivot rewriting is therefore non-universal for q = 2, 3 and 5 (q = 5:
  board #3 data). Correction to the board: some spine exits are Type I, not exclusively Type II.

## 7. Board #4: propagation laws / non-counting global positivity (`~/.pi/boards/20261019-es-propagation/memo.md`)

There were 14 items, tagged (P) for a propagation law and (G) for a global object, with seats fable, astra and
argon, over 3 rounds. **No route survives.** Every (P) law fails in one of two ways. Either it is already ES(p) at
every tested prime: AMPLIFY Thm 2.4 descent, where every Mordell-forced source coordinate in {a, b, a ± b} is
known soluble at 273/273 Mordell-hard p < 10⁵. Or it is gated by a witness-level divisor event. Every (G) object
either restates ES or lands only through a divisor event. Retained as documentation only:
* external-2 odd-t dyadic folding, which extends DELTA_TRANSPORT's move graph from 99 to 131 of 143 primes;
  its targets are existing a = 1 Type II certificates;
* Lemma D, checked on 1 096 solutions: a mixed solution of 4/p² through a window m ≡ 3 (mod 4) with p ∤ m
  requires (p/m) = −1;
* a 4-vertex trapped U_{3p} component through (2p, 2p, 3p) at 1321, 6121, 12241 and 14281 (vertices re-checked
  by the parent at 1321).
Formally open but unconstructed, and championed by no seat: astra-1 (norm-diagonal descent through a non-ET-form
step) and astra-2 (integral Y–Δ network reduction). The dissent (astra) stands: the failed constructions do not
show that B2 is *necessary*. The open crux, which no seat could settle: is there a rule Λ, uniform over an
infinite family of prime pairs (q, p), with Λ(W(q)) ⊆ W(p) whose validity is not a congruence or divisor condition
on the witness? Cheapest verdict-changing experiment: one non-ET-form step from the witnesses at the coordinates
of m² = a² + b² that produces a mixed or scaled solution at an odd square.

## 8. Board #4 follow-ups (2026-10-21)

* **Closure slate written (`PROPAGATION_CLOSURE.md`; addenda in DELTA_TRANSPORT.md and Q3_PIVOT.md; FRONTIER §6 dead
  ends updated).** Every board count was independently re-verified. **PROVED:** Lemma D (Jacobi obstruction),
  checked on all 1 096 mixed solutions.
* **Verdict-changing experiment (`NONET_STEP.md`; PARTIAL, 1/5).** The square-survival condition is met: a non-ET
  "ratio transplant" step reads the reduced ratio r:s of two denominators of a coordinate witness and outputs
  (X, Hr, Hs) with X = (n+3)/4 and H = n(n+3)(r+s)/(12rs), rejecting when H is not an integer. **PROVED example:**
  from (4, 68, 510) ∈ W₄(15) at 289 = 15² + 8² it gives 4/289 = 1/73 + 1/7446 + 1/126582. This is a mixed solution,
  not scaled from 4/17 (parent re-checked). The same step at 3361 recovers the known solution (841, 3361·290,
  3361·8410). **CERTIFIED:** the full grammar reaches 536 of 542 primes but fails completely at six, including 2521
  and 9601. So the (P) descent shape is not killed by T1, but it is not a law: the source witness only proposes a
  ratio, and the integrality of H is a divisor event, B2 again. With this, the board's drop-condition is resolved
  and direction (P) is closed for the campaign, except for a genuinely norm-compatible forcing theorem (open; no
  candidate).

## 9. Relative-hardness map (`HARDNESS_MAP.md`, 2026-10-21)

The map has 19 arrows. Most are repo-known or folklore and are consolidated with exact scope. New arrows:
* **A5 (PROVED, crisp).** QNR-SEARCH ≤ ES-PRIME-SEARCH: one oracle call, deterministic polynomial time, no
  factoring. In every solution of 4/p (p ≡ 1 mod 4), exactly two denominators have equal p-adic valuation, and
  the product of their p-free parts is a quadratic non-residue mod p. So a deterministic polynomial-time ES
  solver at primes would solve deterministic QNR finding, which is open without GRH. The parent re-checked the
  identity independently on all 8 334 solutions of 4/p, p ≡ 1 (4), p < 3000: zero violations, and always exactly
  one equal-valuation pair.
* **A2/A3 (PROVED).** Reduced witness parameters a, b, c ≤ f(p) imply r(p) ≤ f(p). Polylog-height *denominators*
  are impossible: max denominator ≥ p(p+1)/4 for Type I and > p^{3/2}/2 for Type II. So "polylog ES" must mean
  reduced-parameter height.
* **A4 (PROVED, rel. Graham–Ringrose / Lau–Wu Prop 5.1).** For infinitely many Mordell-hard primes, every reduced
  witness parameter, H₄ and the largest prime factor of every p-free denominator are ≥ c·log p·log log log p.
  O(log p) witness bounds are therefore false unconditionally.
* **A15 (PROVED implication).** Elliott–Halberstam ⟹ two fixed mute primes suffice. This applies to the mute
  relaxation only.
Pruning corollaries: an efficient constructive proof of ES derandomises QNR finding. A small-parameter proof proves
least-QNR bounds of the same size. A finite-menu proof refutes Schinzel H / Dickson. A two-sided count contradicts
Linnik. Not implied, either way: no arrow from QNR bounds back to ES, none from any relaxation to ES, and none
between ES and Sierpiński 5/n or three cubes. An equivalence to a named open problem was not found.

## 10. External: the OpenAI math release (`OAI_DUMP_IMPACT.md`, 2026-10-21)

`github.com/openai/math` (2026-10-06) contains 719 unrefereed AI manuscripts. Nothing in it is on Erdős–Straus.
**CLAIMED and Lean-formalized:** quasi-RH, i.e. every Dirichlet L-function is zero-free for Re s > 7/8, with a
uniform Siegel-zero exclusion. *If accepted*, these become unconditional:
* least QNR r(p) ≪ (log p)⁸ (parent re-derived the exponent: 1/(1−θ) with smoothing), hence deterministic QNR
  finding in P, so HARDNESS_MAP A5 loses its hardness content;
* the exponent cap e*(n) ≪ log⁸ n effectively (previously GRH-conditional (16 log n + 70)²);
* M_BM(p) ∼ (3/(2π²))(log p)² (previously GRH-only);
* M_gen ≥ log₂p − log₃p − O(1);
* effective versions of the ineffective Thm U and the moving-window bound.
Family 029's technical propositions (Artin; not formalized) would make the one-fixed-mute-prime relaxation
unconditional. **None of this touches B2, and ES remains open.** GRH itself is not known to imply ES, and the
memo confirms that every transfer still fails checklist lines 4, 8, 9, 12 and 17.

## 11. Local contribution drafts for plasma-ai/erdos (erdosproblems.ai), 2026-10-27; NOT submitted

These are local clones and branches only; nothing is pushed.
* **PR A OPENED 2026-10-28: https://github.com/plasma-ai/erdos/pull/65** (fork pasky/erdos, branch es242-claim-audits, squashed onto upstream main 17c86a0d4). Local: `~/projects/math/plasma-erdos-prA` (branch `es242-claim-audits`; text in `plasma-erdos-prA.PR.md`). It rejects
  the three claimed full proofs (Alomari, Dyachenko, Bradford) as "proof defective; statement unresolved", with
  defects checked against the PDFs. Dyachenko's Lemma 9.24 is false (g = 1 gives the orbit {(j, j)} ≠ ℤ²).
  E0242 becomes open / none.
* `~/projects/math/plasma-erdos-prB` (branch `es242-research-map`; issue and PR texts in `plasma-erdos-prB.*.md`).
  It adds the research map `wiki/research/erdos_242/` (main note, two supplements, 35-check evidence) plus three
  Lean claims, with kernel-only proofs and 0 compiler axioms; the audit passes. Placeholder IDs:
  * L9901: 8/n is not a sum of three unit fractions for n = 11, 17, 131, 241;
  * L9902: the exact first-denominator divisor test;
  * L9903: 4abcd ≠ a + b + m²c for all positive a, b, c, d, with no gcd or parity conditions.
* Reviews, 2026-10-28; files in `~/projects/math/review*-pr{A,B}*.md`:
  * Round 1, three fresh-context GPT-6 Astra reviews: PR A NEEDS FIXES (wording), PR B BLOCKING. The blocking
    items were M(49) ≠ 0 without coprimality, the Type I (c,d) row needing gcd(p, cd) = 1, the B2 family, the
    forest→ES bridge (now explicit five-slot certificate formulas) and overbroad barrier wording. All were fixed.
  * Round 2, two Claude Fable reviews: PR A OK. They also found that Dyachenko's Prop 9.25 is false as stated
    (g = 9, b′ = 1, c′ = 2). PR B NEEDS FIXES: the B2 moduli for constant rows and minor wording; fixed.
  * The Lean claims were refactored into named parts. Re-audited: 3833 constants, 7 claims, 0 compiler axioms, PASS.

## 12. Follow-ups once plasma-ai/erdos#65 (PR A) shows how the project responds

* **F4: post sharp sub-problems where agents work** (TheoremDB, erdosproblems.ai): the one-sided bound (∗), forest
  height H₄ / certificate-edge existence, δ-transport (δ ≤ 1 ⟹ δ = 0 for numerator 4, failing for 8), and
  cancellation on the height-dependent modular hyperbola. Goal: draw outside compute onto B2.
* **F5: public screening kit for claimed proofs.** A script plus the Lean claims (L9901 numerator-8 controls,
  L9903 no Type II at squares) that tests a claimed construction against 8/11, 8/17, 8/131, 8/241, odd squares
  and fixed-congruence coverage (B1). This replaces the long barrier map as PR B's core. The two theorems (3/4
  exceptional set; exponential families) go as a separate PR.

## 13. Wave z48: dump methods, long single-target attempts, forest connectivity (2026-10-28)

Eight side agents ran (Claude Fable, GPT-6 Astra, Claude Opus). All merged; ES remains open.
* **Methods of the OpenAI release** (all promise ≤ 1/5 for ES):
  * `OAI_METHOD_003.md`: quasi-RH comes from a cubic-theta reflection/Poisson recursion on special sextic
    families plus an amplified zero detector. It is not a generic large-sieve gain, and no B2 transfer was found.
  * `OAI_METHOD_007.md`: two-point Chowla, read conditionally on 007's proof, gives only an O(p) implied constant for
    Σ λ(4pC+1)λ(C), trivial at ES scales. The lost factor is identified (progression density).
  * `OAI_METHOD_142.md`: the derandomisation either uses positive-density Chebotarev events or finds objects that
    exist a priori; ES has no such object. Clean negative (0/5).
* **Forest** (`FOREST_DEEP_ASTRA.md`, `FOREST_DEEP_FABLE.md`, `FOREST_CONNECTIVITY.md`):
  * PROVED, three times independently by elementary reciprocity: for p ≡ 1 (mod 4), an edge is a certificate
    ⟺ it is bichromatic, for every edge (10 M edges checked). So ES₅(p) ⟺ the forest has a bichromatic edge.
  * Connectivity routes fail: comp(1) and comp(r(p)) fail i.o. under Dickson. At 59929 and 4962049 no vertex ≤ 12
    has a certifying child. The first certificate usually hangs off an unrelated root.
  * Exact remaining gap (Fable): some v < w ≤ (log p)^C with w | p + v, w ≡ −p (mod v) and opposite colours. That is
    B2 verbatim, with the colour layer removed. Promise 1/5.
* **Lower tail** (`LOWERTAIL_DEEP_ASTRA.md`, `LOWERTAIL_DEEP_FABLE.md`):
  * **CONDITIONAL positive (Astra Thm 5.4):** any fixed Dirichlet zero-free strip (OAI-003 or GRH) ⟹
    M_gen(p) ≥ (2/π⁴ − o(1)) log²p. This settles FRONTIER §7 item 4 conditionally; previously GRH gave only
    log log p. It is a statement about the main term, not R(p).
  * **CERTIFIED:** R + B ≥ M_BM/16 for all p ≡ 1 (mod 4) ≤ 10⁷.
  * Fable: an independent (★) census to 10⁹ finds exactly the 14 known failures.
  * **Conjecture I3** (Fable): a sign-free, prime-free model of the blocking step. I3(n) counts words tuv − u − v = n
    with t, u, v ≥ 3; it has main term ½ log²n. CERTIFIED to 10⁹: I3(n) = 0 at exactly 112 integers, the last being
    2 433 600 = 1560². No method gives I3(n) ≥ 1 for large n. This is the cleanest public sub-problem candidate (F4).
  * Remaining gap (Astra): one-sided control of the non-real character remainder at a single p. Neither GRH nor a
    zero-free strip supplies a signed zero correlation at that p.

## 14. Wave z49: rounds 2–3 of the long single-target attempts (2026-10-28/29)

Eight long attempts and six cross-model reviews were run. The attempts were three lanes (forest, I3, lower tail),
each worked by both Fable and Astra, plus two round-3 follow-ups. Every claim below survived a hostile review by the
other model family (`reviews/z49-*`). ES remains open. **No lane produced a positive mechanism for a fixed prime.**
The durable gain is recalibration: one campaign conjecture is refuted, and it is now known exactly which shape a
witness theorem can have.

* **Calibration (parent session; `data/z49_main/`).**
  * CERTIFIED: among n ≡ 1 (mod 4), n ≤ 10⁹, the sign-free two-line union U(n) fails exactly at the odd squares and
    at six non-squares: 105, 2961, 3985, 25305, 111969, 978145. Here U(n) means some v ∈ 4ℤ ∪ (8ℤ − n) has a divisor
    of n+v that is ≡ −1 (mod v). U holds at every prime p ≡ 1 (mod 4) up to 10⁹.
  * EVIDENCE: a 10⁹-sample prime-Haar simulation, validated against 2·10⁶ real primes near 10¹², gives
    −ln P(H₄ ≥ X) ≈ 0.32 (ln X)².
* **H₄ is not polylogarithmic** (`H4_NOT_POLYLOG.md`, Astra; Opus review SOUND, twice).
  * PROVED, relative to the internal energy lemma (OMEGA10/11): infinitely many primes p ≡ 1 (mod 840) have no forest
    edge with larger endpoint in [4, exp((log p)^κ)], and also have A_min(p) > exp((log p)^κ).
  * The range of κ depends on the analytic input: κ < 1/12 effective (Montgomery–Vaughan I), κ < 1/6 relative to
    Gallagher's theorem, and κ < 1/6 under GRH.
  * This **refutes Conjecture H₂** (H₄ ≪ log²p) and the z48 "colour-free gap" with both endpoints polylog. It also
    shows that Fable's covering form needs moduli beyond every polylog.
  * Untouched: bounds on a single coordinate (u_min, the least López vertex, HC below, H_(★)). Those events are
    Landau-type, not congruences.
* **Conjecture S in the prime-Haar model** (`CONJECTURE_S_MODEL.md`, Opus; Astra review SOUND-AFTER-REPAIRS, minors).
  * PROVED: −log δ(H) ≥ c(log H)². The proof conditions on small-prime coordinates, then applies an atomic Janson
    inequality and the fundamental lemma.
  * Consequence for actual primes: for each fixed large H, the density of primes with H₄(p) > H is
    ≤ exp(−c log²H). This replaces the (log H)^{−1/2} of FOREST_H4 Thm 3.5.
  * The matching side, −log δ(H) ≤ C L² polylog (which would be Conjecture S in the model), is CONDITIONAL on a new
    first-term equidistribution hypothesis FT_β. The bound with L³ is conditional on FT; unconditionally L⁶ log L
    stands.
  * Conditional on FT, κ < 1/3 would follow in the theorem above. Heuristically the truth is κ → 1/2.
* **Conjecture I3, analytic side** (`I3_DEEP_ASTRA.md`, Astra; Opus review SOUND).
  * PROVED: for the all-integer Haar survival of "no interior word with both endpoints ≤ H", with L = log H,
    c L²/(log L)² ≤ −log δ₃(H) ≤ C L⁶/log L.
  * PROVED: integers with no such word for H = exp((log x)^κ), κ ≤ 1/6, exist in every large dyadic range.
  * PROVED: #{n ≤ N : I3(n) = 0} ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3}), a Vaughan-type exponent for I3. This is
    not an ES exceptional-set theorem.
* **Conjecture I3, local theory** (`I3_DEEP_FABLE.md`, Fable; Astra review SOUND-AFTER-REPAIRS; the reviewer found
  two extra coverings).
  * PROVED: the exact (t, u) cell table at squares, the square depletion ½, and the depletion at km².
  * Explained: 1560² is an even square with 2³·3·5·13 | m. The model's expected number of zeros beyond it is 0.16.
    Zeros cluster at m², 2m² and highly divisible n.
  * PROVED, computer-assisted: I3 ≥ 1 on 2^k ± 1, 2^k ± 3, 7·2^k − 1, 5·2^k − 1 and 3·2^k + 1, by
    Sierpiński-type exponent coverings.
  * PROVED: the class-free count is ≥ (1/(72 log 2) − o(1)) log²n at every n. So I3 is exactly its restriction to a
    single class.
* **Lower tail, reformulation** (`LOWERTAIL_ROUND2_FABLE.md`, Fable; Astra review SOUND-AFTER-REPAIRS).
  * PROVED, and parent-verified on 136k words: for n ≡ 1 (mod 4), (uv/n) = −1 iff some coordinate t, u, v lies in
    𝒞_n = 4ℤ ∪ (8ℤ − n). So ES₅ is a character-free covering by six single-coordinate residue lines. This is a
    packaging of Theorems A/B, not a new mechanism.
  * PROVED by exact computation: the 160 shape-cell counts satisfy no linear identity beyond u ↔ v.
  * HC(p), the least 𝒞-coordinate over all words of p:
    - CERTIFIED: HC(p) ≤ 64 for p ≤ 10⁸;
    - PROVED: HC(p) = 4 for all but O(x/log²x) primes p ≡ 1 (mod 8);
    - CONDITIONAL on Dickson: HC is unbounded;
    - CONJECTURE (candidate): HC(p) ≪ (log p)^A.
* **Forest inverse problem** (`FOREST_INVERSE.md`, Fable; Astra review SOUND): no mechanism found.
  * Retained: Theorem E′ (Jacobi form of Theorem E), a complete classification of polynomial words in two free
    factors, and the result that no fixed modulus has a converse to E′.
* **Lower tail, analytic** (`LOWERTAIL_ROUND2_ASTRA.md`, Astra; Opus review: correct, but **no new proof step**).
  * Retained: an all-alphabet zero envelope (a corollary of the sterile-point theorem), sparse-insertion stability
    (T1 in sequence language), and the second-order H⁻crit threshold.
* **Exact remaining gap after z49.** For a prime p ≡ 1 (mod 8), some word of p must have a coordinate in 𝒞_p. The
  witness can be small in one coordinate only; in any two-coordinate or modulus form it must exceed exp((log p)^κ)
  infinitely often. So a proof must control a Landau-type event at a single integer, such as "p + u has a divisor
  ≡ −p (mod u) for some small u ∈ 𝒞_p", among growingly many shifts. This is B2 with all character and sign layers
  removed.
