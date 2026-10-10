# QUATERNION_ES — quaternionic / supersingular reformulation of Erdős–Straus (task O130)

Labels as in DISCOVERIES.md: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
ES is not solved here. Notation: Type I solution of `4/p` at level d = ET data `(a,b,c,d)` with
`e = (a+b)/c`, `f = 4acd − p`, so (ET (2.1)–(2.7))
`4abd = pe + 1`, `a + b = ce`, `ef = 4a²d + 1`, `ef' = 4b²d + 1` (`f' = 4bcd − p`), `ff' = p² + 4c²d`.
`w = √−d`, `K = ℚ(w)`. Scripts: `scripts/quat_*.py`.

## 1. The Type I dictionary: an x = 2 Gross–Zagier collision in B_{p,∞}

### Lemma 1.1 (K-factorisation; PROVED, elementary)
Type I(p) at level d holds iff there are `a, b, c, e ≥ 1` with
`(1 + 2a w)(1 + 2b w) = e(2c w − p)`  in `ℤ[w]`, and `gcd(c,p) = 1`.
*Proof.* LHS `= 1 − 4abd + 2(a+b)w`. Compare coefficients: `4abd − 1 = pe`, `a + b = ce`; these are ET's
(2.1),(2.2) with `b = ce − a`. ∎
Equivalently (eliminating b): `e | 4a²d + 1` (i.e. `(2a)²d ≡ −1 mod e`, i.e. `1 + 2aw ∈ 𝔢` for an ideal 𝔢 of
norm e), `b ≡ −a (mod e)`, `p = (4abd − 1)/e`. [Given `4abd ≡ 1 (e)`: `e | a+b ⟺ e | 4a²d+1`, since
`4ad(a+b) = (4a²d+1) + (4abd−1)` and `gcd(4ad, e) = 1`.]

### Lemma 1.2 (the order Λ_{d,m}; PROVED)
For integers `d, m ≥ 1` let `Λ_{d,m} = ℤ⟨u, v⟩`, `u² = −d`, `v² = −m`, `uv + vu = 1`. Then
`Λ_{d,m} = ℤ + ℤu + ℤv + ℤuv` is an order (closed: `vu = 1 − uv`) in the definite algebra
`B_{d,m} ≅ (−d, −d(4dm − 1))_ℚ` (basis change `v ↦ 2dv + u`, which anticommutes with u and squares to
`−d(4dm−1)`), and its reduced discriminant is `4dm − 1`.
*Proof of the discriminant.* Gram matrix of `trd(x_i x_j)` on `(1, u, v, uv)`:
`[[2,0,0,1],[0,−2d,1,0],[0,1,−2m,0],[1,0,0,1−2dm]]`, determinant `−(4dm−1)²`. ∎

### Proposition 1.3 (Type I ⇒ an x = 2 collision of CM points mod p; PROVED; EVIDENCE check)
Let `(a,b,c,d)` be a Type I solution for the prime p and `m = ab`. Then `B_{d,m} ≅ B_{p,∞}` and
`Λ_{d,m}` is an order of reduced discriminant `pe` in it, hence of index e in every maximal order containing
it. Consequently there is a supersingular `E/𝔽̄_p` with endomorphisms `u, v`, `u² = −d`, `v² = −ab`,
`uv + vu = 1`: **the CM points of discriminant −4d and −4ab (or of the orders they generate optimally
inside End E) have a common supersingular reduction mod p, with Gross–Zagier parameter x = 2**:
`(D₁D₂ − x²)/4 = (16abd − 4)/4 = pe`.
*Proof.* Ramification of `(−d, −dpe)`: at `ℓ ∤ 2dpe` none. At p: `(−d,−dpe)_p = (−d/p) = −1` (Prop 5.1 of
GEOMETRY_ES; `p ∤ d`). At odd `ℓ | e`: `ℓ ∤ d` and `−d ≡ (2a)^{−2}` is a square mod ℓ (Lemma 1.1), so the
symbol is `(−d/ℓ)^{v_ℓ(e)} = 1`. At odd `ℓ | d`: `(−d,−dpe)_ℓ = (−d,−1)_ℓ(−d,pe)_ℓ = ((−1/ℓ)(pe/ℓ))^{v_ℓ(d)}`
and `pe = 4abd − 1 ≡ −1 (ℓ)`, so 1. At ∞: −1. Product formula ⇒ unramified at 2. The rest is Lemma 1.2 and
Deuring's correspondence (maximal orders of `B_{p,∞}` = endomorphism rings of supersingular curves;
Deuring lifting of `(E, u)` and of `(E, v)`). ∎
Check (`scripts/quat_typeI.py 3000`, log `logs/quat_typeI_3000.txt`): all 19690 Type I solutions with `p < 3000` (unordered in a,b): the split
`(d | ab)` gives exactly `Ram = {p, ∞}` in every case; the other splits `(ad | b)`, `(bd | a)`, `(1 | abd)` fail
in 27–42% of cases (the Hilbert step at `ℓ | e` uses `−d ≡ □ mod e`, which is the level-d genus condition).

