# z52b lane `fingerprint` — data fingerprinting of Erdős–Straus-derived sequences

ES is OPEN. Nothing here proves or disproves it. This lane is breadth-first: items were filtered only for obvious
nonsense; no barrier-checklist evaluation was done.

{{SUMMARY}}

## Method
* Computed (scripts `scripts/z52b_fingerprint_*`, raw data `data/z52b/raw/`, large word table git-ignored):
  - exact solution counts for 4/n = 1/x+1/y+1/z (x ≤ y ≤ z) for **all n ≤ 30 000** and **all primes ≤ 2·10⁵**:
    U (unordered), D (distinct), O (ordered), min max-denominator, largest/smallest x, number of distinct x,
    k₁/k₂ = number of solutions with exactly one/two denominators divisible by n, least common denominator
    (`z52b_fingerprint_count.c`);
  - the same for m/n with **m = 5..48 at all primes ≤ 10⁵** and m = 5..13 at all n ≤ 4000;
  - a word sieve n = tuv − u − v for **all n ≤ 3·10⁶**: all words W, I3 (t,u,v ≥ 3), the (★) count R (t ∈ 4ℤ), the
    U-certificate count Uv, and "some coordinate in 4ℤ ∪ (8ℤ − n)" ESC (`z52b_fingerprint_words.c`); reproduces the
    campaign's 114 I3 zeros (max 2 433 600), the 12 R-zeros ≤ 3·10⁶ and the six U failures ≤ 10⁶;
  - ~50 classical invariants at the ≈ 9 000 primes p ≡ 1 (4), 100 < p < 2·10⁵ (class numbers h(−4p), h(−8p), h(−3p),
    h(p), regulator, L(1,χ_p), L(1,χ_{−4p}), CF period of √p, least QNR, least primitive root, ord_p 2, Legendre
    symbols, a_p of 11a1/37a1/32a1, Ramanujan τ, divisor functions of p±k, smoothness of p−1) via cypari2, with
    Spearman correlations against residuals of log(count+1) after regressing on log p, log log p
    (`z52b_fingerprint_classical.py`, output `data/z52b/classical_corr.{json,txt}`), and truncated-Euler-product fits
    (`z52b_fingerprint_lfit.py`, `data/z52b/lfit.json`);
  - ≈ 260 OEIS lookups of the sequences and transforms (records, positions, parities, differences, zero sets), cached in
    `data/z52b/oeis_cache.json`, results `data/z52b/oeis_hits{,2}.json` (OEIS "no match" is itself recorded).
* Items = every match, every suggestive correlation, every suggestive non-match, plus "compute X and check Y" items that
  were not run. Confidence = confidence that the item is not nonsense, not that it helps.

## Coverage notes / what I did NOT get to
{{COVERAGE}}

Item count: 111. Tag histogram (top 45): m-over-n 15, star-count 13, oeis-gap 9, hard-primes 9, divisibility-strengthened-ES 8, oeis-match 7, I3 7, anchor 5, mordell-classes 5, schinzel 5, coincidence 5, min-denominator 4, calibration 4, oeis-null 4, pseudosquares 4, BM 4, type-I 4, type-II 4, sanity 4, U-family 4, records 4, new-conjecture 4, compute-and-check 4, parity 3, small-values 3, covering 3, least-qnr 3, class-number 3, x-distribution 3, certificate-families 3, lemma-candidate 3, squares 3, multiplicativity 3, residue-classes 3, 8-over-n 3, R-zero 3, 2-adic 3, hardness-index 3, cross-numerator 3, union-conjecture 3, words 3, T1-analogue 3, smooth 3, counting 2, primes 2


## Items

1. **OEIS anchor: U(n) = A192787** — Our unordered count U(n) of 4/n = 1/x+1/y+1/z (x≤y≤z) reproduces A192787 term-for-term (n ≤ 30 000 computed); the entry's links/comments are the natural index of prior counting work. — *First step:* Read the A192787 entry's references/links and cross-references; record any formula or conjecture not already in FRONTIER.md. [`fingerprint-0001`; high/cheap; oeis-match, anchor, counting]

2. **OEIS anchor: distinct-solution count D(n) = A073101** — D(n) (x<y<z) matches A073101; D(n)=0 only at n=2 for n ≤ 30 000, i.e. ES with distinct denominators holds 3..30 000. — *First step:* Read A073101 cross-references for 'distinct' and 'k-term' variants; check whether any proved bound for D(n) is better than for U(n). [`fingerprint-0002`; high/cheap; oeis-match, anchor, distinct]

3. **OEIS anchor: ordered count O(n) = A292581, at primes A292624** — O(n) (ordered triples) matches A292581, and O(p) matches A292624; U(p) matches A192789. — *First step:* Pull b-files of A292624/A192789 to extend our prime data past 2·10⁵ for free, if they go further. [`fingerprint-0003`; high/cheap; oeis-match, anchor, primes]

4. **OEIS anchor: min max-denominator = A337432** — Our minz(n) (least possible largest denominator) matches A337432; it is the 'smallest-z' ES fingerprint. — *First step:* Read A337432 comments for a conjectured bound minz(n) ≪ n^{1+ε} or similar; compare to our records 2,3,10,14,33,52,102,138,232,… [`fingerprint-0004`; high/cheap; oeis-match, anchor, min-denominator]

5. **OEIS anchors for 5/n and 6/n: A226644, A226645** — U₅(n), U₆(n) (3-term counts for 5/n, 6/n) match A226644 and A226645; U₇..U₁₃ are NOT in OEIS. — *First step:* Submit U_m(n) for m = 7..13 to OEIS (data in data/z52b/raw/m*_4000.txt) after checking against a second implementation. [`fingerprint-0005`; high/cheap; oeis-match, oeis-gap, m-over-n, sierpinski]

6. **O(n) odd ⟺ 4 | n (involution fixed point)** — O(n) mod 2 equals the characteristic function of 4ℤ (OEIS A121262), because permutation orbits have size 1,3,6 and the size-1 orbit x=y=z=3n/4 exists iff 4|n; O(n) ≢ 0 (mod 6) ⟺ n even. — *First step:* Look for a finer involution on the ES solution set at primes p ≡ 1 (4) whose fixed points are countable (cf. WINDMILL.md); test parity of U(p), k₁(p), k₂(p) against simple invariants. [`fingerprint-0006`; high/cheap; parity, involution, trivial-but-true]

7. **U(n) never equals 5 (n ≤ 30 000)** — The value 5 is the only k ≤ 500 not attained by U(n) for 2 ≤ n ≤ 30 000; at primes ≤ 2·10⁵ the values 5 and 12 are never attained. — *First step:* Extend U(n) to n ≤ 10⁵ and check whether U(n) = 5 ever appears; list all n with U(n) ≤ 8 and test whether they are all ≤ some bound. [`fingerprint-0007`; med/cheap; value-set, small-values, counting]

8. **U(p) ≤ 4 only for p ∈ {2,3,5,13,17}** — Among primes ≤ 2·10⁵, U(p) ≤ 4 only at 2,3,5,13,17; for p > 1000 min U(p) is 9 (at 2521), 11, 15, …  — *First step:* Fit min_{p∈[X,2X]} U(p) vs (log X)² for X up to 10⁷ (count program runs in ~1 s per prime at 10⁶). [`fingerprint-0008`; high/cheap; lower-bound, calibration, small-values]

