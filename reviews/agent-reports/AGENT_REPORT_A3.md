# AGENT REPORT A3 — the balanced-moduli door (checkpoint 1)

Branch: this worktree. Main file: `EXCEPTIONAL_BALANCED.md` (§0 has the
status table). Scripts: `scripts/balanced_numerics.py`,
`scripts/balanced_void.cpp`. Data: `data/balanced/`. Replay is at the end
of the file. Outcome so far: **(C), partial.** Neither (A) nor (B) is
proved. ES is not solved; no θ > 3/4 is claimed.

## PROVED (internal checks only, not refereed)
* **Lemma 2.1.** Let M be η-gapped, i.e. `P(M) > w₀` and
  `P(M) ≥ P₂(M)^{1+η}` with `P₂ = P(M/P(M))`. Then `P(M) ∥ M`, and every
  other prime factor above w₀ lies in an earlier window
  `W_j = (e^{s_j}, e^{s_j(1+η)}]`. So ET's hypothesis (U) holds.
  Dominant moduli are η-gapped with `η = 1/C − 1`.
* **Lemma 2.2.** ET Prop 2.4 holds without `p_i ≤ 1/4`. Coordinates with
  `p_i > 1/4` are conditioned out at cost `Σ −log(1−p_i)`; this needs
  `p_i < 1` throughout.
* **Thm 2.3.** For gapped families with `R = ℤ/Q₀`, assume (NDE): every
  reachable history has `p_ℓ(h) < 1`. Then every level-λ majorant
  satisfies (2.1): the sum over windows of `E_{Q_seq}[Φ_j^{light} +
  heavy charge]`. The proof is ET Thm 2.7 with Lemma 2.2.
* **Lemma 2.4.** For (η,B)-gapped ℛ(M)-families (`M ≤ P(M)^{1+B}`),
  the window mass satisfies `m_j ≤ C₆'((1+B)(1+η)s_j)³`. This is ET
  Lemma 3.1 plus partial summation.
* **Lemma 4.1.** Write `D = sr²` with s squarefree. Then `D | A_q²` iff
  `A_q = srk`. The condition `q | n+4D` is equivalent to `q | nk+r`, and
  `−4D ≡ −r/k (mod ℓ)`.
* **Lemma 4.2.** For every n,
  `|F_ℓ(n)| ≤ Σ_{q∈𝒬_ℓ} τ(A_q²) ≤ |𝒬_ℓ|X^{o(1)}`. This gives (★_δ)
  exactly when B < 1. For B ≥ 1, `|𝒬_ℓ| ≥ ℓ^{1+o(1)}`.
* **Prop 4.3** (uses Linnik's theorem with exponent 5, Xylouris). If
  `X ≥ ℓy` with `y = ℓ^{1/(1+η)}`, then some integer n has
  `|F_ℓ(n)| ≥ y^{1/5−o(1)}`. Reachability is not checked.
* **Prop 4.4.** (E_δ) ⇒ (★_δ) ⇒ H_light(O_δ(1)). The weak-ε variant
  (`p ≤ ε` gives exponent `3/4 + O(ε)`) is only *sketched*.

## CONDITIONAL
* **Thm 2.5.** Under H_light(K), every level-λ majorant of an
  (η,B)-gapped ℛ(M)-family has saving at most
  `C K^{1/4}(1+B)^{3/4}η^{−1}λ^{3/4} + Kλ^{3/4} + O(η^{−1}log λ(log λ+log K))`,
  so `C(η) ≍ η^{−1}`.
  * H_light(K) consists of (NDE), the Q_seq-profile bound `≤ K·m_j`, and
    heavy charge `≤ Kλ^{3/4}`.
  * H_light follows from (★_δ): `p_ℓ(h) ≤ ℓ^{−δ}` on reachable histories.
  * (★_δ) follows from (E_δ).
* **(E_δ)** (open for B ≥ 1). For every integer n,
  `#{−r/k mod ℓ : (4srk−1)/ℓ = q ∈ 𝒬_ℓ, q | nk+r} ≤ ℓ^{1−δ}`.

## EVIDENCE (`EXCEPTIONAL_BALANCED.md` §3, §4.3)
* **Sequential hit probabilities.** On sequentially sampled histories
  (singleton windows, X up to 10⁶), `K = E_seq p/E_U p` lies in
  [0.52, 1]. Also `max p(h)·√ℓ ≤ 4.3`, and `p > 1/4` occurs only for
  ℓ < 128.
* **Adversarial supremum.** The greedy supremum of `|F_ℓ|` is ≈ π(y)
  (13–36 values at ℓ = 101–401), with or without reachability.
* **Exact LP on real-class windows** (4–5 primes < 25, floating-point
  HiGHS, uncertified):
  * balanced classes add **no** saving at level m ≤ 2;
  * matched-mass single-prime controls save more at every m ≥ 2;
  * example, S = {11,13,17,19}, m = 2: control +0.317, balanced +0.035.
* **Real-prime voids** (1.09·10⁹ primes near 10¹², moduli ≤ 4000),
  measured as `−log void` against mass:
  * dominant classes: ratio → 1.00;
  * gapped non-dominant classes, added on top: ≈ 0.55–0.6 of their mass;
  * η-twin classes, added last: ≈ 0.2 of their mass.
* **Caveats.** All scales are tiny, the regime is dense, and the
  adversary is weak.

## Open core
1. **η-twin windows.** Neither §2 nor §4 touches them. A local inequality
   inside a window with internal pair conditions is needed: route 3 of §1,
   the "boost" form `E[G|𝒜_W] ≤ e^{Φ_W}E[G]`.
2. **(E_δ),** a CSP-type extremal problem. How many congruences
   `nk + r ≡ 0 (q)` with distinct `r/k mod ℓ` can one n satisfy? The
   conjectured truth is ≈ π(y), giving `δ < η/(1+η)`.
   * The "steering is rare" averaging route is borderline at exactly the
     same threshold (§4.4 item 3).

## Points for the hostile reviewer
* **Thm 2.3's "verbatim" claim.** Check that ET Thm 2.7's proof uses
  `p ≤ 1/4` only inside Prop 2.4. (NDE) is assumed, not proved.
* **Thm 2.5's arithmetic.** I claim one band per window (`G = 1`), and
  that `E log μ ≤ log E μ` is used correctly.
* **Lemma 2.4** bounds `m_j` by the full mass up to `e^{(1+B)s_{j+1}}`.
  This is lossy (no η factor), which costs `η^{−1/4}`.
* **Prop 4.3.** Check the distinctness of the q_k, and that
  `D_k = A/k` divides `A²`.
* **Scope.** §2 and §4 treat the ℛ(M)-grouping only. The (a,D) and
  Case-A groupings are not checked.

## Recommended next steps
1. **Route 3 on η-twin windows.** Start with "linear" windows
   (`log ℓ > λ/2`), where a marginal-inflation lemma should make the
   boost O(1). This would make conditions beyond the level harmless.
2. **Attack (E_δ)** via the (s,r,k) lattice, or find a counterexample
   with many structured cofactors. A stronger adversary (ILP or
   simulated annealing) would test sup ≈ π(y) at ℓ ~ 10³–10⁴.
3. **Λ² route.** Test H_MS^{Sel} numerically on real windows. Measure
   Ξ_𝒜(α) by Monte Carlo, comparing twin vs no-twin.
