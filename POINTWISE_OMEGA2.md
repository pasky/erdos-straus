# Beyond exponent 2: a support-truncated minorant and `W(p) > (log p)^{3−o(1)}` infinitely often

Task O2. Labels follow the house rules. ES is not solved here or anywhere;
nothing below bears on whether `W(p)<∞`. Notation as in `POINTWISE_OMEGA.md`
(cited as PO): `W`, `𝓡(M)`, `A_M=(M+1)/4`, Fact 1.1 (class of one),
Theorem 4.1 (transfer), H_MIN(θ), Theorem 6.2.

**Results at a glance (checkpoint 1; not yet reviewed).**

1. **Theorem 5.1** (PROVED modulo Thorner–Zaman, via PO Theorem 4.1; effective):
   `W(p) ≥ (log p)^3·exp(−C log log p/log log log p)` for infinitely many
   Mordell-hard p, and `log L_h(T) ≤ T^{1/3+o(1)}`. So H_MIN(θ) holds for
   every θ>1/3, and `H_MOD(A)` is refuted for every `A<3`.
2. **Theorem 3.1** (PROVED; pure CRT combinatorics): a congruence system of
   singles and two-prime edges with per-prime masses `g_ℓ≤1/32` and
   `w_ℓ≤e^{−50}/32` admits a pointwise minorant of its void indicator with
   `log(M_1/μ)=O(S_1+S_2+1)`, moduli on `O(S_1+S_2+1)` primes, and the twist
   condition of PO Theorem 4.1.
3. **New tools** (PROVED): support-truncated inclusion–exclusion
   (Lemmas 1.1–1.3), a pseudoforest bound for `E∏(1+z a_ℓ)` (Lemma 2.1),
   and a Markov-cheap quarantine of hub vertices (Lemma 2.2).
4. **Scope.** PO Prop 6.3 remains true but is no obstruction to H_MIN.
   Below θ=1/3 the missing inputs are an H_PP-type per-prime bound and a
   hypergraph form of Lemma 2.1 (§7). The prime side now matches the Haar
. **Checkpoint 2 (§§8–9).**
   * Single-coordinate atoms are exactly Elsholtz–Tao Type I points (Lemma
     8.1, PROVED).
   * Hence `|F_ℓ^{full}|≤ℓ^{3/5+o(1)}` (modulo ET Prop 1.7), and
     `≪√ℓ log ℓ` for the `r′=1` part (elementary).
   * `ℓ^{1/2}` in general is *not* proved. It would improve ET Prop 1.7,
     and 3/5 is the divisor-method limit (Remark 8.3).
   * `F_I(n)≤n^{η}` implies a Haar exponent `η/(1+η)` (Thm 9.2). So
     η<1/2 is needed to beat 1/3, and `η=1/2` only reproduces it.
   * The single part of H_PP was never the bottleneck. The true per-prime
     target is a progression average of Type I counts (AP-TI), which
     reduces to an explicit Kloosterman-type first-term sum.

6. **Checkpoint 3 (§10, below θ=1/3).**
   * Private-cover majorant (Lemma 10.1) and a hypergraph moment bound
     under a codegree condition (Lemma 10.2), both PROVED.
   * Hypergraph criterion, Theorem 10.3, PROVED.
   * Conditional result (Theorem 10.4, PROVED implication): the
     post-quarantine hypothesis H_CD(θ) implies H_MIN(θ). If it holds
     for every θ>κ, then `W(p) ≥ (log p)^{1/κ−o(1)}` i.o. (modulo
     Thorner–Zaman).
   * The first draft's AP-TI*(κ) is **withdrawn**: it is false because of
     hub residues.
   * Prop. 10.6 (PROVED): the classes `−4d²` give pair codegrees
     `≍1/φ(4d)` at every θ<1/3. Theorem 10.3, with Lemma 10.2's
     per-old-vertex factor, therefore cannot certify θ<1/3 unless an
     unproved quarantine-cost bound fails (Assessment).
   * The open step is a sharper Lemma 10.2. Unconditional estimates stop
     at θ=1/3 (Prop 10.5).

## 0. Idea in one paragraph

PO Prop 6.3 shows that inclusion–exclusion truncated by the **number of
events** fails: a hub configuration on `2r` primes fires `r²` events, and
`binom(r², J)` beats its probability `y^{−2r}`. We truncate instead by the
**number of primes in the support** of the event set. The truncation error is
then controlled by the number `N(n)` of *active primes*, and a hub on `2r`
primes costs only `C^{2r}` against `y^{−2r}`. What remains is a moment bound
for `N(n)` (more precisely for `∏_ℓ(1+z a_ℓ)`), which we prove by a
pseudoforest expansion once high-degree vertices are forbidden (a cheap,
Markov-bounded quarantine of hub *vertices*).

## 1. An abstract support-truncated minorant (PROVED)

**Setting 1.0.** `𝒫` is a finite set of "primes"; `X=(X_ℓ)_{ℓ∈𝒫}` are
independent random variables. `𝓔` is a finite family of events; each
`E∈𝓔` has a support `supp E⊆𝒫`, nonempty, and depends only on
`(X_ℓ)_{ℓ∈supp E}`. For an outcome x put

```
A(x) := {E∈𝓔 : E occurs},   V(x) := ∪_{E∈A(x)} supp E   (active primes),   N(x) := |V(x)|,
a_ℓ(x) := #{E∈A(x) : ℓ∈supp E}.
```

For `L≥0` define

```
B_L(x) := Σ_{F⊆A(x), |supp F|≤L} (−1)^{|F|},      supp F := ∪_{E∈F} supp E,
G_{L+1}(x) := e_{L+1}(a(x)) = Σ_{P⊆𝒫, |P|=L+1} ∏_{ℓ∈P} a_ℓ(x).
```

**Lemma 1.1 (exact form of the truncation; PROVED).** Call `W⊆𝒫`
*independent at x* if no `E∈A(x)` has `supp E⊆W`. If `A(x)=∅` then
`B_L(x)=1`. If `A(x)≠∅` then

```
B_L(x) = R_L(x) := Σ_{W⊊V(x) independent at x, |W|≤L} (−1)^{L−|W|} binom(N−|W|−1, L−|W|),
```

and in particular `B_L(x)=0` whenever `1≤N(x)≤L`.

*Proof.* Fix x and write `A=A(x)`, `V=V(x)`. For `U⊆V`,
`Σ_{F⊆A, supp F⊆U}(−1)^{|F|} = 1[no E∈A has supp E⊆U] =: I(U)`, since the
left side is the alternating sum over all subsets of `{E∈A : supp E⊆U}`.
Möbius inversion on the Boolean lattice gives
`Σ_{F⊆A, supp F=U}(−1)^{|F|} = Σ_{W⊆U}(−1)^{|U∖W|}I(W)`. Every `supp F` lies
in V, so

```
B_L = Σ_{U⊆V,|U|≤L} Σ_{W⊆U} (−1)^{|U∖W|} I(W) = Σ_{W⊆V, I(W)=1, |W|≤L} Σ_{j=0}^{L−|W|} (−1)^j binom(N−|W|, j).
```

The inner sum is `(−1)^{L−|W|}binom(N−|W|−1, L−|W|)` when `N−|W|≥1` and
equals 1 when `W=V`. Finally `I(V)=1` iff `A=∅`. If `N≤L`, every binomial
`binom(N−|W|−1, L−|W|)` has lower index above the upper one, so it vanishes. ∎

**Lemma 1.2 (pointwise minorant; PROVED).** For every x and every `L≥0`,

```
B*_L(x) := B_L(x) − 4^{L+1} G_{L+1}(x)  ≤  1[A(x)=∅],
|B_L(x) − 1[A(x)=∅]| ≤ 4^{L+1} G_{L+1}(x).
```

*Proof.* If `A=∅` then `a≡0`, `G_{L+1}=0`, and `B_L=1`. Let `A≠∅`. If
`N≤L` then `B_L=0` (Lemma 1.1). If `N≥L+1`, Lemma 1.1 and Vandermonde give

```
|R_L| ≤ Σ_{w≤L} binom(N,w) binom(N−w−1, L−w) ≤ Σ_w binom(N,w) binom(N,L−w) = binom(2N, L).
```

Put `f(N)=binom(2N,L)/binom(N,L+1)` for `N≥L+1`. Then

```
f(N+1)/f(N) = 2(2N+1)(N−L) / ((2N+2−L)(2N+1−L)),
```

and with `t=N−L≥1` the denominator minus the numerator is
`L²+3L+4t+2>0`. So f is decreasing and
`binom(2N,L) ≤ f(L+1) binom(N,L+1) = binom(2L+2,L) binom(N,L+1) ≤ 4^{L+1}binom(N,L+1)`.
Finally `binom(N,L+1)=e_{L+1}(1[ℓ∈V])_ℓ ≤ e_{L+1}(a)` because
`1[ℓ∈V]≤a_ℓ` coordinatewise and `e_{L+1}` is monotone on `ℝ_{≥0}^𝒫`. ∎

**Lemma 1.3 (mean, mass, twist reduce to one exponential moment; PROVED).**
Let `z≥16` and `Λ_z := log E∏_{ℓ∈𝒫}(1+z a_ℓ)`. Then:

1. `E G_{L+1} ≤ z^{−(L+1)} e^{Λ_z}`, hence
   `E|B*_L − 1[A=∅]| ≤ 2·4^{L+1}E G_{L+1} ≤ 2·4^{−(L+1)}e^{Λ_z}`.
2. Expand every event indicator as a sum of indicators of "cells" (when the
   events are congruence classes: classes modulo `∏_{supp}ℓ^{e_ℓ}`). Then
   `B_L` is a combination of cell indicators on supports of size `≤L`, and
   `G_{L+1}` a nonnegative combination on supports of size `≤k(L+1)`, where
   `k=max|supp E|`. Their ℓ¹-masses (Σ|coefficient|·probability of the cell,
   after merging equal cells) satisfy
   `M_1(B_L) ≤ E∏_ℓ(1+2a_ℓ) ≤ e^{Λ_z}` and `M_1(G_{L+1}) = E G_{L+1}`.

