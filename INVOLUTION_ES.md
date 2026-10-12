# Involution / windmill route to Erdős–Straus: obstruction theorems (O158)

**Status: ES is not solved here.** This file is the depth follow-up of `BRAINSTORM/invol_windmill_signature.md`
(O152a), `invol_topological.md`, `invol_sign_identities.md` and `WINDMILL.md`. Labels as in DISCOVERIES.md.
Scripts: `scripts/inv_*`.

## 0. Summary (outcome: (B) — obstruction theorems with explicit scope; no construction)

* **T1 kills the O152 odd set on square classes (PROVED, Prop 2.3).** For every odd prime q, `|X(q²)|` is odd
  while its ES part is empty (Lemma 2.2, a parametric form of ET Prop 1.6). So no involution of X(q²) has
  ES-only fixed points. This is a pointwise statement, which is why it holds regardless of how the involution
  is described. A windmill on X therefore cannot be required to work on a unit square class. Windmills on X
  defined on primes only are not affected by T1 (§5). (R158 repair) Lemma 1.1 (an instance of the remark after ET Prop 1.6): any windmill family whose τ-fixed points
  are Type I/II-type certificates needs `|X(m²)|` even.
* **T1 for divisor-type fixed counts (PROVED, Prop 3.1).** For a windmill family defined on the whole class h,
  squares included (R158 repair), if the σ-fixed count is divisor-type mod M (with
  cones, square terms, periodic terms), T1 forces the coefficient of the factorisation `1·p` to vanish: the
  odd point at primes must be a periodic point cancelled at squares by a square detector. A 4-pattern
  certificate in a free model works for every modulus. T1 alone is not a barrier (`1 + [n=□]` passes).
* **Finite-menu rigidity (PROVED, Lemma 4.1, Prop 4.2, Thm 4.4).** If an involution family uses a fixed
  finite list of affine maps (pieces arbitrary, even prime-specific), then outside a fixed proper algebraic
  set Z it acts by symmetries of the level function. In ES, O152 (t,u,v) [n-dependent coefficients allowed],
  O152 SL₂ (A,B,t), ET Type II and Type II SL₂ coordinates [n-independent], these are the coordinate swap,
  reparametrisations and divisor-moving scalings, and none changes the slice integer. So no cross-slice
  coupling of *generic* points exists in this class. Z depends on the menu and is otherwise arbitrary, and a
  windmill may act non-trivially **only on Z**, so this excludes nothing by itself. It **reduces** the gap left by
  WINDMILL Prop 2 ("pieces preserving only the finite point set") to windmills supported on a fixed proper
  algebraic set Z, i.e. to a bounded-slice statement (Thm 5.1). It does not close that gap. (R158 repair)
* **Primes-only windmills on X (PROVED, Thm 5.1).** Any finite-menu involution on X(p), p ≡ 1 (4), with ES-only
  fixed points certifies ES(p) through an ES element on a fixed proper surface Z. So such a windmill is
  equivalent to the **bounded-slice statement `E(p) ∩ Z ≠ ∅` for all p** (Z fixed). For Z a union of coordinate
  planes, such windmills fail infinitely often under Dickson (Cor 5.3, CONDITIONAL). General Z: open.
  **Unconditionally, no windmill defined on primes only is excluded.** The data are consistent with
  coordinate-plane windmills: for every prime p ≡ 1 (24) up to 40000, E(p) meets the 33 planes `{t=c}`,
  `{u=c}`, `{v=c}`, c ≤ 11 (EVIDENCE, `scripts/review_inv_planes.py 40000`). (R158 repair)
* **Status of the route (R158 repair): narrowed, not barred.** What survives T1 and the rigidity results:
  * finite-menu windmills on X defined on primes only, whose relevant fixed points live on a fixed proper
    surface Z (excluded under Dickson when Z is a union of coordinate planes);
  * infinite or growing menus, and non-affine maps;
  * the n-dependent SL₂ symmetry group;
  * other auxiliary sets.

  See §6.

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

