# Hostile review of POINTWISE_OMEGA2.md (branch `side-agent/omega-hub` @ 3f43543)

Reviewer: side agent (review-omega2). Scope: POINTWISE_OMEGA2.md,
reviews/agent-reports/AGENT_REPORT_O2.md, scripts/omega2_*.py as of 3f43543.
Context used: POINTWISE_OMEGA.md (PO) §1, Thm 4.1, §6.2 (H_MIN, Thm 6.2),
§9 (Lemma 9.1/9.2 setting); paper/es-omega-note.tex (definition of W, 𝓡).

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects are numbered
D1, D2, … with severity FATAL / MAJOR / MINOR / COSMETIC.

## Per-item verdicts

(filled in item by item below)

### Item 1 — Lemma 1.1 (closed form of support-truncated B_L): **SOUND**

Re-derived. `Σ_{F⊆A, supp F⊆U}(−1)^{|F|} = I(U)` (alternating sum over the
subsets of `{E∈A: supp E⊆U}`, empty F included); Möbius on the Boolean
lattice; every `supp F⊆V`; swapping sums gives
`Σ_{W⊆V, I(W)=1, |W|≤L} Σ_{j=0}^{L−|W|}(−1)^j binom(N−|W|,j)`, and the
partial alternating row sum is `(−1)^k binom(n−1,k)` for `n≥1`. `I(V)=1` iff
`A=∅`, so for `A≠∅` only `W⊊V` occur, `N−|W|−1≥0`, and for `N≤L` every
binomial vanishes. No gap.

