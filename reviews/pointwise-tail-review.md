# Hostile review of POINTWISE_TAIL.md (task R76)

Reviewer branch `side-agent/review-tail`. Author doc merged ff from `side-agent/two-sided-tail`.
Status: ROUND 1 COMPLETE. Overall: no FATAL, no MAJOR; 6 MINOR; one improvement (S1).

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

### Claim 5 — Thm 3.3 (sum over leaves): **SOUND** (MINOR D3, D4, D6; improvement S1)

* Good leaves: `P(¬(i))≤1/4` (O13 Lemma 3.2(d)+3.3(B), Y as in O13 Thm 3.4), Markov `≤1/8` for
  each of (ii)–(iv) ⇒ `P_proc(good)≥1−1/4−3/8=3/8` ✓. On a good leaf every ingredient of O13 §5
  holds with realised values `≤8×` expectations; `τ` is built from the leaf's own `S_res(L)`, so
  `log Z_L≤C_3𝓛^4log𝓛` uniformly ⇒ one x works for all good leaves ✓.
* The exceptional zero in (G) depends only on x (family `q≤Q_G(x)`), so it is the same for all
  leaves; leaf L is in Case A iff `q_1|Q_L` ✓. Real primitive `q_1=2^e·(odd squarefree)`,
  `e≤3`, odd primes of `Q_L` are `≤Y` (only `ℓ≤Y` eligible, forced 3,5,7) ⇒ `q_1≤8Y^{k_L}` ✓.
* Display: `#_L≥S_L/log x≥λ_Lμ_Lx/(3φ(Q_L)log x)`, `1/φ(Q_L)=P_proc(L)2^{−k_L}/4` (Lemma 3.1),
  disjoint fibres ⇒ counts add ✓; `≥(3/8)·min` ✓.
* Losses: `k_Llog2≪𝓛³(log𝓛)²loglog𝓛`; `log(1/μ_L)≪𝓛³log𝓛`; Siegel `½k_LlogY≪𝓛³(log𝓛)³loglog𝓛` ✓.
  Without Case A the bound is `𝓛³(log𝓛)²loglog𝓛` ✓ (CONDITIONAL, correctly labelled).

### Claim 6 — Cor 2.2 (two-sided tail): **SOUND** (MINOR D2)

* Lower inequality: CU Thm 2.1 (l.73–131): `N≪π(x)e^{−c𝓛³}` for `3≤T≤exp(c₁(log x)^{1/4})`, constants
  ineffective; contains `𝓛≤c(log x/loglog x)^{1/4}` if `c≤c₁`; the `≪`-constant is absorbed for
  `T≥T_0` ✓. Upper inequality: Thm 3.3; `𝓛≤c(log x/loglog x)^{1/4}` ⇒ `C𝓛^4log𝓛≤(Cc^4/4)log x≤log x` ✓.
* Exponents: `𝓛³(log𝓛)³loglog𝓛 = (log T)³(loglog T)³logloglog T` ✓; `loglog(π/N)=(3+o(1))loglogT` ✓.

## Defects
(No FATAL, no MAJOR found.)

**D1 (MINOR; §3 Lemma 3.2 proof, "f_2(p^k)≤2tβ·(3/2)≤7").** At `p=2`, `p/(p−1)=2`, so
`f_2(2^k)=4βt` (not `≤3βt`); still `≤7` for large T, and irrelevant anyway because NT's
right side carries `ρ_{Q_2}(2)=0`. Likewise the Euler-ratio `∏(1+2β(t−1)/(p−1))` ignores
`p^k`, k≥2, terms (`f_2(p^k)=f_2(p)`); the ratio is still `exp(O(β(t−1)loglogY))=O(1)`.
*Repair:* write `f_2(p^k)≤4βt≤7` and "local factor ratio `≤1+O((t−1)/p)`".

**D2 (MINOR; Cor 2.2).** The letter `c` is used both for the (ineffective) lower-tail constant
and for the range constant `log T≤c(log x/loglog x)^{1/4}`; the range constant must be
`≤min(c₁ of CU Thm 2.1, (4/C)^{1/4})`. *Repair:* call it `c'`, state the two constraints.