**Remark (where the ES content goes).** The hypothesis of Prop 1.3 that produces `B_{p,∞}` is only:
`4dm ≡ 1 (mod p)`, `(−d/p) = −1`, and `(−d/ℓ) = 1` for each ℓ dividing `e = (4dm−1)/p` to an odd power.
Everything else in ES — the condition `e | a + b` — is **not** part of the collision datum; see §2.

## 2. What the collision datum carries, and what it does not

### Proposition 2.1 (exact Type I dictionary; PROVED)
Type I(p) at level d holds iff there are `m, e ≥ 1` with
(i) `4dm − 1 = pe` — equivalently (Prop 1.3, Lemma 1.2) `Λ_{d,m}` is an order of reduced discriminant `pe` in
`B_{d,m}`, and `B_{d,m} ≅ B_{p,∞}` as soon as also (−d/p) = −1 and (−d/ℓ) = 1 for ℓ ∥^{odd} e; and
(ii) **m has a divisor a with `a + m/a ≡ 0 (mod e)`** (equivalently `a | m`, `a² ≡ −m (mod e)`).
Then `b = m/a`, `c = (a+b)/e`, and `gcd(c,p) = 1` is automatic (`p | c` would force `a + b ≥ pe = 4abd − 1`,
impossible for `a,b,d ≥ 1`). *Proof.* Lemma 1.1. ∎

**Isogeny reading of (ii) (PROVED).** If `E` is supersingular with `u, v ∈ End E` as in Prop 1.3 and `a | m`,
factor `v = ψ_b ∘ ψ_a` through `E' = E/H`, `H ⊂ ker v` of order a (exists in any group of order m). Put
`φ₁ = ψ̂_a, φ₂ = ψ_b ∈ Hom(E', E)`. Then `deg φ₁ = a`, `deg φ₂ = b`, `tr(φ₁φ̂₂) = tr(v̂) = 0` and
`deg(φ₁ + φ₂) = a + b`. The lattice `L = ℤφ₁ + ℤφ₂ + ℤuφ₁ + ℤuφ₂` has (degree-form) Gram
`[a,1,bd] ⊥ [b,−1,ad]` (binary forms of discriminant `−pe`), determinant `(pe/4)²`, hence index e in
`Hom(E',E)` (determinant `(p/4)²`). So **ES Type I ⟺ there are supersingular E, E', an endomorphism u of E with
u² = −d, and orthogonal `φ₁, φ₂ ∈ Hom(E',E)` with `tr(uφ₂φ̂₁) = 1`, such that
`[Hom(E',E) : L] = (4d·deg φ₁·deg φ₂ − 1)/p` divides `deg(φ₁ + φ₂)`.**

