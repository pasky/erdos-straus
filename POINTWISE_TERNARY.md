# POINTWISE_TERNARY — embedding ES into representations by quadratic forms (task O124)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`).
`f(p)` = number of ordered triples `(x,y,z) ∈ ℕ³` with `4/p = 1/x+1/y+1/z`.

## 0. Summary

**Outcome: a precise negative result.** Pointwise representation theorems for quadratic forms (Duke–Schulze-Pillot,
Kloosterman/HKK, the circle method) contribute nothing beyond finite polynomial (Mordell-type) coverings when
combined with **one fixed** ES embedding of bounded algebraic complexity.

> **Scope (R124 repair M1):** one fixed `(Q, κ, η)` and fixed complexity `(J, D)`, all independent of `p`. Not covered: families with a parameter growing with `p`. That includes every known ES parametrisation (ET Type I/II with `a, d` unbounded; §9.1, Assessment only).
> Two further routes are outside the scope (R124 repair, red team §6): thin side conditions on a level set (H2, where
> (Q_d) sits), and routes where `p` enters only through a side condition on a fixed level set (H5, e.g. Type I's
> `ef − 4a²d = 1` with `f ≡ −p (mod 4ad)`). Thm 4.1 / Cor 7.1 say nothing about either.
 Any ES content outside such a covering must come from
*thin* sets of representations, which these theorems do not control.

* **Theorem 4.1 (PROVED, given Pila's bound (P), Mordell–Schinzel (M) and ET Thm 1.1).** Let `Q` be positive definite
  in `k ≥ 3` variables, and let a recipe of complexity `(J, D)` (piecewise rational, arbitrary side-condition sets
  `S_j`) turn every representation `Q(v) = κp + η`, `v ∈ S_j`, into an ES solution of `4/p`. Call a piece
  *degenerate* if its output depends on `v` only through `Q(v)`.
  * Degenerate pieces are polynomial identities on finitely many residue classes, forming a set `U`. No class of `U`
    is a square class (Lemma 3.1, Cor 3.2).
  * For `p ∉ U`, in particular for `p` a square mod `q*`, the recipe uses at most `C f(p) p^{(k−2)/2 − 1/4 + ε}`
    representations. Mechanism: a nondegenerate rational map is non-constant on all but finitely many level sets
    (Lemma 1.3), and its fibres there carry `≪ p^{1/4+ε}` lattice points per slice (Bombieri–Pila/Pila, Lemma 2.1).
* **Cor 4.2 (PROVED relative to the input (R)).** Suppose the representation theorems give
  `≫ p^{(k−2)/2−ε₀}` admissible representations (`ε₀ < 1/4`) on a congruence set of primes `𝒫_R`. Then `𝒫_R ⊆ U`.
  Caution: thin nondegenerate pieces *can* cover positive-density sets outside `U` (explicit example after
  Cor 4.2), but no representation theorem certifies them. This holds for one fixed embedding only (scope box above).
* **Cor 7.1.** The closure of `𝒫_R` in `Ẑ^×` contains no sterile point. So it contains no square point, and it contains
  x** only through an ET class of ES level `≥ 2.59·10¹⁰` (by MORDELL13E).
* **Step 3, the "sanity count".** The map from representations to ES solutions cannot be highly non-injective on a
  mild set unless it is degenerate. Side conditions that do work must be non-mild, of relative density
  `≤ p^{−1/4+ε}f(p)`.
* **Indefinite ternary forms (§5).** The fibre bound holds in balls `|v| ≤ T` whenever `E_m` has no rational line,
  which holds for all `m` outside one square class (Lemma 5.1, Prop 5.2). Validity forces the admissible set to be
  thin, though not necessarily bounded (Cor 5.3, with a Pell example). Split level sets (rational lines) and
  `k ≥ 4` indefinite forms are a gap of the method.
* **Step 1, systematic search (Comp 6.1, CERTIFIED symbolic).** There are 57 quadratic substructures in ET's Type I/II
  charts, and all are isotropic. Of these, 56 are split binary or degenerate. The remaining one is the rank-3 form
  `Q_d = ef − 4da²` (Type II, `d` fixed). It represents every integer, so it has no local or spinor content. Its
  positive level sets are line-free, and its side condition `4ad | f+1` is not mild (Prop 6.2). ES escapes the
  counting obstruction only through such non-mild conditions.
* **Step 4 (EVIDENCE).** Every Mordell-hard prime `≤ 10⁸` gets a Type II solution through (Q_d) with `d ≤ 8`,
  `a ≤ 22` (the maximum is at p = 84525841). This is a divisor search of growing length, not a representation
  statement.
* **Not excluded (§9).** Recipes of unbounded complexity; families with a growing parameter (only an Assessment, since
  exceptional levels are not uniformly controlled); thin side conditions; split level sets.
* **Novelty (Assessment; R124 repair m6).** ET make two relevant remarks.
  * p. 5, after Thm 1.1: analytic methods such as the circle method appear insufficient because `f(p)` is
    polylogarithmic.
  * p. 6, after Prop 1.6: vanishing at odd squares "rules out many strategies (e.g. a finite set of covering
    congruence strategies, or the circle method)". The square-point parts of Cor 3.2 and Cor 7.1 restate this second
    remark.

  The additions are a version for methods valid only at primes, which ET's square argument does not directly
  constrain, and the fibre-count formalisation (Lemma 2.1, Prop 2.2, Thm 4.1). Novelty is modest at most. An internal self-review (codex, deep mode) found one FATAL overclaim in the first draft of Cor 4.2
  and five MAJOR issues; all are repaired (§§4, 5, 7, 9).

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
auxiliary parameter); see §9.

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
the finite set `C ∩ C̄` (`≤ 4D²` points). If `C = C̄` were a line, `C(ℝ)` would be an (unbounded) real line inside the bounded set
`E_m(ℝ)` — impossible; so no component is a line defined over ℝ. If `C = C̄` has degree `δ ≥ 2`, (P) with `B = B_m` gives `≪ B_m^{1/2+ε} ≪ m^{1/4+ε}` points.
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

