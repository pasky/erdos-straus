# Beyond exponent 2: a support-truncated minorant and `W(p) > (log p)^{3−o(1)}` infinitely often

Task O2. Labels follow the house rules. ES is not solved here or anywhere;
nothing below bears on whether `W(p)<∞`. Notation as in `POINTWISE_OMEGA.md`
(cited as PO): `W`, `𝓡(M)`, `A_M=(M+1)/4`, Fact 1.1 (class of one),
Theorem 4.1 (transfer), H_MIN(θ), Theorem 6.2.

*Status: work in progress (checkpoint 1 being written).*

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
  `deg(v)=Σ_{w:{v,w} edge} p(w)`.

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
fixed total order on vertices); this is injective. Summing over `C_i⊆N(v_i)`
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
