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

### Combiner `zl_r0.py` and the 1/32-octave r-cells — SOUND
Read line by line (diff vs SE's reviewed `se_r0.py`: new tables, tail module, step 1/32 below Bfine). Checks:
* Uniformity inside an r-cell [2^b, 2^{b+1/32}): every table row bounds D on its whole N-cell (se_box uses N0 = DN(2^{j/q}),
  N1 = UP(2^{(j+1)/q}) and every route bound is monotone in the right direction: lower bounds from N0, upper from N1 —
  re-derived for each route, see the engine section below); N = r^K ranges over [2^{Kb}, 2^{K(b+1/32)}), covered by
  `table_max` cell by cell (finest table first, fallback to coarser cells that *contain* x, fail-closed on a gap); weights
  2r^{−k}, 2r^{−(K+1)/2} are maximal and the limit (r − 1)/(2r) minimal at r = 2^b ✓. No monotonicity in r of the table values
  is needed (and none holds: e.g. P_q32 row 978 > row 979).
* All cell endpoints K·b, (j + 1)/q are dyadic rationals, exact in binary, so `floor(x·q + 1e-12)` never selects a cell
  starting above x ✓. Table values padded ×(1 + 10⁻⁹), S ×(1 + 10⁻⁶) + 10⁻²⁰ ✓. Tail used at the top of the N-range with all
  aggregated exponents rounded up and capped at ≥ 0 (terms nondecreasing in N) ✓; for r ≥ 2^800 every term is in the tail and
  decreasing in r (p ≤ (½ − e)·ln N₀ ≤ (½ − e)K ln r) ✓. Series cut-off as in SE (R223 m-A1) ✓. Exit 1 on any failure ✓.
* Reproduced (author's code): plain 30.34375 → 0.494249, l2 30.15625 → 0.497826, both exit 0; plain 30.3125 → FAIL 0.500749;
  l2 30.125 → FAIL 0.504155 ✓ (the "fails below" statements).
Independent combiner `scripts/review_r232_combine.py` (mpmath, own table-cover logic, own admissibility check of every tail
term, own series remainder rule): results in the Thm 2.1 section.

### Thm 2.1 — SOUND (independently re-certified, both variants)
**Independent level-1 tables.** `scripts/review_r232_box.py` is a from-scratch Python re-implementation of the box sums
(Q: routes AD, fa, AC, CD, Ea, Ed, τ₃, fac, fca, fda + (c, d)-row aggregation; P: H, A, C, D, E, F, G, τ₃, I, J + (a, d)-row
aggregation), every route re-derived by me (derivations in the next section), in **exact rational arithmetic**: integer
cell enclosures N0 = ⌊2^{j/32}⌋, N1 = ⌊2^{(j+1)/32}⌋ + 1; integer box windows [X, 2X − 1] (slightly tighter than se_box's
λX); Coppersmith (m, w, J) proposed in floating point but **every accepted J(w − 1) verified by an exact Fraction comparison**
of w^w·n^{m(m+1)/2}·X^{w(w−1)/2} < D₀^{mw} (ℓ² variant: a rational upper bound for μ_w^w = (2√(w/π))^wΓ(w/2 + 1)); Σ1/a and
τ₂, τ₃ envelopes in mpmath (40 digits) padded up 10⁻²⁵ relative. Validated per box and per row against exact enumeration
(`scripts/review_r232_box_validate.py`) at N = 17³, 3¹¹, 17⁵, 10⁶ + 3, 999983, 2·10⁶ + 3, both modes: 0 violations
(D_P = 32, 121 and D_Q = 73, 245 at 17³, 17⁵ reproduced).
Tables `data/review_r232/{P,Q}_q32_cube.txt` (j = 965..1087, all r-cells 2^{30.15625}..2^{34}) and `{P,Q}_q32_l2.txt`
(j = 965..1023). **Every one of my 364 cell bounds is below the author's** (mine/theirs: Q 0.940–0.954, P 0.818–0.898, both
variants) — no cell of the author's tables is undercut by an independent valid bound, and the ratio is stable (no outlier).
**Independent combination.** With my level-1 tables (b < 34) and SE's reviewed tables for every other term:
| variant | B0 | tail | max S | at b | Q₁ | P₁ | P₃ |
|---|---|---|---|---|---|---|---|
| se_box-only (cube) | 30.34375 | author's zl_tail (2^800) | 0.465750 | 30.34375 | 0.42976 | 0.03066 | 0.00526 |
| se_box-only (cube) | 30.34375 | **SE's reviewed se_tail (2^600, G = 873)** | 0.486841 | 30.34375 | 〃 | 〃 | 〃 |
| ℓ² (Lemma 1.1) | 30.15625 | author's zl_tail | 0.469732 | 30.15625 | 0.43214 | 0.03201 | 0.00548 |
| ℓ² (Lemma 1.1) | 30.15625 | SE's se_tail | 0.495274 | 30.15625 | — | — | — |
| cube (control) | 30.15625 | zl_tail | FAIL 0.502062 | 30.15625 | 0.46261 | 0.03387 | 0.00548 |
All runs pass for every r-cell up to 2^800 except the control (cube tables do *not* reach 2^{30.15625}, as the author says).
The author's terms at b = 30.34375 (their code): Q₁ 0.45431, P₁ 0.03460, P₃ 0.00526, P₅ 7·10⁻⁵ → 0.49425 ✓.
So both statements of Thm 2.1 are independently confirmed; moreover, with my (≈ 5 % tighter) level-1 tables the se_box-only
bound r ≥ 2^{30.34375} holds even with SE's original, already-reviewed tail, i.e. without Lemma 1.2. (The SE-tail contribution
is not monotone in b: it peaks when the first tail K lands just above 2^600 — K = 19 at b = 31.5625..31.59375 contributes
0.037–0.038 with 1/32 r-cells, vs 0.018 (K = 21) at b = 30.34375 — which is why the scan over all b matters; mine covers all b.)
Not re-checked independently: `P_q1_hi.txt` rows 600..799 (se_box with box ratio 2^{9..12} at N ~ 2^{600..800}; my engine has
λ = 2 only, infeasible there). They are used only for K·b ∈ [600, 800) in the zl-tail runs; the se-tail runs do not use them.
