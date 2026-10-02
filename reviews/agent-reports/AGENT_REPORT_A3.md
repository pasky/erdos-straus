# AGENT REPORT A3 — the balanced-moduli door (checkpoint 1, post-review)

Main file `EXCEPTIONAL_BALANCED.md` (§0 status table, Replay at end);
scripts `scripts/balanced_numerics.py`, `scripts/balanced_void.cpp`; data
`data/balanced/`. Review `reviews/exceptional-balanced-review.md` (branch
side-agent/review-balanced): no critical defect; D1–D19 applied. Outcome:
**(C), partial.** Neither (A) nor (B) is proved. ES is not solved, and no
θ > 3/4 is claimed.

## PROVED (internal checks only, not refereed)
* **Lemma 2.1.** η-gapped moduli (`P(M) > w₀`, `P(M) ≥ P₂(M)^{1+η}`,
  `0 < η < 1`) satisfy ET (U) for windows of log-ratio 1+η.
* **Lemma 2.2.** ET Prop 2.4 holds without `p ≤ 1/4`. Heavy coordinates
  cost `Σ −log(1−p_i)`.
* **Thm 2.3.** For gapped families, under (NDE), every level-λ majorant
  satisfies `log(1/Eν) ≤ log(Q₀/|R|) + Σ_j E_{Q_seq}[Φ_j^{light} + heavy]`.
  R may be a selector (D2).
* **Lemma 2.4.** For (η,B)-gapped ℛ(M)-families, `m_j ≤ C₆'((1+B)(1+η)s_j)³`.
* **Lemma 2.5a.** In ET Prop 2.4, G may be taken to be the number of
  nonempty bands (D3).
* **Lemma 4.1.** `D = sr²`: `D | A_q²` iff `A_q = srk`; then `q | n+4D` iff
  `q | nk+r`, and `−4D ≡ −r/k (mod ℓ)`.
* **Lemma 4.2.** The *counting bound* gives (★_δ) iff B < 1.
* **Prop 4.3** (given Linnik with some exponent L). Some n has
  `|F_ℓ(n)| ≫ y^{1/L−o(1)}`. The witnesses are **dominant** prime
  cofactors, so this is no evidence on balanced content (D9).
* **Prop 4.4.** For fixed B and `w₀ ≥ 4^{1/δ}`: (E_δ) on `𝒬_ℓ^{(B)}`
  implies (★_δ), which implies H_light(O_δ(1)).

## CONDITIONAL / OPEN
* **Thm 2.5** (for each fixed B; constant 380, D3a). Under H_light(K), the
  saving is at most
  `C K^{1/4}(1+B)^{3/4}η^{−1}λ^{3/4} + Kλ^{3/4} + O(η^{−1}log λ·(log λ+log K+log(1+B)))`.
  H_light(ii) is now the cubic window bound
  `E_{Q_seq}Σ_{W_j} p ≤ K((1+B)s_j)³`, so (★_δ) ⇒ H_light holds literally
  (D4).
* **(E_δ)** (open for B ≥ 1). For every n,
  `#{−r/k mod ℓ : (4srk−1)/ℓ = q ∈ 𝒬_ℓ^{(B)}, q | nk+r} ≤ ℓ^{1−δ}`.
  The open content is the composite (balanced) cofactors `q ∈ [ℓ, ℓ^B]`.
* **Conj 4.4W.** `p ≤ ε` ⇒ cap `λ^{3/4+O(ε)}`. This is a SKETCH only. The
  large-divisor range fails because `h(p) ≍ ε` does not decay (D12-W).
* **Not covered.** Gapped moduli with unbounded `log M/log P(M)` (no
  summation over B, D19), and all η-twin moduli.

## EVIDENCE (corrected readings)
* **Sequential histories.** `K ∈ [0.48, 1]`. **Heavy histories move up
  with X**: at ℓ ∈ [128,256), 2.7% of histories at X = 10⁵, 15.4% at
  X = 10⁶. A fixed w₀ fails for unrestricted B (D13). The earlier
  "consistent with (★_δ) above 128" is withdrawn.
* **LPs (4 primes < 25).** The composites there are mostly η-twin *pairs*,
  which are never balanced. They add ≤ 0.035 at m ≤ 2. The ≥ 3-prime
  (balanced) classes add 0 at m ≤ 3, near their visibility threshold.
  Matched-mass single-prime conditions do better (D16).
* **Real-prime voids, both orders** (D15).
  * Each non-dominant family yields ≈ 0.5 void per unit mass when added to
    dom, and less when added second.
  * "Twin ≈ 0.2, redundant" was an ordering artefact and is withdrawn.
* **Steered greedy sup** (D17). All-type counts ≈ `π(y) + |ℛ(ℓ)|`.
  Balanced cofactors alone reach 58 values at ℓ = 503 (π(y) = 34) and 42
  at ℓ = 701. This is inconclusive on (E_δ).
* **Honest summary.** After the repairs the evidence **no longer favours
  (A)**. It is neutral at the reachable scales and favours (B) nowhere.

## Open core
1. **η-twin windows** (untouched): a local inequality inside a window with
   internal pairs is needed (route 3, `E[G|𝒜_W] ≤ e^{Φ_W}E[G]`).
2. **(E_δ) for composite cofactors.** How many `nk + r ≡ 0 (q)`, with
   `q ∈ [ℓ, ℓ^B]` y-smooth and distinct `r/k mod ℓ`, can one n satisfy?
3. **Gapped moduli with unbounded B.** The heavy-history trend (§3.1)
   suggests w₀ must grow.

## Recommended next steps
1. A stronger adversary (ILP/annealing) for the balanced-only part of
   (E_δ) at ℓ ~ 10³ with fixed B. Does the count grow like #bal or stay
   near π(y)?
2. Route 3 on η-twin windows, starting with "linear" windows
   (`log ℓ > λ/2`) via a marginal-inflation lemma.
3. Monte-Carlo Ξ_𝒜(α) (H_MS^{Sel}) on real windows, twin vs no-twin.
