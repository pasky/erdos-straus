# s9_ladder_thinning — the numerator ladder as one thinning ladder on the numerator-free word set (O271, own)

## Idea
(J)97 found a universal zero law across numerators m/p (Type II ladder). By SYNTHESIS_SPARKS9 Cor 1.2 the two-line union for
k/p is "some word of p has a coordinate ≡ 0 (mod k)": every numerator thins the SAME set W(p). Test whether a mirror-binomial
thinning of W(p), with the cell-mean thinning rate π_k, predicts the k-union failure counts across k.

## Literature
DISPROOF_AVENUES (J)97 (zero law P(f = 0) ≈ exp(−0.535 μ^{0.91})); O268 (zero rate 1.5–15× swap-Poisson at fixed M_BM8).

## Barrier screen
Model-level only (B6: a law over p says nothing at one p). T1: π_4 ≡ 0 at squares (the thinning degenerates there), so any
thinning law must be conditioned on σ, not on k alone. Numerator models: the ladder includes k = 8 (failures 131, 241 ✓).

## Cheap numerics
`scripts/s9_ladder_thinning.py 1000000 4 6 8 10 12 16 20 24 32` (`logs/s9_ladder_thinning.txt`), all primes ≤ 10⁶:
| k | mean π_k | observed union failures | thinning prediction | obs/pred |
|---|---|---|---|---|
| 4 | 0.431 | 0 | 0.5 | — |
| 6 | 0.259 | 36 | 10.3 | 3.5 |
| 8 | 0.208 | 56 | 14.1 | 4.0 |
| 10 | 0.159 | 210 | 29.6 | 7.1 |
| 12 | 0.119 | 528 | 187 | 2.8 |
| 16 | 0.094 | 1198 | 330 | 3.6 |
| 20 | 0.072 | 2849 | 657 | 4.3 |
| 24 | 0.053 | 5904 | 3439 | 1.7 |
| 32 | 0.042 | 9935 | 3981 | 2.5 |

## Assessment
EVIDENCE: the thinning model gets the order of magnitude across a 10⁴-fold range of failure counts, but under-predicts by
1.7–7×, non-monotonically in k (k = 10, 20 worst: their thinning rate is not captured by p mod 24 cells). Same direction as O268's
excess over swap-Poisson: the 2-adic thinning is overdispersed. A heuristic unification of the ladder (one size variable W, one
thinning rate per k), not a mechanism and not a law with a universal constant. No route.
