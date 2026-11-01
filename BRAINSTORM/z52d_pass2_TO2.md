# z52d Pass 2 — batch TO2 (101 "touched" items; ES is OPEN, nothing here is a proof of ES)

**Summary (5 lines).**
1. Counts (101 items): interesting 14, covered 15, nothing 72, needs-compute 0, skipped 0. Every input line has one line in `data/z52b/pass2/outcome_TO2.jsonl`.
2. Interesting (numbers in sections below): Z0510 (chain x|y|z variant fails exactly at primes with (p+1)/2 composed of primes ≡1 mod 4; PROVED criterion), Z0511 (minimal max-denominator exponent ≤ 1.9 for p ≤ 2·10⁵), Z0521 (minimal denominator within 0.114·log²p of p/4), Z0534 ((★) minimal modulus ≈ p/8 at p=184837), Z0543 (bounded-d Type I residue classes cover 99.5% of primes ≡1 mod 24 ≤1e6, d≤50), Z0559/Z0566 (P(U_m(p)=0) calibration; smallest failing m in (m²,2m²) is m=10), Z0616 (slice events E_1,E_2 negatively correlated), Z0628 (R(p) over-dispersed, ≈2× Poisson), Z0673 (no Type I witness with (d/p)=+1 in 13,311 tests), Z0681 (O(n) odd ⟺ n≡2 mod 4 to 30000), Z0692 (log R ~ 0.40·log h(−4p) at fixed size), Z0472 (near-square enrichment of (★)-zero primes), Z0513 (odd exceptions to p+2^a+2^b are only n=3 up to 1e8 with a,b≥0 — conflicts with a literature claim to be checked).
3. Covered by existing repo depth documents: Z0476, Z0477, Z0479, Z0480, Z0481, Z0486, Z0487, Z0499, Z0531, Z0538, Z0595, Z0598, Z0631, Z0639, Z0691.
4. Premise problems recorded: Z0519 (smooth ES impossible for p > smoothness bound: denominator argument), Z0482 and Z0522 (mis-cited arXiv ids), Z0473/Z0512 (arXiv:0901.3075 is Sun's mixed-sums paper), Z0473 (repo path wrong), Z0673 (claim not in T1_TEMPLATE.md).
5. Not done (declared per item in outcome_TO2.jsonl): Vose 1985, Duke 1988, Crocker 1971, Pan 2011, Colliot-Thélène–Wittenberg texts; Q(√2) search (Z0518); U(p) at 2.3·10⁸ (Z0686); 1e7 record extension (Z0685).

Method: repo count outputs (`data/z52b/raw/*`), new exact C enumerations (`scripts/z52d_p2_TO2_*.c`), analysis scripts `scripts/z52d_p2_TO2_an*.py`; outputs `data/z52b/pass2/TO2/`.

---

## Z0510 — restricted denominators: the chain (x | y | z) variant (interesting)

Enumerated all unordered solutions of 4/n for n ≤ 5000 (`scripts/z52d_p2_TO2_restr.c`). Failing n for x|y|z: 45 values, **all primes ≡ 1 (mod 24)**, i.e. 45 of the 76 such primes ≤ 5000: 73, 193, 313, 337, 409, 457, 577, 673, 1009, … 2521, … 3361, … 4657.

**PROVED criterion (elementary).** For a prime p ≡ 1 (mod 4): 4/p = 1/x+1/y+1/z with x|y|z is solvable iff (p+1)/2 has a prime factor ≡ 3 (mod 4).
*Sketch.* Put y = kx, z = lkx; then 4xkl = p(kl+l+1). If p∤kl, then p | x and 4x'kl = kl+l+1 forces 3kl ≤ l+1, impossible. If p | k (k = pk'), then l = 1 and 4k'x = pk'+2, which forces k' ∈ {1,2} and p ≡ 2 or 3 (mod 4), excluded. So p | l, and l = pl' forces l' = 1: the solutions are exactly l = p, x = (p(k+1)+1)/(4k), with 4k | p(k+1)+1. Then k | p+1 and, writing s = (p+1)/k, the condition is 4 | p+s; for p ≡ 1 (mod 4) this says s ≡ 3 (mod 4) divides (p+1)/2. ∎
Verified against the enumeration for all primes ≤ 5000 (zero mismatches).

