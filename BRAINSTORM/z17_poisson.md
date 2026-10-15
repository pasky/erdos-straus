# z17_poisson — how much do the sibling data say? (O242)

## Idea
Calibrate the "never 3 covered children" data of SD §3 against independent placement of the observed number of balls.

## Literature
Galton–Watson / percolation on trees (Lyons–Peres ch. 5); SD §3 percolation reading.

## Barrier screen
Not a proof route; a calibration. B6-like caveat: the model is an average statement.

## Cheap numerics
`scripts/z17_poisson.py`: depths 3–9, expected alive full parents 0.145 per slice (P(none) 0.86), expected alive parents with
≥ 2 ball children 2.90 (observed 2). Beyond depth 9: ≤ 10⁻³ (p_d ≲ 3^{−d/2}). Sibling pairs among all balls are Poisson
(`data/z17/ffpairs_d9.txt`), also at r = 17 (`data/z17/zpairs17_d7.txt`); ball child digits are uniform (61/60/51).

## Assessment
EVIDENCE: the data to depth 9 are weak evidence for the sibling conjecture itself; the conjecture is heuristically very
likely because ball counts grow only like 3^{d/2} (or slower) against 3^{d} cylinders. No structure beyond counts is visible.
