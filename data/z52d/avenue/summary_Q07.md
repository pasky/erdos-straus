# z52d avenue — batch Q07 (113 items) summary
ES is OPEN. Rows: `out_Q07.jsonl`; labels are Assessments unless a PROVED/CERTIFIED source is cited. 33 rows are calibration only; the rest are mostly analytic-NT transfers.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-false | 38 | 0 | 0 | 0 | 38 |
| known-true (gap named) | 0 | 0 | 0 | 34 | 34 |
| unclear | 24 | 0 | 0 | 0 | 24 |
| circular | 15 | 0 | 0 | 0 | 15 |
| open-plausible | 0 | 2 | 0 | 0 | 2 |
Novelty: 0 → 49, 1 → 64, 2 → 0. The two open-plausible rows are already-mapped targets: Z1480 (= §7.1, spectral form) and Z2017 (= §7.2 HC(p)).
**Plausibility ≥ 2 AND novelty ≥ 1**: none with ES yield. All are plaus-3 calibration/main-term facts: Z1493 (class-free shifted divisor sums are
pointwise-provable; the class restriction is the gap), Z1562, Z1577 (C = 1 failure set ≍ x/(log x)^{3/2}, Iwaniec half-dimensional sieve), Z1996,
Z2051, Z2382, Z2399, Z2409 (failure-type census, below), Z2461 (energy at the Cauchy–Schwarz minimum).
**Recurring missing theorems**
1. *Better levels / large sieves move the exceptional-set exponent* (no: constants only, 3/4 CRT cap): Z1542, Z1645, Z1806, Z2072, Z2380, Z2381, Z2408, Z2424.
2. *Tied modulus defeats correlation / level machinery*: Z1536, Z1721, Z1739, Z1815, Z2147, Z2307, Z2383, Z2388, Z2395, Z2396.
3. *Equidistribution of a polylog product set* (M1a absent): Z1046, Z1067, Z1957, Z2148, Z2429, Z2431, Z2459.
4. *Primes are the wrong auxiliary objects*: prime N_C always fails (Z2093, Z2377); prime witnesses are subcritical (Z1449, Z1821); parity is irrelevant (Z1996, Z2306).
5. *Averages only (B6)*: Z0947, Z1363, Z1366, Z1755, Z1825, Z2106, Z2416, Z2423, Z2442, Z2445, Z2446. 6. *Fixed levels = Landau sets*:
   Z1577, Z1578, Z1928, Z2038, Z2219, Z2401. 7. *Main term only*: Z0907, Z1684, Z1824, Z2050, Z2051, Z2338.
**New in this pass** (scripts `scripts/z52d_avenue_Q07_*.py`, timeout ≤ 120)
* **Z2409 failure-type census** (`…_failtype.py`; 14 (★)-zeros vs 14 controls, C ≤ 40). Failing levels split as: BM-kernel (all prime factors in
  ker χ_{−4C}) 58 % vs 46 %; another genus/real character 16 % vs 27 %; higher-order character only 3 % vs 2 %; no character at all (−1 ∈ ⟨prime
  classes⟩ but no divisor ≡ −1, i.e. too few prime factors) 23 % vs 25 %. Beyond BM (§7.3), failures come from genus characters and small-ω
  exhaustion, almost never from higher-order characters.
* **Z1928 (PROVED, one line)**: the u = 1 line succeeds iff p + 1 has a prime factor ≡ 3 (mod 4). So every (★)-zero lies in the chain-world failure set
  {(p+1)/2 has only prime factors ≡ 1 (4)} (out_P00 Z0216). Checked on all 14 zeros ≤ 10¹⁰.
* **Z1814**: any delta-method asymptotic R(p) = 𝔖J + o(M) is false i.o. (Linnik, BM_CORRECTED Prop 3.1). **Z1449/Z1821**: prime-witness
  certificates have mean ≈ 0.55 log p (Poisson heuristic: ≈ x^{0.45} failures), so 'Linnik for shifted multiples' is heuristically false.
* **Z1562**: the 9σ negative dependence of level successes is coprimality (gcd(4p+1, 8p+1) = 1). **Z0907**: Siegel 'starvation' of (★) is impossible
  at main-term level (BM_LVALUE). **Z2461**: Var(R) ≈ (2/log N)·M², super-Poisson by ≍ log N, which calibrates the fat zero law (§2.4).
**Corrections.** Z2038: Pass 1's k = 1 density 0.50 is the p ≡ 3 (4) half (no repeated entries at p ≡ 1 (4)). Z2338: Pass 1 tested (−C/p), not the
BM character χ_{−4C} on divisors of 4Cp+1. Z0948: an all-solutions f(n) over composites inherits divisor solutions (heuristically ≍ log⁴).
**Assessment.** Q07 is the analytic-NT toolbox applied to ES. Every tool either averages (B6), needs a power-size set where ES has a polylog product
set (M1a), or needs a summation variable independent of the modulus (tied). The one new structural datum is the failure-type census (Z2409),
which gives FRONTIER §7.3 a concrete shape: genus characters plus small-ω exhaustion.
