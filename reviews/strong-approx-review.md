# R167 — hostile review of O167 `STRONG_APPROX_ES.md` (§1–§11)

Reviewer: R167 (side-agent/review-strong-approx). Author branch merged: side-agent/strong-approx.
ES is not solved; nothing in the reviewed document claims otherwise, and nothing here changes that.
From-scratch scripts: `scripts/review_sa_*.py` (none reuse the author's code).

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| §1 literature | SOUND-AFTER-REPAIRS (D1 venue of BKS; D2 Sardari's primitivity hypothesis on the local ball omitted) |
| §3 matrix dictionary, Lemma 10.1 | SOUND (re-derived; symbolic + brute force, `scripts/review_sa_typeII.py`) |
| Lemma 2.2 (no plane) | SOUND |
| Thm 2.3 (rel. Pila Thm A) | SOUND |
| Cor 2.4 | SOUND-AFTER-REPAIRS (D4: `σ_p ≥ N^{−o(1)}` must be an explicit hypothesis; gap near exponent 4 correctly recorded) |
| Prop 3.1 | SOUND |
| Cor 3.2 | GAP (D5 box restriction; D6 recipe must factor through g; D7 definite Eichler orders) |
| Thm 4.1 | SOUND-AFTER-REPAIRS (D4: false as stated without a lower bound on σ_p; numerical counterexample) |
| Cor 4.2 | SOUND-AFTER-REPAIRS (D8: label/contrapositive overclaimed) |
| Prop 5.1 | SOUND-AFTER-REPAIRS (D3: "finitely many n with large v_ℓ(N_n)" is false; D10 Type I/II output) |
| §5 EVIDENCE | SOUND (reproduced independently to n ≤ 3000) |
| Prop 7.1 / Cor 7.2 | SOUND-AFTER-REPAIRS (D11: odd χ are not weight-2 Eisenstein coefficients; D13 label) |
| Thm 9.1 | SOUND (re-derived; numerics `scripts/review_sa_eisen.py`) |
| Cor 9.2 | SOUND-AFTER-REPAIRS (D12: last sentence false — counterexample n·μ²(n)) |
| Cor 9.3 | SOUND; its *Reading* overclaims (D14: maps valid only at primes are not covered) |
| Lemma 10.1 / Prop 10.2 | SOUND (10.2: only the periodicity statement is a theorem, D13) |
| §11 | SOUND as Assessment |

## Checks performed

**§1 literature.** Sardari arXiv:1510.00462 (Duke 168 (2019), DOI 10.1215/00127094-2019-0007 — confirmed via
the arXiv record) — I downloaded the arXiv PDF and read Thm 1.2, Conj 1.3, Thm 1.6, Remark 1.7 directly.
* Thm 1.2 (d = 4): "the same result holds provided that N is odd and N ≫ (r⁻¹m)^{6+δ}", constant depending only on
  Ω and δ (Ω a fixed compact subset of the real quadric F = 1, hence on F). Matches §1. Exponent 6 "cannot be
  replaced with a number smaller than 4" — matches.
* Conj 1.3: d = 4, N odd, N ≫ (r⁻¹m)^{4+δ}. Matches.
* Thm 1.6 (1.4), d = 4: `|V_N(ℤ) ∩ B_{a,r}| ≫ S_B(N)|B|³N(1 + O((|B|³√N)^{−1/2}N^ε))`, `|B| = r/m`. Matches
  §1's main term and relative error. **But** Thm 1.6 is stated for global balls with `gcd(a_p, p) = 1`, i.e. the
  class λ is primitive at every p | m (Sardari reduces the imprimitive case by dividing N by p^{2h_p}). §1/Def 2.1
  allow arbitrary λ. (D2.)
* Remark 1.7: the lower bound `S_B(N) ≥ c_ε N^{−ε}` is asserted by Sardari for d = 4 "if N is odd". This is
  the input behind the document's `σ_p ≥ N^{−o(1)}`; it is *not* true for general quaternary forms with an odd
  anisotropic prime (see D4, numerical counterexample) — Sardari's constants depend on F, and his remark should
  be read for a fixed F with the anisotropic-prime part of N bounded. The document's own caveat ("away from
  anisotropic-prime blowups") is right but is not carried into the theorem statements (D4).
* BKS arXiv:1609.06097, "Twisted Linnik implies optimal covering exponent for S³": abstract confirms a covering
  exponent result conditional on a twisted Linnik conjecture. The DOI on the arXiv record is
  10.1093/imrn/rnx116, i.e. **IMRN**, not Duke as §1 says (D1). Sardari's paper (line "Conjecture 1.3 implies
  K₄ = 4/3") confirms the 4/3 ↔ exponent-4 calibration of §4.
* Sardari arXiv:1511.09340 abstract: diameter of LPS bipartite Ramanujan graphs `> (4/3)log_p n + O(1)`, and an
  infinite family with diameter `≥ ⌊(4/3)log_p n⌋`. Matches §1 (LPS). The LPS upper bound `2log + O(1)` I did
  not re-verify (not accessed); the document flags this itself.
* DSP (Duke–Schulze-Pillot): not accessed; statement as given is the standard one.
* Pila Thm A: not re-accessed by me; the verbatim statement was checked by R124 (`reviews/pointwise-ternary-review.md`):
  irreducible affine V of dim n, degree d in 𝔸^N, `≤ c(n,d,N) H^{n−1+1/d} exp(12√(d log H log log H))`, uniform in V.
  This is what Thm 2.3 uses.

**§3 matrix dictionary and Lemma 10.1 (`scripts/review_sa_typeII.py 3000`).** Enumerates ET Type II quadruples
directly from `c(4abd − n) = a + b` (independent of the author's matrix search). For all odd n ≤ 3000: γ =
[[aM−1, M],[cn, bM−1]] (M = 4cd) has det 1; the 4/n identity holds in exact rationals; every prime 5 ≤ p ≤ 3000
has a quadruple; no odd square has one. The product formula of Lemma 10.1 holds symbolically, and the
decomposition `S = ⊔_M U⁻γ_M U⁻` is a bijection `(a, b) ∈ ℤ²` ↔ elements (γ₁₁ = aM−1, γ₂₂ = bM−1 determine γ₂₁ via
det). Converse (all SL₂ matrices with γ₁₂ = M, γ₁₁ ≡ γ₂₂ ≡ −1 (M), γ₂₁ = cn, c | M/4 ↔ quadruples) verified by
brute force for odd n < 200. Prime n never divides M (n ≤ 3000) — see D9.

## Defects

(pending)
