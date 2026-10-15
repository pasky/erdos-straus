# z16_windowed_konig — Cantor sets inside U_c: a windowed local count suffices; global counts provably do not (O241)

## Idea
Replace the game by a tree (König) construction. A cylinder is *alive* if no tuple ball of depth ≤ its depth contains it. If
in every visited alive cylinder the tuple balls of depth in the next window of m levels have local mass ≤ 1 − K·3^{−m}, then
U_c ≠ ∅ and dim ≥ log K/(m log 3) (STERILE_DIOPHANTINE Lemma 3.1, PROVED). For m = 1, K = 1: "no alive cylinder has all three
children covered". This needs no summation over levels — it violates the hypothesis "Σ over all levels of the global mass
< 1" of the union-bound barrier.

## Literature
Jarník (1928) Bad(κ) has positive dimension; mass distribution principle (Falconer, Fractal Geometry, Prop 4.2); Badziahin–
Velani, Multiplicatively badly approximable numbers and generalised Cantor sets, Adv. Math. 228 (2011) 2766–2796 ("Cantor-rich"
local-count framework); Lyons–Peres, Probability on Trees and Networks (2016), ch. 5 (branching processes, percolation on trees).

## Barrier screen
Prop 3.2 (PROVED): with only per-depth counts n_d of tuple balls, an adversary places them to cover the alive set iff
Σ_{d>n₀} n_d 3^{−(d−2)} > μ(alive at n₀). So any argument fed only by per-depth count bounds collapses to the tail union bound for those bounds — B3 in FF form.
(R248 repair D3) This does not say the true counts fail the tail bound: the barrier can be passed by sharper per-depth counts
or by *positional* input (where the balls sit, e.g. sibling-type; class-divisor counts in a prescribed residue class are
positional); Cantor/game cleverness on top of fixed per-depth counts adds nothing.
Percolation reading (Assessment): in the independence model U_c ≠ ∅ if p_d ≤ 2/3 − δ eventually ("if", R248 repair D13; p_d = conditional ball fraction among
children of alive parents, D9), while μ(U_c) > 0 iff Σ p_d < ∞.

## Cheap numerics
`scripts/z16_tree.py` (Case A + B complete to depth 9): per-depth distinct-ball mass .333 .222 .148 .148 .054 .038 .012
(d = 3..9; includes balls inside dead cylinders, so not the model's p_d — R248 repair D9); conditional p_d = 1/3, 0/6, 2/18,
4/48, 2/132, 10/390, 10/1140; alive fraction 0.517 at depth 9; alive parents with 3 covered children: none; with 2: two (depth 6).

## Assessment
PROVED reduction (Lemma 3.1, Prop 3.2) + EVIDENCE. Converts O(3, T²) ≠ ∅ (the conclusion of Conjecture 0.2) into a local positional statement (z16_sibling).
