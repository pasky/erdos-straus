# Involution / windmill route to Erdős–Straus: obstruction theorems (O158)

**Status: ES is not solved here.** This file is the depth follow-up of `BRAINSTORM/invol_windmill_signature.md`
(O152a), `invol_topological.md`, `invol_sign_identities.md` and `WINDMILL.md`. Labels as in DISCOVERIES.md.
Scripts: `scripts/inv_*`.

Notation. ES(n): `4/n = 1/x+1/y+1/z` has a positive solution. For a finite set `S` and an involution ι,
`|S| ≡ |Fix ι| (mod 2)`. A *windmill argument* for ES (WINDMILL Lemma 1) consists of finite sets `X(n)`,
involutions `σ_n, τ_n` of `X(n)` and a map `Φ_n : Fix τ_n → {ES certificates of n}`, with `|Fix σ_n|` odd;
then `|Fix τ_n|` is odd, so ES(n). The *O152 odd set* is

  `X(n) = {(t,u,v) ∈ ℤ³_{≥1} : tuv − u − v = n}` ⟺ `(tu−1)(tv−1) = tn+1`,

with `A = tu−1`, `B = tv−1`. Its *ES part* is `E(n) = {4 | A}`; by CONDITIONAL_ES Lemma 1.1 (with
`(g,f,c) = (t,u,v)`) every element of `E(n)` gives an explicit solution of 4/n (Type I, slice a = 1).
`ρ` denotes the swap `u ↔ v` (i.e. `A ↔ B`).

## 1. T1 for involution families (squares)

**Lemma 1.1 (PROVED, elementary).** Let `F` be a set of odd integers and suppose that for every `n ∈ F`
we are given `(X(n), τ_n, Φ_n)` as above with `Φ_n` taking values in a set `C(n)` of certificates that is
empty whenever n is an odd square (e.g. ET Type I/II solutions, ET Prop 1.6; or `E(n)`, Lemma 2.2 below).
Then `|X(m²)|` is even for every `m² ∈ F`. ∎ (`Fix τ_{m²} = ∅`.)

So a windmill *family* that is defined on a congruence class `n ≡ h (mod M)` with h a square class must
use sets with `|X(m²)|` even for all `m² ≡ h`; by Dirichlet such m² include `q²` for infinitely many primes
`q ≡ a (mod M)` (`a² ≡ h`).

## 2. The O152 set X(n) fails T1

**Lemma 2.1 (PROVED; O152 E4 extended to all n).** For every n ≥ 1, `|X(n)| ≡ #{(t,u) ∈ ℤ²_{≥1}: u(tu−2) = n} (mod 2)`.
*Proof.* ρ is an involution of X(n) with fixed points `u = v`, i.e. `tu² − 2u = n`. ∎

**Lemma 2.2 (PROVED).** If m is odd then `E(m²) = ∅`: there is no `(t,u,v) ∈ ℤ³_{≥1}` with
`tuv − u − v = m²` and `4 | tu − 1`.

*Proof.* Put `A = tu−1 = 4δ`. Then `A | tm²+1` and `t | A+1 = 4δ+1`, so t is odd and `gcd(t,δ)=1`.
From `4 | tm²+1` and `m² ≡ 1 (8)`: `t ≡ 3 (4)`; if δ is even then `8 | tm²+1`, so `t ≡ 7 (8)`.
Write `δ = 2^s δ₀`, δ₀ odd. Every prime `ℓ | δ₀` divides `tm²+1`, so `ℓ ∤ t` and `(−t/ℓ) = 1`; hence
the Jacobi symbol `(−t/δ₀) = 1`. On the other side, `4δ ≡ −1 (mod t)` gives `(δ/t) = (−1/t) = −1`, and
`(2/t) = 1` if s ≥ 1, so `(δ₀/t) = −1` (this already contradicts δ₀ = 1). By reciprocity, as
`(t−1)/2` is odd, `(t/δ₀) = (δ₀/t)(−1/δ₀) = −(−1/δ₀)`, hence `(−t/δ₀) = (−1/δ₀)(t/δ₀) = −1`.
Contradiction. ∎

