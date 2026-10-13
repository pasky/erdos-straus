# Windmills beyond finite menus: reduction theory, genus theory, Legendre-type parity (O164)

**Status: ES is not solved here.** Labels as in DISCOVERIES.md. Scripts `scripts/wr_*`.
Brief: `/tmp/es-briefs/full_t164.txt` (SPARK phase, CONSTRUCT). Predecessors: INVOLUTION_ES.md, INVOLUTION_ES2.md,
WINDMILL.md, BRAINSTORM/invol_*.md, DISCOVERIES (J)2.

## 1. Zagier's windmill is the dihedral symmetry of Conway rivers (dictionary)

Notation. For a non-square discriminant D > 0 let `Y(D) = {[a,b,c] ∈ ℤ³ : a > 0 > c, b² − 4ac = D}` (Conway's
*simple* forms, i.e. the edges of the topograph separating a positive from a negative value, with an orientation).
Zagier's set `X(p) = {(x,y,z) ∈ ℤ³_{>0} : x² + 4yz = p}` is identified with `{φ ∈ Y(p) : b > 0}` via
`(x,y,z) ↦ φ = [y, x, −z]`. The river step is the 2-piece map
`R[a,b,c] = [a+b+c, b+2c, c]` if `a+b+c > 0`, else `[a, b+2a, a+b+c]` (walk one edge along the river; `a+b+c ≠ 0`
since D is not a square). σ = swap `y ↔ z` (= `[a,b,c] ↦ [−c,b,−a]`), ζ = Zagier's 3-piece windmill.

**Observation 1.1 (algebra, PROVED by direct substitution).** Each piece of ζ is `φ ↦ −φ∘g` for an explicit
`g ∈ GL₂(ℤ)`; e.g. on `x < y − z`, `ζ(φ) = −φ∘g` with basis `(e₂, e₂ − e₁)`. Likewise `σ(φ) = −φ∘(e₂, e₁)`.
So ζ and σ map a form to an equivalent form of its *negative*; they never leave the topograph of φ up to sign.

**Computation 1.2 (CERTIFIED for all primes p ≡ 1 (4), p ≤ 1300; `scripts/wr_zagier_river.py 1300`).**
(i) The R-orbits on `Y(p)` are exactly the rivers (one per narrow class; `#orbits = h⁺(p)`), with period `L_C`.
(ii) The rotation `ζ∘σ` on `X(p)` has exactly `h⁺(p)` cycles, in bijection with the classes, of lengths `L_C/2`.
(iii) ζ maps the cycle of class C onto the cycle of the class `C⁻¹`; only the principal class is self-paired
(p prime, so h⁺(p) is odd and the principal class is the only ambiguous one).
Example p = 1297: h⁺ = 11, river lengths `[22,22,22,22,26,26,34,34,42,42,74]`, ζσ-cycles `[11,…,37]`.

