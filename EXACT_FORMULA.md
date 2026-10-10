# EXACT_FORMULA — is some weighted ES count a class-number / theta-coefficient identity? (task O131)

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010. Branches merged for reading:
side-agent/spectral-flip (O123), side-agent/typeii-spectral (O128), side-agent/geometry-es (O126).

Notation (all n ≥ 1, not only primes). "Algebraic" counts, no coprimality filters unless stated:
* Type I:  `T1(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = n(a+b) + c, a ≤ b}` (ET (2.8)-(2.9) shape);
  equivalently, for each (c,d): `(4cd·a − n)(4cd·b − n) = n² + 4c²d`.
* Type II: `T2(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc, a ≤ b}`;
  equivalently `(4cd·a − 1)(4cd·b − 1) = 4c²d·n + 1`.
* f_I, f_II (ET): T1, T2 with gcd(a,b,c) = 1 (and for Type II gcd(abd, n) = 1).

## 0. Summary (verdict: negative, with exact scope)

* **Engine (§1).** Exact dumps of all solutions, n ≤ 2·10⁴, of four families T1± (Type I and its sign flip), T2±
  (Type II and its sign flip). They are validated against O123's counts and an independent brute force. Lemma 1.1
  completes O123's Type I enumeration for composite n (PROVED).
* **Exact identities that do exist (PROVED; all elementary):**
  (a) Type II slices with cd | 6 (where (ℤ/4cd)^× has exponent 2) are exact combinations of weight-1 binary theta
  coefficients `Σ_χ χ(−1)σ_χ(4c²dn+1)`, χ quadratic (§3.2);
  (b) every (c,d) slice is an exact finite Eisenstein combination (§3.1, = O128 Prop 9.1);
  (c) the signed decomposition: `2(T2⁻ ∓ T2⁺) − diag = Σ_{c,d}[(2/φ(4cd))·(odd resp. even Eisenstein part) − 2]`,
  where the `−2` per level is a Kronecker–Hurwitz-type boundary term (§4.1; checked n ≤ 40);
  (d) T2⁺(m²) = 0 for all m, no gcd hypotheses (§2.1); T1±(2^k) = 0 (§4.2).
  **None has a structurally positive part.** In (a)–(c) positivity is "some 4c²dn + 1 has a divisor in a given
  class", which is the original problem.
* **No identity with classical functions (§2; EVIDENCE, exact computation).** There is no exact Hecke relation (§2.2).
  The rank test of 56 ES variants against 54 classical columns (Hurwitz class numbers, class-number convolutions
  Σ_x H(mn − x²) with twists, divisor and character sums) on six row sets gives intersection dimension 0 (§2.3).
  The best fit leaves ≈ 50–70 % of the fluctuation (§4.3).
* **Siegel–Weil route (§3).** The ES orbit is not its genus. The genus average matches the slice only when
  genus = class (cd | 6); otherwise corr ≈ 0.5–0.75. The genus masses summed over c diverge (≍ log²C) while the
  ES count is finite. Hence no "Eisenstein main term + small cusp error" formula exists for the total count.

## 1. Exact engine (step 1)

