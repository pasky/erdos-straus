# AGENT_REPORT_O139 — r = 17 sterile point: attacking the P-count

Branch `side-agent/r17-sterile`. Deliverable: `POINTWISE_MORDELL17D.md`; scripts `scripts/m17d_*`.

## Verdict
**No unconditional sterile point.** The outcome is a sharpened CONDITIONAL statement with an exact gap, a quantified
no-go for the cell-wide explicit route, and new PROVED pointwise structure for rational points with a CERTIFIED
pointwise extension of the exact range.

## Results (labels as in the file)
1. **Compactness (Lemma 1.1, PROVED).** A sterile point exists iff no finite level covers `C_5`; the measure criterion is
   only a sufficient tool.
2. **Quantified no-go for the cell-wide measure route (Comp. 1.2/1.3: exact arithmetic + Assessment).** C* grows only
   ×1.76 per K-step at θ = 0.4 (table to K₀ = 31). An explicit bound `D_P(K) ≤ A·17^{θK}(K ln 17)^B` closes Theorem 4.1 of
   M17B only with exact data through K₀ = 21 (A = 11, B = 0, θ = 0.4), 37 (A = 11, B = 1), 57 (A = 11, B = 2), and 85–165
   at θ = 0.45. ET-type covers give at best around (0.4, 1–2, ≥11). So the cell-wide route needs a P-count with no log loss and
   constant ≲ 2.5 at θ = 0.4 (from K = 15), which is stronger than ET's own (non-explicit) theorem. Angle (1) of the brief is closed in
   this quantitative sense. Averaging over K is M17C §4: it does not help.
3. **Rational points (§2, PROVED).** For `u = −p/q`, P/Q-box membership at level L is the lattice condition
   `qa − pb = zW` (Lemma 2.1). Covering data with `z ≠ 0` are unbalanced, `max(a,b) ≥ W/(|p|+q)` (Lemma 2.2). The
   resonant `z = 0` rays are excluded at **every level** for `u = −2/3`: by a mod-8 argument, `e` would be a power of 5
   and `≡ −1 (8)` (Lemma 2.3). `u = 5` has no rays. Remark 2.4 gives an exact descent identity
   `e | (p+q)² + 68dz²` (checked on 6632 instances).
4. **Pointwise engines (§3, CERTIFIED).** P at level L in `≈ (W/34) ln W` exact 128-bit tests (no factoring); Q at level k
   in `O(√F)` modular square roots. Both are validated against the certified complete lists at all levels ≤ 7:
   716 points, exact set equality, 0 mismatches.
   **Comp. 3.4:** `5` and `−2/3` lie in no box of any ET family of level ≤ 10 (P L = 10: 1.4–1.5·10¹² exact tests, ≈ 3.3 h
   per point), and in no Q-box of level ≤ 15. The cell-wide certified range is level 7.
5. **Sharpened conditional (Theorem 4.1, PROVED reduction).** A ball R of level L* that is free through L* contains a sterile
   point if `Σ_{ℓ>L*} 17^{L*−ℓ}NB^R(ℓ) < 1`. Under the fair-share hypothesis `(H_θ^R)` the admissible constant at θ = 0.4
   is 22.83 (L* = 9) or 40.24 (L* = 10), against 4.969 for the global criterion (box units), i.e. ×4.6 resp. ×8.1. Honest
   caveat: `(H^R)` adds an equidistribution requirement and is not implied by (H_P). Both are unproved; neither is
   provable with known tools.

## Not done / options for the parent
* Full cell-wide enumeration at K = 15 (estimated ≈ 15 h on 2 cores with `m17b_penum.py`). It would certify the K₀ = 17
  column of Comp. 1.2: C* 2.64 → 4.65 at θ = 0.4 in D-units. I did not start it, to leave the cores free.
* P pointwise at L = 11 would take ≈ 2 core-days per point.
* Conjecture 4.2 (`5`, `−2/3` sterile) is consistency evidence only: a random point survives levels > 10 with probability
  `1 − O(10⁻⁸)`.

## Self-check / risks for the reviewer
* Lemma 2.1(i): the box is `−f ≡ −a/b` at level L uses `bf = cN + a` and `2L−1 ≥ L`; 17 | b ⇒ 17 | a ⇒ box ≡ 1.
* Lemma 2.2(ii) bound `acd ≤ (F+1)/2` for a ≤ b (used for Q completeness); Q engine handles the reflected box via
  `w = −1/u`.
* P engine completeness: parts A/B split at `A ≈ W/√68`, with `B` derived from `(4a−1)(4b−1) ≤ 4N+1`. In-engine equation
  rechecks are mod 2^128 at L = 10 (products can exceed 2^128); `c`, `d`, `e` are derived exactly.

## Self-review (reviewer subagent) — repairs applied
* P-engine: `4acd−1` could exceed 2^128 on a genuine hit (L ≥ 9) → explicit abort, not a silent miss; fixed (reduce mod W).
  All Comp. 3.4 runs had ended normally; L = 8, 9 re-run with the fixed engine.
* `m17d_validate.py` now exits nonzero on mismatch; Q-level-7 sample raised to 20 (716 points).
* "constant ≲ 1.5" corrected to ≲ 2.5 (K = 13 already certified).
* Comp. 1.2/1.3: with base ρ₂ the C* values are ceilings and the K₀ values lower bounds (true base ≤ ρ₂); text fixed.
