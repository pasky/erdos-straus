# Second hostile review of POINTWISE_OMEGA3.md (branch side-agent/omega-gpair @ bbe13d0)

Reviewer: independent (review-omega3b). Scope: (1) from-scratch re-derivation
of O2 Lemmas 10.1, 10.2, 2.1 and hypothesis checks at every OMEGA3 use site;
(2) adversarial brute-force small systems; (3) the chain H_MIN(θ) ∀θ ⇒ W ≥
(log p)^{1/θ−ε}. Items are written and committed one by one.

## Item 1 — O2 Lemma 10.1 (private covers), re-derived. Verdict: SOUND

* (1) For P ⊆ V(x), a minimal subfamily of occurring events covering P is a
  private cover (a member without a private prime in P could be dropped).
  Distinct P are distinct summands, so `binom(N,u) ≤ G^cov_u`. `|C|≤|P|`
  because private primes are distinct elements of P. The rest is Lemma 1.2
  (checked: Lemma 1.1 Möbius identity, `|R_L| ≤ binom(2N,L) ≤
  4^{L+1}binom(N,L+1)`, the ratio computation `den−num = L²+3L+4t+2`).
* (2) `κ(U,c)≠0` forces every prime of U to be covered by events supported
  in U and occurring on c (pairing `W ↔ W∪{ℓ}`); a minimal such family is a
  private cover of U supported in U, determined by the U-coordinates, so
  `Σ_c |κ|P(c) ≤ 2^{|U|} Σ_{C priv. cover of U} P(C occurs)`. Correct for
  mixed-size events and unions of cells.
* Nothing in the proof uses event sizes or a particular base measure beyond
  independence of coordinates and "event = union of cells on its support".

## Item 2 — O2 Lemma 10.2 (hypergraph moment bound), re-derived. Verdict: SOUND (two cosmetic gaps)

Re-derivation, step by step:

* *Reduction.* Swap sums: `Σ_{u≤U_0} w^u EG^cov_u = Σ_C P(C occurs)·Σ_{P:
  C priv. covers P, |P|≤U_0} w^{|P|}`; such P ⊆ π(C) and `|C|≤|P|≤U_0`, so
  the inner sum is `≤(1+w)^{|π(C)|}`. ✓.
* *Singles.* At most one single per prime in a private C (two singles at ℓ
  have no private prime); a single's prime is used by no other member, so
  singles factor off by independence: `≤∏(1+(1+w)g_ℓ)`. ✓
* *Components* (connectivity through shared vertices). Different vertices at
  one prime ⇒ P=0; otherwise components live on disjoint prime sets and P
  multiplies; each component inherits privacy; `|V(K)|=|π(K)|` when P(K)>0.
  `Σ ≤ ∏_K(1+(1+w)^{|V(K)|}P(K))`. ✓
* *Exploration.* The private vertex of a child e of v is neither v (v was
  brought by another hyperedge) nor old (it lies in no other hyperedge), so
  `O_e:=e∩pool ⊊ e`, `|O_e|≤k−1`, and summing over e by `O=e∩pool ∋ v`
  gives `≤Σ_j binom(|pool|−1,j)Δ^{(j+1)} ≤ D` since `|pool|≤kh≤kU_0`. ✓
  The ordered-tuple argument for unordered sibling sets is correct (the
  product of sibling weights equals ∏p over all vertices they bring, order-
  independent; the private vertex is new under every order).
* *Counting.* `Σ_{c_1+…+c_N=h−1}∏1/c_i! = N^{h−1}/(h−1)!` and with
  `N=kh`: `k^{h−1}h^h/h! ≤ e(ke)^{h−1}`. Geometric sum under
  `(1+w)^k keD≤1/2`. ✓ Constants exactly as stated.

Cosmetic gaps (no effect on the statement):
* **2a.** "n processed vertices" with n=|V(K)| depending on K: make it
  rigorous by encoding into a fixed number `N=kh` of BFS slots, padding
  with c_i=0; the map K ↦ (e_1, child sets) is injective. Same bound.
* **2b.** Simplicity of the hypergraph is not needed (multi-edges only
  enlarge Δ_O and S_H consistently).

**Hypotheses actually used** (to be checked at every use site): (i) the
coordinates X_ℓ are *independent* under the measure in which P, p(v),
Δ_O, S_H are computed; (ii) vertices at one prime are pairwise disjoint;
(iii) every event is a single or a hyperedge = conjunction of vertex events
at distinct primes, of size ≤k; (iv) the codegree maxima Δ^{(j+1)} are over
the *whole* system used (not just over occurring/realised parts), at pool
size `kU_0`; (v) `D` includes the j=0 term `Δ^{(1)}=max deg`.

## Item 3 — O2 Lemma 2.1 (pseudoforest bound), re-derived. Verdict: SOUND

* `1+z(s+d)≤(1+zs)(1+zd)`; expansion over (U,f); on {F occurs} primes of U
  ↔ vertices of F injectively, so each component has `|E|≤|V|`. ✓
* `Σ_{f(U)=F} z^{|U|} ≤ ∏_{v∈V(F)}(1+z deg_F v) ≤ e^{2z|E(F)|}`. ✓
  Singles give `(1+z)^{|π(F)|}e^{zS_1}`, total weight `e^{3z|V(F)|}`. ✓
