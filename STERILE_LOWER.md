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

## 1. Two certified ingredients

**Lemma 1.1 (ℓ²-Minkowski form of SE Lemma 1.3; PROVED, elementary).** SE Lemma 1.3 (and hence SE Cor 1.4) holds with
(Cop) replaced by
  μ_w^w · n^{m(m+1)/2} · X^{w(w−1)/2} < D₀^{mw},   μ_w := 2√w · Γ(w/2 + 1)^{1/w} / √π                      (Cop₂)
(μ₁ = 1, μ₂ ≈ 1.60, μ₁₀ ≈ 5.76, μ₂₄ ≈ 12.7; μ_w < w for w ≥ 2, so (Cop₂) is weaker than (Cop)).
*Proof.* As in SE Lemma 1.3, the coefficient vectors (g_l X^l)_{l<w} of g ∈ 𝓛 form a lattice of determinant
Δ = n₁^{m(m+1)/2} X^{w(w−1)/2} ≤ n^{m(m+1)/2} X^{w(w−1)/2}. The closed Euclidean ball of radius ρ has volume
π^{w/2}ρ^w/Γ(w/2 + 1), which is ≥ 2^wΔ for ρ = 2(Γ(w/2 + 1)Δ)^{1/w}/√π; by Minkowski's convex body theorem some g ≠ 0 in 𝓛
has ‖v‖₂ ≤ ρ. For |y| ≤ X, |g(y)| ≤ Σ_l |g_l|X^l = ‖v‖₁ ≤ √w‖v‖₂ ≤ μ_w Δ^{1/w} < D₀^m by (Cop₂). The rest is verbatim. ∎
`scripts/zl_box.c` is `se_box.c` with w·ln w replaced by w·ln μ_w (computed with `lgammal`, padded up by a relative 10⁻¹²,
capped at w·ln w, so it is never weaker than se_box). Effect: −5 % (P) to −7 % (Q) on the tables near N = 2^30.

**Lemma 1.2 (tail by value-selected routes; PROVED, same proof as SE §3.3).** SE §3.3 proves, for every box of the
normalised mesh and every route of SE Table 2 / Q-routes, a term list Σ c N^e (ln N)^p bounding the box count for all N ≥ N₀,
and the combiner only needs, for the *chosen* route of each box, that every term has e < h and p ≤ (h − e) ln N₀
(h = 1/2 for P, 1 for Q; these make c N^{e−h}(ln N)^p nonincreasing for N ≥ N₀). The choice of route is free. `scripts/zl_tail.py`
chooses the admissible route of least value at N₀ (SE: least maximal exponent, then value). Result (SE_W = 40, M = 32):
G := bound/√N at N₀ is 7.26 (N₀ = 2^600; SE: 873.6), **1.36·10⁻² (N₀ = 2^800)**, 4.1·10⁻⁵ (2^1000); max exponent 0.4797 (2^800).

## 2. The certificate: r₀ = 2^{30.15625}

**Theorem 2.1 (explicit r₀ lowered; PROVED, computer-assisted, relative to exactly the inputs of SE Thm 3.4).**
**For every prime r ≥ 2^{30.15625} ≈ 1.19·10⁹, (S) holds; hence the r-generic line contains a sterile point x(u), u a
quadratic non-residue mod r, and no finite set of ET Prop 1.9 classes covers all sufficiently large primes whose least
quadratic non-residue is r.** Using only SE's reviewed engine `se_box.c` (without Lemma 1.1) the same holds for
r ≥ 2^{30.34375} ≈ 1.39·10⁹.
*Proof (certificate).* `ZL_L2=1 python3 scripts/zl_r0.py 30.15625 800 34` (log `data/zl/r0_certify.txt`; plain:
`data/zl/r0_certify_plain.txt`): SE's combiner `se_r0.py` with three changes, each covered by a proved statement:
(i) r-ranges [2^b, 2^{b+1/32}) for b < 34 (then quarter octaves as in SE), each term bounded by the certified table value at
the worst N-cell of the range and the largest weight 2r^{−k} resp. 2r^{−(K+1)/2} at r = 2^b — exactly SE's rule with a finer
partition; (ii) new certified tables `data/zl/P_q32.txt`, `Q_q32.txt` (se_box, N ∈ [2^24, 2^34), 1/32-octave cells),
`P_q32_l2.txt`, `Q_q32_l2.txt` (zl_box, N ∈ [2^29, 2^32)), `P_q1_hi.txt` (se_box, N ∈ [2^600, 2^842), octaves), each row an
upper bound for D_P resp. D_Q on its whole N-cell (SE §3.2; Lemma 1.1 for the _l2 tables); (iii) tails from N ≥ 2^800 (P) and
2^100 (Q) by Lemma 1.2, with SE's checks (all exponents < h, p ≤ (h − e)·ln N₀, merged exponents rounded up, negative ones
capped at 0; for r ≥ 2^800 every N = r^K is in the tail and every weighted term is decreasing in r). Result: max S = 0.49783
(at b = 30.15625; limit (r − 1)/(2r) > 0.4999999), no failure; for b ≤ 30.125 it fails (S = 0.5042 at b = 30.125). ∎
*What limits it now:* at r ≈ 2^{30.16} the terms are Q (k = 1) ≈ 0.45, P (K = 1) ≈ 0.04, P (K = 3) ≈ 0.006, rest < 10⁻³.
The P tail of SE (≈ 0.11 at 2^32) is gone. So r₀ is now set by **one number: the certified bound for the level-1 count
D_Q(r) of Type I N-points of 4/r**, which must be ≤ 0.22 r; the engine gives ≈ 0.22 r at r = 2^{30.16} against a true count
of a few hundred.
