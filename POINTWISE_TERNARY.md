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

**Cited input (M) (Mordell, *Diophantine Equations* (1969) p. 287–290; Schinzel; restated in ET p. 8, and a
consequence of ET Prop 1.6).** Call a primitive class `r mod q` *solvable by polynomials* if there are
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
`#R(p) ≤ C(Q, J, D, ε)·f(p)·p^{(k−2)/2 − 1/4 + ε}`;

(b) for every `ε₀ > 0, c > 0`: `#{p ≤ N : p ∉ U, #R(p) ≥ c p^{(k−2)/2 − ε₀}} ≪_{c,ε₀} N^{3/4 + 2ε₀}`.

*Proof.* (a): for `p ∉ U`, `p > p_0`, only nondegenerate pieces contribute (Cor 3.2); apply Prop 2.2 to each (the
finite sets `𝔐_j` exclude finitely many `p`). (b): such `p` have, by (a) with `ε = ε₀/2`, `f(p) ≫ p^{1/4 − 3ε₀/2}`.
For prime `p`, `f(p) = 3f_I(p) + 3f_II(p)` and ET Thm 1.1 gives `Σ_{p≤N} f(p) ≪ N log²N log log N`; so the number of
such `p ∈ (N/2, N]` is `≪ N^{3/4 + 3ε₀/2} log³N`; sum dyadically. ∎

**Corollary 4.2 (the representation-theorem route closes; PROVED relative to the cited representation theorems as
input (R)).** Suppose in addition that the embedding is *mild* in the sense that the input one intends to use holds:

> (R) there are a modulus `L`, a nonempty union `𝒫_R` of primitive classes mod `L`, and a set `ℰ` of primes with
> `#(ℰ ∩ [1,N]) = o(N/log N)`, such that `#R(p) ≥ c p^{(k−2)/2 − ε₀}` for all large `p ∈ 𝒫_R ∖ ℰ`.

Then `𝒫_R ⊆ U` (as sets of classes mod `lcm(L, q*)`). Hence `𝒫_R` contains no prime that is a square mod `q*`, and the
embedding proves ES only for primes that a **finite polynomial (Mordell-type) covering already handles** (`U`), plus a
set of `≪ N^{3/4+ε}` primes up to `N` on which `f(p) ≥ p^{1/4−ε}` (which cannot be identified without knowing `f(p)`).

*Proof.* If a primitive class mod `lcm(L, q*)` lay in `𝒫_R ∖ U`, it would contain `≫ N/log N` primes up to `N`
(Dirichlet), all but `o(N/log N)` of them satisfying `#R(p) ≥ c p^{(k−2)/2−ε₀}`, contradicting Thm 4.1(b). ∎

*Where (R) comes from (Assessment as to the exact form of each cited theorem).* For
`S_j ⊇ S° := {v ≡ v_0 (mod M), v ∈ Γ}` (fixed modulus `M`, open cone `Γ`, optionally primitivity):
* k ≥ 5: the circle method.
* k = 4: Kloosterman's method (Heath-Brown's δ-method; Hsia–Kitaoka–Kneser for the local–global form). For
  `m = κp + η`, `p ∤ η`, the divisibility of `m` by anisotropic primes is bounded, so no exception arises.
* k = 3: Duke 1988 / Iwaniec 1987 (weight-3/2 coefficient bounds), Duke–Schulze-Pillot 1990 (primitive
  representations, all large `m` outside finitely many spinor exceptional square classes `tℤ²`), Golubeva–Fomenko
  and Blomer for congruence/coset conditions, Siegel's ineffective `L(1,χ) ≫_ε m^{−ε}` for the size `m^{1/2−ε}`.
  The spinor exceptions give `ℰ = {p : κp + η ∈ tℤ² for one of finitely many t}`, of size `O(√N)`.
In each case `𝒫_R` is the set of primes with `κp + η` (primitively) locally represented by the coset `v_0 + Mℤ^k`.
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

