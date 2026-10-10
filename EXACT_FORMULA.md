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
