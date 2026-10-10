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
