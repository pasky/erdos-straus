# STERILE_LOWER — lowering the explicit r₀ of STERILE_EXPLICIT, and the r = 17 line (O228, wave Z-d2)

Status: checkpoint 1 (O228): Thm 2.1 (r₀ = 2^{30.15625}, certified) + Lemma 3.1 (joint level-1 parametrisation) + Comp. 4.1; hostile reviews R231 (`reviews/sterile-lower-review.md`) and R232 (`reviews/sterile-lower-review-2.md`): no FATAL/MAJOR, Thm 2.1 SOUND (both variants re-certified); minors applied as (R231 repair)/(R232 repair). Checkpoint 2 (round 2): §6 Thm 6.3 (r₀ = 2^{21.4375} ≈ 2.84·10⁶, joint sweep), §7 (r = 17 descent: negative). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
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
  Conclusion (Assessment): the Q₁ bound ≈ 50·F^{0.6}·ln F (R231 repair m6: was "10·"; on the certified tables 48.8–51.1 at
  b = 24…32) is "(number of (c, d) pairs with cd ≈ F^{0.6}) × (≈ 20 divisor candidates per pair, summed over the f-windows of a
  (c, d)-row; ≈ 4 in the top window f ≈ F)" — the per-row figure is the dump value 3.54·10⁵ / 16384 ≈ 21.6 for the heaviest row at
  F = 2^24 — i.e. ET's Type I exponent 3/5 with an honest constant; no local tweak gives the ×3–25 needed.
