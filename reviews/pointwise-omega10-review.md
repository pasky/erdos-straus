# Hostile review R38 of POINTWISE_OMEGA10.md (task O38, branch esw-suppression)

Reviewer branch: side-agent/review-omega10. Reviewed: author commit fcc9b93.
Status: IN PROGRESS.

## Summary verdicts (per claim)

| Claim | Verdict |
|---|---|
| Lemma 3.1 (cover bound) | (pending numerical) re-derived: SOUND |
| Lemma 3.2 (polarization) | re-derived: SOUND |
| Lemma 3.3 (deletion–contraction, matching bound) | re-derived: SOUND |
| Thm 3.4 (Q, Q′, QM) | re-derived: SOUND |
| Cor 3.5 (C-1) | pending |
| Cor 4.1 | pending |
| Thm 4.2 | pending |
| Remark 4.3 | pending |
| §1, §2 | pending |

## Re-derivations

### Lemma 3.1
* `Λ=⊗(I+μ_vL_v)=Σ_V μ^V L_V`; `L_V` is a product of commuting orthogonal
  projections, so `⟨F,L_VF⟩=‖L_VF‖²`. Identity (i) OK.
* `(L_VF)(σ,x_{V^c})=(L_V g)(σ)` with `g=F(·,x_{V^c})` since `L_V` acts only
  on V; on `Ω_V`, `L_V g=g^{=V}`. OK.
* Expanding `g=∏_E(1−A_E|_V)=Σ_𝒥(−1)^{|𝒥|}A_𝒥`: inconsistent 𝒥 give 0;
  cylinders on a proper subset of V have zero top component (some `E_v`
  kills them); support V ⇒ point mass. So `g^{=V}=L_Vc`, `‖L_Vc‖≤‖c‖`. OK.
* At `x=(σ,x_{V^c})` the 𝒥 counted in `c(σ)` are exactly sub-families of
  events holding at x whose supports cover V. Multiplicity: two distinct
  events with equal support cannot both hold at x (distinct value vectors),
  and in any case `N(V)=(−1)^{|V|}τ̂(V)` depends only on the transversal
  function τ, which is insensitive to repeated edges. I re-derived
  `τ̂(V)=(−1)^{|V|}N(V)` directly. V=∅ term: `N(∅)=1[𝓗=∅]`, giving
  `E F=‖F‖²`, equality. OK.
* Not used: uniformity of the measure (only `‖L_Vc‖≤‖c‖`); the lemma holds
  for any product probability measure. (Observation, not a defect.)

### Lemma 3.2
Multilinear extension `T(p)=Σ_R τ(R)p^R(1−p)^{R^c}=Σ_V τ̂(V)p^V`;
independent mean-0 variance-μ_v variables ⇒ `E T²=Q_μ`. With
`p_v∈{1,−μ_v}` (probabilities `μ/λ`, `1/λ`): mean 0, variance μ. Factor
`(1−p_v)` kills `R⊉P`; on `P^c∖R`, `1−p=λ`; on `R∖P`, `p=−μ`. Then the
inclusion–exclusion and the identity `Σ_{B⊆P^c∖U}(−μ)^Bλ^{P^c∖U∖B}=1`
give `T=Θ_λ(𝓗_P)`. μ_v=0 is harmless (`p_v≡0`). OK.

### Lemma 3.3
Split 𝒥 by `𝒥_1=` edges through v. `𝒥_1=∅` gives `Θ(𝒞−v)`; all 𝒥
weighted by `λ_v^{1[𝒥_1≠∅]}λ^{∪(𝒥∖v)}` give `λ_v[Θ(𝒞/v)−Θ(𝒞−v)]`
for the `𝒥_1≠∅` part. Identity OK (multisets fine). Induction on |vertex
set|: weights stay ≤2; `𝓜∖E_0∪{E_0∖v}` is a matching *sub-multiset* of
`𝒞/v` (edges of `𝓜∖E_0` avoid v); if `E_0={v}` the bound is 0 and indeed
`∅∈𝒞/v` ⇒ `Θ(𝒞/v)=0`; `λ_v(w/λ_v−1)+μ_v=w−1`. Base cases (∅∈𝒞, 𝒞=∅,
𝓜=∅ reduced to one edge since `w−1≤1`) OK.

### Thm 3.4
`P(E∩P=∅)=∏_{v∈E}(1/λ_v)=1/w_E`, independent over disjoint E;
`(1−1/w)+(w−1)²/w=w−1`. OK.

### Numerical, from scratch (all PASS)
* `scripts/review_o10_q.py` (exact Fractions): all 127 hypergraphs on 3
  vertices × 3 boundary weightings, plus 40000 random hypergraphs (n≤7,
  1/3 of them graphs: triangles, stars, hubs), rational weights pushed to
  `max w_E=2`: Lemma 3.2 identity exact (n≤6), `|Θ|≤∏_𝓜(w−1)` and
  `Q≤∏_𝓜(w−1)` for **every** matching 𝓜 (enumerated). Max Q = 1 (single edge).
* `scripts/review_o10_cover.py` (exact Fractions, q∈{2,3}, n≤4, 20000
  systems incl. equal supports): `G_F ≤ E_xQ(𝓗(x)) ≤ 1` always.
* `scripts/review_o10_c1.py` (float, q∈{2,3,4}, n≤7, product ≤5000):
  identity `Σ_Vμ^V‖L_VF‖² = Σ_Uλ^U‖F^{=U}‖²` (Efron–Stein by explicit
  inclusion–exclusion) to 1e−15; 3000 random systems with very
  non-uniform λ normalised to `max w_E=2`: max G=0.99971; 300 hill-climbs
  (60 steps, event add/delete/mutate + λ jitter): max G=0.99991, attained
  by a single full-width event. No counterexample.
