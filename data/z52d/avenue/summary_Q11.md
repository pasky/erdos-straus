# z52d avenue — batch Q11 (113 items) summary
ES is OPEN. Rows: `out_Q11.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 2 | 0 | 0 | 36 | 38 |
| known-false | 40 | 0 | 0 | 0 | 40 |
| circular | 20 | 1 | 0 | 0 | 21 |
| open-plausible | 0 | 1 | 0 | 0 | 1 |
| unclear | 9 | 4 | 0 | 0 | 13 |
Novelty: 0 → 74, 1 → 38, 2 → 1 (Z2786, plaus 0). ≈ 25 gate-G4, ≈ 20 forest/frieze/sandpile, ≈ 25 data items; plaus 3 = calibration.

**Plausibility ≥ 2 AND novelty ≥ 1:** none with a proof yield. Calibration-only: Z1512, Z1561, Z1599, Z2427, Z2652, Z2758, Z2840,
Z2850, Z2851, Z0233. Best open row: **Z1600** (plaus 1): *some level C ≤ (log p)^{log 2 − ε} has −1 ∈ D_C* (one-coordinate window).

**Recurring missing theorems**
1. *Structure-only forcing of −1 among subset products of the factors of 4Cp+1 / N_e* (Kneser, Olson, EGZ, Davenport, PFR, KM,
   BGK, Balandraud, pigeonhole on splits): Z1444, Z1596, Z1599, Z1600, Z1608, Z1690, Z1691, Z1915, Z1916, Z2425, Z2712, Z2713,
   Z2810, Z2920, Z3007, Z3010, Z3157 (Z3186's ±1-products are weaker; open). Poverty kills them (B4; |D| ≤ τ(N)).
2. *Forest F_p / bichromatic edge* (fixed roots fail under Dickson; §7.2): Z2678, Z2679, Z2681, Z2757, Z2792, Z2840.
3. *Frieze/sandpile/cluster reformulations of ES₅* (circular): Z2651, Z2675, Z2688, Z2689, Z2691, Z2693, Z2694, Z2695, Z2890.
4. *Pooling across levels* (privacy): Z2385, Z2648, Z2819, Z3079, Z3158, Z1964. 5. *Parity* (M5/T1): Z0463, Z0613, Z1896, Z2676, Z2761.
6. *B1 covering calibrations*: Z0529, Z0549, Z0625, Z0626, Z2758, Z3018, Z3059.

**New in this pass** (scripts `scripts/z52d_avenue_Q11_*`, timeout 60)
* Gate-G4 taxonomy (EVIDENCE): among level failures (10³ < p < 2·10⁴, C ≤ 30) the share where the prime factors DO generate −1
  (multiplicity poverty) is 0/7/39/75/95 % for ω = 1…5; rich failures (ω ≥ 6, 9·10⁴ < p < 10⁵, C ≤ 200) are 179/183 poverty and
  only 10/183 have a periodic D_C — the poor/periodic dichotomy (Z1596) fails. At the (★)-failing primes 409…23929, 10–13 of the
  levels C ≤ 50 are poverty failures (Z1916). Least winning C: 1 (754/1045), 2 (177), 3 (45).
* Z1561 (PROVED, elementary): for 4C | 24 the group is elementary 2-abelian, so level failure = genus confinement exactly.
* Z1599 (PROVED): H = {1, 7} ⊂ (ℤ/16)^× avoids −1 yet both odd real characters are −1 on 7 — a class obstruction invisible to
  the genus layer (so GT1's genus-free level need not win, Z1478).
* Z2652/Z2851 (PROVED given a prime q ≡ 3 (4), (q/p) = −1, q ≤ √(2p) — GRH gives it for large p; census: all p ≡ 1 (4) < 3·10⁴) p is
  τ of a TRIANGLE multigraph with non-square sandpile pairing (a ≡ √(−p) mod q, b = q − a, c = (a²+p)/q − a). The pairing ladder
  bottoms out at 3 vertices: ES₅'s cost is the fan shape, not the vertex count (the ES^□ one-Dirichlet-prime mechanism, B-fin).
* Z2655/Z0517: of the U(n) sporadics only 105 is idoneal (h(−4n) = 48, 24, 80, 240, 424 with |Cl[2]| = 8, 4, 16, 16, 8 for the rest).
* Z2607: U_n's reciprocal arrangement is n-independent (no T1). Z0263: Type II max denominator ≥ p^{3/2}√C/2 (heuristic θ* = 3/2).

**Assessment.** Q11 sharpens B4 empirically (poverty, not confinement, is the generic failure) but no row escapes B2/B4/T1.