9. **Least prime with U(p) = 6 is 193 (a Type-A failure)** — The sequence 'least prime p with U(p)=k' begins 2,5,3,13,–,193,7,97,11,89,19,–,53,…; 193 (López Type-A failure) is the first prime with exactly six solutions. — *First step:* Tabulate, for each k ≤ 40, the least p with U(p)=k and check whether these are enriched in p ≡ 1 (24) and in the m/p-failure sets (data/z52b/raw/m*_pr1e5.txt). [`fingerprint-0009`; high/cheap; first-occurrence, hard-primes, type-A]

10. **Record lows of U(p)/log²p are 53, 61, 73, 193, 2521** — Scanning primes 50 < p < 2·10⁵, U(p)/log²p sets record lows exactly at 53, 61, 73, 193, 2521 (ratio 0.147 at 2521); no further record up to 2·10⁵. — *First step:* Extend to 10⁷ with the count program restricted to candidates p ≡ 1 (mod 840) or with large least-QNR (cheap pre-filter), to see if 66529 or other A/R failures become records. [`fingerprint-0010`; high/cheap; record-low, hard-primes, oeis-null]

11. **2521 = lcm(1..9) + 1 is the hardest prime ≤ 2·10⁵** — 2521 = lcm(1,…,10)+1 minimises U(p)/log²p over primes ≤ 2·10⁵ (U=9); the primes lcm(1..k)+1 = 7, 13, 61, 421, 2521 have ratios 1.85, 0.61, 0.65, 0.44, 0.15 — monotone towards hard. — *First step:* Compute U, R, Uv for the next such prime 232 792 561 = lcm(1..19)+1 (≈ 1–2 h with the count program; words sieve to 2.4·10⁸ is cheaper) and test whether it is a (★) or b=1 failure. [`fingerprint-0011`; high/medium; lcm-plus-one, hard-primes, extremal, covering]

12. **Prediction: 232 792 561 should be an extreme ES-hard prime** — By the lcm(1..k)+1 heuristic, p = 232 792 561 (prime, = lcm(1..19)+1) has all primes ≤ 19 as QRs and p ≡ 1 mod 2⁴·3²·5·7·11·13·17·19; expect U(p)/log²p far below every prime of comparable size. — *First step:* Run z52b_count on 232792561 (needs ~3 GB spf sieve; or patch to factor x by trial division) and check R(p) via the words sieve extended to 2.4·10⁸. [`fingerprint-0012`; high/medium; prediction, lcm-plus-one, hard-primes]

13. **ES-hard primes vs pseudosquares (A002189)** — Least primes p≡1(4) with least QNR = 2,3,5,…,47: 5,17,73,241,1009,2689,8089,33049,53881,87481,483289,515761,1083289,7921489,3818929; the first terms match OEIS A102295 (record least-QNR primes); several (73, 241, 53881, 87481) coincide with Lehmer pseudosquares A002189 and with our 40 hardest primes. — *First step:* Compute U(p)/log²p for the pseudosquare primes up to 10⁸ and compare to random p≡1(840) of the same size; read Lukes–Patterson–Williams on pseudosquares and Schinzel's 1997 bound. [`fingerprint-0013`; high/cheap; pseudosquares, least-qnr, oeis-match, hard-primes]

14. **U(p) at least-QNR-record primes is only moderately small** — At the least p≡1(4) with least QNR q (q=11..47), U(p)/log²p = 0.40,0.37,0.54,0.53,0.36,0.29,0.60,0.53,0.55,0.67,0.61 — below typical (≈1–2) but not record-hard; 2521 (least QNR 11) is far harder (0.15). — *First step:* Regress log U(p) on log L(1,χ_p) and log(σ(p−1)/(p−1)) jointly; check which explains 2521 vs 87481. [`fingerprint-0014`; high/cheap; pseudosquares, least-qnr, two-axis-hardness]

15. **U(p) residual is driven by L(1,χ_p) (Spearman −0.69)** — At ≈9 000 primes p≡1(4) <2·10⁵, the residual of log U(p) (after log p, loglog p) has Spearman ρ = −0.69 with L(1,χ_p) ≈ h(p)·log ε_p/√p (real quadratic field Q(√p)); more small QRs ⇒ fewer solutions. — *First step:* Prove/derive the expected-count heuristic E U(p) ≈ c(log p)² · F(χ_p) with F a finite Euler product, and compare F with our fitted exponent (−0.30). [`fingerprint-0015`; high/medium; correlation, L-function, real-quadratic, BM]

16. **log U(p) ≈ const − 0.30·log L_Q(1,χ_p), saturating at Q ≈ 30** — Adding log of the truncated Euler product ∏_{q≤Q}(1−χ_p(q)/q)^{−1} to the (log p, loglog p) regression gives α ≈ −0.30 and R²-gain 0.29 (Q=2), 0.40 (Q=3), 0.47 (Q=7), 0.49 (Q=31), 0.48 (Q=1000). — *First step:* Fit with separate coefficients per small prime q (2,3,5,7,11,13) to get the local weights; compare to the Elsholtz–Tao local densities. [`fingerprint-0016`; high/cheap; L-function, euler-product, regression, local-densities]

17. **Type II count k₂(p) prefers L(1,χ_{−4p}) large (α ≈ +0.21)** — Solutions with two denominators divisible by p (k₂) correlate positively with L(1,χ_{−4p}) = πh(−4p)/(2√p) (ρ=+0.37) and negatively with L(1,χ_p) (α ≈ −0.20); Type I (k₁) sees only χ_p (α ≈ −0.34, χ_{−4p} gain ≈ 0). — *First step:* Test the complementarity: correlation between k₁ and k₂ residuals; is min(k₁,k₂) ever 0 at p ≡ 1 (4) and if so, is the other large? [`fingerprint-0017`; high/cheap; type-I, type-II, class-number, twist, complementarity]

18. **(★) count R(p) correlates with h(−4p) (α ≈ +0.38, R²-gain 0.20)** — The c=1 Type-II line R(p) = #{4uBC−u−B=p} fits log R ≈ … + 0.38 log L_Q(1,χ_{−4p}) (gain 0.20) and only −0.17 on χ_p (gain 0.09). — *First step:* Fit log R(p) on log L(1,χ_{dp}) for twists d ∈ {−4,−8,−3,−20,…} jointly (class numbers themselves scale like √p, R like log²p, so only L-values/Euler products can enter); identify the minimal twist set. [`fingerprint-0018`; high/cheap; class-number, star-count, hurwitz, theta]

19. **U(p) uncorrelated with a_p of non-CM elliptic curves** — Spearman of U(p)-residual with a_p(11a1)/2√p is +0.004, with a_p(37a1)/2√p −0.005, with |a_p(32a1)|/2√p +0.007, with Ramanujan τ(p)/p^{5.5} +0.006 (n≈9 000). — *First step:* Repeat with weight-2 newforms of level 4·d for d | 840 and with weight-3/2 forms (Shimura lifts) where class numbers do appear. [`fingerprint-0019`; high/cheap; null-result, elliptic-curve, modular-forms, LMFDB]

20. **a_p(32a1) mod 8 is just (2/p)** — The strong correlation of U(p) with a_p(y²=x³−x) mod 8 (ρ=+0.55) is identical to that with (2/p) (ρ=−0.55): for this CM curve a_p mod 8 encodes p mod 8. — *First step:* None needed; use as a sanity check whenever a CM form correlates. [`fingerprint-0020`; high/cheap; spurious, CM, sanity]

21. **(7/p) anomaly: U(p) does not see the character at 7** — Residual Spearman of U(p) with (2/p), (3/p), (5/p) is −0.55, −0.31, −0.28 but with (7/p) only −0.013, although Mordell's classes p ≡ 3,5,6 (mod 7) are covered by identities. — *First step:* Split U(p) by p mod 7 class and by whether the mod-7 identity solution exists; check whether the 7-family has bounded size. [`fingerprint-0021`; med/cheap; local-primes, mordell-classes, anomaly]

