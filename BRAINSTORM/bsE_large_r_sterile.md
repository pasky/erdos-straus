# bsE_large_r_sterile — sterile points exist for every large Mordell prime r (O178)

## Idea
Translate Thm 2.5 back: T ↦ r, slice point ↦ r-generic point (x_q = 1 for q ≠ r). MORDELL17 already reduced sterility at r = 17 to
the measure inequality S(17) < 0.677 with S built from f(r^k) and Type II N-point counts at half level. It failed only on explicit
constants. For general r the same series S(r) → 0 by the exponents 2/3+ε (Browning–Elsholtz, all non-P boxes) and 2/5 (ET, P-boxes) against weights r^{−k} and r^{−⌈K/2⌉}, after
averaging over the (r − 1)/2 non-residue cells (DEPTH_ASPECT Thm 3.1).
## Literature
Elsholtz–Tao Prop 1.7 and §3; Browning–Elsholtz, Illinois J. Math. 55 (2011); POINTWISE_MORDELL §2.1; POINTWISE_MORDELL17 Lemmas 1.1, 2.1–2.3, Cor 4.2, Thm 4.1.
## Barrier screen
It obstructs finite ET coverings of {p : least non-residue = r} (B1-side statement), not ES. It is consistent with Thm C
(POINTWISE_SIZE) and Mordell. r₀ is astronomical, so r = 13, 17 stay open.
## Cheap numerics
None beyond MORDELL17's tables (at r = 17 the low levels already leave 67.7 % uncovered).
## Assessment
**SHARP candidate: PROVED relative to cited inputs, pending review of the general-r transfer (caveat list in DEPTH_ASPECT §3).**
If it survives, it is the first proved sterile Mordell point other than the square points.
