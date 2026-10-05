# Hostile review R49 of POINTWISE_OMEGA14.md (task O49, branch side-agent/junta-third)

Reviewer branch: side-agent/review-omega14. Reviewed state: junta-third @ 12df24b.
Status: IN PROGRESS (claims written one at a time).

## Verdicts (summary; filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 (planting) | SOUND |

## Claim-by-claim

### Lemma 1.1 (planting) — SOUND

Re-derived independently.
* Marginals: for |K|≤k, z⊆K, the σ_J-mass of {x_K=1_z} is [z⊆J]·Σ_{y'⊆J∖K}(−1)^{|z|+|y'|+1};
  J∖K≠∅ since |J|=k+1>|K|, so the alternating sum vanishes. ✔ (K=∅ gives total mass 1.)
* ν(0)=P_0−P_0Σw_J=0 ✔.
* Positivity: negative atoms are exactly 1_y with |y|=j even, 2≤j≤k+1, receiving
  P_0∏_y r·e_{k+1−j}(s)/e_{k+1}(r). Needs e_{k+1−j}(s)≤e_{k+1}(r). The counting identity
  Σ_{|I|=n−1}∏_I s·Σ_{i∉I}s_i = n·e_n(s) and Σ_{i∉I}s_i ≥ Σs−(n−1)r* give
  n e_n(s) ≥ e_{n−1}(s)(R−jr*−(n−1)r*) ≥ e_{n−1}(s)(R−(2k+1)r*) ≥ (k+1)e_{n−1}(s) ≥ n e_{n−1}(s)
  for n≤k+1 (uses j≤k+1, n−1≤k). Chaining n=k+2−j..k+1 gives e_{k+1−j}(s)≤e_{k+1}(s)≤e_{k+1}(r). ✔
* Edge cases: zero p_i (w_J=0 for J∋i, harmless); k=0 (no even |y|≥2 atoms; only needs
  e_1>0); e_{k+1}(r)>0 argued correctly. p_i<1 required for r_i finite — stated.
* From-scratch check `scripts/review_o14_planting.py` (full 2^n enumeration, exact Fractions,
  n≤10, k≤3; random p incl. exact zeros and one large coordinate p_0∈[0.6,0.9]; plus 18
  *equality* instances R=(k+1)+(2k+1)r*): 97+18 instances satisfying (1.1), **0 failures**
  of ν≥0, ν(0)=0, mass 1, all ≤k-marginals. On 294 instances violating (1.1), the same
  construction has a negative atom in 77 — so the check is not vacuous (positivity is the
  only hypothesis-dependent part).
* Minor: the author's own numerics check only ρ on |y|≤k+1 for n≤22; mine enumerate the
  full cube for n≤10 — consistent.

## Defects

(none yet)
