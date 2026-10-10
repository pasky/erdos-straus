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

## 2. Fibres of a nondegenerate piece on a definite quadric are thin

From here to §4, `Q` is **positive definite**. Integer points of `E_m` then satisfy `|v| ≤ B_m := (m/λ_min(Q))^{1/2}`.

**Cited input (P) (Pila, *Density of integral and rational points on varieties*, Astérisque 228 (1995) 183–187,
Thm A; for plane curves Bombieri–Pila, Duke Math. J. 59 (1989)).** If `C ⊂ ℂ^N` is an irreducible curve of degree
`δ ≥ 2`, defined over `ℝ`, then `#(C ∩ ℤ^N ∩ [−B,B]^N) ≤ c(N, δ, ε) B^{1/δ + ε}`.

**Lemma 2.1 (PROVED, given (P)).** Let `k ≥ 3`, `m ≥ 1`, and `H ∈ ℂ[v]` of degree `≤ D` not vanishing identically on
`E_m`. Then `#{v ∈ ℤ^k : Q(v) = m, H(v) = 0} ≤ C(Q, D, ε)·m^{(k−2)/2 − 1/4 + ε}`.

*Proof.* *Case k = 3.* `E_m` is an irreducible surface (Lemma 1.3(i)), so `W = E_m ∩ {H = 0}` is a curve of degree
`≤ 2D` (Bézout) with at most `2D` irreducible components `C`. If `C ≠ C̄` (complex conjugate), its real points lie in
the finite set `C ∩ C̄` (`≤ 4D²` points). If `C = C̄` is a line, it is a real line, and a real line meets the bounded
real ellipsoid `E_m(ℝ)` in `≤ 2` points; so `C` is not contained in `E_m`, absurd — hence lines contribute `≤ 2`
points anyway. If `C = C̄` has degree `δ ≥ 2`, (P) with `B = B_m` gives `≪ B_m^{1/2+ε} ≪ m^{1/4+ε}` points.
*Case k ≥ 4 (slicing).* Write `v = (v', t)`, `v' ∈ ℂ³`, `t ∈ ℂ^{k−3}`, and complete the square:
`Q(v', t) = Q_3(v' + Mt) + Q*(t)` with `Q_3` (restriction to the first 3 coordinates) and `Q*` (Schur complement)
positive definite, `M` a rational matrix. For integer `t` the slice `E_m^t = {v' : Q_3(v'+Mt) = m − Q*(t)}` is empty
(over ℝ) if `Q*(t) > m`, a single point if `Q*(t) = m`, and otherwise a real ellipsoid of radius `≪ √m`, irreducible.
There are `≪ m^{(k−3)/2}` integer `t` with `Q*(t) ≤ m`.
Divide `H` by `Q − m` as polynomials in `v_1` (leading coefficient `Q_{11} > 0` is a constant):
`H = (Q − m)G + R_1 v_1 + R_0` with `R_i ∈ ℂ[v_2, v_3, t]`. For a slice with `Q*(t) < m`, `H(·,t)` vanishes on `E_m^t`
iff `(Q(·,t) − m) | H(·,t)` iff `R_0(·,t) ≡ R_1(·,t) ≡ 0` (uniqueness of division by a polynomial monic in `v_1`). The
set `T_bad` of such `t` is the common zero set of the `(v_2,v_3)`-coefficients of `R_0, R_1`, polynomials in `t` of degree
`≤ D_1(D)`. `T_bad ≠ ℂ^{k−3}`, else `R_0 = R_1 = 0` and `(Q − m) | H`, contrary to hypothesis. So `T_bad` lies in a
hypersurface `g = 0`, `g ≢ 0` of degree `≤ D_1`, which has `≤ D_1 (2B_m+1)^{k−4}` integer points in the box.
* Good `t` (`t ∉ T_bad`): the k = 3 argument in the slice (curve of degree `≤ 2D` on a bounded real ellipsoid in a box
  of side `≪ √m`) gives `≪ m^{1/4+ε}` points; total `≪ m^{(k−3)/2 + 1/4 + ε}`.
* Bad `t`: an inhomogeneous ternary positive definite equation `Q_3(v'+Mt) = m − Q*(t)` has `≪ m^{1/2+ε}` integer
  solutions (fix `v_1`: `≪ √m` choices; the remaining positive definite binary quadratic equation becomes, after
  completing squares, `F(u, w) = N'` with `|N'| ≪ m`, which has `≪ m^ε` solutions by the divisor bound in imaginary
  quadratic orders). Total `≪ m^{(k−4)/2}·m^{1/2+ε} = m^{(k−3)/2+ε}`.
Both are `≪ m^{(k−2)/2 − 1/4 + ε}`. ∎

**Proposition 2.2 (nondegenerate pieces see few representations; PROVED, given (P)).** Let piece `j` of a valid
embedding be nondegenerate. Then there is a finite set `𝔐_j` such that for every prime `p` with
`m = κp + η ∉ 𝔐_j`:
`#R_j(p) ≤ C(Q, D, ε)·f(p)·m^{(k−2)/2 − 1/4 + ε}`.

*Proof.* Some coordinate, say `X_j = A/B`, is not in `ℚ(Q)`. Let `𝔐_j` = the finite set of Lemma 1.3 for `X_j`,
together with `0` and the finitely many `m` with `(Q − m) | B`. For `p` as stated, group `v ∈ R_j(p)` by the value
`x = X_j(v)`; there are at most `f(p)` values (each is the first coordinate of an ES solution of `4/p`, and distinct
values come from distinct solutions). Each group lies in `{Q = m} ∩ {H_x = 0}`, `H_x = A − xB`, of degree `≤ D`. If
`H_x` vanished on `E_m`, then `X_j ≡ x` on the dense open set `E_m ∖ {B = 0}`, contradicting `m ∉ 𝔐_j`. Apply
Lemma 2.1. ∎
