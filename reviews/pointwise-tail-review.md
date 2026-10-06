# Hostile review of POINTWISE_TAIL.md (task R76)

Reviewer branch `side-agent/review-tail`. Author doc merged ff from `side-agent/two-sided-tail`.
Status: IN PROGRESS.

## Verdicts per claim
(filled in below as checked)

### Claim 1 — Lemma 1.1 (quantitative coset transfer): **SOUND**

Re-derived from O9 Thm 1.1 (lines 111–196) + O11 Lemma 3.1 (lines 223–246) + O13 I3.
* The proof of O9 Thm 1.1 fixes `Q_G:=x^{1/(κL)}` *as a function of x*; every derived
  inequality (`Q_G≥Z`, `Q_G≥10^4C_G(A+1)(κL)²`, `Q_G^{6c}≤x`, `log x≥16`, `x≥Z^5`) follows
  from `log x≥C_2(1+log A)log Z` alone, so the bound holds for every such x (no
  "some x" quantifier hidden). The exceptional zero may differ between x's; harmless,
  the bound is pointwise in x.
* Case 0 / χ_1 outside support: `1−1/400−1/200` ✓. Case B: `|c(χ)|x^{β_1}/β_1 ≤ (μ/4)(2x)/φ(Q)` ✓
  (coset: `c(χ)=ψ_1(r)E_{rH}[Bψ_2]/φ(Q)`, `|ψ_1(r)|=1`) — total `≥ μx/φ(Q)·(1−1/2−1/100−1/400) ≥ μx/(3φ(Q))` ✓.
* Case A: `χ_D` trivial ⇒ χ induced from mod Q ⇒ `q_1|Q` ✓ (this is O11 l.239–241).
  `χ(r)=1` for real χ mod Q because r is a square at every odd prime and `r≡1 (8)` ✓.
  `λ≥min(u,1)/2`, `u=(1−β_1)log x≥16(1−β_1)` and Page `1−β_1≥c'q_1^{−1/2}(log q_1)^{−2}`
  (Davenport ch. 14, effective) ⇒ `0.98λ≥0.49·min(1,16c'Q^{−1/2}(log3Q)^{−2})≥λ_Q/3`
  with `c_P:=16c'`. ✓ `R_1≤2AZ³μ/φ(Q)≤λμx/(100φ(Q))` needs `x≥200AZ^{3.5}(log Z)²/(16c')`,
  implied by `x≥Z^5` for `Z≥Z_0` ✓.
* The improvement over O9 (`q_1|Q` instead of `q_1≤Z`) is correct and is exactly what
  Thm 3.3 later exploits (`q_1|Q_L`).

### Claim 2 — dropping `ℓ_aux` (Thm 2.1): **SOUND**

* `W(p)=min{M≡3 (4): p≡−4D (M), D|((M+1)/4)²}` (POINTWISE_SIZE §7 / O16 l.6) is a pure
  congruence condition; nothing requires `p>T` or `p>M`. `N(x,T)` counts all primes, so
  `p>T` is not needed. Property (I) (O13 §5, l.571–573) holds for every
  `p≡r (Q)`, `p∤QD`; atoms with `p|M` cannot fire since `gcd(M,4D)=1`.