## 3. Degenerate pieces are polynomial (Mordell-type) identities

**Cited input (M) (Mordell [ET ref. 44], *Diophantine Equations* (1969) p. 287–290, and Schinzel [ET ref. 68]; restated
in ET p. 8).** ET add that this "also follows from Prop 1.6". That deduction would also need the polynomial solution
at a large odd square `n` to be of Type I/II, i.e. `gcd(P_i(n), n) = 1` for each `P_i` with a nonzero constant term.
This is not automatic for composite `n`, so we rely on Mordell–Schinzel (R124 repair m2). Call a primitive class `r mod q` *solvable by polynomials* if there are
`P_1,P_2,P_3 ∈ ℚ[n]` with `P_i(n) ∈ ℕ` for all large `n ≡ r (q)` and `4/n = Σ 1/P_i(n)` identically. A primitive
class `r mod q` with `r ≡ s² (mod q)` is **not** solvable by polynomials.

**Lemma 3.1 (PROVED).** Let piece `j` of a valid embedding be degenerate and suppose `R_j(p) ≠ ∅` for infinitely many
primes `p`. Then there are `P_1,P_2,P_3 ∈ ℚ[n]` and `q_j ≥ 1` such that every prime `p > p_j` with `R_j(p) ≠ ∅` lies in a
primitive class mod `q_j` that is solvable by polynomials (by the `P_i`).

*Proof.* `X_j = G_1(Q)` etc. with `G_i ∈ ℚ(t)`, so on `R_j(p)` the solution is `(P̃_1(p), P̃_2(p), P̃_3(p))` with
`P̃_i(n) = G_i(κn + η) ∈ ℚ(n)`. The identity `4/n = Σ 1/P̃_i(n)` holds at infinitely many `n`, hence identically.
*Polynomiality:* write `P̃_i = P_i + S/T` with `P_i ∈ ℚ[n]`, `deg S < deg T`, and let `δ` be a common denominator of the
coefficients of all `P_i`. For large `p`, `|S(p)/T(p)| < 1/δ`, while `P̃_i(p) ∈ ℤ` and `P_i(p) ∈ δ^{−1}ℤ` force
`S(p)/T(p) ∈ δ^{−1}ℤ`; so `S(p) = 0` for infinitely many `p`, `S = 0`. *Periodicity:* if `δ c ∈ ℤ` then
`c((n+δt)^ℓ − n^ℓ) ∈ ℤ`, so the set `{n : P_i(n) ∈ ℤ ∀i}` is a union of classes mod `q_j := δ`. Each `P_i` takes
positive values at infinitely many large `p`, so has positive leading coefficient (or is a positive constant) and is
positive for all large `n`. Hence for `p > max(q_j, p'_j)` the (primitive) class of `p` mod `q_j` is solvable by
polynomials. ∎

