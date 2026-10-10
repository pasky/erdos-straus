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
Check (`scripts/quat_typeI.py 1000`): all 5071 Type I solutions with `p < 1000` (unordered in a,b): the split
`(d | ab)` gives exactly `Ram = {p, ∞}` in every case; the other splits `(ad | b)`, `(bd | a)`, `(1 | abd)` fail
in 24–39% of cases (the Hilbert step at `ℓ | e` uses `−d ≡ □ mod e`, which is the level-d genus condition).

**Remark (where the ES content goes).** The hypothesis of Prop 1.3 that produces `B_{p,∞}` is only:
`4dm ≡ 1 (mod p)`, `(−d/p) = −1`, and `(−d/ℓ) = 1` for each ℓ dividing `e = (4dm−1)/p` to an odd power.
Everything else in ES — the condition `e | a + b` — is **not** part of the collision datum; see §2.
