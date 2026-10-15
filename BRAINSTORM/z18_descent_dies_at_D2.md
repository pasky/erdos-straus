# z18_descent_dies_at_D2 — the genus ladder is flat: descent-sterility of unit-square points lives only at D = 1 (O245)

## Idea
Spark 3 of O240 predicted that 2-cover descent (Theorem A) stops obstructing root menus X = 2^{s/D} once the curve
w² = c₀X^D + k has genus ≥ 2 (Bruin–Stoll: fake 2-Selmer sets often empty). Test it exactly at the unit-square point μ = 0.
## Result (MENU_LADDER §1)
Prop 1.1 (PROVED): μ = 0 is in Ster(c₀Y^D + k) iff θ(θ − 1) is a square in A ⊗ ℚ₂, A = ℚ[Y]/(c₀Y^D + k) (Chebotarev pins
γ = 1 − θ; Y* = 1 at odd places, 0 at 2). Geometric reading: the glued adelic point (P₁ at odd places, P₀ at 2) of
w² = φ(Y) survives 2-descent iff the x − θ images of the rational points P₁ = (1, 2^J), P₀ = (0, √k) (a ℚ₂-point) agree 2-adically.
Computation 1.2 (CERTIFIED, PARI `nfislocalpower`, `scripts/z18_descent2.py`): for (c₀, k) ∈ {(3,1), (15,1), (63,1), (7,9),
(31,33), (7,57)} and every 2 ≤ D ≤ 10 the class is a 2-adic non-square. D = 1 recovers Schinzel/Cor 1.5 (square).
## Literature
N. Bruin, M. Stoll, Two-cover descent on hyperelliptic curves, Math. Comp. 78 (2009) 2347–2370; M. Stoll, Finite descent
obstructions and rational points on curves, Algebra & Number Theory 1 (2007) 349–391.
## Barrier screen
Family statement (B5/B6 not applicable). It REMOVES a candidate barrier rather than adding one: descent is not why
15·2^s + 1 resists (O239 Prop 2.7/Cor 2.8 is a window-shape + magnitude obstruction at D = 2, 4 where descent is silent).
## Cheap numerics
`z18_descent2.py c₀ k 10` (≈ 1 min per family).
## Assessment
PROVED (Prop 1.1) + CERTIFIED for the six families and 2 ≤ D ≤ 10 only (all D ≥ 2: CONJECTURE; R-O245 scope repair).
The brief's "genus ≥ 2" threshold is irrelevant in the tested range: already g = 0 (D = 2) kills the descent obstruction.
So any sterility of μ = 0 for D ≥ 2 menus must be shape/archimedean/magnitude, not 2-descent. SHARP (negative-steering).