**Corollary 3.2.** Let `U` be the union over degenerate pieces (with infinitely many covered primes) of the solvable
classes of Lemma 3.1, `q* = lcm q_j`. Then `U` is a finite union of primitive classes mod `q*`, none of which is a
square class (by (M)); every prime `p > p_0` covered by a degenerate piece lies in `U`. In particular **no prime
`p > p_0` that is a square mod `q*` is covered by a degenerate piece.**

## 4. Main theorem: definite embeddings are disguised congruence coverings

**Theorem 4.1 (PROVED, given (P), (M) and ET Thm 1.1).** Let `(S_j, Φ_j)_{j≤J}` be a valid embedding of complexity
`(J, D)` for a positive definite `Q` in `k ≥ 3` variables, and `U, q*` as in Cor 3.2. Then:

(a) for every prime `p > p_0` with `p ∉ U` (in particular every `p > p_0` that is a square mod `q*`):
`#R(p) ≤ C(Q, κ, η, J, D, ε)·f(p)·p^{(k−2)/2 − 1/4 + ε}` (`p_0` depends on `Q, κ, η` and the recipes);

(b) for every `0 < ε₀ < 1/4`, `c > 0`, `ε > 0`: `#{p ≤ N : p ∉ U, #R(p) ≥ c p^{(k−2)/2 − ε₀}} ≪ N^{3/4 + ε₀ + ε}`.

*Proof.* (a): for `p ∉ U`, `p > p_0`, only nondegenerate pieces contribute (Cor 3.2); apply Prop 2.2 to each (the
finite sets `𝔐_j` exclude finitely many `p`). (b): such `p` have, by (a) with `ε/2` in place of `ε`, `f(p) ≫ p^{1/4 − ε₀ − ε/2}`.
For prime `p`, `f(p) = 3f_I(p) + 3f_II(p)` and ET Thm 1.1 gives `Σ_{p≤N} f(p) ≪ N log²N log log N`; so the number of
such `p ∈ (N/2, N]` is `≪ N^{3/4 + ε₀ + ε/2} log³N`; sum dyadically. ∎

**Corollary 4.2 (the representation-theorem route closes; PROVED relative to the cited representation theorems as
input (R)).** Suppose in addition that the embedding is *mild* in the sense that the input one intends to use holds:

> (R) there are a modulus `L`, a nonempty union `𝒫_R` of primitive classes mod `L`, and a set `ℰ` of primes with
> `#(ℰ ∩ [1,N]) = o(N/log N)`, and `0 < ε₀ < 1/4`, such that `#R(p) ≥ c p^{(k−2)/2 − ε₀}` for all large
> `p ∈ 𝒫_R ∖ ℰ`.

Then `𝒫_R ⊆ U` (as sets of classes mod `lcm(L, q*)`). Hence `𝒫_R` contains no prime that is a square mod `q*`: **the
primes on which the representation input (R) delivers ES are among the primes that a finite polynomial (Mordell-type)
covering already handles** (R124 repair m1: an inclusion). This is for one fixed embedding; see the scope box in §0
(R124 repair M1).

*Caution (O124 self-review, FATAL in the first draft).* This does **not** say that the embedding proves ES only on `U`.
A nondegenerate piece on a *thin* set can cover a positive-density set of primes outside `U`. Example: `Q = Σ_{i≤5} v_i²`,
`κ = η = 1` (so `Q(v) = p + 1`), piece `S = {v₁ = 1, Q(v) ≡ 0 (mod 4)}` (so `p ≡ 3 (4)`), output
`((p+1)/4 + v₁ − 1, p(p+1)/2, p(p+1)/2)`. It is nondegenerate (it involves `v₁`), and it covers every prime `p ≡ 3 (4)`
via `≍ p` representations, which is far fewer than `p^{3/2−ε₀}`. What the corollary excludes is that a
representation *theorem* (which only produces mild, `≍ p^{(k−2)/2}`-sized sets) does any work outside `U`. Any ES
content outside `U` must come from an existence statement for a thin set of representations, and no representation
theorem supplies that.