(R158 repair) This is a direct instance of the remark after ET Prop 1.6 (Elsholtz–Tao, arXiv:1107.1010): any
method showing `f_I(p)` or `f_II(p)` is nonzero "must necessarily fail when p is replaced by an odd square such
as p²". The T1 principle is theirs (going back to Schinzel and Yamamoto); Lemma 1.1 only phrases it for
involution families.

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
(ii) no family of involutions `τ_n` of `X(n)` with `Fix τ_n ⊆ E(n)` can be defined on all n of a square class
`h (mod M)`: it fails at `n = q²` for every prime `q` with `q² ≡ h`. (R158 repair: this is pointwise. By (i), no
involution of X(q²) whatsoever has ES-only fixed points, so the description complexity of the family is
irrelevant. Windmills on X defined on primes only are not affected, see §5.)
(iii) more generally, for odd n, `|X(n)| ≡ #{u | n : n/u ≡ −2 (mod u)}`, where u runs over unitary
divisors of n (for odd n, `u | n/u + 2` forces `gcd(u, n/u) = 1`); `u = 1` always contributes.

*Proof.* Lemma 2.1: `u | q²` and `u | q²/u + 2`; u = q fails (`q ∤ q+2`), u = q² fails (`q² ∤ 3`), u = 1
works (`t = q²+2`). So `|X(q²)| ≡ 1`. `E(q²) = ∅` by Lemma 2.2. (i), (ii) follow; (iii) is Lemma 2.1. ∎

(In (ii), h is a unit square class, `h ≡ a² (mod M)` with `gcd(a,M) = 1`, so that Dirichlet supplies primes
`q ≡ a`.) So the O152 set has the right parity at primes for the *wrong* reason: its odd point `(n+2,1,1)`
exists for every n (a "periodic" fixed point), and nothing cancels it at squares. Any involution family on X
defined on a whole square class has non-ES fixed points at the members q² of the class; so a windmill on X
must either be defined only on (a subset of) the non-squares, e.g. the primes, or have fixed points whose
ES-ness is proved only at those n. §4–§5 treat constructions defined on primes only.

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
this when D is the σ-fixed count of a windmill family on the *whole* class h, squares included, with D valid
at every odd m² of the class, and with τ-fixed points that are certificates which do not exist at odd squares
(R158 repair)).
In particular Prop 3.1 says nothing about windmills defined on primes only. Then `φ(1,h) = 0`; hence `D(p) = c(h)` for every prime `p ≡ h`, and
`ψ(a') = c(h)` for every `a'` with `a'² ≡ h`. In particular, if `D(p)` is odd then `c(h) = 1` and `ψ(a') = 1`.

So, *for a windmill family defined on the whole class h, squares included* (R158 repair), *the odd fixed point
at primes can never come from the divisor part `1·p`* (as it does in Zagier's proof,
where the fixed point `(1,1,(p−1)/4)` is the factorisation `p = 1·(1+4z)`); it must be a periodic point
present for every n of the class, and then the fixed locus must contain a square-detecting piece that cancels
it at every m². (For X(n) the periodic point is `(n+2,1,1)` and the square piece is missing: Prop 2.3.)

*Proof.* `D(p) = φ(1,h) + c(h)`. Choose primes `q_1 < q_2 < …`, prime to M, in prescribed classes, with
`q_j > ∏_{i<j} q_i^{2e_i}` (Dirichlet). For `m = ∏ q_i^{e_i}` and `d | m²`, `d ≠ m`, the comparison
`d < m²/d` is decided by the largest index where the exponents of d and m²/d differ (that `q_j^{±1}`
dominates the rest). [If D is defined with finitely many fixed homogeneous cones `λ_j u < v < μ_j u` instead of `u < v`,
take the q_j also large compared with all `λ_j^{±1}, μ_j^{±1}`: at the specific m used below every pair
`(d, m²/d)`, `d ≠ m`, has ratio `≥ q_1` or `≤ 1/q_1`, so `D(m²)` equals the model expression for suitable
`(φ, ψ)` (φ records which cones contain the two limiting directions, ψ the diagonal). The proof below uses D
only at these m, so it applies verbatim; cone-restricted counts are *not* claimed to be residue functions in
general.] Write `ā = a⁻¹`, and
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