**Reading (dictionary; PROVED given 1.2's structure, elementary).** ζ and σ both conjugate the rotation ρ = ζσ to
its inverse (`σρσ = σζ = ρ⁻¹`, same for ζ). Hence on each ρ-cycle they act as reflections of a polygon, or swap
two cycles. Paired classes `C ≠ C⁻¹` are swapped (no fixed points). The principal cycle has odd length
`L_1/2` (because `|X(p)| = Σ_C L_C/2` and the non-principal terms pair up), so each of ζ, σ has exactly **one**
fixed point on it. ζ's is the principal form `[1,1,−(p−1)/4]`; σ's is `[a,b,−a]`, i.e. `p = b² + 4a²`.
So Zagier's proof is the statement *"the principal river has odd half-period, and the reflection σ of an odd
polygon has a fixed vertex"* — this is H. J. S. Smith's (1855) palindromic-continuant proof and Legendre's
period-parity argument in topograph language. (I make no claim of novelty for this dictionary; it is the
folklore "Zagier = reduction" observation, here checked mechanically.)

**Consequence for the ES programme.** The windmill mechanism has three ingredients:
(W1) a finite set carrying a "rotation" whose cycles are classes (reduction cycles / rivers);
(W2) an involution pairing a class with its inverse, so that only **ambiguous** classes contribute fixed points;
(W3) an anchor that makes one ambiguous cycle odd (here: the principal form, the ζ-fixed point).
The fixed points of reflections of ambiguous cycles are *ambiguous / symmetric forms*: `[a,b,−a]`
(sums of two squares) or `a | b` (factorisations of D; Gauss: `#ambiguous classes = 2^{μ−1}`).
The ES question becomes: find D (built from p and a parameter) and a reflection whose fixed points on a
forced-odd cycle are ES certificates. §2 onwards.

## 2. A class-group formulation of a Type II slice (disc −4p)

**Lemma 2.1 (PROVED, elementary; a repackaging of ET Type II with `(a,b) = (N/β', β')`).** Let p be an odd prime.
If there are integers `b ≥ 1`, `e ≥ 1` with `e | p + 4b²` and `4b | p + e`, then ES(p): with `N = (p+e)/4`,
`α = N/b`, `β = b` (so `e | α + β` because `e | N + b²`),
`4/p = 1/N + 1/y + 1/z`, `y = pN(α+β)/(eα)`, `z = pN(α+β)/(eβ)`.
*Proof.* `4/p − 1/N = e/(pN)` and `1/y + 1/z = e(α+β)/(pN(α+β)) = e/(pN)`; integrality: α, β | N and e | α+β. ∎

**Corollary 2.2 (PROVED).** Put `k = (p+4b²)/e`. For `p ∤ b`, the condition `4b | p+e` is equivalent to
`4b | k+1` (as `ke ≡ p (mod 4b)` and `gcd(e,4b) = 1`). Hence ES(p) holds as soon as some **positive definite form
`[k, B, e]` of discriminant −4p has `B > 0`, `4 | B` and `B | k + 1`** (`B = 4b`). Equivalently: some odd `a` and
some `β` with `β² ≡ −p (mod a)`, `2 | β`, `2β | a+1` (then `[a, 2β, (β²+p)/a]` is such a form).
Call such forms **ES-forms**. For each primitive representation `a = Q(v)` the middle coefficient with `|B| ≤ a`
is unique (up to `B = ±a`), so the ES-condition is a property of (class, represented value, root of −p mod a).
At `p = m²` there are no ES-forms (they would give a Type II solution; ET Prop 1.6) — T1 is built in.

**Computation 2.3 (CERTIFIED, `scripts/wr_esforms.py`).** The slice of Cor 2.2 alone (discriminant −4p) is **not**
sufficient: among the 267 primes `p ≡ 1 (24)`, `p ≤ 20000`, 15 have no ES-form at all (exhaustive, using the bound
`b ≤ (p+1)/3` forced by `k ≥ 4b−1`, `e ≥ 4b−p`), e.g. 97, 193, 673, 1033, 1297; 78 have no *reduced* ES-form.

**Lemma 2.4 (PROVED; the full Type II e-slice as forms of discriminant −4gp, cf. STATUS (I)4).** ES(p) holds if for some
`g ≥ 1` there is a form `[k, B, c]` of discriminant `−4gp` with `B > 0`, `4g | B`, `B | k+1`. Proof: write
`B = 4gb`; then `c = ge`, `ke = p + 4gb²`, and `k ≡ −1 (mod 4gb)` gives `4bg | p + e`; with `N = (p+e)/4 = αβg`,
`β = b`, `α = N/(bg)`, one has `e | α + β` (as `4N ≡ −4gb² (mod e)`), and Lemma 2.1's formula with `x = N`,
`y = pN(α+β)/(eα)`, `z = pN(α+β)/(eβ)` works verbatim (α, β | N; `e | α+β` uses `gcd(e, bg) = 1`, which holds because a common prime divides
`ke − 4gb² = p`, while `e ≥ 4bg − p` and `e ≤ (p+4gb²)/(4gb−1)` force `bg < p`). ∎ So the windmill question for Type II is a
question about forms in the class groups `Cl(−4gp)`, g ≥ 1 (the Heegner discriminants of (I)4), and an "ES-form" is the
non-genus condition `B | k+1` on (class, represented value k, root).

## 3. Legendre/SQUFOF midpoints carry no ES bias (EVIDENCE, negative)

The forced object in Legendre's argument is the second ambiguous form of the principal cycle of √N
(the "midpoint"; for even period it yields a divisor `g = gcd(N, Q_{l/2−1})` — Legendre's / Shanks' factor).
`scripts/wr_legendre.py 20000 40` tests it as an ES certificate on all 267 primes `p ≡ 1 (24)`, `p ≤ 20000`:

| slice | trials | midpoint is a certificate | some divisor pair is a certificate | primes with no success |
|---|---|---|---|---|
| F1: `N = tp+1`, t odd ≤ 39, `A ≡ −1 (t)`, `4 | A` | 5073 | 113 (2.2%) | 740 (14.6%) | mid 175 / any 1 |
| F2: `N = (p+e)/4`, e ≤ 159, `e | g + N/g` | 10680 | 178 (1.7%) | 789 (7.4%) | mid 138 / any 16 |

The midpoint succeeds at roughly (any-rate)/(number of factor pairs): no forcing, no bias. **Assessment:**
in these discriminants the forced ambiguous form is a lottery ticket like any other divisor.

## 4. Type I: the σ-symmetric river does not prefer ES divisors (EVIDENCE, negative)

Type I ⟺ `f | D = p² + 4c²d`, `f ≡ −p (mod 4cd)` ((I)3). In discriminant D the simple form `[c, p, −cd]` lies on
a river; for d = 1 it is σ-fixed (`[c,p,−c]`, the windmill's "two-squares" point `D = p² + (2c)²`). Ambiguous forms
on a river ↔ factor pairs of D, so the natural Legendre-type hope is: *the ambiguous points on the river of
`[c,p,−cd]` are ES divisors.* `scripts/wr_typeI_river.py 3000 6 6` (46 primes `p ≡ 1 (24)`, c, d ≤ 6, 1655 pairs):
the class is ambiguous in 1244 cases; its river holds 1941 of all 5896 factor pairs (33%) and 20 of all 82
certificate pairs (24%). **No enrichment** (Assessment: the class of `[c,p,−cd]` sees divisors through genus/class
data only, and the ES condition mod 4cd is not class data).

## 5. Structural observations (dictionary items)

**5.1 Positive ES is definite (CM); signed ES is indefinite (rivers). (PROVED for the Type II slices of Lemma 2.4;
cf. the CM dictionary of (J)1.)** Replacing p by −p in Lemma 2.1/2.4 turns `ke = p + 4gb²` (forms of disc −4gp,
definite) into `ke = 4gb² − p` (disc +4gp, indefinite), and the formula yields `4/p = −1/N + 1/|y| + 1/|z|`, a
*signed* solution (always available). Zagier's set `x² + 4yz = p` is the indefinite side (`yz = (p − x²)/4`:
divisors of *downward* shifts of p); ES needs divisors of *upward* shifts `p + 4gb²`. On definite discriminants
the topograph has a well and no river: Gauss reduction has no cycles, a finite reduction-closed set of forms is a
union of classes, and the reduction-type involutions available are class-group involutions (`φ ↦ ψφ⁻¹`), whose
fixed points are ambiguous forms or square roots in Cl — genus data of the fixed discriminant −4gp, i.e.
factorisations of g. **Consequence (Assessment, stated precisely):** ingredient (W1) of §1 (a rotation with long
cycles) is unavailable on the Heegner side; a Zagier-type windmill for ES must live on an *indefinite* auxiliary
discriminant and transport fixed points to definite (CM) data, as σ does in Zagier (σ-fixed river edges ↔ the
definite form x² + 4y²).

**5.2 X-slice certificates are faces adjacent to ambiguous edges (PROVED, algebra).** `γ = [[A,t],[p,B]] ∈ SL₂(ℤ)`,
`AB − pt = 1` ↔ the simple form `[p, B−A, −t]` of discriminant `T² − 4`, `T = A+B`. The ES conditions
`A ≡ B ≡ −1 (mod t)` are equivalent to `T ≡ −2 (mod t)` and `t | B − A`, i.e. `[−t, A−B, p]` is an **ambiguous**
form (`a | b`) of discriminant `T² − 4 = (T−2)(T+2)`, and p is the face across that ambiguous edge. So ES(p) via X
⟺ for some T, some ambiguous river of discriminant `T² − 4` has p as the face adjacent to an ambiguous edge whose
other face −t divides T+2 (plus `4 | A`). Ambiguous rivers are exactly the reflection-symmetric ones; this is the
precise sense in which ES certificates are "fixed points of a reflection", but on a discriminant chosen per
certificate (T is part of the solution — B2 in reflection language).

**5.3 Modular-hyperbola form (PROVED, elementary).** The per-level quadric `AB − pt = 1` has symmetry group
`ℤ² ⋊ ⟨A↔B⟩` (translations `A += kp`, `B += lp`, t adjusted; abelian, so not hyperbolic like `O(x²+4yz)`), and in
each orbit only the representative with `A, B ≤ p + O(1)` can satisfy `t | A+1`, `t | B+1`. So X-slice ES(p) ⟺
some `A ∈ [1, p)` with `4 | A`, `B = A⁻¹ mod p`, has `t = (AB−1)/p` dividing `A+1` and `B+1`: a *small-product
point* of the modular hyperbola `AB ≡ 1 (p)`. Involutions of the hyperbola that are algebraic over 𝔽_p (Möbius)
have fixed points = square roots mod p (Legendre-symbol data); the ES condition is archimedean (sizes of lifts).
A windmill here must mix the two, as Zagier's inequalities do.
