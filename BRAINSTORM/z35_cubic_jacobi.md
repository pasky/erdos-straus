# z35_cubic_jacobi — cubic/Eisenstein data: Jacobi sums, 4p = L² + 27M², Gauss periods (O265, goal (4))

## Idea
For p ≡ 1 (3) the cubic Jacobi sum J(χ, χ) ∈ ℤ[ω] (norm p) is canonical; it is equivalent to 4p = L² + 27M² (L ≡ 1 (3)), and
cubic Gauss periods are roots of x³ − 3px − pL (classical). Cubic residue symbols (q/p)_3 of small q are functions of
(L, M) mod q (Jacobi/Eisenstein; e.g. 2 is a cube ⟺ 2 | M, 3 is a cube ⟺ 9 | M). Try the same constructions as in the
quartic case.

## Literature
Ireland–Rosen Ch. 8–9 (cubic reciprocity, Jacobi sums), Lemmermeyer Ch. 7; Berndt–Evans–Williams, *Gauss and Jacobi Sums*.

## Barrier screen
Same three statements as the quartic case: (i) the cubic part of a certificate's residue-symbol content is an output (cubic
symbols of m, d, g are functions of (L, M) mod the parameters; MODP_RECIPROCITY Prop 1.2's analogue); (ii) bounded level:
inert (Prop 2.1); (iii) the representation 4p = L² + 27M² acts on windows by Prop 5.1 with D = 27: divisors of M forbidden,
divisors m of L permitted iff (3/m) = −1. Polynomial families in (L, M): (J)78/(J)79 (irreducible binary form). Gauss periods:
integers only via the cubic x³ − 3px − pL, i.e. via (L, M) again.

## Cheap numerics
`scripts/z35_principal_windows.py` covers D = 3 (p = x² + 3y², the same prime set): 0 hits on forbidden windows, 2.06 % on
permitted ones.

## Assessment
PROVED by the general Prop 5.1 / Prop 2.1 (no cubic-specific new content) + EVIDENCE. Cubic data behave exactly like quartic
data: inert at bounded level, a Jacobi selection rule in the balanced range.