**Lemma 4.1 (PROVED, elementary).** Let `(σ_n)` be a finite-menu family of **involutions**. Assume the generic
level set `S_{n₀} = cl{P = n₀}` is irreducible and not contained in an affine hyperplane (true for all P below).
Call a menu map g a *symmetry* if `P∘g = P` identically (as rational functions of x, with `n := P(x)`
substituted in the coefficients). A symmetry is *invertible* if `g(n₀)` is invertible for generic n₀, else
*degenerate*. Let `E` be the finite set of levels n₀ at which some coefficient has a pole or the genericity
statements below fail, and put
* `Z₀ = ⋃_{g not a symmetry} cl{x : P(g(x)) = P(x)}` (zero sets of nonzero rational functions),
* `Z₁ = ⋃_{g degenerate symmetry} cl{x : x ∈ g(P(x))(ℚ^d)}`: for generic n₀ the image `L(n₀)` of `g(n₀)` is a
  proper affine subspace, and `S_{n₀} ⊄ L(n₀)`, so `Z₁ ∩ S_{n₀}` is a proper closed subset of `S_{n₀}` and Z₁ is
  proper,
* `Z₂ = ⋃_{g in menu} cl g(Z₁)` (proper: affine/rational images do not raise dimension), all closures Zariski
  closures over ℚ̄.

(i) For every `n ∈ F ∖ E` and `x ∈ X(n) ∖ (Z₀ ∪ Z₂)`, `σ_n(x) = g(x)` for an invertible symmetry g of the menu.
(ii) [R158 repair: precisely, H is generated by the menu's invertible symmetries h for which some point x of
the integral set outside Z₃ has h(x) in the integral set.] Suppose moreover that the invertible symmetries of the menu that can map a point of 𝒳 to a point of 𝒳
outside a proper algebraic set `Z₃` generate a finite group H. Then with `Z = H·(Z₀ ∪ Z₁ ∪ Z₂ ∪ Z₃)` (proper,
algebraic, H-invariant), `G(n) := X(n) ∖ Z` is σ_n-invariant and `σ_n(x) ∈ H·x` for every `x ∈ G(n)`, n ∉ E.

*Proof.* (i) Let g be the map used at x. As `P(σx) = P(x)` and `x ∉ Z₀`, g is a symmetry. If g were
degenerate, `y = σ(x) ∈ Z₁`, and `x = σ(y) = g'(y)` (σ is an involution) for the map g' used at y, so
`x ∈ Z₂`. (ii) By (i) and `x ∉ Z₃`, `σ(x) = h(x)` with `h ∈ H`; `σ(x) ∉ Z` because Z is H-invariant. ∎
(The hyperplane hypothesis is needed: for `P(x,y) = x` the rank-1 maps `g(n)(x,y) = (n,y)` compose to the
identity. Here the level sets are irreducible cubic surfaces in (a), (b) and irreducible hypersurfaces in
(c), (d); none lies in a hyperplane.)

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
(ii) In the Type II SL₂ coordinates, a scaling preserves `4c²d` and hence the slice integer
`N = ff' = 4c²dn + 1`; it moves a factor α between f and f′ and changes `(c,d)` to `(λc, d/λ²)`, with the same N.
*Proof.* (i) `rA + s ≡ s − r (mod t)` because `A ≡ −1`; and `t | αA + 1` means `t·s | rA + s`
(as `s | A` for `αA ∈ ℤ`), so `t | s − r`. (ii) is immediate from (d). ∎

**Theorem 4.4 (rigidity; PROVED).** (1) Let `(σ_n)` be a finite-menu family of involutions on the O152 sets X(n), n ranging
over any set F (e.g. only the primes ≡ 1 mod 24), in the `(t,u,v)` coordinates (menu coefficients rational in
n) or in the `(A,B,t)` coordinates (n-independent menu). Then there is a proper algebraic, ρ-invariant
`Z ⊂ ℚ³`, depending only on the menu (in the `(A,B,t)` case it contains finitely many planes `t = c`), such that for all but finitely many n,
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
precise form of the O152 "level = own matrix entry" remark. Uniformity of the menu over n turns "preserves
the finite point sets" into "preserves P on a Zariski-dense set", which is the identical-preservation case
covered by WINDMILL Prop 2.

