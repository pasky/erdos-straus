# POINTWISE_TERNARY — embedding ES into representations by quadratic forms (task O124)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`).
`f(p)` = number of ordered triples `(x,y,z) ∈ ℕ³` with `4/p = 1/x+1/y+1/z`.

## 0. Summary

(written at the end; see §§1–6)

## 1. Setting: what an "embedding" is

Fix `k ≥ 3`, a quadratic form `Q ∈ ℤ[v_1,…,v_k]` (homogeneous of degree 2, nondegenerate), integers `κ ≥ 1`, `η`.
For `m ∈ ℂ` put `E_m = {v ∈ ℂ^k : Q(v) = m}`.

**Definition 1.1 (embedding of complexity (J, D)).** A finite family of *pieces* `(S_j, Φ_j)`, `1 ≤ j ≤ J`, where
`S_j ⊆ ℤ^k` is an **arbitrary** subset and `Φ_j = (X_j, Y_j, Z_j)` is a triple of rational functions in `ℚ(v_1,…,v_k)`,
each a quotient of polynomials of degree `≤ D`. It is *valid* if

> (E) for every prime `p`, every `j` and every `v ∈ S_j` with `Q(v) = κp + η`, `Φ_j` is defined at `v` and
> `Φ_j(v) ∈ ℕ³` satisfies `4/p = 1/X_j(v) + 1/Y_j(v) + 1/Z_j(v)`.

Put `R_j(p) = {v ∈ S_j : Q(v) = κp + η}` and `R(p) = ∪_j R_j(p)`. The embedding *proves ES(p)* iff `R(p) ≠ ∅`.

This covers "p (or κp + η) is represented by Q with side conditions C ⇒ ES(p)" with an explicit (piecewise
rational) recipe: the side conditions are the sets `S_j` (congruences mod a fixed M, primitivity, sign/cone
conditions, or anything else — no restriction is imposed on `S_j`). Explicit recipes in the literature (Mordell,
Schinzel, ET's parametrisations) are polynomial, hence of this form. What is **not** covered: recipes whose
algebraic complexity is unbounded (e.g. dividing by `gcd`s of unbounded size, or a search over an unbounded
auxiliary parameter); see §5.

**Definition 1.2.** Piece `j` is *degenerate* if `X_j, Y_j, Z_j ∈ ℚ(Q)`, i.e. each is a rational function of the
single quantity `Q(v)` (so the ES solution depends on `v` only through `p`).

**Lemma 1.3 (level sets; PROVED).** Let `X ∈ ℚ(v_1,…,v_k)`, `k ≥ 3`, with `X ∉ ℚ(Q)`. Then there are only finitely
many `m ∈ ℂ` such that `X` is defined and constant on a Zariski-dense subset of `E_m`.

*Proof.* (i) For `m ≠ 0`, `Q − m` is irreducible over `ℂ` (a quadratic polynomial is reducible over `ℂ` only if its
homogenisation `Q − m w²` has rank ≤ 2; here the rank is `k + 1 ≥ 4`). Hence `E_m` is an irreducible hypersurface and
`(Q − m)` is a prime ideal of `ℂ[v]`. The same argument over `\overline{ℚ(t)}` shows that `Q − t` is absolutely
irreducible over `ℚ(t)`, so `ℚ(Q)` is algebraically closed in `ℚ(v)` (the generic fibre of `Q` is geometrically
integral).
(ii) Write `X = A/B` in lowest terms. For `m ≠ 0` with `(Q − m) ∤ B`, suppose `X ≡ x_m` on a dense subset of `E_m`.
Then `A − x_m B` vanishes on `E_m`, and so do the numerators of the 2×2 minors
`ω_{il} = ∂_i X ∂_l Q − ∂_l X ∂_i Q` of the Jacobian of `(X, Q)`: indeed `dX` restricted to the smooth locus of `E_m`
is 0, i.e. `dX ∥ dQ` there. Each numerator `N_{il} = (B∂_iA − A∂_iB)∂_lQ − (…)` is a polynomial divisible by
`Q − m`. If this happened for infinitely many `m`, each `N_{il}` would be divisible by infinitely many pairwise
coprime irreducibles, so `N_{il} ≡ 0`, i.e. `dX ∧ dQ ≡ 0`.
(iii) By the Jacobian criterion (characteristic 0), `dX ∧ dQ ≡ 0` means `X, Q` are algebraically dependent, so `X`
is algebraic over `ℚ(Q)`, hence `X ∈ ℚ(Q)` by (i). Contradiction. Only finitely many `m` divide `B` or equal 0. ∎

So a nondegenerate piece is non-constant on `E_m` for all `m` outside a finite set `𝔐_j`.
