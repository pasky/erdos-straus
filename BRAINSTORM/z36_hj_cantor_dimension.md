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
  κ ≥ 2^{−1656}: c = C₀ astronomically large. Even granting the χ-twist, the method would give λ(p) ≤ C₀ log p, which
  beats Theorem A (≈ 10 log p log log p) only for log log p ≳ C₀/10, and improves it by the log log factor only.
* So on the ES ladder the growth method's operating window is above the rung L ≍ log p: below it the sets are too thin
  (fixed L: polylog; this is where ES lives), and in it counting (Theorem A) already gets within a log log factor.

## Barrier screen
B3 in Cantor language. T1 unaffected (all rungs void at squares).

## Assessment
Assessment (EVIDENCE for θ). A clean way to state why the 2026 method cannot help ES: its window is
[w ≥ 1 − κ/8], which on the ES ladder lies at L ≥ C₀ log p, within a log log factor of what pigeonhole gives.
