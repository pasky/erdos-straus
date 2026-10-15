# z16_zz_sibling — the r = 17 sterile-point question as 17-ary percolation (O241)

## Idea
Transplant the windowed König lemma (z16_windowed_konig) to the 17-generic line: C₅ contains a sterile point if no alive
cylinder ever has all 17 children inside P/Q/U boxes of the next level. The measure route (M17–M17D) needs the cell-wide tail
mass < 0.677 and fails by constants; the tree route needs only "17 boxes never fill a parent" (percolation threshold 16/17).

## Literature
POINTWISE_MORDELL17/17B/17C/17D (box tables, lattice form of membership, pointwise certification); STERILE_EXPLICIT (r₀ = 2³²);
Lyons–Peres ch. 5.

## Barrier screen
Prop 3.2 of STERILE_DIOPHANTINE: with per-level box-count bounds only, the tree route collapses to the cell-wide union bound
for those bounds — so improving the explicit-r₀ certificates needs either sharper per-level counts (the r = 17 measure route
fails by constants) or positional input (R248 repair D3). Gap principle: two boxes in one parent
give |a_ib_j − a_jb_i| ≥ 17^{L−1}, compatible with P-data sizes (ab ≲ 17^{2L−1}/4). B6 not engaged (pointwise in u, fixed r).
T1 not engaged (generic line, not odd squares).

## Cheap numerics
`scripts/z16_ztree.py` (complete to depth 7, `data/z16/ztree17.txt`): alive fraction of C₅ 0.765, 0.685, 0.678, 0.6772,
0.6771, 0.6771 (depths 2–7); maximum boxed children per alive parent 4, 4, 2, 2, 2, 1 out of 17.

## Assessment
EVIDENCE + Assessment. The cleanest statement of what would give an explicit sterile 17-generic point: a 17-sibling bound.