* (I4) **The P tail was the cheap slack.** SE's `se_tail` chooses, per box, the route of least *maximal exponent*;
  its constant at N₀ = 2^600 is G = 873 (bound/√N), while `se_box` itself gives 7·10⁻¹¹ there. Choosing instead the route
  of least *value at N₀* among routes whose every term is admissible (e < 1/2, p ≤ (1/2 − e) ln N₀ — exactly SE's
  decreasing-check, so validity is unchanged) gives G = 7.26 at N₀ = 2^600 and **G = 4.1·10⁻⁵ at N₀ = 2^1000**
  (`scripts/zl_tail.py`, SE_W = 40). With `se_box` tables extended to 2^1000 the tail term disappears from (S).
  (R231 repair m5 / R232 repair m4: two separate effects. Like-for-like at N₀ = 2^600 the value selection alone gives 873.6 → 7.26
  (and raises the max exponent there from 0.4797 to 0.4960); at N₀ = 2^800 SE's own route choice already gives G = 1.01 (R231), so of
  the ×6.4·10⁴ between "873 at 2^600" and "0.0136 at 2^800" about ×860 is the move N₀: 2^600 → 2^800 (new table `P_q1_hi`) and ×74
  the re-selection. R231: Thm 2.1 (ℓ² variant) holds even with SE's selection at 2^800 (max S 0.49788). R232: with SE's *original*
  tail (N₀ = 2^600) the se_box-only certificate would fail (S ≈ 0.494 + 0.021 > 0.5 at b = 30.34375).)

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
G := bound/√N at N₀ is 7.26 (N₀ = 2^600; SE: 873.6), **1.36·10⁻² (N₀ = 2^800**; SE's selection there: 1.01, R231), 4.1·10⁻⁵ (2^1000);
max exponent 0.4797 (2^800), 0.4960 (2^600). (R231 repair m5 / R232 repair m4: see (I4) for the split of the gain.)

## 2. The certificate: r₀ = 2^{30.15625}

**Theorem 2.1 (explicit r₀ lowered; PROVED, computer-assisted, relative to the inputs of SE Thm 3.4 plus Lemma 1.2 (both variants)
and Lemma 1.1 (the 2^{30.15625} variant); R232 repair m5: was "exactly the inputs of SE Thm 3.4").**
**For every prime r ≥ 2^{30.15625} ≈ 1.19·10⁹, (S) holds; hence the r-generic line contains a sterile point x(u), u a
quadratic non-residue mod r, and no finite set of ET Prop 1.9 classes covers all sufficiently large primes whose least
quadratic non-residue is r.** Using only SE's reviewed engine `se_box.c` (without Lemma 1.1) the same holds for
r ≥ 2^{30.34375} ≈ 1.39·10⁹.
*Proof (certificate).* `ZL_L2=1 python3 scripts/zl_r0.py 30.15625 800 34` (log `data/zl/r0_certify.txt`; plain:
`data/zl/r0_certify_plain.txt`): SE's combiner `se_r0.py` with three changes, each covered by a proved statement:
(i) r-ranges [2^b, 2^{b+1/32}) for b < 34 (then quarter octaves as in SE), each term bounded by the certified table value at
the worst N-cell of the range and the largest weight 2r^{−k} resp. 2r^{−(K+1)/2} at r = 2^b — exactly SE's rule with a finer
partition; (ii) new certified tables `data/zl/P_q32.txt`, `Q_q32.txt` (se_box, N ∈ [2^24, 2^34), 1/32-octave cells),
`P_q32_l2.txt`, `Q_q32_l2.txt` (zl_box, N ∈ [2^29, 2^32)), `P_q1_hi.txt` (se_box, N ∈ [2^600, 2^842), octaves; (R232 repair m7) the
run `se_box P 600 999 1 1 64 24` was stopped deliberately after row 841 to free a core, rows 600–841 are complete lines, only rows
≤ 799 are used, and these coarse-box rows (box ratio 2^9–2^13) have not been independently re-checked — R232's re-certification
of Thm 2.1 does not use them), each row an
upper bound for D_P resp. D_Q on its whole N-cell (SE §3.2; Lemma 1.1 for the _l2 tables); (iii) tails from N ≥ 2^800 (P) and
2^100 (Q) by Lemma 1.2, with SE's checks (all exponents < h, p ≤ (h − e)·ln N₀, merged exponents rounded up, negative ones
capped at 0; for r ≥ 2^800 every N = r^K is in the tail and every weighted term is decreasing in r). Result: max S = 0.49783
(at b = 30.15625; limit (r − 1)/(2r) > 0.4999999), no failure; for b ≤ 30.125 it fails (S = 0.5042 at b = 30.125). ∎
*What limits it now:* at r ≈ 2^{30.16} the terms are Q (k = 1) ≈ 0.45, P (K = 1) ≈ 0.04, P (K = 3) ≈ 0.006, rest < 10⁻³.
The P tail of SE (≈ 0.11 at 2^32) is gone (by Lemma 1.2 together with the move to N₀ = 2^800, see (I4)). So r₀ is now set by **one number: the certified bound for the level-1 count
D_Q(r) of Type I N-points of 4/r**, which must be ≤ 0.22 r; the engine gives ≈ 0.22 r at r = 2^{30.16} against a true count
of a few hundred.

## 3. Below 2^30: the level-1 terms must be certified per r — and can be, jointly (amortised polylog per prime)

**Assessment 3.0 (why uniform box bounds stop near 2^30).** With exact level 1 the remaining terms of (S) are
P(K = 3) + P(K = 5) + … + Q(k ≥ 3) ≈ 0.16 (b = 24), 0.45 (b ≈ 22), 1.3 (b = 20) (table (I1)). So a certificate down to
r ≈ 2^{22.5} needs only the *level-1* counts D_Q(r), D_P(r) to be ≤ ~0.15 r, which they are by 5–6 orders of magnitude
(true values: a few hundred), but the uniform engine bound for D_Q(r) is ≈ 50·r^{0.6}·ln r (R231 repair m6: was "10·"), i.e. 2.3·(r/2) at 2^24
((I3): no local tweak changes this by more than ~10 %). Exact per-r enumeration costs ≍ r per prime (≈ 0.4r pairs (a, d) for
P, (r/2)·ln r for Q), i.e. ≍ X² over all primes up to X: hopeless for X ≈ 2^30.

