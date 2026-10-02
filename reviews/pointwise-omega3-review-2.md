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

## Item 5 — Adversarial brute force (independent code). Verdict: no violation found

`scripts/omega3_review2_adversarial.py SEED TRIALS` (written from scratch,
shares no code with the omega2/omega3 scripts). Abstract product spaces
with arbitrary non-uniform coordinate laws, mixed-size events (1..4
vertices), random and "cluster" systems (one heavy vertex `p∈[.3,.97]` per
prime, all events sharing it — the hub/sunflower regime), exact
expectations by full enumeration. Tests:

* **T1** Lemma 1.1/1.2/10.1(1) pointwise for every outcome and every L
  (`binom(N,u)≤G^cov_u`, `B_L−4^{L+1}G^cov_{L+1}≤1[A=∅]`, two-sided
  bound) and Lemma 10.1(2) `M_1(B_L)≤Σ_{u≤L}2^uEG^cov_u` via explicit
  Möbius cell coefficients κ(U,c).
* **T2** Lemma 10.2's per-h component inequality
  `Σ_{|K|=h}(1+w)^{|V(K)|}P(K) ≤ (1+w)^{kh}ekS_H(keD_h)^{h−1}` *without*
  the smallness hypothesis (this is the real combinatorial content), for
  `w∈{0,1,16,17e^{1/2}−1}`; **T2b** the full Lemma 10.2 statement on
  systems scaled into its hypothesis.
* **T3** Lemma 2.1's tree count `≤2S_2e^vδ^{v−2}` and the pseudoforest
  count `≤(1+v²/2)·2S_2e^vδ^{v−2}`, hypothesis-free.
* **T4** conditional LLL (O3 Lemma 3.1(2) in its `∏(1−x_A)^{−1}` form),
  exact, whenever the asymmetric LLL condition holds.
* **T5** cell conditioning of O3 Thm 5.1: `F_r=F_r^{(i)}` on the cell
  (pointwise), `S_induced ≤ Σ_i binom(h,i)Δ^{(i)}` and
  `Δ'_O ≤ Σ_i binom(h,i)Δ^{(|O|+i)}` for every vertex set O.

Results: seeds 1 (300 trials), 2 and 3 (1000 trials each): **0
violations**; ~4 400 in-hypothesis instances of T2b, ~10⁵ T1 outcomes per
1000 trials. Max observed lhs/rhs: T2 per-h 7.5·10⁻³ (h=2), ≤1.1·10⁻⁵
(h≥3); T3 trees 0.068 (=1/(2e²) at v=2, exact); T1/T4/T5 reach 1 (tight
cases exist, e.g. h=0 or single fixed vertex). **Negative control**
`NEG=1` (drop the higher-codegree terms `i≥1` in the Δ'_O bound, i.e.
use only the unconditioned codegree) gives 123 violations at seed 1,
confirming the test bites and confirming O3's remark that fixing several
vertices of one event needs the higher codegrees.

Limitation: Lemma 10.2/2.1 are proven with huge slack, so brute force
can only refute structural (not constant-level) errors; the constants
were checked by hand in Items 2–3.

## Item 6 — O3 Thm 5.1 (k-level induction). Verdict: SOUND (two cosmetic slips)

Every Lemma 10.2 use site re-checked:

* **Level k (no conditioning).** (a)/(b) give `deg≤δ_k/2`,
  `Δ_O≤δ_k(4N_k)^{−j}/(2k)` (|O|=j+1); pool `k(L_k+1)≤N_k`, so
  `D≤δ_k+Σ_{j≥1}4^{−j}δ_k/(2k)≤2δ_k=[2ek(1+w')^k]^{−1}` ✓.
* **Level r, cell-conditioned.** `|P_i|≤Σ_{s>r}s(L_s+1)≤H_r`
  (B_L cells ≤L_s primes; G^cov cells ≤s(L_s+1)). Conditioned codegree
  `Δ'_O ≤ Σ_{F'⊆fixed}Δ_{O∪F'}`; with `H_r≤N_r`:
  `Δ'_v≤δ_r/2+δ_r/(6r)≤δ_r`, `Δ'_O≤(4/3)δ_r(4N_r)^{−(|O|−1)}/(2r)` ✓.
  Pool `r(L_r+1)≤N_r` (conditioned supports ≤r), so
  `D≤δ_r(1+1/(3r))≤2δ_r` ✓. Induced singles/edges are allowed by Lemma
  10.2 (singles via `(1+w')S_1≤2er(1+w')^rS_1`); duplicates harmless
  (Item 2b). Induced mass `≤hδ_r/2+hδ_r/(6r)≤hδ_r≤H_r`, hence
  `Λ_r=2er(1+w')^r(Σ_r+H_r+1)` dominates both the tilted and untilted
  sums ✓. Brute-force T5 (Item 5) confirms the conditioning inequalities
  and that the higher codegrees are genuinely needed.
