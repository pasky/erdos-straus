# z36 — Effective Cantor dimension of the ES ladder rungs (O266 memo 6)

## Idea
Treat S_L(p) = {A : r(p/A) ≤ L} as a Moshchevitin–Shkredov Cantor set and measure its "w" against the method's
threshold 1 − w ≤ κ/8 (memo z36_density_threshold).

## Content (Assessment + EVIDENCE)
* Fixed L: |S_L(p)| ≈ c_L (log p)^{L−1}: dimension 0 as a subset of ℤ/p; at the gluing scale t the half set
  {A : odd-digit sum below scale t ≤ L} has measure ≈ (log t)^{O(L)}/t, i.e. effective w = 1/2 — exactly critical
  (DEDEKIND_ES §5.3, 2δ = 1).
* L = c log p: |S_L| = p^{θ(c)} (`z36_ladder.py`): θ(1/2) = 0.30, 0.47, 0.59, 0.60, 0.61 and θ(1) = 0.74, 0.75, 0.83,
  0.84, 0.85 at p ≈ 10², 10³, 10⁴, 10⁵, 10⁶. Effective w = (1 + θ)/2 ≈ 0.80 (c = 1/2), 0.93 (c = 1) — Zaremba-like with
  M ≈ 3 resp. M ≈ 8 (w₃ ≈ 0.705, w₅ ≈ 0.837; Hensley/Jenkinson values from memory). The method needs w ≥ 1 − κ/8 with
  κ ≥ 2^{−1656}: c astronomically large, and at that rung Theorem A (pigeonhole, c ≍ log log p) is already stronger.
* So on the ES ladder the growth method's operating window is empty: below it counting is impossible (polylog sets),
  above it counting already wins.

## Barrier screen
B3 in Cantor language. T1 unaffected (all rungs void at squares).

## Assessment
Assessment (EVIDENCE for θ). A clean way to state why the 2026 method cannot help ES: its window is
[w ≥ 1 − κ/8], and on the ES ladder that window lies above the rung where trivial counting already succeeds.