**Lemma 3.1 (joint parametrisation of level-1 data; PROVED, elementary).** (i) For positive integers a, c, d put f = 4acd − 1.
Every positive integer N ≡ −4a²d (mod f) gives a P-datum (a, b, c, d, e) of N with b = (Nc + a)/f, e = (N + 4a²d)/f, and
a ≤ b ⇔ cN ≥ 4a²cd − 2a; conversely every P-datum of N arises so from its own (a, c, d). (ii) For positive integers
a, d, f with f | 4a²d + 1 and every c ≥ 1 with n := 4acd − f > 0, (a, b, c, d) with b = (na + c)/f is a Q-datum of n
(e = (4a²d + 1)/f); a ≤ b ⇔ na + c ≥ af ⇔ c ≥ a(f − n) (automatic if f ≤ n) (R231 repair m3 / R232 repair m1: was the
vacuous "a ≤ b ⇔ b ≥ a"); conversely every Q-datum arises so (f = 4acd − n).
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
from ≈ 2^{157} on (R231 repair m8: last cell with G ≥ 1 is 2^{156.75}), 7·10⁻¹¹ at 2^{600}; `data/se/P_q4.txt`). With weights 17^{−(K+1)/2} this is Σ_K 2G/√17 ≫ 1: off by ≈ 10⁴, and the true counts are
≈ 10⁻⁶ of the bound. Pointwise (M17D §2–3): for a rational u = −p/q every covering datum satisfies, besides M17D's
"unbalanced" constraint, the exact identity below; it restricts but does not count covering data to zero.
**Lemma 4.3 (U–V factorisation; PROVED, elementary).** Let (a, b, c, d, e) be a P-datum of N = r^{2L−1}, W = r^L, r ∤ ab, with
qa − pb = zW (p, z ∈ ℤ, q ≥ 1; R231 repair m2 / R232 repair m2: q ≥ 1 is needed for U, V > 0). Put G := ((p + q)² + 4rdz²)/e (an
integer: the identity e[c(p²b + q²a) + rz²] = ab[(p + q)² + 4rdz²] (M17D Remark 2.4 with 17 ↦ r; it only uses W² = rN) gives
e ∣ ab[(p + q)² + 4rdz²], and gcd(e, ab) divides 4abd − e = N = r^K with r ∤ ab, so gcd(e, ab) = 1), U := Ga − cp², V := Gb − cq². Then
Ub = cq²a + rz², Va = cp²b + rz² (so U, V > 0 are integers) and **UV = c²p²q² + G·r·z²**. In particular, if a ≤ b and
b ≤ N/(2(|p| + q)²), then e ≤ 4q²a.
*Proof.* Remark 2.4 reads e[c(p²b + q²a) + rz²] = ab·eG, i.e. c(p²b + q²a) + rz² = Gab; so Ub = Gab − cp²b = cq²a + rz² and
symmetrically; multiply: UV·ab = (cq²a + rz²)(cp²b + rz²) = ab·(c²p²q² + rz²·G) after substituting Gab. For the last claim,
U ≥ 1 gives 1 ≤ cq²a/b + rz²/b ≤ 2q²a/e + (qa − pb)²/(Nb) ≤ 2q²a/e + (|p| + q)²b/N ≤ 2q²a/e + 1/2. ∎
(Check: u = 11/9 ∈ C₅ (R231 repair m1: was "C₇"; 11/9 ≡ 5 mod 17, box −63 ≡ 226 mod 289) at level 2 via (1, 78, 1, 16): z = 3, G = 124, U = 3, V = 9591, UV = 28773 = 9801 + 124·17·9.)
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

## 6. The joint level-1 sweep, run (O228 round 2): r₀ lowered to 2^{21.4375} ≈ 2.84·10⁶

**6.1 Splitting the level-1 Q count.** For a prime r and parameters A, Y,
  D_P(r) + D_Q(r) ≤ JP(r) + JQ_{A,Y}(r) + 2·#{(a, d) : ad ≤ Y} + B_A(r),
