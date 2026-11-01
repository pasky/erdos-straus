# z52d avenue — batch Q19 (110 items) summary
ES is OPEN. Rows: `out_Q19.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch (feature flips, analogies, Erdős-problem pages): 67 rows are "calibration only", handled briefly.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration fact) | 0 | 1 | 0 | 70 | 71 |
| known-false | 17 | 0 | 0 | 0 | 17 |
| circular | 12 | 0 | 0 | 0 | 12 |
| open-plausible | 0 | 5 | 2 | 0 | 7 |
| unclear | 0 | 2 | 0 | 0 | 2 |
| harder-than-open | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 84, 1 → 26, 2 → 0. All plaus-3 rows are calibration facts or main-term statements (yield none).
**Plausibility ≥ 2 AND novelty ≥ 1 with any yield**
* **Z1557** (partial, thin family): *for a fixed base a ≡ 0 (4), some C(m) periodic or algebraic in m makes 4C(m)·(a^m − 1)/(a − 1) + 1 factor
  cyclotomically with a factor ≡ −1 (mod 4C(m)) for every m*. Next: run the 3·2^s + 1 machinery on (12^m − 1)/11 and (8^m − 1)/7.
* **Z2027** (relaxation, no ES yield): *ES + K unit fractions from {2^j}, K bounded*; the K → 0 transport is missing (B-fin).
(Other plaus ≥ 2, nov ≥ 1 rows, e.g. Z1927, Z1982, Z2028, Z2047, Z2209, Z3125, are calibration facts with yield none.)
**Recurring missing theorems**
1. *Tied divisor event / forest bichromatic edge* (circular): Z1437, Z1442, Z2009, Z2023, Z2058 (union of two lines), Z2884 (Thue ratio set +
   divisibility = ES₅), Z2590 (subset-product local limit = Q18 Z0498), Z3140 (3-4-1), Z2043/Z2092 (q-series positivity), Z1552, Z2087.
2. *One-coordinate polylog window* (open, plaus 1; FRONTIER §6/§7.2/§7.17): Z1406, Z1850. The two-coordinate form and the (★)-only form are false (Z1457).
3. *Privacy of large primes kills incidence/stickiness/recursion* (known-false): Z3113, Z3191, Z2065, Z2371.
4. *Main term governed by one character χ_p* (known-true, BM_LVALUE Thm A): Z2905, Z3160, Z2071, Z2103. Gap: the error R − M_BM.
5. *Bounded/finite menus and local criteria* (B1/T1): Z2101, Z2339, Z3159, Z1419, Z2221, Z2927. *Freedom-of-choice methods* (M4):
   Z2251 (absorption), Z2621 (Ramaré–Walker has a power-size box).
**New in this pass** (script `scripts/z52d_avenue_Q19_xyz3.py`, timeout 120)
* **Z1982** (PROVED identity + CERTIFIED to 10⁵): for n = xyz − x − y − z, (xy − 1)(xz − 1) = x(n + x) + 1. At x = 2 the class condition is
  vacuous, so n is represented whenever 2n + 5 is composite. All 708 exceptions in (10³, 10⁵] have 2n + 5 prime, and 324 also have 3n + 10
  prime. The n ≡ 3 (6) enrichment is the mod-3 admissibility of {2n + 5, 3n + 10, …}. So this sibling's "not finite-looking" failure set comes
  from primality at the low levels, and Pass 1's Poisson comparison was mis-specified. ES's level 1 is not vacuous.
* **Z1927** (Assessment): the maximal confinement sets avoiding −1 in (ℤ/4B)^× are kernels of odd quadratic characters, so δ_B = 1/2 for every
  B. "Fails iff the factors lie in a subgroup avoiding −1" is exact only when 4B | 24 (elementary 2-group, Q18 Z0498).
* **Z1926 = P00 Z0216**: the B = 1 slice of (★) and the chain world x | y | z have the same Landau criterion ((p + 1)/2 has a prime ≡ 3 mod 4).
* **Z2047** (from Pass 1 data): the ++ continuant tuv + u + v (4 | t) is (★) with the BM/T1 layer removed. Its failures among p ≡ 1 (4) stop at
  449 (≤ 2·10⁵), while (★) fails up to 8 813 281. This is a clean measure of what the BM layer costs.
**Corrections.** Z1398: "min max-denominator ≤ p^{1+o(1)}" is false at every prime (≥ p^{3/2}/2; Q03 Z0644). Z2332: ES *does* have multiplicative
closure, contrary to Pass 1. Z1457: "C_min ≪ log²p" is false for (★) (14 zeros; C_min = 23105 at p ≤ 2·10⁵).
**Assessment.** Q19 has no architecture that escapes B1/B2/B3/M1–M5. The siblings (Z1982, Z2047) sharpen the calibration: failure sets look
infinite when the lowest levels are primality events or carry the BM layer.
