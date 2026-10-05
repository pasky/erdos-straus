# The energy switching lemma: suppression and a generating-function route (task O38)

Task O38 (branch `esw-suppression`). Labels as in the house rules. ES is not
touched; nothing below bears on whether `W(p)<∞`. Notation: PO =
`POINTWISE_OMEGA.md`, O2, O8, O9 likewise; `𝓛=log T`.

**Status: checkpoint 2 — Conjecture Q / C-1 PROVED (§3.1); self-review R38a and parent review R38 (`reviews/pointwise-omega10-review.md`): all claims SOUND, no FATAL/MAJOR; R38 MINOR 1–5 applied; second review R38b (`reviews/pointwise-omega10-review-2.md`): all SOUND, D1–D4 applied.**

## 0. Notation

A *single-value system* on a product space `Ω=∏_v[q_v]`. §§1–2 use the
uniform measure; from §3 on, any product probability measure `π=⊗π_v` is
allowed (R38b D1).
events `E` (cylinders) fixing `X_v=c_E(v)` for `v∈supp E`; `A_E=1_E`;
`h:=1[some event occurs]`, `F:=1−h`; `w_E:=∏_{v∈supp E}λ_v` for weights
`λ_v≥1`. Efron–Stein decomposition `f=Σ_U f^{=U}`, `L_v:=I−E_v`,
`L_V:=∏_{v∈V}L_v` (so `L_Vf=Σ_{U⊇V}f^{=U}`), and

```
Λ = Λ_λ := ⊗_v (I + (λ_v−1)L_v),     G_f(λ) := ⟨f,Λf⟩ = Σ_U (∏_{v∈U}λ_v)·‖f^{=U}‖².
```

`G` is the *energy generating function*: if all `λ_v=λ`, then
`energy(f;t) ≤ G_f(λ)·λ^{−(t+1)}`, and with weights,
`Σ_{U: Σ_{v∈U}log λ_v > τ}‖f^{=U}‖² ≤ e^{−τ}G_f(λ)`.

## 1. Independent check of O9 §4 (Lemma 4.1, Cor 4.2)

*Lemma 4.1: correct.* `F^{=U}=∏_i(1−A_i)^{=U∩E_i}` holds for disjoint
supports (and `F^{=U}=0` if U meets no support only when U≠∅ contains an
unused coordinate — harmless). `‖A_i^{=E_i}‖²=∏_{ℓ}q^{−1}(1−q^{−1})` is right
(A_i is a product of independent literal indicators). The limit is a lower
bound obtained by truncating to finitely many j, so no interchange issue.

*Cor 4.2, bullet 1: correct* (Choi: median of `Po(S)` is `≥S−log 2`, so
`Pr[Po(S)≥S−1]≥1/2`). Vacuous for `S<1`.

*Cor 4.2, bullet 2: correct as a necessary condition, slightly mis-described.*
EL is `energy(F^{(j)};t) ≤ e^{−3S}/(100m²(S+1))`; in the limit `q→∞` with S
fixed, `m=S/π→∞`, so EL becomes *stronger* than `Pr[Po(S)>t/k] ≤ e^{−2S}`
(it eventually fails for every `t<km`). The derived `t ≥ (c_*−o(1))kS`,
`c_*≈3.59`, is therefore a valid necessary condition. (`c_*log c_*−c_*+1=2`
checked: `c_*=3.5911`.)

*Cor 4.2, the "1/6 ceiling": arithmetic slip and a scope caveat.*
1. With `z=𝓛²`, `k=𝓛/(2log𝓛)`, `S*≍𝓛^4log𝓛`: `kS*·log z ≍ 𝓛^5log𝓛` and
   `kS*·𝓛 ≍ 𝓛^6` (not `𝓛^6/log𝓛`). The conclusion "1/6" is unaffected.
2. The floor counts **coordinates** at cost `≤𝓛` each (O9 Thm 2.2:
   `log Z ≤ log Q_Π+2(3k+2d+1)𝓛`). The true cost of a junta set U is
   `Σ_{ℓ∈U}log(modulus used at ℓ)`. In the ES system an event with support
   `supp E` is a class mod its rough part `r_E ≤ T`, so the lower-bound
   juntas of Lemma 4.1 (unions of j event supports) cost
   `≤Σ log r_E ≤ j𝓛`, not `jk𝓛`. Lemma 4.1 then gives the floor
   `≍S·𝓛` for the *modulus* (if the junta function only reads `X_ℓ` to the
   precision the events use), i.e. `≍𝓛^5log𝓛` under ET, not `𝓛^6`.
   So "1/6 is the ceiling" is right for arguments that charge every junta
   coordinate `≍𝓛` (as ESW in coordinate count does); an argument with
   **modulus-weighted** energy tails could in principle go below
   (towards 1/5, if also `log Q_Π≪𝓛^5`). §2 below is such an argument.
   (Precision refinement: units mod `ℓ^a` ≅ units mod ℓ × `(ℤ/ℓ)^{a−1}` by
   base-ℓ digits, and the Haar measure is the product measure, so an event
   fixing `X_ℓ mod ℓ^b` is single-value on the first b digit coordinates;
   each digit coordinate costs `log ℓ`.)