(This is the a = 1 case of ET Prop 1.6, but proved for the parametric set, without ET's coprimality
convention.)

**Proposition 2.3 (PROVED).** For every odd prime q, `|X(q²)|` is odd and `E(q²) = ∅`. Consequently:
(i) for every n = q², every involution of X(q²) has a fixed point outside the ES part;
(ii) no family of involutions `τ_n` of `X(n)` with `Fix τ_n ⊆ E(n)`, of *any* description complexity, can be
defined on all n of a square class `h (mod M)` (it fails at `n = q²` for every prime `q` with `q² ≡ h`);
(iii) more generally, for odd n, `|X(n)| ≡ #{u | n : n/u ≡ −2 (mod u)}`, where u runs over unitary
divisors of n (for odd n, `u | n/u + 2` forces `gcd(u, n/u) = 1`); `u = 1` always contributes.

*Proof.* Lemma 2.1: `u | q²` and `u | q²/u + 2`; u = q fails (`q ∤ q+2`), u = q² fails (`q² ∤ 3`), u = 1
works (`t = q²+2`). So `|X(q²)| ≡ 1`. `E(q²) = ∅` by Lemma 2.2. (i), (ii) follow; (iii) is Lemma 2.1. ∎

So the O152 set has the right parity at primes for the *wrong* reason: its odd point `(n+2,1,1)` exists for
every n (a "periodic" fixed point), and nothing cancels it at squares. A windmill on X can therefore only
work if it uses the primality of p in its very definition, which rules out every uniformly defined
construction on a congruence class (in particular every piecewise-affine one whose pieces and maps do not
depend on n). §4 treats constructions defined on primes only.

EVIDENCE (`scripts/inv_x_squares.py 1500 90000`, 4 min): Lemma 2.1 checked for all odd n ≤ 1500; `E(m²) = ∅`
for all odd m ≤ 300; `|X(m²)|` odd for 137 of the 149 odd m in [3,300], and for every odd prime m there.

## 3. Divisor-type fixed-point counts: what T1 forces

In a Zagier-type windmill the σ-fixed count is evaluated through binary forms of square discriminant on
the fixed loci (O152a §1.1), i.e. it is *divisor-type*. Fix a modulus M and a square class
`h ≡ a² (mod M)`, `gcd(a,M)=1`. Consider

  `D(n) = Σ_{uv=n, u<v} φ(u mod M, v mod M) + [n = u²]·ψ(u mod M) + c(n mod M)   (mod 2)`,        (D)

