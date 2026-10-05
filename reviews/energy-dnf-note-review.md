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

## 2. Cor 1.2 (energy tail with a(2−a)) and Cor 1.3 (DNF tails, 1+4p, influence, q-ary) — SOUND (one MINOR overstatement of novelty-relevance, see D2)

Re-derived: Σ_{U≠∅}λ^{|U|}‖F^{=U}‖² ≤ 1 − (EF)² = a(2−a); g = 2F−1 multiplies non-constant energies by 4;
G_g = (1−2p)² + 4(G_F − (1−p)²) ≤ 1+4p; I ≤ (k/ln2)·Σ(λ^{|U|}−1)‖g^{=U}‖² ≤ 4kp/ln2 (using λ^{|U|}−1 ≥ |U| ln2/k).
CNF sign convention (p = P[h=+1]) and q-ary splitting into disjoint cylinders with equal support: correct.
ε-concentration degree k·log₂(4/ε): correct.

From-scratch check (`scripts/review_r50_dnf.py`, output `data/r50_dnf_seed1.txt`; exact rationals for tails via
tail^k·2^{t+1} ≤ (4p(2−p))^k, 60-digit mpmath only at the irrational endpoint λ = 2^{1/k}):
* all 65536 Boolean functions on 4 bits, uniform measure, k = minimal DNF width: pass; max of
  W^{>t}/(4p(2−p)2^{−(t+1)/k}) = 0.680315 (reproduces the author's 0.680); max I/(kp) = 2.0; max (G_g−1)/p = 2.0;
* 1500 random DNFs, n ≤ 6, random widths, biased measures with biases down to 1/50 and up to 49/50: pass, max ratio 0.9899;
* adversarial: disjoint ANDs (tribes / the sharpness family) at p ∈ {1/2,1/5,1/20,1/100}: pass, max ratio 0.99498
  (bound essentially tight under strong bias, as Prop 6.1 predicts); sunflowers (common core of k−1 variables)
  and threshold-≥k DNFs on 6 bits: pass, max ratio 0.764.

Defect D2 (MINOR, comparison with known influence bound), §1 "Comparison" paragraph and Cor 1.3:
the note says its influence bound (4k/ln2)p ≈ 5.77kp "is weaker by a constant factor than the known bound 2w".
This understates the known bound: the elementary certificate argument gives **I[g] ≤ 2w·p** on the uniform cube
(each sensitive edge has exactly one endpoint where the DNF is true, and there the sensitivity is ≤ w, so
I = 2·E[s(x)·1{g(x)=−1}] ≤ 2wp), and under a product measure the same argument gives Σ_v‖L_v g‖² ≤ 4wp.
(My data: max I/(kp) = 2.0 uniform, 3.92 biased — consistent with these.) So the factor p is *not* a gain of the
new method; the new bound is worse by 2/ln2 (uniform) resp. 1/ln2 (biased).
Repair: state "I ≤ 2wp (uniform), ≤ 4wp (product measures) follows from the trivial certificate argument; our
(4k/ln2)p is weaker by a constant and is stated only because it falls out" — or drop the influence claim.
