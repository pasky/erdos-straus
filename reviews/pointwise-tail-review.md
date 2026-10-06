# Hostile review of POINTWISE_TAIL.md (task R76)

Reviewer branch `side-agent/review-tail`. Author doc merged ff from `side-agent/two-sided-tail`.
Status: IN PROGRESS.

## Verdicts per claim
(filled in below as checked)

### Claim 1 — Lemma 1.1 (quantitative coset transfer): **SOUND** (MINOR D1)

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

## Defects