**D3 (MINOR; Lemma 1.1 statement vs Thm 3.3 use).** Thm 3.3's refined Siegel factor uses
`λ≥min(1,c_Pq_1^{−1/2}(log3q_1)^{−2})` with the *actual* exceptional conductor `q_1|Q_L`, which is
"Lemma 1.1's proof", not its statement (`λ_Q` in terms of Q). *Repair:* state Lemma 1.1 with
`λ:=1` if Case A does not occur and `λ:=min(1,c_Pq_1^{−1/2}(log3q_1)^{−2})` otherwise, `q_1|Q`;
then `λ≥λ_Q` is a corollary.

**D4 (MINOR; Thm 3.3 conditional clause).** "No character of conductor `≤x` has a Landau–Siegel
zero in the sense of (G)" depends on `κ, Q_G(x)`; the clean sufficient hypothesis is the
usual zero-free statement `1−β≥c/log q` for real primitive χ of conductor `q|Q_L` (then
`u=(1−β_1)log x≥c log x/log q_1≥1` and `λ≥1/2`). *Repair:* state that (weaker, standard;
implied by GRH for real characters).

**D5 (MINOR; Replay).** "No computations" — fine, but Lemma 3.1 and the Euler-ratio claim of
Lemma 3.2 now have from-scratch checks (`scripts/review_tail_leaves.py`,
`scripts/review_tail_twist.py`); cite them if desired.

**D6 (MINOR; Cor 2.2 last sentence "the lower-tail constant C is [effective]").** True only if
the implied constants of NT, (G) (MV Thm 28.19 constants `c, κ_0, C_G`), Lemma 3.3(B)'s `C_0`
and OMEGA10 Thm 3.4 are effective. Plausible, but say "effective, given that the implied
constants of the cited inputs are" (as CU does for the opposite side).

## Suggested improvement (not a defect)

**S1 — removes the `logloglog T` from Cor 2.2.** Bound the Siegel loss by `log rad(Q_L)`
instead of `k_L logY`. With `s=1/logY`, `Σ_{ℓ|M,ℓ≤Y}logℓ ≤ (logY/e)·rad(M_Y)^s`
(`y≤e^{sy}/(es)`), the twist `ℓ^s∈[1,e]` keeps F in `M_2(A,B,ε)` (A=12), and the Euler ratio
is `exp(2β Σ_{ℓ≤Y}(ℓ^s−1)/ℓ+O(1)) ≤ exp(2β(e−1)+O(1))=O(1)` (`ℓ^s−1≤(e−1)s logℓ`). The
optional-stopping argument of Lemma 3.2 with weight `logℓ` at `a=0` only gives
`E[log rad_odd Q_end] ≤ log105 + η^{−1}ΣP_H2^{ω_Y}β^{ω}log rad(M_Y) ≪ η^{−1}𝓛³(logY)² ≍ 𝓛³(log𝓛)³`.
Add a good-leaf condition (v) `log rad Q_L≤8E[…]` (`P(good)≥1/4`). Then `q_1≤rad(Q_L)·4`
(q_1's 2-part `≤8`, rad has one factor 2) and the Siegel loss is `≪𝓛³(log𝓛)³`, so Thm 3.3 /
Cor 2.2 become `C(log T)³(loglog T)³`. Numerics (`review_tail_twist.py`, T=10⁶) agree:
the w-weighted mean of `log rad M_Y` tracks `logY` (10.0 vs 10.3 at Y=3·10⁴), whereas
`ω_Y·logY` is ≈3× larger and grows like `loglogY·logY`.

## Verdict summary

| Claim | Verdict |
|---|---|
| Lemma 1.1 (quantitative coset transfer, `λ_Q` via Page) | SOUND (D3) |
| Dropping `ℓ_aux` / Thm 2.1 (one fibre, `(log𝓛)^5`) | SOUND |
| Lemma 3.1 (leaf calculus) | SOUND (brute-forced) |
| Lemma 3.2 (`E[k]`, NT with `t^{ω_Y}` twist) | SOUND (D1) |
| Thm 3.3 (`(log𝓛)³loglog𝓛`; `(log𝓛)²loglog𝓛` CONDITIONAL) | SOUND (D4, D6); S1 improves |
| Cor 2.2 (two-sided tail, exponent 3) | SOUND (D2, D6) |

Labels: all PROVED-modulo labels are appropriate (inputs (G), NT, OMEGA10 Thm 3.4; Page is
classical). ES itself is untouched, as the document says.
