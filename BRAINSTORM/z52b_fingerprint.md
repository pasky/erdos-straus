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

Item count: 50. Tag histogram (top 45): hard-primes 7, oeis-match 6, oeis-gap 6, mordell-classes 5, anchor 4, min-denominator 4, type-I 4, type-II 4, small-values 3, oeis-null 3, least-qnr 3, class-number 3, star-count 3, x-distribution 3, records 3, counting 2, parity 2, trivial-but-true 2, lcm-plus-one 2, pseudosquares 2, L-function 2, real-quadratic 2, twist 2, complementarity 2, null-result 2, sanity 2, p-minus-1 2, smoothness 2, divisor-function 2, lemma-candidate 2, height 2, lcm 2, 840 2, distinct 1, primes 1, m-over-n 1, sierpinski 1, involution 1, value-set 1, lower-bound 1, calibration 1, first-occurrence 1, type-A 1, record-low 1, extremal 1


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

18. **(★) count R(p) correlates with h(−4p) (α ≈ +0.38, R²-gain 0.20)** — The c=1 Type-II line R(p) = #{4uBC−u−B=p} fits log R ≈ … + 0.38 log L_Q(1,χ_{−4p}) (gain 0.20) and only −0.17 on χ_p (gain 0.09). — *First step:* Regress R(p) (not log) on h(−4p), h(−8p), h(−3p), h(−12p) for exact linear relations at small p (integer-relation search with PSLQ on vectors). [`fingerprint-0018`; high/cheap; class-number, star-count, hurwitz, theta]

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
