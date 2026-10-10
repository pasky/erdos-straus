# POINTWISE_SPECTRAL — "flip the average": fixed p, average over the Type I parameters (task O123)

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6. Type I coordinates (ET Prop 2.2/2.3):
`p = 4acd − f`, `f | 4a²d+1`, `e = (4a²d+1)/f`, `b = (pa+c)/f`; equivalently `pe + 1 = 4abd`, `e | a+b`
(c = (a+b)/e). Type II (ET Prop 2.6/2.7): `p + e = 4abd`, `e | a+b`. Throughout f_I(p), f_II(p) count
solutions (x,y,z) with y ≤ z (each once; normalisation a ≤ b, gcd(a,b,c) = 1).

## 1. Numerics (EVIDENCE)

Script `scripts/spec_typecount.c` (exact counts for all n ≤ N; sieve factorisation of 4a²d+1 in two regimes,
a ≤ √N linear in d, a > √N quadratic in a), validated against brute force (`scripts/spec_brute_validate.py`:
all primes ≤ 400, both types, 0 mismatches). Statistics: `scripts/spec_stats.py`, output
`data/spec/t1e7_stats.txt`.

**Result (p ≤ 10⁷, all 664 578 odd primes):** `f_I(p) ≥ 1` and `f_II(p) ≥ 1` for every p; even the a = 1
sub-family (`p = cef − c − f`, `ef ≡ 1 mod 4`, ET Remark 2.5) is non-empty for every p ≡ 1 (mod 4)
(consistent with the literature check of that sub-family to 10¹⁴ cited by ET Remark 2.5). So **numerically Type I
alone always works**; the question "which p fail Type I" has no answer below 10⁷.

Dyadic windows [X, 2X) (L = log(1.5X)):

| X | min f_I (at p) | mean f_I | mean/L² | min f_I/L | min f_II | min f_I^{a=1} (p≡1 mod 4) |
|---|---|---|---|---|---|---|
| 2¹⁰ | 7 (1201) | 52.2 | 0.97 | 0.95 | 4 | 1 |
| 2¹⁴ | 14 (20521) | 114.9 | 1.12 | 1.38 | 9 | 1 |
| 2¹⁸ | 35 (471241) | 220.8 | 1.33 | 2.72 | 17 | 3 |
| 2²⁰ | 57 (1092961) | 291.5 | 1.43 | 3.99 | 18 | 2 |
| 2²² | 62 (4889641) | 376.2 | 1.54 | 3.96 | 30 | 1 |

* All window minimisers from 2⁹ on are Mordell-hard (p mod 840 ∈ {1,121,169,289,361,529}).
* The minimum tracks the mean: min/mean ≈ 0.16–0.2, stable over 2¹² … 2²². mean f_I ≈ 0.1·L³ (ET: Σ_{p≤N} f_I ≍ N L²).
  So min f_I grows like a power of log p (fit ≈ L^{2.5}·const is indistinguishable from c·L³ here); the
  pointwise count is "polylog with a robust constant fraction of the mean".
* The a = 1 sub-family alone has minimum 1–3 throughout: the full 3-parameter family is needed for growth.
