# R232 — hostile review #2 of STERILE_LOWER.md (O228), round 1 (no edits to the author's files)

Reviewer branch: side-agent/review-sterile-lower (merged side-agent/sterile-lower at start).
Scope: Thm 2.1, Lemmas 1.1, 1.2, the 1/32-octave combiner zl_r0.py, Lemma 3.1, Comp 4.1, Lemma 4.3, labels.
From-scratch scripts: scripts/review_r232_*.py.

## Summary verdicts
(filled in as the review proceeds)

## Defects
(numbered; FATAL / MAJOR / MINOR)

## Detailed checks

### Comp 4.1 (level-1 survivors) — SOUND
`scripts/review_r232_level1.py` (from scratch, no project imports): enumerates *all* N-points of Σ^II_r (4abcd = a + b + rc,
a ≤ b; loop (a, d, c) with the two monotone cut-offs b ≥ a and c ≤ a + b) and of Σ^I_r (4abcd = r(a + b) + c, a ≤ b;
f = 4acd − r ∈ [1, r + 2]), every tuple asserted against the defining equation; boxes −f, −f' (P, K = 1, r ∤ cd) and
−4a²d, −4b²d (Q, r ∤ e; covers Q⁻¹ since (4a²d)(4b²d) = (4abd)² ≡ 1). No restriction beyond the definitions (r ∤ ab, r ∤ c
are reported if they ever bite: they never do at N = F = r, as expected — r | a or r | c is impossible at level 1).
Extra (r < 200): level-1 U-boxes −e, −1/e enumerated independently add no new covered non-residue (consistent with M17 L5.2).
Result for **all 2261 primes 3 ≤ r < 20000**: (#non-residues, #survivors) identical to `data/zl/level1_survivors.txt` line by
line; survivors = ∅ exactly for r ∈ {3, 5, 7, 11, 13}; r = 17: {5, 7}; r = 19: {2, 3, 10, 13}; r = 23: {5, 14}; least
surviving fraction for r ≥ 17 is 2/11 (r = 23). Log: `data/review_r232/level1_r20000.txt`. The label CERTIFIED is justified.
Note (not a defect): the author's script imports R223's enumerators; this run is an independent second implementation.

### Lemma 3.1 (joint parametrisation) — SOUND (one wording MINOR, m1)
Re-derived: (i) Nc + a ≡ −4a²cd + a = −a·f (mod f) ✓; 4abd = N + e ✓ (multiply by f: 4ad(Nc + a) = (f + 1)N + 4a²d);
ce = a + b ✓; b ≥ a ⇔ Nc + a ≥ a(4acd − 1) ⇔ cN ≥ 4a²cd − 2a ✓; converse = SE L1.1(i),(ii) ✓ (e > 0, b > 0 automatic).
(ii) f | na + c since na + c ≡ 4a²cd + c = c(4a²d + 1) ≡ 0 ✓; 4abcd = n(a + b) + c ✓; ce = a + b ✓; converse needs
f = 4acd − n ≥ 1, true as fb = na + c > 0, and f | 4a²d + 1 is ET's ef = 4a²d + 1 ✓.
Brute force (`scripts/review_r232_joint.py`): per-n enumerators by *divisors* (f | n + 4a²d, f ≡ −1 (4ad), resp.
f | 4a²d + 1, f ≡ −n (4ad)) — a different loop structure from the lemma — themselves validated against a naive 4-fold
(a, b, c, d) search for n ≤ 12; then the lemma's two sweeps implemented literally (every produced tuple asserted against the
defining equations and e-formula) and compared **as sets of tuples** per n: X = 300: 3301 P + 4909 Q data, X = 1000:
17328 P + 25674 Q data (the author's totals), 0 mismatching n. (X = 3000: see below.)
The cost model after the lemma is correctly labelled Assessment and is plausible (Σ_{acd≲X} X/(4acd) ≈ X(ln X)³/24).

### Lemma 4.3 (U–V factorisation) — SOUND (MINOR m2: implicit q ≥ 1)
Re-derived without M17D: e·[c(p²b + q²a) + rz²] − ab[(p + q)² + 4rdz²] = (a + b)(p²b + q²a) − ab(p + q)² + rz²(e − 4abd)
= (qa − pb)² − rz²N = z²W² − rz²r^{2L−1} = 0, using ce = a + b, 4abd = N + e, W² = rN. Hence Gab = c(p²b + q²a) + rz² ∈ ℤ
and Ge ∈ ℤ; gcd(e, ab) = 1 (a prime dividing e and a divides 4abd − e = N, so it is r, excluded by r ∤ ab) gives G ∈ ℤ —
so the integrality does not even need M17D Remark 2.4. Ub = cq²a + rz², Va = cp²b + rz², UV·ab = ab(c²p²q² + Grz²) ✓.
Size claim: U ≥ 1, c ≤ 2b/e, rz² = (qa − pb)²/N ≤ (|p| + q)²b²/N ✓ ⇒ e ≤ 4q²a ✓. The worked example (1, 78, 1, 16),
u = 11/9 (p = −11, q = 9), N = 17³: z = 3, G = 124, U = 3, V = 9591 ✓.
`scripts/review_r232_uv.py`: all in-cell P-data of N = r^{2L−1} for (r, L) ∈ {(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(11,2),(13,2),
(17,2),(19,2)}, 30 random (p, q) with qa ≡ pb (mod W) each: 5700 instances, G integral, U, V > 0, UV identity, and
e ≤ 4q²a whenever the size hypothesis holds (14 instances — it rarely holds since |p| ~ W): 0 failures.
Positivity U, V > 0 uses q ≠ 0 resp. p ≠ 0 or z ≠ 0 (u = −p/q with q ≥ 1 is clearly intended) — m2.

### Assessment 4.2 — SOUND as Assessment
Spot-checked the quoted engine values: `data/se/P_q4.txt` rows 155 (2^{38.75}: 931), 244 (2^{61}: 538 ≈ "550"), 364 (2^{91}: 98),
`P_q1_hi` row 600 (7.1·10⁻¹¹) ✓. The conclusion "box-sum certificates cannot reach r = 17" is an Assessment and is labelled so.

### Lemma 1.1 (ℓ²-Minkowski form of (Cop)) — SOUND
Re-derived: the lattice of vectors (g_l X^l)_{l<w} is full rank (triangular basis, diagonal n₁^{m−i}X^i, X^{m+j}), det
Δ = n₁^{m(m+1)/2}X^{w(w−1)/2}; the closed ball of radius ρ = 2(Γ(w/2+1)Δ)^{1/w}/√π has volume exactly 2^wΔ, so Minkowski
(compact convex symmetric body, vol ≥ 2^w det) gives g ≠ 0 with ‖v‖₂ ≤ ρ; for |y| ≤ X, |g(y)| ≤ Σ|g_l|X^l = ‖v‖₁ ≤ √w‖v‖₂
≤ μ_wΔ^{1/w}, μ_w = 2√w Γ(w/2+1)^{1/w}/√π. With n₁ ≤ n this is (Cop₂) ✓. Constants recomputed (mpmath, 30 digits):
μ₁ = 1, μ₂ = 1.59577, μ₁₀ = 5.75935, μ₂₄ = 12.7128 ✓; μ_w/w = 0.80, 0.58, 0.53 (w = 2, 10, 24) → √(2/(πe)) ≈ 0.48, so μ_w < w
for w ≥ 2 ✓. `zl_box.c` (diff against `se_box.c`: only the w·ln w term of lhs0 changes, LMK[w] = ½ln w + ln 2 + lgamma(w/2+1)/w
− ½ln π, padded up by 10⁻¹²·(1 + |v|), capped at ln w) implements exactly (Cop₂) with the same safety margins ✓.
*Optional improvement (not a defect):* since the quantity actually needed is ‖v‖₁, Minkowski on the cross-polytope
{‖v‖₁ ≤ ρ} (volume (2ρ)^w/w!) gives directly ‖v‖₁ ≤ (w!)^{1/w}Δ^{1/w}, i.e. (Cop₁) with w! in place of μ_w^w:
(w!)^{1/w} = 1.414, 4.529, 9.803 for w = 2, 10, 24 — another ≈ 20–23 % below μ_w, equally elementary.
Minor: `zl_box.c` header and `zl_r0.py` comment call it "Lemma 2.1" (the document's Lemma 1.1) — m3.

### Lemma 1.2 (value-selected tail routes) — SOUND
The validity of every per-box term list is SE §3.3's (reviewed by R222/R223; the term lists and the cop() logic are
unchanged — diff of `zl_tail.py` vs `se_tail.py` touches only the route choice). Any valid route may be chosen per box ✓.
Monotonicity: for a term c N^e (ln N)^p with e < h, d/dL[(e − h)L + p ln L] = (e − h) + p/L ≤ 0 for all L ≥ L₀ iff p ≤ (h − e)L₀ ✓
(and p ≥ 0 always). If no admissible route exists, `pick` falls back to SE's rule and the combiner's own check
(`wP < 0.5`, all aggregated terms e < h, p ≤ (h − e)L₀ after rounding e up) fails closed ✓.
Reproduced (`SE_W=40 zl_tail.py P 32 L`, author's code, reproduction only): G = 7.260 (2^600), **1.3618·10⁻² (2^800)**,
max exponent 0.4960 resp. 0.4797; SE's rule at 2^600 gives 873.57 ✓ (the "873 → 0.0136" claim). Note: SE's rule at
L₀ = 800 crashes with an OverflowError in `val` (exp(e·L₀) with e > 1.28 for some candidate route) — harmless (fail-closed),
but it means the document's comparison is 600-vs-800 with different rules, not like for like (m4).
How much the tail matters: at b = 30.16 the first tail K is 27 and each tail term is ≈ 2G·r^{−1/2} ≈ 8·10⁻⁷; the certificate
margin (≈ 0.0022) would tolerate G up to roughly 3, so the 2^800 tail is not delicate.