* **Tilt.** Lemma 3.1(2) for `𝒜_{<r}` (per-prime ≤1/(64k), neighbour sum
  `|U|/(32k)`) applied to `C_i∩{C occurs}` on `P_i∪π(C)` gives
  `e^{|P_i|/2}·e^{|π(C)|/2}`; the first is in `L_r` via `H_r/2`, the
  second is absorbed in `w'` before factorisation, under Haar ✓.
* **Error budget.** Per level `≤P(𝒜_{<r})e^{−3Ŝ_{≥r}}/(100k)≤P(all)/(100k)`
  (using frozen masses as upper bounds — correct, since after level s is
  processed only deletions at levels ≥s occur) ✓. Telescoping
  `E[F_{<r+1}B_{≥r+1}]−E[F_{<r}B_{≥r}]≤ε_r` re-derived ✓.
  `M_1(B_{≥r})≤4e^{Λ_r}M_1(B_{≥r+1})` ✓.
* **Frozen masses / no circularity.** Thresholds at level r use only
  `Σ_s (s≥r)`, `L_s (s>r)`; pushes go strictly down; per-prime and total
  masses are amplified by `poly_k(N_r)` finitely often, so
  `Σ_{r−1},L_r,N_r ≤ C_kŜ^{A_k}` and `(P_k)` follows from
  `c_k(Ŝ)=Ŝ^{−A_k}/C_k` ✓. All constants depend on k only (A_k possibly
  factorial — acknowledged in the Remarks).
* **Push-downs (Markov).** `Σ_{O∋v@ℓ,|O|=j+1}P(O)Δ_O=binom(r−1,j)w^{(r)}_ℓ≤2^rw^{(r)}_ℓ` ✓.
  Pushed sets merge with existing events of the same vertex set ✓;
  every deleted event contains a pushed event, so `F≤1[no original event]` ✓.

Cosmetic defects:
* **D2.** The level-2 error is "chosen as in Thm 3.2 Step 2", which gives
  `P/200`; with `Σ_{r=3}^k 1/(100k)` the total is `≤(3k−4)/(200k)·P <
  0.015P`, not `P/100`. Harmless (μ≥0.985P; twist margin
  `0.015+0.053<0.985/4`), or choose L_2 with `200k𝔐_3` in place of
  `800e^{Λ_3}`.
* **D3.** Thm 5.2 proof: `y=T^{1/k}e^{2𝓛/log𝓛}` gives `y^k>T`, so
  `Ω(r)≤k−1` (text says `≤k`). Harmless (understatement); for k=3 the
  supports are ≤2 and the exponent-3 case is O2's.

## Item 7 — Logic chain H_MIN(θ) ∀θ ⇒ W ≥ (log p)^{1/θ−ε}; hidden T^c terms. Verdict: SOUND

* **PO Thm 4.1 re-derived** (given TZ Cor 1.4 + McCurley region): CRT
  classes `a_i≡1 (Q)`, `≡b_i (d_i)`; Case A (`q*|Q`): `λ_i=λ_*` common,
  relative error `C_0E_1M_1`; Case B: `χ_1(a_i)=χ*'(b_i)=ψ(b_i)` exactly
  for `i` with `q*'|d_i` (needs `q*_Q|Q`), else `|λ_i−1|≤2E_2`; `λ<2`.
  `μ_ψ=E_Haar[Bψ]` (characters at primes outside `d_i` average to 0), so
  the twist condition of O3 Thm 3.2/5.1 is the one Thm 4.1 needs. The
  requirement `E_1,E_2≤μ/(8(C_0+1)M_1)` is met for
  `log x≥C_1K·max(log Z,K)` (E_2 needs `log x≳K log Z`; E_1's second term
  needs `log x≳K²`; `x≥Z^{12}`). ✓
* **PO Thm 6.2 / O3 Thm 4.3, 5.2.** `ℓ_0∈(R,2R]`, `R=max(T,max d_i)`
  forces `p>T` (so distinct T give distinct p even if some W(p)=∞) and
  keeps `d_i` coprime to `Qℓ_0`. ✓
