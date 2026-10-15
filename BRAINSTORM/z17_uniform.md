# z17_uniform — uniform multiplicity on the r-generic line: sterile points for every r ≥ 17? (O242)

## Idea
At every prime 17 ≤ r ≤ 61 (depth 4), r = 19 (depth 6), r = 17 (depth 7) an alive parent never holds more than 3 boxes of the
next level from depth 4 on (≤ 5 at depth 3, ≤ 14 at depth 2). Conjecture (SIBLING 4.2): ≤ 3 for all r ≥ 17, depth ≥ 4. With
SD Lemma 3.1 this gives sterile points with dim ≥ log(r−3)/log r for every r ≥ 17, closing [17, 2^{21.44}) (STERILE_LOWER
covers r ≥ 2^{21.44} by measure); r ≤ 13 have every non-residue cell covered at level 1. A sharp threshold at 17 (R249 repair D5: given level-1 survival, CERTIFIED only for r < 2·10⁴).

## Literature
STERILE_LOWER Comp. 4.1 (level-1 survivors exactly for r ≥ 17, r < 20000), Thm 6.3; M17D Lemma 2.1 (lattice form).

## Barrier screen
B2: bounded number of N-points of Σ^II_{r^{2L−1}} with a/b in a fixed class mod r^{L−1}; average r^{0.6−0.2L} per class (ET
exponent), pointwise unknown. Lemma 1.2 gives ≤ 6 per key (c, d) only. T1/B5 not engaged (generic line).

## Cheap numerics
`scripts/z17_rrun.sh`, `z17_rtree.py`; `data/z17/landscape_d4.txt`, `data/z17/rtree19_d6.txt`.

## Assessment
CONJECTURE with clean EVIDENCE; the cleanest single statement that would settle r-generic sterility for all r ≥ 17. Proving
even "≤ r − 1 per class" uniformly would need a new idea for upper bounds of Type II points in thin classes.
