# z5_pell_unit_T1 — the Pell unit of ℚ(√n) is T1-shaped but never enters the ES^{[2]} orbits (O229)

**ES is not solved here.**

## Idea
u² − nv² = 1 has a solution with v ≠ 0 ⟺ n is not a square: a deterministic existence mechanism with exactly the T1
shape. Can (u, v) generate an ES^{(y,e)} / ES^{[2]} point (nA² + B² + D = 2λD·AB)?

## Literature
Classical (Lagrange). GROWING_MUTE Prop 1.2(c) (n ∤ λ by reciprocity); MARKOFF_ES Thm 5.1 (no polynomial λ-families).

## Result
* (PROVED, elementary) The ES^{[2]} point at (λ, D) lives in the order ℤ[√(μ² − n)], μ = λD. This order lies in
  ℚ(√n) iff μ² − n = n·w², i.e. n | μ² , and (n squarefree, gcd(D, n) = 1) iff n | λ — excluded for every odd n > 1
  by GROWING_MUTE Prop 1.2(c). So the unit of ℚ(√n) never acts on an ES^{[2]} fibre (for squarefree n).
* (PROVED) Direct substitutions fail: A = v, B = u forces D ≡ 1 (mod u), D ≡ −1 (mod 2v), D | 2u² − 1 and
  2u² − 1 = DE with E ≡ −1 (mod 2uv) > 2u² unless v | u; B = 1 is ES's own line, where A = v ≤ 3(n+1)/2 (Thm 2.1 of
  EXPONENT_CAP) excludes all but the smallest Pell solutions. Pell identities produce *differences*
  (4v²/(u² − 1) = 2v²/(u−1) − 2v²/(u+1)): the signed world (SYNTHESIS_SPARKS4 L1/L2).
* (Assessment) The ES-relevant T1-shaped existence is the *imaginary* one — a prime q ≡ 3 (4) with (−n/q) = 1, i.e. a
  non-principal genus of discriminant −4n — which is what ES^□ uses; the real unit is positivity-blind.

## Barrier screen
SPARKS4 (a): Pell is a real-topology/sign-blind tool; it would also "prove" the signed relaxation. T1-shaped yes,
positivity no.

## Cheap numerics
None needed (statements are algebraic).

## Assessment
Negative, PROVED in the stated scope (squarefree n). Closes an obvious "deterministic T1-shaped mechanism".