So the chain variant fails exactly on p ≡ 1 (mod 8) whose (p+1)/2 has only prime factors ≡ 1 (mod 4). Heuristically such p have density ≍ (log x)^{-3/2} (numbers with prime factors in a half-density set), so the failure set is thin and possibly infinite. **Next:** decide whether infinitely many p have (p+1)/2 composed of primes ≡ 1 (mod 4) (a shifted-prime question), and whether any ES-type statement with divisibility constraints inherits this obstruction.

Other restrictions (n ≤ 5000): squarefree denominators fail at 1199 n (first n=9); exactly one even denominator fails at 4374 n; all three ≡ 1 (mod 4) fails at 4688 n; pairwise coprime never holds (PROVED: S = xy+yz+zx would divide 4, and S ≥ 3 with S=4 impossible).

## Z0511 / Z0624 — size of the minimal solution (interesting for Z0511)

From repo counts, primes p ≡ 1 (mod 4), 5 < p ≤ 2·10⁵: z_min (smallest max-denominator) satisfies z_min > p^{1.5} for 74% of primes, z_min > p^{1.75} for 0.35%, and never z_min > p^{1.9}; the worst exponent is 1.89 at p = 1201. z_min/p² ≤ 0.50 (max at p = 577), median 0.006.

## Z0521 — minimal denominator (interesting)

x_min − p/4 ≤ 0.114·log²p for all p ≡ 1 (4), p ≤ 2·10⁵ (median 0.006 log²p), x_min/p ∈ [0.250, 0.308], x_min − p/4 ≤ √p throughout. (Note x > p/4 always; the content is the width of the window.)

## Z0534 — no polylog bound for the (★) witness modulus (interesting)

Minimal C over (★) triples (4uBC − u − B = p), all p ≡ 1 (4), p ≤ 10⁷: 99% have C_min ≤ 0.036 log²p, but C_min(184837) = 23105 ≈ p/8 (the unique witness is (u,B) = (1,2), C = (p+3)/8), giving max C_min/log²p = 157. The (★) subfamily has no Linnik-type bound; the full Type I ∪ II families were not checked.

## Z0543 / Z0673 — Type I residue coverage and the (d/p) constraint (interesting)

With the grid a ≤ 50, the classes −f mod 4ad (f | 4a²d+1) cover 50.5% (d ≤ 5), 69.8% (d ≤ 10), 95.8% (d ≤ 20), 99.5% (d ≤ 50) of primes p ≡ 1 (mod 24) ≤ 10⁶ (upper bound on exact coverage; exact when f ≤ p/2).
Numerically, among 13,311 Type I witnesses (f ≤ p/2, b ≥ a, a,d ≤ 50, 1038 primes ≡ 1 mod 24 in [10⁴,10⁵]), none has (d/p) = +1. The T1 template does not record this (grep), so the necessity of (d/p) = −1 is an empirical lead needing proof.

## Z0559 / Z0566 / Z0514 — Schinzel/Pomerance–Weingartner family (interesting for Z0559, Z0566)

From repo counts U_m(p) for m = 5..48, primes ≤ 10⁵:
* m/p with p ∈ (m², 2m²) not a sum of three unit fractions: smallest m is **m = 10, p = 181** (exact brute force agrees: no solutions for 10/181). Failures exist for 37 of 44 m; none for m ∈ {5,6,7,8,9,11,19}.
* Calibration: over the 33 m with failures and p ∈ (10⁴, 10⁵], log P(U_m(p) = 0) ≈ −2.75 − 0.071·(log p)³/m (R² = 0.58). Consistent with a Poisson-type exponent in (log p)³/m; the intercept says it is not pure Poisson. The m = 4 extrapolation predicts no ES failures in this range, which matches the data.
* Reproduced PW's largest exceptions for m = 8, 12, 15 (241, 12241, 20521). The largest-exception scale (log p)³/m varies (20–91) and is not constant.
* The m = 12 anomaly is mostly size-driven (Spearman with (log p)³/m: −0.92 over m ≥ 12; with τ(m): +0.40).

## Z0616 — slice correlations (interesting)

Events E_C(p) = [slice C carries a (★) triple], C = 1..8, over 39,174 primes ≡ 1 (4) ≤ 10⁶: P(E_1) = 0.76, P(E_2) = 0.51, P(no slice ≤ 8 hit) = 1.3%. Mean off-diagonal correlation −0.016; corr(E_1, E_2) = −0.14 overall and −0.13 to −0.21 within size windows. This is the negative-coupling lead in the item (not tested against Type I events yet).

