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

**2.2 Hypergraph lemmas** (`review_o10b_hyper.py 2000 7`, own brute force,
`n≤6` vertices, ≤5 edges, random weights with all `w_E≤2`, 60% of cases at
the boundary `max w_E=2`): `|N(V)|=|τ̂(V)|` exact; Lemma 3.2 identity
`Q=E_PΘ(𝓗_P)²` (exact sum over all P) to 1.1e−15; Lemma 3.3
`|Θ(𝒞)|−∏_𝓜(w−1) ≤ 2.7e−15` (rounding at equality cases) over every matching
𝓜 and random 𝒞⊇𝓜; Thm 3.4 `Q−∏_𝓜(w−1) ≤ 4.4e−16`; Lemma 3.1
`G_F−E_xQ(𝓗(x)) ≤ −3e−5 < 0` on 500 random single-value systems with
**biased** measures on alphabets {2,3} (outside the document's uniform
hypothesis — confirms D1 below), and `E_xQ ≤ 1` there. All consistent.

**2.3 Adversarial search** (`review_o10b_hill.py`, simulated-annealing-style
hill climbing over term sets, literals, widths, and — in modes bb/qa —
per-coordinate measures; `review_o10b_random.py`, 1200 random DNFs on
n∈{14,15,16}, up to 200 width-≤k terms drawn from a small variable pool to
force heavy overlap, 40% p-biased). Results (`reviews/agent-reports/r38b_hill.txt`):

| setting | max G (C-1: ≤1) | max tail ratio (Cor 4.1: ≤1) | max ratio for t≥2k−1 |
|---|---|---|---|
| uniform bits, n=10–12, k=1..4 | 0.930 (k=3, single AND) | 0.5 | 0.25 (k=1,2), 0.089 (k=3), 0.024 (k=4) |
| p-biased bits (measure climbed), n=9–10 | 1 − O(ε), excess ≤ +1.6e−15 | 0.354 | 0.078 (k=3) |
| q-ary (q≤4) random measures, n=6–7 | 1 − O(ε), excess ≤ +2.2e−15 | 0.4995 | 0.069 (k=3) |
| random overlapping DNFs n=14–16 | 0.999999 | 0.5 | 0.295 |

The G-maximisers are always a single event whose fixed values have
vanishing probability (`G=1−π(2−∏_v(λ−(λ−1)p_v))↑1`), i.e. C-1 is tight only
in this degenerate limit, as the document says. Excesses of order 1e−15
are float rounding. **No violation of C-1 or Cor 4.1 found.**

## 3. Consistency with lower bounds; sharpness of the rate (own analysis)

**3.1 The exponential rate `2^{−1/k}` of Cor 4.1 is SHARP over general
product spaces** (stronger than the document's "tail rate not claimed
sharp"). Family: m disjoint width-k events, each fixing values of
probability p (q-ary uniform with p=1/q, or p-biased bits). With
`π=p^k`, `F=∏(1−A_i)` and the block polynomial
`B(z)=(1−π)²+π²((1+z(1−p)/p)^k−1)`, the level generating function is
`B(z)^m`. As `p→0` with `S:=mπ` fixed, the top component of a block has
mass `π(1−p)^k≈π` and lower components `O(πkp)`, so the number J of
"active" blocks is ≈ `Po(S)` tilted by `e^{−S}`, degree = kJ, and
`energy(F; jk−1)·2^{j} ≈ Σ_{i≥j}2^{j−i}P(Po(2S)=i)·… → max_S ≈ 2/√(2πj)`.
Exact computation (`review_o10b_sharp.py`, float; one cancellation-affected
cell rechecked with 60-digit mpmath in `review_o10b_sharp_mp.py`; output
`reviews/agent-reports/r38b_sharp.txt`): `max_m energy(t)·2^{(t+1)/k}` at
`t=jk−1`, p=10⁻³: k=1: 0.407, 0.296, 0.224, 0.166, 0.135 for j=2,5,10,20,30;
k=3, j=30: 0.131; times `√(2πj)` it tends to ≈1.8–1.9 (→2). So
`sup energy(t)·2^{(t+1)/k} ≍ (t/k)^{−1/2}` along this family: the base
`2^{1/k}` cannot be improved, only a `√(t/k)` factor could be gained.
Cor 4.1 is consistent with (and almost matched by) this lower bound.

**3.2 Uniform Boolean cube.** There the rate is not attained: for p=1/2
(tribes-like disjoint ANDs) the normalised tail decays (k=1, j=30: 0.0000;
x√(2πj)→0). The best Boolean family found is OR of s disjoint k-parities
(`F=∏(1+χ_{B_i})/2`): `energy(jk−1)=Σ_{i≥j}C(s,i)4^{−s}`, maximised over s at
`≍3^{−j}` (`Σ_sC(s,j)4^{−s}=(4/3)3^{−j}`). So on `{±1}^n` uniform the truth
for width-k DNFs lies between rates `3^{−t/k}` (this example) and `2^{−t/k}`
(Cor 4.1): ε-concentration degree between `k·log₃(1/ε)` and `k·log₂(4/ε)`.
The hill climbs (§2.3) never beat the parity family. Nothing here
contradicts any known Boolean lower bound that I know of (LMN/Mansour-type
upper bounds `O(w log 1/ε)` are of course consistent).

**3.3 Corollaries as sanity checks.** From `G_F(2^{1/k})≤1` and `Σ_U‖F^{=U}‖²=E F`:
`Σ_U(2^{|U|/k}−1)‖F^{=U}‖² ≤ P(h)`, hence for ±1 `g`: total influence
`I[g] ≤ (4k/ln 2)·P(h) ≈ 5.77k·P(h)` — consistent with (weaker than) the
known `I ≤ 2w` for width-w DNFs (Boppana; from memory). Tribes: `I≈w ln2`.
