# s7_normform_collapse — the binary-form rung of the menu ladder collapses (O247, (v); deep item 1)

## Idea
Wave Z's escapes from B1 used parameters that are algebraic functions of n on thin families. At a positive density of
primes the only algebraic parametrisations are norm forms p = Q(u, v) ((J)76 Prop 7.1, MENU_STERILITY §5: "only B2 or
norm-form data remain"). POINTWISE_BINARYFORM killed binary-form families on *square* classes (T1) and proved Type II
collapse on cones for definite Q (Prop 5.2); Type I with non-constant level was open (O145). Attack it by a plain
degree / top-form argument using only that Q is irreducible over ℚ.

## Result (SYNTHESIS_SPARKS7 §1)
**Theorem 1.1 (PROVED).** Every polynomial Type II family (ET coordinates A, B, C, D ∈ ℚ[u, v]) for an irreducible binary
quadratic form Q, valid at one point, has A, B, C, D ∈ ℚ[Q] — no cone, no definiteness needed.
**Theorem 1.2 (PROVED).** The same for Type I families valid on a coset inside an open cone, at any level (C, D arbitrary
polynomials). Hence the binary-form rung collapses to ET identities in n on every congruence class.

## Literature
POINTWISE_BINARYFORM Thm 3.2/3.2′, Prop 5.1, Prop 5.2, §6 search; O145 Prop 3.2; Elsholtz–Tao §2 (Σ^I, Σ^II);
MENU_LADDER Prop 7.1; MENU_STERILITY §5.

## Barrier screen
This *is* a barrier result (B1 for the norm-form menu). Hypotheses that a future escape must violate: degree-2 form
(degree ≥ 3 norm forms: the "lower-order terms lie in ℚ[N]" step fails), polynomial ET coordinates (rational families have
density-zero validity, Lemma 3.3 there), validity on a cone for Type I (for positive definite Q, families living near finitely
many directions are density zero among prime points by Hecke; for indefinite Q this fails near the null directions,
POINTWISE_BINARYFORM §4.3 — R-O247 review fix). T1 is not used.

## Cheap numerics (scripts/s7_normform_check.py)
Sympy confirms the four rearrangements used in the proofs. A random search (16 425 trials; B, C of degree ≤ 1, D of degree
≤ 2, coefficients in [−2, 2], solving Type II for A over ℚ) finds 345 polynomial families, all with constant B, C, D (positive
controls), none outside ℚ[Q]. POINTWISE_BINARYFORM §6 (0 two-variable Type I families for u² + v², linear levels) agrees.

## Assessment
PROVED (two theorems, elementary; R-O247 review: both sound, Thm 1.2 after editorial repairs). Closes the open Type I question of POINTWISE_BINARYFORM §5 on cones and removes the
cone/definiteness hypotheses of its Prop 5.2. For ES at primes: one more hatch closed; next candidate is degree-3 norm forms.
