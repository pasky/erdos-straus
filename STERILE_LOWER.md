# STERILE_LOWER — lowering the explicit r₀ of STERILE_EXPLICIT, and the r = 17 line (O228, wave Z-d2)

Status: checkpoint 1 (O228): Thm 2.1 (r₀ = 2^{30.15625}, certified) + Lemma 3.1 (joint level-1 parametrisation) + Comp. 4.1; not yet reviewed. **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
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
  (a) Finer boxes (ratio 2^{1/2}, 2^{1/4}): worse (Q: +1 %, +69 %; P: +14 %, +69 % at N = 2^20; the per-box "+1" and the per-pair minimum 1
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

## 3. Below 2^30: the level-1 terms must be certified per r — and can be, jointly (amortised polylog per prime)

**Assessment 3.0 (why uniform box bounds stop near 2^30).** With exact level 1 the remaining terms of (S) are
P(K = 3) + P(K = 5) + … + Q(k ≥ 3) ≈ 0.16 (b = 24), 0.45 (b ≈ 22), 1.3 (b = 20) (table (I1)). So a certificate down to
r ≈ 2^{22.5} needs only the *level-1* counts D_Q(r), D_P(r) to be ≤ ~0.15 r, which they are by 5–6 orders of magnitude
(true values: a few hundred), but the uniform engine bound for D_Q(r) is ≈ 10·r^{0.6}·ln r, i.e. 2.3·(r/2) at 2^24
((I3): no local tweak changes this by more than ~10 %). Exact per-r enumeration costs ≍ r per prime (≈ 0.4r pairs (a, d) for
P, (r/2)·ln r for Q), i.e. ≍ X² over all primes up to X: hopeless for X ≈ 2^30.

**Lemma 3.1 (joint parametrisation of level-1 data; PROVED, elementary).** (i) For positive integers a, c, d put f = 4acd − 1.
Every positive integer N ≡ −4a²d (mod f) gives a P-datum (a, b, c, d, e) of N with b = (Nc + a)/f, e = (N + 4a²d)/f, and
a ≤ b ⇔ cN ≥ 4a²cd − 2a; conversely every P-datum of N arises so from its own (a, c, d). (ii) For positive integers
a, d, f with f | 4a²d + 1 and every c ≥ 1 with n := 4acd − f > 0, (a, b, c, d) with b = (na + c)/f is a Q-datum of n
(e = (4a²d + 1)/f); a ≤ b ⇔ b ≥ a; conversely every Q-datum arises so (f = 4acd − n).
*Proof.* (i) f ∣ Nc + a since Nc + a ≡ −4a²cd + a = −af (mod f); 4abd = (4acdN + 4a²d)/f = ((f + 1)N + 4a²d)/f = N + e;
ce = c(N + 4a²d)/f = (a(f + 1) + Nc)/f = a + b. b ≥ a ⇔ Nc + a ≥ a(4acd − 1). Converse: SE Lemma 1.1(i)–(ii).
(ii) e·f = 4a²d + 1, and f ∣ na + c as na + c ≡ 4a²cd + c = c(4a²d + 1) ≡ 0 (mod f); then
4abcd = (n + f)b = nb + na + c = n(a + b) + c, and a + b = (af + na + c)/f = c(4a²d + 1)/f = ce. Converse: SE §3.2 (ef = 4a²d + 1, f = 4acd − F). ∎
*Check (EVIDENCE):* `scripts/zl_joint_check.py X` counts P- and Q-data of every n ∈ [X, 2X) both ways (joint loops over
(a, c, d) resp. (a, d, f, c) vs. R223's per-n enumerators): X = 300 and X = 1000, **0 mismatches** (3301 + 4909 resp.
17328 + 25674 data).
**Consequence (Assessment, cost model).** The level-1 counts of *all* N in a dyadic range [X, 2X) are obtained in one sweep:
P: Σ_{(a,c,d): acd ≲ X} (X/(4acd) + 1) ≈ X(ln X)²/2 + X(ln X)³/24 steps, no factoring; Q: one divisor list of 4a²d + 1 per pair
(a, d), ad ≤ X (sieve in d for fixed a), then Σ τ(4a²d + 1)(X/(4ad) + 1) increments. That is **polylog per prime** instead of
≍ r: ≈ 10^{11}–10^{12} elementary steps for [2^29, 2^30], less below. Combined with the existing uniform bounds for
K, k ≥ 3, this would certify (S) for every prime r ≥ ≈ 2^{22.5} (≈ 6·10⁶; P at K = 3 becomes binding below). Not run here
(multi-day, sieve engineering for large a); flagged as the concrete next step (SHARP 1).

## 4. Small r and the r = 17 line

**Computation 4.1 (level-1 survivors; CERTIFIED by exhaustive exact enumeration, `scripts/zl_level1_survivors.py`, R223's
enumerators, output `data/zl/level1_survivors.txt`).** For every prime 3 ≤ r ≤ 13 *all* non-residue cells are covered at
level 1; for **every prime 17 ≤ r < 20000 some non-residue cell survives level 1** (r = 17: {5, 7}; r = 19: {2, 3, 10, 13};
r = 23: {5, 14}; least surviving fraction 2/11 at r = 23; it tends to 1 quickly, e.g. 9898/9996 at r = 19993). So the
dichotomy "r ≤ 13: finite ET covering at level 1; r ≥ 17: level 1 leaves room" is exact up to 2·10⁴. This is necessary,
not sufficient, for sterility: deeper levels are controlled by (S) only for r ≥ 2^{30.16} (Thm 2.1).

**Assessment 4.2 (r = 17 is out of reach of every box-sum certificate).** M17D §1 needs D_P(17^K) ≤ 2.5·17^{0.4K} from K = 15
(N ≈ 2^{61}) with no log loss; SE's engine gives D_P(N) ≈ 550√N there (G = bound/√N ≈ 930 at 2^{39}, 550 at 2^{61}, 100 at 2^{91}, < 1 only
from ≈ 2^{159} on, 7·10⁻¹¹ at 2^{600}; `data/se/P_q4.txt`). With weights 17^{−(K+1)/2} this is Σ_K 2G/√17 ≫ 1: off by ≈ 10⁴, and the true counts are
≈ 10⁻⁶ of the bound. Pointwise (M17D §2–3): for a rational u = −p/q every covering datum satisfies, besides M17D's
"unbalanced" constraint, the exact identity below; it restricts but does not count covering data to zero.
**Lemma 4.3 (U–V factorisation; PROVED, elementary).** Let (a, b, c, d, e) be a P-datum of N = r^{2L−1}, W = r^L, r ∤ ab, with
qa − pb = zW (p, q, z ∈ ℤ). Put G := ((p + q)² + 4rdz²)/e (an integer: M17D Remark 2.4 with 17 ↦ r), U := Ga − cp², V := Gb − cq². Then
Ub = cq²a + rz², Va = cp²b + rz² (so U, V > 0 are integers) and **UV = c²p²q² + G·r·z²**. In particular, if a ≤ b and
b ≤ N/(2(|p| + q)²), then e ≤ 4q²a.
*Proof.* Remark 2.4 reads e[c(p²b + q²a) + rz²] = ab·eG, i.e. c(p²b + q²a) + rz² = Gab; so Ub = Gab − cp²b = cq²a + rz² and
symmetrically; multiply: UV·ab = (cq²a + rz²)(cp²b + rz²) = ab·(c²p²q² + rz²·G) after substituting Gab. For the last claim,
U ≥ 1 gives 1 ≤ cq²a/b + rz²/b ≤ 2q²a/e + (qa − pb)²/(Nb) ≤ 2q²a/e + (|p| + q)²b/N ≤ 2q²a/e + 1/2. ∎
(Check: u = 11/9 ∈ C₇ at level 2 via (1, 78, 1, 16): z = 3, G = 124, U = 3, V = 9591, UV = 28773 = 9801 + 124·17·9.)
Outcome for goal (2): **undecided** (no sterile point proved, no covering found); M17D's Conjecture 4.2 and conditional
Theorem 4.1 stand unchanged.

## 5. Sparks (not pursued here)

1. **Run §3** (SHARP 1): a C sweep of Lemma 3.1 over dyadic ranges [2^{22}, 2^{30.16}], recording max over primes r of
   (D_P(r) + D_Q(r))/r per 1/32-octave, plus the existing tables for K, k ≥ 3 → expected r₀ ≈ 2^{22.5}. For Q the only
   non-trivial part is listing divisors of 4a²d + 1 for ad ≤ X (sieve in d for a ≤ X^{1/2}; for a > X^{1/2} use cd < X^{1/2}
   and enumerate via (c, d) instead).
2. Then the binding term is P at K = 3 (N = r³): the same joint idea for level 2 (all N = r³ with r in a range are sparse, so
   Lemma 3.1(i) applies with N restricted to cubes: count triples (a, c, d) with r³ ≡ −4a²d (mod 4acd − 1) — a cubic-residue
   condition; cost per r is no longer polylog). Pushing below 2^{22} needs a better K = 3 bound or this.
3. Lemma 4.3 for a fixed rational u: U is a small positive integer (U ≤ 2q²a/e + 1/2), so covering data of u come in
   families indexed by U; a descent U ↦ U' (Vieta on Ga − cp²) preserving "W is a power of r" would prove sterility. None found.
