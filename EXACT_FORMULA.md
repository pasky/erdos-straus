# EXACT_FORMULA — is some weighted ES count a class-number / theta-coefficient identity? (task O131)

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010. Branches merged for reading:
side-agent/spectral-flip (O123), side-agent/typeii-spectral (O128), side-agent/geometry-es (O126).

Notation (all n ≥ 1, not only primes). "Algebraic" counts, no coprimality filters unless stated:
* Type I:  `T1(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = n(a+b) + c, a ≤ b}` (ET (2.8)-(2.9) shape);
  equivalently, for each (c,d): `(4cd·a − n)(4cd·b − n) = n² + 4c²d`.
* Type II: `T2(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc, a ≤ b}`;
  equivalently `(4cd·a − 1)(4cd·b − 1) = 4c²d·n + 1`.
* f_I, f_II (ET): T1, T2 with gcd(a,b,c) = 1 (and for Type II gcd(abd, n) = 1).

(work log follows; sections are added as steps complete)

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