* **Every term of `log p ≤ C_1K·max(log Z,K)`**, for fixed k (y=T^{1/k}e^{2𝓛/log𝓛}):
  - `log Q ≤ Σ_{ℓ∈Π_0}e_ℓlog ℓ + |𝓑|𝓛 + log24 ≤ π(y)𝓛+|𝓑|𝓛 ≈ k·y + T^{o(1)}`
    — prime powers `ℓ^{e_ℓ}≤T` cost only the factor `𝓛/log y≈k`;
    bad primes may be as large as T but each costs ≤𝓛 and
    `|𝓑|≤(k−1)S*/c_k=O_k(Ŝ^{A_k+1})=T^{o(1)}` (Lemma 11.2 re-derived:
    each atom is charged once per prime >y dividing M, ≤k−1 of them, and
    each charge is ≤ its S* term because S* takes the max over Π);
  - `log max d_i ≤ (#primes per cell)·𝓛 = O_k(Ŝ^{A_k})𝓛 = T^{o(1)}`;
    `log ℓ_0 ≤ log 2R` same order;
  - `K=1+log(M_1/μ)=O_k(Ŝ^{A_k})`, `log(1/μ)≤3Ŝ_tot+1`, all `T^{o(1)}`
    because `S*≤exp(O(𝓛/log𝓛))` uniformly in Π (O2 Lemma 11.1: the max
    over Π is inside the sum, so it covers the iterated quarantine).
  No term grows like `T^c` with c independent of θ: the only `T^{Θ(1)}`
  quantity is `π(y)𝓛 ≍ y/θ`. Hence `log p ≤ T^{1/k}exp(O_k(𝓛/log𝓛))`
  and `W(p)>T ≥ (log p)^k·exp(−C_k log log p/log log log p)`. ✓
* **(I) transfer.** O2 Lemma 4.3 (I) uses only `ℓ^{v}‖M ⇒ ℓ^v≤T≤ℓ^{e_ℓ}`
  for `ℓ∈Π`, independent of y and of k; `B≤F≤1[no original event]` since
  every pushed/deleted event is implied by a level event; B is a pointwise
  minorant at *every* outcome (Lemmas 1.1/1.2 hold for arbitrary values of
  the coordinates, including non-units), so `B(n)≤1[W(n)>T]` for all
  `n≡1 (Q)`, as Thm 4.1 requires. ✓
* **Per-prime hypothesis.** Thm 3.4/5.1 need per-prime mass `≲Ŝ^{−A_k}`,
  far below the O2 constant level; Lemma 11.2 delivers any threshold
  `c_0` at quarantine cost `kS*/c_0` primes, which is `T^{o(1)}` for
  `c_0=Ŝ^{−A_k}/C_k`. ✓ (This is the step where a hidden power of T could
  have entered; it does not, because `S*=T^{o(1)}`.)

## Item 8 — O3 §1 (Thm 1.1, Cor 1.2, Lemma 1.3), spot check. Verdict: SOUND

Bonferroni parities (J odd ⇒ β lower, α upper), `0≤V_i−Eβ_i≤e_{J+1}`,
`P(cell_i)V_i=V·P'(cell_i)`, twist identity
`E[1_{𝒜_1}1_{cell}ψ]=V·E'[1_{cell}ψ]`, and the `0.011` correction in
Lemma 1.3 all check. §§3–5 do not depend on §1 (as the text says).

## Summary

| Item | Subject | Verdict |
|---|---|---|
| 1 | O2 Lemma 10.1 (private covers) | SOUND |
| 2 | O2 Lemma 10.2 (hypergraph moment) | SOUND (cosmetic 2a, 2b) |
| 3 | O2 Lemma 2.1 (pseudoforest) | SOUND |
| 4 | O3 §3: Lemma 3.1, Thm 3.2 (tilt 1+w'), Lemma 3.3, Thm 3.4 | SOUND (D1 notational) |
| 5 | Independent adversarial brute force + negative control | 0 violations |
| 6 | O3 Thm 5.1 k-level induction (conditioned codegrees, induced mass, frozen budgets, k-dependence) | SOUND (D2, D3 cosmetic) |
| 7 | Chain to `W≥(log p)^{1/θ−ε}`; no hidden `T^c` | SOUND |
| 8 | O3 §1 | SOUND |

Numbered defects (none affects any theorem statement):

* **D1** Setting 3.0's `t:=δ_3/(C_3(S_H+1))` vs Constants' `t(Ŝ)=δ_3/(3(L_3+1))`; keep one.
* **D2** k-level error total is `<0.015P(all)`, not `≤P/100`, unless L_2 is
  chosen with `200k𝔐_3`; margins unaffected.
* **D3** Thm 5.2: rough parts have `Ω≤k−1`, not `≤k` (understatement).
* (2a/2b, in O2 Lemma 10.2's proof) fixed-slot encoding and
  non-use of simplicity — wording only.

**Overall: SOUND.** The two lemmas the first review did not re-derive
(O2 10.2, 2.1) hold as stated, including the private-vertex/new-vertex
step and the order-independent sibling sum; every OMEGA3 use (tilted
weight, mixed-size induced events, conditioned systems with higher
codegrees, frozen budgets, k-dependent constants) satisfies the
hypotheses actually used in the proofs. Status of Thms 4.3/5.2 remains
"PROVED modulo Thorner–Zaman Cor 1.4 + McCurley region (or Landau–Page)".

Replay:
```
(ulimit -v 8000000; for s in 1 2 3; do timeout 900 env PYTHONPATH=scripts uv run python scripts/omega3_review2_adversarial.py $s 1000; done)
(ulimit -v 8000000; NEG=1 timeout 900 env PYTHONPATH=scripts uv run python scripts/omega3_review2_adversarial.py 1 300)  # negative control: exits 1
```
