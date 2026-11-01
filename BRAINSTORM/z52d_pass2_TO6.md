# z52d Pass 2 — batch TO6 (101 "touched" items, Pass 1 absent)

**Counts (101 input lines, 101 output lines in `data/z52b/pass2/outcome_TO6.jsonl`, lint 0 flagged):** interesting 7 · covered 3 · nothing 91 · needs-compute 0 · skipped 0.
**Interesting:** Z2035 (8/n 3-term failure control set), Z2048 (first witness = factoring a ~p-size integer), Z2021 (witness absence is ≈0.4× the independence prediction), Z2123 (Lenstra threshold t ≳ √p vs witness location), Z2215 (3-term failure sets k/n, n ≤ 60000), Z2357 (union-of-lines failure phase: zero failures from 43 lines, t ≤ 171), Z2367 (classes of 4/m² solutions; prime m never has exactly one denominator divisible by m).
**Covered:** Z1997, Z2292 (FF large-q refutation, Thm 2.1), Z2029 (BRAUER_TWISTS §(0)).
**Honesty note:** 93 items are `nothing` but most of them were NOT executed: they are literature/analysis items that I did not finish in this pass. Each such record says so in `not_done`. They are not evidence of emptiness. Premise failures found are listed below.

## Method / scripts
- `scripts/z52d_p2_TO6_egypt3.c` — exact 3-term Egyptian fraction test/count for k/n (x ≤ y ≤ z), 128-bit arithmetic. Cross-checked against brute force (primes ≤ 37) and the Python recursion `scripts/z52d_p2_TO6_egypt4.py` (4-term and 3-term, n ≤ 300).
- `scripts/z52d_p2_TO6_tmin.c`, `..._lenstra_regime.c` — minimal Type-I slice parameter t (CONDITIONAL_ES.md §1, Lemma 1.1) for all p ≡ 1 mod 4 ≤ 10⁶; reproduces the repo's t = 367 at p = 830041.
- `scripts/z52d_p2_TO6_analysis.py`, `..._control.py` — R(p) vs least non-residue, total splitting, mod-840 controls.
- `scripts/z52d_p2_TO6_quick.py`, `..._signed.py`, `..._sqclass.py`, `..._typeI_II.py` — smaller exact checks.
- Data in `data/z52b/pass2/TO6/` (< 1.5 MB total).

## Interesting items