*Proof.* (1) `e_{L+1}(a) ≤ z^{−(L+1)}∏(1+za_ℓ)` termwise, since all
`a_ℓ≥0`. The second claim is Lemma 1.2 plus `E|B_L−1[A=∅]| ≤ 4^{L+1}EG`.

(2) Group the terms of `B_L` by `U=supp F`. On a cell c of the coordinates in
U the coefficient is `κ(U,c)=Σ_{F⊆A_U(c), supp F=U}(−1)^{|F|}`, where
`A_U(c)` is the set of events with support in U occurring on c. By the
Möbius formula in Lemma 1.1, `κ(U,c)=Σ_{W⊆U}(−1)^{|U∖W|}I_c(W)`, so
`|κ|≤2^{|U|}`. Also `κ(U,c)=0` unless every `ℓ∈U` lies in the support of
some event of `A_U(c)`: if ℓ does not, then `I_c(W)=I_c(W∪{ℓ})` and the terms
cancel in pairs. Hence

```
M_1(B_L) ≤ Σ_U 2^{|U|} P(every ℓ∈U is covered by an occurring event) ≤ Σ_U 2^{|U|} E∏_{ℓ∈U} a_ℓ = E∏_ℓ(1+2a_ℓ).
```

`G_{L+1}` expands with coefficients +1 into products of event indicators,
so its mass equals its mean. ∎

*Remark (why this beats PO Prop 6.3).* On a hub configuration with `2r`
active primes and `r²` events, the event-level truncation error is
`binom(r²−1,J−1)`, while here it is at most `binom(4r,L)≤16^r`. So the error
is exponential in the number of *primes*, and each prime costs a factor
`≍1/ℓ` in probability.

## 2. The exponential moment for graph-type systems (PROVED)

**Setting 2.0.** As in 1.0, with `X_ℓ` taking values in a finite set
`Ω_ℓ`. The events are of two kinds.

* **Singles.** One set `S_ℓ⊆Ω_ℓ` per ℓ (possibly empty); the event is
  `{X_ℓ∈S_ℓ}`, with probability `g_ℓ`. Put `S_1=Σ_ℓ g_ℓ`.
* **Edges.** A *vertex* is a pair `v=(ℓ,V_v)` with `V_v⊆Ω_ℓ`; distinct
  vertices at the same ℓ are disjoint; `p(v)=P(X_ℓ∈V_v)`. An *edge* is an
  unordered pair `{u,w}` of vertices at distinct primes; it occurs iff both
  `X_{ℓ_u}∈V_u` and `X_{ℓ_w}∈V_w`. Put `S_2=Σ_{edges}p(u)p(w)` and
  `deg(v)=Σ_{w:{v,w} edge} p(w)`. The edge graph is simple: edges are
  distinct pairs of vertices (for congruence systems, distinct classes mod
  `ℓℓ'`), and repeated atoms giving the same class are merged into one edge.

Thus `a_ℓ=s_ℓ+d_ℓ` with `s_ℓ=1[X_ℓ∈S_ℓ]` and `d_ℓ` the number of occurring
edges at ℓ. (A congruence class modulo `ℓℓ'` is the edge between the vertices
`(ℓ, c mod ℓ)` and `(ℓ', c mod ℓ')`.)

**Lemma 2.1 (pseudoforest bound; PROVED).** Let `z≥1` and suppose
`deg(v)≤δ≤e^{−3z−2}` for every vertex v. Then

```
Λ_z = log E∏_ℓ(1+z a_ℓ) ≤ z S_1 + 16 e^{6z+2} S_2.
```

*Proof.* **Expansion.** `1+z(s+d)≤(1+zs)(1+zd)`. Expand
`∏_ℓ(1+zd_ℓ) = Σ_{(U,f)} z^{|U|} 1[f(ℓ) occurs ∀ℓ∈U]`, where U is a set of
primes and f assigns to each `ℓ∈U` an edge incident to a vertex at ℓ.
Let `F=f(U)`. If F occurs, its vertices lie at distinct primes, and each
component K of F has `|E(K)|≤|V(K)|`: each edge of K is `f(ℓ)` for an ℓ whose
vertex lies in K, and distinct ℓ give distinct vertices. So every component is
a tree or unicyclic (F is a *pseudoforest*). For fixed F,

```
Σ_{(U,f): f(U)=F} z^{|U|} ≤ ∏_{v∈V(F)} (1+z deg_F(v)) ≤ e^{2z|E(F)|} ≤ e^{2z|V(F)|}.
```

**Singles.** Let `π(F)` be the set of primes of `V(F)`. For any set `U_s`,
independence gives
`E[∏_{ℓ∈U_s}s_ℓ·1[F occurs]] ≤ ∏_{ℓ∈U_s∖π(F)}g_ℓ · P(F occurs)`. Summing
`z^{|U_s|}` over `U_s` gives at most `(1+z)^{|π(F)|}∏_ℓ(1+zg_ℓ)`. Hence

```
E∏_ℓ(1+za_ℓ) ≤ e^{zS_1} Σ_F e^{3z|V(F)|} P(F occurs).
```

**Components.** If the components of F lie on disjoint prime sets,
`P(F occurs)=∏_K P(K occurs)`; otherwise it is 0. So the last sum is at most
`∏_K(1+w_K) ≤ exp(Σ_K w_K)`, with K over connected pseudoforests in the edge
graph and `w_K=e^{3z|V(K)|}P(K occurs)`.

**Trees.** A connected pseudoforest K on v vertices is a spanning tree T plus
at most one of the `≤v²/2` remaining vertex pairs, and `P(K)≤P(T)`. For a
tree, `P(T occurs)≤∏_{w∈T}p(w)`. Root T at any vertex `v_0` and encode it by
the child sets `C_1,…,C_v` in breadth-first order (children ordered by a
fixed total order on vertices). For each choice of root, T is recovered
from `(v_0; C_1,…,C_v)`, so summing over all roots overcounts each tree by
the factor v, which is harmless for an upper bound. Summing over `C_i⊆N(v_i)`
with `|C_i|=c_i` gives at most `deg(v_i)^{c_i}/c_i!`; for `i=1`, `c_1≥1`,
bound it by `deg(v_0)δ^{c_1−1}/c_1!`. The number of weighted compositions is
`Σ_{c_1+…+c_v=v−1}∏1/c_i! = v^{v−1}/(v−1)! ≤ e^v`. Hence

```
Σ_{T: |V(T)|=v} P(T occurs) ≤ Σ_{v_0} p(v_0)deg(v_0) e^v δ^{v−2} = 2S_2 e^v δ^{v−2}.
```

**Sum.** With `e^{3z+1}δ≤e^{−1}`,

```
Σ_K w_K ≤ Σ_{v≥2} e^{3zv}(1+v²/2)·2S_2 e^v δ^{v−2} = 2S_2 e^{6z+2} Σ_{j≥0}(3+2j+j²/2)(e^{3z+1}δ)^j ≤ 16 e^{6z+2} S_2,
```

since `Σ_j(3+2j+j²/2)e^{−j} = 7.58…`. ∎

*Remarks.* (i) The hypothesis is a **vertex-degree** bound, not a bound on
how many events a configuration can fire; complete bipartite hubs are allowed.
(ii) The constants are astronomically lossy but absolute; only
`Λ_z=O_z(S_1+S_2)` matters below.

**Lemma 2.2 (forbidding hub vertices; PROVED).** For `δ>0` let
`H={v : deg(v)>δ}`. Replace `S_ℓ` by `S_ℓ^+ := S_ℓ ∪ ⋃_{v∈H at ℓ}V_v`, and
delete every edge with an endpoint in H. Then:

* "no event of the new system" implies "no event of the old system";
* every remaining vertex has degree `≤δ` in the new edge graph;
* `S_1^+ ≤ S_1 + 2S_2/δ`, and at each ℓ, `g_ℓ^+ ≤ g_ℓ + w_ℓ/δ`, where
  `w_ℓ := Σ_{edges at ℓ}p(u)p(w)`;
* `S_2^+ ≤ S_2`.

*Proof.* An old edge with an endpoint `v∈H` cannot occur without the new
single at `ℓ_v`. Degrees only decrease when edges are deleted. Markov:
`Σ_{v∈H at ℓ}p(v) ≤ Σ_{v at ℓ}p(v)deg(v)/δ = w_ℓ/δ`, and `Σ_ℓ w_ℓ=2S_2`. ∎

## 3. The abstract criterion for H_MIN (PROVED, modulo nothing)

**Setting 3.0 (congruence systems).** Fix `Q` with `2|Q` and a finite set `𝒫` of primes
coprime to Q, with exponents `e_ℓ≥1`. Put `X_ℓ := n mod ℓ^{e_ℓ}`. The
"Haar" measure is the uniform measure on `∏_ℓ(ℤ/ℓ^{e_ℓ})^×`, i.e. the
measure in which PO Theorem 4.1 computes `μ=Σc_i/φ(d_i)`. A single is a set
`S_ℓ` of unit classes mod `ℓ^{e_ℓ}`; a vertex is a unit class mod ℓ (a union
of fibres mod `ℓ^{e_ℓ}`, `p(v)=1/(ℓ−1)`); an edge is a unit class mod `ℓℓ'`.
The pointwise statements of §1 hold for every integer n (non-unit residues
simply trigger no event); only expectations use the Haar measure.

**Theorem 3.1 (support-truncated minorant; PROVED).** Put `z=16`,
`δ=e^{−50}`. Assume, in Setting 3.0 with singles and edges as in §2:

* (G) `g_ℓ ≤ 1/32` for every `ℓ∈𝒫`;
* (W) `w_ℓ ≤ δ/32` for every `ℓ∈𝒫`, where `w_ℓ=Σ_{edges at ℓ}p(u)p(w)`;
* (I) for every integer `n≡1 (mod Q)`: if no single and no edge occurs at n,
  then `W(n)>T`.

