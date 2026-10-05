# R38b — second independent hostile review of POINTWISE_OMEGA10.md (focus: Cor 4.1)

Reviewer branch: `side-agent/review-omega10b`. Document reviewed: `POINTWISE_OMEGA10.md`
as merged from `side-agent/esw-suppression` (HEAD 9cc78e7). The first review
(R38a, `reviews/pointwise-omega10-review.md`) was deliberately NOT read before
this review's own derivation and numerics were complete.

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 3.1 (cover bound) | (pending) |
| Lemma 3.2 (polarization) | (pending) |
| Lemma 3.3 (matching bound for Θ) | (pending) |
| Thm 3.4 (Q, Q′, QM) | (pending) |
| Cor 3.5 (C-1) | (pending) |
| Cor 4.1 (energy concentration) | (pending) |

## 1. Independent re-derivation (own notation)

Setup. `Ω=∏_v Ω_v` with an arbitrary product probability measure `π=⊗π_v`
(the document assumes uniform; see D1). `L_v=I−E_v` are commuting orthogonal
projections on `L²(π)`, `L_V=∏_{v∈V}L_v`, `L_V f=Σ_{U⊇V}f^{=U}`. With
`μ_v=λ_v−1≥0`, `⊗_v(I+μ_vL_v)=Σ_V μ^V L_V`, so
`G_F=Σ_V μ^V⟨F,L_VF⟩=Σ_Vμ^V‖L_VF‖²` (identity (i)) — checked.

**Lemma 3.1.** Fix V and `y=x_{V^c}`. Since `L_V` only acts on V-coordinates,
`(L_VF)(·,y)=L_V[F(·,y)]` and for a function `g` of `x_V` only, `L_Vg=g^{=V}`.
`g=F(·,y)=∏_{E: E|_{V^c} holds at y}(1−1[x_{E∩V}=c_E])`. Inclusion–exclusion:
`g=Σ_𝒥(−1)^{|𝒥|}1[∩_{E∈𝒥}{x_{E∩V}=c_E}]`; each term is the indicator of a
(possibly empty) cylinder on `S_𝒥=∪_{E∈𝒥}(E∩V)`, killed by `L_V` unless
`S_𝒥=V`, in which case it is a point mass `1_σ` (or 0 if inconsistent).
So `g^{=V}=L_V c_y`, `c_y(σ)=Σ{(−1)^{|𝒥|}: S_𝒥=V, all E∈𝒥 hold at (σ,y)}`,
and `‖L_Vc_y‖²≤‖c_y‖²_{L²(π_V)}` because `L_V` is an orthogonal projection
**for any product measure** (not only uniform). `c_y(σ)=N_{𝓗(σ,y)}(V)` where
`N_𝓗(V)=Σ_{𝒥⊆𝓗,∪𝒥⊇V}(−1)^{|𝒥|}`; `N=0` if some `E∈𝓗` misses V
(toggle E). Möbius check: `τ_𝓗(R)=Σ_𝒥(−1)^{|𝒥|}1[R∩∪𝒥=∅]` and the Möbius
transform of `R↦1[R∩U=∅]` at V is `(−1)^{|V|}1[V⊆U]`, so
`τ̂(V)=(−1)^{|V|}N(V)` — checked. Duplicate events (same cylinder twice) do
not matter: `N` depends only on `τ`, which is unchanged. **SOUND.**

**Lemma 3.2.** `Q_μ=Σ_Vμ^Vτ̂(V)²=E[T(p)²]` for any independent mean-0,
variance-`μ_v` `p_v` (orthogonality of distinct multilinear monomials).
With `p_v∈{1,−μ_v}`, `P(p_v=1)=μ_v/λ_v`: mean `μ/λ−μ·(1/λ)=0`, variance
`μ/λ+μ²/λ=μ` ✓. In the basis `T=Σ_Rτ(R)∏_Rp∏_{R^c}(1−p)` (equal to
the Möbius form) the factor `1−p_v=0` on P forces `R⊇P`; for `v∉P`,
`p_v=−μ_v`, `1−p_v=λ_v`. `τ(P∪B)=τ_{𝓗_P}(B)` for `B⊆P^c` ✓, and
`Σ_{B⊆P^c∖U}(−μ)^Bλ^{P^c∖B}=λ^U∏_{P^c∖U}(λ−μ)=λ^U` ✓. **SOUND.**

