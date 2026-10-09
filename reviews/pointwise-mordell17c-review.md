# Review R98b of POINTWISE_MORDELL17C.md (O98) — hostile reviewer

Reviewed: POINTWISE_MORDELL17C.md and reviews/agent-reports/AGENT_REPORT_O98.md (merged from `side-agent/r17-explicit-et`).
From-scratch scripts: `scripts/review_m17c_*.py` (the author's scripts were not reused).

## Verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (cumulative (H_P),(H_Q)) + table | SOUND (minor wording) |

## Claim-by-claim

### Lemma 1.1 (Abel summation)
Re-derived: with `D(K) = S(K) − S(K−2)` (S(11) := 0), `Σ_{13}^{K₁} w_K D(K) = w_{K₁}S(K₁) + Σ_{13}^{K₁−2}(w_K − w_{K+2})S(K)`;
`w_K − w_{K+2} = (16/17)w_K` for `w_K = 17^{(1−K)/2}`; boundary `≤ C·17^{1/2}·17^{(θ−1/2)K₁} → 0` for θ < 1/2; all summands ≥ 0.
Same for Q with `w_k = 17^{1−k}`, ratio `1 − 17^{−2}`. Correct. Only cumulative bounds are needed; M17B Thm 4.1's proof
(Lemma 1.1 of M17B + `NB ≤ 2D` + summation) uses (H_P) only inside `Σ w_K D_P(K)`, so the replacement is legitimate.

Table recomputed from closed-form geometric series (`scripts/review_m17c_tail.py`, mpmath 40 digits, no truncation):
`Σ_{K≥K₀ odd} 17^{θK+(1−K)/2} = 17^{1/2} r^{K₀}/(1−r²)`, `r = 17^{θ−1/2}`; `T_Q = 34·q⁹/(1−q²)`, `q = 17^{−2/5}` = 1.410566·10⁻³.
Exact thresholds (θ = 0.4): pointwise K≥13 = 1.409796…, cumulative K≥13 = 1.497908…, cumulative K≥15/ρ₂ = 2.639795…;
all 18 floor-rounded entries of the table agree digit for digit, and the pointwise row equals M17B §4 (also the M17B
K≥15 row 2553/272.9/27.53/2.484/0.8947/0.1692 is reproduced). Data check `1463 ≤ 1.497·17^{5.2} ≈ 3.7·10⁶`: true (trivially).

