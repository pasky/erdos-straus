# AGENT_REPORT_O1 — (E_δ), heavy coordinates, η-twin windows (checkpoint 1)

Branch: `side-agent/twin-windows`. Deliverable: `EXCEPTIONAL_TWIN.md`
(scripts `scripts/twin_*.py`, data `data/twin/`).

## Headline

**(E_δ) is bypassed, not settled.** The (η,B)-gapped part of the balanced
door is now unconditional (Theorem 2.7): `S_λ ≪_B η^{−1}λ^{3/4}` for every
fixed B, with no (E_δ), (★_δ), H_light or (NDE).

Two new ingredients:
1. **QR base (Lemma 1.1, 1.3).** Every Case-B class `−4D (mod M)` has
   Jacobi symbol −1 (classical Mordell obstruction). So the *product*
   measure "n a nonzero square mod every odd p ≤ W" lives on avoiders of
   all W-smooth classes. It costs `π(W) log 2` and inflates later
   probabilities by only `2p/(p−1)` per prime, instead of ET's
   `L' = e^{O(W^{1+C})}`.
2. **Capped distortion (Thm 2.3).** Following
   Balister–Bollobás–Morris–Sahasrabudhe–Tiba, the sequential measure
   conditions only where `p_ℓ(h) ≤ ℓ^{−1/2}`. Heavy hits leak. The leak is
   bounded by a second moment, `E p_ℓ² ≪ ℓ^{−2+ε}` (Lemma 2.4). This needs
   only divisor bounds, and with the QR base it is uniform in W. So the
   leak is `≪ W^{−1/4}` (Cor 2.5). The caps give ET Cor 3.6's inflation
   structure for free (Lemma 2.6).

**η-twin.** Twin classes are harmless with top prime `≤ e^{λ^{1/4}}`
(singleton windows; cost = void, Prop 4.1) or `> e^{λ/2}` (one-prime-per-term
window inequality, Lemma 4.2 / Cor 4.3). Theorem 4.4 combines these with
Theorem 2.7. The residual is twin moduli with top prime in
`(e^{λ^{1/4}}, e^{λ/2}]`, reduced to one named inequality: Conjecture 4.5,
a window inequality with binary conditions (the 2-prime local boost). §4.5
gives quantitative reasons why splitting, over-conditioning, leak, void and
the linear lemma each fail there.

**(E_δ) itself (§3).** OPEN. New: the u-form (Lemma 3.1), a Legendre-sign
constraint (Lemma 3.2), and an entropy heuristic predicting
`sup ≈ π(y)ℓ^{o(1)}`.

**Global (§5).** Not settled. 3/4 is now proved sharp (internally) for
ℛ(M)-families with `M ≤ P(M)^{1+B}`, for each fixed B, except for η-twin
moduli in the middle range. Also open: uniformity in B, and
(a,D)/Case-A classes for balanced moduli.

## Labels

PROVED: Lemma 1.1–1.3, Lemma 2.1, 2.2, Thm 2.3, Lemma 2.4, Cor 2.5,
Lemma 2.6, Thm 2.7, Lemma 3.1, 3.2, Prop 4.1, Lemma 4.2, Cor 4.3, Thm 4.4.
EVIDENCE: §2.4 (leak 0.056 at X = 10⁵, 0.070 at X = 10⁶ with κ = 0.2,
W = 30, full system including twin). HEURISTIC: Heur 3.3, §4.5 items 1–2 and
the quadratic-test observation. OPEN: (E_δ), Conj 4.5.

## Where a hostile reviewer should look first

* Thm 2.3, the induction step: f̃ is λ-level in the light indicators
  after averaging out the heavy ones, and the final Jensen step with
  `Q'(𝒜) ≥ 1/2`.
* Lemma 2.4: the uniformity in W of `E N_ℓ²` (the Γ ≤ 3^ω bound and the
  τ(A_q²) ≤ ℓ^{ε} bound, which needs B fixed).
* Lemma 2.6: transplanting ET Cor 3.6's γ-weighted Lemma 3.1 to the weight
  Γ (h(p) ≤ 2 for p ≤ W; h(ℓ) ≤ 2ℓ^{−1/2} above).
* Cor 4.3: Lemma 4.2 is applied to f as a function of residues (not hit
  indicators), with σ the in-window sequential capped law.

## Decision needed from parent

Should the next step attack Conjecture 4.5 directly (a binary version of
ET Prop 2.4), or first make the B-dependence explicit? The latter is
needed to cover moduli with `log M/log P(M) → ∞`.