### Proposition 2.2 (the quaternionic side is congruence data; PROVED)
For fixed `(d, e)`, condition (i) and the `B_{p,∞}` conditions depend only on `p mod 4d` (namely
`p ≡ −e^{−1} (mod 4d)`), on `(−d/p)` and on `e`; and then `m = (pe+1)/4d` is *determined*. Hence for each
admissible `(d,e)` the existence of the CM collision of Prop 1.3 is automatic, and **all of the ES content is
(ii): a divisor of the single integer `m = (pe+1)/(4d) ≍ pe/d` in the square-root classes of `−m` mod e.**
Writing `X = a + b = ce`, `Y = b − a`, (ii) reads `X² − Y² = 4m`, `e | X`: a *split* (isotropic) binary problem,
exactly the shape of GEOMETRY_ES Prop 3.2. The Siegel-theta reading (count pairs `φ₁ ⟂ φ₂` in `Hom(E',E)`) does
not absorb (ii) either: `e | a + b` is a condition on the *Gram matrix* `(a, b, d)` being represented, not on the
representation, so it selects which coefficients to sum over — a p-dependent target set.
*Assessment.* So, for Type I, the dictionary exists but is a re-encoding: p becomes the level of `B_{p,∞}`, but the
condition that carries the difficulty is a divisor-in-residue-class statement about `m ≍ pe/d`, i.e. the same
shrinking-target structure as GEOMETRY_ES Prop 4.1 (modulus `e` is a coordinate of the point).

## 3. Type II is genuinely non-commutative (PROVED identity; analysis in progress)