**Proposition 5.2 (PROVED, given (P)).** Let `Q` be indefinite ternary, `m ≠ 0` with `E_m` line-free over `ℚ`, and
`H` of degree `≤ D` not vanishing identically on `E_m`. Then for every `T ≥ 1`:
`#{v ∈ ℤ³ : Q(v) = m, H(v) = 0, |v| ≤ T} ≤ C(D, ε)·T^{1/2+ε} + 4D²`.
Consequently, for a nondegenerate piece of a valid embedding and `p` with `m = κp + η ∉ 𝔐_j`, `E_m` line-free:
`#(R_j(p) ∩ {|v| ≤ T}) ≤ C f(p) T^{1/2+ε}`.
*Proof.* As in Lemma 2.1 (k = 3): `≤ 2D` components; non-real components carry `≤ 4D²` real points in total; a line
containing two integer points is a `ℚ`-line, so each line carries `≤ 1`; real components of degree `≥ 2` carry
`≪ T^{1/2+ε}` points by (P). The second part follows as in Prop 2.2. ∎

**Corollary 5.3 (positivity is not mild; PROVED given (P), and given the cited counting input (DRS) for the
last clause).** Let `p` be as in Prop 5.2 and `G = (v_0 + Mℤ³) ∩ Γ ∩ E_m` with `Γ` an open cone.
(i) If `G ⊆ R_j(p)` for a nondegenerate piece `j`, then `#(G ∩ {|v| ≤ T}) ≪ f(p) T^{1/2+ε}` for all `T`. Since for a
Zariski-dense orbit the count `#(G ∩ {|v| ≤ T})` grows like a positive multiple of `T` (Duke–Rudnick–Sarnak,
Eskin–McMullen; in the ternary case up to log factors), **no valid nondegenerate piece contains an untruncated mild
set**: validity of the ES recipe (positivity of the output!) forces `S_j ∩ E_m` to be thin.
(ii) If the piece is mild only on a truncation `G ∩ {|v| ≤ T(p)}` and the counting input gives
`#(G ∩ {|v| ≤ T(p)}) ≫ T(p)^{1−ε}`, then `f(p) ≫ T(p)^{1/2−2ε}`. With `T(p) ≥ p^{δ}` this is the analogue of
Thm 4.1(b) (exceptional set `≪ N^{1−δ/2+ε}`) and Cor 4.2 follows verbatim.

*Remark (the split case is a genuine gap).* When `E_m` contains `ℚ`-lines (a square class of `m`, Lemma 5.1), or for
indefinite forms in `k ≥ 4` variables (whose level sets typically contain `ℚ`-lines once `k ≥ 4`; Assessment), a fibre of `Φ_j` can be a rational line carrying `≍ T` points, and the counting argument gives
nothing. This is the **divisor-problem** regime: `n + 4a²d = ef` with `(a, d)` fixed is a split binary form, whose
integer points lie on the rational lines `e = const`. §6 shows that every quadratic substructure of ES is of this kind.

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

`Q_d = ef − 4da²` contains the hyperbolic plane `ef`. Also the defining surface itself is split: fixing `x`,
`4xyz = n(xy+yz+zx)` becomes `((4x−n)y − nx)((4x−n)z − nx) = n²x²`.
So ES carries **no** positive definite (or anisotropic) quadratic substructure in ET's coordinates; its quadratic
pieces are divisor problems.

**Proposition 6.2 (the rank-3 piece; PROVED, elementary).**
(i) `Q_d` represents every integer primitively over `ℤ` (`(e,f,a) = (n,1,0)`); so local representation
conditions, genus and spinor genus impose nothing: all the arithmetic sits in the side condition `4ad | f + 1`.
(ii) The side condition is not mild: `{(e,f,a) : 4ad | f+1}` is not a finite union of cosets of a lattice (its
density in `{a ≍ A}` is `≍ 1/(dA)`), and positivity does not truncate `Q_d`: for fixed `n`, `E_n ∩ ℕ³` is
infinite (`Σ_{a≤A} τ(n + 4da²) ≍ A log A` points with `a ≤ A`).
(iii) For fixed `(a, d)` the side condition becomes a fixed-modulus condition, but then the form drops to the split
binary `ef = n + 4a²d`, `f ≡ −1 (mod 4ad)`: ES(n) via `(a,d)` iff `n + 4a²d` has a divisor `f ≡ −1 (mod 4ad)` with
`(f+1)e/(4ad) > a`. This is ET's Type II criterion (Prop 2.7 / Prop 1.9 family `−4a²d mod f`), a divisor-in-progression
problem, not a representation problem.
*Proof.* (i) direct. (ii) The density: among `f` in a range, a proportion `1/(4ad)` satisfies the congruence; a finite
union of lattice cosets has a fixed positive density or zero. The `τ` count is ET (A.5)-type standard. (iii) ET (2.18),
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
*Proof.* `𝒫_R ⊆ U` (Cor 4.2), a finite union of polynomially solvable primitive classes. If a sterile `x` were in
the clopen closure of `𝒫_R`, it would lie in one of these classes, `r mod q`. By ET Prop 1.9 all large primes of
`r mod q` lie in finitely many ET classes; primes are dense in `r + qẐ` (Dirichlet), so `r + qẐ ⊆` this finite
(clopen) union, and `x` lies in an ET class. ∎

