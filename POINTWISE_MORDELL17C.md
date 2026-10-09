# POINTWISE_MORDELL17C — explicit P-count at prime powers, r = 17 (task O98)

Status: O98 (branch `side-agent/r17-explicit-et`), in progress. Builds on POINTWISE_MORDELL17.md (= M17) and
POINTWISE_MORDELL17B.md (= M17B; Theorem 4.1, hypotheses (H_P), (H_Q)). Labels as in DISCOVERIES.md.
`N = 17^K`, `F = 17^k`, K, k odd.

## 1. The hypotheses only need to hold on average over K (PROVED)

**Lemma 1.1 (cumulative form of (H_P), (H_Q)).** Put `S_P(K) = Σ_{13 ≤ K' ≤ K, K' odd} D_P(K')` and
`S_Q(k) = Σ_{9 ≤ k' ≤ k, k' odd} D_Q(k')`. In M17B Theorem 4.1, (H_P) may be replaced by
`(H_P^cum)  S_P(K) ≤ C·17^{θK}` for all odd `K ≥ 13` (θ < 1/2), and then `T_P ≤ 2·(16/17)·C·Σ_{K≥13 odd} 17^{θK+(1−K)/2}`.
Likewise (H_Q) may be replaced by `S_Q(k) ≤ 17^{3k/5}` (k ≥ 9), with `T_Q` multiplied by `1 − 17^{−2}`.
*Proof.* With `w_K = 17^{(1−K)/2}` (decreasing, `w_K − w_{K+2} = (16/17) w_K`), Abel summation gives for every odd `K₁`
`Σ_{K=13}^{K₁} w_K D_P(K) = w_{K₁} S_P(K₁) + Σ_{K=13}^{K₁−2} (w_K − w_{K+2}) S_P(K)`. Under (H_P^cum) the boundary term is
`≤ C·17^{1/2}·17^{(θ−1/2)K₁} → 0`, and all terms are ≥ 0; let `K₁ → ∞`. Use `NB_P ≤ 2D_P` (M17B Lemma 1.1). Same for Q
with `w_k = 17^{1−k}`, `w_k − w_{k+2} = (1 − 17^{−2}) w_k`. ∎

Since `S_P(K) ≥ D_P(K)`, (H_P) ⇒ (H_P^cum) with the same C, so the cumulative form is strictly weaker, and the
admissible constant grows by the factor 17/16 (`scripts/m17c_tail_cum.py`, floor-rounded; the pointwise column
reproduces M17B §4):

| θ | 0.25 | 0.30 | 0.35 | **0.40** | 0.42 | 0.45 |
|---|---|---|---|---|---|---|
| C*, pointwise (H_P), K ≥ 13, base ρ₁ (= M17B) | 619.2 | 87.88 | 11.76 | 1.409 | 0.5686 | 0.1275 |
| C*, cumulative (H_P^cum), K ≥ 13, base ρ₁ | 657.9 | 93.38 | 12.50 | **1.497** | 0.6042 | 0.1354 |
| C*, cumulative, K ≥ 15, base ρ₂ | 2712 | 290.0 | 29.25 | **2.639** | 0.9507 | 0.1798 |

(T_Q kept at the un-weakened `1.4106·10⁻³`, a safe over-estimate.) Data check: `S_P(13) = 1463 ≤ 1.497·17^{5.2}`.
The point of Lemma 1.1 is less the constant than the *shape*: a bound for `Σ_{K' ≤ K} D_P(K')` may be attacked by
averaging over the exponent `K'`, which a pointwise bound cannot (see §3).