22. **U(p) vs least QNR: ρ = −0.66** — Residual of U(p) correlates −0.66 with the least quadratic non-residue of p and +0.46 with #QNR among primes ≤ 29. — *First step:* Write the Type-I count as a sum over QNRs and check numerically that its main term scales with #QNR ≤ log p. [`fingerprint-0022`; high/cheap; least-qnr, burgess, type-I]

23. **U(p) vs least primitive root: ρ = −0.57** — Residual U(p) correlates −0.57 with the least primitive root g(p), and +0.45 with ord_p(2)/(p−1). — *First step:* Partial correlation of U with ord_p(2)/(p−1) controlling for (2/p) and least QNR. [`fingerprint-0023`; med/cheap; primitive-root, artin, proxy]

24. **U(p) vs τ(p−1) and σ(p−1)/(p−1): ρ ≈ −0.53** — More divisors of p−1 ⇒ fewer ES solutions (ρ(τ(p−1)) = −0.53, ρ(σ(p−1)/(p−1)) = −0.53, ρ(φ(p−1)/(p−1)) = +0.42). — *First step:* Test whether τ(p−1) remains significant after controlling for L(1,χ_p) (partial correlation). [`fingerprint-0024`; high/cheap; p-minus-1, smoothness, divisor-function]

25. **U(p) vs τ((p+3)/4): ρ = +0.59** — U(p) residual correlates +0.59 with τ((p+3)/4) and +0.48 with τ(p+3), but only +0.12 with τ(4p+1), +0.12 with τ(p+4), +0.05 with τ(p+12). — *First step:* Count solutions by x−⌈p/4⌉ ∈ {0,1,2,…} and measure what fraction of U(p) comes from the first few x; relate to divisors of p+3, p+7, … [`fingerprint-0025`; high/cheap; divisor-function, shifts, x-distribution]

26. **Real quadratic regulator log ε_p anticorrelates with U(p) (ρ = −0.44)** — log ε_p and log ε_p/√p correlate −0.44 / −0.51 with U(p)-residual; h(p) alone ≈ 0 (−0.04); CF period of √p −0.27. — *First step:* Correlate the five-slice / λ(p) ≤ 3 certificate counts with the CF period of √p and with the regulator. [`fingerprint-0026`; high/cheap; pell, regulator, continued-fraction, real-quadratic]

27. **h(−3p) correlates positively with U(p) (ρ=+0.46)** — U(p) residual vs h(−3p) (imaginary quadratic field Q(√−3p)) ρ = +0.46; vs h(−4p) only +0.08 (raw) / +0.14 (normalised). — *First step:* Fit log U on all of log L(1,χ_{dp}) for d ∈ {1,−1,−3,−4,−8,5,−20,…} jointly and identify the minimal set. [`fingerprint-0027`; med/cheap; class-number, twist, imaginary-quadratic]

28. **Uv(p) (U-certificates) ~ U(p): ρ = +0.64; R(p) only +0.24** — The ES count U(p) correlates +0.64 with the U-certificate word count Uv(p), +0.46 with I3(p), +0.32 with W(p) but only +0.24 with the (★) count R(p). — *First step:* Compute what fraction of each p's ES solutions correspond to (★), U, I3 words via the explicit maps; check whether the fraction is stable. [`fingerprint-0028`; high/cheap; certificate-families, star-count, U-family, I3]

29. **minz(p) is always a multiple of p (p ≤ 2·10⁵)** — For every prime p ≤ 2·10⁵ the least possible largest denominator minz(p) ≡ 0 (mod p) (OEIS-style constant-zero transform). — *First step:* Try to prove: in any solution of 4/p with largest denominator z, if p ∤ z then z ≥ … > some solution with p | z; else find a counterexample for composite-free p beyond 2·10⁵. [`fingerprint-0029`; high/cheap; min-denominator, lemma-candidate, structure]

30. **minz(p)/p sequence: 1,1,2,2,3,4,6,3,6,8,8,10,… (not in OEIS)** — floor(minz(p)/p) at primes; at p≡1(4): 2,4,6,8,10,4,14,9,10,8,28,7,…; minz(p)/p correlates −0.42 with τ(4p+1) and −0.31 with R(p). — *First step:* Identify minz(p)/p with the least C such that 4Cp+1 has a divisor ≡ −1 (mod 4C) or similar; test equality over our range. [`fingerprint-0030`; med/cheap; min-denominator, star-count, height]

31. **Height growth: max_{p≤X} minz(p)/p** — Record values of minz(p) occur at 2,3,5,7,11,13,17,23,29,31,37,53,… (nearly every prime early on); record minz(p)/p would measure the worst certificate height. — *First step:* Compute max_{p ≤ X} log(minz(p)/p)/log p for X up to 10⁷ and fit. [`fingerprint-0031`; high/cheap; height, min-denominator, growth]

32. **n ∤ minlcm(n) ⟺ 4 | n** — The least common denominator of a solution of 4/n is divisible by n except exactly when 4 | n (data n ≤ 30 000; OEIS A008586 match for the exception positions). — *First step:* Prove: if 4 ∤ n then every solution's lcm is divisible by n (consider v_q of both sides for q^a ∥ n). [`fingerprint-0032`; high/cheap; lcm, lemma-candidate, trivial-but-true]

33. **minlcm(p)/p at primes not in OEIS; correlates +0.23 with least QNR** — The least common denominator over solutions, divided by p, behaves like a cost: larger when small primes are QRs (ρ=+0.23 with least QNR, +0.20 with L(1,χ_p)). — *First step:* Check: is minlcm(p)/p always a practical number? Compute and compare to OEIS A005153. [`fingerprint-0033`; med/cheap; lcm, practical-numbers, cost]

34. **Mordell classes: x = (n+3)/4 fails only for n ≡ 1 (mod 24)** — For n ≤ 30 000 the least first denominator exceeds ⌊n/4⌋+1 exactly for 373 values, all ≡ 1 (mod 24): 49,73,169,193,241,313,361,409,433,553,601,673,…; includes 193, 409, 2521, 5569, 9601 (not 577, 66529). — *First step:* Characterise: n with no solution with x=(n+3)/4 ⟺ 12/(n(n+3)) not a sum of two unit fractions ⟺ no divisor pair condition; derive the density and compare to count 373 ≤ 30 000. [`fingerprint-0034`; high/cheap; greedy, mordell-classes, oeis-gap, single-identity]

35. **Greedy-failure composites: 49, 169, 361, 553, … (squares and products)** — The composite members of the x=(n+3)/4 failure set include all odd squares ≡ 1 (24) and products like 553 = 7·79; the square subfamily is forced by T1-type reciprocity. — *First step:* List non-square composite members ≤ 10⁵ and check whether each factors into primes that are themselves failures (multiplicativity test). [`fingerprint-0035`; med/cheap; T1, squares, multiplicativity]

36. **U(n) records at 2,3,6,8,10,12,15,24,30,40,48,60,… vs highly composite numbers** — Record positions of U(n) (not in OEIS) are dominated by smooth numbers but are not A002182 (15, 30, 40 appear; 36 does not). — *First step:* Compare record positions with records of Σ_{d|n} τ(d)², τ(n)τ(n+1)…; fit max_{n≤X} U(n) vs exp(c log X/log log X). [`fingerprint-0036`; med/cheap; records, highly-composite, extremal-order]

