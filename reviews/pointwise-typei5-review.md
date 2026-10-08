# Hostile review R92 of POINTWISE_TYPEI5.md (task O92)

Reviewer: side agent R92 (branch `side-agent/review-typei5`). Reviewed: `side-agent/lfl-sign-point` up to `853e4de`
(incl. Lemma 3.6 case A, Theorem 3.7). From-scratch scripts: `scripts/review_typei5_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (Lehmer minimality) | SOUND (MINOR wording: L1, L2) |
| Cor 1.2 (`k ∈ {1,2,4}`; engine complete) | SOUND, can be sharpened to `k ∈ {1,2}` (L3) |
| (filled in below) | |

## Lemma 1.1 — SOUND

Re-derived line by line.
* (a) The ratio `η/η'` has norm 1 and the shape `A + 4B√d` ✓; `α·G` has the shape ✓; positive solutions ↔ elements `> 1`
  of `αG` (with the conjugation `√Q ↦ −√Q`, `η^{-1} = 4X√P − u√Q`) ✓; `u√Q = (η−η^{-1})/2` increasing ✓.
  `m ≥ 3` ⇒ `αν_0^{-1} ∈ (1,α)` ✓. `m = 1` ⇒ positive solutions `α^n`, `n` odd ✓.
  `m = 2`: `α, α^{-1} ∈ ℚ(√d)` ⇒ `√P ∈ ℚ(√d)` ⇒ `P` or `Q` is a perfect square. `P = p²` ⇒ all `u = 4Bp` even ✓.
  `Q = q²` is excluded since `u` odd forces `Q ≡ −u^{-2} ≡ 7, 15 (mod 16)` — not by "`Q ≠ 1/k²`" (see L2).
* (b) integrality, (c) `L_n ≡ n (mod 7)`, (d) `L_7 = 7s⁶+35s⁴r²+21s²r⁴+r⁶ ≡ 7 (mod 49)`, (e) `L_{mn}(α) = L_n(α)L_m(α^n)`,
  `L_m ≥ m s^{m−1} > 1`, (f) the descent `n = 7^r n'` — all ✓. (f) uses `L_{7^r}(α^{n'})` integral, true by (b) applied to
  the solution `α^{n'}`.
* From scratch (`scripts/review_typei5_lehmer.py`):
  (1) all solutions with `u ≤ 2·10⁴` for `P ≤ 40`, `7 | Q ≤ 280` (15 solvable systems, 6 with ≥ 2 solutions in range):
  the solution set is exactly `{α^n}` (exact powering), `u_n/u_1 ≡ n (mod 7)`, 7-power `u` only at `n = 1`.
  (3) 1148 systems **constructed** to contain a solution with `u = 7^b` (`b ≤ 3`, `X ≤ 60`, `Q ≤ 2·10⁴`): the brute-force
  search over all smaller `u' < 7^b` finds no solution in any of them, so the 7-power solution is minimal, as claimed.

Defects:
* **L1 (MINOR)**, Lemma 1.1(a): "`G` … is infinite cyclic". `G = {A+4B√d : A²−16dB²=1}` contains `−1`, so it is `{±1} × ℤ`.
  Repair: write `G_+ := G ∩ (0,∞)` (infinite cyclic, generator `ν_0`). Only positive elements are used afterwards.
* **L2 (MINOR)**, Lemma 1.1(a), `m = 2`: "`√P = p ∈ ℤ` (`√P ∈ ℚ(√d)`, `Q ≠ 1/k²`)" is garbled. Correct statement: `√P ∈ ℚ(√d)`
  means `P` is a square or `Q` is a square. `Q` square is impossible when some `u` is odd (`Qu² ≡ −1 (mod 16)` gives
  `Q ≡ 7,15 (mod 16)`). Repair: replace with this sentence.

## Corollary 1.2 — SOUND (sharpening L3)

* Hypotheses ✓: `v_7(d) = a` odd ⇒ `d` is not a square; `u = 7^b` odd; `7 | Q`. The step from Lemma 1.1 to "`α² = ν_0`" is
  `m = 1` ✓.
* **L3 (MINOR, sharpening)**: `k ∈ {1,2}`, not just `{1,2,4}`. For odd `d`, a norm-±1 unit `x + y√d` has `x + y` odd, so `xy`
  is even and `ε² = (x²+dy²) + 2xy√d` has `4 | 2xy`. So `(ℤ[√d]/4)^×/(ℤ/4)^×` (order 4) has exponent 2. From scratch:
  over all 1473 odd non-square `d ≤ 3000`, `k = 1` occurs 915 times, `k = 2` 558 times, and `k = 4` never. The author's claim is
  true but weaker than necessary; the engine completeness ("`mmax ≥ 4`") holds a fortiori (`mmax ≥ 2` suffices).
  `typei4_dgraded.py` uses `fund(d)` = least `x > 1` with `x² − dy² = 1` in `ℤ[√d]`, i.e. exactly `ε_f`, so the
  completeness transfer is valid.
* Comp 1.3 relies on the replay of `typei4_dgraded.py 5 24 3000 6`; see the §2 checks below (my own engine).
