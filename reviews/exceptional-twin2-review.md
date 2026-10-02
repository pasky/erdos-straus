# Hostile review: EXCEPTIONAL_TWIN2.md (task O3), commit 3ea1bcb

Reviewer: side agent (review-twin2). Subject files brought in from
`side-agent/twin-lambda2@3ea1bcb`: `EXCEPTIONAL_TWIN2.md`,
`reviews/agent-reports/AGENT_REPORT_O3.md`, `scripts/twin2_*.py`.
Context read: TW §6.6–6.8 (Lemma 6.6, Red 6.7, Conj 6.8, Lemma 6.10/6.11,
(6.2)/(6.3)), TW Lemma 1.3, ET Thm 5.5 / Cor 5.6.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
D1, D2, … (severity: **major** = claimed statement not proved as stated;
**minor** = local slip, fix is mechanical; **nit** = wording).

## Item 1. Lemma 1.1 and Corollary 1.2 (conditional local lemma) — SOUND

Checked line by line. (1) is the Erdős–Lovász induction. (2): with
`𝓢₁ = Γ(B)∩𝓢`, `𝓢₂ = 𝓢∖𝓢₁`, B is independent of `A_{𝓢₂}` (disjoint
coordinate sets), so the numerator is `≤ P(B)`; the denominator bound uses
only (1) applied to `F_i ∉ 𝓢₂ ∪ {F₁..F_{i−1}}`. Correct.
Cor 1.2: each edge at ℓ yields two events of probability `π_e`, so
`Σ_{F∈Γ(E_e)} x_F ≤ 4(w_ℓ+w_m) ≤ 8δ ≤ 1/2`; `x_F ≤ 2π_e ≤ 2δ ≤ 1/8`;
`(1−x)^{−1} ≤ e^{(8/7)x}` gives `exp((32/7)Σ_T w) ≤ exp(5Σ_T w)`. Correct.

## Item 2. Lemma 1.3 (derivative identity) — SOUND

There are no edges inside one coordinate (`ℓ ≠ m`), so "no bad event" is
exactly `A_{−j} ∩ {y_j ∉ F, y′_j ∉ F′}` with F, F′ functions of `Y_{−j}`.
`μ̃_j` is affine in `κ_j`; the slope evaluated on `F^c × F′^c` is
`ν(F∩F′) − ν(F)ν(F′)` (verified). Lower bound for Z₂ by the union bound with
both marginals ν. The point that only `E[J 1_{A₋ⱼ}]` (a number) is divided by
is correct and is a genuine improvement on ET Prop 5.7.

## Item 3. Theorem 1.4 (log form of (6.2)) — SOUND

Proof checked step by step:
* `ν(F∩F′) ≤ Σ_a ν(a) N_a N′_a` and `E[N_aN′_a 1_A] = P(A)Σ P(B|A)` over
  ordered partner pairs — correct (𝓔 is a set, so partners are not repeated).
* The three cases for `P(y_m=c, y′_{m′}=c′)` are exact for the coupling
  `μ̃_m(tρ̃_m)`; summing gives `tΣν_m(c)ρ̃_m + deg(j,a)²`. Correct.
* `A_{−j} = A_𝓢` with 𝓢 = events off j; Cor 1.2 with `|T| ≤ 2` gives
  `e^{10δ}`; the denominator uses `|T| = 1`. Correct.
* `e^{10δ}/(1−2δe^{5δ}) ≤ 1+25δ` on `[0,1/16]`: checked numerically on a
  grid of 1001 points (max of difference is 0, attained at δ = 0; value at
  1/16 is 2.254 vs 2.5625).
* Summing `ρ̃_j·tΣ_{e∋j}π_eρ̃_{e∖j}` over j counts each edge twice; with
  `∫2t dt = 1` and `∫dt = 1` this is exactly (1.2).
* `κ = ρ̃` reproduces TW's conditioned coupling (TW §6.8 "Unary part"), so
  `Z₂(ρ̃)` is TW's Z₂ and Ξ_c = unary factor + `log(Z₂/Z₁²)`.

**Independent numerics** (`reviews/twin2-review-scripts/thm14_check.py`,
reviewer's own code: Z₁ by product-space enumeration, Z₂ by brute-force
enumeration of the doubled space `Π(Ω_ℓ×Ω_ℓ)` — no contraction trick; 2–5
coordinates of size 3–6 incl. an edge-free "safe" residue used to set δ
uniformly in `(0.002, 1/16]`; random, hub and cycle-rich edge sets; random or
all-one ρ̃):
* random: seeds 1,5,6 (≈690 systems in range): worst `lhs/((1+25δ)rhs)` =
  0.88;
* adversarial hill-climb over (ν, ρ̃), 60 steps/system, seeds 2,3,4,7
  (≈950 systems): worst 0.9999, **no violation**. The near-1 maximisers are
  single edges with ρ̃ supported on one end, where exactly
  `lhs/rhs = (ν_c−π)/(ν_c(1−π)²) → 1` as `ν_a → 0`: the `q_j` term is sharp
  with constant 1, confirming the author's "sharp to leading order".

No defect.