Put `Σ := S_1+S_2`. Then there is a minorant `B` as in PO Theorem 4.1
(moduli coprime to Q, unit classes, `B(n)≤1[W(n)>T]` for all `n≡1 (Q)`) with

```
μ ≥ exp(−C(Σ+1)),   log(M_1/μ) ≤ C(Σ+1),   log max_i d_i ≤ C(Σ+1) log max_ℓ ℓ^{e_ℓ},
```

and the twist condition `|μ_ψ|≤μ/4` holds for every real primitive ψ required by PO Theorem 4.1 (conductor
`f>1`, `gcd(f,Q)=1`, `f|d_i` for some i). Here C
is absolute (astronomically large; see Lemma 2.1).

*Proof.* **Step 1 (hubs).** Apply Lemma 2.2 with δ. By (W), the new singles
satisfy `g_ℓ^+ ≤ 1/32+1/32 = 1/16`, `S_1^+ ≤ S_1+2S_2/δ`, every vertex has
degree `≤δ`, and (I) still holds for the new system. Write `A(n)` for its
occurring events.

**Step 2 (LLL lower bound).** Use the asymmetric local lemma (Erdős–Lovász;
Alon–Spencer Lemma 5.1.1) on all singles and edges with `x_E=2P(E)`; two
events are adjacent iff their supports meet. For a single at ℓ, the
neighbours are edges at ℓ, and `∏(1−x)≥1−2w_ℓ≥1/2`. For an edge at `ℓ,ℓ'`,
`∏(1−x) ≥ (1−1/8)²(1−2w_ℓ−2w_{ℓ'}) ≥ 1/2`. So the condition
`P(E)≤x_E∏_{E'∼E}(1−x_{E'})` holds, and

```
P(A=∅) ≥ ∏_E(1−x_E) ≥ exp(−3(S_1^+ + S_2)) =: e^{−λ}      (1−x≥e^{−1.1x} for x≤1/8).
```

We also use the conditional form (Haeupler–Saha–Srinivasan, J. ACM 58
(2011), Thm 2.1; it is also immediate from the Alon–Spencer proof): if the
condition holds for a family 𝒜 and an event B is mutually independent of the
events of 𝒜 outside `Γ(B)`, then
`P(B | ∩_{𝒜}Ā) ≤ P(B)∏_{A∈Γ(B)}(1−x_A)^{−1}`.

**Step 3 (the minorant).** Let `Λ=Λ_{16}` (Lemma 2.1: `Λ≤16S_1^++16e^{98}S_2`).
Choose the least L with `4^{L+1} ≥ 200e^{Λ+λ}`, and set `B:=B*_L` (Lemma
1.2), expanded into unit congruence classes. Then:

* `B≤1[A=∅]≤1[W>T]` on `n≡1 (Q)`, by Lemma 1.2 and (I).
* `E|B−1[A=∅]| ≤ 2·4^{−(L+1)}e^{Λ} ≤ e^{−λ}/100 ≤ P(A=∅)/100` (Lemma 1.3),
  so `μ ≥ 0.99 P(A=∅) ≥ 0.99e^{−λ}`.
* `M_1 ≤ e^{Λ} + 4^{L+1}EG ≤ 2e^{Λ}` (Lemma 1.3), so
  `log(M_1/μ) ≤ Λ+λ+1`.
* Each term lives on at most `2(L+1)` primes of 𝒫, and
  `L ≤ (Λ+λ)/log 4 + 5`.

All of `Λ, λ, L` are `O(S_1+S_2/δ+S_2+1)=O(Σ+1)`.

**Step 4 (twist).** Let ψ be real primitive with conductor `f>1`,
`gcd(f,Q)=1`, `f|d_i` for some i. Then f is odd and squarefree (`2|Q`), and
its primes lie in 𝒫; fix one, `ℓ_0`. If `f∤d_i`, some prime of f does not
divide `d_i`, and the character sum over that coordinate vanishes; so
`μ_ψ = E[Bψ]` (Haar). Hence

```
|μ_ψ| ≤ E|B−1[A=∅]| + |E[1[A=∅]ψ]|.
```

Let `Ā'` be "no event whose support avoids `ℓ_0` occurs", a function of
`X_{−ℓ_0}`. Then `1[A=∅] = 1_{Ā'}·1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]`, where Forb
is the union of `S^+_{ℓ_0}` and the vertices at `ℓ_0` joined to an occurring
vertex. Write `ψ=χ_0(X_{ℓ_0})ψ'(X_{−ℓ_0})`, `χ_0=(·/ℓ_0)`. Since
`E χ_0(X_{ℓ_0})=0`,
`|E_{X_{ℓ_0}}[1[X_{ℓ_0}∉Forb]χ_0]| = |E_{X_{ℓ_0}}[1[X_{ℓ_0}∈Forb]χ_0]| ≤ P_{X_{ℓ_0}}(Forb)`. So

```
|E[1[A=∅]ψ]| ≤ P(Ā' ∩ {an event at ℓ_0 occurs}) ≤ P(Ā')·( g^+_{ℓ_0} + Σ_{edges {u,w}, u at ℓ_0} p(u)·P(w occurs | Ā') ).
```

The single at `ℓ_0` and `X_{ℓ_0}` are independent of `Ā'`. The event "w
occurs" depends on `X_{ℓ_w}` only; its neighbours in the family defining
`Ā'` are the single and the edges at `ℓ_w`, with
`∏(1−x)≥(7/8)(15/16)>0.82`. The conditional LLL gives
`P(w|Ā')≤1.22p(w)`. So the bracket is `≤ 1/16+1.22w_{ℓ_0} < 0.064`, while
`P(A=∅) = P(Ā') − P(Ā'∩{…}) ≥ 0.936 P(Ā')`. Therefore

```
|μ_ψ| ≤ P(A=∅)(0.01 + 0.064/0.936) < 0.08 P(A=∅) < μ/4.  ∎
```

*Remark.* Nothing in Theorem 3.1 refers to primes being prime numbers beyond
the CRT; it is a statement about congruence combinatorics, exactly the shape
of H_MIN. The analytic transfer is PO Theorem 4.1, untouched.

## 4. Application: H_MIN(θ) for every θ>1/3, and `W(p) > (log p)^{3−o(1)}` i.o.

Put `𝓛=log T`, `τ*=τ*(T+2)=max_{n≤T+2}τ(n)` (so
`τ*≤exp((log 2+o(1))𝓛/log 𝓛)`, Wigert), and

```
y := T^{1/3}·exp(2𝓛/log 𝓛),     Π_0 := {primes ℓ≤y}.
```

For a set Π of primes and `M≤T`, `M≡3 (4)`, write `M=m_Π(M)·r_Π(M)` with
`m_Π` the Π-part. An atom `(M,D)`, `D|A_M²`, **survives Π** if
`m_Π | 4D+1` and `r_Π>1`; its Haar weight is `1/φ(r_Π)`.

**Lemma 4.1 (global mass for any class-of-one quarantine; PROVED).** For
every set Π of primes,

```
S_tot(Π) := Σ_{atoms surviving Π} 1/φ(r_Π) ≤ C log log T·(3+𝓛)·Σ_{s r'² ≤ T, s squarefree} τ(4sr'²+1)/(s r') ≤ exp((log 2+o(1))𝓛/log 𝓛).
```

*Proof.* This is PO Lemma 9.2 (stated there for `Π={ℓ≤z}`); the proof uses
only `m:=m_Π(M) | M` and `m | 4D+1`. In detail: `1/φ(r) ≤ C log log T·m/M ≤
C log log T·m/(3A)`. The involution `D↦A²/D` preserves `m|4D+1` (because
`4A≡1 (m)`), so take `D≤A` at a factor 2. Write `D=sr'²`, `A=sr'k`,
`k≥r'`. Then `m | 4sr'(r'+k)` and `gcd(m,4sr')=1`, so `m|r'+k`. For fixed
`(s,r')` each k determines M, hence m, and `m|4sr'²+1`. So the sum is at
most `(2C log log T/3)Σ_{s,r'}(sr')^{−1}Σ_{m|4sr'²+1} m Σ_{k≡−r' (m), r'≤k≤X} 1/k`
(`X=(T+1)/4`, since `k≤A≤X`),
and the inner k-sum is `≤(3+log T)/m` (PO Lemma 2.3, step 3). The last
bound is the divisor bound, as in PO Lemma 2.3. ∎

(Modulo Elsholtz–Tao Prop. 1.4 the bound is `≪(log T)^4 log log T`, PO
Lemma 9.2; we do not need this.)

**Construction 4.2.**

1. `g^{(0)}_ℓ` (`ℓ>y`): the Haar measure of the set of `n mod ℓ^{e_ℓ}`
   (units; `e_ℓ=max{e:ℓ^e≤T}`) hit by atoms surviving `Π_0` with
   `r_{Π_0}∈{ℓ,ℓ²}`. Bad primes: `𝓑 := {ℓ>y : g^{(0)}_ℓ > 1/64}`. Then
   `|𝓑| ≤ 64 S_tot(Π_0)`.
2. `Π := Π_0∪𝓑`, `Q := lcm(24, ℓ^{e_ℓ} : ℓ∈Π)`, `𝒫 := {y<ℓ≤T}∖𝓑`.
3. Every atom surviving Π has `r=r_Π ≤ T` with all prime factors in 𝒫,
   hence `>T^{1/3}`; so `r∈{ℓ, ℓ², ℓℓ'}`. If `r∈{ℓ,ℓ²}` it contributes the
   class `−4D mod r` (lifted to `mod ℓ^{e_ℓ}`) to the single `S_ℓ`. If
   `r=ℓℓ'` it is the edge `−4D mod ℓℓ'`.

**Lemma 4.3 (hypotheses of Theorem 3.1; PROVED).** For T large:

