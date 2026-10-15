# R232 — hostile review #2 of STERILE_LOWER.md (O228), round 1 (no edits to the author's files)

Reviewer branch: side-agent/review-sterile-lower (merged side-agent/sterile-lower at start).
Scope: Thm 2.1, Lemmas 1.1, 1.2, the 1/32-octave combiner zl_r0.py, Lemma 3.1, Comp 4.1, Lemma 4.3, labels.
From-scratch scripts: scripts/review_r232_*.py.

## Summary verdicts
**No FATAL, no MAJOR defect.** 7 MINOR (wording/attribution/provenance).
| claim | verdict |
|---|---|
| Thm 2.1, se_box-only variant (r ≥ 2^{30.34375}) | **SOUND** — independently re-certified: own exact-arithmetic level-1 tables + own combiner give max S = 0.4658 (author's tail) / 0.4868 (SE's original reviewed tail) |
| Thm 2.1, ℓ² variant (r ≥ 2^{30.15625}) | **SOUND** — independently re-certified: max S = 0.4697 / 0.4953; control (cube tables at 2^{30.15625}) fails as the author says |
| Lemma 1.1 (ℓ²-Minkowski (Cop₂)) | SOUND (optional: ℓ¹ cross-polytope gives (w!)^{1/w}, ≈ 20 % better still) |
| Lemma 1.2 (value-selected tails; 873 → 0.0136) | SOUND (m4: comparison mixes rule and N₀) |
| 1/32-octave r-cells, combiner `zl_r0.py` | SOUND (fails closed; rounding directions correct; uniformity per cell correct) |
| Lemma 3.1 (joint parametrisation) | SOUND (m1: tautological "a ≤ b ⇔ b ≥ a" in (ii)) |
| Comp 4.1 (level-1 survivors) | SOUND — reproduced for all 2261 primes 3 ≤ r < 20000 by independent code |
| Lemma 4.3 (U–V) | SOUND (m2: q ≥ 1 implicit) |
| Assessments 3.0, 4.2, §3 cost model, r = 17 "undecided" | appropriately labelled |

## Defects
* **m1 (MINOR) — Lemma 3.1(ii), "a ≤ b ⇔ b ≥ a".** Tautological. Repair: "a ≤ b ⇔ na + c ≥ af ⇔ c ≥ a(f − n) (automatic if
  f ≤ n)", mirroring (i)'s explicit condition.
* **m2 (MINOR) — Lemma 4.3 hypotheses.** U, V > 0 (and hence U ≥ 1 in the size claim) need q ≥ 1 (u = −p/q in lowest terms,
  q > 0). Repair: add "q ≥ 1" to the hypotheses. Also optional: G ∈ ℤ follows directly from Gab ∈ ℤ, Ge ∈ ℤ and gcd(e, ab) = 1
  (r ∤ ab), so the M17D citation can be replaced by one line.
* **m3 (MINOR) — numbering.** `zl_box.c` header/comment and `zl_r0.py` comment say "Lemma 2.1 of STERILE_LOWER" for what the
  document calls Lemma 1.1. Repair: fix the comments.
* **m4 (MINOR) — Lemma 1.2 / (I4) / §2 "the P tail of SE is gone".** "873 → 0.0136" compares SE's rule at N₀ = 2^600 with the
  new rule at N₀ = 2^800; like-for-like the rule alone gives 873.6 → 7.26 at 2^600, and SE's rule cannot be evaluated at 2^800 by
  the code (OverflowError in `val`). Repair: state both effects separately. Optional: record that with SE's *original* tail
  the se_box-only certificate still needs the author's Lemma 1.2 (with the author's level-1 tables S ≈ 0.494 + 0.021 > 0.5 at
  b = 30.34375) — whereas with R232's tighter level-1 tables it does not.
* **m5 (MINOR) — Thm 2.1 attribution.** "relative to exactly the inputs of SE Thm 3.4" — the certificate also uses the new
  Lemma 1.2 (both variants) and Lemma 1.1 (ℓ² variant). Repair: "relative to the inputs of SE Thm 3.4 plus Lemma 1.2 (and
  Lemma 1.1 for 2^{30.15625})".
* **m6 (MINOR) — provenance.** `zl_box` prints the header "# se_box …", so `P_q32_l2.txt`/`Q_q32_l2.txt` are not
  self-identifying (only MANIFEST says they are zl_box output). I regenerated Q_q32_l2 row 971 with zl_box (exact match), so
  the data are right. Repair: make zl_box print "# zl_box".
