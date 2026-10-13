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