(R158 repair) **What this does not exclude.** Z depends on the menu and is otherwise an arbitrary fixed proper
algebraic set, and Theorem 4.4 says nothing about how σ acts on Z. A windmill may act non-trivially *only* on
Z. Theorem 4.4 therefore **reduces** the WINDMILL Prop 2 gap to windmills supported on a fixed proper algebraic
set; it does not close it. For X, Theorem 5.1 makes the reduction exact: such a windmill is equivalent to the
bounded-slice statement `E(p) ∩ Z ≠ ∅` for all p. Nothing excludes this unconditionally. Cor 5.3 excludes it
under Dickson's conjecture for coordinate-plane Z only, and the data are consistent with it.
EVIDENCE (`scripts/review_inv_planes.py 40000`): for every prime p ≡ 1 (24) up to 40000, E(p) meets the
33 planes `{t=c}`, `{u=c}`, `{v=c}`, c ≤ 11. In practice, ES certificates live on low slices; CONDITIONAL_ES
records t ≤ 367 for all Mordell-hard primes below 2·10⁶.

(R158 repair) *Precursor.* Elsholtz, "A combinatorial approach to sums of two squares and related problems"
(Additive Number Theory, Springer 2010), §§2.1 and 3, derives Zagier's matrix (and its analogues for
`sx² + tyz`) *uniquely* from three assumptions: a linear map with k-independent integer coefficients,
identical invariance of the form, and a prescribed unique fixed point. That is the "uniform coefficients ⇒
symmetry of the form" mechanism of Prop 4.2, with identical invariance *assumed*. The new step here is
Lemma 4.1, which *derives* identical invariance off a fixed algebraic set from "finite menu + preserves the
fibres". I could not check Jackson, Generalov or Shiu (cited there).

**Remark 4.5 (the SL₂ unipotents; PROVED for this family).** For fixed n the quadric `AB − nt = 1` has the
infinite group of affine symmetries `(A,B) ↦ (αA + a₀, βB + b₀)` (`αβ` and t adjusted), containing O152's
unipotents `u_k : (A,B,t) ↦ (A, B + kn, t + kA)` (right multiplication of γ by `(1 k; 0 1)`). These have
n-dependent coefficients and are not covered by Prop 4.2(d). For them integrality alone suffices: if
`x ∈ 𝒳` and `u_k(x) ∈ 𝒳` with k ≠ 0, then (using `A ≥ t − 1 ≥ 0`, `t' = t + kA ≥ 1`, `t' | A + 1`): for k ≥ 1,
`t + kA ≤ A + 1` forces `k = 1, t = 1`; for k ≤ −1, `t − |k|A ≥ 1` and `A ≥ t − 1` force `A = t − 1` (u = 1) and
`|k| = 1` (the case t = 1 would force A = 0, which is impossible; R158 repair). So the unipotents act only on the planes `t = 1` and `u = 1` — the single degenerate
bijection `AB = n+1 ↔ (t,u) = (A+1,1)` found in O152 E4. (The general per-level group with n-dependent
`α, β, a₀, b₀` is not classified here. (R158 repair) That group is infinite and its elements change the slice integer, so
Remark 4.5 does **not** settle the SL2/quadric coordinates. Only the unipotents u_k with fixed integer k are
shown to act on two planes; the full n-dependent SL2 symmetry group remains an open escape.)

## 5. Consequence for windmills on X defined on primes only

Prop 2.3 kills every windmill on X that is defined on a whole congruence class. A construction may instead
be defined only on primes (using primality in the choice of pieces). Theorem 4.4 still applies, because it
needs no density over n beyond F itself.

**Theorem 5.1 (PROVED).** Let F be any set of primes `p ≡ 1 (4)` and let `(τ_p)_{p∈F}` be involutions of X(p)
forming a finite-menu family as in Theorem 4.4(1), with `Fix τ_p ⊆ E(p)` for all p ∈ F. Let Z be the proper
algebraic subset of Theorem 4.4 for τ's menu. Then for all but finitely many p ∈ F the point `(p+2,1,1)` lies in Z, and
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
*Sketch (R158 repair: branch bookkeeping and the residue step corrected).* Take `p = Mq + 1`, with M divisible by
8, by 3 and by high powers of every constant appearing below (all relevant c, c+1, d+1, c+d+1, …). The
candidate values of A on each plane are:
* `{t=c}`: A divides `cp+1 = (c+1)·r`, where `r = (cM/(c+1))q + 1`;
* `{u=c}`: `A = tc − 1` divides `p+c = (c+1)·r'`, where `r' = (M/(c+1))q + 1`;
* `{v=c}`: `B = tc − 1` divides `p + c = (c+1)r'`, so `B = d` or `B = d·r'` with `d | c+1`. A is determined by B,
  and in both branches it is linear in q:
  * `cd·A = (d+1)p + c` for `B = d`;
  * `cd·A = dp + c + 1` for `B = d·r'` (use `p = (c+1)r' − c`, so that `(dr'+1)p + c = r'(dp+c+1)`).

  Both identities were checked symbolically by R158.