**Lemma 3.3.** Split `𝒥=𝒥_a⊔𝒥_b` (edges avoiding / containing v). If
`𝒥_b≠∅`, `λ^{∪𝒥}=λ_v·λ^{∪(𝒥/v)}`. Hence `Θ(𝒞)=Θ(𝒞−v)+λ_v[Θ(𝒞/v)−Θ(𝒞−v)]`
✓. Induction on |vertex set|; base: all edges empty → `Θ∈{0,1}` ✓.
Weights in `𝒞/v`, `𝒞−v` stay `≤2` ✓ (needs `λ_v≥1`). `𝓜−E_0+(E_0∖v)` is a
matching of `𝒞/v` ✓ (if `E_0={v}`, `∅∈𝒞/v` so `Θ(𝒞/v)=0` and the bound
`(w_{E_0}/λ_v−1)Π′=0` is exact). Triangle inequality:
`λ_v(w/λ_v−1)Π′+μ_vΠ′=(w−1)Π′` ✓ (uses `μ_v≥0`). Edge-free/`𝓜=∅` cases ✓.
**SOUND.**

**Thm 3.4.** `Θ(𝓗_P)²≤∏_{E∈𝓜, E∩P=∅}(w_E−1)²`; `P(E∩P=∅)=∏_E(1/λ_v)=1/w_E`,
independent over disjoint E; `(1−1/w)+(w−1)²/w=(w−1)` ✓. **SOUND.**

**Cor 3.5 / Cor 4.1.** `G_F≤E_xQ_μ(𝓗(x))≤1`. With `λ_v≡2^{1/k}`, `|E|≤k ⇒
w_E≤2`; `λ^{t+1}·Σ_{|U|>t}‖F^{=U}‖²≤G_F≤1` ✓; `f=1−F` has the same
components for `U≠∅` ✓. Boolean ±1 form: `g=1−2h=2F−1`, `ĝ(U)²=4‖F^{=U}‖²`,
so `W^{>t}[g]≤4·2^{−(t+1)/k}` for every width-k DNF and every product
measure (p-biased included). **SOUND** (derivation independently reproduced;
numerics in §2).

## 2. From-scratch numerics

Library `scripts/review_o10b_lib.py` (own code): exact Efron–Stein level
weights on an arbitrary finite product probability space, by a degree-tagged
tensor sweep. Validated in `scripts/review_o10b_sanity.py` against a
brute-force Walsh transform (uniform bits, diff 0) and against brute-force
inclusion–exclusion Efron–Stein for a biased q-ary space (diff 4e−17).
"tail ratio" := `max_t energy(F;t)·2^{(t+1)/k}` (Cor 4.1 ⟺ ratio ≤ 1);
also `G:=G_F(2^{1/k})` (C-1 ⟺ G ≤ 1, stronger).

**2.1 Structured Boolean DNFs, uniform bits, n ≤ 16** (`review_o10b_families.py`,
output `reviews/agent-reports/r38b_families.txt`, 127 functions): tribes
(w≤5, all s with ws≤16), thresholds `[|x|≥k]` (all k-ANDs, n∈{8,12,14},
k≤6), `[|x|≥k or |x|≤n−k]`, OR of s disjoint k-parities, parity_n as a
2^{n−1}-term DNF (n≤12), majority (n≤15, k=(n+1)/2), multiplexers,
sunflowers. **Max G = 0.9822** (single AND of width 5; equals
`1−2^{−5}(2−((1+2^{1/5})/2)^5)=0.98223`, §2's single-event formula), **max tail ratio = 0.5**
(attained by parity_k at t=k−1 and a single literal). No violation; the
Boolean bound has a factor ≥2 slack on all of these.