* Components on disjoint prime sets multiply; `≤exp(Σ_K w_K)`. ✓
* Trees: BFS child-set encoding over all roots, `Σ_{|C|=c,C⊆N(v)}∏p ≤
  deg^c/c!`, root factor `deg(v_0)δ^{c_1−1}`, compositions `v^v/v! ≤ e^v`,
  `Σ_{v_0}p(v_0)deg(v_0)=2S_2`. Unicyclic: ≤ v²/2 extra pairs, P(K)≤P(T). ✓
* Final constant: `Σ_j(3+2j+j²/2)e^{−j} = 4.746+1.841+0.997 = 7.584`,
  ×2 = 15.17 ≤ 16. ✓
* Same hypotheses (i),(ii) of Item 2 (independence; disjoint vertices per
  prime) plus the vertex-degree bound `δ≤e^{−3z−2}`.

## Item 4 — O3 §3 (Lemma 3.1, Thm 3.2, Lemma 3.3, Thm 3.4) use sites. Verdict: SOUND (one notational slip)

* **Lemma 3.1.** (1) Neighbour sums `≤3·2/32=3/16` for supports ≤3, so
  `P(E)≤x_E/2≤x_E∏(1−x)`; the chain over level-3 events conditioned on
  `𝒜_2` is the standard AS 5.1.1 argument; `−log(1−x)≤1.07x` for
  `x≤1/16`, so the `e^{−3S}` bounds hold with room. (2) The conditional
  bound is elementary here: `P(B∩𝒜_2) ≤ P(B)P(∩_{A∉Γ(B)}Ā)` and
  `P(𝒜_2) ≥ P(∩_{A∉Γ(B)}Ā)∏_{Γ(B)}(1−x_A)` (the second by the same LLL
  chain). `Σ_{Γ(B)}x_A ≤ |U|/16`, so `e^{1.2|U|/16}≤e^{|U|/2}`. ✓
* **Tilted weight `1+w'=17e^{1/2}` (Thm 3.2 Step 1).** The tilt is applied
  to the *pointwise* reduction inequality of Lemma 10.2 *before* any
  factorisation: `E[F_2 1[C]] ≤ P(𝒜_2)P_Haar(C)e^{|π(C)|/2}`, and
  `e^{|π(C)|/2}` is multiplicative over components. After that, everything
  (components, exploration, counting) is under Haar, so hypothesis (i) of
  Item 2 (independence) holds where it is used. Level 3 has no singles,
  so `Λ_3=2e·3(1+w')³Ŝ` exactly. Hypothesis: `D=Δ^{(1)}+3(L_3+1)Δ^{(2)} ≤
  δ_3+δ_3=2δ_3=[2e·3(1+w')³]^{−1}` ✓ (k=3, U_0=L_3+1; pool size
  `3U_0` matches `3(L_3+1)` in t). The untilted Haar mass bound follows
  from the same hypothesis since `1+w<1+w'`. ✓
* **Arithmetic re-checked:** `2·4^{−(L_3+1)}e^{Λ_3} ≤ e^{−3Ŝ}/200`;
  Step 2 error `2e^{Λ_3}·2·4^{−(L_2+1)}e^{Λ_2} ≤ e^{−3Σ}/200`;
  `P(𝒜_2∩𝒜_3)≥e^{−3Σ}`; total `≤P/100`. Mass `≤4e^{Λ_2+Λ_3}`. Supports
  `≤3(L_3+1)+2(L_2+1)` (G-terms of a graph system carry ≤2 primes per
  factor). ✓
* **Cell-conditioned level 2 (Step 2).** On a cell, edges with one end in
  P_i become induced singles (or die), so `F_2=F_2^{(i)}` is a function
  of the complementary coordinates, Haar-independent of the cell;
  induced mass `≤Σ_{v realised}deg(v) ≤ δ|P_i|`; degrees unchanged ≤δ;
  `z=16`, `δ=e^{−50}=e^{−3z−2}` exactly as Lemma 2.1 requires. ✓
* **Twist.** `E[1_{𝒜'}ψ]=0` (𝒜' independent of `X_{ℓ_0}`); conditional
  LLL on ≤2 remaining primes gives factor `(15/16)^{−2}=1.14≤1.3`;
  `0.01+0.05/0.95=0.063<0.99/4`. ✓
* **Lemma 3.3 Markov bookkeeping** re-derived: (a) `≤w^{(3)}_ℓ/δ_3`;
  (b) `Σ_{O∋v@ℓ}P(O)Δ_O = 2w^{(3)}_ℓ` (two pairs through the ℓ-vertex of
  a 3-edge), globally `3S_H/t`; (c) `≤w^{(2),new}_ℓ/δ`. Per-prime total
  `≤c_0(2+1/δ_3+(1+2/t)(1+1/δ)) ≤ 9c_0/(tδδ_3) ≤ 1/32`. Threshold t is
  fixed from the *a-priori* Ŝ before (b), so there is no circularity.
  Order (a)→(b)→(c) only deletes, so all degree/codegree bounds persist. ✓
* **Thm 3.4.** `Σ=O(Ŝ/t)=O(Ŝ²+1)` since `1/t=3(L_3+1)/δ_3=O(Ŝ+1)`. ✓
  Note the per-prime requirement `c_0(Ŝ)≍1/(Ŝ+1)`, i.e. **every free
  prime must carry mass ≲1/Ŝ** — checked at the application sites below.

Defect **D1 (notational, harmless):** Setting 3.0 defines
`t:=δ_3/(C_3(S_H+1))`, while "Constants" defines `t(Ŝ):=δ_3/(3(L_3+1))`
with `L_3=L_3(Ŝ)`. Only the latter is used in the proofs; delete the
former or state they agree up to the choice of `C_3`.