*Proof.* If a primitive class mod `lcm(L, q*)` lay in `𝒫_R ∖ U`, it would contain `≫ N/log N` primes up to `N`
(Dirichlet), all but `o(N/log N)` of them satisfying `#R(p) ≥ c p^{(k−2)/2−ε₀}`, contradicting Thm 4.1(b). ∎

*Where (R) comes from (Assessment as to the exact form of each cited theorem).* For
`S_j ⊇ S° := {v ≡ v_0 (mod M), v ∈ Γ}` (fixed modulus `M`, open cone `Γ`, optionally primitivity):
* k ≥ 5: the circle method.
* k = 4: Kloosterman's method (Heath-Brown's δ-method; Hsia–Kitaoka–Kneser for the local–global form). For
  `m = κp + η` the divisibility of `m` by the (finitely many) anisotropic primes `ℓ` must be bounded, `v_ℓ(m) ≤ B`.
  This is **not** automatic (e.g. `v₂(p + 1)` is unbounded along primes). However, `v_ℓ(κp+η) ≤ B` is a congruence
  condition on `p` mod `ℓ^{B+1}`, so it can be built into `𝒫_R`.
* k = 3: Duke 1988 / Iwaniec 1987 (weight-3/2 coefficient bounds), Duke–Schulze-Pillot 1990 (primitive
  representations, all large `m` outside finitely many spinor exceptional square classes `tℤ²`), Golubeva–Fomenko
  and Blomer for congruence/coset conditions, Siegel's ineffective `L(1,χ) ≫_ε m^{−ε}` for the size `m^{1/2−ε}`.
  The spinor exceptions give `ℰ = {p : κp + η ∈ tℤ² for one of finitely many t}`, of size `O(√N)`.
In each case `𝒫_R` is the set of primes with `κp + η` (primitively) locally represented by the coset `v_0 + Mℤ^k`
(intersected with the bounded-valuation conditions for k = 4).
For `ℓ ∤ 2κηM·disc Q` this is automatic (a unimodular rank-≥3 lattice represents every `ℓ`-adic integer
primitively; at `ℓ = p ∤ η`, `κp + η` is a unit), and at the finitely many other `ℓ` it depends on `p` mod a power of
`ℓ` — a congruence condition. Corollary 4.2 only needs that (R) holds on **some** primitive class, which is exactly
what an application of these theorems would deliver.

## 5. Indefinite forms: what positivity costs

Now let `Q` be a nondegenerate **indefinite** ternary form (k = 3). Lemma 1.3 and §3 did not use definiteness.

**Lemma 5.1 (line-free level sets; PROVED).** `E_m` (`m ≠ 0`) contains a line defined over `ℚ` iff the quaternary form
`Q ⊥ ⟨−m⟩` has Witt index 2 over `ℚ`, which requires `−m·det(Q) ∈ ℚ^{×2}` (discriminant of `H ⊥ H` is a square). Hence
for `m = κp + η`, `E_m` contains a `ℚ`-line only for `p` in a set of size `O(√N)` up to `N` (one square class).
*Proof.* A `ℚ`-line in `{Q = m}` is the projective line through `(v_0 : 1)` and `(w : 0)` with `Q(w) = 0`,
`B(v_0, w) = 0`, `Q(v_0) = m`, i.e. a 2-dimensional totally isotropic subspace `⟨(v_0,1), (w,0)⟩` of `Q ⊥ ⟨−m⟩`;
conversely such a subspace not inside `{w_4 = 0}` (where `Q` alone, rank 3, has Witt index ≤ 1) gives a line. A
4-dimensional form of Witt index 2 is `H ⊥ H`, of determinant `1` mod squares; `det(Q ⊥ ⟨−m⟩) = −m det Q`. ∎
*Convention (R124 repair m4).* Here and below, `det Q` is the determinant of the Gram matrix of
`B(x,y) = ½(Q(x+y) − Q(x) − Q(y))`. The Hessian determinant printed by `scripts/tern_sweep.py` is `2^k det Q`, so
for `Q_d` the script shows `8d` while `det Q_d = d`. For k = 3 the two conventions differ by the square class of 2.

