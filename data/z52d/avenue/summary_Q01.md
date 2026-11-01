# z52d avenue — batch Q01 (113 items) summary — ES is OPEN. Rows: `out_Q01.jsonl`; labels are Assessments unless a PROVED/CERTIFIED source is cited.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 3 | 0 | 0 | 28 | 31 |
| known-false | 30 | 0 | 0 | 0 | 30 |
| circular | 25 | 3 | 0 | 0 | 28 |
| open-plausible | 0 | 2 | 3 | 7 | 12 |
| unclear | 8 | 4 | 0 | 0 | 12 |
Novelty: 0 → 72, 1 → 40, 2 → 1 (Z0012, genus-1 FF ring; calibration). 41 rows are calibration only (yield none; most plaus-3 rows).
**Plausibility ≥ 2 AND novelty ≥ 1** (only Z2000 has proof yield):
* **Z2000** (plaus 2, partial): *inf_p F(p) ≥ c > 0 for the RESIDUE_HARDNESS local factor along nested all-QR classes p ≡ 1 (mod 840·11·13·…)* —
  a main-term floor, same as P00 Z0671. First-order model (F − 1 ∝ 1/log p) already predicts saturation: ∏ factors = exp(−O(log log P/log p)) → 1.
* Calibration, no ES yield: Z0061 (totally positive ES over number fields with unit rank ≥ 1; ℚ(√3) test), Z0005/Z0013/Z0045/Z0047/Z0050/Z0012
  (FF runs), Z2642, Z0069, Z0090, Z0095, Z0097 (settled).
**Recurring missing theorems**
1. *One tied divisor event / (★) at a fixed p* (circular): Z1570, Z1826, Z1622, Z1938, Z1819, Z3110, Z2375, Z1822 (prime-witness
   subcase), Z2018 (small-C strengthening), Z3097, Z3127, Z1574 (exceptional set finite = H⁻-type), Z2630 (sieving over e: the
   sieved variable is the modulus), Z2390/Z2906 (parity/switching at fixed p), Z2559, Z3153, Z3182 (union of two lines).
2. *Restatements of ES*: Z1749, Z1933, Z2011, Z1955, Z1605/Z2986 (Type II(c, d) ⟺ C-form of cp at C = cd), Z0073, Z3032, Z2896 (I3).
3. *Identity families in auxiliary parameters* (known-false via T1 / square-mimicking points): Z1583, Z1709, Z1830, Z1831 ((a, b) with
   p = a² + b²); Z1586, Z0035, Z0036 (p = P(t), never-square P); Z1799, Z2299, Z2313, Z3038, Z0039, Z0043, Z3022, Z3115.
4. *Size / anatomy instead of class* (smooth values, energy, approximate groups, abc, Jacobsthal, Erdős 1965 typicality, Lucas/GZ
   factorisations): Z1805, Z1826, Z2454, Z1717, Z2563, Z2018, Z1716, Z1715, Z3071 — all hit B4/B2 (class of private large primes).
5. *Local–global / reciprocity* (true at squares): Z2067, Z2622, Z2727, Z2663, Z0073.
6. *Calibration-only analogue worlds* (FF, ℤ[i], matrices, ℝ[T], dual numbers, ℤ[[T]], ℤ̄): Z0001–Z0105 block.
**Cheap checks in this pass** (scripts `scripts/z52d_avenue_Q01_*.py`, timeout 60–150 s, ulimit 4 GB)
* Z1630: (★)-zeros are NOT closed under odd-square multiples (409·9, 409·25, 577·9 solvable; 45 violations, m ≤ 7, n ≤ 10⁵);
  99 non-square (★)-zeros n ≡ 1 (4) ≤ 10⁵.
* Z1605: the Type II (c, d) = (2, 1) line (16p + 1 has a divisor ≡ 7 (8)) rescues 7 of the 14 (★) zeros, fails at the other 7.
* Z1606: least winning e-slice at the first five (★) zeros: II e ∈ {7, 3, 7, 19, 7}, I e ∈ {15, 7, 31, 7, 3}.
* Z1925: small-B shifted slices B ≤ K leave 13.6 / 1.18 / 0.35 / 0.078 % of primes ≡ 1 (4) < 2·10⁵ uncovered at K = 1 / 5 / 10 / 100.
* Z0083: positive-entry 2×2 matrix ES solvable at n = 5, 13, 17 (small entries), none found at 401, 409 (X, Y ≤ 7). Z0021: ℝ[T]-ES trivial.
**Corrections / sharpenings of inputs.** Z1619: win(p, ·) has finite support (C ≲ p/4), so the almost-periodic frame is void; Z1621: G_p(x) is a
polynomial, so the modular object is Thm K in the n-aspect; Z1627: item's expected counts (52/66) inconsistent, Pass 1's 37.3 stands;
Z2375: Pass 1's least-witness statistic (q = 3) only reflects p ≡ 2 (3), irrelevant at hard primes; Z2830: the PROVED quantitative B1
(OMEGA13 Thm 5.1) is stronger than the Maynard–Tao route; Z2966: Burgess + forced QR is refuted by sterile Mordell points at large
lnr r ((J)54/(J)70); Z0036: the Gaussian trap extends to P = N(t − ζ), ζ a root of unity (covers T² + T + 1, T⁴ + 1; Assessment).
**Assessment.** Q01 is structurally screened but non-proof-attempt material: nothing escapes the B2 / H⁻_BM / B1 picture. The only
proof-relevant open statement is the main-term floor (Z2000 = P00 Z0671), which does not touch the lower tail.
