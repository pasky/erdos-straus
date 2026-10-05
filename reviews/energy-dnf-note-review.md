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

## 3. Prop 6.1 (sharpness), Ex 6.2 (parities), Ex 6.3 (non-monotonicity) — SOUND (minor wording)

Re-derived Prop 6.1: per-block level weights (1−π)² at W=∅ and π²((1−p)/p)^{|W|} at W⊆S_i (so π(1−p)^k at W=S_i);
Poisson limit e^{−2s}s^j/j!; at s=j/2 and with j! ≤ e·j^{j+1/2}e^{−j} the bound 2^{−j}/(e√j) follows. Correct.
Consequence "no Cρ^{−(t+1)/k} with ρ>2" correct; it needs p→0 as t grows (bias depending on t), which the
statement allows ("a suitable product measure") — fine, but see D4.
From scratch (`scripts/review_r50_sharp.py`, `data/r50_sharp.txt`): level formula = brute force on [3]^3, {±1}^4
(biased), [3]^4; limit ≥ 2^{−j}/(e√j) for j ≤ 80; finite p = 1/40, k ≤ 3, j ∈ {1,2,4}: max_m En(F;jk−1)·2^j well above
1/(e√j) and below the Cor 1.2 bound. Parity formula En = 4^{−s}Σ_{i≥j}C(s,i) = brute force; (max_s En)^{1/j} =
0.298587, 0.310939, 0.319400 for j = 10, 20, 40 (reproduces the note's 0.299/0.311/0.319; → 1/3 by Stirling).
Ex 6.3 (`scripts/review_r50_mono.py`, `data/r50_mono.txt`): exactly G = 323/4096 + 343√2/2048 ≈ 0.3157106 and,
after adding A, 147/1024 + 63√2/512 ≈ 0.3175692 — increase confirmed. [5]^3 (λ=2^{1/3}, points with exactly two
nonzero coordinates): adding A=(0,0,0) increases G (0.75406 → 0.75467); adding (1,0,0), (1,1,1), (1,2,3) does not.

D3 (MINOR) §6 after Prop 6.1: "the supremum over m … is about 2/√(2πj) for small p (an earlier internal
computation; we do not prove it)". My numbers (p→0 limit, sup over s): 0.2255 vs 2/√(2πj)=0.2523 at j=10; 0.0876 vs
0.0892 at j=80. So it is an *asymptotic* (j→∞) statement, ~11% off at j=10. It is also easy to prove
(sup_s e^{−2s}Σ_{i≥j}s^i/i! ~ 2·2^{−j}/√(2πj): the i=j term at s=j/2 plus a geometric tail of ratio ½). Repair: write
"~ 2/√(2πj) as j→∞" and either prove it in two lines or keep the hedge.

D4 (MINOR) Prop 6.1 / abstract / §1 "Over general product spaces the base 2^{−1/k} is sharp": the extremal measures
have bias p→0 *depending on t*. For any fixed product measure with all atoms ≥ δ (e.g. q-ary uniform with q fixed,
or uniform cube) the proposition says nothing. Worth one sentence: "sharp in the sense of the sup over all product
measures; for a fixed measure the optimal rate is open (cf. Ex 6.2)".

D5 (MINOR) Ex 6.3: the [5]^3 sentence does not say which event is added. Repair: "…; adding A={x=(0,0,0)}
increases G_F from 0.75406 to 0.75467 (λ=2^{1/3})" (my values; the author's script does not check [5]^3, as the
report admits).