37. **Record U(p) at primes: 2,3,7,11,19,23,47,71,167,191,239,359,…** — Primes setting U(p) records are all ≡ 3 (mod 4) beyond 2,3 and mostly ≡ 23 (mod 24) (p+1 highly divisible); identical record set for O(p). — *First step:* Check if record primes satisfy p+1 = smooth with record τ(p+1); OEIS search of the record list (no match). [`fingerprint-0037`; high/cheap; records, easy-primes, p-plus-1]

38. **U(p) mod m is equidistributed (small bias at U ≡ 1 mod 6)** — For p≡1(4) >100 (n=8 843), U(p) mod 2,3,4,8 are flat within noise; U(p) ≡ 1 (mod 6) is 1361 vs ≈1490 expected (≈3.5σ low). — *First step:* Separate solutions with repeated denominators (x=y or y=z) and recount mod 6. [`fingerprint-0038`; med/cheap; parity, equidistribution, null-result]

39. **k₁(n), k₂(n) are new sequences** — Number of solutions of 4/n with exactly one (k₁) / two (k₂) denominators divisible by n: k₁ = 0,2,0,1,5,5,0,5,6,6,9,…; k₂ = 1,1,1,1,2,2,2,1,4,3,…; neither in OEIS. — *First step:* Submit both (with k₃ ≡ 0 for n>1, a trivial lemma) to OEIS after independent verification. [`fingerprint-0039`; high/cheap; oeis-gap, type-I, type-II]

40. **k₂(p) ≥ 1 for every prime p ≤ 2·10⁵** — Every prime ≤ 2·10⁵ has a solution with exactly two denominators divisible by p (Type II); min k₂(p) over p ≡ 1 (4) > 1000 is small but nonzero. — *First step:* Record the minimum k₂(p) per dyadic range and list primes with k₂(p) = 1. [`fingerprint-0040`; high/cheap; type-II, universality, small-values]

41. **k₁(p) can be small while k₂(p) is not — or vice versa?** — k₁ and k₂ have residual correlation driven by different characters; tabulating the joint distribution of (k₁(p), k₂(p)) shows whether simultaneous smallness is rarer than independence predicts. — *First step:* Compute Spearman(k₁ residual, k₂ residual) and the count of p with both below their 5% quantiles vs 0.25% expected. [`fingerprint-0041`; high/cheap; type-I, type-II, complementarity, joint-distribution]

42. **nx(n): number of distinct first denominators** — nx(n) = #{x : some solution has this smallest denominator}: 1,2,2,1,3,3,4,3,4,3,6,2,… (not in OEIS); at primes correlates like U (ρ=−0.65 with L(1,χ_p)). — *First step:* Fit nx(p) vs log p (likely ≍ log p, not log²p) and check whether nx(p) ≥ 1 has a shorter proof form (one-shift divisibility). [`fingerprint-0042`; med/cheap; oeis-gap, branching, x-distribution]

43. **maxx(p) − p/4 (largest smallest-denominator)** — The largest possible smallest denominator maxx(p) has maxx − p/4 weakly tied to least QNR (ρ=−0.19); maxx(p) ≤ 3p/4 always; the sequence is not in OEIS. — *First step:* Plot (maxx(p) − p/4)/p; compare with the balanced-solution census in BALANCED_LATTICE.md. [`fingerprint-0043`; med/cheap; balanced, oeis-gap, x-distribution]

44. **U(p) at p ≡ 1 (24) vs p ≡ 1 (840) distributions** — Spearman of residual U(p) with 1[p≡1 mod 24] is −0.62, with '840-square class' −0.38, with 1[p≡1 mod 840] −0.15 (rare event). — *First step:* Compute mean U(p)/log²p per class mod 840 (the six square classes 1,121,169,289,361,529) and rank them. [`fingerprint-0044`; high/cheap; mordell-classes, 840, residue-classes]

45. **Which square class mod 840 is hardest?** — The six Mordell hard classes {1,121,169,289,361,529} mod 840 likely differ in mean U(p)/log²p; the 30 hardest primes ≤ 2·10⁵ fall in classes 1 (×9), 361 (×8), 121 (×6), 169 (×3), 289, 529 — and three outside the square classes (193, 241 ≡ 193, 241; 3169 ≡ 649). — *First step:* Group primes ≤ 2·10⁵ by class mod 840 and by class mod 9240 = 840·11, compute mean and min of U(p)/log²p. [`fingerprint-0045`; high/cheap; 840, mordell-classes, class-constants]

46. **U(p) vs smoothness of p−1: ρ(P⁺(p−1) exponent) = +0.40** — log P⁺(p−1)/log p correlates +0.40 with U(p) residual: smooth p−1 ⇒ hard. — *First step:* Estimate density of 'ES-hard' (ratio below 0.3) among primes with P⁺(p−1) ≤ p^{1/3} vs others. [`fingerprint-0046`; high/cheap; smoothness, p-minus-1, thin-set]

