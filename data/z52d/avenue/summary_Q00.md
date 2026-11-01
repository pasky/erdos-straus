# z52d avenue — batch Q00 (113 items) summary
ES is OPEN. Rows: `out_Q00.jsonl`. Labels are Assessments unless a PROVED/CERTIFIED source is cited. 56 rows (mostly fingerprint) are brief calibration-only rows.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 2 | 0 | 0 | 58 | 60 |
| known-false | 25 | 0 | 0 | 0 | 25 |
| circular | 21 | 0 | 0 | 0 | 21 |
| open-plausible | 0 | 1 | 5 | 1 | 7 |
Novelty: 0 → 107, 1 → 6, 2 → 0. Plausibility-3 rows are true calibration statements; none yields ES.
**Plausibility ≥ 2 AND novelty ≥ 1.** All are calibration with no ES yield:
* Z0867 (PROVED here): for p ≡ 1 (4), some pair of denominators is coprime ⟺ p + 4 has a prime factor ≡ 3 (mod 4).
* Z0877: primitive failures (gcd(x, y, z) = 1) ⊂ the Z0867 failure set (CERTIFIED to 6000). R-zeros 409, 577, 23929, … are not primitive failures.
* Z0850 / Z0759: the (★) boundary line u = 1 is "p + 1 has a divisor ≡ 3 (mod 4)" (= chain world, P00 Z0216); n + 1 = 2^k kills it.
* Z0062 (EVIDENCE): over Q(√5), totally positive unit-sum e's reach exactly e ≡ ±□ (mod 4O_K); the uncovered classes are the non-±squares (positivity cut, not T1).
**Recurring missing theorems**
1. *One tied-divisor event / H⁻_BM at a fixed p* (circular): Z0060, Z0254, Z0258, Z0328, Z0351, Z0480, Z0528, Z0648, Z0664, Z0702,
   Z0764, Z0775, Z0976, Z1101 (L = pm with d′ = 1 reduces exactly to (★)), Z1129, Z1218, Z1467, Z1469, Z1519.
2. *Union of two word lines* (circular): Z0772, Z0846. The main-term-only version is Z0829.
3. *Local main-term floor F(p)·M_BM(p) ≫ log²p* (= P00 Z0671; B3, partial): Z0199, Z0354, Z0691, Z0908, Z0829.
4. *Fixed finite menus / identity coverings* (B1/B2(iii); known-false): Z0018 and Z1459 (DEPTH_ASPECT Thm 3.1: non-square
   classes mod large r are not finitely coverable either), Z0335, Z0608, Z0957, Z0989, Z1147, Z1294, Z1415, Z1502. Quantified in Z1336/Z1362.
5. *Dichotomy / anti-correlation* (refuted, because the coupling is positive): Z0531, Z0610, Z0715, Z0911.
6. *Count congruences / involutions (M5)*: Z0770, Z1023, Z1476. *Transport / closure / composition* (privacy of large primes, M3):
   Z1025, Z1097, Z1344, Z1439, Z1475.
7. *Fixed-modulus (M2) sub-worlds with Landau-type criteria* (solvable; fail i.o.): Z0867, Z0850, Z0759, Z0774, Z0709, Z0974, Z0852.
   With P00 Z0216 they form one family: a fixed-modulus event on one shift (p + 1, p + 3, p + 4, 4p + 1).
**Cheap checks / small results** (scripts `scripts/z52d_avenue_Q00_*.py`, timeout 60)
* Z0867 proof: D = 4xy − p(x + y) divides pxy and is coprime to the pair, so D ∈ {1, p} or D = pD′, D′ ∈ {1, p}; the only live case is
  (4x′ − 1)(4y − p) = p + 4. Matches all 87 failures < 4000. Z0327 / Z1558: 4·3^k + 1 ≡ 5 (mod 8) and 4^k + 1 ≡ 2 (mod 3) are trivial.
**Corrections to inputs**
* Z1492 (Pass 1 "interesting"): F_p(s) is a finite Dirichlet polynomial (the cofactor is also ≡ −1 mod 4C, so C ≲ p/4); no pole.
  The S/E slowdown is a size effect (divisors below 4C cannot be ≡ −1).
* Z1529, Z0664: (★), Type I and Type II are each ≍ log²p at primes (no extra log from c; log³ is the all-n average).
* Z0018 is answered by DEPTH_ASPECT Thm 3.1; Z0877's needs-compute by the Z0867 criterion; Z0849's record 23105 is the forced p ≡ 5 (8) line.
**Assessment.** Nothing in Q00 points outside the B2 / H⁻_BM / B1 picture. The real yield is calibration: chain world, coprime pair, (★) boundary,
the C = 1 and e = 3 slices and the isosceles locus are all M2 events on one shifted integer, each with an exact Landau-type criterion and
failing i.o. ES leaves solvable territory exactly where the modulus becomes tied to the solution.