## Z0628 / Z0629 — over-dispersion of R(p) (interesting)

For p ≡ 1 (mod 24): var/mean of R(p) = 3.66 on [10⁵, 10⁶) and 4.13 on [10⁶, 10⁷). R counts ordered pairs, so R/2 is the unordered count and has var/mean ≈ 1.83 and 2.06 — clearly over-dispersed relative to Poisson (≈1). The clustering comes from the divisor pairs within C-slices.

## Z0681 — parity of ordered solution counts (interesting)

O(n) (ordered solutions of 4/n) is odd iff n ≡ 2 (mod 4), verified for all 2 ≤ n ≤ 30000 (0 mismatches; `data/z52b/raw/f4_all_30000.txt`). U(n) itself is ~50/50 on n ≡ 2 (4), so only the ordered count has the law. Proof not written (isosceles counting).

## Z0692 — class-number dependence of (★) counts (interesting)

Over 8,969 primes p ≡ 1 (4) ≤ 2·10⁵: log R(p) = 0.396·log h(−4p) − 0.008·log p + const (R² = 0.36; log p alone gives 0.21). Adding h(−8p) and h(−3p) raises R² only to 0.38, so {−4} is the essential twist. Only R (the (★) subfamily) was used.

## Z0472 / Z0484 — near-square and special-form primes (interesting for Z0472)

Exact R(p) for all 332,180 primes p ≡ 1 (4) ≤ 10⁷: the 14 zeros are 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 (= FRONTIER.md:103). Three of the 14 are within 10 of a square (409 = 20²+9, 577 = 24²+1, 9601 = 98²−3), versus 0.6% of primes (expected ≈ 0.09 zeros; Poisson P ≈ 10⁻⁴). Odd squares: R(m²) = 0 for all 1580 odd m² ≤ 10⁷ (T1 for the (★) shape). Full Type I/II counts for these primes not yet computed.

## Z0513 / Z0512 / Z0590 — exceptions to p + 2^a + 2^b (interesting for Z0513)

Exact sieve: odd n ≤ 10⁸ not of the form p + 2^a + 2^b (a, b ≥ 0): only n = 3 (verified in Python up to 2·10⁵). With a, b ≥ 1: n ∈ {3, 5, 6495105}. For three powers (a,b,c ≥ 0) up to 10⁷: only n = 3. The repo's citation of a ≫ x^{1−ε} exception count (BRAINSTORM/s9_lower_tail_literature.md:17) does not match these data; the normalisation must be checked against Pan (2011). arXiv:0901.3075 is Sun's "Mixed sums of primes and other terms", not Crocker's paper.

## Z0686 — lcm(1..19)+1

232792561 is prime. R = 22 (so not a (★) failure), f_I = 254, f_II = 111 (`data/z52b/pass2/TO2/fIfII_232792561.txt`). U and the b = 1 test not run.

## Non-interesting but checked

* Z0528 / Z0531: exact f_I, f_II for all 9,732 primes ≡ 1 (24) ≤ 10⁶: no zeros. Correlation positive (Pearson of logs +0.88; residual +0.75), agreeing with BRAINSTORM/corr_typeI_typeII_joint.md §4.
* Z0565: h(−4p) mod 8 shows no effect on mean R (0.171, 0.176, 0.169, 0.177).
* Z0683–Z0685: U(p) ≤ 4 only for p ∈ {2,3,5,13,17} (p ≤ 2·10⁵); least prime with U = 6 is 193; records of U/log²p over primes ≥ 50 are 53, 61, 73, 193, 2521 (with p < 50 the records are 3, 5, 13, 17, which is why the item's list starts at 53).
* Z0690: per-q regression weights for U(p): q=2: −0.30, 3: −0.30, 5: −0.46, 7: −0.11, 11: −0.35, 13: −0.06 (R² = 0.73); not uniform; collinearity not controlled.
* Z0696 / Z0579 / Z0580: tie-aware Spearman of U(p) with #QNR ≤ log p = +0.66; with least QNR −0.48; with least primitive root −0.42.
* Z0478, Z0515, Z0527: m-family details above.