So every candidate A is a fixed integer K_i times a value of a linear form `α_i q + 1`. Dickson's conjecture
applies to the finitely many forms `Mq+1`, `α_i q + 1`: they are admissible once every prime ℓ ≤ (number of
forms) divides every α_i. So all of them are simultaneously prime for infinitely many q.

The residue step: choose M so large that `L := 8·∏(c, d+1, c+1, …)` divides every α_i. Then each prime is
automatically ≡ 1 (mod L). Choosing the class of q could not achieve this, since the residue of `α_i q + 1`
mod L is fixed once `L | α_i`. Every prime factor of A is then a residue mod p:
* the primes of K_i divide M, so p ≡ 1 mod them;
* 2 is a residue because p ≡ 1 (8);
* the big primes satisfy `(−c/r) = (−c(d+1)/s) = (−d(c+1)/s) = 1`.

This contradicts Lemma 5.2. The label stays CONDITIONAL (Dickson); with these repairs the sketch is a complete
conditional argument (R158 review, §"Cor 5.3"). ∎

**Remark 5.4 (non-coordinate surfaces; Assessment).** For a surface Z not of this form, E(p) ∩ Z is typically
sparse: e.g. on `Z = {t = u}`, `E(p) ∩ Z = {t odd : t² − 1 | p + t}`, and for p ≡ 1 (24) this needs
`t ≡ 15` or `23 (mod 24)` and `p ≡ −t (mod t² − 1)` (e.g. p = 433, t = 15). Since `Σ_t 1/φ(t²−1)` converges, a
Brun–Titchmarsh union bound *should* show that a positive proportion of p ≡ 1 (24) have no such t; I have not
checked the constants (heuristic, not a claim). A general theorem "for every fixed proper surface Z, infinitely
many hard p have E(p) ∩ Z = ∅" would need a classification of the surfaces carrying ≫ 1 points per prime on
average (coordinate planes; possibly others) and is **not** proved here (CONJECTURE).

Checks: `scripts/inv_stab_check.py 13` and `97` (sympy; all permutations, generic monomial-plus-translation
maps) reproduce Prop 4.2(a)–(c): ES: only the 6 permutations; X: only id and ρ; Type II: the scalings
`(λa, λb, c/λ², λk)` and the swap, plus solutions whose coefficients involve n (the n-dependent maps of
Prop 4.2(c)). `scripts/inv_lemma52_check.py 1500`: Lemma 5.2 holds on all 275 E-elements of X(p),
p ≡ 1 (8), p < 1500.

## 6. Scope: what is excluded, what is left (rewritten as an R158 repair)

**Bottom line (R158 repair).** The windmill route is **narrowed, not barred**. Finite-menu windmills reduce to a
bounded-slice statement `E(p) ∩ Z ≠ ∅` for a fixed proper surface Z (Thm 5.1). **Unconditionally, no windmill
defined on primes only is excluded.** The surviving route consists of windmills whose relevant fixed points
live on a fixed proper surface Z. For coordinate-plane Z these are excluded under Dickson's conjecture
(Cor 5.3, CONDITIONAL). Infinite or growing menus, non-affine maps, the n-dependent SL₂ group and other
auxiliary sets remain open as well.

**Excluded (PROVED):**
1. Windmills on the O152 set X(n) that are required to work at some n = q², q an odd prime: no involution of
   X(q²) has ES-only fixed points (Prop 2.3; pointwise, so the description complexity is irrelevant). Hence a
   windmill on X cannot be defined on a unit square class. More generally, any windmill on any sets whose
   τ-fixed points are certificates absent at odd squares needs `|X(m²)|` even wherever it is defined at an odd
   square (Lemma 1.1, an instance of the remark after ET Prop 1.6). Windmills defined on primes only are
   **not** affected. (R158 repair)