* **m7 (MINOR) — P_q1_hi provenance.** MANIFEST: "se_box P 600 999 … (stopped after j=841)" — an interrupted run; rows 600..841
  are complete and only ≤ 799 are used, but the document should say the run was truncated deliberately, and note that these rows
  (box ratio 2^{9..13}) have not been independently re-checked (R232 could not, λ = 2 only; they are unused in the SE-tail
  re-certification above, so Thm 2.1 *as re-certified by R232* does not depend on them).

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
17328 P + 25674 Q data (the author's totals), X = 3000: 74908 P + 110668 Q data — 0 mismatching n in all three
(`data/review_r232/joint_3000.txt`).
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
Spot reproduction of the author's tables with the author's engines (compiled afresh, gcc -O2; hashes of se_box.c, zl_box.c,
zl_tail.py, zl_r0.py, se_r0.py match `data/zl/MANIFEST.txt`): `zl_box Q 971` = Q_q32_l2 row 971 and `se_box P 971` =
P_q32 row 971, digit for digit.

### Route derivations used by my engine (re-derived, each validated by the exact per-box test above)
Q-datum: 4abcd = F(a + b) + c, a ≤ b, e = (a + b)/c; identities ef = 4a²d + 1, 4abd = eF + 1, fb = aF + c,
f(4bcd − F) = F² + 4c²d (expand), and f = (aF + c)/b ≤ F + 2. Box (c, d, f) ∈ [C, 2C) × [D, 2D) × [P, 2P): a = (f + F)/(4cd)
∈ [⌈(P + F₀)/(4(2C−1)(2D−1))⌉, ⌊(2P − 1 + F₁)/(4CD)⌋]. (AD) ≤ 2 per (a, d): f ≡ −F and e ≡ f⁻¹ (mod s = 4ad) have fixed
classes and ef = as + 1 < s², so f < s or e < s, each case ≤ 1. (fa) d ≡ −(4a²)⁻¹ (mod f). (AC) f | aF + c, f ≡ −F (4ac).
(CD) f | F² + 4c²d, f ≡ −F (4cd). (Ea) 4a | eF + 1, then b | (eF + 1)/(4a), b ≡ −a (mod e) [or d ≡ −(4a²)⁻¹ (mod e)].
(Ed) 4d | eF + 1, a² ≡ −(4d)⁻¹ (mod e), ≤ 2^{ω(e)} classes (e odd). (τ₃) e in one class mod 4, then abd = (eF + 1)/4.
(fac) 4a | f + F, then c ≡ −aF or d ≡ −(4a²)⁻¹ (mod f). (fca) 4c | f + F, a ≡ −cF⁻¹ (mod f) (gcd(f, F) = 1 as r ∤ c).
(fda) 4d | f + F, a² ≡ −(4d)⁻¹ (mod f). Row: per (c, d) the data are divisors f of F² + 4c²d. All classes are units.
P-datum: N/(4ad) < b ≤ N/(2ad), N/(4acd) < e ≤ N/(acd), 2a²d ≤ N, acd ≤ N (from f ≤ ef ≤ 3N); routes as in SE Table 2;
J: given (c, e, d), {a, b} are the roots of t² − ce·t + (N + e)/(4d), so ≤ 2 (se_box's extra 2^{ω} factor in J is unneeded).
Lemma 1.3/Cor 1.4 is used with the smallest admissible modulus and the largest integer factored (both monotone) ✓.

## Labels
All labels are appropriate: Thm 2.1 PROVED (computer-assisted) — now independently re-certified; Lemmas 1.1, 1.2, 3.1, 4.3
PROVED (elementary, re-derived); Comp 4.1 CERTIFIED (independently reproduced for all primes < 20000); §3 cost model, 3.0,
4.2 Assessment; "ES not solved" disclaimer present; r = 17 outcome "undecided" — correct, nothing proved about r = 17 beyond
Comp 4.1 and Lemma 4.3. Spot value for "true count of a few hundred": D_Q(10000019) = 486 (r ∤ e), D_P(10000019) = 170 (my
enumerator), so at 2^30 "a few hundred to ~10³" — fine as Assessment.

---------------------------------------------------------------------------------------------------------------------------
# Round 2 (checkpoint 2: §6 joint sweep, Thm 6.3 r₀ = 2^{21.4375}; §7 r = 17) — still no edits to the author's files

Merged side-agent/sterile-lower again. New scripts of mine: `scripts/review_r232_l1count.c`, `review_r232_cells.py`,
`review_r232_combine2.py` (+ an `R232_ACUT` option in `review_r232_box.py`); data `data/review_r232/r2/`.

### R2.1 §6.1 decomposition — SOUND
D_P(r) + D_Q(r) ≤ JP + JQ_{A,Y} + 2#{ad ≤ Y} + B_A: P-data all swept; Q-data split into a ≥ A (box bound), a < A & ad ≤ Y
(≤ 2 per (a, d) — re-derived in round 1: f and e = f⁻¹ have fixed classes mod s = 4ad and ef = 4a²d + 1 < s²), a < A & ad > Y
(swept) ✓. Ranges: f = (aF + c)/b ≤ F + c/b ≤ F + 2 (c ≤ a + b ≤ 2b), 4acd = F + f ≤ 2F + 2 ⇒ a ≤ acd ≤ (F + 1)/2, d ≤ (2X₁+2)/(4a)
✓ (so "all rows" ⇒ B_A = 0 ✓). The level-1 weights 2r⁻¹ (k = 1 and K = 1) combine into 2(D_P + D_Q)/r ≤ 2(…)/2^{j/32} ✓.
`zl_boxa.c` (diff vs zl_box.c: one line skipping Q-boxes with a₁ < ACUT; the (c, d)-row τ-aggregate stays a valid bound for the
subset) ✓. Spot-checked with my engine restricted to a ≥ A (`R232_ACUT`, which even clips a₀ to A): cell 940, A = 40000:
mine 7.533·10⁷ vs Qa_40000 8.463·10⁷; cell 800, A = 262144: 3.330·10⁶ vs 3.484·10⁶ — both below the author's ✓.

### R2.2 Independent exact level-1 counts — SOUND (64/64 cells identical)
`review_r232_l1count.c` uses parametrisations *different from the joint sweep*:
* P: loop (a, b) with b ≤ X₁/(4a − 2), c over the divisors of a + b (smallest-prime-factor table), e = (a + b)/c, then the
  progression r = 4abd − e in d [author: (a, c, d) and r ≡ −4a²d (mod 4acd − 1)];
* Q, a < A: divisor pairs {g, m/g} of m = 4a²d + 1 found without factoring — for each g ≤ √m_max, gcd(g, 2a) = 1, d runs over
  d ≡ −(4a²)⁻¹ (mod g) with g² ≤ m, both orientations (e, f); Q, a ≥ A: for each d ≤ (2X₁+2)/(4A) the quadratic polynomial
  4d·a² + 1 is sieved *in a* (two Tonelli–Shanks roots of a² ≡ −(4d)⁻¹ per prime p ≤ √m_max, leftover cofactor prime)
  [author: sieve/ρ-factoring of 4a²d + 1 in d for fixed a]; then r = 4acd − f in c, b = ce − a ≥ a;
* every datum checked against its defining equation in 128-bit arithmetic; cell membership exact (2^j ≤ r^{32} < 2^{j+1}).
Validation: vs my round-1 Python enumerator for all primes in [1000, 2000), [100000, 103000) (A = 5, i.e. mostly via the
polynomial sieve) and [100000, 101000) (A = 7): 0 mismatches; the two Q methods agree on all 2204 primes in [10⁶, 1.03·10⁶)
(A = 5 vs A = 20000). Runs: octave 21 = [2^21, 2^22) (A = 2048, 26 s), octave 22 (A = 2896, 60 s); ALL Q-data counted (no Y),
plus separately the Q-data with ad ≤ Y to compare with the author's split.
**Result: for all 32 + 32 cells j = 672..735, (max_r JP, max_r JQ_{ad>Y}, max_r (JP + JQ_{ad>Y}), #primes) agree exactly with
`data/zl/sweep_21.txt` (Y = 300) and `sweep_22.txt` (Y = 1048)** (`data/review_r232/r2/cells_oct2{1,2}.txt`). The author's
level-1 bound ms + 2#{ad ≤ Y} (e.g. 7694 + 3534 at j = 686) is ≥ my exact max_r(D_P + D_Q) over *all* data (8509) ✓.
Remark (correcting my round-1 comment, as the author did): in octave 21 the *median* of D_P + D_Q is 536 but the max is
17458 (r = 3991679, r + 1 = 2⁷·3⁴·5·7·11); my round-1 "a few hundred is fine" was about typical r and was wrong for the
worst primes; the author's §6 correction is right.

### R2.3 Deeper terms — the K = 3 tables re-computed; the 2^800 tail cross-checked independently
* **K = 3 (the binding deeper term, 0.31–0.44 in these octaves).** My exact-arithmetic engine (`review_r232_box.py P 32 j`,
  the same code that was validated per box against exact counts in round 1): ℓ² cells j = 2058..2111 (N ∈ [2^{64.31}, 2^{66}),
  used by octave 21) and cube cells j = 2112..2207 (N ∈ [2^{66}, 2^{69}), octave 22): `data/review_r232/r2/P_q32_k3_{l2,cube}.txt`.
  mine/theirs = 0.842–0.957 (ℓ², vs P_q32_k3_l2) and 0.858–0.963 (cube, vs P_q32_k3): every cell below the author's.
* **K ≥ 5, k ≥ 3:** I use only SE's reviewed tables (`data/se/P_q4, P_q1, Q_q4`), *not* the author's new P_q32_k5_l2 — so that
  table is not needed (it costs me P₅ ≈ 0.037 instead of the author's 0.033 at j = 686).
* **Tail.** With SE's original tail (N₀ = 2^600, SE's rule, G = 873) both octaves FAIL badly (max S = 1.40 resp. 1.69): Thm 6.3
  genuinely rests on Lemma 1.2 (value-selected tail at 2^800) and on `P_q1_hi` rows 600..799. Both checked:
  (a) `scripts/review_r232_tail800.py` runs **R223's independent exact-exponent tail code** (`review_se2_tail.py`, not the
  author's) with L₀ = 800 and the value rule substituted by source transformation: 4913 boxes, 12973 terms, max exponent
  0.47969, every term admissible, **G(2^800) = 1.361841·10⁻²** (author's zl_tail: 1.361842·10⁻²) — Lemma 1.2's number is
  reproduced by an implementation independent of the author; its term list is used as the tail in my combiner (TAIL=r223).
  (b) `P_q1_hi` rows 600, 700, 799 regenerated with SE's reviewed se_box: identical. Numerically these rows are irrelevant here
  (bound/√N ≈ 10⁻¹³, i.e. terms ≈ 10⁻¹⁶ in S); what matters is only that the SE tail is *not* used below 2^800.

### R2.4 End-to-end re-certification of two octaves — SOUND
`scripts/review_r232_combine2.py` (from scratch; mpmath; exact cell membership; level 1 = my exact max_r(D_P + D_Q) over **all**
level-1 data, no A/Y split; K = 3 = my tables; everything else SE's reviewed tables; tail: R223-code value-selected list at
2^800 (P) + SE's se_tail (Q, 2^100); series remainder bounded by tρ/(1 − ρ) with ρ the explicit ratio bound of the tail terms):
| octave | cells | max S (R232) | at | author's max S | terms at the worst cell (R232) |
|---|---|---|---|---|---|
| **[2^{21.4375}, 2^{22})** (ℓ² K = 3) | j = 686..703, all ok | **0.455444** | j = 686 | 0.483248 (j = 686) | L1 0.00599, P₃ 0.41013, P₅ 0.03719, Q₃ 4·10⁻⁵ |
| [2^{22}, 2^{23}) (cube K = 3) | j = 704..735, all ok | **0.380115** | j = 704 | 0.417317 | L1 0.00560, P₃ 0.34788, P₅ 0.02538 |
(limit (r − 1)/(2r) ≥ 0.4999998.) The same with the author's zl_tail instead of the R223-code tail: identical maxima.
So the two octaves, including the lowest one, are independently certified end to end.

### R2.5 Does the per-octave claim give Thm 6.3? — SOUND (minor m9, m10)
(The criterion is S < (r − 1)/(2r) ≈ ½ per cell, not "< 1".) From the author's logs `r1_22..29.txt` and `r1_21_l2.txt`:
cells j = 686..964 are 279 contiguous cells, every one "ok", max S = 0.483248 (j = 686); j = 965 = 32·30.15625 is where Thm 2.1
starts. Every prime r ≥ 2^{21.4375} lies in exactly one cell (cell membership exact; for octaves 21, 22 my exact membership gives
the same #primes per cell). zl_r1.py rule: L1 = 2(ms + 2#{ad ≤ Y} + B_A)/2^{j/32} ✓ (ADY = 3534 at Y = 300 and 14900 at Y = 1048
recomputed); partial cells skipped, counter saturation ⇒ FAIL, missing engine row ⇒ exit ✓. Deeper terms: identical code path to
zl_r0 (reviewed in round 1) plus the k3/k5 tables ✓.
m9: `r1_21_l2.txt` (the octave-21 certificate) ends "failures 13" and exits 1, because it also processes j = 672..685, which fail;
Thm 6.3 uses only j ≥ 686. Fail-closed hygiene: add a jmin argument (or a run restricted to j ≥ 686) so that the certificate
of record exits 0.
m10: the series cut-off (term < 10⁻³⁰ ⇒ add 10⁻²⁰) was justified by R223 m-A1 only for b ≥ 32 (ratio < ½). At b ≈ 21.4 the
ratio of successive tail terms is ≈ 2^{2(b+1/32)·0.4797 − b}·((K+2)/K)^p ≈ 0.56–0.64 — still < 1, so the remainder is
≤ 2·10⁻³⁰, fine; but say so (my combiner uses the explicit tρ/(1 − ρ)).

### R2.6 What the octaves 23–29 rest on (not re-run end to end)
Octaves 23–29 were not re-certified end to end by me. Their new ingredients are the sweep (whose output I matched exactly in
octaves 21–22, same binary family), the zl_boxa B_A tables (two cells spot-checked above, mine below theirs) and SE tables.
The worst of them is octave 27 (max S 0.4732, margin 0.027).

### R2.7 §7 (r = 17, conic Γ_{c,d,z}) — labels SOUND, one wording MINOR (m11)
Re-derived: since 4abcd − (a + b) = c(4abd − e) = cN, Γ is cX² = rz²·cN, i.e. X² = rz²N with X = qa − pb — the covering
condition qa − pb = zW with W² = rN, W = r^L ✓. Given integrality, v_r(N) = 2v_r(X) − 1 − 2v_r(z) is odd, so r | N and
N = r·w², w = X/(rz) ✓ ("levels = points with w a power of r"). Vieta in a: a·a′ = (cp²b² + rz²b)/(cq²) = bV·a/(cq²), so
a′ = bV/(cq²) = 78·9591/81 = 748098/81 ✓, b′ = aU/(cp²) = 3/121 ✓. For (1, 78, 1, 16) the quadratic form has discriminant
16rc²dz²(pq + rdz²) > 0 (pq + rdz² = −99 + 2448), so Γ is a hyperbola; the S-unit/binary-recurrence remark is a correctly
labelled Assessment. The equivalence is labelled "PROVED, elementary" with integrality of e, N and r ∤ ab stated as extra
conditions ✓; outcome "undecided" ✓.
m11: (iii) "U = Ga − cp² is the value of a linear form at a point of Γ" — G = ((p + q)² + 4rdz²)c/(a + b) depends on the point,
and U = (cq²a + rz²)/b; U is a ratio of linear forms (a linear form only after fixing e). Repair: say "U = (cq²a + rz²)/b".

### Round 2 verdicts
| claim | verdict |
|---|---|
| §6.1 split of the level-1 count | SOUND |
| §6.2 sweep counts (octaves 21, 22) | SOUND — 64/64 cells identical to an independent method |
| Thm 6.3, octave [2^{21.4375}, 2^{22}) | **SOUND, independently re-certified** (max S 0.4554) |
| Thm 6.3, octave [2^{22}, 2^{23}) | **SOUND, independently re-certified** (max S 0.3801) |
| Thm 6.3 as a whole (cells 686..964 + Thm 2.1) | SOUND from the author's logs; octaves 23–29 not re-run (R2.6) |
| Lemma 1.2's G(2^800) = 0.0136 | confirmed by R223's independent code with the value rule |
| §7 labels | SOUND (m11 wording) |
New defects round 2: m9, m10, m11 (all MINOR). No FATAL / MAJOR. The round-1 minors m1–m7 still apply to §§1–4.
Attribution note for Thm 6.3 (extends m5): the inputs include Lemma 1.2 and the P_q1_hi rows in an essential way (with SE's
2^600 tail octaves 21–22 fail with S ≈ 1.4–1.7); "inputs as Thm 2.1" covers this formally, but it is worth stating.
