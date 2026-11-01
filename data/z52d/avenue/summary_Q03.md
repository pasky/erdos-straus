# z52d avenue — batch Q03 (113 items) summary
ES is OPEN. Rows: `out_Q03.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 57 rows are "calibration only" (Erdős-problem pages #300–#355, numerator m/n tables, lead checks), handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 52 | 52 |
| circular | 26 | 0 | 0 | 0 | 26 |
| known-false | 11 | 0 | 0 | 0 | 11 |
| open-plausible | 0 | 0 | 6 | 8 | 14 |
| unclear | 6 | 1 | 2 | 0 | 9 |
| harder-than-open (⇒ PH) | 0 | 1 | 0 | 0 | 1 |
Novelty: 0 → 61, 1 → 45, 2 → 7 (all calibration or lead-checks). Plaus-3 rows are calibration lemmas or main-term statements (yield none).

**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**: none with ES yield. Main-term/thin-family items only:
* **Z0515/Z0737/Z0731/Z0969**: *ES hardness across numerators and along p ↦ (p+3)/4 is the RESIDUE_HARDNESS local factor (p − 1 smooth)*. B3, main term only.
* **Z2776**: *I3 holds on 3^k ± 2 and 5·3^k + 1 by finite exponent coverings*. A thin family, no transfer to primes.
* **Z2650**: *mixing of greedy-with-choice residue chain ⇒ almost-all success*. B6, weaker than Vaughan.
(Other plaus ≥ 2, nov ≥ 1 rows, e.g. Z0730, Z0900, Z0902, Z1944, Z2372, Z2771, are calibration lemmas with yield none.)

**Recurring missing theorems**
1. *Merge 4 → 3 / split–merge reachability* (circular; = ES): Z0310, Z0984, Z1123, Z1270, Z1393, Z1639, Z2268.
2. *2-term gate / e-slice form* (circular): Z0488, Z0597, Z1901, Z2163, Z2199, Z2207, Z2780, Z2875; Z1626 (trial form of (★)), Z0630 (pair form).
3. *Numerator interpolation / threshold statements* (circular, strictly stronger than ES): Z0478, Z0514, Z0592, Z1872.
   Only valid monotonicity: m | m′ ⇒ fail(m) ⊆ fail(m′) (scaling; Z0730, Z0736, Z0746).
4. *Universal hardness = p − 1 smooth / practical* (main term, B3): Z0515, Z0731, Z0737, Z0900, Z0925, Z0926, Z0927, Z0969, Z2217.
5. *Density/Fourier unit-fraction machinery* (Bloom, Croot, Liu–Sawhney, Vose, OAI 025; B3 + term count): Z1262, Z1634, Z2034, Z2154,
   Z2192, Z2200, Z2448, Z2649, Z2779.
6. *Bounded procedures / identity families* (B1/T1, known-false): Z1456, Z1657, Z2195, Z2278, Z2374, Z1338.

**New in this pass** (scripts `scripts/z52d_avenue_Q03_*.py`, timeout 60)
* **Z0900 correction**: Pass 1's script ranked by −U4, so it took the 30 *largest* counts. With the ranking fixed, 29/30 of the hardest
  primes ≤ 3·10⁴ (95/100) have practical p − 1, against a base rate of 0.354. This is a strong confirmation of RESIDUE_HARDNESS (`…_practical_fix.py`).
* **Z0969**: U(p) vs U((p+3)/4) residual corr 0.505 falls to 0.29 after partialling 43 indicators 1[d | n − 1]. This works because p − 1 = 4(q − 1),
  so the local factor is inherited; the rest is unexplained (`…_greedy_inherit.py`).
* **Z0644**: 'all denominators ≤ p^{1+ε}' is false for ε < 1/2 at every prime (scale lemma: max ≥ p^{3/2}/2; Pass 1 H02).
* **Z2374**: 'small prime witness q ≤ log²p, q | 4Cp + 1, q ≡ −1 (4C)' is a congruence atom of modulus q, so it is killed i.o. by OMEGA13 Thm 5.1.
* **Z0515**: all 12/n exceptions > 37 (73, …, 12241) are ≡ 1 (mod 24), and several are ES-hard primes (193, 577, 2521). Also, m = 15 has more exceptions (32) than m = 12 (24).
* **Z0322**: the A = T² + 1 companion run already exists (data/ffl/grid.txt l.105–117: failures only n = 3, 6; clean 7–15) but was unindexed.

**Corrections.** Z0900 (inverted Pass-1 conclusion). Z0746: "test all prime divisors solvable ⇒ composite solvable" is a one-line
scaling fact; do not compute it. Z0736: the reduction to primes works for every m. Z0524 is largely answered by Pass 1 H07 (Z2771).

**Assessment.** Q03 contains no proof architecture that escapes B1/B2/B3/B6. The only non-trivial signal is main-term: ES hardness
at a prime, across numerators and along p ↦ (p+3)/4, is one local axis (p ≡ 1 mod many small q), which is RESIDUE_HARDNESS's F.