2. For windmill families defined on the *whole* class h, squares included: a divisor-type σ-fixed count
   whose odd point at primes is the factorisation `1·p` (the Zagier mechanism). T1 forces `φ(1,h) = 0`
   (Prop 3.1). A T1-compatible divisor-type count must be "periodic point + square detector" (Remark 3.2),
   which is allowed but carries no information about p beyond non-squareness. Windmills defined on primes
   only are **not** affected. (R158 repair)
3. Moving *generic* points (outside a fixed proper algebraic set Z depending on the menu) across slices by
   finite-menu affine maps (pieces arbitrary, even prime-specific). This covers ES coordinates, O152's
   (t,u,v) with coefficients that may depend on n, and (A,B,t), ET Type II (a,b,c,k) and Type II SL₂
   (f,f',c,d) with n-independent menus (Theorem 4.4). O152's SL₂ unipotents u_k (fixed integer k) act only on
   two planes (Remark 4.5). This excludes no windmill by itself: the windmill may act only on Z. (R158 repair)
4. Reduction (not exclusion): finite-menu windmills on X restricted to primes certify ES(p) only through
   `E(p) ∩ Z` for a fixed proper surface Z (Thm 5.1). They are therefore equivalent to the bounded-slice
   statement "`E(p) ∩ Z ≠ ∅` for all p". (R158 repair)

**Conditional:** if Z is a union of coordinate planes, such windmills fail for infinitely many p ≡ 1 (24)
under Dickson's conjecture (Cor 5.3, CONDITIONAL; branch bookkeeping completed in the R158 repair). This is the
only exclusion of a primes-only windmill in this file, and it is conditional. The data do not refute
coordinate-plane windmills in any computed range: for all primes p ≡ 1 (24) up to 40000, E(p) meets the planes
`{t,u,v = c}`, c ≤ 11 (EVIDENCE, `scripts/review_inv_planes.py`).

**Not excluded (the surviving route):**
* finite-menu windmills on X defined on primes only and supported on a fixed proper surface Z: unconditionally
  for all Z, and also conditionally when Z is not a union of coordinate planes (Remark 5.4: no theorem);
* menus that are infinite or grow with p (e.g. divisor-moving scalings by every prime factor: unbounded
  description complexity), and non-affine (polynomial/rational) maps beyond the n-dependent affine ones;
* n-dependent menus in ET Type II and SL₂ coordinates beyond the families analysed (Prop 4.2(c), Rem 4.5). In
  particular, the full per-level affine group of `AB − nt = 1`, `(αA+a₀, βB+b₀, ·)` with α, β, a₀, b₀ ∈ ℚ(n),
  is infinite, changes the slice integer and is not classified;
* auxiliary sets other than X (e.g. sets built on a quadric with infinite orthogonal group whose fixed loci
  *map* to ES certificates), as long as their T1 behaviour (|X(m²)| even) and the image of the generic part are
  compatible. Theorem 4.4 must be redone in each coordinate system.

**Assessment.** By Lemma 4.1, every finite-menu affine windmill in the coordinates above acts on generic points
only through the symmetry group of the level function; the exceptional-surface part is *not* excluded. For
all natural ES coordinates (n-independent menus where stated) that group is finite up to reparametrisation and
divisor-moving scalings (Prop 4.2), and none of its elements changes the slice integer. This is the structural
reason behind the O152/WINDMILL nulls on generic points. A windmill proof of ES must therefore do one of the
following:
* live on a fixed exceptional surface, which is equivalent to a bounded-slice statement;
* use an infinite or growing menu, or non-affine maps;
* use a coordinate system with an *infinite* symmetry group of the level function (as `O(x²+4yz)` for
  Zagier), with the ES congruence preserved on generic points.

Remark 4.5 shows only that the integer unipotents of the SL₂/quadric coordinates act on two planes; the full
n-dependent SL₂ group is open. (R158 repair: the earlier sentence "the obvious candidate fails exactly there"
overclaimed.)
