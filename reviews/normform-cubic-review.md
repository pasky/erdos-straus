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

### Thm 1.2′ (Type I, P* irreducible, valid on a lattice coset in an open cone) — SOUND-AFTER-REPAIRS (minor)
Re-derived every case; all algebraic rearrangements verified symbolically (review_r259_identities.py: (c1) B/C/D cases,
(c2) μ = k expansion incl. the "P²-coefficient" step).
* The "coefficient of P²" step in (c2) μ = k is not a coefficient comparison in a polynomial ring in P (E_A, E_B ∉ ℚ[P]);
  it is a degree argument: (4CDκκ′ − κ − κ′)P² has degree 2k while P·G and C − 4CD·E_A·E_B have degree ≤ 2k − 1. Correct,
  but should be said (MINOR D3).
* (c1) B-case: E* | P*² ⇒ E* = λP*^i by unique factorisation (P* prime), 0 < deg E* < k impossible. Correct; this is
  genuinely degree-free (the degree-2 proof's "Q on a rational line" is replaced correctly).
* (c2) 0 < μ < k: γ, δ ≤ k − μ < k, μ < k, so P* divides a product of forms of degree < k. Correct.
* Positivity paragraph: it says every coordinate "is positive" at valid points. Validity (POINTWISE_BINARYFORM §1) allows
  the sign pattern (A, B, C) < 0 < D; the R256 repair to SYNTHESIS_SPARKS7 Thm 1.2 handles it by the dilation
  (A, B, C) ↦ −(A, B, C) (preserves the Type I identity and the conclusion). That repair was not carried over (MINOR D1).
* The cone/direction argument needs L to be a coset of a *full-rank* sublattice of ℤ^r (otherwise L need not have points
  tending to infinity in an open set of directions). Implicit; state it (MINOR D2).
Edge case: P irreducible, P* reducible — the conclusion FAILS: P = 4u² − 4v² − 1 (P* = 4(u − v)(u + v)) carries the Type I
family (A, B, C, D) = (u − v, u + v, 2u, 1), valid on the open cone u > |v| (e.g. (u, v) = (1, 0): n = 3,
4/3 = 1/(abdn) + 1/(acd) + 1/(bcd) = 1/3 + 1/2 + 1/2), and not in ℚ[P]. So again P* irreducible is the operative
hypothesis. (Search found 18 such non-ℚ[P] families, all with valid points.)