* (I) holds: if `n≡1 (mod Q)` and no single and no edge of 4.2 occurs at n,
  then `W(n)>T`.
* (W) `w_ℓ ≤ 8τ*²T/y³ ≤ exp((2log 2−6+o(1))𝓛/log 𝓛) → 0` for all `ℓ∈𝒫`.
* (G) `g_ℓ ≤ 1/64 + 2|𝓑|τ*²T/y³ ≤ 1/32` for all `ℓ∈𝒫`.
* `Σ = S_1+S_2 ≤ S_tot(Π) ≤ exp((log 2+o(1))𝓛/log 𝓛)`.
* `log Q ≤ (π(y)+|𝓑|)𝓛 + log 24 ≤ 5y`.

*Proof.* (I) Let `M≤T`, `M≡3 (4)`, `m=m_Π(M)`, `r=r_Π(M)`. Every prime
power `ℓ^v‖M` with `ℓ∈Π` has `ℓ^v≤T`, so `m|Q` and `n≡1 (m)`. If `r=1`,
`n≡1 (M)` and Fact 1.1 gives `n mod M∉𝓡(M)`. If `r>1` and `n≡−4D (M)` with
`D|A_M²`, then reducing mod m gives `m|4D+1` (m is odd), so `(M,D)` survives
Π, and reducing mod r shows that its single or edge occurs.

(W) An edge at ℓ comes from an atom with `M=mℓℓ'`, `ℓ'∈𝒫`, `m≤T/(ℓℓ')`,
and each M carries at most `τ(A_M²)≤τ*²` atoms. With
`1/((ℓ−1)(ℓ'−1))≤4/(ℓℓ')`:
`w_ℓ ≤ Σ_{ℓ'>y} (T/(ℓℓ'))τ*²·4/(ℓℓ') ≤ 8τ*²T/(ℓ²y) ≤ 8τ*²T/y³`, and
`T/y³ = exp(−6𝓛/log 𝓛)`.

(G) Atoms with `r_Π∈{ℓ,ℓ²}` either survive `Π_0` with the same rough part
(counted in `g^{(0)}_ℓ≤1/64`, since `ℓ∉𝓑`), or have `M=m b ℓ` with `b∈𝓑`
(not `bℓ²` or `b²ℓ`, which exceed `y³≥T`). There are at most
`|𝓑|·T/(yℓ)` such M, each with `≤τ*²` atoms, each of Haar weight
`≤2/ℓ`. With `|𝓑|≤64S_tot(Π_0)` and Lemma 4.1 the extra term is
`exp((3log 2−6+o(1))𝓛/log 𝓛)→0`.

Mass: by the union bound `g_ℓ ≤ Σ_{single atoms at ℓ}1/φ(r)`, and each edge
has `p(u)p(w)=1/φ(ℓℓ')`; apply Lemma 4.1 with Π.

`log Q`: each `ℓ∈Π` contributes `e_ℓ log ℓ ≤ 𝓛`, and
`π(y)𝓛 ≤ (1.26y/log y)·𝓛 ≤ 4y` because `𝓛/log y → 3`; `|𝓑|𝓛=T^{o(1)}`.
(Unlike PO Fact 1.2, every `ℓ≤y<√T` now has `e_ℓ≥2`; this costs only a
constant factor.) ∎

## 5. The theorem

**Theorem 5.1 (PROVED modulo Thorner–Zaman, exactly as PO Theorem 5.1;
effective).** There is an absolute constant C such that for infinitely many
Mordell-hard primes p,

```
W(p) ≥ (log p)^3 · exp(−C log log p / log log log p).
```

More precisely, for every large T there is a prime `p≡1 (mod 840)` with
`W(p)>T` and `log p ≤ T^{1/3}exp(O(log T/log log T))`; so
`log L_h(T) ≤ T^{1/3+o(1)}`. In the language of PO §6.2, **H_MIN(θ) holds
for every θ>1/3** (indeed with `θ=1/3` and `T^{o(1)}=exp(O(𝓛/log 𝓛))`).

*Proof.* Lemma 4.3 verifies the hypotheses of Theorem 3.1 for Construction
4.2. Theorem 3.1 gives a minorant B with `K:=1+log(M_1/μ) ≤
exp(O(𝓛/log 𝓛))`, moduli `log d_i ≤ exp(O(𝓛/log 𝓛))`, the twist condition,
and quarantine `log Q≤5y`. Follow PO Theorem 6.2: let `ℓ_0` be a prime in
`(R,2R]`, `R=max(T, max_i d_i)`, and replace Q by `Qℓ_0`. The minorant
inequality persists on the subclass; `ℓ_0` is coprime to every `d_i`
(all prime factors of `d_i` are `≤T<ℓ_0`); μ, `M_1` and every `μ_ψ` are
unchanged; `log Z ≤ 5y + log 2R + log max d_i ≤ 6y`. PO Theorem 4.1 yields
a prime `p≡1 (mod Qℓ_0)` with `W(p)>T` and

```
log p ≤ C_1 K max(log Z, K) ≤ y·exp(O(𝓛/log 𝓛)) = T^{1/3}·exp(O(𝓛/log 𝓛)).
```

`840|Q` because `y≥7`, so p is Mordell-hard; `p>ℓ_0>T`, so distinct T give
infinitely many distinct p. Inverting: if `𝓛 ≥ 4 log log p` then already
`W(p)>T≥(log p)^4`; otherwise `𝓛/log 𝓛 ≪ log log p/log log log p`, and
`log log p ≤ 𝓛/3 + O(𝓛/log 𝓛)` gives
`𝓛 ≥ 3 log log p − O(log log p/log log log p)`. ∎

**Corollaries and scope.**

* This improves PO Theorem 5.1 (exponent 2) to exponent 3, and refutes
  `H_MOD(A)` (notes (51.19)) for every `A<3`, with the same citation label.
* The prime side now matches the best proved Haar bound,
  `log(1/δ*(T)) ≤ T^{1/3+o(1)}` (PO Theorem 9.3). Both are limited by the same
  crude per-prime estimate (W), `w_ℓ≲T^{1+o(1)}/(ℓ²y)`.
* PO Prop. 6.3 (event-level Bonferroni fails because of hubs) remains true;
  it is not an obstruction to H_MIN. The hub classes are handled by two
  devices: support truncation (Lemma 1.2), whose error grows exponentially in
  the number of *primes* rather than events, and the Markov-cheap quarantine
  of high-degree hub *vertices* (Lemma 2.2), after which the pseudoforest
  bound (Lemma 2.1) controls the moments.
* **Corollary 5.2 (joint statement; PROVED modulo Thorner–Zaman).** For
  infinitely many hard p, jointly `W(p)≥(log p)^{3−o(1)}` and
  `ck_min(p)≥(log p)^{1−o(1)}`. *Proof.* The primes of Theorem 5.1 are
  `≡1` mod 24 and mod every prime `ℓ≤y`. Since `p≡1 (4)`, reciprocity gives
  `(ℓ/p)=(p/ℓ)=1` for odd `ℓ≤y`. PO Lemma 8.1 (`ck_min>B` when
  `(ℓ/p)=1` for all `5≤ℓ≤B`) gives `ck_min(p)>y`, and
  `y=T^{1/3}e^{2𝓛/log 𝓛}≥(log p)^{1−o(1)}`. This upgrades PO Cor. 8.2,
  which had exponent 2 for W. ∎
* PO Prop. 6.1 (prime-local designs cap at exponent 2) is untouched: the
  design here is not prime-local (two unquarantined primes per modulus are
  allowed).

## 6. EVIDENCE and finite-T status

* `scripts/omega2_abstract_check.py` (brute force over random event systems
  with supports of size ≤3, all outcomes, all `L≤|𝒫|+1`): Lemma 1.1's closed
  form equals the definition of `B_L`, and both inequalities of Lemma 1.2
  hold. 0 failures in 207 361 (seed 1) and 1 166 784 (seed 7) cases.
* `scripts/omega2_es.py` builds Construction 4.2 at finite T. **It is an
  illustration, not an instance of the theorem**: the theorem's constants
  (`δ=e^{−50}`, bad-prime threshold `1/64`, `y=T^{1/3}e^{2𝓛/log 𝓛}`) are
  far outside the accessible range. With the threshold 1/64, at
  `T=10^4, θ=0.4`, 245 primes are bad and *no* edge survives. With an
  illustrative threshold `g>1/4` and `δ=0.05`:

| T | θ | log Q | free primes | `S_1` | edges | `S_2` | max `w_ℓ` | hub vertices (`deg>0.05`) | hub mass | max deg after |
|---|---|---|---|---|---|---|---|---|---|---|
| 10⁴ | 0.40 | 109 | 1215 | 15.3 | 3529 | 0.63 | 0.18 | 555 | 8.2 | 0.048 |
| 10⁵ | 0.36 | 187 | 9573 | 29.0 | 101057 | 2.53 | 0.26 | 5013 | 29.1 | 0.039 |

  * The hub vertices sit at the smallest free primes (`ℓ=41,53` at `10^4`;
    `ℓ=67,73,79` at `10^5`), as (W) predicts (`w_ℓ≲T/(ℓ²y)`). Their actual
    mass is about a third of the Markov bound `2S_2/δ` (25.3 and 101.0).
  * Monte Carlo of the reduced system (2000 resp. 500 samples): no sample
    had more occurring events than active primes (`#events>N` in 0
    samples).
  * At these T the hub-vertex quarantine costs as much as the singles, and
    `P(A=∅)` is below the Monte Carlo resolution. So the minorant is not
    useful numerically; only the asymptotic statement is claimed.
  * The exact Lemma 1.2 check inside this script runs only on samples with
    `N≤12`; at `T=10^5` there are none, so that line is vacuous there
    (Lemma 1.2 is covered by the abstract brute force). Neither run tests
    Lemma 2.1 quantitatively.
  * Data: `data/omega2/es_1e4_0.4.txt`, `es_1e5_0.36.txt`.
