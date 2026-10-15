# R259 — hostile review of O248 (NORMFORM_CUBIC.md, BRAINSTORM/z20_*.md, AGENT_REPORT_O248)

Reviewer: R259 side agent (branch side-agent/review-normform, merged side-agent/normform-cubic at 7f070f22).
From-scratch scripts: `scripts/review_r259_identities.py` (sympy: every rearrangement in Thms 1.1′/1.2′/3.1),
`scripts/review_r259_search.py` (python-flint exact brute-force search for Type I/II families over 9 forms incl. controls).
Status: IN PROGRESS (written claim by claim).

## Verdict table
(filled in below, claim by claim)

## Claim-by-claim

### Thm 1.1′ (Type II, P* irreducible, valid at one point) — SOUND
Re-derived independently. Setting check: "leading form" P* is the top-degree homogeneous part (§1 "Setting"), and the
hypothesis is irreducibility of P* over ℚ, not of P. Note P* irreducible ⇒ P irreducible (P = FG ⇒ P* = F*G*), not
conversely. Steps:
* s ≤ max(α, β, γ + k) and case (a) (s ≤ α ⇒ β = γ = δ = 0, A(4BCD − 1) = B + CP, 4BCD = 1 impossible as CP non-constant):
  correct.
* (b): if γ + k > s the top C*P* survives (no other term reaches that degree), if γ + k < s the RHS has degree < s; so
  4A*B*D* = P* with α + β + δ = k. (F1) for a 3-fold product: grouping two factors, at most one of A*, B*, D* has positive
  degree, so exactly one has degree k. Correct.
* (b1) C(4ABD − P) = A + B, A + B ≠ 0 ⇒ deg C + deg(4ABD − P) = 0. Correct.
* (b2) the identity E(4BDC − 1) = P + 4B²D is verified symbolically (review_r259_identities.py). If deg E ≥ 1 then
  deg C = k − deg E ≥ 1 and E*·4BD·C* = P* with both factors of positive degree: contradicts (F1). Correct.
* The positivity remark ("used only through A + B ≠ 0") is correct; with A + B = 0 the never-valid family
  A = −B = κ, D = −P/(4κ²), C arbitrary is the only escape (case (b1)), as in the degree-2 Remark.
Edge cases (from-scratch search, see §Numerics): for P irreducible with P* reducible the conclusion FAILS —
P = 4uv − u − 1 has the valid Type II family (A, B, C, D) = (u, 1, 1, v) (n = 4uv − u − 1, 4uv = u + 1 + n), not in ℚ[P].
So irreducibility of the *top part* is the hypothesis that does the work; irreducibility of P alone is not enough. The
hypothesis is sufficient, not necessary: P = v + u² (P* = u² reducible) also collapses, trivially, since ℚ[u, v] = ℚ[P][u]
and a u-degree count over the domain ℚ[P] kills u-dependence (reviewer's argument; search confirms).
