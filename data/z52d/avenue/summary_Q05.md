# z52d avenue — batch Q05 (113 items) summary
ES is OPEN. Rows: `out_Q05.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 46 rows are calibration only (fingerprints, generic technique stubs, lit checks), handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 48 | 48 |
| known-false | 42 | 0 | 0 | 0 | 42 |
| circular | 16 | 0 | 0 | 0 | 16 |
| unclear | 3 | 2 | 0 | 0 | 5 |
| open-plausible | 0 | 1 | 0 | 1 | 2 |
Novelty: 0 → 66, 1 → 47, 2 → 0. All plaus-3 rows are calibration or main-term statements (yield none).
**Plausibility ≥ 2 AND novelty ≥ 1**: 28 rows, all calibration/main-term (yield none) except Z2490, a CKMP-type 'positive proportion' that is already superseded (B6).
The one open thin-family row is **Z1847** (*ES for all 4m² + 1*; plaus 1: universal trap under H, no forced budget visible).

**Recurring missing theorems**
1. *Class-group/genus/form data force the divisor class* (class-not-parity): Z1000, Z1001, Z1836, Z2091, Z2430, Z2485, Z2491, Z2709, Z1823.
2. *Exact class-number / theta / mock-modular identity with positivity* (T1 or B3 by scale: Siegel h ≫ p^{1/2−ε} vs f ≤ p^{o(1)}): Z1302, Z1347,
   Z1356, Z1682, Z1988, Z2346, Z2365, Z2634, Z2731, Z2732, Z1972.
3. *Ternary forms / Duke–Schulze-Pillot / Siegel–Weil / Gross–Keating* (T1, B3; form moves with p): Z1481, Z1489, Z1647, Z2666, Z2728, Z2730, Z1305, Z2118.
4. *Binary-form identity families on forms representing p* (T1 along square values): Z1584, Z1707, Z1829 (+ Q04 Z0019). See the lemma sketch below.
5. *Finite menus via Legendre-symbol loci* (sign layer ⇒ positive-density escape): Z1501, Z2312, Z2336, Z1840, Z1048.
6. *Heegner/CM/isogeny/Duke equidistribution* (B3): Z1714, Z2505, Z2515, Z2531. *Thick object + extraction rule* (circular): Z1832, Z1833, Z1834.
7. *Fingerprints = main term* (RESIDUE_HARDNESS, BM_LVALUE): Z0904, Z0917, Z0918, Z0921, Z0968, Z1686, Z1999, Z2566.

**New in this pass** (scripts `scripts/z52d_avenue_Q05_*.py`; exact R from `scripts/z52b_p1_H04_rstar.c` to 5·10⁷)
* **Z1510 (EVIDENCE)**: R(p)/2 mod 2 over 1 500 441 primes p ≡ 1 (4) ≤ 5·10⁷ is a fair coin (0.4998). It is flat within ±0.0008 across p mod 8/16/24,
  (3/p), (5/p), (7/p) and (2/p)₄, so no bounded-level parity (M5) law exists for (★).
* **Z1501 (PROVED + checked)**: a Type I certificate at (c, d) forces (d/p) = −1 (0 violations in 1610 certificates). So any finite menu of d, including
  the nine Heegner d, fails on the positive-density set {(d/p) = +1 ∀ d in the menu}.
* **Z1584 (sketch, Assessment)**: a 2-variable Type I identity on a form representing odd squares must have f | Y·Z (T1 on the square-value conic,
  plus Iwaniec primes), so it is Type II, which Prop 3.2 excludes. This would close Z1584, Z1707, Z1829 and Q04 Z0019 at once.
* **Z2365**: no ES sub-count can equal a class number (Siegel vs divisor bound). **Z1001**: d ≡ 3 (4) is never a ℤ[i]-norm. **Z1999**: Euler primes
  n² + n + 41 have R/L² 3–8 % above all primes, and are identical within the Mordell classes (EVIDENCE; a local-class effect only).

**Corrections.** Z1568: Pass 1's 'C-form exceptional set' = the (★) zero set (CERTIFIED, 14 primes ≤ 10¹⁰). Z1548/Z1481: the d = 1 test cases are empty (Z1482).

**Assessment.** Nothing in Q05 escapes B1/B2/B3/T1/class-not-parity. Quadratic-form material collapses as genus-level (T1), power-size (B3, Siegel)
or parity-only (CLASS_FORCING). The useful output is housekeeping: the Z1584 lemma and the (★) parity null.