Independent brute force (reviewer code, written without reading the
author's script): `reviews/omega2-review-scripts/bf_lemma12.py`. Events are
arbitrary subsets of `∏_{supp}Ω_ℓ` (supports 1–3, `|Ω_ℓ|≤3`, up to 5
primes, up to 9 events), all outcomes, all `0≤L≤|𝒫|+1`; `B_L` computed by
enumerating `F⊆A(x)`. Closed form = definition in 102 277 cases (seeds
11, 12, 13), 0 failures. Mutation check (sign `(−1)^w` instead of
`(−1)^{L−w}`): 213 failures in 4 412 cases, so the test has teeth.

### Item 2 — Lemma 1.2 (pointwise minorant): **SOUND**

Re-derived: `|R_L| ≤ Σ_w binom(N,w)binom(N,L−w)=binom(2N,L)` (Vandermonde);
`f(N+1)/f(N)=2(2N+1)(N−L)/((2N+2−L)(2N+1−L))`, and with `N=L+t` the
difference denominator − numerator is `L²+3L+4t+2` (checked by hand);
`f(L+1)=binom(2L+2,L)≤4^{L+1}`; `binom(N,L+1)=e_{L+1}(1_V)≤e_{L+1}(a)` by
monotonicity. Both inequalities hold in all 102 277 brute-force cases
(same script). Observed `max |B_L|/(4^{L+1}e_{L+1}(a)) = 1/4` over cases with
`A≠∅, N≥L+1`: the constant is lossy by a factor ≥4 in practice, which is
harmless.

### Item 3 — Lemma 1.3 (mean, mass, twist reduce to `E∏(1+za)`): **SOUND**

(1) termwise `e_{L+1}(a)≤z^{−(L+1)}∏(1+za_ℓ)`; with `z=16`,
`2·4^{L+1}·16^{−(L+1)} = 2·4^{−(L+1)}`. Correct.
(2) Grouping by `U=supp F`: on a cell c of the U-coordinates the
coefficient is `κ(U,c)=Σ_{F⊆A_U(c), supp F=U}(−1)^{|F|}`; Möbius gives
`|κ|≤2^{|U|}`; κ vanishes unless every `ℓ∈U` is covered by an occurring
event (trivially, since `supp F=U` forces this). Hence
`M_1(B_L)≤Σ_U 2^{|U|}E∏_{ℓ∈U}a_ℓ=E∏(1+2a_ℓ)`. Non-unit cells get κ=0
(no event occurs at a non-unit coordinate), so the expansion is into unit
classes as PO Thm 4.1 requires (`gcd(b_i,d_i)=1`). The `G_{L+1}` expansion
has nonnegative coefficients (products of event indicators are indicators
of intersections of unit classes), so mass = mean. The brute force also
computes the exact merged cell expansion of `B_L` and checks
`M_1(B_L) ≤ E∏(1+2a_ℓ)` for every L: 0 failures.

PO Thm 4.1's `M_1=Σ|c_i|/φ(d_i)` is representation-dependent; using the
merged-cell representations of `B_L` and `G_{L+1}` separately and the
triangle inequality is legitimate. No defect.

### Item 4 — Lemma 2.1 (pseudoforest exponential-moment bound): **SOUND** (one MINOR wording defect)

Re-derived step by step.

* *Expansion.* `1+z(s+d)≤(1+zs)(1+zd)` for `s,d≥0`;
  `∏_ℓ(1+zd_ℓ)=Σ_{(U,f)}z^{|U|}1[F occurs]` with `d_ℓ=Σ_{edges e at ℓ}1_e`.
  Correct.
* *Pseudoforest.* If F occurs, at most one vertex of F per prime (vertices
  at one prime are disjoint). Choose for each `e∈F` one `ℓ` with `f(ℓ)=e`;
  e is incident to the unique F-vertex at ℓ, and distinct e give distinct
  ℓ, hence distinct vertices. So `E(K)↪V(K)` per component. Correct.
* *Multiplicity.* For fixed F only `ℓ∈π(F)` can lie in U, and `f(ℓ)` must be
  an F-edge at the F-vertex at ℓ: `≤∏_v(1+z deg_F v)≤e^{2z|E(F)|}`. Correct
  (when F has two vertices at one prime the count may differ, but then
  `P(F)=0`).
* *Singles.* Independence of `s_ℓ` (`ℓ∉π(F)`) from F; `(1+z)^{|π(F)|}≤e^{z|V(F)|}`.
  Correct.
* *Components.* F ↦ set of its components is injective, `P(F)=∏_K P(K)` or
  0, so `Σ_F∏_K w_K≤∏_K(1+w_K)`. Correct.
* *Trees.* `P(K)=P(T)` for a spanning tree (same vertex set); `≤binom(v,2)`
  extra edges. BFS encoding with nested sums, each inner sum
  `Σ_{|C|=c, C⊆N(v_i)}∏p ≤ deg(v_i)^c/c!` bounded uniformly, the root factor
  `deg(v_0)δ^{c_1−1}`, total δ-power `v−2`;
  `Σ_{c_1+…+c_v=v−1}∏1/c_i! = v^{v−1}/(v−1)! = v^v/v! ≤ e^v`;
  `Σ_{v_0}p(v_0)deg(v_0)=2S_2`. Correct.
* *Sum.* `1+(j+2)²/2=3+2j+j²/2`; I recomputed
  `Σ_j(3+2j+j²/2)e^{−j}=3·1.5820+2·0.9207+½·1.9922=7.583`, so the factor
  `2·7.583≤16` holds.

Degree condition: used only via `e^{3z+1}δ≤e^{−1}`, i.e. `δ≤e^{−3z−2}`,
exactly as stated. Remark (i) is right: a complete bipartite hub on vertices
of degree ≤δ is allowed; what is forbidden is a *vertex* of large degree,
and Lemma 2.2 removes those.

**D1 (MINOR, Lemma 2.1 *Trees*, "this is injective").** The encoding
`(v_0; C_1,…,C_v)` is injective on *rooted* trees, and every tree is
counted once per root; the subsequent bound sums over `v_0`, so the
inequality is right but "injective" should read "each tree is recovered
from (v_0, C_1, …) for every choice of root; we overcount by a factor v".
Also the edge graph must be *simple* (`C_i⊆N(v_i)`): the text never says
that two atoms producing the same class mod `ℓℓ'` give one edge. The
script dedups (`edges` is a dict keyed by vertex pair), so only the prose
needs "edges are distinct classes mod ℓℓ'; repeated atoms are merged".

Not tested numerically: the hypothesis `δ≤e^{−50}` makes any finite
instance meaningless, and the author says so (§6). The proof is short and
checked by hand above.

### Item 5 — Lemma 2.2 (forbidding hub vertices, Markov cost): **SOUND**

`Σ_{v∈H at ℓ}p(v)≤Σ_{v at ℓ}p(v)deg(v)/δ=w_ℓ/δ` because
`Σ_v p(v)deg(v)=Σ_{edges at ℓ}p(u)p(w)` (each edge at ℓ has exactly one
endpoint at ℓ, since edges join distinct primes); `Σ_ℓ w_ℓ=2S_2`.
"No new event ⇒ no old event": an old edge through `v∈H` occurring forces
`X_{ℓ_v}∈V_v⊆S^+_{ℓ_v}`. Degrees of surviving vertices only drop; vertices
in H have no edges left. Correct and genuinely cheap: under (W)
(`w_ℓ≤δ/32`) a hub vertex even has `p(v)<1/32` individually.

### Item 6 — Theorem 3.1 (abstract criterion): **SOUND**

*Citation check.* Haeupler–Saha–Srinivasan, "New constructive aspects of
the Lovász local lemma", J. ACM 58(6) (2011), arXiv:1001.1231. I fetched the
arXiv version: **Theorem 2.1** there reads "If the LLL-conditions from
Theorem 1.1 are met, … for any event B determined by P,
`Pr[B | ∧_{A∈𝒜}Ā] ≤ Pr[B]·∏_{C∈Γ(B)}(1−x_C)^{−1}`", in the variable
setting where `Γ(B)` = events of 𝒜 sharing a variable with B. This is
exactly the form used (variables `X_ℓ`, adjacency = intersecting supports).
Citation correct; the remark "immediate from the Alon–Spencer proof" is
also correct (`P(B|∩Ā)≤P(B∩⋂_{A∉Γ(B)}Ā)/P(⋂_{Γ(B)}Ā | ⋂_{A∉Γ(B)}Ā)`).

*Step 1.* Lemma 2.2 with (W): `g^+_ℓ≤1/32+1/32`; (I) persists. Correct.

*Step 2 (LLL).* Variable-setting dependency graph (supports meet) is a
valid lopsided/mutual-independence graph. Single at ℓ: neighbours = edges
at ℓ, `∏(1−x)≥1−2w_ℓ≥1/2`; edge at ℓ,ℓ': two singles (`x≤2g^+≤1/8`) and
edges at ℓ or ℓ', `≥(7/8)²(1−4δ/32)≥1/2`. With `x_E=2P(E)` the condition
`P(E)≤x_E∏(1−x)` holds. `1−x≥e^{−1.1x}` on `[0,1/8]`
(`−log(7/8)=0.1335<0.1375`). Correct.

*Step 3.* `z=16`, `δ=e^{−50}=e^{−3z−2}` — matches Lemma 2.1 exactly
(`6z+2=98`). `4^{L+1}≥200e^{Λ+λ}` gives `E|B−1[A=∅]|≤e^{−λ}/100`;
`M_1≤e^Λ+4^{L+1}16^{−(L+1)}e^Λ≤2e^Λ`; `log(M_1/μ)≤Λ+λ+log 2−log .99`.
Each term is on `≤2(L+1)` primes. All budgets
`O(S_1+(2/δ+16e^{98}+3)S_2+1)=O(Σ+1)` with an astronomical absolute
constant. Correct.

*Step 4 (twist).* μ_ψ in PO Thm 4.1 is `Σ_{i: f|d_i}c_iψ(b_i)/φ(d_i)`; the
terms with `f∤d_i` have Haar-mean-zero twist (a prime of f is a free unit
coordinate), so `μ_ψ=E_Haar[Bψ]`. f is odd (gcd with Q, 2|Q) and real
primitive, hence squarefree, with primes in 𝒫. The factorisation
`1[A=∅]=1_{Ā'}1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]` is right (an event at `ℓ_0` is
the single or an edge `{u,w}`, u at `ℓ_0`, which fires iff `X_{ℓ_0}∈V_u` and
w occurs). `E_{X_{ℓ_0}}χ_0=0` swaps `∉Forb` for `∈Forb`. Conditional LLL
for "w occurs" against the sub-family defining `Ā'` (a sub-family of an
LLL family satisfies the condition with the same x): `Γ` = single and edges
at `ℓ_w`, `∏(1−x)≥(7/8)(1−2δ/32)`; the author's `(7/8)(15/16)` is looser
but fine. Final numbers: `0.01+0.064/0.936=0.0784<0.08`, `μ/4≥0.2475P`.
Correct.

No defect. The theorem is a clean, genuinely CRT-only statement.

### Item 7 — Lemma 4.1 (global mass for an arbitrary quarantine): **SOUND**

Re-derived. `1/φ(r)≪log log T/r = log log T·m/M`, `M=4A−1≥3A`. The
involution `D↦A²/D` keeps M (hence `r_Π>1`) and preserves `m|4D+1`
(multiply `4A²/D+1` by the unit D: `4A²+D≡¼+D≡(1+4D)/4≡0 (m)`, using
`4A≡1 (m)`). `D=sr'²|A²` with s squarefree implies `sr'|A` (prime by prime:
`1+2v_q(r')≤2v_q(A)⇒v_q(A)≥v_q(r')+1`), so `A=sr'k`, `k≥r'` when `D≤A`.
`m | (4sr'k−1)+(4sr'²+1)=4sr'(k+r')` and `gcd(m,4sr')=1`, so `m|k+r'`;
`(s,r',k)` determines the atom. Inner sum: the least admissible k has
`k+r'≥m` and `k≥r'`, so `k≥m/2`, giving `≤(3+log T)/m`. Final divisor
bound: `τ(4sr'²+1)≤τ*`, `Σ_{s,r'}1/(sr')≤(1+𝓛)²`. Nothing in the proof
uses the shape of Π. With the *explicit* Wigert constant
(`τ(n)≤2^{1.5379 log n/log log n}`) the exponent is
`≈1.066·𝓛/log 𝓛`; I use this below for the effectivity check.