* **Implication (I), directly** (`omega2_es.py checkI`): integers
  `n≡1 (Q)` built by CRT from residues at the free primes; 'forced'
  samples avoid every single and edge (rejection). At `T=1000, θ=0.4`
  (200 forced) and `T=3000, θ=0.36` (100 forced), every forced survivor
  has `W(n)>T` checked against the witness residues of every M≤T directly; 0 mismatches. Random
  samples (non-units allowed) never avoided all events at these T.
  (`data/omega2/checkI.txt`.)

## 7. Below θ=1/3: what is missing (Assessment)

Theorem 5.1 uses `θ>1/3` in exactly two places.

1. **Per-prime smallness.** (W) and (G) are proved by the crude count
   `w_ℓ ≤ 8τ*²T/(ℓ²y)`, which is `o(1)` only for `y≥T^{1/3+o(1)}`. This is the
   same estimate that limits the Haar bound (PO Thm 9.3), and it is what
   PO's H_PP replaces. Below 1/3 the smallest free primes carry `w_ℓ≫1`
   under the crude bound; whether they actually do is the H_PP question
   (PO §9 EVIDENCE: the ratio is `<1` only for `z≳T^{0.6}` at accessible T).
2. **Supports of size ≤2.** For `θ<1/3` (more precisely `y<T^{1/3}`) there are events on three or more
   free primes. Lemmas 1.1–1.3 are support-size free. Lemma 2.1 is proved
   for graphs only. Its hypergraph analogue needs a codegree hypothesis:
   in a k-uniform pseudoforest a new hyperedge may contain several old
   vertices, and the number of such "closing" hyperedges is not bounded by
   one per component. We have not proved a hypergraph version.

So the honest status below 1/3 is: **H_MIN(θ) for θ<1/3 would follow from a
per-prime/codegree hypothesis of H_PP type plus a hypergraph form of
Lemma 2.1.** Neither is proved. In particular the prime side and the Haar
side now stand at the *same* exponent (3), and any further progress on
the Haar side that goes through per-prime local-lemma conditions is likely
to transfer by the method of §§1–3 (Assessment, not a theorem).

## 8. Checkpoint 2: single-coordinate masses are Elsholtz–Tao Type I counts

Notation: Elsholtz–Tao (arXiv:1107.1010, archived as
`sources/elsholtz-tao-1107.1010.pdf`; cited as ET) define `Σ_I^n` as the set
of sextuples `(a,b,c,d,e,f)` obeying their (2.1)–(2.9), e.g.

```
4abd = ne+1,  ce = a+b,  4acd = n+f,  ef = 4a²d+1,  bf = na+c.
```

Put `F_I(n) := #{(a,b,c,d,e,f) ∈ ℕ⁶∩Σ_I^n : a≤b}`.

**Lemma 8.1 (dictionary; PROVED).** Let `r>1` be odd. Consider the atoms
`(M,D)` with `M=mr≡3 (4)`, `D|A_M²`, `m|4D+1`, `D≤A_M` (any `m≥1`). They
correspond bijectively to the points of `ℕ⁶∩Σ_I^r` with `a≤b` and d
squarefree, via

```
a=r',  b=k,  c=(r'+k)/m,  d=s,  e=m,  f=(4D+1)/m,    where D=sr'², A_M=sr'k (s squarefree).
```

The atom's class is `−4D ≡ −a/b (mod r)`. Consequently the number `E(r)` of
distinct classes mod r carried by atoms with rough part r (for any
quarantine, including partners `A²/D`) satisfies `E(r) ≤ 2F_I(r)`.

*Proof.* PO Lemma 2.3/9.1 shows `m|r'+k`, so c is a positive integer. Then:

* (2.1) holds: `4abd=4sr'k=4A_M=mr+1`.
* (2.2) is the definition of c.
* (2.7) holds: `ef=4sr'²+1=4a²d+1`.

By direct computation, (2.1), (2.2) and (2.7) with nonzero entries imply the
remaining identities; we check the two we use by hand. (2.6):
`e·4acd = 4ad(a+b) = 4a²d + 4abd = (ef−1) + (ne+1) = e(f+n)`. (2.8):
`e·bf = b(4a²d+1) = a(ne+1)+b = ane+ce`, so `bf=an+c`. Conversely, a point with `a≤b` and d squarefree gives `D=da²`,
`A=dab`, `M=ne`, `m=e`. Here `D|A²` and `D≤A`. Also `m|4D+1`, by (2.7).
And `M=4A−1≡3 (4)`. The map is injective, because `(s,r',k)` determine D
and A, hence M. Finally, `4A≡1 (r)` gives `−4D = −4A·(r'/k) ≡ −r'/k`. The
partner class `−(4D)^{−1}` at most doubles the count. ∎

EVIDENCE (`scripts/omega2_ffull.py dict 2001`): for every odd `r≤2001`
(primes, prime powers, composites) the atom enumeration via PO's
`(s,r',v)` parametrisation and the Type I enumeration via `(a,c,d)` give
identical sets: 32 241 atoms, 0 mismatching r. The parametrisation also
reproduces PO's `F_full(ℓ)` exactly at `ℓ=107, 331, 1031, 3011`.

*Remark.* So `|F_ℓ^{full}|`, the T-independent single-prime forbidden set of
PO §9, is at most twice the number of Type I representations
`4/ℓ = 1/(abdℓ) + 1/(acd) + 1/(bcd)`. The Lemma 9.1 "atoms" are exactly
the Type I solutions of ES for the rough part.

**Proposition 8.2 (sizes of `F_I`).**

1. *(PROVED modulo the proof of ET Prop. 1.7, i.e. its Lemma 2.8 and §3; cited.)* `F_I(n) ≤ n^{3/5+O(1/log log n)}`
   for every n. Hence `|F_ℓ^{full}| ≤ ℓ^{3/5+o(1)}` and
   `g_ℓ^{full}:=|F_ℓ^{full}|/(ℓ−1) ≤ ℓ^{−2/5+o(1)}`. More generally, the
   single-coordinate classes at `ℓ^e` number at most `ℓ^{3e/5+o(1)}`.
   Here ET's proof counts points of `Σ_I^n` that obey the bounds of their
   Lemma 2.8. The proof of that lemma uses only the identities,
   positivity and `a≤b`, so it applies to every point counted by `F_I`.
2. *(PROVED, elementary.)* Let ℓ be prime and `A_0≥1`. The points of
   `Σ_I^ℓ` with `a≤A_0` number at most
   `τ*(2A_0ℓ)·(A_0² + 3A_0^{3/2}√(ℓ+1))`. Those with `a=1` number
   `≪√ℓ log ℓ`. In particular the atoms with `r'≤ℓ^{o(1)}` contribute
   `ℓ^{1/2+o(1)}` classes.

*Proof of 2.* The point is determined by `(a,c,f)`, by (2.6) and (2.2).

* `ℓ∤c`: otherwise ℓ divides `y=acd` and `z=bcd` as well as `x=abdℓ`,
  and `4 = ℓ/x+ℓ/y+ℓ/z ≤ 3`. Hence `g:=gcd(c,f)`, which divides `ℓa+c`
  and `ℓ+f` (by (2.8), (2.6)), divides ℓ, so `g=1`.
* Then `f|aℓ+c` and `c|a(ℓ+f)` give `cf | a(ℓ+f)+c`, so
  `(c−a)(f−1) ≤ a(ℓ+1)`.
* If `f≤1+√(a(ℓ+1))`: we have `f≡−ℓ (mod 4a)` by (2.6). That leaves at
  most `√(ℓ+1)/(4√a)+2` values of f, and for each, c divides `ℓ+f`.
* Otherwise `c≤a+√(a(ℓ+1))`, and f divides `aℓ+c`.

Summing over `a≤A_0` gives the bound. For `a=1` both cases are sums of
`τ(ℓ+j)` over `j≤2+√ℓ`. By `τ(n)≤2#{δ|n: δ≤√n}`, each is
`≤2Σ_{δ≤√(2ℓ)}(√ℓ/δ+1) ≪ √ℓ log ℓ`. ∎

EVIDENCE (`omega2_ffull.py`): `#triples/√ℓ` = 1.64, 1.59, 2.09, 1.26 at
`ℓ=107, 331, 1031, 3011`. At the Linnik-type hub prime
`ℓ=87359` (`(ℓ+1)/4=2^4·3·5·7·13`) it is 4.14, with 1224 triples and 923
classes. Most triples have `r'>1` (1147 of 1224 at 87359), and `r'` reaches
`≈ℓ/4`, so part 2 alone does not cover them.

**Remark 8.3 (why `ℓ^{1/2}` is not proved; Assessment, with an exact
computation).** A bound `F_I(ℓ)≤ℓ^{1/2+o(1)}` for all `a` would improve ET
Prop 1.7 at primes. ET remark that 3/5 "appears to be the limit of what
one can obtain purely from the divisor bound". We confirm this for the
natural determining quantities.

* Each of `e, f, cd, ac, a²d, ab, bd, bf` fixes the point up to
  `n^{o(1)}` choices, via (2.1), (2.6), (2.9), (2.8), (2.7), (2.2)+(2.1), (2.1)
  and (2.8) respectively, together with the divisor bound.
* Consider the box `a≍n^{2/5}, c≍n^{1/5}, d≍n^{2/5}, b≍n^{4/5}`, so that
  `e≍f≍n^{3/5}`. It is consistent with all identities and with Lemma 2.8.
  There these quantities have sizes
  `n^{3/5}, n^{3/5}, n^{3/5}, n^{3/5}, n^{6/5}, n^{6/5}, n^{6/5}, n^{7/5}`.
* So every "fix one determining quantity" argument costs `≥n^{3/5}` in
  this box.
* The progression trick of part 2 (fix a; then `f≡−ℓ (4a)`) gives about
  `√(aℓ)` per a, i.e. `n^{0.7}` per a in the box.
