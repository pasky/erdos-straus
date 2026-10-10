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