with arbitrary `φ, ψ, c` (values in 𝔽₂). This covers divisor counts restricted by congruences mod M and by
finitely many homogeneous cones `λu < v` (see the proof), square loci (Zagier's boundary correction) and
isolated "periodic" fixed points (the `(1,1,(n−1)/4)` of Zagier, the `(n+2,1,1)` of X(n)).

**Proposition 3.1 (PROVED).** Suppose `D(m²) ≡ 0` for every odd m with `m² ≡ h (mod M)` (Lemma 1.1 forces
this when D is the σ-fixed count of a windmill family on the class h whose τ-fixed points are certificates
that do not exist at odd squares). Then `φ(1,h) = 0`; hence `D(p) = c(h)` for every prime `p ≡ h`, and
`ψ(a') = c(h)` for every `a'` with `a'² ≡ h`. In particular, if `D(p)` is odd then `c(h) = 1` and `ψ(a') = 1`.

So *the odd fixed point at primes can never come from the divisor part `1·p`* (as it does in Zagier's proof,
where the fixed point `(1,1,(p−1)/4)` is the factorisation `p = 1·(1+4z)`); it must be a periodic point
present for every n of the class, and then the fixed locus must contain a square-detecting piece that cancels
it at every m². (For X(n) the periodic point is `(n+2,1,1)` and the square piece is missing: Prop 2.3.)

*Proof.* `D(p) = φ(1,h) + c(h)`. Choose primes `q_1 < q_2 < …`, prime to M, in prescribed classes, with
`q_j > ∏_{i<j} q_i^{2e_i}` (Dirichlet). For `m = ∏ q_i^{e_i}` and `d | m²`, `d ≠ m`, the comparison
`d < m²/d` is decided by the largest index where the exponents of d and m²/d differ (that `q_j^{±1}`
dominates the rest). [The same holds for any fixed cone `λd < m²/d` once the q_j are large compared with
λ^{±1}; the diagonal `d = m` is the ψ-term, so finitely many cones only change ψ.] Write `ā = a⁻¹`, and
`φ_r := φ(a^r, a^{2−r})`, `ψ := ψ(a)`. The patterns (classes; exponents)

| pattern | m | expansion of `D(m²) − c(h)` |
|---|---|---|
| P1 | `q₁²q₂³`, `q₁≡ā, q₂≡a` | `φ₀+φ₃+φ₋₁+φ₋₂+φ₋₄+ψ` |
| P2 | `q₁q₂`, `q₁≡ā, q₂≡a²` | `φ₀+φ₂+φ₋₁+φ₋₂+ψ` |
| P3 | `q₁q₂`, `q₁≡1, q₂≡a` | `φ₀+φ₁+ψ` |
| P4 | `q₁²q₂q₃`, `q₁≡ā, q₂≡a, q₃≡a²` | `φ₁+φ₂+φ₃+φ₋₄+ψ` |

all have `m ≡ a`, `m² ≡ h`. (E.g. P3: the smaller member of each pair `{d, m²/d}` is `1, q₁, q₁²` (residue 1,
giving `3φ₀`) and `q₂` (pair `(q₂, q₁²q₂)`, giving `φ₁`).) The four expansions sum to `φ₀ = φ(1,h)` mod 2, so
`0 = Σ D(m_i²) = φ(1,h) + 4c(h) = φ(1,h)`. Then `D(p) = c(h)`, and `m = q ≡ a'` gives
`0 = D(q²) = φ(1,h) + ψ(a') + c(h)`. ∎

The rows are computed in the *free model* (`a` of infinite order; `scripts/inv_t1_free.py 3 3 -1 2` finds this
certificate); specialising to an actual `(M, a)` only identifies variables, so the cancellation persists for
every M and every unit a. Independent check on actual integers (actual primes with the size condition,
divisors enumerated, all variables cancel): `scripts/inv_t1_cert_check.py M a` for
`(M,a) = (840,11), (24,5), (120,7), (1,1), (7,3)`. In the free model restricted to residues `{1, a}` no
certificate exists (`inv_t1_free.py 3 2 0 1`): the classes `ā, a²` are needed.

**Remark 3.2 (what this does and does not exclude).** Prop 3.1 does **not** exclude divisor-type windmills:
`D(n) = 1 + [n = □]` (`c = 1`, `ψ = 1`, `φ = 0`) satisfies all T1 constraints. What it shows is the *shape*
any T1-compatible windmill must have: a periodic odd fixed point plus a fixed piece that sees exactly the
squares. Neither ingredient uses more about p than "p is not a square", so all the content of such a
windmill sits in the identity `W ≡ D (mod 2)` at composite non-squares of the class, about which T1 says
nothing. T1 alone is therefore no barrier to the windmill route; a barrier must come from the structure of
the maps (§4).

## 4. Finite-menu rigidity: uniform affine windmills cannot couple generic points

**Setting.** A *parametrisation* is a set `𝒳 ⊆ ℤ^d` with a rational *level function* `P` (regular on 𝒳); the
fibres are `X(n) = 𝒳 ∩ P⁻¹(n)`, n in a set F (all n of a class, or **only the primes** of a class). A
*finite-menu family* is a family of maps `σ_n : X(n) → X(n)` (n ∈ F) such that for every x,
`σ_n(x) ∈ {g_1(x), …, g_r(x)}` for a fixed finite list (the *menu*) of maps `g_i : ℚ^d → ℚ^d` that are affine
with coefficients rational functions of n (i.e. `g_i(x) = A_i(n)x + β_i(n)` evaluated at `n = P(x)`).
This contains every "piecewise-affine map with finitely many pieces" whatever the pieces are: polyhedra,
congruence cosets, sets defined through the factorisation of n or of anything else. Zagier's windmill is a
finite-menu family (three maps, n-independent) for `P = x² + 4yz`.

**Lemma 4.1 (PROVED, elementary).** Call a menu map g a *symmetry* if `P∘g = P` identically (as rational
functions of x, with `n := P(x)` substituted in the coefficients), and *invertible* if `g(n₀)` is invertible for
generic n₀. Put
* `Z₀ = ⋃_{g not a symmetry} {x : P(g(x)) = P(x)}` (zero sets of nonzero rational functions),
* `Z₁ = ⋃_{g degenerate symmetry} {x : x ∈ g(P(x))(ℚ^d)}` (the image of a rank-deficient affine map is a
  proper affine subspace, so this is a proper algebraic subset of the total space),
* `Z₂ = ⋃_{g in menu} cl g(Z₁)` (proper: affine/rational images do not raise dimension).

(i) For every n ∈ F and `x ∈ X(n) ∖ (Z₀ ∪ Z₂)`, `σ_n(x) = g(x)` for an invertible symmetry g of the menu.
(ii) Suppose moreover that the invertible symmetries of the menu that can map a point of 𝒳 to a point of 𝒳
outside a proper algebraic set `Z₃` generate a finite group H. Then with `Z = H·(Z₀ ∪ Z₁ ∪ Z₂ ∪ Z₃)` (proper,
algebraic, H-invariant), `G(n) := X(n) ∖ Z` is σ_n-invariant and `σ_n(x) ∈ H·x` for every `x ∈ G(n)`.

*Proof.* (i) Let g be the map used at x. As `P(σx) = P(x)` and `x ∉ Z₀`, g is a symmetry. If g were
degenerate, `y = σ(x) ∈ Z₁`, and `x = σ(y) = g'(y)` for the map g' used at y, so `x ∈ Z₂`. (ii) By (i) and
`x ∉ Z₃`, `σ(x) = h(x)` with `h ∈ H`; `σ(x) ∉ Z` because Z is H-invariant. ∎

So the only maps that act on *generic* points are invertible symmetries of the level function. In Zagier's
case these form the infinite group `O(x²+4yz)(ℤ)`, which is what lets a windmill move points between slices.
For n-dependent maps: an invertible g is a symmetry iff for generic n₀ the affine map `g(n₀)` maps the
(irreducible) level surface `S_{n₀} = {P = n₀}` onto itself, i.e. `F_{n₀}∘g(n₀) = μ·F_{n₀}` for its equation.

**Proposition 4.2 (PROVED). Invertible symmetries in the standard coordinates.**

(a) *ES coordinates*, `P(x,y,z) = 4xyz/(xy+yz+zx)`: for every n ≠ 0 the invertible affine maps preserving
`S_n` are the 6 coordinate permutations. So `H ⊆ S₃` even for n-dependent menus.

(b) *O152 coordinates* `(t,u,v)`, `P = tuv − u − v`: for every n ≠ 0 they are `{id, ρ}`. (Degenerate
symmetries exist, e.g. the constant map `x ↦ (n+2,1,1)`; Lemma 4.1 puts their images into Z.)

(c) *ET Type II coordinates* `(a,b,c,k)` (solutions `(abc, nkbc, nkac)`, level set `4abck − a − b − nk = 0`),
n-independent menus: `{(a,b,c,k) ↦ (λa, λb, c/λ², λk)} ⋊ ⟨a↔b⟩`. The scalings fix the solution `(x,y,z)`
(reparametrisations), so on solutions H acts through `⟨a↔b⟩`. (With n-dependent coefficients there are more,
e.g. `(a,b,c,k) ↦ (nk, b, c, a/n)`; it maps the solution `(x,y,z)` to `(y,x,z)`, i.e. it is again a coordinate
permutation of the solution. I do not classify the n-dependent case here.)

(d) *Divisor / SL₂ coordinates of X*, `(A,B,t)`, `P = (AB−1)/t` (O152's `γ = (A t; n B) ∈ SL₂(ℤ)`),
n-independent menus: `{(A,B,t) ↦ (αA, B/α, t)} ⋊ ⟨A↔B⟩`. Type II SL₂ coordinates `(f,f',c,d)`,
`P = (ff'−1)/(4c²d)` ((I)4), n-independent: `{(αf, f'/α, λc, d/λ²)} ⋊ ⟨f↔f'⟩`. (The per-level quadric
`AB − nt = 1` has the infinite unipotent symmetries `(A, B+kn, t+kA)`; they have n-dependent coefficients and
are *not* covered by (d) — see Remark 4.5.)

*Proofs.* (a) `F = cxyz − (xy+yz+zx)`, `c = 4/n`; `g(x)_i = λ_i x_{π(i)} + β_i` (the cubic part forces a
monomial linear part, by unique factorisation of `xyz`). Comparing coefficients in `F∘g = μF`: cubic
`μ = λ₁λ₂λ₃`; monomial `x_{π(i)}x_{π(j)}` (k the third index): `λ_iλ_j(cβ_k − 1) = −μ`, i.e. `1 − cβ_k = λ_k`;
linear: `cβ_iβ_j = β_i + β_j`, i.e. `(cβ_i − 1)(cβ_j − 1) = 1` for all pairs, so all `cβ_i − 1` equal ±1;
constant: `cβ₁β₂β₃ = β₁β₂ + β₂β₃ + β₃β₁`. The choice `cβ_i − 1 = 1` (all `β_i = n/2`) violates the constant
equation (`n²/2 ≠ 3n²/4`), so `β = 0` and then `λ_k = 1`.
(b) `F = tuv − u − v − n`. Monomial linear part as in (a); F has no quadratic monomials, and the quadratic part
of `F∘g` is `Σ_k β_kλ_iλ_j·(monomial)`, so β = 0. The constant term gives μ = 1 (n ≠ 0), the linear part
`−(u+v)` forces π to preserve `{u,v}` with coefficients 1, and then `λ_t = 1`.
(c) `F = 4abck − a − b − nk`. Monomial linear part; translations create the four distinct cubic monomials
`4β_k·(product of the other three)`, absent from F, so β = 0. The linear part `−a − b − nk` (c absent, generic n,
coefficients independent of n) forces π to fix c and k and preserve `{a,b}`, `λ_a = λ_b = λ_k = μ`, and
`λ_aλ_bλ_cλ_k = μ` gives `λ_c = μ⁻²`; then `(abc, nkbc, nkac)` is unchanged.
(d) The polar divisor of `(AB−1)/t` is `{t = 0}`, which an n-independent invertible affine g preserving the
function must map to itself: `t' = λt`. Then `A'B' − 1 = λ(AB−1)`; the quadratic part forces
`{A', B'} = {αA + a₀, βB + b₀}`, `αβ = λ`; the linear part forces `a₀ = b₀ = 0`, the constant `λ = 1`. For
`(ff'−1)/(4c²d)` the polar divisor `2{c=0} + {d=0}` has components of different multiplicity, so `c' = λc`,
`d' = νd`, and the same argument gives `λ²ν = 1` and the scaling/swap of `(f,f')`. ∎

**Lemma 4.3 (PROVED). Scalings act only on finitely many slices.**
(i) In (d) for X: if `α = r/s ≠ 1` (lowest terms) and both `(A,B,t)` and `(αA, B/α, t)` lie in 𝒳 (i.e.
`t | A+1`, `t | αA+1`), then `t | r − s`. Hence the points where a non-trivial scaling is used lie on the
finitely many planes `t = c`, `c | r − s`; the scaling maps each such plane to itself (it moves a factor
between A and B: a *divisor-moving* map on the divisor pairs of `cn+1`, preserving the slice integer).
(ii) In the Type II SL₂ coordinates, a scaling preserves `4c²d` and hence the slice integer `N = 4c²dn + 1`
and the divisor pair; it changes `(c,d)` only to `(λc, d/λ²)` with the same N.
*Proof.* (i) `sαA + s = rA + s ≡ s − r (mod t)` because `A ≡ −1`; and `t | αA + 1` means `t·s | rA + s`
(as `s | A` for `αA ∈ ℤ`), so `t | s − r`. (ii) is immediate from (d). ∎

**Theorem 4.4 (rigidity; PROVED).** (1) Let `(σ_n)` be a finite-menu family on the O152 sets X(n), n ranging
over any set F (e.g. only the primes ≡ 1 mod 24), in the `(t,u,v)` coordinates (menu coefficients rational in
n) or in the `(A,B,t)` coordinates (n-independent menu). Then there is a proper algebraic, ρ-invariant
`Z ⊂ ℚ³`, depending only on the menu (in the `(A,B,t)` case it contains finitely many planes `t = c`), such that
`G(n) = X(n) ∖ Z` is σ_n-invariant and `σ_n(x) ∈ {x, ρ(x)}` on G(n). In particular σ_n preserves the slice
index t (and the slice integer `tn+1`) of every point of G(n).
(2) In ES coordinates the same holds with `S₃` (H acts by permuting the coordinates of the solution).
(3) In ET Type II coordinates (n-independent menus), every `x ∉ Z₀ ∪ Z₂` is mapped to a parameter vector of the
same solution or of the solution with `y,z` exchanged (`a ↔ b`).

*Proof.* (1) Lemma 4.1(ii) with `H = {id, ρ}` (Prop 4.2(b), resp. (d)); in the `(A,B,t)` case `Z₃` = the planes
of Lemma 4.3(i). (2) Lemma 4.1(ii) with Prop 4.2(a). (3) Lemma 4.1(i) with Prop 4.2(c). ∎

Interpretation. The triage asked for a "set-theoretic cross-slice bijection between divisor sets of different
`N_θ(p)` respecting the moving classes". Theorem 4.4 says: **no such coupling of generic points exists in the
class of finite-menu (bounded-description) piecewise-affine maps** in any of the four natural coordinate
systems — the menu maps that are not symmetries of P can only act on a fixed proper algebraic subset, and the
symmetries (swap; reparametrising or divisor-moving scalings) never change the slice integer. This is the
precise form of the O152 "level = own matrix entry" remark and closes the gap left by WINDMILL Prop 2 (which
covered only maps preserving the equation identically): uniformity of the menu over n turns "preserves the
finite point sets" into "preserves P on a Zariski-dense set", which is the identical-preservation case.

**Remark 4.5 (the SL₂ unipotents; PROVED for this family).** For fixed n the quadric `AB − nt = 1` has the
infinite group of affine symmetries `(A,B) ↦ (αA + a₀, βB + b₀)` (`αβ` and t adjusted), containing O152's
unipotents `u_k : (A,B,t) ↦ (A, B + kn, t + kA)` (right multiplication of γ by `(1 k; 0 1)`). These have
n-dependent coefficients and are not covered by Prop 4.2(d). For them integrality alone suffices: if
`x ∈ 𝒳` and `u_k(x) ∈ 𝒳` with k ≠ 0, then (using `A ≥ t − 1 ≥ 0`, `t' = t + kA ≥ 1`, `t' | A + 1`): for k ≥ 1,
`t + kA ≤ A + 1` forces `k = 1, t = 1`; for k ≤ −1, `t − |k|A ≥ 1` and `A ≥ t − 1` force `A = t − 1` (u = 1) and
`|k| = 1`, or t = 1. So the unipotents act only on the planes `t = 1` and `u = 1` — the single degenerate
bijection `AB = n+1 ↔ (t,u) = (A+1,1)` found in O152 E4. (The general per-level group with n-dependent
`α, β, a₀, b₀` is not classified here.)

## 5. Consequence for windmills on X defined on primes only

Prop 2.3 kills every windmill on X that is defined on a whole congruence class. A construction may instead
be defined only on primes (using primality in the choice of pieces). Theorem 4.4 still applies, because it
needs no density over n beyond F itself.

**Theorem 5.1 (PROVED).** Let F be any set of primes `p ≡ 1 (4)` and let `(τ_p)_{p∈F}` be involutions of X(p)
forming a finite-menu family as in Theorem 4.4(1), with `Fix τ_p ⊆ E(p)` for all p ∈ F. Let Z be the proper
algebraic subset of Theorem 4.4 for τ's menu. Then for every p ∈ F the point `(p+2,1,1)` lies in Z, and
`|Fix τ_p ∩ Z|` is odd; in particular **E(p) ∩ Z ≠ ∅**. (No second involution σ is needed: |X(p)| is odd.)

*Proof.* On `G(p) = X(p) ∖ Z`, `τ_p ∈ {id, ρ}` pointwise, and G(p) is τ_p- and ρ-invariant. The point
`(p+2,1,1)` is fixed by id and by ρ, and is not in E(p) (`A = p+1 ≡ 2 (4)`); so it is not in G(p). Since it is
the only fixed point of ρ on X(p) (Lemma 2.1), ρ acts freely on G(p), `|G(p)|` is even, hence
`|Fix τ_p ∩ G(p)|` is even, while `|Fix τ_p| ≡ |X(p)| ≡ 1`. ∎
(For p ≡ 3 (4) the periodic point `(p+2,1,1)` is itself an ES element, `4 | p+1`: the easy case.)

So **a bounded-description involution on X can certify ES(p) only through ES elements lying on a fixed proper
algebraic surface Z ⊂ ℚ³** (fixed = independent of p). Every such windmill is therefore no stronger than the
statement "E(p) ∩ Z ≠ ∅ for all p ∈ F" for one fixed surface Z — a "finitely many slices" type statement in
the sense of the barrier map, with "slice" generalised from coordinate planes to arbitrary fixed surfaces.

**Lemma 5.2 (PROVED; Lemma 2.2 with p in place of m²).** Let `p ≡ 1 (8)` be prime and `(t,u,v) ∈ E(p)`,
`A = tu − 1 = 4·2^s·δ₀` with δ₀ odd. Then the Jacobi symbol `(δ₀/p) = −1`; in particular A has a prime factor
that is a quadratic non-residue mod p.
*Proof.* The proof of Lemma 2.2 uses only `m² ≡ 1 (8)` up to the last line, which now reads
`1 = (−tp/δ₀) = (−t/δ₀)(p/δ₀) = −(p/δ₀)`, and `(p/δ₀) = (δ₀/p)` as p ≡ 1 (4). ∎

**Corollary 5.3 (CONDITIONAL on Dickson's prime k-tuples conjecture; proof sketched, needs review).** If Z is
contained in a finite union of coordinate planes `{t=c}, {u=c}, {v=c}`, then infinitely many primes
`p ≡ 1 (24)` have `E(p) ∩ Z = ∅`. Hence no finite-menu windmill on X whose exceptional set is of this form
proves ES for all p ≡ 1 (24).
*Sketch.* On `{t=c}`, `A | cp+1`; on `{u=c}`, `A | p+c`; on `{v=c}`, `B = tc − 1 | p + c` and
`A = ((B+1)p + c)/(cB)` is determined by B. Take `p = Mq + 1` with M divisible by 8, 3, all relevant c, `c+1`
and their prime factors, and impose (Dickson) that each of the finitely many integers `cp+1`, `p+c` is a fixed
constant times one prime `r(q)`, and that each of the finitely many linear forms `A(B)` attached to the
bounded set of divisors B is a constant times a prime, with q in a class making every such prime ≡ 1 modulo
4·(all constants). By reciprocity every prime factor of every A that can occur is then a residue mod p,
contradicting Lemma 5.2. This is the mechanism of POINTWISE_SIZE Theorem C (formal odd square) applied to the
bounded program "test the finitely many planes"; I have not re-verified Theorem C's hypotheses line by line. ∎

**Remark 5.4 (non-coordinate surfaces; Assessment).** For a surface Z not of this form, E(p) ∩ Z is typically
sparse: e.g. on `Z = {t = u}`, `E(p) ∩ Z = {t odd : t² − 1 | p + t}`, and for p ≡ 1 (24) this needs
`t ≡ 23 (24)`, `p ≡ −t (mod t² − 1)`; Brun–Titchmarsh plus a union bound shows (unconditionally, sketch) that a
positive proportion of p ≡ 1 (24) have no such t. A general theorem "for every fixed proper surface Z, infinitely
many hard p have E(p) ∩ Z = ∅" would need a classification of the surfaces carrying ≫ 1 points per prime on
average (coordinate planes; possibly others) and is **not** proved here (CONJECTURE).

Checks: `scripts/inv_stab_check.py 13` and `97` (sympy; all permutations, generic monomial-plus-translation
maps) reproduce Prop 4.2(a)–(c): ES: only the 6 permutations; X: only id and ρ; Type II: the scalings
`(λa, λb, c/λ², λk)` and the swap, plus solutions whose coefficients involve n (the n-dependent maps of
Prop 4.2(c)). `scripts/inv_lemma52_check.py 1500`: Lemma 5.2 holds on all 275 E-elements of X(p),
p ≡ 1 (8), p < 1500.

## 6. Scope: what is excluded, what is left

**Excluded (PROVED):**
1. Any involution family on the O152 set X(n) with ES-only fixed points, of any complexity, defined on a
   square class (Prop 2.3). Any windmill family on any sets whose τ-fixed points are certificates absent at
   odd squares needs `|X(m²)|` even (Lemma 1.1).
2. A divisor-type σ-fixed count whose odd point at primes is the factorisation `1·p` (the Zagier mechanism):
   T1 forces `φ(1,h) = 0` (Prop 3.1). A T1-compatible divisor-type count must be "periodic point + square
   detector" (Remark 3.2) — allowed, but it carries no information about p beyond non-squareness.
3. Cross-slice coupling of generic points by finite-menu affine maps (pieces arbitrary, even prime-specific)
   in ES coordinates, in O152's (t,u,v) (coefficients may depend on n) and (A,B,t) coordinates, in ET Type II
   (a,b,c,k) and Type II SL₂ (f,f',c,d) coordinates (n-independent menus): Theorem 4.4. O152's SL₂ unipotents
   act only on two planes (Remark 4.5).
4. Finite-menu windmills on X restricted to primes certify only on a fixed proper surface (Thm 5.1); if that
   surface is a union of coordinate planes, they fail for infinitely many p ≡ 1 (24) under Dickson's
   conjecture (Cor 5.3, CONDITIONAL, sketch).

**Not excluded (honest list of escapes):**
* menus that are infinite or grow with p (e.g. divisor-moving scalings by every prime factor: unbounded
  description complexity), and non-affine (polynomial/rational) maps beyond the n-dependent affine ones;
* n-dependent menus in ET Type II and SL₂ coordinates beyond the families analysed (Prop 4.2(c), Rem 4.5);
* auxiliary sets other than X (e.g. sets built on a quadric with infinite orthogonal group whose fixed loci
  *map* to ES certificates), as long as their T1 behaviour (|X(m²)| even) and the image of the generic part are
  compatible — Theorem 4.4 must be redone in each coordinate system;
* windmills on X whose exceptional surface is not a union of coordinate planes (Remark 5.4: no theorem).

**Assessment.** Every bounded-description windmill we can write down reduces, by Lemma 4.1, to the symmetry
group of the level function in the chosen coordinates. For all natural ES coordinates that group is finite
up to reparametrisation and divisor-moving scalings (Prop 4.2), and none of its elements changes the slice
integer; this is the structural reason behind the O152/WINDMILL nulls. A windmill proof of ES would need a
coordinate system in which ES certificates are the fixed points of an involution drawn from an *infinite*
symmetry group of the level function (as `O(x²+4yz)` for Zagier), with the ES congruence preserved on generic
points. Remark 4.5 shows that the obvious candidate (the SL₂/quadric coordinates) fails exactly there.