where JP(r) = number of all P-data of r (a ≤ b) and JQ_{A,Y}(r) = number of Q-data of r (a ≤ b) with a < A and ad > Y, both
computed exactly by the sweep; 2·#{ad ≤ Y} bounds the Q-data with ad ≤ Y (at most two per pair (a, d): M17C Lemma 2.1(iv), as
SE route AD); B_A(r) is the `zl_boxa` bound (= `zl_box` restricted to Q-boxes whose a-enclosure [a₀, a₁] = [(P + F₀)/(4λ²CD),
(λP + F₁)/(4CD)] has a₁ ≥ A) for the Q-data with a ≥ A; if A > (X₁ + 1)/2 + 1 then B_A = 0, since every Q-datum of F has
a ≤ acd ≤ (F + 1)/2 (M17D Lemma 2.2(ii)). (D_P, D_Q count in-cell data; the sweep counts all data, a superset.)
**PROVED** from Lemma 3.1, its converse halves, and acd ≤ (r + 1)/2, f ≤ r + 2 (M17D Lemma 2.2(ii)), which give the sweep's
ranges d ≤ (2X₁ + 2)/(4a), f ≤ X₁ + 1.

**6.2 The sweep (`scripts/zl_sweep.c X0 X1 A Y 32`).** P: loop over triples (a, c, d) and the arithmetic progression
N ≡ −4a²d (mod 4acd − 1), N ≥ ⌈4a²d − 2a/c⌉ (Lemma 3.1(i)); no factoring. Q: for each a < A, m = 4a²d + 1 is factored
completely — by a segmented sieve in d with all primes ≤ √m (one modular inverse per (a, p); the leftover cofactor is prime),
or, for short rows (`ZL_SHORT`), number by number (trial division below 2^10, deterministic Miller–Rabin with the 12 prime
bases ≤ 37, Brent–Pollard ρ); then all divisors f ≤ X₁ + 1 and all c with n = 4acd − f ∈ [X₀, X₁), na + c ≥ af
(Lemma 3.1(ii)). Counters only at primes n (odd-n sieve bitmap), 16-bit, saturation ⇒ failure; the prime-table and
divisor-buffer limits exit with an error (one false alarm of the prime-table check was fixed: fail-closed, not a wrong count).
Split runs (`ZL_ALO`, `ZL_NOP`, `ZL_BIN`) are merged per prime by `zl_merge.py` (exact integer cell endpoints).
*Validation (EVIDENCE for the implementation of PROVED statements):* `scripts/zl_sweep_check.py` compares, for every n, the
sweep's counts with R223's per-n enumerators: n ∈ [1001, 2000) and [3001, 6000), "all" mode (every odd n, A = X₁, Y = 0) and
prime mode, for the binaries actually used (sieve version and ρ version with every row forced short): **0 mismatches**; on
n ∈ [10⁶, 2·10⁶), A = 20000, Y = 1500 the sieve version, the ρ version (all rows short / ZL_SHORT = 4) and the final binary
give byte-identical per-n dumps (2.9·10⁷ counted data); a split run merged = the unsplit run (all cell lines identical).

