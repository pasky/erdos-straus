# STERILE_LOWER — lowering the explicit r₀ of STERILE_EXPLICIT, and the r = 17 line (O228, wave Z-d2)

Status: in progress (O228). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on STERILE_EXPLICIT.md (= SE; Thm 3.4, r₀ = 2³²), its reviews R222/R223, POINTWISE_MORDELL17*.md (= M17, M17B–D),
FF_STERILE_PUSH.md / FF_STERILE_SMALL.md (division routes). Scripts `scripts/zl_*`, data `data/zl/`.

## 0. Iteration log

* (I1) **Where S(r) lives (arithmetic on SE's certified tables plus new tables for N ∈ [2^15, 2^50), `se_box` unchanged,
  `/tmp`-style exploration, recorded in §1).** Terms of (S) at r ≈ 2^b (each term = table value × weight):

  | b | Q, k=1 | P, K=1 | P, K=3 | P, K=5 | P, K≥7 |
  |---|---|---|---|---|---|
  | 16 | 11.0 | 1.86 | 6.62 | 2.04 | 0.29 |
  | 20 | 5.41 | 0.74 | 1.16 | 0.14 | 0.01 |
  | 24 | 2.32 | 0.26 | 0.16 | 0.008 | — |
  | 28 | 0.935 | 0.084 | 0.020 | 0.001 | — |
  | 30 | 0.578 | 0.046 | 0.007 | — | — |
  | 32 | 0.350 | 0.025 | 0.002 | — | — |

  plus SE's P tail (N ≥ 2^600), ≈ 0.109 at b = 32 and growing like r^{−1/2}·(#K) below. So the binding term is the
  **level-1 Type I count** 2D_Q(r)/r, then level-1 Type II, then K = 3 below b ≈ 22. Target r₀ = 10⁶ (b ≈ 20) would need
  the Q₁ bound lowered ×25 and the P₃ bound ×5.
* (I2) **Division routes (FF_STERILE_SMALL Lemma 1.1) over ℤ.** The FF lemma "a monic divisor of degree > deg v₁ determines
  v₁" has the ℤ twin "a divisor 4a > e-window of N + e fixes e mod 4a", which SE already uses in routes A, F, G, I, J and in
  Q's fac/fca/fda (SE §3.4 note). Nothing new to transplant there; the FF gain came from degree rigidity
  (y + t = max(a, b) exactly), which over ℤ is only an inequality up to constants — exactly where the polylog box count lives.
* (I3) **Local engine tweaks, measured on the dominant Q₁ boxes (`se_box` dumps at N = 2^24, 2^28, 2^32).**
  (a) Finer boxes (ratio 2^{1/2}, 2^{1/4}): worse (+2 %, +69 % at N = 2^20; the per-box "+1" and the per-pair minimum 1
  dominate). (b) Exact max τ(n), τ₃(n) for n ≤ X instead of SE's envelope min_η C_k(η)X^η: the envelope is within 10 % of
  the true maximum for X ∈ [2^20, 2^80] (e.g. X = 2^64: max τ = 184320, envelope 1.87·10⁵) — no gain. (c) Excluding small
  e (exact enumeration of e ≤ E by sieving eF + 1): removing all boxes with e-range ⊂ [1, 4096] lowers the Q₁ bound only
  by 40 % — the mass is spread over ≈ 7000 boxes, not concentrated. (d) Lenstra's "≤ 11 divisors in a class mod s > n^{1/3}"
  per (c, d)-row: < 2 % (the heavy rows sit at 4cd ≈ (F²)^{1/3}, just below Lenstra's threshold).
  Conclusion (Assessment): the Q₁ bound ≈ 10·F^{0.6}·ln F is "(number of (c, d) pairs with cd ≈ F^{0.6}) × (a Coppersmith
  constant ≈ 4 per f-window)", i.e. ET's Type I exponent 3/5 with an honest constant; no local tweak gives the ×3–25 needed.
* (I4) **The P tail was the cheap slack.** SE's `se_tail` chooses, per box, the route of least *maximal exponent*;
  its constant at N₀ = 2^600 is G = 873 (bound/√N), while `se_box` itself gives 7·10⁻¹¹ there. Choosing instead the route
  of least *value at N₀* among routes whose every term is admissible (e < 1/2, p ≤ (1/2 − e) ln N₀ — exactly SE's
  decreasing-check, so validity is unchanged) gives G = 7.26 at N₀ = 2^600 and **G = 4.1·10⁻⁵ at N₀ = 2^1000**
  (`scripts/zl_tail.py`, SE_W = 40). With `se_box` tables extended to 2^1000 the tail term disappears from (S).