* Heuristically the box contains `O(n^{o(1)})` points. The `(a,c,d)` with
  `|4acd−n|≤n^{3/5}` number about `n^{3/5}`, and each needs
  `f | 4a²d+1` with `f≍n^{3/5}`.

Beating 3/5 there is a genuine lattice-point/equidistribution problem,
which we do not attempt.

## 9. What a per-prime (H_PP-type) input buys

Here `w_ℓ=w_ℓ(T,z)` is PO §9's per-prime event mass after the class-of-one
quarantine at the primes `≤z`, and `E_T(r)` is the number of distinct
surviving events (classes mod r) with rough part r and `M≤T`.

**Lemma 9.1 (per-prime mass through Type I counts; PROVED).** For every
prime `ℓ>z`,

```
w_ℓ = Σ_{r≤T, ℓ|r} E_T(r)/φ(r) ≤ C log log T · Σ_{r≤T, ℓ|r} min(2F_I(r), τ*² T/r)/r.
```

*Proof.* `E_T(r)≤2F_I(r)` by Lemma 8.1, for any quarantine. Also
`E_T(r)≤#{atoms with M=mr≤T}≤(T/r)τ*²`. Finally `1/φ(r)≤C log log T/r`. ∎

**Theorem 9.2 (conditional Haar exponent; PROVED implication).** Suppose
`F_I(n) ≤ n^{η+o(1)}` for all n, for some `0≤η≤1`, and put `κ=η/(1+η)`.
Then:

* `w_ℓ(T,z) ≤ T^{κ+o(1)}/ℓ` for every z and every prime ℓ;
* H_PP(`T^{κ+ε}`) holds for every `ε>0` and large T;
* `log(1/δ*(T)) ≤ T^{κ+o(1)}`.

*Proof.* Put `R=T^{1/(1+η)}` and split Lemma 9.1's sum at `r=R`:

```
Σ_{r≤R, ℓ|r} r^{η−1+o(1)} ≤ ℓ^{η−1}Σ_{j≤R/ℓ} j^{η−1} T^{o(1)} ≤ R^{η}T^{o(1)}/ℓ,     Σ_{r>R, ℓ|r} τ*²T/r² ≤ 2τ*²T/(ℓR).
```

Both are `T^{κ+o(1)}/ℓ`. For `ℓ>z=T^{κ+ε}` this is
`T^{−ε+o(1)} ≤ log z/(8 log T)`, which is H_PP(z). PO Theorem 9.4 then
gives `log(1/δ*) ≤ π(z)log T + 4S_tot + O(1)`, with
`S_tot=T^{o(1)}` (Lemma 4.1; its proof needs only this, not ET Prop 1.4). ∎

**What this means (Assessment, with the exact bookkeeping above).**

1. **ET's exponent 3/5 gives κ=3/8.** This is *worse* than PO Theorem 9.3's
   unconditional 1/3. Theorem 9.3 uses only the crude count, with all
   rough primes `>T^{1/3}`.
2. **η=1/2 gives exactly κ=1/3.** So the bound `|F_ℓ^{full}|≤ℓ^{1/2+o(1)}`
   I originally aimed at, even proved for every n, would only *reproduce*
   the 1/3 barrier. The crude bound `(T/r)τ*²` and `r^{1/2}` cross at
   `r=T^{2/3}`, with value `T^{1/3}`; that is where the 1/3 comes from.
   **Beating 1/3 through individual counts needs η<1/2**, i.e. a Type I
   bound well beyond ET Prop 1.7 and the divisor-bound limit of
   Remark 8.3.
3. **The single-coordinate part was never the bottleneck.**
   * By Prop 8.2.1, `g_ℓ^{full} ≤ ℓ^{−2/5+o(1)}`, so for
     `z ≥ (log T)^{5/2+ε}` the single-coordinate part of H_PP(z) holds
     (modulo ET Prop 1.7). So **H_PP(z) reduces to its multi-prime part**
     for such z.
   * But both PO Thm 9.3 and our Construction 4.2 already absorb the
     single part by quarantining `T^{o(1)}` bad primes. So this buys
     nothing for the Haar exponent or for θ<1/3. Its only use is cosmetic:
     modulo ET, `𝓑=∅` for large T in Construction 4.2.
4. **The real target is an averaged statement.** The per-prime input
   needed is the progression average
   `(AP-TI)  Σ_{r≤T, ℓ|r} F_I(r)/r ≤ T^{κ+o(1)}/ℓ` uniformly in primes
   `ℓ≤T`. Theorem 9.2's proof uses exactly this. AP-TI with `κ=o(1)` would
   give `log(1/δ*)=T^{o(1)}`. On average ET Theorem 1.1 gives
   `Σ_{n≤N}f_I(n) ≍ N log³N`, so AP-TI(o(1)) is the natural conjecture.
   * It cannot hold in the stronger form `polylog/ℓ`. PO's Linnik
     example has `ℓw_ℓ ≥ exp(c log ℓ/log log ℓ)`, coming from the single
     term `r=ℓ`.
   * In ET coordinates, `ℓ|r` is the congruence `4acd≡f (mod ℓ)`, with
     `f | 4a²d+1`. For fixed `(a,d,f)`, c then runs over one class mod ℓ,
     and summing `1/c` there gives `(log T)/ℓ` plus a "first term"
     `1/c_0(a,d,f)`.
   * The full sum of the regular parts is
     `≪(log T/ℓ)Σ_{a,d}τ(4a²d+1)/(ad)`, which is polylogarithmic by ET
     Prop 1.4.
   * So AP-TI(o(1)) reduces (an upper-bound reduction; terms with `ℓ|ad` vanish,
     since they force `ℓ|f|4a²d+1≡1 (mod ℓ)`) to controlling the
     first terms `Σ_{a,d,f}1/(ad·c_0)`, where
     `c_0 ≡ f(4ad)^{−1} (mod ℓ)`. This is the Kloosterman-type
     equidistribution flagged in PO §9, now in explicit form.
5. **Prime side, θ<1/3.** H_MIN(θ) would need the Haar-side input (η<1/2,
   or AP-TI with κ<1/3) *and* a hypergraph form of Lemma 2.1 (§7). Neither
   is available.

## 10. Below θ=1/3: a hypergraph minorant and what it needs

### 10.1 Private covers (PROVED)

Setting 1.0, with supports of size `≤k` (`k≥1`). For a set P of primes, a
*private cover* of P is a set C of events such that:

* `P ⊆ ∪_{E∈C} supp E`;
* every `E∈C` has a prime of `supp E ∩ P` that lies in the support of no
  other member of C (its *private prime*).

Then `|C|≤|P|`. Put

```
G^cov_u(x) := Σ_{|P|=u} Σ_{C private cover of P} 1[every E∈C occurs at x].
```

**Lemma 10.1 (PROVED).** For every outcome x and all `u, L ≥ 0`:

1. `binom(N(x),u) ≤ G^cov_u(x)`. Hence Lemma 1.2 holds with `G^cov_{L+1}`
   in place of `G_{L+1}`:
   `B_L − 4^{L+1}G^cov_{L+1} ≤ 1[A=∅]` and
   `|B_L−1[A=∅]| ≤ 4^{L+1}G^cov_{L+1}`.
2. If every event is a union of cells, then
   `M_1(B_L) ≤ Σ_{u≤L} 2^u E G^cov_u`, and `M_1(G^cov_u)=E G^cov_u`.

*Proof.*

1. Every `P⊆V(x)` is covered by occurring events. A minimal subfamily
   covering P is a private cover: if some member had no private prime in
   P, removing it would leave a cover. So each u-subset of `V(x)`
   contributes at least 1 to `G^cov_u(x)`. The rest is the proof of
   Lemma 1.2 verbatim.
2. In the proof of Lemma 1.3, a cell c on U with `κ(U,c)≠0` has every
   prime of U covered by events supported in U and occurring on c. A
   minimal such subfamily is a private cover of U whose members are
   supported in U. So
   `Σ_c |κ(U,c)|P(c) ≤ 2^{|U|} Σ_{C private cover of U} P(C occurs)`.
   Summing over `|U|≤L` gives the bound. `G^cov_u` has coefficients +1. ∎

EVIDENCE: `scripts/omega2_abstract_check.py` also checks, by brute force,
`binom(N,L+1) ≤ G^cov_{L+1}` and both inequalities of part 1, in the same
207 361 (seed 1) and 1 166 784 (seed 7) cases. There were 0 failures.

### 10.2 The moment bound for hypergraph systems (PROVED)

**Setting 10.0.** As Setting 2.0, but hyperedges replace edges.

* A *hyperedge* is a set of `2..k` vertices at distinct primes. It occurs
  iff all its vertices are realised, so `P(e)=∏_{v∈e}p(v)`.
* The hypergraph is simple: distinct hyperedges have distinct vertex sets.
* Put `S_H=Σ_e P(e)` and `w_ℓ=Σ_{e at ℓ}P(e)`.
* For a set O of vertices at distinct primes, the *codegree* is
  `Δ_O := Σ_{e⊋O} ∏_{v∈e∖O} p(v)`. So `Δ_{{v}}=deg(v)`.
* Put `Δ^{(i)} := max_{|O|=i} Δ_O`.

**Lemma 10.2 (PROVED).** Let `U_0≥1`, `w≥0`, and put

```
D := Σ_{j=0}^{k−2} (kU_0)^j Δ^{(j+1)}.
```

If `D ≤ [2ek(1+w)^k]^{−1}`, then

```
Σ_{u=0}^{U_0} w^u E G^cov_u ≤ exp( (1+w)S_1 + 2ek(1+w)^k S_H ).
```

*Proof.*

**Reduction to private families.** Given C, every P that C privately
covers lies in `π(C)`, the set of primes of C. Hence

```
Σ_{u≤U_0} w^u E G^cov_u ≤ Σ_{C private, |C|≤U_0} (1+w)^{|π(C)|} P(C occurs).
```

Here "C private" means that every member has a prime lying in no other
member.