47. **Hard primes are p ≡ 1 mod a large smooth modulus — compare with Carmichael/Korselt primes** — 2521, 1201, 3361, 20521, 21841, 4201, 14401, 9601 all have p−1 divisible by 2⁴·3·5² or 2⁴·3·5·7 etc.; these are exactly the primes used to build Carmichael numbers (Erdős construction, p−1 | L). — *First step:* Test: are ES-hard primes over-represented among prime factors of Carmichael numbers ≤ 10¹²? (Pinch's tables). [`fingerprint-0047`; med/medium; carmichael, smooth-modulus, AGP]

48. **O(p) record primes = U(p) record primes** — The record positions of O(p) and U(p) coincide (2,3,7,11,19,23,47,71,167,191,239,359,…) — degenerate solutions are negligible at record primes. — *First step:* None; use O(p)/6 ≈ U(p) in heuristics. [`fingerprint-0048`; high/cheap; records, sanity]

49. **Hardest 30 primes ≤ 2·10⁵ by U/log² are all ≡ 1 (mod 24)** — Sorted: 193, 241, 1201, 2521, 3169, 3361, 4201, 5281, 8761, 9601, 12601, 14401, 20521, 21841, 24481, 44641, 54121, 59929, 66529, 67369, … — every one ≡ 1 (mod 24); no OEIS match. — *First step:* Compute the hard list's distribution mod 5, 7, 9, 16, 25 vs all p ≡ 1 (24) to measure each prime power's contribution. [`fingerprint-0049`; high/cheap; hard-primes, mordell-classes, oeis-null]

50. **Campaign hard-prime lists are not in OEIS** — The R-zeros (409,577,5569,9601,23929,…,8813281), Type-A failures (193,2521,66529), union (193,409,577,2521,3361,…) and U failures (105,2961,3985,25305,111969,978145) give no OEIS hit. — *First step:* Submit the R-zero list with a definition and b-file to OEIS; also add I3 zeros (114 terms) and U failures. [`fingerprint-0050`; high/cheap; oeis-null, oeis-gap, hard-primes, outreach]

51. **5/n and 6/n: no 3-term failure (primes ≤ 10⁵, all n ≤ 4000)** — U₅(p), U₆(p) ≥ 1 for all primes 3..10⁵ and all n ≤ 4000 (6/n trivially follows from 3/n except tiny n). — *First step:* Compute Spearman(U₄(p)/log²p, U₅(p)/log²p) at p ≤ 10⁵ and list primes hard for both. [`fingerprint-0051`; high/cheap; sierpinski, m-over-n, sibling]

52. **7/n fails only at n = 2 (≤ 10⁵ primes, n ≤ 4000)** — Consistent with PW (no 7/n exception in [3, 10¹³]); 7/p counts at primes are small (U₇(p) = 0,1,2,3,2,8,4,…). — *First step:* Fit U₇(p) vs log²p and check whether the hardest 7/p primes coincide with the hardest 4/p primes. [`fingerprint-0052`; high/cheap; m-over-n, sibling, schinzel]

53. **'Even ES': every prime p > 241 has an ES solution with x, y, z all even (≤ 10⁵)** — 8/p = 1/x'+1/y'+1/z' ⟺ 4/p has a solution with 2 | x, y, z; failures at primes: {2,3,11,17,131,241} (known, PW Table 1). — *First step:* Search for a polynomial/covering family giving all-even solutions for p ≡ 1 (24) and see which residue classes remain; compare with T1 at squares (do even squares-type obstructions exist?). [`fingerprint-0053`; high/cheap; divisibility-strengthened-ES, m-over-n, 8-over-n]

54. **'3-divisible ES': 12/p fails at 22 primes ≤ 10⁵, last 12 241** — 12/p ⟺ ES solution of 4/p with 3 | x, y, z; failures 2,3,5,7,13,29,31,37,73,97,193,433,577,1129,1657,1873,2521,2593,3433,10369,12049,12241. — *First step:* Extend 12/p to 10⁷ (fast: x ∈ (p/12, p/4]) to test finiteness; check whether 66529, 409, 5569 eventually appear (they do not ≤ 10⁵ except as listed). [`fingerprint-0054`; high/cheap; divisibility-strengthened-ES, hard-primes, 12-over-n]

55. **'4-divisible ES': 16/p last failure ≤ 10⁵ is 83449 — an R-zero** — 16/p failures (38 primes ≤ 10⁵) include 193, 577, 1201, 2521, 3361, 3169, 4801, 33601, 36529, 78721 and end at 83449, which is also a (★) failure. — *First step:* Compute v₂(p−1), p mod 16/32/64 for all 16/p failures and for the 14 R-zeros; test whether 2-adic depth predicts both. [`fingerprint-0055`; high/cheap; divisibility-strengthened-ES, R-zero, 2-adic, coincidence]

56. **'5-divisible ES': 20/p fails at 63 primes ≤ 10⁵, last 90001** — No ES solution with 5 | x, y, z at 63 primes ≤ 10⁵, including 1201, 2521, 4201, 4801, 8761, 21841, 24481 (ES-hard) — the last at 90001 = 9·10⁴+1. — *First step:* Tabulate p mod 25 and mod 125 for 20/p failures vs random primes. [`fingerprint-0056`; high/cheap; divisibility-strengthened-ES, local-5-adic]

57. **Divisibility-strengthened ES_k ladder (k | x,y,z): last failures 241, 12241, 83449, 90001, ≥97777, 92401, …** — ES_k := 4k/p is 3-term; last failure ≤ 10⁵ for k = 2..12: 241, 12241, 83449, 90001, 97777, 92401, 97561, 98737, 99961, 99529, 98737; counts 6, 22, 38, 63, 146, 133, 222, 383, 399, 478, 698. — *First step:* Pick the smallest k (k=2, 'even ES') and try to push the census to 10¹⁰ with a dedicated sieve; check whether the 8/n exceptions really stop at 241. [`fingerprint-0057`; high/medium; divisibility-strengthened-ES, ladder, calibration, schinzel]

58. **Failure sets are monotone under divisibility of the numerator (sanity + structure)** — If m | m′ then fail(m) ⊆ fail(m′) (divide all denominators by m′/m); verified on all m ≤ 48, p ≤ 10⁵. 'Primitive' failures (not explained by a divisor d ≥ 5 of m) number 0,0,1,6,4,8,3,22,10,8,25,32,17,45,… — *First step:* Submit primitive-failure counts to OEIS; examine whether primitive failures of 4k concentrate on primes hard for 4/p. [`fingerprint-0058`; high/cheap; lattice, m-over-n, primitive-failures, sanity]

59. **Hardness index H(p) = #{m ≤ 48 : m/p fails} correlates with U(p)/log²p (ρ = −0.43)** — Primes failing many m/p are hard for 4/p: Spearman −0.43 over p≡1(4) ≤ 10⁵. Highest H: 113 (20), 193 (19), 101 (18), 137, 181, 421 (17), 149, 241, 281, 353 (16). — *First step:* Regress H(p) on Legendre symbols (q/p) for q ≤ 30 and on p mod 8,9,16,25; report R². [`fingerprint-0059`; high/cheap; hardness-index, cross-numerator, locality-test]

60. **R-zeros and Type-A failures across numerators: 193 fails 19 numerators, 577 13, 2521 11, 3361 11, 409 7, 9601 5, 5569 4, 66529 3, 23929 0** — Among m ∈ [5,48], the campaign's hard primes fail many m/p; but 23929 (an R-zero) fails none — R-failure is not 'globally hard'. — *First step:* For each of the 14 R-zeros compute U(p)/log²p and H(p) to rank 'intrinsic' vs 'line-specific' hardness. [`fingerprint-0060`; high/cheap; R-zero, type-A, hardness-index, line-specific]

61. **PW numerics reproduced: for every m ∈ [20,48] some prime in (m², 2m²) fails m/p** — Counts of failing primes in (m², 2m²): m=20:6, 21:5, 22:5, 23:5, 24:13, …, 48:70 — consistent with PW's reported numerics for m ≥ 20. — *First step:* Compare the counts with PW's predicted number (their Elsholtz–Tao-style density) in (m², 2m²). [`fingerprint-0061`; high/cheap; literature-check, schinzel, m-over-n]

62. **Prime numerators have far fewer failures than composite ones** — Failures ≤ 10⁵: m=7:1, 11:3, 13:10, 17:17, 19:16, 23:46, 29:79, 31:123, 37:187, 41:147, 43:246, 47:348 vs m=12:22, 16:38, 18:49, 20:63, 24:146, 36:383, 48:698. — *First step:* Fit #failures(m) for prime m vs m (power law?) and compare with PW's exp(m^{1/3}) lower bound for n_m. [`fingerprint-0062`; high/cheap; m-over-n, prime-numerators, growth]

63. **9/n fails exactly at {2,5,11,19} (≤ 10⁵ primes, n ≤ 4000)** — Tiny, apparently complete exception set for 9/n; 9 = 3² so 9/n relates to 3/n-type identities. — *First step:* Prove completeness of {2,5,11,19} for 9/n by covering congruences (expected possible since 9/n has many identities) — a warm-up for the ES covering obstruction. [`fingerprint-0063`; med/medium; m-over-n, complete-exception-set, covering]

64. **10/n fails at {2,3,7,11,43,61,67,181}; 11/n at {2,3,4,37}; 13/n at {2,3,4,5,7,14,53,61,67,79,211,281}** — Complete-looking small exception lists (n ≤ 4000 all, primes ≤ 10⁵), none in OEIS; composite exceptions occur (4 for 11 and 13, 14 for 13). — *First step:* Explain 13/14 and 11/4 failures (why multiplicativity breaks) and check whether any composite n > 100 fails m/n for m ≤ 13. [`fingerprint-0064`; high/cheap; m-over-n, composite-exceptions, complete-exception-set]

65. **15/p failure set contains three of the 30 hardest ES primes (4201, 12601, 20521)** — 15/p fails at 25 primes ≤ 10⁵ ending 1103,1171,1367,4201,6301,12601,16831,20521; 4201, 12601, 20521 are top-30 hard for 4/p though 15 is not a multiple of 4. — *First step:* Compute p mod 840 for 15/p failures and test enrichment of p ≡ 1 (mod 120). [`fingerprint-0065`; high/cheap; cross-numerator, coincidence, hard-primes]

66. **m/p failures are enriched in primes adjacent to 5-smooth numbers** — For m=12, 15 of 22 failures have p−1 or p+1 5-smooth (only 182 such primes ≤ 10⁵ in total); m=20: 27/63; m=24: 39/146 — OEIS returns spurious A219669 ('primes neighboring a 5-smooth number') for m=45. — *First step:* Compute failure rate among 5-smooth-neighbour primes vs others for each m; extend to 7-smooth. [`fingerprint-0066`; high/cheap; smooth-neighbour, m-over-n, spurious-match]

67. **Last-failure sequence by numerator m (7..48) is not in OEIS** — 2, 241, 19, 181, 37, 12241, 281, 353, 20521, 83449, 2081, 35281, 353, 90001, 14051, 14543, 31771, 97777, … — *First step:* Extend each m to 10⁷ (cost drops ∝ 1/m) and submit as 'largest known prime p with m/p not a sum of 3 unit fractions'. [`fingerprint-0067`; high/medium; oeis-gap, schinzel, n_m]

68. **Number of m/p failures ≤ 10⁵ by m: 0,0,1,6,4,8,3,22,10,9,25,38,17,49,16,63,… (no OEIS match)** — The failure-count profile across m (5..48) has strong arithmetic modulation (peaks at m ≡ 0 mod 12). — *First step:* Regress log(#fail(m)+1) on log m and the indicator functions 4|m, 3|m, 5|m. [`fingerprint-0068`; high/cheap; m-over-n, profile, oeis-null]

69. **U₇..U₁₃ count sequences are OEIS gaps** — U_m(n) for 7 ≤ m ≤ 13 (n ≥ 2) are absent from OEIS; e.g. U₇: 0,1,1,2,7,3,2,3,5,2,13,8,…; U₈: 0,0,1,1,3,3,3,1,2,0,8,3,… — *First step:* Cross-check with a brute-force Python enumerator for n ≤ 300 and submit. [`fingerprint-0069`; high/cheap; oeis-gap, m-over-n, outreach]

70. **U₈(p) = number of all-even ES solutions of 4/p** — By scaling, U₈(p) counts solutions of 4/p with x, y, z even; at primes: 0,0,1,3,0,3,0,2,7,4,12,6,… — *First step:* Compute U₈(p)/U₄(p) average by p mod 8 and mod 16; compare with the 2-adic local density of the ES surface. [`fingerprint-0070`; high/cheap; 2-adic, local-density, 8-over-n]

71. **U₁₂(p)/U₄(p): the 3-divisible fraction of ES solutions** — U₁₂(p) counts solutions of 4/p with 3 | x,y,z; its ratio to U₄(p) is a 3-adic local statistic; failures at 193, 577, 2521 mean this fraction hits 0 at hard primes. — *First step:* Compute E[U_{4k}(p)/U₄(p)] for k=2,3,5 and compare with 1/k³-type local densities on the ES surface. [`fingerprint-0071`; med/cheap; local-density, manin, 3-adic]

72. **Joint failure: no prime ≤ 10⁵ fails both 8/p and 12/p beyond {2,3}** — fail(8) ∩ fail(12) = {2,3}; fail(8) ∩ fail(16) = fail(8) by monotonicity; overlaps of non-nested failure sets are small. — *First step:* Verify 'every prime p > 3 has an ES solution with all-even or all-3-divisible denominators' to 10⁷, and find the minimal such union family. [`fingerprint-0072`; high/cheap; covering-by-subfamilies, divisibility-strengthened-ES, union]

73. **A union conjecture: ES_2 ∪ ES_3 (even or 3-divisible solutions) for all primes p > 3** — Since fail(8) ∩ fail(12) ∩ primes = {2,3} ≤ 10⁵, conjecture: every prime p > 3 has an ES solution with 2 | x,y,z or 3 | x,y,z. — *First step:* Extend the joint census; search for the natural certificate lines in each subfamily and check whether their failure sets are disjoint. [`fingerprint-0073`; high/medium; union-conjecture, divisibility-strengthened-ES, new-conjecture]

74. **Composite-n failures for m ≤ 13 are only 4, 14, 25** — Among n ≤ 4000, the composite failures of m/n for 5 ≤ m ≤ 13 are n = 4 (m=11,13), 14 (m=13), 25 (m=12) — tiny. — *First step:* Prove: if m/p solvable for each prime p | n then m/n solvable except finitely many n (check 25 for m=12: 12/5 solvable? no — so it's inherited). [`fingerprint-0074`; med/cheap; multiplicativity, composite-exceptions, m-over-n]

75. **12/25 fails while 12/5 fails: inherited, but 13/14 fails with 13/2, 13/7 failing** — Composite failures appear to be products of failing primes (25 = 5², 14 = 2·7, 4 = 2²): consistent with 'fail(m/n) ⇒ each prime factor fails or is tiny'. — *First step:* Test the implication on m ≤ 48 and n ≤ 4000 composite (needs composite runs for m > 13). [`fingerprint-0075`; med/cheap; multiplicativity, reduction-to-primes, m-over-n]

76. **Hardest-for-15 vs hardest-for-4: correlation across numerators** — Compute Spearman between U₄(p)/log²p and U_m(p)/log²p for each m ≤ 48 (data on disk). — *First step:* Run the 44 correlations; cluster m by correlation profile. [`fingerprint-0076`; high/cheap; cross-numerator, latent-variable, compute-and-check]

77. **Schinzel sibling with j unit fractions (PW's generalisation)** — PW also treat m/n as a sum of j unit fractions; the analogous fingerprints (failure sets of m/n with j=2,3,4) give a two-parameter table. — *First step:* Compute the j=2 failure density for 4/n (known: fails for most n) and the j=4 exceptions for m ≤ 48. [`fingerprint-0077`; high/cheap; j-unit-fractions, calibration, m-over-n]

78. **Explicit check of PW's 'prime in (m², 2m²)' theorem threshold** — PW prove the existence of a failing prime in (m², 2m²) for m ≥ 6.52·10⁹ and observe it numerically from m ≥ 20; our census confirms m=20..48. — *First step:* Read PW §§3–4 and write down where m → ∞ is used; check whether any of it says something about fixed m=4 (it shouldn't). [`fingerprint-0078`; high/cheap; literature, schinzel, no-go-calibration]

79. **Primes failing ≥ 15 numerators are all < 700** — High H(p) occurs only at small p (113, 193, 101, 137, 181, 421, 149, 241, 281, 353, 397, …); for p > 10⁴, H(p) is small. — *First step:* Plot max H(p) over dyadic ranges. [`fingerprint-0079`; high/cheap; hardness-index, decay]

80. **8/n failures 131 and 241 vs ES hardness of 131 (≡ 3 mod 4) and 241** — 241 is a top-30 hard prime for 4/p and the last 8/p failure; 131 ≡ 3 (mod 4) is easy for 4/p. — *First step:* Examine all ES solutions of 4/131 and why none has all-even denominators (parity of x,y,z patterns). [`fingerprint-0080`; high/cheap; 8-over-n, 2-adic, case-study]

81. **Last 16/p failure 83449 and last 12/p failure 12241: next-term prediction** — If ES_k failure sets are finite, the largest elements grow quickly with k; PW-type heuristics would predict last(ES_k) ≈ exp(c k^{1/3}) or similar. — *First step:* Fit log last(4k) for k = 2..5 and compare with PW's density model; extend 16/p and 20/p to 10⁷ to see if new failures appear. [`fingerprint-0081`; med/medium; prediction, divisibility-strengthened-ES, model-check]

82. **Word sieve reproduces every campaign census (cheap independent engine)** — A 25-line C sieve over n = tuv − u − v (all n ≤ 3·10⁶ in 5 s) reproduces the 114 I3 zeros (max 2 433 600), the R-zeros ≤ 3·10⁶, and the six non-square U failures ≤ 10⁶. — *First step:* Extend to 3·10⁸ with uint16 counters in a memory-bounded segmented version and re-certify the (★) census to that height. [`fingerprint-0082`; high/cheap; engine, certification, words]

83. **All I3 zeros > 50 that are odd: 55, 59, 83, 87, 103, 105, 119, 143, 145, 159, 175, 1225** — Of the 114 I3 zeros only 12 odd ones exceed 50, the last being 1225 = 35²; even zeros go up to 2 433 600 = 1560². — *First step:* State and record the odd-I3 conjecture with census to 3·10⁶; check whether odd I3 suffices for the ES application (primes are odd). [`fingerprint-0083`; high/cheap; I3, odd-restriction, new-conjecture]

84. **I3 zero squares: 1,4,…,1225,1600,19600,2 433 600** — The square I3 zeros are 1,4,9,16,25,36,49,64,100,144,196,324,576,784,900,1225,1600,19600,2433600 (19600 = 140², 2433600 = 1560² = 2⁶3²5²13²). — *First step:* Compute I3(m²) for m ≤ 3000 and check whether I3(m²) is systematically small (but nonzero) for m divisible by 4·3·5·… [`fingerprint-0084`; high/cheap; I3, squares, T1-analogue]

85. **2 433 600 = 1560² is a zero of I3, R, Uv and ESC simultaneously** — At n = 1560² every certificate family in the word sieve vanishes (W = 54 but I3 = R = Uv = ESC = 0); same at 1225 = 35² and 105. — *First step:* Test I3(m²) for smooth m (m = 2^a3^b5^c13^d…) up to 10⁸ via a targeted solver for tuv−u−v = m². [`fingerprint-0085`; high/cheap; I3, squares, smooth, coincidence]

86. **105 = 3·5·7 is a zero of I3, R, Uv and ESC** — n = 105 is the first non-square zero of the U family and also an I3, (★) and 'some coordinate in 4ℤ∪(8ℤ−n)' zero; ES(105) holds via other identities. — *First step:* List all ES solutions of 4/105 and classify which structural family produces each. [`fingerprint-0086`; high/cheap; 105, certificate-families, test-case]

87. **ESC zero set: non-squares are 105, 288, 336, 672, 1380, 29568, 41220, 57696, 97440, 255360, …, 2 402 400** — n with no word having a coordinate in 4ℤ ∪ (8ℤ − n): only 105 among odd non-squares ≤ 3·10⁶; the even ones are highly smooth (2402400 = 2⁵·3·5²·7·11·13). — *First step:* Check whether even ESC zeros are exactly the n with n+1 and 2n+1 having no divisors in the required classes (characterise). [`fingerprint-0087`; med/cheap; ESC, smooth, even-n]

88. **R(n) = 0 at n = 2^k − 1 for k ∈ {2,3,4,5,7,8,13}** — The (★) count vanishes at 3, 7, 15, 31, 127, 255, 8191 although R(n) = 0 has density < 0.1% among n ≡ 3 (mod 8); R(2^k−1) > 0 for other k ≤ 21. — *First step:* Explain via the divisor form R(n) = Σ_C #{d | 4Cn+1 : d ≡ −1 (mod 4C)} with n = 2^k − 1; test R(2^k − 1) for k ≤ 61 with a dedicated divisor search. [`fingerprint-0088`; med/cheap; mersenne, star-count, coincidence]

89. **R(3^k) = 0 exactly for even k (squares) and k = 1** — R(3^k): 0,0,2,0,2,0,4,0,18,0,10,0,10 for k = 1..13 — T1 kills even k; odd k ≥ 3 positive. — *First step:* Compare R(3^{2j+1}) with the BM main term M_BM(3^{2j+1}). [`fingerprint-0089`; high/cheap; T1, prime-powers, sanity]

90. **R-zeros among odd non-squares: 3,7,15,31,39,51,57,79,99,105,127,177,199,249,255,291,295,345,387,409,…** — Not in OEIS; for n ≡ 1 (8) R=0 has frequency 0.30%, n ≡ 5 (8) exactly 0 (≤ 3·10⁶), n ≡ 3,7 (8) ≈ 0.05%. — *First step:* Prove R(n) ≥ 1 for n ≡ 5 (mod 8) (look for an explicit (u,B,C) family), and similarly U(n) ≥ 1 for n ≡ 3,5,7 (mod 8) (Uv zero rate is exactly 0 there). [`fingerprint-0090`; high/cheap; star-count, residue-classes, covering, lemma-candidate]

91. **Composite R-zeros include the pseudosquare 2641 = 19·139** — Composite non-square n ≡ 1 (4) with R(n) = 0: 57, 105, 177, 249, 345, 465, 777, 801, 969, 1345, 1465, 1617, …, 2641, …; 2641 is Lehmer's pseudosquare L₁₃ (A002189) and also an x=(n+3)/4 greedy failure. — *First step:* Compute R, U, Uv, I3 at all pseudosquares A002189 up to 10¹⁰ (targeted divisor-form computation) and compare with typical values. [`fingerprint-0091`; high/medium; pseudosquares, T1-analogue, approximate-reciprocity]

92. **Pseudosquares as approximate squares for T1: a conjecture** — Conjecture: for pseudosquares L_q (QR mod all primes ≤ q, ≡ 1 mod 8), every certificate-line count is ≪ (small) and tends to vanish as q grows, i.e. T1 is 'approximately' active. — *First step:* Test on A002189 terms up to 10¹² using R's divisor form (only C ≤ few hundred needed for a lower bound on R). [`fingerprint-0092`; med/medium; pseudosquares, T1-analogue, new-conjecture]

93. **Mean R(n)/log²n on n ≡ 1 (4) drifts 0.145 → 0.133 (10³ → 10⁶)** — Average of R(n)/(log n)² over n ≡ 1 (4) in [X, 2X]: 0.1446 (10³), 0.1388 (10⁴), 0.1353 (10⁵), 0.1332 (10⁶); FRONTIER lists constants 1/8 = 0.125 (all integers) and 3/(2π²) = 0.152. — *First step:* Fit mean = 1/8 + a/log X + b/log²X to 10⁸; compare with a second-order term from the divisor-sum asymptotics. [`fingerprint-0093`; high/cheap; star-count, mean-value, second-order-term]

94. **BM main term explains the ES count U(p) better than its own (★) count** — At 696 primes p≡1(4) ≤ 12 000: residual Spearman(M_BM, U) = +0.65 but residual Spearman(M_BM, R) = +0.10; raw Spearman(R, M_BM) = 0.47 (shared log² growth); mean R/M_BM = 1.31. — *First step:* Recompute on 20 000–30 000 (running: data/z52b/bm_check_20000_30000.json) and decompose R(p) − M_BM(p) into higher-order characters (the X(n) part of FRONTIER §2.1). [`fingerprint-0094`; high/cheap; BM, star-count, data-vs-theory, surprise]

95. **R-zeros sit in the low tail of M_BM but not at its bottom** — Quantile of M_BM(p) among primes ≤ 12 000: 409 → 0.6%, 577 → 3.4%, 5569 → 12%, 9601 → 20%. — *First step:* For each R-zero compute the full character decomposition M_gen and X; record which characters cancel the main term. [`fingerprint-0095`; high/cheap; BM, R-zero, higher-characters]

96. **(★) and Uv and I3 zero rates by n mod 8** — Zero frequency ≤ 3·10⁶: R=0 at 0.30% (n≡1 mod 8), 0 (n≡5), 0.044% (n≡3), 0.053% (n≡7); Uv=0 only at n ≡ 1 (8). — *First step:* Tabulate zero rates by n mod 24 and mod 840 for each family; find the family whose zero set is contained in the square classes mod 840. [`fingerprint-0096`; high/cheap; residue-classes, zero-rates, certificate-families]

97. **I3(n) = 1 is rare beyond 1000: 2160, 2316, 3900, 9090, 9408, 30276, 453660** — Only seven n in (1000, 3·10⁶] have exactly one I3 word. — *First step:* Factor them (2160 = 2⁴3³5, 453660 = 2²·3·5·7561, 7561 prime) and look for a common shape with 2433600. [`fingerprint-0097`; high/cheap; I3, near-zeros, smooth]

98. **W(n) (all words) has records at 1,3,5,7,11,17,19,23,35,47,59,71,…** — Records of W(n) = #{t,u,v ≥ 1 : tuv−u−v = n} are at n with n+1 and 2n+1, 3n+1… all highly divisible (W counts divisors of tn+1 in classes); not in OEIS. — *First step:* Identify W(n) with a classical divisor-sum (Σ_t τ_{−1 mod t}(tn+1)); submit to OEIS. [`fingerprint-0098`; med/cheap; words, records, oeis-gap]

99. **t=1 and t=2 word counts are τ(n+1) and τ(2n+1) (OEIS A000005, A099774)** — The t=1 slice of tuv−u−v=n is (u−1)(v−1)=n+1 → τ(n+1); the t=2 slice is (2u−1)(2v−1)=2n+1 → τ(2n+1) (OEIS confirmed). — *First step:* None (anchor); use as unit tests. [`fingerprint-0099`; high/cheap; oeis-match, anchor, words]

100. **R(p) is always even — the (u,B) swap involution** — R(p) at primes p≡1(4): 2,2,2,4,2,6,4,4,2,8,…, always even (FRONTIER notes it); R(p)/2 = #{u<B}. — *First step:* Check the distribution of R(p)/2 mod 2 by p mod 8; search for a second involution on (★) triples with computable fixed points. [`fingerprint-0100`; high/cheap; parity, involution, star-count]

101. **U failure set vs I3 zero set: only 105 is common** — The U failures {105, 2961, 3985, 25305, 111969, 978145} and the I3 zeros intersect only in 105. — *First step:* Compute the joint zero set of U and I3 among n ≡ 1 (4), n ≤ 3·10⁶; state a union conjecture. [`fingerprint-0101`; high/cheap; union-conjecture, I3, U-family]

102. **Joint zeros of R and Uv among n ≡ 1 (4)** — Since R (t ∈ 4ℤ) and Uv (v ∈ 𝒞_n) are different slices of the same word equation, their joint zero set among n≡1(4) non-squares should be tiny. — *First step:* Compute the joint zero set of (R, Uv) and of (R, I3) ≤ 3·10⁶ from words_3e6.npy. [`fingerprint-0102`; high/cheap; union-conjecture, star-count, U-family, compute-and-check]

103. **ESC(n) counts are an ES lower bound at primes — check ESC(p) ≥ c log²p** — ESC(p) (words with some coordinate in 4ℤ ∪ (8ℤ−p)) is ES-equivalent at primes per CONTEXT; its residual follows χ_p with α ≈ −0.24 (R²-gain 0.31). — *First step:* Compute min_{p ∈ [X,2X]} ESC(p)/log²p up to 3·10⁶ and compare its stability to U(p)'s. [`fingerprint-0103`; high/cheap; ESC, lower-bound, calibration]

104. **R(p) correlates with τ(4p+1)? — divisor-form check** — R(p) = Σ_C #{d | 4Cp+1 : d ≡ −1 (mod 4C)}; the C=1 term is #{d | 4p+1 : d ≡ 3 (mod 4)}; minz(p)/p correlates −0.42 with τ(4p+1). — *First step:* Compute the C-profile of R(p): fraction of R from C = 1, 2, 3, … at p ≤ 10⁶. [`fingerprint-0104`; high/cheap; star-count, divisor-form, C-profile]

105. **Distribution of the smallest C in (★) certificates** — For each p with R(p) > 0, Cmin(p) = least C contributing; its distribution (geometric? power law?) is a fingerprint of how 'far' the certificate is. — *First step:* Compute Cmin(p) for p ≤ 3·10⁶ via a C-major sieve and fit max_{p≤X} Cmin(p). [`fingerprint-0105`; high/cheap; star-count, certificate-height, compute-and-check]

106. **I3(p) at primes: 31, 43, 47, 59, 83, 103 are zeros** — I3(p) = 0 at small primes 31, 43, 47, 59, 83, 103; none beyond 103 (odd zeros > 103 are composite: 105, 119, 143, 145, 159, 175, 1225). — *First step:* State 'every prime p > 103 is tuv−u−v with t,u,v ≥ 3' with census to 3·10⁶; look for a covering-congruence proof for p ≡ 1 (4). [`fingerprint-0106`; high/cheap; I3, primes, new-conjecture]

107. **Uv zero set (all residues): 12, 28, 60, 96, 105, 124, 156, 204, 228, 288, …, 2961, …** — Without the n ≡ 1 (4) restriction, U-zeros are mostly even (multiples of 4 with n+1 prime-ish); non-OEIS. — *First step:* None beyond recording; possibly characterise the even zeros as n with n+v having no divisor ≡ −1 (mod v) for every allowed v. [`fingerprint-0107`; med/cheap; U-family, scope, even-n]

108. **Greedy failures (no solution with x = ⌈(n+1)/4⌉) at composites: 1729 (taxicab) and 2641 (pseudosquare)** — Composite greedy failures: 49, 169, 361, 553, 721, 793, 889, 961, 1369, 1393, 1729, 1849, 2041, 2353, 2401, 2449, 2569, 2641, … — *First step:* Check: are greedy failures exactly the n ≡ 1 (24) all of whose 'x=(n+3)/4 divisor pairs' are blocked mod 3 — derive and test closure. [`fingerprint-0108`; low/cheap; greedy, coincidence, 1729]

109. **A segmented word sieve to 10¹⁰ for per-n counts** — The word sieve is O(N log²N); a segmented version (block in n, loop over (t,u) with v-range intersecting the block) gives counts to 10¹⁰ in hours. — *First step:* Implement segmented z52b_fingerprint_words with uint8 saturating counters for I3, R, Uv; run to 10¹⁰ on primes p≡1(4) only. [`fingerprint-0109`; high/medium; engine, scaling, compute-and-check]

110. **min over p ≤ X of R(p)/log²p: does it go to 0?** — R has 14 zeros ≤ 10¹⁰, so inf R/log²p = 0 infinitely often is possible; the empirical lower envelope of R(p)/log²p over primes with R > 0 is a separate fingerprint. — *First step:* Histogram R(p)/log²p near 0 (values 2, 4, 6) for p ≤ 3·10⁶ and compare with Poisson with the BM mean. [`fingerprint-0110`; high/cheap; star-count, lower-tail, poisson]

111. **Poisson test for R(p) given M_BM(p)** — If R(p) ≈ Poisson-like with mean ∝ M_BM(p), P(R=0) ≈ exp(−c M_BM) — at M_BM ≈ 3 (p=409) this gives a few % — test against the 14 observed zeros. — *First step:* Fit P(R=0 | M_BM) by logistic regression on p ≤ 3·10⁶ (needs M_BM for all p; use the script with chunking). [`fingerprint-0111`; high/medium; star-count, poisson, model-check, BM]