### Lemma 3.1 (Type II factorisation in (−d, −p))
Let `B = (−d, −p)_ℚ`, `i² = −d`, `j² = −p`, `ij = −ji`, `k = ij` (`k² = −dp`). Then Type II(p) at level d
(ET: `4abd − p = e`, `a + b = ce`, `ef − 4a²d = p`, `f = 4acd − 1`) holds iff for some `a, b, c, e ≥ 1`
`(2a·i + j)(2b·i − j) = −e(1 + 2c·k)`.
*Proof.* `(2ai+j)(2bi−j) = −4abd − 2a·k − 2b·k + p = −(4abd − p) − 2(a+b)k`; compare coefficients. ∎
Norms: `N(2ai + j) = 4a²d + p = ef`, `N(2bi − j) = ef'`, `N(1 + 2ck) = 1 + 4c²dp = ff'` (O128's level-dp shell).
Compare Type I (Lemma 1.1): `(1 + 2ai)(1 + 2bi) = e(2ci + j²)` — commutative, inside `ℚ(i)`. ET's dilation swaps
`1 ↔ j`. In Type II the product of two elements of the order `ℤ⟨i,j⟩` (reduced disc 4dp) lands in `e·ℤ[k]`:
a statement about left/right ideals of norm e in a quaternion order of level `4dp` (to be developed: §3.2 ff.).

### Proposition 3.2 (Type II residual condition is split — the Type II analogue of Prop 2.2; PROVED)
Type II(p) at level d holds iff there is `e ≥ 1` with `4d | p + e` such that `m = (p+e)/(4d)` has a divisor a with
`a + m/a ≡ 0 (mod e)`. (Then `b = m/a`, `c = (a+b)/e`; `gcd(abd, p) = 1` is automatic, since `p | e` would give
`4abd = p + e ≤ 2(a+b)`, forcing `p = 2`.) *Proof.* ET (2.18)–(2.19): `4abd = p + e`, `a + b = ce`. ∎
Again `X = a+b`, `Y = b−a`: `X² − Y² = 4m`, `e | X` — an isotropic (split) binary problem. Lemma 3.1 does not change
this: the ES elements `2ai + j` run over the *line* `{2xi + j}` of `ℤ⟨i,j⟩`, on which `N = 4dx² + p` is a
one-variable polynomial; the conditions `e | N(2ai+j)`, `e | N(2bi−j)`, `e | a+b` are divisor conditions on values
of `4dx² + p` (Hooley-type), not representation numbers of a definite form.

**Ideal reading of Lemma 3.1 (PROVED, local).** `R = ℤ⟨i,j⟩` has reduced discriminant `4dp`, so `R_ℓ ≅ M₂(ℤ_ℓ)`
for `ℓ ∤ 2dp`. `α = 2ai + j` and `β = 2bi − j` are primitive (j-coefficient ±1). For `ℓ^k ∥ e`, `ℓ ∤ 2dp`, the
reductions `ᾱ, β̄ ∈ M₂(ℤ/ℓ^k)` have rank one, and `αβ ∈ ℓ^k R_ℓ ⟺ im β̄ = ker ᾱ` in `ℙ¹(ℤ/ℓ^k)`. So Type II is:
two elements of the line `{2xi ± j}` whose level-e structures (cyclic e-isogenies, Brandt/Hecke `T_e`
adjacency) are composable, with `αβ/e = −(1 + 2ck) ∈ ℤ[√−dp]`. The matching is a congruence modulo e, and
`e = 4abd − p` is a coordinate of the solution: again a shrinking target.

### 3.3 Supersingular reading of Type II (Assessment; standard facts cited, not re-proved)
The Type II form `[f, 4ad, de]` has discriminant `−4dp`. CM points of discriminant `−4dp` (p ramified) reduce mod p
to supersingular curves E on which `√−dp` factors through Frobenius, i.e. E admits an isogeny of degree d to
`E^{(p)}` (for d = 1: `j(E) ∈ 𝔽_p`; cf. Delfs–Galbraith). The reduction map sees the *class* of the form (the CM
point), while the ES side condition `A ≡ −1 (mod B)` is a condition on the *representative*. Each class contains
infinitely many representatives of the shape `[A, 4da, dE]` (orbit of a congruence subgroup containing
`[[1,0],[2,1]]` and `[[1,2d],[0,1]]`), of which finitely many are ES-good (GEOMETRY_ES Prop 4.1). So ES-goodness is
not a function of the CM point, still less of its reduction mod p. The same holds for Type I and its disc `−4d` points.

### 3.4 Fixed-(d,e) test (EVIDENCE; `scripts/quat_residual.py 1500`)
* (A) Lemma 3.1 holds, by explicit quaternion multiplication, on all 3303 ordered Type II solutions with p < 1500.
* (B) Take `p ≡ 1 (24)`, `p < 1500`, `d ≤ 12`, `e < 60`, with all the collision/genus data in place. For Type I that
  means `4d | pe+1`, `(−d/p) = −1` and `4r²d ≡ −1 (e)` solvable. For Type II it means `4d | p+e` and
  `4r²d ≡ −p (e)` solvable. Under these conditions the divisor condition holds in only **40/93 (Type I)** and
  **120/450 (Type II)** cases.
* There are explicit pairs with the same `(d,e)` and opposite ES status:
  * Type I: `(d,e) = (5,23)`, p = 313 (ES) vs 73 (no ES); `(10,7)`, 457 vs 97.
  * Type II: `(1,7)`, 73 vs 97; `(1,11)`, 73 vs 193.

## 4. Checks: ET Prop 1.6 (odd squares) and square-mimicking primes (PROVED)
* *n = p².* Run the dictionaries with n in place of p.
  * Type I: `Λ_{d,m}` lies in `(−d, −dne)`, and its symbol at p is `(−d/p)^{v_p(n)} = 1`. The collision is no longer
    supersingular-at-p. Consistently, Type I(n) needs `(−4d/n) = −1` (proof of GEOMETRY Prop 5.1 verbatim with n),
    and that is impossible for a square: f_I(p²) = 0.
  * Type II: the proof of Prop 5.2 gives `(n/f) = (−d/f) = −1`, impossible for `n = p²`: f_II(p²) = 0.
  * So both dictionaries fail at odd squares, as they must. They do so through the genus characters, i.e. through
    congruence data (inside Theorem C's scope). Nothing in §§1–3 escapes POINTWISE_SIZE Thm M/C. The quaternionic
    side of Props 1.3/2.2/3.2 is determined by `p mod 4d`, Legendre symbols and e. The non-congruence part (the
    divisor condition) is the classical one.
* *Square-mimicking p* (`(q/p) = 1` for all small primes q, `p ≡ 1 (24)`):
  * Type I collisions need `(−d/p) = −1`, hence `d ≥ d*(p)`.
  * Type II at a small level d lives in `(−d,−p)`, which splits at p; there is no constraint from the algebra.
  * By Lemma CT, some prime factor ℓ of f has `(ℓ/p) = −1`, so ℓ is large.
  * This adds nothing new and contradicts nothing.

## 5. Summing over the Gross–Zagier parameter (question (3))
For `D₁ = −4d`, `D₂ = −4m` the Gross–Zagier / Lauter–Viray count of supersingular collisions mod p is
`Σ_{x² < D₁D₂, x ≡ D₁D₂ (2)} Σ_{n | (D₁D₂−x²)/4, ...}` (ε-weighted local factors; cited, not re-derived). Summed over
all x and averaged over d, m, this is a class-number-product quantity: an intersection number of CM cycles, a
coefficient of an Eisenstein series via Siegel–Weil / Gross–Kohnen–Zagier. Type I forces **x = 2**.
**Proposition 5.1 (the x = 2 term does not see ES; PROVED modulo the cited shape of the GZ local factor).** The x = 2
term depends only on `n = pe` and on the genus characters `ε` of `(D₁, D₂)` at the primes of n. Those are
`(−d/ℓ)` for `ℓ | pe`. ES at `(d,e)` is not a function of these data: in the pairs of §3.4 (e.g. `(d,e) = (5,23)`,
p = 313 vs 73) e is the same, the characters `(−5/23)` and `(−5/p) = −1` are the same, and ES differs.
Summing over `(d,e)` therefore gives `Σ_{d,e: 4d | pe+1} F_ε(e)`, a congruence-weighted divisor sum in e, not a
class-number product. The class-number size of the full GZ quantity comes from the ≍ `√(dm)` values of x. The
restriction to the single value x = 2 removes it, and the ES weight (a divisor of `m = (pe+1)/4d` in the classes
`±√(−m)` mod e) is an extra condition on top. *Assessment:* no GZ/GKZ coefficient reproduces `f_I(p)`; the x = 2
restriction is exactly what kills the class-number structure.

## 6. Verdict on the route (Assessment, with the PROVED content listed)
* PROVED dictionaries: Type I ↔ an x = 2 GZ collision of CM points of discriminant −4d and −4ab in `B_{p,∞}`, plus a
  divisor condition (Props 1.3, 2.1, 2.2). Type II ↔ a non-commutative factorisation in `(−d,−p)` with matched level-e
  structures, plus the same divisor condition (Lemma 3.1, Prop 3.2).
* In both, the quaternionic / supersingular / level-p object carries only congruence and genus data (Prop 2.2, §3.2,
  §4). The ES content is the split divisor problem "m has a divisor in the square-root classes of −m mod e", where e
  is a coordinate of the solution. No definite form appears whose representation numbers or theta coefficients
  decide ES. So the level-aspect tools (Michel's equidistribution of supersingular reductions, EMV, Kane,
  Liu–Masri–Young) have nothing to act on here. They would give equidistribution of the collision data, which is
  automatic (congruence) in these dictionaries.
* *Scope of the negative statement:* it concerns these dictionaries, i.e. encodings in which p enters only as the
  ramified prime / Frobenius and the ES witness is a pair of CM endomorphisms with fixed relative trace. A hypothetical
  encoding in which the divisor condition itself became a definite representation problem is not excluded. Prop 3.2's
  isotropic `X² − Y² = 4m` shows it cannot come from any quadratic map of the ES parameters `(a, b)` alone.
