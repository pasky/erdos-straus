# z52b Pass 1 — batch U01 (all 207 items have a line; ES remains OPEN)

1. Counts: nothing 150, covered 27, interesting 14, needs-compute 16, skipped 0 (outcome_U01.jsonl, one line per mid).
2. Interesting: Z0728 (20/p failures on p≡1 mod 120), Z0730 (F(m)⊆F(mk) 39/39), Z0746 (composite failures inherit from a failing prime divisor, 1556/1556), Z0900 (p−1 practical ⇒ harder), Z0969 (residual corr 0.50), Z1416 and Z1735 (greedy two-term completion: lag max at 2521/1201; per-p success rate 0.03–0.75), Z1591 (C-form sign variant and standard give identical failure sets for p≤2000, C≤20), Z1941 (min max-denominator ~p^{1.5}, not p·polylog), Z1944 (4th term rescues to ≈0.75p), Z1282 / Z0893 / Z0894 / Z0355 (F_5[T] engine: irreducible denominators ~4.7× fewer solutions; constant numerator 4 degenerate; non-square twist ×4–5).
3. Needs-compute (16): mostly specs missing or 1–3 h coding (Z0752, Z0739, Z0896, Z0949 ~2–3 CPU-days extrapolated, Z0323, Z0524, Z1322, Z1337, Z1479, Z2483, Z2498, Z2577, Z2909, Z3057, Z1123).
4. HONEST GAP: 65 lines say (in their summary) that part of the first step was not executed — for items whose step was an unspecified analogy/metaphor, or a formal/literature item I did not chase (listed below). They should be re-triaged by the parent; I did not mark them `skipped` because rule 3 only allows restatements/meta.
5. Scripts: `scripts/z52b_p1_U01_*.py` (allsols, stats2, rescue, triples, four, chain, cform, twoterm, ff, practical, isosceles, quick, fingerprint, items_a..f, record). Data gzipped in `data/z52b/pass1/U01/`.

Flagged (summary admits step not run or only partly run): Z0076 Z0104 Z0051 Z0077 Z0228 Z0285 Z0293 Z0315 Z0524 Z0984 Z1123 Z1276 Z1338 Z1360 Z1393 Z1434 Z1646 Z2034 Z2137 Z2185 Z2186 Z2187 Z2188 Z2191 Z2192 Z2193 Z2195 Z2198 Z2199 Z2200 Z2201 Z2202 Z2205 Z2206 Z2207 Z2208 Z2236 Z2484 Z2650 Z2701 Z2776 Z2780 Z2794 Z1051 Z1098 Z1239 Z1315 Z1322 Z1337 Z1506 Z1942 Z2070 Z2086 Z2266 Z2495 Z2550 Z2579 Z2627 Z2773 Z3028 Z3107 Z0725 Z0747 Z2171 Z1731(partial).

## Interesting items

### Z1591 — C-form sign variant
* p+u+v=4Cuv (standard) and p+u−v=4Cuv (sign variant), v=(p+u)/(4Cu∓1). For primes 3≤p≤2000 and C≤20 the sets of primes with no certificate are identical (302 primes; symmetric difference empty). Primes failing all C≤20: 7, 31, 79, 127, 199 (standard), 5, 11 (sign).
* Reproduce: `python3 scripts/z52b_p1_U01_cform.py`. Next: find the bijection or a case (C>20 or p>2000) where they differ.

### Z1735 / Z1416 — greedy two-term completion
* Z1416: x=⌈p/4⌉ works for most primes ≤3000; lag max 5 at p=2521 and 1201.
* Z1735: over primes ≤400, fraction of first terms x giving a two-term remainder: mean 0.192, range 0.031–0.750; lag-1 autocorrelation of the indicator 0.12 (Z3046).
* Reproduce: `python3 scripts/z52b_p1_U01_chain.py 400`, `scripts/z52b_p1_U01_twoterm.py 3000`.

### Z1941 / Z1944 — size of the smallest solutions
* Z1941 (allsols, p≤5000, 667 primes): min over ES triples of max-denominator / p has log–log slope 0.54 in p (dyadic maxima 68, 290, 561, 1014). The (log p)^A hypothesis does not fit this range.
* Z1944 (4th term free, w≤p³, p≤150): min max(x,y,z) ≈0.75p (e.g. p=53: 40 vs 3-term R=742).
* Reproduce: `python3 scripts/z52b_p1_U01_allsols.py 5000`, `scripts/z52b_p1_U01_rescue.py 150`.

### Z1282 — irreducible vs split over F_5[T]
* Mean #ES(T,P), deg 2: irreducible 5.4 (2 of 10 with zero), split 25.2, square 22.6. Next: degree 3–4 with the same split.