### Z2035 — numerator-8 control set
Exact 3-term check: 8/n has no representation for n ∈ {2, 3, 11, 17, 131, 241} and for no other n ≤ 60000. Among primes > 3: 11, 17, 131, 241 (the record's list). Cross-checked with the independent Python recursion for n ≤ 300. Reproduce: `gcc -O2 -o egypt3 scripts/z52d_p2_TO6_egypt3.c && ./egypt3 8 60000 fail`. Next: run each tool in the lane on 8/11, 8/17, 8/131, 8/241.

### Z2048 / Z2123 — what the Type-I witness search costs (Lenstra regime)
Witness parameter: tp+1 = m·m″, m ≡ m″ ≡ −1 (mod t), 4 | m (Lemma 1.1). Over all 39,175 primes p ≡ 1 (mod 4) ≤ 10⁶:
- minimal t: median 3; max 407 (p = 601849); t_min ≥ p^{1/4} for 0.89 %; t_min ≥ √p for 5 primes (5, 17, 41, 241, 21169; these are exactly the primes with no witness below √p).
- Lenstra/Hales regime (S³ > N with S = t, N = tp+1 ⇔ t ≳ √p): within t ∈ [√p, 4√p] (t ≡ 3 mod 4), 86.3 % of the 8,977 primes ≡ 1 (mod 4) below 2·10⁵ have at least one witness (median count 2); 13.7 % have none there and must use a smaller t.
- Reading: a polynomial-time method at t ≥ √p would find witnesses for most primes, but the minimal witnesses sit at small t where the guarantee does not apply, and at small t the test is factoring tp+1 (≈ p-size). Not measured: any timing at large p.
Reproduce: `./tmin 1000000 3000` and `./lens 200000`.

### Z2215 — largest 3-term failure n for numerator k (cutoff 60000)
Failing n for k/n = 1/x+1/y+1/z (k = 3…40, all n ≤ 60000): k=3–6 none; k=7: {2}; k=8: 6 failures, max 241; k=9: max 19; k=10: max 181; k=11: max 37; k=12: 23 failures, max 12241; k=13: max 281; k=14: 841; k=15: 20521; k=16: 36529. For k ≥ 27 the max is near the cutoff, so n(k) is not determined. Failure density at k=40: 461/60000 (≈0.8 %). The PW prediction (arXiv:2511.16817: a prime p ∈ (m², 2m²) with m/p not a sum of 3 unit fractions, for m ≥ 20) is confirmed for every m = 20…40 (e.g. 401 for m=20, 1051 for m=29 …). Data: `data/z52b/pass2/TO6/egypt3_fail_k3-40_n60000.txt`.

### Z2367 — the 4/m² classes
For odd m ≤ 61 (primes) and composite m up to 81: classified all sorted solutions of 4/m² by the number of denominators divisible by m.
- Prime m: never exactly one denominator divisible by m (classes (1,·) absent for m = 3…61). This is the Type-I absence the T1 picture predicts at squares. Fully divisible solutions correspond to 4/m solutions (m=7: 7 = #solutions of 4/7).
- Composite m: exactly-one classes occur (m=9: 6+11; m=15: 91+37; m=21: 193+56).
- Record claim "every solution of 4/m² is a scaled solution of 4/d, d | m" is false: m=9 has 46 solutions; gcd(x,y,z) ∈ {9, 27} for only 5 of them (scaled from 4/9 or 4/3), and 9 are primitive.
Reproduce: `uv run --with sympy python scripts/z52d_p2_TO6_sqclass.py 61`.

## Premise corrections found in this batch (for the record)
1. **Z2040 / Z2361 (Elsholtz–Tao):** their theorem is Σ_{p≤N} f(p) ≍ N log²N (up to a log log factor), so the average over primes is ≈ log³p. The record's "Σ_{n≤N} f(n) ≍ N log³N" is wrong as stated (abstract arXiv:1107.1010).
2. **Z2033:** the title holds only for p ≡ 1 (mod 4). For p ≡ 3 (mod 4) diagonal solutions always exist (x=y=(p+1)/2, z=p(p+1)/4); for p ≡ 1 (mod 4) the absence is an elementary proof (a(4z−p)=2p² with a ∈ {2,2p,2p²}).
3. **Z2050 / Z2023:** the total-splitting and least-non-residue effects on R(p) are entirely the Mordell square classes mod 840 (residual correlation −0.015; split∧non-square-mod-840 mean 124 ≈ nonsplit 123).
4. **Z2036 / Z2370 / Z2334:** signed nonzero-integer solutions of 4/p are finite in practice: for p = 13 the count is 120 for every bound in [3000, 10⁴] (24 positive, 63 with exactly one negative). The record's "count grows polynomially" is false.
5. **Z2140 / Z2258:** the "nontrivial" involution d ↦ b²/d in the fixed-x fibre (a y − b)(a z − b) = b² is exactly the transposition y ↔ z. The ES surface is linear in x, so no Vieta root swap exists.
6. **Z2028 / Z2085 (Crocker):** brute force finds only n = 1, 3 as odd exceptions up to 2·10⁵; literature (arXiv:2607.05357) gives N(x) ≫ log log x, so the exceptions start far beyond the computed range.
7. **Z2031 (BHV):** primitive-divisor results apply to Lucas values with index n; tp+1 is not a Lucas value in general.
8. **Z2286:** the cited arXiv:2302.02143 is Tall's Scholz-conjecture paper (addition chains), not a general certificate bound.
9. **Z2136:** arXiv ID should be math/9811112 (G. Martin, "Denser Egyptian fractions").
10. **Z2366 / Z2032 (two-term ladder):** 2-term criteria verified: 3/p two-term iff p ≡ 2 (mod 3) or p = 3; 4/p two-term iff p ≡ 3 (mod 4).

## Not done (summary)
Most `nothing` records: literature-only items (Z2012, Z2013, Z2015, Z2063, Z2072, Z2095, Z2100, Z2110–Z2113, Z2133, Z2136, Z2146, Z2147, Z2154, Z2230, Z2253, Z2276, Z2281, Z2379, Z2383, Z2415) and analysis items not started (Z2019, Z2021, Z2056, Z2062, Z2071, Z2107, Z2122, Z2125, Z2132, Z2267, Z2302, Z2310, Z2327, Z2337, Z2346, Z2357, Z2359, Z2369, Z2376, Z2377, Z2396, Z2398, Z2409). Each record's `not_done` field says what was missing. No lattice (Coppersmith / Hales) implementation was run (Z2016, Z2121, Z2122). The 4-term ladder beyond m=8 and the k ≥ 27 cutoff extension to 10⁶ are the most useful follow-ups.

## Lint-fix round (25 flagged items, `scripts/z52d_p2_TO6_fix_*`)
Each flagged item got an executed step; the lines were replaced, the others untouched. Lint: 0 flagged.
- **Z2021 (interesting):** witness lines are positively correlated: P(no witness in lines t ≤ 63) = 0.00078 vs 0.00196 under independence (ratio 0.40); variance 5.92 vs 4.93. Data: `witness_stats_TO6.json`.
- **Z2357 (interesting):** failures F_k of the union of the first k lines: 2140, 123, 33, 7, 2 at k = 1, 4, 8, 16, 32; F_43 = 0 (t ≤ 171); fitted slope −0.49 per line.
- Characters (Z2062, Z2107, Z2310, Z2337): real (order ≤ 2) characters of (Z/840)* explain R² = 0.84 of the class means vs a 0.16 shuffle null; non-real part not resolvable at this sample.
- Z2071: the Legendre singular-series product correlates 0.42 with R/log²p but 0.02 after the mod-840 class mean.
- Z2095: Graham's 77 threshold reproduced by exact search (no set at m = 77, sets at 78–80); the problem class differs from ES.
- Z2122: Hales Thm 1.1 covers Z[i] with the same |S|³ > |N| threshold; no new regime for integer witnesses.
- Z2125: F₅[T] nondegenerate solutions exist for deg P = 1 (e.g. 4/(T+2) = 1/T + 1/(T+3T²) + 1/(2T)); monic-denominator solutions absent (consistent with Prop 1.2).
- Z2132/Z2267: M(u)M(t)M(v) ∈ SL₂(ℤ) has (0,0)-entry tuv − u − v; the congruence word exists for 146 of 147 primes p < 2000 (p ≡ 1 mod 4).
- Z2302/Z2056: rational parametrisation (birational, verified in sympy); integral points are a ~2·10⁻⁵ density subset of the box.
- Z2359: depth of p/4 in the Stern–Brocot tree is ~p/4 (unbounded); the regular CF of p/4 is trivially length 2 — the record's λ(p) must mean a different expansion.
- Z2276, Z2409: witness-line densities are not equidistributed mod 105/1155; the t=3 correlation with (2/p) is the mod-8 effect (p ≡ 5 mod 8 always witnessed at t=3).
- Z2346: Kronecker's identity verified to 10⁻³⁰; the (K1′) completion itself not checked.
- Z2396: DFI joint χ² = 2.49 (9 dof) for D = 12.
- Z2376/2377: at-least-m witness counts match the independence (Poisson-binomial) prediction to ~0.01.
- Z2374: every sampled prime has a small prime q ≤ (log p)² in class −1 mod t (t ≤ 63) dividing tp+1; cofactor condition not checked.
- Z2327: no quaternion treatment found; Z2398: Bettin–Chandee bounds are averaged over moduli, the ES phase is linear in p and t — no pointwise route found.
- Z2369: top R/log²p values lie in non-Mordell classes.
