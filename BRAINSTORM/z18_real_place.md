# z18_real_place — archimedean constraint on root families (O245)

## Idea
Theorem A uses the real place only through "u − θ > 0". Polynomial families must also be positive; that is a constraint
on the *shape*, not on the point, and it is invisible to descent.
## Result (PROVED; MENU_LADDER Lemma 2.3)
Normal form (a = λ constant) n = σTT′ − T − T′ (Lemma 2.2). At a real root t of T: n(t) = −T′(t); at a real root t′ of T′:
n(t′) = −T(t′). For even D (n > 0 on ℝ) T and T′ have NO real roots; for odd D all their real roots lie left of the real
root of n. Corollaries: T, T′ both linear is impossible; the "a constant, m linear" shape never passes positivity (0 hits in
grids of 5041–33489 rational (p, q), every D, (c₀, k) tested; for D = 4 a two-line proof).
## Literature
NEAR_SQUARE Thm 2.2 (the same mechanism: "above the squares" positivity kills escaping quadratic families).
## Barrier screen
Archimedean analogue of B1's degree constraints; no conflict with T1.
## Cheap numerics
`scripts/z18_quad.py` (with the POS counter in the debug copy) — positivity never satisfied.
## Assessment
PROVED (lemma) + EVIDENCE (grids). With z18_descent_dies_at_D2: what remains of sterility at D ≥ 2 is archimedean +
magnitude (O239 Cor 2.8) + finite algebraic supply (Capelli).
