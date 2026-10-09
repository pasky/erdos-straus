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