**Proposition 5.2 (PROVED, given (P)).** Let `Q` be indefinite ternary, `m ≠ 0` with `E_m` line-free over `ℚ`, and
`H` of degree `≤ D` not vanishing identically on `E_m`. Then for every `T ≥ 1`:
`#{v ∈ ℤ³ : Q(v) = m, H(v) = 0, |v| ≤ T} ≤ C(D, ε)·T^{1/2+ε} + 4D² + 2D`. The `+ 2D` term counts the real lines not
defined over ℚ, each carrying `≤ 1` integer point (R124 repair m3).
Consequently, for a nondegenerate piece of a valid embedding and `p` with `m = κp + η ∉ 𝔐_j`, `E_m` line-free:
`#(R_j(p) ∩ {|v| ≤ T}) ≤ C f(p) T^{1/2+ε}`.
*Proof.* As in Lemma 2.1 (k = 3): `≤ 2D` components; non-real components carry `≤ 4D²` real points in total; a line
containing two integer points is a `ℚ`-line, so each line carries `≤ 1`; real components of degree `≥ 2` carry
`≪ T^{1/2+ε}` points by (P). The second part follows as in Prop 2.2. ∎

**Corollary 5.3 (positivity is not mild; PROVED given (P); the counting input in (i)/(ii) is a hypothesis).** Let `p`
be as in Prop 5.2 and `G = (v_0 + Mℤ³) ∩ Γ ∩ E_m` with `Γ` an open cone.
(i) If `G ⊆ R_j(p)` for a nondegenerate piece `j`, then `#(G ∩ {|v| ≤ T}) ≪ f(p) T^{1/2+ε}` for all `T`. Hence, if
`#(G ∩ {|v| ≤ T}) ≫ T^{1−ε}` along a sequence `T → ∞`, no valid nondegenerate piece contains `G`. Such growth holds when
`G` contains a positive-mass sector of a Zariski-dense orbit (Duke–Rudnick–Sarnak, Eskin–McMullen). Whether a given
cone `Γ` provides one depends on `Γ` meeting `E_m(ℝ)` in an unbounded region; this is Assessment. So validity of the
ES recipe (positivity of the output) forces `S_j ∩ E_m` to be **thin**, though **not necessarily bounded**. Example
(O124 self-review): `Q = x² + y² − 2z²`, piece `{y = 1, Q ≡ 3 (4)}`, output `((Q+1)/4 + y − 1, Q(Q+1)/2, Q(Q+1)/2)`. It is
valid and nondegenerate, and at `p = 3` the Pell equation `x² − 2z² = 2` gives infinitely many admissible points, all
mapping to `(1, 6, 6)`.
(ii) Suppose the piece is mild only on a truncation `G ∩ {|v| ≤ T(p)}`, and the counting input gives
`#(G ∩ {|v| ≤ T(p)}) ≫ T(p)^{1−ε}`. Then `f(p) ≫ T(p)^{1/2−2ε}`. With `T(p) ≥ p^{δ}` this gives the analogue of
Thm 4.1(b), with exceptional set `≪ N^{1−δ/2+ε}`, and Cor 4.2 follows with the same caution.

*Remark (split level sets are a gap of the method; ES is not in it).* When `E_m` contains `ℚ`-lines (one square class
of `m`, Lemma 5.1), a fibre of `Φ_j` can be a rational line carrying `≍ T` points, and the counting argument gives
nothing. The same can happen for indefinite forms in `k ≥ 4` variables, whose level sets often contain `ℚ`-lines
(Assessment). **ES's own rank-3 piece (Q_d) is not in this gap.** `det Q_d = d`, and `−nd < 0` is never a square, so
`E_n` is line-free. It is in fact a two-sheeted hyperboloid with no real lines. For fixed `(a, d)` its points lie on
the hyperbola `ef = n + 4a²d`, a conic. Prop 5.2 applies to the Type II recipe on (Q_d), but it says nothing there.
For fixed `d`, the Type II map `(a,b,c,d,e,f) ↦ (abd, acdp, bcdp)` is injective (ET p. 14: injective modulo the
dilation (2.10), and that dilation moves `d`). So `#R(p) ≤ f(p)` holds trivially for this piece, and the piece is a
divisor problem, not a representation problem (R124 repair m7). It is consistent with Prop 5.2 because
the side condition `4ad | f + 1` is thin (Prop 6.2). ES escapes the counting obstruction through **non-mild side
conditions** (§9, item 3), not through rational lines.

## 6. The quadratic substructures of ES (step 1: systematic search)

