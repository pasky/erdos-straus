# Hostile review B of EXCEPTIONAL_TYPEI_LOGLOG3.md (task R121B)

Reviewer: side agent `side-agent/review-ttl3-b` (independent of reviewer A). Reviewed: `EXCEPTIONAL_TYPEI_LOGLOG3.md`
and `scripts/ttl3_*.md` as of merge of `side-agent/eff-di7` @ f0c5fe9. From-scratch scripts: `scripts/review_ttl3b_*.py`.

**Status: IN PROGRESS** (written claim by claim).

## Verdict per section

| Section / claim | Verdict |
|---|---|
| §1 Lemmas 1.1–1.3 (toolkit) | SOUND |
| §2 (M), (PS), Prop 2.1, Thm 2.2, Cor 2.3 | SOUND (relative to (P1)–(P3)) |

### §1 — SOUND
Re-derived line by line. Lemma 1.1: `f(n)/n^δ ≤ Π((a+1)p^{−aδ/B})^B`, factor ≤ 1 if `p ≥ 2^{B/δ}`, else
≤ `max_a (a+1)e^{−ca} = e^{c−1}/c ≤ 1/c ≤ 2B/δ` (`1/log 2 < 2`); count of small primes ≤ `2^{B/δ}`. ✓.
Exact `sup_n τ(n)^B/n^δ` computed for 5 (B,δ) pairs, always far below the bound (`review_ttl3b_toolkit.py`).
Lemma 1.3: Cauchy circle `|z−x| = x/2` gives `Re(1/z) ≥ 2/(9x)` ✓; max of `u^pe^{−2u/9}` ✓; Leibniz with
`Σ_k C(p,k)k!²(p−k)!² = p!Σk!(p−k)! ≤ (p+1)(p!)²` ✓; convolution identity for η^{(p)} ✓; final constant
`2^{p+1}·4·18^{p−1} ≤ 8·36^p` ✓. Numerically: `max|h^{(p)}|/(9^p(p!)²) ≤ 1` for p ≤ 24 (exact polynomial recursion
`Q_{p+1} = u²(Q_p − Q_p')`), `I = 4.85·10^{−5} ≥ e^{−16}/4` ✓.

### §2 — SOUND relative to (P1)–(P3)
(M) needs only `0 < 2σ_j ≤ 1/2` ✓. (PS) Abel summation + Cauchy–Schwarz in `dξ/ξ` ✓ (constant `2(1+t²(log 2)²)`).
Prop 2.1 (A),(B),(C) re-derived: `Q₁ = πQ^{1−2δ} ∈ [N, Q/2]`, `Y/Y₁ = (Q^{2δ}/π)^{2−2δ} ≥ 1`, exponent
`2δ(1−δ)+(1−2δ)(1+4δ) = 1+4δ−10δ²` (sympy) ✓, `2√2π·π^{1.4} = 44.13 < 45` ✓, `∫(1+t²)/(1+t⁴) = √2π` ✓, error term
`c·Q^{2δ−2δ²}·3Q·N` ✓. Thm 2.2 both branches ✓. Cor 2.3 ✓ (`δ^{−2} ≤ e^{2/δ}/4` for δ ≤ 1/10).
Note: the whole induction is only as good as the *shape* of (P2) (same N, same interval I, `t`-integral with weight
`(1+t⁴)^{−1}` and the switched parameter `πNY/Q`); this is checked against DI Lemma 8.1 below (§4).

## Defects
(numbered as found)

### §8 (nebentypus induction, Prop 8.1, Thm 8.2) — SOUND relative to (P1χ)–(P3χ)
Re-derived independently. Switching geometry: for the first trace at levels rq the arithmetic side is
`Σ_{q,c} g(q)Sχ(m,n;rqc)φ(4π√mn/(rqc))/(rqc)`; for fixed c this *is* the Kuznetsov sum of `(Γ₀(rc),χ)` at moduli
`(rc)q` (same χ mod r induced), so the destination levels are `rc`, `c ∈ (C,16C)`, `C = πNY/(rQ)`, with the **same**
Y (x-support of φ is `≍ 1/Y` on both sides). The `1/r` in C is real and C can be `< N` or `< 1/16`. ✓
* (C1) `C ≥ N`: `C = πQ^{1−2δ}/r ≤ Q/2`, `Y_C = C^{2−2δ}/N ∈ [1, Y]`, `(Y/Y_C)^{1/2} = (Q/C)^{1−δ}`, giving
  `2√2π c H Q^{1−δ}C^{5δ}N`, and `C^{5δ} ≤ π^{5δ}Q^{5δ−10δ²}` uses r ≥ 1 only. ✓ (constant `2√2π·π^{1/2} ≈ 15.7 < 45`).
* (C2) `C < N`: (P1χ) at C with `Y₁ = C+N`: `(C+N+Y₁) ≤ 4N`, `(NY₁)^δ ≤ (2N²)^δ`, `√(YN) = Q^{1−δ}`, `N ≤ Q^{1−2δ}`. ✓
  (Actually gives `10K₁Q^{1+δ}N`.) If `C < 1/16` the destination sum is empty (main term 0). ✓
* Error term `c(QYN)^δ·3Q·N = 3cQ^{1+3δ}N` ✓; closing `H/2 + 90cK₁ + 3c ≤ H` with `H ≥ 200cK₁` ✓.
* Thm 8.2, `Q ∈ [1/16,1)`: (P1χ) at Q with `Y₁ = 1+N`, `Q+N+Y₁ ≤ 4N` ✓.
So the "extra branch" is genuinely needed (Drappeau's "r appears only with negative powers" is not enough on its own:
nothing is inducted when the switched level drops below N) and the author's repair works. The new branch costs only
the absolute factor `200cK₁` in H; class 𝓔 preserved.

### Thm 9.1 conversion and Thm 9.2 deduction — SOUND (relative to Thm 8.2 and TTL2 Thm 4.1)
Checked against TTL2 §1 (DI7_ε): levels `M = rq ≤ M₀` covered by `≤ 2 + log M₀` blocks with `Q_i ≥ 1/16`; prefix
`[1,t]` = closed blocks `[2^k, min(2^{k+1}−1,t)]`, `K ≤ log₂t + 1 ≤ 1.5 log 2t` blocks (Cauchy–Schwarz cost K, which
TTL2 even allows as `(log 2t)²`); `(Q N_k + 1)^{5δ} ≤ (2M₀t)^{5δ}`; with `δ = ε/6`,
`2^{5ε/6}(2 + log M₀) ≤ (2 + 6/(eε))·1.16·M₀^{ε/6} ≤ (12/ε)M₀^{ε/6}` (Lemma 1.2) ✓. Bracket `Q_i ≤ M₀/r ≤ M₀` ✓.
Constant chain `K₇χ(δ) ≤ exp(exp((4B_χ+4)/δ))` ⇒ `C_ε ≤ exp(exp((24B_χ+30)/ε))` ✓ (absorbing `100/ε`).
TTL2 Thm 4.1(ii) uses (DI7_ε) only at `ε = w_N/128`, `w_N = 256A₀/log L`, where `log C_ε ≤ exp(A₀/ε) = L^{1/2}` ✓;
TTL2 needs χ even mod q, levels `4dq²` (q | level), exceptional `t_j ∈ iℝ∖{0}` — all match Thm 8.2's setting. ✓
TTL2's other inputs (Drappeau Prop 4.7 at the fixed tolerance `ε₁ = 1/100`, etc.) carry absolute constants. ✓
