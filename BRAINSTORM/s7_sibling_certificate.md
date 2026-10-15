# s7_sibling_certificate — can r = 17 sterility be certified by a finite positional computation? (O247, mandatory (iii))

## Idea
(J)72's windowed König lemma needs, at every depth beyond some N₀, that no alive parent has all 17 children boxed;
(J)77 Conjecture 4.2 asserts ≤ 3 boxes per alive parent from depth 4 on. Question: exact sweeps to depth ≤ 8 plus a
*provable* bound beyond — is there a finite certificate? Construction attempt: use the x-window (fixed e-slice)
description of boxes on the 17-generic line, where every datum is explicit, and look for (a) a self-similarity
that propagates "≤ 16 children" from finitely many depths to all, or (b) a per-parent bound that does not count.

**Lemma 1 (fixed windows on the r-generic line; PROVED, elementary).** At the r-generic point x(u) (x_ℓ = 1 for ℓ ≠ r,
x_r = u), K_m = (p + m)/4 ≡ 1/4 (mod m) and v_ℓ(K_m) = v_ℓ((1 + m)/4) for ℓ ≠ r. A fixed Type II window m (r ∤ m)
certifies x(u) at cap 0 iff some d = δ·r^c, δ | K₀² (K₀ the r-free part of (1 + m)/4), 0 ≤ c ≤ 2v_r(u + m), has
d ≡ −1/4 (mod m). With c_m the least such c, window m covers exactly the ball v_r(u + m) ≥ ⌈c_m/2⌉; the Type I e-slice
with the same number covers the mirror ball around −1/m with the same radius (N = (pe + 1)/4 has the same known part).
(R-O247 review fix: the first version called these M17's (U)/(U⁻¹) boxes and claimed (P) is invisible. Wrong: e.g. r = 17,
m = 11, K₀ = 3, c_m = 3 (d = 9·17³ ≡ 8 ≡ −1/4 mod 11) gives the level-2 ball u ≡ −11 (mod 289), which is the P-datum
(a, d, f) = (51, 17, 11); U has no even-level data (POINTWISE_MORDELL17 Lemma 5.2). The exact dictionary between fixed-window
balls and M17's box types is not established here; the ratio test of s7_rgeneric_windows.py (r-offsets [−1, 1]) is narrower
than the fixed-divisor test of s7_window_mass.py.)
**Lemma 2 (parity law; PROVED).** c_m is odd. *Proof.* Let χ = (·/m) (Jacobi, m ≡ 3 (4)). For ℓ | (1 + m)/4 odd,
(m/ℓ) = (−1/ℓ) and reciprocity give (ℓ/m) = 1; for ℓ = 2, 8 | 1 + m gives (2/m) = 1; so χ(δ) = 1. The cell condition
(−m/r) = −1 gives χ(r) = −1 (both r ≡ 1 and r ≡ 3 (4)). Then χ(−1/4) = −1 = χ(r)^c forces c odd. (c = 0 is
excluded independently by T1: it would certify the square point u = 1.) ∎
This is the exact ℤ-twin of (J)67's root-product parity law (the μ₂ shadow predicted in (J)67's Assessment).

## Literature
POINTWISE_MORDELL17 §1–3 (box types, exact levels ≤ 5–7), STERILE_LOWER Comp 4.1 / Assessment 4.2 (M17D tail wall),
STERILE_DIOPHANTINE Lemma 3.1 / Thm 2.1 / Prop 3.2, SIBLING Conj 4.2, FF_STERILE_PUSH; König's lemma.

## Barrier screen
* (J)72 Prop 3.2: per-depth counts cannot beat the union bound — a certificate must be positional at all large depths.
* Self-similarity: over F₃[T], Frobenius maps valid families at x_u to x_{u³} with level N ↦ 3N + 2 ((J)72 Prop 5.1).
  Iterating, u^{3^k} = 1 + cT^{3^k} agrees with the T1 point 1 to order 3^k while the level becomes 3^k(N + 1) − 1, whose
  ball (radius T^{3^k(N+1)}) contains 1 iff N = 0. So Frobenius pushes coverings toward the T1 point at *exactly the
  critical rate* (PROVED, one line): it excludes only level-0 families and gives no induction. ℤ has no analogue map.
* Fixed windows: enumerating windows by size is not complete for a given level — windows with small c can
  be as large as ≈ r^{2c} (D = 1 solutions 4βwt = r^c + 1, m = 4βw(β + t) − 1); a complete level-c list is the set of
  ES solutions of 4/r^c (M17 §2), i.e. exactly the M17D tail count. No new handle.

## Cheap numerics (scripts/s7_window_mass.py, s7_rgeneric_windows.py)
* r = 17, windows m ≤ 10⁷, c ≤ 16: all 955+ firing windows have odd c (Lemma 2), no T1 violation; per level b = ⌈c/2⌉:
  b = 1: m ∈ {3, 7, 23, 39} (cells 14, 10, 11, 12, mirrors in the same cells); b = 2: 44 windows (m ≤ 10⁶).
  union mass of the fixed-window balls and their mirrors inside the non-residue cells (ultrametric, maximal balls): 0.31857 (m ≤ 10⁶), 0.31888 (m ≤ 10⁷),
  of 8/17 = 0.4706. Lower bound only (the enumeration in m is incomplete, see above).
* Level 1, ratio test (s7_rgeneric_windows.py) only: survivors r = 13: {2, 5, 7, 8}, r = 17: {3, 5, 6, 7}, r = 19: {2, 3, 10, 13},
  r = 23: {5, 14}; STERILE_LOWER Comp 4.1 (all box types): none, {5, 7}, {2, 3, 10, 13}, {5, 14}. So at r ≥ 19 the
  fixed windows already account for every level-1 box; at r ≤ 17 the moving-slice (P/Q) classes matter.

## Assessment
PROVED (Lemmas 1–2 where c_m exists, Frobenius criticality) + EVIDENCE. Answer to (iii): no finite certificate was obtained
by these attempts. Every
fixed-slice description reduces the deep levels to ES solutions of 4/17^c (M17D's wall); the moving-slice boxes
need positional data at all depths; the only self-map (FF Frobenius) is exactly critical. A finite certificate would need
a genuinely new per-parent bound (Conj 4.2) — a B2-type statement, as (J)77 says.
