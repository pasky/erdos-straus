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