**Singles.** A single in a private C has its only prime private. So the
singles of C sit on primes disjoint from the rest of C and are independent
of it. They contribute at most `∏_ℓ(1+(1+w)g_ℓ) ≤ e^{(1+w)S_1}`.

**Components.** The hyperedge part splits into connected components, each
private.

* If two components use the same prime with different vertices, they
  cannot occur together.
* Otherwise `P` is multiplicative over components.

So the hyperedge part is at most `exp(Σ_K (1+w)^{|V(K)|}P(K))`, over
connected private K with `h:=|K|≤U_0` hyperedges and `n:=|V(K)|≤kh`
vertices.

**Exploration.**

1. Pick a hyperedge `e_1` of K and declare its vertices discovered.
2. Process the discovered vertices in breadth-first order (ties broken by a
   fixed total order).
3. At a vertex v, attach as *children* all not-yet-attached hyperedges of K
   that contain v. Their vertices are either old (discovered earlier, or
   brought by an earlier sibling) or new; new ones become discovered.

Every hyperedge of K is attached, because K is connected. A child e of v
has a private vertex, which lies in no other hyperedge. That vertex is
therefore new, so `e∖({v}∪old)≠∅`.

Let `O_e` be v together with e's old vertices, with `|O_e|=j+1`. The weight
of e is then the product of p over its new vertices. Summed over all
admissible e, this is at most `Σ_j binom(n,j) Δ^{(j+1)} ≤ D`, since there
are at most n candidates for each old vertex.

**Counting.**

* The first hyperedge contributes
  `Σ_{e_1}P(e_1)·(#roots) ≤ Σ_{e_1}|e_1|P(e_1) ≤ kS_H` in total. (The root
  index only overcounts.)
* The children sets at the at most n processed vertices are unordered:
  `Σ over sets of c children ≤ D^c/c!`.
* The number of weighted compositions is
  `Σ_{c_1+…+c_n=h−1}∏1/c_i! = n^{h−1}/(h−1)! ≤ (kh)^{h−1}/(h−1)! ≤ e(ke)^{h−1}`.

Hence

```
Σ_{K: |K|=h} (1+w)^{|V(K)|}P(K) ≤ (1+w)^{kh}·e·kS_H·(keD)^{h−1},
```

and summing over `h≥1`, with `(1+w)^k keD≤1/2`, gives
`≤2ek(1+w)^kS_H`. ∎

*Remarks.*

* For `k=2` the condition is just `deg≤[4e(1+w)²]^{−1}`. With the private
  covers there is no unicyclic case, so Lemma 2.1 is recovered (with
  different constants) in truncated form.
* The factor `(kU_0)^j` in front of the codegree `Δ^{(j+1)}` is real.
  Consider a cluster in which each new hyperedge reuses `j+1` old vertices
  out of n. It costs only `Δ^{(j+1)}`, but it can be placed in `binom(n,j)`
  ways.
* Only `u≤U_0=L+1` is ever needed (Lemma 10.1), so the codegree condition
  is needed only at size `k(L+1)`.

### 10.3 The hypergraph criterion (PROVED)

**Theorem 10.3 (PROVED).**

*Setting.* Setting 3.0 (congruences, `2|Q`), with singles and hyperedges of
at most k primes. Hyperedges are congruence classes mod r, split into
classes mod `∏_{ℓ|r}ℓ^{e_ℓ}` if necessary, so that all vertices at ℓ are
classes mod `ℓ^{e_ℓ}`; see the remark below.

*Constants.* Put `δ_k := [4ek·17^k]^{−1}`, and let `C_k` be the constant
defined in the proof.

*Hypotheses.*

* (G_k) `g_ℓ ≤ 1/(32k)` for all `ℓ∈𝒫`;
* (W_k) `w_ℓ ≤ δ_k/(32k)` for all `ℓ∈𝒫`;
* (CD_k) `Σ_{j=1}^{k−2} (C_k(Σ+1))^j Δ^{(j+1)} ≤ δ_k`, where `Σ=S_1+S_H`;
* (I) as in Theorem 3.1.

*Conclusion.* The conclusion of Theorem 3.1 holds with constants depending
on k only: a minorant B with `μ≥exp(−O_k(Σ+1))`,
`log(M_1/μ)=O_k(Σ+1)`, moduli on `O_k(Σ+1)` primes, and the twist
condition.

*Proof.* We follow Theorem 3.1. Only the changes are listed.

1. **Hubs.** Forbid the vertices with `deg>δ_k` (Lemma 2.2).
   * The Markov bound reads `Σ_{v∈H at ℓ}p(v) ≤ w_ℓ/δ_k`, because each
     hyperedge at ℓ has exactly one vertex there.
   * Hence `g^+_ℓ ≤ 1/(16k)` and `S_1^+ ≤ S_1+kS_H/δ_k`.
   * Deleting hyperedges only lowers every codegree.
2. **Local lemma.** Take `x_E=2P(E)`.
   * For a single, the neighbours have `∏(1−x) ≥ 1−2w_ℓ ≥ 1/2`.
   * For a hyperedge, the neighbours have
     `∏(1−x) ≥ (1−1/(8k))^k (1−2kδ_k/(32k)) ≥ 0.86`.
   * So `P(A=∅) ≥ e^{−λ}` with `λ=3(S_1^++S_H)`.
3. **Minorant.** Use `B := B_L − 4^{L+1}G^cov_{L+1}` (Lemma 10.1).
   Apply Lemma 10.2 with `w=16` and `U_0=L+1`. Its hypothesis
   `D≤[2ek17^k]^{−1}=2δ_k` follows from `deg≤δ_k` and (CD_k), once
   `C_k(Σ+1) ≥ k(L+1)`. This gives
   `4^{L+1}E G^cov_{L+1} ≤ 4^{−L−1}e^{Λ'}` and
   `M_1(B_L) ≤ Σ_{u≤L}2^uEG^cov_u ≤ e^{Λ'}`, with
   `Λ' := 17S_1^+ + 2ek17^kS_H`. Choose L least with
   `4^{L+1} ≥ 200e^{Λ'+λ}`. Then `L=O_k(Σ+1)`, which defines `C_k`.
   Every term involves at most `k(L+1)` primes.
4. **Twist.** As in Theorem 3.1, Step 4. A hyperedge through `ℓ_0` is
   forced when the event `e∖u` occurs. That event depends on at most `k−1`
   coordinates, and its neighbours have
   `∏(1−x) ≥ (1−1/(8k))^{k−1}·0.99 > 0.86`. So
   `P(e∖u | Ā') ≤ 1.17P(e∖u)`. The bracket is
   `≤ 1/16+1.17w_{ℓ_0} < 0.073`, which gives
   `|μ_ψ| ≤ (0.01+0.079)P(A=∅) < μ/4`. ∎

*Remark (prime powers).*

* For `y<T^{1/3}` an event can have rough part `ℓ²ℓ'`. Its ℓ-vertex is
  then a class mod ℓ², while edges with `ℓ‖r` use classes mod ℓ, so the
  vertex sets at ℓ would overlap.
* Splitting every class mod ℓ (at primes with `e_ℓ=2`) into its ℓ lifts
  mod ℓ² makes all vertices at ℓ classes mod `ℓ^{e_ℓ}`, hence disjoint.
* This replaces one event by ℓ disjoint events with the same union.
  `P`, `w_ℓ`, `deg` and `Δ_O` (for O containing the lifted vertex) are
  unchanged, and the event "no event" is unchanged.

*What changed relative to §3.* The degree condition is still enforced
cheaply by Markov. The new requirement is (CD_k), a bound on the **maximal**
codegrees of sets of `2..k−1` vertices. It cannot be enforced in the same
way; see §10.5.

### 10.4 The conditional theorem, and the codegree hub obstruction

*Withdrawn (review of checkpoint 3).* An earlier version of this section
stated a residue-uniform hypothesis "AP-TI*(κ)": `Δ_O ≤ T^{κ+o(1)}/q_O` for
**all** vertex sets O of the unquarantined system. **That hypothesis is
false for every κ<1/2.**

* Take `T=4ℓ²` with `ℓ≡3 (4)`, and the vertex `v=(ℓ,−4)`.
* For every prime `t∈(ℓ,2ℓ]` with `t≡1 (4)`, the atom `M=ℓt`, `D=1`
  survives. It contributes `1/(t−1)` to `deg(v)`.
* So `deg(v) ≫ 1/log ℓ`, far above `T^{κ}/ℓ`.

Hub residues must be quarantined *before* any maximal codegree condition
is imposed. The theorem below is therefore stated on the quarantined
system. Proposition 10.6 then shows that hub-type residues defeat even that
form.

**Hypothesis H_CD(θ)** (per-prime and codegree smallness after
quarantine; open). For the system at `y=T^θ` there is an additional vertex
quarantine Φ satisfying:

* (i) Φ forbids a set of vertex classes of total mass
  `m(Φ) = T^{o(1)}`;
* (ii) in the system obtained after the class-of-one quarantine at the
  primes `≤y` and at `T^{o(1)}` bad primes, and after forbidding Φ and
  deleting the hyperedges through Φ, there is an `ε>0` with:
  * `g_ℓ ≤ 1/(64k)` and `w_ℓ ≤ T^{−ε}` for every free ℓ,
  * `Δ^{(j+1)} ≤ T^{−ε}` for `1≤j≤k−2`.

Here `k=⌊1/θ⌋`, and all vertices are classes mod `ℓ^{e_ℓ}` (§10.3 remark).

**Theorem 10.4 (PROVED implication, modulo Thorner–Zaman for the last
clause).**

* H_CD(θ) implies H_MIN(θ).
* So if H_CD(θ) holds for every `θ>κ`, then `W(p) ≥ (log p)^{1/κ−ε}`
  for infinitely many hard primes, for every `ε>0`.

*Proof.* After the quarantines, (I) holds by the proof of Lemma 4.3. A
forbidden vertex is a single, so it only strengthens "no event". Then:

