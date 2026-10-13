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
* Full range N ≤ 30000: from-scratch census running (`logs/review_tf_census30000.txt`); result recorded in §2b below.

## 3. Thm 3.1 (no BM obstruction from Br U at the 16 failures) — SOUND (all 16 certificates re-verified)

BL inputs over k = ℚ(ω), checked against the paper. BL §2 is explicitly "over a field k of characteristic 0", n ∈ k^*.
(i) The K-linear change u_i = x_i/c_i turns TES into 9/n = Σ 1/u_i, i.e. BL's U_{n'} after u_i = (9/4)u'_i, n' = 16n/81 ✓
(ratios, hence α_ζ, are scaling-invariant). (ii) Prop 2.5/2.6: Br Ũ/Br k ≅ (ℚ/ℤ(−1))^{G_k} ≅ μ(k), representatives
α_ζ = (−u₁/u₃, −u₂/u₃)_ζ, ζ ∈ μ(k); for k = ℚ(ω), μ(k) = μ₆ ✓. α_ω ≠ 0 has order 3, α_{−1} ≠ 0 order 2, so they generate
ℤ/6 ✓ (the bijection ζ ↦ α_ζ is not claimed to be a homomorphism, and isn't needed). Lemma 2.4 (Br₁Ũ = Br k) uses only
Pic Ũ_k̄ = ℤ·L₁₂ with trivial action ✓ over any k. (iii) Cor 2.9 (Br U → Br Ũ iso): surjectivity Thm 1.7; injectivity
from (2.8) with Pic Ũ → Pic E onto — E is the exceptional conic of the A₁ point, its tangent cone u₁u₂+u₁u₃+u₂u₃ = 0
has the k-point (1:0:0), so E ≅ ℙ¹_k and L₁₂ (defined over k) meets it with intersection 1 ✓ — valid over K. So
Br U/Br K ≅ ℤ/6 = ⟨α_ω, α_{−1}⟩ ✓, and orthogonality to Br U ⟺ Σ inv α_ω = Σ inv α_{−1} = 0 ✓ (Br K pairs to 0;
Br ℂ = 0 at the complex place).

Certificate logic ✓: Q_v = P₀ (v ≠ 𝔮), Q_𝔮 = P₁ is in W (P₀ ∈ W_v for v ∉ T(P₀) = {𝔮}; P₁ ∈ 𝒰(O_𝔮) ∩ U°), and
Σ_v inv_v β(Q) = Σ_v inv_v β(P₀) + [inv_𝔮 β(P₁) − inv_𝔮 β(P₀)] = 0. Only the TAME place 𝔮 (∤ 6n) enters, so the
wild invariants (computed by the author via reciprocity) are not needed for the certificate; and only equality of
symbol values at 𝔮 is needed, so sign/inverse conventions are irrelevant.

From-scratch check `scripts/review_tf_bm.py` (own valuations, residue fields, tame symbol, cubic and quadratic
residue symbols; u = (x/ω, y/ω², z/2)): for each certificate it recomputes z₀ from (x₀, y₀), checks both points on U,
recomputes T(P₀) by factoring the denominator of z₀ and testing x₀, y₀, z₀ ≡ 1 at (2) — T(P₀) = {𝔮} exactly — checks
P₁ 𝔮-integral, and compares the symbols. Hand-entered: N = 7, 103, 151, 211, 26893 (data from the document /
author's run); the other 11 parsed (data only) from the author's `tf_bm.py` output (`logs/review_tf_author_certs.txt`).
**All 16 pass**; in every case (inv_𝔮 α_ω, inv_𝔮 α_{−1}) = (0, 0) for both P₀ and P₁. N = 103: P₀ = (−7−14ω, 5+4ω,
(630−672ω)/(326−428ω)), T = {(49−33ω)}, N𝔮 = 5107; P₁'s only bad norm 7687 ✓ (as stated).
Symbol code is not trivially-zero: `scripts/review_tf_symcheck.py` on complete TES sets at π (N = 307, 439, 601, 1009)
gives the cubic exponent of α_ω at π constant = 2 ≠ 0 (order-3 T1 law of TWISTED_T1 Thm 3.2(a)), and the quadratic
symbol at N = 439 split 27/27 ✓ (matches the author's convention check).

Remaining caveats are correctly stated by the author (Br U° classes ramified along L_ij not considered; étale-BM /
descent not excluded). See D3 for the wording of the theorem statement.