No error affecting O9 §§1–3 or the statements of Lemma 4.1 was found.

## 2. The generating function and the one-step monotonicity conjecture

**Why G.** If `G_F(λ) ≤ 1` for weights `λ_v := 2^{log m_v/𝓛}` (`m_v` = the
modulus that coordinate v contributes), then for every τ

```
Σ_{U: log m_U > τ} ‖F^{=U}‖²  ≤  2^{−τ/𝓛}·G_F(λ)  ≤  2^{−τ/𝓛},     m_U := ∏_{v∈U} m_v.
```

So the Efron–Stein truncation of `F^{(j)}` at modulus `e^τ` has ℓ²-error
`≤ e^{−3S}/(100m²(S+1))` (O8 EL) as soon as `τ ≥ 𝓛·log₂(100m²(S+1)e^{3S})
≍ 𝓛(S+k𝓛)`. This is a **modulus-weighted** EL, with no bit factor b and no
width factor k: compare O8 Lemma 6.1, `log(modulus) ≍ k·b·k_0·𝓛 ≍ k𝓛²S`.
Uniform weights `λ_v=2^{1/k}` give ESW-type coordinate tails
`energy(F;t) ≤ 2^{−t/k}G_F`.

**Single events.** For a cylinder C on support E (`π=P(C)`):
`G_{1_C}(λ) = π·∏_{v∈E}(λ_v−(λ_v−1)/q_v) ≤ π·w_E` and
`G_{1−1_C} = 1−2π+G_{1_C} ≤ 1−π(2−w_E)`. So `w_E≤2` is exactly the threshold
for `G≤1` (O9 Lemma 4.1's disjoint systems: `G=∏_i(1−π_i(2−w̃_i))`).

**Useful identities (PROVED, standard).** (i) `G_F = Σ_V ∏_{v∈V}(λ_v−1)·‖L_VF‖²`.
(ii) With `h=1−F`: `G_F = 1−2E h+G_h`, so `G_F≤1 ⟺ G_h ≤ 2E h`.
(iii) `G_F = E_x[F(x)·(ΛF)(x)]`, and `ΛF(x)` is the "probability" of no event
under the signed product measure `ν_x` with `ν_x(x_v)=λ_v−(λ_v−1)/q_v`,
`ν_x(b)=−(λ_v−1)/q_v` (`b≠x_v`). (iv) For `λ_v∈[1,2]`,
`Λ = E_V[⊗_{v∈V}(2I−E_v)]`, V random with `P(v∈V)=λ_v−1` independently,
i.e. G at general weights is an average of G at weights `{1,2}` (random
restrictions).

**Conjecture MONO (EVIDENCE, no counterexample found).** For every
single-value system with good-indicator F and every further cylinder A
(weight `w_A`), `G_{F(1−A)}(λ) ≤ G_F(λ)·(1+P(A)(w_A−2)_+)`.

Consequences (if MONO holds): by induction from `G_1=1`,

```
(C-exp)  G_F(λ) ≤ ∏_E (1+P(E)(w_E−2)_+) ≤ exp(Σ_E P(E)(w_E−2)_+),
(C-1)    G_F(λ) ≤ 1  whenever every event has w_E ≤ 2.
```

Evidence (`scripts/omega10_*.py`, exact Efron–Stein on `[q]^n`, `q≤5`, `n≤8`):
* `omega10_mono.py`: 2000 random (system, A, λ) triples, `λ_v∈[1,2]` and
  `[1,3]`: max of `G_{F(1−A)}/(G_F(1+P(A)(w_A−2)_+)) − 1` is `0` (attained
  when A is redundant).
* `omega10_cexp.py`: 1600 random systems incl. full coincidence systems
  (`X_i=X_j=c`, all pairs and values), `λ_v∈[1,3]`: C-exp never violated.
* `omega10_bool.py`, `omega10_gen.py` (hill-climbing for max `G_F` with
  `λ^k=2`, q=2 up to n=10 and q≤6): the maximiser is always a single event.
* C-1 is false beyond its range: q=2, k=1, `λ=4`, OR of n literals:
  `G_F=(5/4)^n`. And the **pointwise** versions fail
  (`omega10_pointwise.py`: `ΛF(x)≥−1` on bad x fails), so any proof must
  average over x.
* A natural generalisation is false: for `ψ=g·F` (bad for one system, good
  for another, disjoint supports) `G_ψ=G_g G_F` may exceed `E[ψ w_min]`.

**MONO is FALSE (PROVED by example; `scripts/omega10_monocex.py`).** Take n
coordinates on `[q]`, `λ_v=2^{1/n}` (so every full-width cylinder has `w=2`),
the system of all full-width cylinders with an even number `≥2` of
mismatches against `c=0`, and `A={x=0}` (`w_A=2`). Then `G` increases:
`q=8,n=2: 0.31571→0.31757`; `q=5,n=3: 0.75406→0.75467`. Mechanism (exact):
writing `F=u+r` with `u=F·1_A`, `G_F−G_{F(1−A)} = ⟨u,Λu⟩+2⟨u,Λr⟩`, and the
adversarial `r=1[Λu<0]` off A gives `π[a−(b−1)]` for `φ≡1`, with
`a=∏(1+θ_v)`, `b=∏(1+2θ_v)`, `θ_v=(λ_v−1)(1−1/q_v)`; for `a=2` spread over
many coordinates `b≈4>a+1`. (For a single coordinate `a=1+θ≥2θ=b−1`, and a
direct computation proves MONO when `|supp A|=1`: `G_F−G_{F(1−A)} =
π F(c)[λF(c)−μ(2EF−F(c)π)]≥0` for n=1, boolean F.) In all these examples
`G_F<1` still: C-1 and C-exp are **not** refuted, but a proof cannot be a
one-event-at-a-time monotonicity.

## 3. Reduction of C-1 to a pointwise hypergraph inequality

For a finite hypergraph 𝓗 (a set of nonempty vertex sets) let
`τ_𝓗(R):=1[R∩E≠∅ ∀E∈𝓗]` (transversal indicator, `R⊆` vertices),
`τ̂_𝓗(V):=Σ_{R⊆V}(−1)^{|V∖R|}τ_𝓗(R)` its Möbius transform, and

```
Q_μ(𝓗) := Σ_V μ^V τ̂_𝓗(V)²      (μ^V:=∏_{v∈V}μ_v;  Q_μ(∅)=1).
```

Equivalent forms (PROVED, by expanding `τ=∏_E(1−∏_{v∈E}(1−r_v))=Σ_{𝒥⊆𝓗}(−1)^{|𝒥|}∏_{v∈∪𝒥}(1−r_v)`):
`|τ̂(V)| = |N(V)|`, `N(V):=Σ_{𝒥⊆𝓗: ∪𝒥⊇V}(−1)^{|𝒥|}` (signed count of
covers of V), and with `λ=1+μ`

```
Q_μ(𝓗) = Σ_{𝒥,𝒦⊆𝓗} (−1)^{|𝒥|+|𝒦|} ∏_{v∈(∪𝒥)∩(∪𝒦)} λ_v .
```

Examples: one edge E: `Q=w_E−1`; disjoint edges: `Q=∏(w_{E_i}−1)`.

**Lemma 3.1 (cover bound; PROVED).** For every single-value system on a
finite product probability space `(∏_v[q_v], ⊗π_v)` and all
`λ_v≥1` (`μ_v=λ_v−1`; `E_v`, `L_v`, `f^{=U}` taken in `L²(⊗π_v)`),

```
G_F(λ) ≤ Γ := E_x[ Q_μ(𝓗(x)) ],     𝓗(x) := {supp E : E holds at x}.
```

*Proof.* By §2 (i), `G_F=Σ_Vμ^V‖L_VF‖²` and
`‖L_VF‖² = E_{x_{V^c}}‖(F_{x_{V^c}})^{=V}‖²`, where `g:=F_{x_{V^c}}` is the
good-indicator on `Ω_V` of the restricted system (events whose part off V
holds at `x_{V^c}`, restricted to `E∩V`). Expand
`g=Σ_𝒥(−1)^{|𝒥|}A_𝒥` (A_𝒥 = indicator of the intersection cylinder). A
cylinder whose support is a proper subset of V has zero top component, and a
cylinder with support V is a point indicator `1_σ`, with
`(1_σ)^{=V}=L_V1_σ=∏_{v∈V}(1[x_v=σ_v]−π_v(σ_v))`. The cylinders with support
exactly V sum to the function `c(x):=Σ_{𝒥: supp A_𝒥=V, value x}(−1)^{|𝒥|}` on
`Ω_V` (as functions, `Σ_σ c(σ)1_σ=c`). So `g^{=V}=L_Vc` and
`‖g^{=V}‖²=‖L_Vc‖²≤‖c‖²=E_σc(σ)²` (`L_V` is an orthogonal projection
in `L²(⊗π_v)`; σ distributed by `π_V`).
*Degenerate cases (R38b D4a).* If the cylinders of 𝒥 are inconsistent,
then `A_𝒥=0` and 𝒥 contributes to no σ. Duplicate events (equal
cylinders) are allowed. A class of m equal events contributes
`Σ_{j≥1}C(m,j)(−1)^j=−1`, exactly like a single event, so `c(σ)=±N(V)` still
holds with 𝓗(x) taken as a set.
Writing `x=(σ,x_{V^c})`, the 𝒥 in `c(σ)` are exactly the subfamilies of
events holding at x whose traces on V cover V, so `c(σ)=±N_{𝓗(x)}(V)`
(an event avoiding V that holds at x makes `c=0`, consistently with
`N(V)=Σ_{R⊆V}(−1)^{|R|}τ(R)=0` when some edge misses V). Summing,
`G_F ≤ Σ_Vμ^V E_x N_{𝓗(x)}(V)² = E_x Q_μ(𝓗(x))`. ∎

Note the **suppression is built in**: `N_{𝓗(x)}(V)=0` whenever some event
holding at x avoids V (this is O9 §4.3's condition (b), now exact). For
O9's hub (core H plus M completions at distinct coordinates) one gets
`|N|≤1` and a contribution `O(P(H)·min(1,M/q))=O(S_hub)`, with no
`e^{M/q}`.

**Conjecture Q (now PROVED, Thm 3.4 below).** If every `E∈𝓗` has `w_E=∏_{v∈E}(1+μ_v)≤2`,
then `Q_μ(𝓗)≤1`.

By Lemma 3.1, Conjecture Q implies C-1 (`G_F≤1` for every single-value
system with all `w_E≤2`; no mass, codegree or quarantine hypothesis), since
`𝓗(x)` only contains supports of events.

Evidence: `scripts/omega10_q.py` (20000 random weighted hypergraphs, n≤10),
`scripts/omega10_qhc.py` (hill-climbing, n=7 and n=10): max `Q=1`, attained
by a single edge with `w=2`. `scripts/omega10_gamma.py`: `G_F≤Γ` in 300
random systems (as proved), and `Γ≤0.992` whenever `w≤2`.
Two facts already PROVED: (a) weights `μ_v∈{0,1}` (each edge meets
`Ξ:={μ=1}` at most once): `Q=1[every edge meets Ξ]`; (b) by multilinearity,
`Q_μ(𝓗)=E_Ξ[Q_1(𝓗|_Ξ)]` with Ξ random, `P(v∈Ξ)=μ_v` independently
(valid for `μ_v≤1`), `𝓗|_Ξ` the traces, `Q_1` the unweighted sum
(`=0` if a trace is empty).
The naive unweighted bound `Q_1(𝓗)≤min_E(2^{|E|}−1)` is **false**
(`scripts/omega10_q1.py`: ratios up to 423, driven by singleton edges), so
the averaging over Ξ is essential.

**Stronger form Q′ (now PROVED, Thm 3.4).** Under the same hypothesis,
`Q_μ(𝓗) ≤ min_{E∈𝓗} w_E − 1` (`scripts/omega10_qmin.py`, 20000 random
weighted hypergraphs, no violation beyond rounding). Q′ is the hypergraph
analogue of "C-min" (`G_h ≤ E[h·w_min]`, also numerically supported in §2).
Two edges A, B (PROVED by direct expansion): with `a=λ^{A∖B}`,
`b=λ^{B∖A}`, `c=λ^{A∩B}`, `Q = c(a−1)(b−1)+c−1`, and under `ac,bc≤2`
one checks `Q ≤ c·min(a,b)−1 ≤ 1`.

**Vertex recursion (PROVED).** For a vertex v, with `𝓐:=𝓗−v` (edges not
containing v) and `𝓑:=𝓗/v={E∖{v}}` (contraction),
`N_𝓗(V∪v) = N_𝓑(V)−N_𝓐(V)` for `v∉V`, hence

```
Q_μ(𝓗) = Q_μ(𝓑) + μ_v·Σ_V μ^V (N_𝓑(V)−N_𝓐(V))².
```

`Q_μ` is a multilinear polynomial in μ with **nonnegative** coefficients
`N(V)²`, so it suffices to check the boundary of the weight region. The
naive inductive step (v in a minimum-weight edge, Q′ for `𝓗/v`) would need
`Σ_Vμ^V(N_𝓑−N_𝓐)² ≤ min_{L∈link(v)} w_L`, which is **false** in general
(random search: e.g. `𝓐={01}`, link `{0},{1}`), so a proof must use the
slack in `Q(𝓗/v)`. (Resolved in §3.1.)

**Matching forms.** Strongest form tested, *Conjecture FM* (EVIDENCE; open): if
all `w_E≤2`, then `Q_μ(𝓗) ≤ ∏_E (w_E−1)^{y_E}` for every fractional matching
y (`y≥0`, `Σ_{E∋v}y_E≤1`). `scripts/omega10_fm.py` (LP over y; 20000 random
weighted hypergraphs, n≤9): never violated, and **equality** (to `10^{−14}`)
is frequent. Its integral case, *Conjecture QM*: `Q_μ(𝓗)≤∏_{E∈𝓜}(w_E−1)` for
every matching `𝓜⊆𝓗` (now PROVED, Thm 3.4), contains Q (𝓜=∅), Q′ (one edge) and the disjoint
product (equality).
*Induction attempt for QM (PROVED reduction).* Take `E_0∈𝓜`, `v∈E_0`. In
the vertex recursion write `X:=Σ_Vμ^V N_𝓐(V)N_𝓑(V)`; then
`Q(𝓗)=λ_vQ(𝓑)+μ_v(Q(𝓐)−2X)`. Applying QM to 𝓑 (matching
`𝓜−E_0+{E_0∖v}`) and to 𝓐 (matching `𝓜−E_0`) gives
`Q(𝓗) ≤ (w_{E_0}−1)Π′ − 2μ_vX`, `Π′:=∏_{𝓜−E_0}(w−1)`. So QM follows by
induction **whenever X≥0**. But X<0 occurs (triangle `{01},{0v},{1v}`,
`X≈−0.17` at `w=2`; `scripts/omega10_*` search), where QM survives only
through slack in the bounds for `Q(𝓐)`, `Q(𝓑)`. (Superseded by §3.1: the right induction is on Θ, not on Q.)

### 3.1 Proof of Conjecture Q (PROVED)

For a finite multiset 𝒞 of vertex sets ("edges", possibly empty) and
weights `λ_v≥1`, put

```
Θ_λ(𝒞) := Σ_{𝒥⊆𝒞} (−1)^{|𝒥|} λ^{∪𝒥}        (λ^U:=∏_{v∈U}λ_v; Θ(∅)=1).
```

**Lemma 3.2 (polarization; PROVED).** Let `μ_v=λ_v−1≥0` and let P be a random
vertex set with `P(v∈P)=μ_v/λ_v` independently. Then for every hypergraph 𝓗

```
Q_μ(𝓗) = E_P[ Θ_λ(𝓗_P)² ],     𝓗_P := {E∈𝓗 : E∩P=∅}.
```

*Proof.* Let `T(p):=Σ_Vτ̂(V)p^V` be the multilinear extension of `τ=τ_𝓗`.
If the `p_v` are independent with mean 0 and variance `μ_v`, then distinct
monomials are orthogonal and `E[T(p)²]=Σ_Vμ^Vτ̂(V)²=Q_μ(𝓗)`, whatever the
law of `p_v`. Take `p_v=1` with probability `μ_v/λ_v` and `p_v=−μ_v`
otherwise (mean `μ/λ−μ/λ=0`, variance `μ/λ+μ²/λ=μ`); `P:={p_v=1}`. Since
`T(p)=Σ_Rτ(R)∏_{v∈R}p_v∏_{v∉R}(1−p_v)`, only `R⊇P` survive, and with
`R=P∪B`, `B⊆P^c`: `T=Σ_{B⊆P^c}(−μ)^Bλ^{P^c∖B}τ(P∪B)`. Here
`τ(P∪B)=τ_{𝓗_P}(B)=Σ_{𝒥⊆𝓗_P}(−1)^{|𝒥|}1[B∩∪𝒥=∅]` (inclusion–exclusion),
and `Σ_{B⊆P^c}(−μ)^Bλ^{P^c∖B}1[B∩U=∅]=λ^U∏_{v∈P^c∖U}(λ_v−μ_v)=λ^U` for
`U⊆P^c`. Hence `T=Θ_λ(𝓗_P)`. ∎
(`scripts/omega10_qtheta.py`: exact enumeration, 300 random cases,
`μ` up to 3, max discrepancy `5·10^{−13}`.)

**Lemma 3.3 (matching bound for Θ; PROVED).** If every edge of 𝒞 has
`w_E=λ^E≤2`, then for every matching `𝓜⊆𝒞` (pairwise disjoint edges)

```
|Θ_λ(𝒞)| ≤ ∏_{E∈𝓜}(w_E−1)          (in particular |Θ_λ(𝒞)|≤1).
```

*Proof.* Deletion–contraction: for a vertex v let `𝒞−v` be the edges not
containing v and `𝒞/v:={E∖{v}:E∈𝒞}`. Splitting `𝒥` according to whether
it contains an edge through v,

```
Θ(𝒞) = Θ(𝒞−v) + λ_v[Θ(𝒞/v) − Θ(𝒞−v)] = λ_v Θ(𝒞/v) − μ_v Θ(𝒞−v).
```

Both families again have all weights `≤2` (`w_{E∖v}=w_E/λ_v` for `E∋v`, unchanged otherwise), and
vertex sets smaller by one. Induct on `|∪𝒞|`, the size of the ground set
actually used (R38b D4b). The base case `|∪𝒞|=0` is a family of empty
edges: `Θ=1` if `𝒞=∅`, and `Θ=0` otherwise.
If `∅∈𝒞`, then `Θ(𝒞)=0` (toggling the empty edge pairs the terms), so the
claim holds. If `𝒞=∅`, `Θ=1` and `𝓜=∅`. If `𝓜=∅` and `𝒞≠∅`, it
suffices to prove the bound for `𝓜={E}`, since `w_E−1≤1`. So let
`E_0∈𝓜` be nonempty, `v∈E_0`, `Π′:=∏_{𝓜∖E_0}(w−1)`. In `𝒞/v` the family
`𝓜∖{E_0}∪{E_0∖v}` is a matching, so `|Θ(𝒞/v)|≤(w_{E_0}/λ_v−1)Π′`
(if `E_0={v}` this reads `0`, consistent with `∅∈𝒞/v`). In `𝒞−v` the
family `𝓜∖{E_0}` is a matching, so `|Θ(𝒞−v)|≤Π′`. Therefore
`|Θ(𝒞)| ≤ (w_{E_0}−λ_v)Π′+μ_vΠ′ = (w_{E_0}−1)Π′`. ∎

**Theorem 3.4 (Conjectures Q and QM; PROVED).** If every edge of 𝓗 has
`w_E≤2`, then `Q_μ(𝓗) ≤ ∏_{E∈𝓜}(w_E−1)` for every matching `𝓜⊆𝓗`; in
particular `Q_μ(𝓗)≤1` and `Q_μ(𝓗)≤min_E w_E−1`.

*Proof.* Lemma 3.2, then Lemma 3.3 for `𝓗_P` with the matching
`𝓜∩𝓗_P`. The edges of 𝓜 are disjoint, so the events `{E∩P=∅}` are
independent, with probability `∏_{v∈E}λ_v^{−1}=1/w_E`. Hence
`Q ≤ ∏_{E∈𝓜}[(1−1/w_E)+(w_E−1)²/w_E] = ∏_{E∈𝓜}(w_E−1)`. ∎

**Corollary 3.5 (C-1; PROVED).** For every single-value system on a finite
product probability space (any product measure; R38b D1), and all weights `λ_v≥1` with
`w_E=∏_{v∈supp E}λ_v≤2` for every event,

```
G_F(λ) = Σ_U (∏_{v∈U}λ_v)·‖F^{=U}‖² ≤ 1 .
```

*Proof.* Lemma 3.1 and Theorem 3.4 (𝓗(x) consists of event supports). ∎

So C-1, and with it the modulus-weighted EL of §4, holds with **no** mass,
codegree, quarantine or width hypothesis. (FM, the fractional-matching form,
remains open, but nothing below needs it.)

## 4. Consequences: ESW in energy form and the junta term (PROVED)

**Corollary 4.1 (q-ary energy concentration; PROVED).** Let f be the
bad- or good-indicator of a single-value system whose events have support
`≤k`, on any finite product probability space (any alphabet sizes, any
product measure). Then

```
energy(f; t) = Σ_{|U|>t}‖f^{=U}‖² ≤ 2^{−(t+1)/k}     for all integers t≥0 (k≥1).
```

*Proof.* Corollary 3.5 with `λ_v=2^{1/k}`, and `f^{=U}=−F^{=U}` for `U≠∅`. ∎

This is the energy form of ESW (O8 §6.4) with no dependence on the alphabet
size, on masses or on codegrees. It is the q-ary analogue of the Boolean
fact "width-w DNFs are ε-concentrated up to degree `O(w log 1/ε)`", here
with the threshold `λ^k=2` of Cor 3.5 sharp as the alphabet sizes grow (a single
event has `G=1−π(2−∏(λ_v−(λ_v−1)/q_v))`, §2).

*Sharpness (R38b D2, §3.1 of `reviews/pointwise-omega10-review-2.md`).*
Over general product spaces the rate `2^{−1/k}` per level is **sharp**. Take
m disjoint width-k events fixing values of probability p, let `p→0` and
choose m optimally. Then `max_m energy(t)·2^{(t+1)/k} ≍ (t/k)^{−1/2}`
(exact numerics, `scripts/review_o10b_sharp*.py`). So only a factor
`√(t/k)` could be gained, never the base. On the uniform Boolean cube the
truth for width-k DNFs is open: it lies between `3^{−t/k}` (OR of s
disjoint k-parities, `energy(jk−1)≍3^{−j}`) and `2^{−t/k}`.

*Set-valued literals (R38b D4c).* Cor 4.1 applies verbatim to q-ary DNFs
with literals `x_v∈S_v`. Split each term into single-value cylinders on
the same support: the good-indicator and the supports are unchanged.

*Normalisation (R38 MINOR 1).* Cor 4.1 is for **0/1-valued** f, which is
what ES uses. For the ±1-valued `g=1−2f` of the DNF literature,
`g^{=U}=−2f^{=U}` for `U≠∅`, so `W^{>t}[g] ≤ 4·2^{−(t+1)/k}`. Likewise
`λ^{|U|}≥1+|U|ln λ` gives `I_{0/1}[f] ≤ (k/ln 2)·P[f=1]`. For q=2 these are
stronger in the exponent than the switching-lemma bound
`W^{≥t}≤2·2^{−t/(20w)}` (O'Donnell §4.4). No known lower bound contradicts
them: parity written as a width-w DNF, tribes and a single AND all satisfy
them with room (R38 exhaustive check of all Boolean functions on ≤4 bits).

*Boolean form (R38b D3).* For every width-k DNF `g:{±1}^n→{±1}` and every
product measure on `{±1}^n` (Efron–Stein weights; for the uniform measure
`W^{>t}[g]=Σ_{|S|>t}ĝ(S)²`),

```
W^{>t}[g] ≤ 4·2^{−(t+1)/k},   i.e. g is ε-concentrated up to degree k·log₂(4/ε).
```

The standard bound is ε-concentration up to degree `C·w·log(1/ε)` with an
unspecified or large constant. It comes from Håstad's switching lemma via
Linial–Mansour–Nisan (JACM 1993), Mansour (JCSS 1995), O'Donnell,
*Analysis of Boolean Functions*, Ch. 4 (`W^{≥t}≤2·2^{−t/(20w)}`), and
Lecomte–Tan Fact 6. Total influence: `I[g]≤(4k/ln2)·P[g=−1]` (from
`λ^{|U|}≥1+|U|lnλ`). It is weaker than, but of the same order as, the
known `I≤2w`.

*Prior art and novelty (R38 MINOR 2).* The nearest prior art is
Lecomte–Tan, "Sharper bounds on the Fourier concentration of DNFs" (FOCS
2021, arXiv:2109.04525). They bound `|f̂(S)|` by the probability that S is
*covered* by the terms satisfied at a random x, which is the device of
Lemma 3.1. There are three differences.
* Their cover counts are unsigned, so there is no cancellation and no
  analogue of `N(V)=0` when an event avoiding V holds.
* They work over `{±1}^n`.
* Their degree concentration still comes from Håstad, with an unspecified
  constant.

Lemmas 3.2–3.3, C-1 and Cor 4.1 (switching-free, constant 1, any alphabet
and product measure, sharp base) are **new to us. Assessment: possibly new
as a sharp-constant statement; the literature search is partial and still
pending** (Håstad/Rossman switching-lemma variants, the Fourier-growth
literature, "hypercontractivity with ρ>1") (R38 checked
Lecomte–Tan and lecture notes by Lovett, Cornell CS6817 and O'Donnell).
*Observation (R38 item 6).* Lemma 3.1 uses only that `L_V` is an orthogonal
projection, and Lemmas 3.2–3.4 are purely combinatorial. So C-1 and Cor 4.1
hold on arbitrary finite product probability spaces, not only uniform ones.
This is now built into the statements (R38b D1), and R38b checked it
numerically for biased q-ary systems.

**Theorem 4.2 (junta term without the bit factor; PROVED as an
implication inside O8 Thm 3.4 / O9 Thm 2.2; the rates below are modulo (G)
and Elsholtz–Tao Prop 1.4, like O9 Thm 2.2).** In O8 Thm 3.4 (events split
into single values mod `ℓ^{e_ℓ}` as in O8 Setting 3.0, supports `≤k`,
`m≤T^{k+2}`), take `u_j` to be the Efron–Stein truncation of `F^{(j)}` at
level

```
t := k·⌈log₂(100 m²(S+1) e^{3S})⌉ ≤ C·k(S + k𝓛).
```

Then EL(t) holds. Each restricted event of `F^{(j)}` again has support
`≤k`, so Corollary 4.1 applies. In O9 Thm 2.2 this replaces
`d=4C_H·k·b·k_0`, so

```
log Z ≤ log Q_Π + 2(3k+2t+1)𝓛 ≪ log Q_Π + k𝓛(S*+k𝓛) ≪ log Q_Π + 𝓛^6     (z=𝓛², under ET).
```

The rest of O9 Thm 2.2 is unchanged: Lemma 2.1 gives `A≤1.03`, the twist
uses only `E[F−B]≤δ/100`, and the cells of B lie on `≤3k+2t` free primes.

*Proof details (R38 MINOR 3).* O9 Thm 2.2 used O8 Lemma 6.1's minorant
(bit-level Fourier truncation). Here we return to O8 Lemma 3.1 with the
Efron–Stein truncations `u_j` (functions of the coordinates off
`supp E_j`, so `E[A_je_j²]=P(E_j)·energy(F^{(j)};t)`), and O8 **Lemma 3.2**
shows that B is a combination of unit cells, each on `≤3k+2t` free primes.
O9 Thm 1.1 uses only the following: the cell form, `B≤1[W>T]` (O2
Lemma 4.3(I)), `μ>0`, the twist (O8 Lemma 3.3, which needs only
`E[F−B]≤EF/100`), `A=E|B|/μ≤1.03` (O9 Lemma 2.1, which needs only `B≤F`
and `E[F−B]≤μ/99`), and `log Z≤log Q_Π+2(3k+2t+1)𝓛`. None of these
depends on the choice of `u_j` beyond EL and the cell support count, and
Lemma 3.2's `M_1` bound is not needed.

So the junta term drops from `≍𝓛^7` to `≪𝓛^6`, and already, **modulo (G) and ET
Prop 1.4**, `log L_h(T) ≪ 𝓛^7/log𝓛`, i.e. `W(p) ≥ exp(c(log p·log log p)^{1/7})` i.o. (a log
gain over O9 Thm 2.2), and
`log Q_Π≪𝓛^7/log𝓛` is now the **only** term of order `𝓛^7`. With a
quarantine `log Q_Π≪𝓛^6` (task item (b)), O9 Thm 2.2 would give exponent
1/6. That is O9 Cor 4.2's ceiling for coordinate-counting arguments, and
it is now reached on the junta side.

**Remark 4.3 (modulus weighting; PROVED under a stated hypothesis).**
Suppose every event's modulus satisfies `∏_{ℓ∈supp E}ℓ^{a_ℓ} ≤ T^ρ`, where
`a_ℓ` is the largest exponent of ℓ used by any event. Take coordinates
`X_ℓ mod ℓ^{a_ℓ}`, events split to single values there, and
`λ_ℓ:=2^{a_ℓ log ℓ/(ρ𝓛)}`. Then every `w_E≤2`, and by Cor 3.5
`Σ_{U∉𝒟}‖F^{(j),=U}‖² ≤ 2^{−τ/(ρ𝓛)}` for the down-closed family
`𝒟:={W: Σ_{ℓ∈W}a_ℓ log ℓ ≤ τ}`.
* (a) *Cell moduli (R38 MINOR 5).* Take `u_j:=Σ_{U∈𝒟}F^{(j),=U}`. As in
  O8 Lemma 3.2, Möbius inversion of
  `φ^{=U}=Σ_{W⊆U}(−1)^{|U∖W|}E[φ|X_W]` gives `u_j=Σ_{W∈𝒟}c_WE[F^{(j)}|X_W]`
  with `c_W=Σ_{U∈𝒟,U⊇W}(−1)^{|U∖W|}`. So every cell has modulus `≤e^τ`,
  and EL holds for `τ:=ρ𝓛·⌈log₂(100m²(S+1)e^{3S})⌉`.
* (b) Splitting into single values mod `ℓ^{a_ℓ}` multiplies m by at most
  `T^ρ`, which is harmless inside `log m`.

Hence `log Z ≤ log Q_Π + O(τ+ρ𝓛) = log Q_Π + O(ρ𝓛(S+k𝓛))`. O8's setting
guarantees only `ℓ^{e_ℓ}≤T` per prime, i.e. `ρ≤k`, which gives back `𝓛^6`. If all free primes enter the event
moduli to the first power (`ρ=1`), this is `≪ log Q_Π+𝓛^5log𝓛` under ET.
`W ≥ exp(c(log p/log log p)^{1/5})` would then need `log Q_Π≪𝓛^5log𝓛`. We have **not** checked
whether the ES events at free primes `>z` use higher prime powers, or
whether those can be quarantined cheaply. (Digit coordinates do not
help: a junta function of the i-th base-ℓ digit alone needs modulus
`ℓ^{i+1}`.)

## 5. Status summary, scope

* PROVED: §1 check of O9 §4 (no error in Lemma 4.1/Cor 4.2's statements;
  arithmetic slip `𝓛^6/log𝓛→𝓛^6`; the 1/6 ceiling is for coordinate-counting
  arguments only); §2 identities and the single-coordinate case of MONO; the
  counterexample to MONO; **Lemma 3.1** (`G_F ≤ E_x Q_μ(𝓗(x))`, suppression
  built in); the vertex recursion; the two-edge formula; §4's implication.
* PROVED (checkpoint 2): Conjectures Q, Q′, QM (Thm 3.4), hence C-1 (Cor 3.5), q-ary energy concentration (Cor 4.1), junta term `≪𝓛^6` (Thm 4.2; rates modulo (G) and ET Prop 1.4). C-1/Cor 4.1 hold for arbitrary product measures; the base `2^{−1/k}` is sharp over general product spaces (R38b §3.1). Novelty: possibly new as a sharp-constant statement, literature search pending (nearest prior art Lecomte–Tan 2021).
* CONJECTURE (EVIDENCE): FM (fractional matchings), C-exp (`w_E>2` allowed).
* Not claimed: the random-restriction form of ESW (not needed: Cor 4.1 is
  the energy-tail statement that ESW+LMN was meant to supply); any exponent improvement
  by itself (needs a cheaper quarantine); anything about ES.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_mono.py 7 1000 2.0)   # MONO random check (~5 min)
(ulimit -v 8000000; timeout 600 uv run python scripts/omega10_monocex.py)           # MONO counterexample (~1 min)
(ulimit -v 8000000; timeout 1200 uv run python scripts/omega10_cexp.py 5 800 2.0)   # C-exp random (~5 min)
(ulimit -v 8000000; timeout 1200 uv run python scripts/omega10_gamma.py 1 300)      # Lemma 3.1 check (~3 min)
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_q.py 1 20000 10)      # Conjecture Q (~5 min)
(ulimit -v 8000000; timeout 1500 uv run python scripts/omega10_qhc.py 2 150 7)      # Q hill-climb
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_qmin.py 1 20000 9)    # Q'
(ulimit -v 8000000; timeout 900 uv run --with scipy python scripts/omega10_fm.py 1 20000 9)  # FM
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_xsign.py 1 20000 8)   # X<0 cases
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_qtheta.py 1 300 7)    # Lemma 3.2 identity (exact enumeration)
(ulimit -v 8000000; timeout 900 uv run python scripts/omega10_theta.py 1 30000 10)  # |Theta|<=1 (Lemma 3.3)
```
