# y3_gross_koblitz_box — Gross–Koblitz at semi-primitive level: the Morita Γ reads the box coordinate j (O211 (a))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Gross–Koblitz expresses Gauss sums over F_{h^f} through Morita's h-adic Γ_h at fractions a/(h^f − 1). In the
semi-primitive case the Gauss sum is pure, so the Γ-product must collapse; maybe the collapse is a Wilson/Gauss-
factorial congruence that carries p-information when the fraction is p-dependent.

## Literature
Gross–Koblitz, Ann. Math. 109 (1979) 569–581; A. M. Robert, *A Course in p-adic Analysis*, §VII.2 (reflection
formula Γ_h(x)Γ_h(1 − x) = −(−1)^{ℓ(x)}, ℓ(x) ∈ {1..h} the residue of x mod h); Berndt–Evans–Williams ch. 11;
Cosgrave–Dilcher, "Gauss factorials" (Integers 2011 / Acta Arith.), where the h ≡ ±1 (mod m) cases of
((h ∓ 1)/m)!-type products are evaluated via Jacobi sums.

## Computation (PROVED, classical)
q = h², m | h + 1, j = (h + 1)/m, a = i(q − 1)/m = i·j(h − 1) = (ij − 1)h + (h − ij): base-h digits (h − ij, ij − 1),
digit sum h − 1. Gross–Koblitz: g(ω^{−a}) = −π^{h−1} Γ_h(i/m) Γ_h(⟨h·i/m⟩), and ⟨h·i/m⟩ = 1 − i/m (since
h·i/m = ij − i/m). With π^{h−1} = −h and the reflection formula, g = (−1)^{ℓ(i/m)+1}·h·(−1), where ℓ(i/m) ≡ i/m ≡ ij
(mod h) because mj = h + 1 ≡ 1. For i = 1: **the sign is (−1)^j and the Morita argument 1/m has h-adic residue
exactly j** — the box coordinate (−p ≡ c/j). Consistent with Stickelberger's pure sign (y3_semiprimitive_collapse (1)).

## Construction attempts
(1) Make the fraction p-dependent: Gauss sums of characters χ with χ ∘ (F_h^* ↪ F_{h²}^*) ≠ 1 have order not dividing
h + 1 — no longer semi-primitive, Γ-products don't collapse, and the resulting congruences (Jacobi sums ≡ binomials,
Cosgrave–Dilcher) live in the (h − 1)-world (they evaluate representations h = a² + Db² for split h). The semi-
primitive (inert) case is exactly where these binomial congruences degenerate (Jacobi sums ≡ 0 mod h).
(2) Mixed characters λ = (χ ∘ N)·ψ (χ on F_h^*, ψ of order | h + 1): g(λ) = ½ g_{F_h}(χ²) Σ_{ε∈{0,1}} χ(Nγ)^ε Σ_{u ∈ T} ψ(uγ^ε) χ̄²(Tr(uγ^ε)) for χ² ≠ 1, γ any element with Nγ a
non-square (F_h^*·T has index 2 in F_{h²}^*; checked numerically, scripts/y3_gauss.py mixed_check, 6 cases, error
< 10⁻¹¹): a torus character sum of "Salié/Kloosterman on the conic" type — equidistributed
(Katz), no closed form for general χ: the only place p could enter (via χ) is a square-root-cancelling sum: B3.

## Barrier screen
B2/B3 as in y3_semiprimitive_collapse; Thm 2.1 of BRIDGE_WORLDS (case (b): Γ-values at i/m reduce to residues of
rationals); T1 not reached.

## Assessment
COLLAPSES (PROVED): Gross–Koblitz at semi-primitive level computes the residue of 1/m, i.e. j — the box. The mixed
torus sum in (2) is the one genuinely two-world object found, but it is a Weil-bounded character sum (B3).