* `scripts/exf_engine.c` (from O123's `spec_typecount.c`): dumps every tuple (n,a,b,c,d), n ≤ N, a ≤ b, no gcd
  filter, for sign S = +1 (ES Type I/II) and S = −1 (the signed partner families below). Loader
  `scripts/exf_load.py`.
* **Lemma 1.1 (completion for composite n; PROVED).** The O123 Type I enumeration (f | 4a²d + 1) is complete only for
  primes. In general `f := 4acd − n` divides `c(4a²d + S)` (since `c(4a²d+S) ≡ a(n+f) + Sc ≡ an + Sc ≡ 0 mod f`),
  so with `h = gcd(f, 4a²d+S)`, `k = f/h` we get `k | c` and `n = k(4a(c/k)d − h)`: every solution of n is
  `(k m, a, b, k c', d)` for an enumerated solution `(m, a, b, c', d)` with `h | 4a²d + S`, and conversely every such
  scaling is a solution (b is unchanged). `expand_T1` scales and deduplicates.
* Validation: `scripts/exf_validate.py` — f_I, f_II (gcd-filtered) identical to `spec_typecount` for all n ≤ 2·10⁴;
  `scripts/exf_validate_signed.py` — all four families equal an independent brute force for every n ≤ 120.

Families (a ≤ b, all variables ≥ 1, no gcd conditions):

| name | equation | parametrisation |
|---|---|---|
| T1⁺ = T1 | `4abcd = n(a+b) + c` | `n = 4acd − f`, `f | c(4a²d+1)`, `b = (na+c)/f` |
| T1⁻ | `4abcd + c = n(a+b)` | `n = 4acd − f`, `f | c(4a²d−1)`, `b = (na−c)/f` |
| T2⁺ = T2 | `4abcd = a + b + nc` | `n = 4abd − e`, `e | a+b` |
| T2⁻ | `4abcd + a + b = nc` | `n = 4abd + e`, `e | a+b` |

**Lemma 1.2 (signed Type II = T2⁺ + T2⁻ + trivial; PROVED).** For q = 4cd the Type II equation is
`(qa−1)(qb−1) = qcn + 1`. Allowing a, b ∈ ℤ: mixed signs are impossible (the product is positive), a = 0 gives the
trivial family b = −cn (all c, d), and a, b ≤ −1 gives, with a' = −a, b' = −b, exactly T2⁻. So
`#{X | qcn+1 : X ≡ ±1 (mod q)} − 2` summed over (c,d) is `2T2⁺ + 2T2⁻` minus diagonal corrections.
For Type I the same manoeuvre gives nothing new: `(qa−n)(qb−n) = n² + qc` with a, b ≤ 0 forces
`4|a||b|cd + n(|a|+|b|) = c`, impossible unless a = 0 (trivial family c = n|b|). T1⁻ is instead the ES equation
with one sign flipped (`4/n = 1/x + 1/y − 1/z` shape).

## 2. First structural facts and the linear-relation search (steps 1–2)

Data: `scripts/exf_arrays.py` → `data/exf/arrays_2e4.npz` (n ≤ 2·10⁴).

**Prop 2.1 (T2⁺ vanishes at every square; PROVED).** `T2⁺(m²) = 0` for every m ≥ 1 (odd *and even*; no
coprimality hypotheses). *Proof.* A solution gives `XY = 4c²d m² + 1` with `X = 4cda − 1 ≡ −1 (mod 4d)`, X > 0.
Then `−d(2cm)² ≡ 1 (mod X)` and `gcd(X, 2cm) = 1`, so the Jacobi symbol `(−d/X) = 1`; but `(−4d/·)` is a
character mod 4d with `(−4d/X) = (−4d/−1) = −1` (odd character of a negative discriminant) and `(−4d/X) = (−d/X)`
for odd X > 0. Contradiction. ∎ (This is ET Prop 1.6 / O128 Lemma 6.1 without the gcd hypotheses.)
Numerically (n ≤ 2·10⁴) T2⁺ has 144 zeros: the 141 squares and 3 non-squares (288, 336, …; EVIDENCE).

Other zero sets (EVIDENCE, n ≤ 2·10⁴): `T1⁺(n) = 0` and `T1⁻(n) = 0` **iff n is a power of 2**; T2⁻ has the 12
zeros {1,2,3,4,7,8,12,15,24,44,108,168}. T1⁺ does *not* vanish at odd squares (imprimitive solutions,
gcd(m, cd) > 1; e.g. T1⁺(9) = 2, T1⁺(p²) = T1⁺(p) for small primes p), and T1⁻, T2⁻ are large at squares — so
only Type II⁺ carries the square obstruction unconditionally.

Sizes (EVIDENCE): all four counts are polylogarithmic on average, mean ≈ κ·log³n with κ ≈ 0.17–0.18 (T1⁺),
0.22–0.23 (T1⁻), 0.040–0.044 (T2⁺, T2⁻). **No √n main term**, so any identity with class numbers H(·) ≍ √n
must involve exact cancellation of the √n parts (as in Kronecker–Hurwitz, where the boundary term
`λ(n) = Σ_{d|n} min(d, n/d)` is a difference of two ≍ n quantities).

**2.2 Hecke test (`scripts/exf_hecke.py`; negative).** If a count were a coefficient of a Hecke eigenform (or a
fixed combination of a few), `F(nℓ²)` would be an exact combination of `F(n), F(n/ℓ²), (±n/ℓ)F(n), F(nℓ),
F(n/ℓ), 1`. Least squares over n ≤ 2·10⁴/ℓ², ℓ = 3, 5, 7: relative residual 0.14–0.24 (T1±) and 0.41–0.51 (T2±).
No Hecke structure.

**2.3 Exact relation search (`scripts/exf_columns.py`, `scripts/exf_nullspace.py`; negative).** 56 ES-variant
columns (for each of T1±, T2±: total, diagonal a = b, a = 1 slice, primitive gcd(a,b,c) = 1, d = 1,2,3 slices,
c = 1,2,3 slices, signs (−1)^{a+b}, (−1)^c, (−1)^d, d a square) against 54 classical columns (1, n, [n square],
12H(kn) for k ∈ {1,3,4,8,12,16,20,24}; `Σ_x 12H(mn − x²)` for m ∈ {1,4,8,12,16,20} plain, (−1)^x- and
χ₋₄(x)-twisted and 3|x-restricted; τ, σ, λ, Σ_{d|n} χ_D(d) for D ∈ {−4,−3,8,−8,5,12,−7}; τ(n±1), τ(4n±1),
τ(2n+1), τ(8n+1), τ(n²+1), τ(n²+4)). Exact rank computation mod 2³¹−1 on 500 random rows of each row set:

| rows | rk C | rk E | rk(C∪E) | dim(span E ∩ span C) |
|---|---|---|---|---|
| all n ≥ 2 | 46/54 | 56/56 | 102 | 0 |
| odd n | 41 | 52 | 93 | 0 |
| primes ≥ 5 | 27 | 50 | 77 | 0 |
| primes ≡ 1 (4) | 23 | 47 | 70 | 0 |
| primes ≡ 3 (4) | 22 | 49 | 71 | 0 |
| primes ≡ 1 (24) | 18 | 45 | 63 | 0 |

So **no ES variant, and no linear combination of them, is a linear combination of the classical columns** on
any of these row sets (a single exact relation would make the intersection ≥ 1). Columns flagged as "in span C"
are identically zero there (e.g. the d = 1 slice of T1⁺ vanishes for p ≡ 1 (4): Lemma 2.4 of O123). The only
pure-ES relations on primes are elementary: `(−1)^c = (−1)^{a+b}` (reduce the equation mod 2), and
`T1⁺.diag(p) = T2⁺.diag(p) = #{a : 4a² | p + 1}` (both diagonals reduce to `p = 4a²d − 1`; similarly for T±⁻).

## 3. The Siegel–Weil route at fixed (c,d), computed in divisor language (step 3)

*Overlap note.* O128 round 2 (POINTWISE_TYPEII_SPECTRAL.md §§8–9, merged here afterwards) independently proves the
character expansion of 3.1 (its Prop 9.1, with the weight-1/weight-0 Eisenstein identification), the genus pairing at
squares (Prop 9.2) and that all local/genus/spinor data hold for every n (Prop 8.3: the obstruction is the sign at ∞,
ray class group mod 4cd·∞ of a split torus). 3.1 is kept as the computational dictionary; 3.2 (the exponent-2
levels where genus = class) and 3.3–3.4 (numerical genus-vs-orbit comparison, non-summability in c) are additions.

**3.1 Dictionary (PROVED, elementary).** Fix (c,d), q = 4cd, `M = 4c²dn + 1`. By O128 Prop 2.5 the Type II
solutions with this (c,d) are the forms Q = [A,B,C] in the level lattice `L_d = {4d | B, d | C}` with
disc −4dn, Q > 0, and `ℓ_c(Q) := A − cB = −1`, i.e. vectors Q with a prescribed Gram matrix T against the fixed
split vector `w_c ↔ ℓ_c` (w_c^⊥ is the cuspidal geodesic (∞, −1/(2c))). Since the Γ-stabiliser of w_c is finite,
this is, up to a bounded factor, the representation number of T by L_d **restricted to one SO(L_d)(ℤ)-orbit of
second vectors**. In divisor language (A = X = 4acd − 1) it is

  `A_{c,d}(n) := #{X | M : X ≡ −1 (mod q)} = 2·T2⁺_{c,d}(n) − [diagonal]`,

and the other second vectors y with q(y) = q(w_c) (other orbits in the genus) correspond to the other residue
classes r mod q. Character orthogonality gives the **exact** decomposition

  `A_{c,d}(n) = (1/φ(q)) Σ_{χ mod q} χ(−1) σ_χ(M)`,  `σ_χ(M) = Σ_{X|M} χ(X)`  (= coefficient of the weight-1
  Eisenstein series E₁(χ, 1) at M),

whose χ = 1 term `τ(M)/φ(q)` is the naive local-density mass. The **genus average** (Siegel–Weil / Eisenstein part:
mean over the classes of the coset `−1·(ℤ/q)^{×2}`, i.e. keep only the quadratic χ) is
`G_{c,d}(n) = #{X | M : X ∈ −(ℤ/q)^{×2}} / |(ℤ/q)^{×2}|`.

**3.2 Exact theta identities for cd | 6 (PROVED; checked).** If `(ℤ/q)^×` has exponent 2 — exactly q ∈ {4, 8, 12, 24},
i.e. cd ∈ {1, 2, 3, 6} — the coset is the single class −1, so `A_{c,d} = G_{c,d}` identically:

  `A_{c,d}(n) = 2^{−k} Σ_{χ quadratic mod q} χ(−1) σ_χ(4c²dn + 1)`,

a combination of coefficients of weight-1 theta series of binary quadratic forms (genus characters of
discriminants dividing 24), e.g. `A_{1,1}(n) = (τ(4n+1) − r₂(4n+1)/4)/2`. Checked on all primes p < 3000
(`scripts/exf_genus.py`: mean|A − G| = 0.000 for (c,d) = (1,1),(1,2),(1,3),(2,1),(3,1),(2,3)).
**These are genuine exact theta-coefficient identities for slices of f_II, but their positivity is not
structural:** `A_{1,1}(p) > 0` iff `4p + 1` has a prime factor ≡ 3 (mod 4), etc. Every slice with cd | 6 vanishes
exactly on a union of square classes (the Mordell/ET covering congruences), which is why all ES-hard primes are the
square classes mod 840.

**3.3 Other (c,d): the ES class is not its genus (EVIDENCE, primes 5 ≤ p < 3000).**

| (c,d) | q | mean A | mean G | corr(A,G) | mean abs(A−G) | P(A = 0) | P(A = 0 given G ≥ 1) |
|---|---|---|---|---|---|---|---|
| (1,5) | 20 | 0.327 | 0.371 | 0.72 | 0.26 | 0.84 | 0.45 |
| (1,7) | 28 | 0.229 | 0.551 | 0.50 | 0.49 | 0.89 | 0.54 |
| (5,2) | 40 | 0.201 | 0.196 | 0.74 | 0.16 | 0.90 | 0.44 |

The genus average predicts the slice only on average, and for (1,7) not even that (ratio 0.42). In about half the
cases where the genus mass is ≥ 1 the actual slice is empty.

**3.4 The genus mass is not summable over c, the ES count is (EVIDENCE + PROVED finiteness).** For fixed n,
`A_{c,d}(n) = 0` once c is large (c ≤ a + b, ET; finitely many solutions). The genus masses do not decay:

| p | Σ_{c≤C} A_{c,1}: C = 10, 100, 300, 1000, 2000 | Σ_{c≤C} G_{c,1} |
|---|---|---|
| 101 | 12, 12, 12, 12, 12 | 12.2, 21.1, 28.2, 38.2, 44.5 |
| 1009 | 4, 4, 4, 4, 4 | 2.5, 9.0, 13.3, 19.1, 22.2 |
| 2003 | 6, 8, 10, 12, 12 | 6.7, 12.8, 16.6, 21.8, 24.8 |

(growth consistent with Σ_c τ(M_c)/φ(4c) ≍ log²C). *Interpretation (Assessment).* The ES class r = −1 is the
"small residue" class: `X = qa − 1 | qcn + 1` forces `(4acd − 1) | cn + a`, a size condition that the other
classes of the genus do not satisfy. So the total ES count is **not** a genus average (Siegel–Weil main term)
plus a lower-order cuspidal error; the Eisenstein part summed over the ES range of (c,d) is infinite and must
cancel exactly against the character parts. This is the representation-theoretic form of the "Planck-scale
barrier": ES selects one orbit of second vectors, and orbit-level counts in a genus are governed by the
non-principal characters, which are as large as the main term.

## 4. Signed decomposition, boundary terms, residuals (steps 2 and 4)

**Prop 4.1 (Type II: positive = signed − boundary, exactly; PROVED).** For q = 4cd, N = 4c²dn + 1 let
`A_{±1}(c,d) = #{X | N : X ≡ ±1 (mod q)}`. Lemma 1.2 gives `A_{+1} = 2 + 2T2⁻_{c,d} − δ⁻_{c,d}`,
`A_{−1} = 2T2⁺_{c,d} − δ⁺_{c,d}` (δ = diagonal a = b), and orthogonality gives

  `2(T2⁻ − T2⁺)(n) − (δ⁻ − δ⁺)(n) = Σ_{c,d ≥ 1} [ (2/φ(4cd)) Σ_{η odd mod 4cd} σ_η(4c²dn + 1) − 2 ]`,
  `2(T2⁻ + T2⁺)(n) − (δ⁻ + δ⁺)(n) = Σ_{c,d ≥ 1} [ (2/φ(4cd)) Σ_{η even mod 4cd} σ_η(4c²dn + 1) − 2 ]`,

each sum having only finitely many non-zero terms. The constant `−2` per level is the trivial factorisation
N = 1·N (a = 0): it is the exact analogue of the boundary term `λ(n) = Σ min(d, n/d)` in Kronecker–Hurwitz, and it
is what makes the sums finite. Thus ES Type II = (even part − odd part)/2 of a family of weight-1/weight-0
Eisenstein coefficients, *minus* a boundary. Neither part is sign-definite. On primes 5 ≤ p ≤ 2·10⁴,
`T2⁻ − T2⁺` ranges over [−276, 288] (mean +22 for p ≡ 1 (4), −24 for p ≡ 3 (4); corr(T2⁻ − T2⁺, T2⁺) = −0.77):
the "signed total" T2⁺ + T2⁻ does not dominate T2⁺ in any structural way. For Type I the signed manoeuvre gives
nothing (Lemma 1.2); the sign-flipped family T1⁻ satisfies `T1⁻ − T1⁺ < 0` for 21 % of primes (2.8 % of p ≡ 1 (4)).

**Prop 4.2 (zero sets of T1±; PROVED).** `T1⁺(2^k) = T1⁻(2^k) = 0` for all k. *Proof.* By Lemma 1.1 every
solution of n is a k-scaling of a solution of an odd m = 4ac'd − h with h | 4a²d ± 1 (h odd), m | n. m = 1 is
impossible: for S = +1, h = 4ac'd − 1 would divide a + c' < h; for S = −1 it forces a = c', b = 0. ∎ Conversely
`T1⁺(n) ≥ T1⁺(m)` for every odd m | n (scaling), so "T1⁺(n) > 0 unless n = 2^k" (EVIDENCE, n ≤ 2·10⁴) is just
Type I solvability of the odd primes ≤ 2·10⁴.

**4.3 Residuals of the best classical fit (`scripts/exf_residual.py`; EVIDENCE).** Least squares of each family
on the 54 classical columns of §2.3, trained on primes < 10⁴, tested on primes in [10⁴, 2·10⁴]: relative
residual (‖r‖/‖y − ȳ‖) on the test set 0.57 (T1⁺), 0.72 (T1⁻), 0.60 (T2⁺), 0.63 (T2⁻), 0.46 (f_I = T1⁺.prim),
0.50 (f_II-type T2⁺.prim); test rms 61, 49, 21, 21, 31, 11 against means 139, 186, 49, 48, 102, 38. The
dictionary (mostly τ(p ± 1), τ(4p ± 1), τ(8p + 1)-type columns) captures about half of the fluctuation, as the
Eisenstein picture (Prop 4.1) predicts (the low levels contribute σ_η at 4p+1, 8p+1, 12p+1, …), and nothing more.

## 5. Round 2: the Type I CM torus (anisotropic) — it collapses too

Setting: p prime, p ∤ 2cd, `K = ℚ(√−d)`, `α = α_{c,d}(p) = p + 2c√−d ∈ ℤ[√−d]`, `N(α) = p² + 4c²d`, q = 4cd.
Type I solutions with this (c,d) (ordered, i.e. both a ≶ b) are the divisors `f | N(α)` with `f ≡ −p (mod q)`
(O123 Lemma 2.1(iii)); only p inert in K contribute (O123 Lemma 2.4 / GEOMETRY_ES Prop 5.1).

**Lemma 5.1 (ideal divisors of α = integer divisors of N(α); PROVED).** α is primitive (no rational integer
m > 1 divides it, as gcd(p, 2c) = 1) and every prime ℓ | N(α) is odd, prime to d (ℓ | d ⇒ ℓ | p), hence prime to
the conductor of ℤ[√−d] and unramified in K; since α is primitive, ℓ is not inert (ℓ | α would follow), so ℓ splits,
ℓ = 𝔩𝔩̄, and α is divisible by exactly one of 𝔩, 𝔩̄, to the full power `v_ℓ(N(α))`. Hence
`𝔞 ↦ N𝔞` is a bijection `{ideals 𝔞 | (α)} → {f ∈ ℕ : f | N(α)}` (inverse `f ↦ (f, α)`). ∎
Checked with PARI (`scripts/exf_cm_check.py`, maximal orders, idealfactor): 9908 triples (p < 400 inert,
c ≤ 7, d < 60 squarefree), #ideal divisors = τ(N(α)) and one prime ideal per rational prime, 0 failures.

**Theorem 5.2 (Type I fixed (c,d) is a ray-class divisor count of one element, seen only through norms; PROVED).**
(i) `T1_{c,d}(p) = #{𝔞 | (α) : N𝔞 ≡ −p (mod 4cd)}`, and the condition depends only on the ray class of 𝔞 in
`Cl_{4cd}(K)` through the norm map `Cl_{4cd}(K) → (ℤ/4cd)^×`.
(ii) Expanding in Hecke characters ψ of `Cl_{4cd}(K)`, only the characters trivial on ker(Norm) occur, i.e.
`ψ = χ∘N` with χ a Dirichlet character mod 4cd:
  `T1_{c,d}(p) = (1/φ(4cd)) Σ_{χ mod 4cd} χ̄(−p) Σ_{𝔞|α} χ(N𝔞) = (1/φ(4cd)) Σ_χ χ̄(−p) σ_χ(p² + 4c²d)`.
(iii) The class-group characters of K that occur are exactly those of the form χ∘N, i.e. the **genus characters**;
every non-genus class-group character (and every Hecke character not factoring through the norm) has coefficient 0.
Pairing χ ↔ χχ_{−4d} (χ_{−4d}(N𝔞) = 1) gives
  `T1_{c,d}(p) = ((1 + χ_{−4d}(−p))/φ(4cd)) Σ_{χ mod 4cd / ⟨χ_{−4d}⟩} χ̄(−p) σ_χ(p² + 4c²d)`,
the genus factor of O123 Lemma 2.4 as an exact identity.
*Proof.* (i) Lemma 5.1. If 𝔞 ≡ 𝔞' in `Cl_{4cd}` then `𝔞 = 𝔞'(β)`, β ≡ 1 mod 4cd, so `N𝔞 ≡ N𝔞'`. (ii) orthogonality
on the finite group `(ℤ/4cd)^×` after composing with N; then Lemma 5.1 turns `Σ_{𝔞|α} χ(N𝔞)` into `σ_χ(N(α))`.
(iii) A character of Cl(K) is of the form χ∘N iff it is a genus character (genus theory). ∎

**Answer to the round-2 question.** The CM torus does **not** bring class-group structure into the count: the ES
condition sees an ideal divisor 𝔞 of α only through `N𝔞 mod 4cd`. That loses exactly the information of the
class of 𝔞 beyond its genus. The count is the *same* object as in the split (Type II) case: a divisor count of the
single integer `p² + 4c²d` in a residue class mod 4cd, expanded in Dirichlet characters (σ_χ = weight-1
Eisenstein coefficients). The only difference from Type II is the genus factor `1 + χ_{−4d}(−p)` (inert condition).
It is not "a class-group-theoretic quantity for fixed p": non-genus Hecke-L data enter with coefficient 0. For a
fixed p there is no Frobenius of p in the Hilbert class field to correlate with either, since p is inert, so pO_K is
principal and splits completely in H/K.

**5.3 Where the class group does show up: only in the mean (EVIDENCE; `scripts/exf_cm_classes.py`,
`scripts/exf_cm_bias.py`, outputs `data/exf/cm_*_out.txt`).** For fixed (p,d) all Type I ideals lie in **one genus**
(N𝔞 ≡ −p fixes every genus character). Within it, the classes of the Heegner forms [f, 4ad, de] (= class of 𝔞,
up to the principal ramified ideal (√−d)) are **not** uniform. Primes ≤ 2·10⁴:
* the principal class carries 0.23–0.37 of the solutions for d = 14, 26, 29, 41, against 1/h = 0.25, 0.17, 0.17,
  0.125 (it is ≈ 2× any other class of its genus; e.g. d = 26: 594 vs 340, 320);
* the bias persists for f > 100 and does not decay over p ∈ [5, 2·10⁴]. It comes from the complementary norm
  e = (4a²d+1)/f being small (the class of 𝔞 is that of an ideal of norm e). This is a small-norm
  (Kronecker-limit / L(1,ψ)) bias of the *averaged* Heegner count, the class-dependent constant in the TTL main term;
* no class is always hit (P(class hit) 0.24–0.85). Per-p dispersion across the classes of a genus is 2.6–11× the
  multinomial value, from the clumping of solutions with small e.
So class-group/Hecke-L data enter only as lower-order constants in averages over p, never as a pointwise identity.

**5.4 Weight 3/2 / Brandt (not done beyond round 1; Assessment).** Round 1 already tested the weight-3/2 Eisenstein
(Zagier/Cohen) coefficients H(kn) and their convolutions Σ_x H(mn − x²): rank intersection 0. Brandt-matrix
theta series at level n were not computed. By Thm 5.2 and O128 Prop 9.1, both Type I and Type II fixed-(c,d) counts
are exactly Dirichlet-twisted divisor counts of the integers p² + 4c²d and 4c²dp + 1, with no definite-quaternion
or class-group input. A Gross-type formula (which counts ideal classes of a definite order) would have to reproduce
these divisor counts summed over ≍ p log p levels. I see no mechanism for that, and the √p size of Brandt/class-number
coefficients against the log³p size of the count would require exact cancellation.

**Net (round 2).** Both tori collapse to the same thing: Type II has a split torus (O128) and Type I an anisotropic CM
torus (Thm 5.2), but in both cases the ES condition is on norms mod 4cd only. ES at fixed (c,d) is a ray-class
divisor condition on a single integer, with genus theory as the only class-group content. No class-number
positivity is available on this route. Negative; ES not proved.