* (G_k) holds.
* (W_k) holds, since `w_ℓ ≤ T^{−ε}`.
* (CD_k) holds: `Σ ≤ S_tot(Π)+m(Φ) = T^{o(1)}` (Lemma 4.1), so
  `Σ_j(C_k(Σ+1))^jΔ^{(j+1)} ≤ T^{−ε+o(1)} → 0`.
* `log Q ≤ (π(y)+T^{o(1)})log T ≤ 2y/θ`.

Theorem 10.3 gives a minorant with `log(M_1/μ), log max d_i ≤ T^{o(1)}`
and the twist condition, which is H_MIN(θ). PO Theorem 6.2 does the rest.
∎

For `θ>1/3` (so `k=2`), H_CD(θ) holds with Φ = the hub vertices
(Lemma 4.3). This is Theorem 5.1 again.

**Proposition 10.6 (codegree hubs; PROVED, using the prime number theorem
for a fixed modulus).** Fix `θ<1/3` and an integer `d≥1`. Put
`R:=(y, T^{1/3}]` and `c_θ := log(1/(3θ)) > 0`. For primes
`ℓ_1≠ℓ_2∈R` coprime to 2d, consider the vertices
`v_i=(ℓ_i, −4d² mod ℓ_i^{e_{ℓ_i}})` (lifts as in §10.3). Then, as `T→∞`,

```
Δ_{{v_1,v_2}} ≥ (c_θ − o(1))/φ(4d).
```

The count runs over the vertices `(ℓ_3, −4d²)`, `ℓ_3∈R`, `ℓ_3` in one
fixed class mod 4d, whose hyperedges `{v_1,v_2,(ℓ_3,−4d²)}` are present.

*Proof.* Let `ℓ_3∈R` with `ℓ_1ℓ_2ℓ_3≡−1 (mod 4d)`; this is one unit class
of `ℓ_3` mod 4d. Then:

* `M=ℓ_1ℓ_2ℓ_3≡3 (4)`;
* `M≤T`, since `ℓ_1ℓ_2≤T^{2/3}` and `ℓ_3≤T^{1/3}`;
* `d | A_M`, so `D=d²` divides `A_M²`.

The atom has rough part M (m=1), so it survives `Π_0`. Its class
`−4d² mod M` is the hyperedge through `v_1, v_2` and `(ℓ_3,−4d²)`. Its
weight beyond `{v_1,v_2}` is `p((ℓ_3,·)) ≥ 1/ℓ_3`. Hence
`Δ_{{v_1,v_2}} ≥ Σ_{ℓ_3∈R, ℓ_3≡a (4d)} 1/ℓ_3`. By the prime number theorem
in progressions for the fixed modulus 4d, this is
`(1/φ(4d))(log(log T^{1/3}/log y)+o(1)) = (c_θ+o(1))/φ(4d)`. ∎

**Consequence for Theorem 10.3 (Assessment, with the bookkeeping made
explicit).**

* (CD_3) needs `Δ^{(2)} ≤ δ_3/(C_3(Σ+1))`.
* By Prop. 10.6, for every d with `φ(4d) ≤ c_θC_3(Σ+1)/(2δ_3)`, the
  quarantine Φ must destroy all heavy pairs in the family
  `{(ℓ,−4d²): ℓ∈R}`.
* That is, for each residue pattern, either almost all of the relevant
  `(ℓ_3,−4d²)` vertices are forbidden, or all but a sparse set of the
  `(ℓ_i,−4d²)` vertices are.
* Since `Σ_{ℓ∈R}1/ℓ → c_θ`, a product-set argument in `(ℤ/4d)^×` suggests
  a cost `≫c_θ` per such d. We have *not* proved this lower bound.
* If it holds, then `Σ ≫ c_θ·#{d: φ(4d) ≤ c_θC_3(Σ+1)/(2δ_3)} ≫ c_θ²C_3(Σ+1)/δ_3`.
  That is impossible, because `δ_3` is a tiny absolute constant.
* So, *assuming that cost bound*, Theorem 10.3 as proved cannot certify
  H_MIN(θ) for ES at any `θ<1/3`.
* The obstruction is in Lemma 10.2's factor `(kU_0)^j`. Each child pays
  again for choosing its old vertices, whereas in a `−4d²` cluster the
  shared vertices are few and are reused.
* A heuristic count of private families on such clusters (h private
  vertices, s≤h shared ones) gives `(c²e²/d)^h`. That is harmless for
  `d≫1`, which suggests the true moments are fine.
* **The open step is therefore a sharper Lemma 10.2** that pays once per
  shared vertex (a `1/s!` for the shared set), not a new arithmetic input.
  This is the codegree-level analogue of PO Prop. 6.3, and it is
  circumvented in the same spirit, but we have not done it.

### 10.5 What the hypergraph lemma gives unconditionally (PROVED bookkeeping + Assessment)

**Proposition 10.5 (the available estimates certify nothing below θ=1/3;
PROVED).** Take the system at `y=T^θ` with `θ<1/3`. For a vertex set O
write `q_O=∏_{v∈O}ℓ_v^{e_v}`, where `ℓ_v^{e_v}` is the modulus of v.

1. *Crude counts.* `w_ℓ ≤ Cτ*²T log log T/(ℓ²y)` and, for `|O|≥2`,
   `Δ_O ≤ Cτ*²T log log T/(q'_O y)`. Here `q'_O=∏_{v∈O}ℓ_v`. At the
   smallest free primes these upper bounds are `≥T^{1−3θ−o(1)}`, so they
   do not certify (W_k) or (CD_k).
2. *Individual Type I bounds.* `F_I(n)≤n^η` gives
   `w_ℓ ≤ T^{η/(1+η)+o(1)}/ℓ` (Thm 9.2). For codegrees it gives only
   `T^{η/(1+η)+o(1)}`, whatever the residue pattern. That does not
   certify (CD_k) for any `η>0`.
3. Prop. 10.6 shows that the true maximal pair codegrees are `≍1/φ(4d)`
   on the `−4d²` vertices. So (CD_k) can hold only after a quarantine
   whose cost is discussed in §10.4.

*Proof.*

1. A hyperedge `e⊋O` has rough part `r=r_O·m`. Here `r_O` is the part of r
   supported on the primes of O (possibly with higher powers), and m is
   coprime to `r_O` with all primes above y. There are at most
   `τ*²T/r` atoms at r. The weight beyond O is
   `1/φ(m)·(φ(ℓ^{e_v})/φ(ℓ^{v_ℓ(r)}))^{±}`, which is
   `≤ C log log T/m`. Summing over `m>y` and `r_O ≥ q'_O` gives the bound.
   (This is an upper estimate only.)
2. The split of Thm 9.2's proof applies with `1/φ(m)` in place of
   `1/φ(r)`. The gain `1/q'_O` is lost, and a bound on `F_I(r)` cannot see
   residue classes. ∎

**On quarantining codegrees (Assessment).**

* Degrees are enforced by Markov at a *constant* threshold δ_k.
* Large codegrees could be removed by adding the offending sets O as new
  events. The **Markov upper bound** on the cost of that is
  `binom(k,j+1)S_H/t` at threshold t. With `t≈(C_k(Σ+1))^{−j}` that upper
  bound exceeds Σ. This shows only that the worst-case Markov budget does
  not close. It does **not** show that codegree quarantine is impossible,
  since few sets may actually exceed the threshold.
* The genuine evidence of difficulty is the structured family of Prop. 10.6
  and its cost discussion in §10.4.
* The Haar side (PO Thm 9.4) uses only averaged per-prime masses; the local
  lemma does not see codegrees. This is the precise asymmetry between the
  two sides below θ=1/3.

**Summary of (a)+(b).**

| inputs | prime side (W(p) exponent, i.o.) | Haar side (`log(1/δ*)`) |
|---|---|---|
| unconditional (this note) | 3 (Thm 5.1) | `T^{1/3+o(1)}` (PO Thm 9.3) |
| `F_I(n)≤n^η` | 3 (codegrees uncontrolled) | `T^{η/(1+η)+o(1)}` (Thm 9.2) |
| H_CD(θ) for all `θ>κ` | `1/κ` (Thm 10.4) | `T^{κ+o(1)}` (its `w_ℓ` part, via PO Thm 9.4) |

* The hypothesis H_CD(θ) includes a quarantine of mass `T^{o(1)}`.
* Prop. 10.6 shows that any such quarantine must neutralise the `−4d²`
  codegree hubs for all d up to `≍Σ/δ_k`.
* Whether this is affordable is exactly the open cost question of §10.4.
* The more promising route is a sharper Lemma 10.2.

## Replay

```
export PYTHONPATH=scripts
uv run python scripts/omega2_abstract_check.py 300 1        # Lemmas 1.1-1.2 brute force, ~2 s
uv run python scripts/omega2_abstract_check.py 2000 7       # ~10 s
(ulimit -v 8000000; uv run python scripts/omega2_es.py 10000 0.4 0.05 2000 0.25)    # §6, ~1 min -> data/omega2/es_1e4_0.4.txt
(ulimit -v 8000000; uv run python scripts/omega2_es.py 100000 0.36 0.05 500 0.25)   # §6, ~10 min -> data/omega2/es_1e5_0.36.txt
(ulimit -v 8000000; uv run python scripts/omega2_es.py 10000 0.4 0.05 200 0.015625) # threshold 1/64: no edge survives
uv run python scripts/omega2_es.py checkI 1000 0.4 0.25 200    # (I) directly, ~1 min -> data/omega2/checkI.txt
uv run python scripts/omega2_es.py checkI 3000 0.36 0.25 100   # ~3 min
uv run python scripts/omega2_ffull.py dict 2001                 # §8 Lemma 8.1 dictionary, all odd r<=2001, ~20 s
uv run python scripts/omega2_ffull.py 107 331 1031 3011 87359   # §8 triple counts, ~10 s -> data/omega2/ffull_triples.txt
uv run python scripts/omega2_ffull.py cmp 107 331 1031 3011      # parametrisation reproduces PO F_full, ~5 s
```
