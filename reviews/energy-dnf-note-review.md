# Referee report R50 — `paper/energy-dnf-note.tex` (branch side-agent/energy-paper, Draft v1)

Referee: hostile side agent R50 (branch side-agent/referee-energy-note).
From-scratch scripts: `scripts/review_r50_*.py` (no reuse of `scripts/energy_note_check.py`).

## Status: IN PROGRESS

## 1. Core: Thm 1.1, Lemma 2.2, Prop 2.3, Lemma 3.1, Lemma 4.1, Lemma 4.2, Thm 4.3 — SOUND

Re-derived line by line:
* Lemma 2.2(a)–(d): correct (λ^U = Σ_{V⊆U} μ^V; (c) G_{1-φ} = (1-Eφ)² + Σ_{U≠∅}λ^U‖φ^{=U}‖²; (d) tensorisation).
* Prop 2.3: G_{1_E} = Π(p_v² + λ_v p_v(1-p_v)) = π_E Π(λ_v − μ_v p_v); limit p→0 gives 1 − 2π_E + π_E w_E(1+o(1)) > 1 iff w_E > 2. Correct.
* Lemma 3.1 (cover bound): restriction to fibre y, inclusion–exclusion, L_V kills cylinders whose support is a proper subset of V, the surviving point indicators are exactly the subfamilies of events holding at x=(σ,y) whose traces cover V; collapsing repeated supports via the "class of m equal traces contributes −1" remark is right. Equality at V=∅ (N(∅)=1[H=∅]=F(x)) correct.
* Lemma 4.1 (polarization): the two-point law p_v ∈ {1, −μ_v} with P(p_v=1)=μ_v/λ_v has mean 0, variance μ_v; collapse Σ_{B⊆P^c∖U}(−μ)^B λ^{P^c∖B} = λ^U·Π(λ−μ) = λ^U. Correct.
* Lemma 4.2: deletion–contraction identity Θ(C)=λ_vΘ(C/v)−μ_vΘ(C−v) re-derived; induction on |∪C| is well-founded (both C/v and C−v lose v); contraction keeps weights ≤ 2 and w_{J0∖v}−1 ≥ 0. Correct.
* Thm 4.3: P(J∩P=∅)=1/w_J, independence over a matching, (1−1/w)+(w−1)²/w = w−1. Correct.

From-scratch exact check (`scripts/review_r50_core.py`, seed 3, 2000 random systems on Π[q_v], n≤4, q_v≤4,
half with adversarially biased measures (rare value of prob ≈1/150) and events concentrated on rare values,
rational weights pushed to the threshold w_E = 2): Thm 1.1, Lemma 3.1 for every V, the matching refinement
G_F ≤ E_x min_M Π(w_J−1), the polarization identity (exact expectation over P), |Θ| ≤ Π_M(w_J−1) and
Q ≤ Π_M(w_J−1) for every matching with equality on matchings — all pass. Max G observed 0.99999999873
(the bound is essentially attained; consistent with Prop 2.3/6.1). Output: `data/r50_core_seed3.txt`.

No defect in the core proof.