*Interpretation.* The campaign's formal obstruction (POINTWISE_SIZE Thms M, C) says that procedures using only
congruence data fail at square-mimicking points; a representation-theorem argument is **not** congruence-only (it
searches over `≍ p^{1/2}` representations, a search of growing length, type (E1)). Theorem 4.1 shows that this extra
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
a **divisor search of growing length** (the window regime of STATUS, `a_min ≍ log p/log log p` heuristically), not a
representation statement: for a sample of 2000 such primes, `d = 1`, `a ≤ 50`, only 14109 of the 562792 points
`(e, f, a) ∈ ℕ³` of `E_p` satisfy `4a | f + 1` (ratio 0.025, and the ratio → 0 as the `a`-range grows, Prop 6.2(ii)).

*On the known hard candidates.* x** (r = 13) and `x̂_9` (Type I) are points of `Ẑ^×`, not primes; Cor 7.1 is the
relevant statement (no mild embedding reaches a sterile point). The ET class `−4a²d mod f` (`4ad | f+1`) through which
(Q_d) acts at a *fixed* `(a, d, f)` is one of the Type II families tested in MORDELL13E Comp 3.1, so no such class of
ES level `< 2.59·10¹⁰` contains x** (CERTIFIED there; not re-run here).

## 9. Scope: what the theorem does not exclude

1. **Families with a growing parameter** (`∃ t ≤ T(p)` such that `κ_t p + η_t` is represented by `Q_t` with
   recipe `Φ_t`). For k = 3 the constants of Lemma 2.1 and Prop 2.2 are **uniform in `Q_t`** given `D` (Minkowski-reduce
   `Q_t` by a `GL₃(ℤ)` change, which preserves `D`; a reduced integral form has `Q(v) ≫ Σ v_i²`; Pila's constant
   depends only on the degree; `|𝔐_{t,j}| ≤ C(D)` because `Q_t − m` must divide a fixed nonzero polynomial of degree
   `O(D)`). So each nondegenerate `(t, j)` still sees `≤ C f(p) p^{1/4+ε}` representations, while a mild `(t, j)`
   needs `≫ p^{1/2−ε} disc(Q_t)^{−O(1)}` (Siegel; the exponent is not made explicit here). Hence for
   `disc Q_t ≤ p^{δ}` (small δ) the nondegenerate parts are again useless (PROVED modulo the uniform form of (R)), and
   what remains is the union of the degenerate parts: a congruence covering whose moduli grow with `T(p)`. That is
   the multiplier/covering mechanism of the OMEGA line, subject to its Ω-results (`W(p)` can be as large as
   `exp(c(log p)^{1/4−o(1)})`): Assessment.
2. **Unbounded algebraic complexity.** Recipes that divide by `gcd`s of unbounded size, or use floor functions, or
   have degree growing with `p`, are `J, D → ∞` and are not covered (constants in Prop 2.2 depend on `J, D`).
3. **Non-mild side conditions.** Side conditions of relative density `≤ p^{−1/4+ε}f(p)` (e.g. divisibility conditions
   with moduli depending on the variables, as in (Q_d)) are allowed by Theorem 4.1(a), but no representation theorem
   controls them; proving that such a set meets `E_m` is as hard as the original divisor problem (Prop 6.2(iii)).
4. **Split indefinite forms** (§5 Remark): fibres can be rational lines; this is where ES's own structure lives.
5. **Higher-degree forms / norm forms.** Not considered (the count of representations would be smaller, so the
   counting argument is weaker; Assessment).