**6.3 Certificate (`scripts/zl_r1.py SWEEP A Y ENGINE`, fail-closed).** For each cell j (r ∈ [2^{j/32}, 2^{(j+1)/32})):
level-1 terms ≤ 2(max_r (JP + JQ) + 2·#{ad ≤ Y} + B_A)/2^{j/32}; deeper terms (K, k ≥ 3, tails) exactly as `zl_r0.py`, with the
extra certified P tables `data/zl/P_q32_k3.txt` (se_box, N ∈ [2^62, 2^70), 1/32-octaves) and, for octave 21,
`P_q32_k3_l2.txt`, `P_q32_k5_l2.txt` (zl_box, N ∈ [2^62, 2^66) and [2^104, 2^110)).

| r-octave | A | Y | sweep (s) | max_r JP + JQ | max S | log |
|---|---|---|---|---|---|---|
| [2^29, 2^{30.15625}) | 40000 | 536870 | 4853 | 75210 | 0.3266 | r1_29 |
| [2^28, 2^29) | 65536 | 268435 | 3053 | 61294 | 0.3584 | r1_28 |
| [2^27, 2^28) | 32768 | 134217 | 1068 | 46749 | 0.4732 | r1_27 |
| [2^26, 2^27) | 131072 | 67108 | 2422 | 40243 | 0.3786 | r1_26 |
| [2^25, 2^26) | 262144 | 8388 | 4440 | 38092 | 0.3130 | r1_25 |
| [2^24, 2^25) | 524288 | 4194 | 426 + 4415 (split) | 33174 | 0.2891 | r1_24 |
| [2^23, 2^24) | all rows | 2097 | 1801 | 23092 | 0.2536 | r1_23 |
| [2^22, 2^23) | all rows | 1048 | 537 | 20008 | 0.4173 | r1_22 |
| [2^{21.4375}, 2^22) | all rows | 300 | 157 | 16084 | 0.4832 | r1_21_l2 (cells j ≥ 686) |

**Theorem 6.3 (PROVED, computer-assisted; inputs as Thm 2.1 plus M17C Lemma 2.1(iv) and M17D Lemma 2.2(ii)):
(S) holds for every prime r ≥ 2^{21.4375} ≈ 2.84·10⁶.** Hence for every such r the r-generic line contains a sterile point,
and no finite set of ET Prop 1.9 classes covers all sufficiently large primes whose least quadratic non-residue is r.
(Thm 2.1 for r ≥ 2^{30.15625}; the table for 2^{21.4375} ≤ r < 2^{30.15625}; the cells are contiguous.)
*What stops it now:* the K = 3 term (P-data of N = r³, uniform engine bound): the deeper terms alone are 0.47–0.58 for
j ≤ 685 (b ≤ 21.4); with exact level 1 the cells j = 681 (0.4997) pass and j = 685 (0.5013), 682 (0.567) fail. Going lower needs the
level-2 analogue of the sweep (N = r³: Lemma 3.1(i) with N restricted to cubes) — Spark 2 of §5.
*Correction to §§0, 2 (not rewritten during review):* the exact level-1 counts of the worst primes are 1.6·10⁴–7.5·10⁴, not "a few
hundred" (that is the typical size); still ≤ 6·10⁻³·r.

## 7. r = 17: the descent question for Lemma 4.3 (Assessment; written during O228 round 2)

For a rational u = −p/q and fixed (c, d, z), the covering condition of M17D Lemma 2.1 plus 4abd = N + e, a + b = ce,
W² = rN is equivalent to: **(a, b) is an integral point of the conic**
  Γ_{c,d,z}: c(qa − pb)² − 4rcdz²·ab + rz²(a + b) = 0,   **and (qa − pb)/(rz) = ±r^{L−1}**
(PROVED, elementary: given (a, b) on Γ put X = qa − pb, N := X²/(rz²), e := (a + b)/c; then Γ reads cX² = rz²(4abcd − (a + b)),
i.e. N = 4abd − e; the second condition says N = r^{2L−1}; integrality of e, N and r ∤ ab are extra conditions.) Mod r and
mod r², Γ already forces r | X and N ≡ 0 (mod r), so the conic family is exactly "coverings of u by P-data of N = r·w² at
modulus W = rw" with w arbitrary — the levels are the points where w is a power of r. Consequences (Assessment):
(i) A descent would have to be an automorphism of Γ preserving "w ∈ r^ℕ". The obvious ones (Vieta involutions in a or b)
do not even preserve integrality: on the known covering (1, 78, 1, 16) of 11/9 at level 2 (c = 1, d = 16, z = 3) they give
a′ = bV/(cq²) = 748098/81 and b′ = aU/(cp²) = 3/121. (ii) Along an infinite orbit of integral points of a fixed Γ, w satisfies a
binary linear recurrence, and "w = ±r^k" is an S-unit equation with finitely many, effectively bounded solutions (Baker) — but
Γ ranges over infinitely many (c, d, z), with no uniformity. So sterility of a rational point is a *uniform S-unit problem
over a two-parameter family of conics*; nothing in reach decides it. (iii) Lemma 4.3's U = Ga − cp² is the value of a linear
form at a point of Γ; U ≥ 1 is what forces e ≤ 4q²a, a sieve-type restriction, not an exclusion.
Outcome: no descent found; r = 17 stays undecided (Conjecture M17D 4.2 unchanged).