**Computation 6.1 (CERTIFIED, exact symbolic; `scripts/tern_sweep.py`, output `logs/tern_sweep.out.txt`).** On ET's
total spaces `T^I = {4abd = ne+1, ce = a+b, 4acd = n+f, ef = 4a²d+1}` and
`T^II = {4abd = n+e, ce = a+b, 4acd = f+1, ef = n+4a²d}` (4-dimensional; `n` is a coordinate), for each of the 15
four-element subsets `V ⊂ {a,…,f}` we eliminate the other two coordinates (lex Gröbner basis) and keep the `V` for
which `n` is a rational function of `V` (22 of 30). For each such `V` and each choice of 0, 1 or 2 coordinates of `V`
treated as fixed parameters such that `n` is a **quadratic polynomial** in the free ones, we record the quadratic
part. Result: 57 quadratic substructures; rank 1: 2, rank 2: 54, rank 3: 1, rank 4: 0. **Every one is isotropic over
`ℚ(parameters)`**: all binary ones have discriminant a perfect square (e.g. `4ad·ce`, disc `16a²d²`; `−4ad(a − ce)`,
disc `16c²d²`), i.e. they are split products of two linear forms; the ternary/rank-2 ones in three variables are
degenerate. The only rank-3 one is

> **(Q_d)** Type II with `d` fixed: `n = ef − 4d a²`, with side conditions `4ad | f + 1` (`c = (f+1)/(4ad)`) and
> `b = ce − a ≥ 1`.

`Q_d = ef − 4da²` is isotropic (it contains the hyperbolic plane `ef`), but its level sets `E_n`, `n > 0`, contain no
rational (indeed no real) line (§5 Remark). Also the defining surface itself is split: fixing `x`,
`4xyz = n(xy+yz+zx)` becomes `((4x−n)y − nx)((4x−n)z − nx) = n²x²`.
So ES carries **no** positive definite (or anisotropic) quadratic substructure in ET's coordinates, among the
substructures in which `n` is a quadratic polynomial in the free coordinates. Its quadratic pieces are divisor
problems. The sweep drops quadrics that do not involve `n`, for example Type I's `ef − 4da² = 1`, which is the same
isotropic form `Q_d` at level 1 (R124 repair m8; this is the H5 route of §9).

**Proposition 6.2 (the rank-3 piece; PROVED, elementary).**
(i) `Q_d` represents every integer primitively over `ℤ` (`(e,f,a) = (n,1,0)`); so local representation
conditions, genus and spinor genus impose nothing: all the arithmetic sits in the side condition `4ad | f + 1`.
(ii) The side condition is not mild: `S = {(e,f,a) : 4ad | f+1}` is not a finite union of lattice cosets. Positivity
does not truncate `Q_d`: for fixed `n`, `E_n ∩ ℕ³` is infinite, with `≫ A` points having `a ≤ A` (each `a` gives at
least the point `(e, f) = (n + 4da², 1)`).
(iii) For fixed `(a, d)` the side condition becomes a fixed-modulus condition, but then the form drops to the split
binary `ef = n + 4a²d`, `f ≡ −1 (mod 4ad)`: ES(n) via `(a,d)` iff `n + 4a²d` has a divisor `f ≡ −1 (mod 4ad)` with
`(f+1)e/(4ad) > a`. This is ET's Type II criterion (Prop 2.7 / Prop 1.9 family `−4a²d mod f`), a divisor-in-progression
problem, not a representation problem.
*Proof.* (i) direct. (ii) Argue by slices (R124 repair m5). The slice `S ∩ {a = a₀}` is `{f ≡ −1 (mod 4a₀d)}`, whose
`f`-period `4a₀d` is unbounded in `a₀`. For a finite union of cosets `v_i + L_i`, every slice `{a = a₀}` is a union of
cosets of the finitely many lattices `L_i ∩ {a = 0}`, so its `f`-periods are bounded. The count `≫ A` is the explicit
points. (iii) ET (2.18),
(2.19), (2.14). ∎

*Assessment.* Linear changes of variables preserve isotropy, and the coordinates `x, y, z, a, …, f` and their
products exhaust the known parametrisations (ET §2 lists all classical ones as charts of `Σ^I, Σ^II`). We did not
search over arbitrary nonlinear reparametrisations; Theorem 4.1 makes that unnecessary for definite forms.

## 7. Consequences for square-mimicking primes and for the candidate sterile points