### Z0728 — 20/p failures and p ≡ 1 (mod 120)
* Failures of 20/p (= 4/p with all denominators divisible by 5) at primes 5<p≤1e5: 60 (plus 2,3,5). Last 90001.
* Residue classes: 33/60 are p≡1 (mod 5) (base 25%). 21/60 are p≡1 (mod 120): 21 of 286 such primes fail (7.3%), vs 39 of ≈9300 others (0.4%).
* Reproduce: `python3 scripts/z52b_p1_U01_fingerprint.py`-style counts on `data/z52b/raw/m20_pr1e5.txt` (column 2 = U).
* Next: is the mod-120 enrichment a character-sum effect? Extend to p≡1 mod 120 up to 1e6.

### Z0730 / Z0746 — divisibility structure of failure sets
* For m|mk (m,mk ≤48, p≤1e5): F(m) ⊆ F(mk) in 39/39 nontrivial pairs (e.g. F(8)={2,3,11,17,131,241} ⊆ F(16)); the reverse inclusion fails.
* Composite n≤4000, m=5..48: 1556 composite failures, all with a prime q|n such that m/q fails (0 exceptions). The converse fails heavily (137775 composites have a failing prime divisor, 1556 fail).
* Reproduce: `gcc -O2 -o /tmp/c scripts/z52b_fingerprint_count.c -lm; /tmp/c m 2 4000 0` for each m; then compare.

### Z0900 — p−1 practical and ES hardness
* Over primes 5<p≤3e4 (3242 primes, data/z52b/raw/f4_all_30000.txt): mean residual of log(U4+1) (quadratic in log p) is −0.31 when p−1 is practical, +0.17 otherwise.
* 0 of the 30 hardest primes have practical p−1 (null ≈0.65^30 ≈ 1e−6). Effect persists in classes mod 8 and mod 24.
* Reproduce: `python3 scripts/z52b_p1_U01_practical.py`.
* Next: control for divisor-count of p−1 (compare with random n of the same ω), and test for hard primes with p−1 having a large prime factor.

### Z0969 — U(p) vs U((p+3)/4)
* 271 pairs (p, (p+3)/4 prime), p≤3e4: raw Spearman 0.657 (matches item). Pearson of residuals after a quadratic in log p: 0.50.
* Next: partial out p mod 8 and the 2-adic class of (p+3)/4; compare with random prime pairs of similar size.

### Z1416 — greedy first term and two-term completion
* For primes ≤3000, the smallest x≥⌈p/4⌉ with (4x−p)/(px) a sum of two unit fractions is found for all 428 primes checked in the window. Lag median 0, mean 0.09, max 5 at p=2521 and p=1201; then 3 at p=2689.
* Reproduce: `python3 scripts/z52b_p1_U01_twoterm.py 3000`.
* Next: run to 1e6; test whether lag≥3 concentrates on the top-30 hard primes.

### Z0355 / Z0893 / Z0894 — function-field engine (F_5[T], scripts/bs_ff_es.py)
* Constant numerator 4: 0 solutions for every monic P of degree 3 and 4 (lc(4X−P)=3 ∉{1,2}, the engine's lc condition). Constants 1,2,3 give 159240, 41070, 5000 at deg 3.
* Non-square twist A=2T vs A=T: total #ES over monic deg-3 P 4110 vs 16450 (×4.0); deg 4: 82350 vs 416223 (×5.1). Over irreducibles: mean #ES(T,P) 5.4, 25.6, 56.8 (deg 2,3,4); T/2T ratio 3.4, 6.4, 9.2.
* Square-at-linear-primes P (P(c) a nonzero square ∀c∈F_5, deg 5): mean #ES 659 vs 2361 for 200 random monic deg-5 P (A=T).
* Reproduce: `python3 scripts/z52b_p1_U01_ff.py` (takes a few minutes).
* Next: check whether the lc lemma is already in EXSET_FUNCTION_FIELD.md; if the FF "4/P" analogue is degenerate, use numerators with lc∈{2,3}.

## Notes on non-interesting outcomes (for the record)
* Z0973 isosceles criterion (m-general): m/p has x=y solutions (p≠m) iff m | p+1, m | p+2, or m | 2p+1. Verified by brute force for p≤200, m∈{4,5,7,8}, and independently by the counter's V7 column on 9592 primes for m=5.
* Z0743/Z0744: 8/p and 12/p failure sets disjoint for primes 3<p≤1e5.
* Z0740: failure counts reproduce the item's sequence; regression R²=0.974 is just growth in m.
* Z1877 (multiplicative variant): 397/400 primes ≤2000 without solution under a bounded search (x,y≤2p); caveat: bounded.
* Z3073/Z0310/Z1639: 4→3 merge is exactly the 3-term ES condition (split/merge identity), no new handle.
* Erdős-page items (Z2153–Z2203): statements read from erdosproblems.com; none is an ES-count statement.
