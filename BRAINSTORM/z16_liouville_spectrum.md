# z16_liouville_spectrum — which levels a point protects from balanced tuples: the approximation profile η_u (O241)

## Idea
Generalise O227's Liouville lemma from polynomial points to all u via the approximation profile
η_u(D) = least height of a rational agreeing with u to order D. Theorem (STERILE_DIOPHANTINE Thm 4.2, PROVED): a tuple covering
x_u at level N has height H_τ ≥ N + 1 − η_u(N + 1) unless −w₁/C₁ is the best approximant itself. Level N is *protected*
from the thirds corner (H_τ ≈ 2(N + 1)/3) when η_u(N + 1) < (N + 1)/3. Cor 4.3 (PROVED): only rational points are protected at
all large levels; T-adic Liouville numbers are protected outside thin windows (D_h, 3h'] at each new convergent.

## Literature
Mahler, On a theorem of Liouville in fields of positive characteristic, Canad. J. Math. 1 (1949) 397–400; Lasjaunias, A survey
of Diophantine approximation in fields of power series, Monatsh. Math. 130 (2000) 211–229; Schmidt, On continued fractions and
Diophantine approximation in power series fields, Acta Arith. 95 (2000) 139–166. ℤ twin: M17D Lemma 2.2(iii) (O139).

## Barrier screen
B5/T1: FF model, no Type I/II count. B3: the protected levels remove the super-critical thirds corner exactly (O227 §7 grid:
restricted exponent 0.000), but what remains at a protected level is a single-point lottery (lopsided tuples), so no union bound
can close it (a point has measure 0). B6: pointwise by construction.

## Cheap numerics
`scripts/z16_points.py` (alive-to-depth-9 fraction of rational points of height ≤ 3 vs the cylinder average 0.517) — see
STERILE_DIOPHANTINE §6.

## Assessment
PROVED (Lemma 4.1, Thm 4.2, Cor 4.3, 4.4); continued-fraction window description Assessment. Explains exactly which points
can be "Liouville-sterile": rational ones (all levels) and Liouville-type ones (most levels).
