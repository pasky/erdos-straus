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