* Twist condition: the ψ to be checked are those with `f|d_i`, `gcd(f,Q)=1`. Since
  `ℓ_aux>R≥max d_i`, `ℓ_aux∤f` for every relevant ψ: the family of twist conditions is
  identical with or without `ℓ_aux` (and I1(b)'s "`ℓ_0≠ℓ_aux`" is automatic).
* Case A/B split: with `ℓ_aux|Q'` a real character of conductor divisible by `ℓ_aux`
  would be trivial on `H'`→ Case A with `q_1≤Q'`, costing `ℓ_aux^{−1/2}`; without `ℓ_aux`,
  no character of the expansion (`N=lcm(Q,D)`, `ℓ_aux∤N`) involves `ℓ_aux` at all. So
  dropping it only removes Case-A candidates. ✓
* Cell consistency, `μ`, `A≤1.03`, `log Z` ledger: none mentions `ℓ_aux` (O13 l.595–597). ✓
* Count: `B≤1` (BRW form `1−Σ A_i(1−v_i)²`) and `B(p)>0⇒W(p)>T`, so
  `log x·#{…}≥Σ_{B(p)>0}B(p)log p≥S_r(x)` ✓. Losses: `log(1/λ_Q)≤½log Q+O(loglog Q)`,
  `log φ(Q)`, `(4/3)S_res` — all `≪𝓛³(log𝓛)^5` ✓. Threshold `log Z≤log Q+2τ+3𝓛`,
  `τ≍𝓛(S_res+𝓛)` ⇒ `≪𝓛^4log𝓛` ✓; range `𝓛≤c(log x/loglog x)^{1/4}` ⇒ threshold ✓.

### Claim 3 — Lemma 3.1 (leaf calculus): **SOUND**

* Re-derived: start mass `Haar{n≡1 (8)}=1/4`, process prob 1; an `(ℓ,0)` step has process
  prob `2/(ℓ−1)` vs conditional Haar `1/(ℓ−1)` (ratio 2); an `(ℓ,a≥1)` step has `1/ℓ` vs `1/ℓ`
  (every lift of a nonzero square mod odd ℓ is a square mod `ℓ^{a+1}`, Hensel); forced step at 3:
  `1 = 2/(3−1)` ✓. Product: `P_proc(L)=4·2^{k_L}/φ(Q_L)`, `k_L=ω(Q_L)−1` ✓. Disjointness:
  the rule depends only on `(Q,r)`, so it is a decision tree on digits ✓.
* **From-scratch brute force** `scripts/review_tail_leaves.py` (6 random deterministic
  state-dependent rules, forced 3,5,7, then steps at 11 (≤2 levels) and 13; 308–1190 leaves each,
  enumerated mod `N=840·11²·13`): (1) all lifts are squares; (2) `ΣP_proc=1` exactly; (3) the
  formula holds for every leaf (exact rationals); (4) leaf fibres are pairwise disjoint, lie in
  the square classes mod 840, and n is covered iff its own path never meets a non-square at an
  `a=0` step; Haar mass of the union `=Σ1/φ(Q_L)`. All OK.
* Note (not a defect): the leaves do *not* cover the hard set; the uncovered mass (non-squares at
  stepped primes) is exactly why the sum pays `2^{−k_L}` — consistent with Thm 3.3's display.

### Claim 4 — Lemma 3.2 (`E[k]≪𝓛³(log𝓛)²loglog𝓛`): **SOUND** (MINOR D1)

* *Optional stopping.* For a non-forced `(ℓ,0)` step the rule requires `w̃_{ℓ,0}(τ)>η`, and
  `w̃_{ℓ,0}=Σ_{ℓ|M}β^{s}p ≤ Σ_{ℓ|M}2^{u}β^{ω}p =: G^{(ℓ,0)}` (`s≤ω`, `u≥0`). `G^{(ℓ,0)}` is O13
  Lemma 3.2(a) with `φ(E)=1[ℓ|M]β^{ω(M)}`; times are bounded; `G≥0` ⇒
  `P(τ_{ℓ,0}<∞)≤η^{−1}G_0^{(ℓ,0)}`, `G_0=Σ_{ℓ|M}P_H2^{ω_Y}β^{ω}` (at the start `n≡1 (8)`, M odd ⇒
  `p_0=P_H`, `u_0=ω_Y`). Summing over `ℓ≤Y`, `ℓ∉{3,5,7}` and adding 3 forced steps gives the
  first inequality ✓.
* *Elementary step.* `y≤t^y/(e log t)` (max of `y t^{−y}` is `1/(e log t)`) and
  `1/log(1+1/a)≤a+1` ✓.
* *NT hypotheses* — checked against `sources/henriot-1102.1643.pdf` p.1–2 (Theorem 1 = NT, (1.1)):
  class `M_k(A,B,ε)`: `F(a_1b_1,…)≤min(A^{Ω(a_1⋯a_k)},B(a_1⋯a_k)^ε)F(b_1,…)` for coprime
  arguments, `ε≤αδ/(12g²)`; implied constant depends on `g,D,α,δ,A,B` only. Here `k=2`,
  `Q_1=X`, `Q_2=4X−1` (coprime, irreducible, `g=2`, fixed discriminant, no fixed prime divisor:
  `Q(1)=3`, `Q(2)=14`). `F=τ(n_1²)·f_2(n_2)t^{ω_Y(n_2)}`: per prime power `F` grows by
  `≤max(2k+1, 4βt)`, so `A=8`, and `8^{ω(a)}≤B_εa^ε` with ε the fixed NT value ✓. Uniform in T
  (`β,t≤2`) ✓. NT's RHS has `ρ_{Q_2}(2)=0`, so even `n_2` never contribute.
* *Euler product.* The `t`-twist multiplies the `p≤Y` local factors by `≤1+O(β(t−1)/p)`, total
  `exp(O(β(t−1)loglogY))=O(1)` ✓. **From-scratch numerics** `scripts/review_tail_twist.py`
  (T=10⁵,10⁶; Y=30…3·10⁴): ratio `Σw t^{ω_Y}/M ÷ Σw/M` = 3.0–4.0, flat in T, below the
  author's bound `e^{2β(t−1)loglogY}≈16` ✓.
* Final: `η^{−1}(loglogY+1)𝓛³logY ≍ 𝓛³(log𝓛)²loglog𝓛` with `logY=(C_0+4)log𝓛` ✓.

## Defects