Call a point `x ∈ Ẑ^×` *sterile* if it lies in no ET class (no class of ET Prop 1.9's seven families); square points
(`x ≡ s²` at every modulus) are sterile by (M), and x** (MORDELL13E), `x̂_9` (TYPEI2–7), the r = 17 line (MORDELL17–17C)
are candidates.

**Corollary 7.1 (PROVED, given Thm 4.1 / Cor 4.2 / Cor 5.3 and ET Prop 1.9).** For every valid embedding which is
mild in the sense of (R) (definite `Q`, any `k ≥ 3`; or indefinite ternary with the truncated counting input of
Cor 5.3(ii)), the closure of `𝒫_R` in `Ẑ^×` contains **no sterile point**. In particular it contains no square
point, and it contains x** only if the embedding's degenerate pieces produce an ET class containing x**, which by
MORDELL13E Comp 3.1 (CERTIFIED) must have ES level `≥ 2.59·10¹⁰`; if Conj 5.2 of MORDELL13B (x** sterile) holds, never.
*Proof.* Work with primitive cylinders `C(r, q) = {x ∈ Ẑ^× : x ≡ r (q)}`, `gcd(r, q) = 1`, and let `𝒫̂_R`, `Û` be
the (clopen) unions of the cylinders of the classes making up `𝒫_R`, `U`. Cor 4.2 gives `𝒫̂_R ⊆ Û`. If a sterile `x`
lay in `𝒫̂_R`, it would lie in `C(r, q)` for one of the polynomially solvable classes `r mod q` of `U`. By ET Prop 1.9,
all large primes `≡ r (q)` lie in a finite union of ET classes, each a union of primitive classes mod some modulus;
let `Q'` be the lcm of these moduli and `q`. By Dirichlet, every primitive class mod `Q'` inside `r mod q` contains
large primes, so it lies in one of the ET classes. Hence `C(r, q)` is covered by the cylinders of these ET classes,
and `x` lies in an ET class, a contradiction. ∎

*Scope of Cor 7.1 (R124 repair, red team §6).* Cor 7.1 is about **mild** inputs (R) to one fixed embedding. It says
nothing about two routes, and that is where the ES content lives:
* thin side conditions on a level set (H2): ES's own (Q_d) with `4ad | f+1`;
* routes where `p` enters only through a side condition on a fixed level set (H5): Type I's `ef − 4a²d = 1` with
  `f ≡ −p (mod 4ad)`, the (D)32 / O123 set-up.

*Interpretation.* The campaign's formal obstruction (POINTWISE_SIZE Thms M, C) says that procedures using only
congruence data fail at square-mimicking points; a representation-theorem argument is **not** congruence-only (it
searches over `≍ p^{1/2}` representations, a search of growing length, type (E1)). For one fixed embedding (R124 repair M1), Theorem 4.1 shows that this extra
length is wasted: on a mild representation set, a bounded-complexity ES recipe is constant on level sets except on a
`p^{−1/4}f(p)`-thin subset, so it is a congruence covering in disguise and inherits the formal obstruction. To escape,
an argument must use representation sets of relative density `≤ p^{−1/4+ε}f(p)` (non-mild side conditions, which no
representation theorem controls), or a recipe of unbounded algebraic complexity (§9).

## 8. Numerics for the rank-3 piece (Q_d) (step 4; EVIDENCE)

`scripts/tern_qd.py N DMAX AMAX` (outputs `logs/tern_qd_1e7.out.txt`, `logs/tern_qd_1e8.out.txt`; ≈10 s for N = 10⁸).
For the Mordell-hard primes `p ≤ N` (`p mod 840 ∈ {1,121,169,289,361,529}`) it computes
`a_min(p)` = least `a` such that some `d ≤ DMAX` gives a Type II solution through (Q_d), i.e. a divisor
`f | p + 4a²d`, `f ≡ −1 (mod 4ad)`, with `b = ce − a ≥ 1`.

| N | primes | a_min = 1 | 2 | 3 | 4 | ≥ 5 | max a_min (at p) |
|---|---|---|---|---|---|---|---|
| 10⁷ | 20513 | 19634 | 682 | 160 | 21 | 16 | 13 (733321) |
| 10⁸ | 179468 | 174503 | 4076 | 731 | 99 | 59 | 22 (84525841) |

(DMAX = 8, AMAX = 200; at N = 10⁶ with DMAX = 4, AMAX = 100 the two small primes 3361, 7681 are not covered — they
need `d > 4`.) So every Mordell-hard prime below 10⁸ is reached by (Q_d) with `d ≤ 8`, `a ≤ 22` (EVIDENCE). This is
a **divisor search of growing length** (cf. the window regime (E1) of STATUS), not a
representation statement: for a sample of 2000 such primes, `d = 1`, `a ≤ 50`, only 14109 of the 562792 points
`(e, f, a) ∈ ℕ³` of `E_p` satisfy `4a | f + 1` (ratio 0.025, and the ratio → 0 as the `a`-range grows, Prop 6.2(ii)).

*On the known hard candidates.* x** (r = 13) and `x̂_9` (Type I) are points of `Ẑ^×`, not primes; Cor 7.1 is the
relevant statement (no mild embedding reaches a sterile point). The ET class `−4a²d mod f` (`4ad | f+1`) through which
(Q_d) acts at a *fixed* `(a, d, f)` is one of the Type II families tested in MORDELL13E Comp 3.1, so no such class of
ES level `< 2.59·10¹⁰` contains x** (CERTIFIED there; not re-run here).

*What the numerics do not show (R124 repair, red team Prop 6.2).* The table bounds only the **small** parameters
`a, d`. A (Q_d) point is a Type II multiplier witness with modulus `f`: `p ≡ −4a²d (mod f)` and `(f+1)/4 = acd`, so
`f ≥ W(p)`. Here `f` is the large cofactor of `p + 4a²d`, and by the OMEGA results `W(p) ≥ exp(c(log p)^{1/4−o(1)})`
infinitely often on Mordell-hard primes. So small `a_min` is **not** evidence of small witness moduli, and the table
says nothing about congruence coverings.

## 9. Scope: what the theorem does not exclude

1. **Families with a growing parameter** (`∃ t ≤ T(p)` such that `κ_t p + η_t` is represented by `Q_t` with
   recipe `Φ_t`). Assessment only, not proved. For fixed `t` everything above applies. For k = 3, the Lemma 2.1 bound
   is uniform in `Q_t` given `D`: Minkowski-reduce, and Pila's constant depends only on the degree. But two things
   are not controlled. (i) The exceptional levels `𝔐_{t,j}` are finite for each `t` (`|𝔐_{t,j}| ≤ C(D)`), yet their
   union over `t` is not: the recipe chosen for `p` can be one whose exceptional level is `κ_t p + η_t`, e.g. after a
   perturbation by `(Q_t − m_t)v₁` (O124 self-review). (ii) The bounds are in `(κ_t p + η_t)`, not `p`, and the lower bound
   (R) is uniform in `disc Q_t` only up to `disc^{−O(1)}`. Heuristically, the nondegenerate parts are again useless,
   and what remains is a congruence covering whose moduli grow with `T(p)`. That is the multiplier mechanism of the
   OMEGA line, subject to its Ω-results.
2. **Unbounded algebraic complexity.** Recipes that divide by `gcd`s of unbounded size, or use floor functions, or
   have degree growing with `p`, are `J, D → ∞` and are not covered (constants in Prop 2.2 depend on `J, D`).
3. **Non-mild side conditions.** Side conditions of relative density `≤ p^{−1/4+ε}f(p)` (e.g. divisibility conditions
   with moduli depending on the variables, as in (Q_d)) are allowed by Theorem 4.1(a), but no representation theorem
   controls them; proving that such a set meets `E_m` is as hard as the original divisor problem (Prop 6.2(iii)).
4. **Split level sets** (`E_m` containing `ℚ`-lines; indefinite `k ≥ 4`; §5 Remark): fibres can be rational lines.
   ES's own quadratic piece is *not* of this kind; it escapes via item 3.
5. **Fixed level set, `p` in the side condition (H5; R124 repair, red team §6).** Example: Type I `ef − 4a²d = 1`
   (level 1 for every `p`) with side condition `f ≡ −p (mod 4ad)` (`4acd = p + f`). Def 1.1 requires
   `Q(v) = κp + η`, so Thm 4.1 is silent here. This is the (D)32 Heegner/Kuznetsov set-up (O123's route).
6. **Higher-degree forms / norm forms.** Not considered (the count of representations would be smaller, so the
   counting argument is weaker; Assessment).
