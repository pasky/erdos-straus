# R194 — hostile review of TES_FINITE.md (O194)

Reviewer: side agent R194 (branch side-agent/review-tes-finite; author branch side-agent/tes-finite merged).
From-scratch scripts: `scripts/review_tf_*.py` (own ℤ[ω] arithmetic, own solvers, own Hilbert / cubic symbols;
no import of `tf_*`, `tw_*`). Source checked: Bright–Loughran arXiv 1908.02526 (sources/bright-loughran-1908.02526.pdf,
read in full for §2–§3).

## Summary verdicts
(filled in claim by claim below)

## 1. Prop 1.1 / Cor 1.2 (finiteness) — SOUND (minor attribution / wording defects)

Re-derived. (a) |t/n| ≤ Σ|c_i|/|x_i| ≤ 3 max_i |c_i|/|x_i| ⇒ some |x_i| ≤ 3|c_i||n|/|t|, i.e. N(x_i) ≤ 9N(c_i)N(n)/N(t).
For TES (t = 9, N(c) = (1, 1, 4)): N(x) ≤ N(n)/9, N(y) ≤ N(n)/9, N(z) ≤ 4N(n)/9. ✓
(b) r = t/n − c_i/x_i = (t x_i − c_i n)/(n x_i) = A/B; c_j/x_j + c_k/x_k = A/B ⇔ A x_j x_k − B c_k x_j − B c_j x_k = 0;
multiplying by A: (A x_j − B c_j)(A x_k − B c_k) = A²x_jx_k − AB(c_k x_j + c_j x_k) + B²c_jc_k = B²c_jc_k. ✓ Both factors
are non-zero (product ≠ 0), each divisor d determines x_j = (d + Bc_j)/A, x_k = (B²c_jc_k/d + Bc_k)/A. ✓
Two-term triangle bound: min(|x_j|/|c_j|, |x_k|/|c_k|) ≤ 2/|r|, i.e. N(x_j) ≤ 4N(c_j)N(B)/N(A) for the smaller one ✓
(this is what method B uses). r = 0 ⇔ x_i = c_i n/t; for TES, c_i n/9 ∈ O would need λ⁴ | c_i n, impossible as
gcd(n, 6) = 1 and c_i ∈ {ω, ω², 2}. ✓ Remark (3): if c_i n/t ∈ O then (c_i n/t, c_j m, −c_k m) is a solution for every
m ∈ O∖0 ✓, and the proof shows all but finitely many solutions then have a vanishing two-term subsum ✓.
No quantifier issue: the bound in (a) is uniform in the solution; the finite union over i covers every solution.
Count bound "Σ_i Σ_{x_i} 6·τ_O(...)" ✓ (6 units per ideal divisor).

Defects: see D1 (attribution: over ℤ this is BL Lemma 3.10 verbatim, incl. the "u_i = −u_j" exception).

## 2. Thm 2.1 (16 TES failures, N ≤ 30000) — SOUND (N ≤ 3000 and N = 26893 independently reproduced; full range: see below)

Completeness logic re-derived. (i) Every solution has some coordinate in the Prop 1.1(a) disk; it is 2-primary,
so enumerating only 2-primary x_i in the three disks is complete. (ii) Given x_i, (x_j, x_k) ↔ divisors d of
M = (n x_i)² c_j c_k, all 6 unit multiples of every ideal divisor; the 2-primary and integrality conditions are then
tested. (iii) Reduction to one 2-primary π per conjugate pair: Lemma 3.1 of TWISTED_T1 forces n ≡ 1 (mod 2), so
only ±π matter; x_i ↦ −x_i maps TES(π) to TES(−π) (−1 ≡ 1 mod 2) and (x, y, z) ↦ (ȳ, x̄, z̄) maps TES(π) to
TES(π̄) (ω̄ = ω²). ✓ Both symmetries also confirmed by brute force (all split π, N ≤ 400:
`review_tf_zomega.py conjcheck 400`).

From-scratch solver `scripts/review_tf_zomega.py` (own a + bω arithmetic, own Eisenstein factorisation via
norms, own divisor enumeration — same mathematics as the author's method A, independent code; every solution is
checked in the cleared equation 9xyz = n(ωyz + ω²xz + 2xy)):
* `census 3000` (21 s): zeros exactly at N ∈ {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769, 2029, 2239};
  N ≤ 1000: 85 primes, 507 solutions, mean 5.96, 13 zeros; (1000, 3000]: 130 primes, 1244 solutions, mean 9.57,
  2 zeros — identical to the author's numbers. All 1751 solutions have π dividing exactly 1 (1301) or 2 (450)
  coordinates (Type I / II shapes) ✓.
* `one 179 36` (N = 26893, 3 s): 0 solutions ✓. `one 11 2` (N = 103): 0 ✓. Disk count for N = 103, z-disk N ≤ 45.8:
  162 non-zero lattice points, 42 of them 2-primary ✓.
