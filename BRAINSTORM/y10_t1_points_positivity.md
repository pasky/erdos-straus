# y10_t1_points_positivity — positivity propagates down to the largest real root of n (O221)

## Idea
Polynomial families are positive at +∞; the ET identities (4abd = ne + 1, ce = a + b, ef = 4a²d + 1; Type II analogues)
forbid any coordinate from vanishing where n > 0. Hence all coordinates are positive on (ρ, ∞), ρ = largest real root of n
(NEAR_SQUARE Lemma 3.2). Integrality is L-periodic, so a family valid on m ≡ g (L) evaluates to an N-point at every
integer m₀ ≡ g (L) above ρ. If n(m₀) is an odd square this contradicts ET Prop 1.6 (Thm 3.3).

## Literature
ET Prop 1.6, §10; Schinzel's substitution argument for square classes (cited in ET). Our version replaces the substitution
by one integer evaluation + positivity, and works for every polynomial n(m).

## Barrier screen
It is T1 (B5) applied at one integer point; the novelty is that the *archimedean position* of the point matters: m₀ = 3
and −3 (j = 8) have the same n but only the one above √j obstructs.

## Cheap numerics
Max real root over all coordinates of all found families: 2.818 / 3.865 / 4.895 vs √j = 2.828 / 3.873 / 4.899
(j = 8, 15, 24) — the bound is sharp in the data.

## Assessment
PROVED (short). Recovers ET's "square classes are not polynomially solvable" for linear n. A clean general tool: any
polynomial n(m) with an integer point above its largest real root at which n is an odd square has no finite polynomial
covering.
