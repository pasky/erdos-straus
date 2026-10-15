# Hostile review R240 of FF_ODD_ABSENCE.md (O226) — round 1

Reviewer: R240 (side agent, branch side-agent/review-ff-odd). Merged author branch side-agent/ff-odd-absence at review start.
From-scratch scripts: `scripts/review_r240_*`.

## Summary verdicts
(filled in as the review proceeds)

## Lemma 1.1 (root-product identity)
Re-derived independently. At a root β of V (multiplicity counted), C(β) = −W(β) and M(β)W(β)C(β) = β^s, so −M(β)W(β)² = β^s;
∏β_i = (−1)^t V(0)/λ. Resultant step: ∏_i W(β_i) = μ_W^t ∏_{i,j}(β_i − γ_j) = μ_W^t (−1)^{ta} λ^{−a} ∏_j V(γ_j), and V(γ_j) = −γ_j^s
because (MWC)(γ_j) = 0; ∏γ_j = (−1)^a W(0)/μ_W. Same for M. Substituting and cancelling M(0)^s via V(0) = M(0)W(0)C(0) gives
  (W(0)/C(0))^s = (−1)^{ts + t + tz + z + zs} μ_M^{s−t} μ_W^{2(s−t)} λ^{z + 2a − s},
which is the stated formula. Roots of W, M are nonzero (W(0), M(0) ≠ 0), so V(γ) = −γ^s ≠ 0 and no division by zero occurs;
G is used only through C(β) = −W(β). Valid over any field, including a = 0 or t = 0 (empty products). **SOUND.**
