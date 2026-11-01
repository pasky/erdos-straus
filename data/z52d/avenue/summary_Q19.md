# z52d avenue — batch Q19 (110 items) summary
ES is OPEN. Rows: `out_Q19.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. Non-proof-attempt batch
(feature flips, analogies, Erdős-problem pages): 67 rows are "calibration only", handled briefly.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration fact) | 0 | 1 | 0 | 69 | 70 |
| known-false | 16 | 0 | 0 | 0 | 16 |
| circular | 12 | 0 | 0 | 0 | 12 |
| open-plausible | 0 | 5 | 3 | 0 | 8 |
| unclear | 1 | 2 | 0 | 0 | 3 |
| harder-than-open | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 84, 1 → 26, 2 → 0. Plaus-3 rows are calibration facts (yield none), except Z3160 (partial: main term, PROVED in BM_LVALUE).
**Plausibility ≥ 2 AND novelty ≥ 1** (one line each; only Z1557 has any yield)
* **Z1557** (partial, thin family): *for fixed a ≡ 0 (4), some C(m) makes 4C(m)·(a^m − 1)/(a − 1) + 1 factor cyclotomically with a factor ≡ −1 (mod 4C(m)) ∀m.*
* Z2027: *ES + K unit fractions from {2^j}, K bounded* (relaxation; K → 0 transport missing, B-fin). Z1927: *each B-slice fails with density ≍ (log p)^{−1/2}* (heuristic).
* Z1982: *n = xyz − x − y − z fails only if 2n + 5 is prime* (PROVED). Z2047: *the ++ continuant reverses the BM sign (weight 1 + χ(p))*.
* Z2028: *Crocker failures need forced compositeness; ES failures would need forced confinement*. Z2565: *single-slice failure density → 0 (upper sieve)*.
* Z2209: *xy + yz + zx omissions are an idoneal-type list; irrelevant at primes*. Z3125: *a power main term also needs enough free variables*.
* Z2111/Z2113: *approximation properties do not produce integral ES witnesses*. Z2119: *the ES form is cubic, so quadratic near-miss identities do not apply*. Z2133: *certificate ordering has no existence content*.
**Recurring missing theorems**
1. *Tied divisor event / forest bichromatic edge* (circular; (★)-forms qualified to p > 8 813 281): Z1437, Z1442, Z2023, Z2058, Z2884 (Thue ratio
   set + divisibility = ES₅), Z2590 (= Q18 Z0498), Z3140 (3-4-1), Z2043/Z2092 (q-series positivity), Z1552, Z2087.
2. *One-coordinate polylog window* (open, plaus 1; FRONTIER §6, §7.2, §7.17): Z1406, Z1850. The (★)-only form is false (Z1457).
3. *Privacy of large primes kills incidence/stickiness/recursion* (known-false): Z3113, Z3191, Z2065, Z2371.
4. *BM deficit governed by one L-value L(1, χ_p)* (known-true, BM_LVALUE Thm A; asymptotic): Z2905, Z3160, Z2071, Z2103. Gap: error R − M_BM.
5. *Finite menus, local criteria, freedom of choice* (B1/T1/M4): Z2101, Z2339, Z3159, Z1419, Z2221, Z2927, Z2251 (absorption), Z2621.
**New in this pass** (script `scripts/z52d_avenue_Q19_xyz3.py`, timeout 120)
* **Z1982** (identity PROVED, data CERTIFIED to 10⁵): (xy − 1)(xz − 1) = x(n + x) + 1, and the x = 2 class condition is vacuous, so n is represented
  whenever 2n + 5 is composite. All 708 exceptions in (10³, 10⁵] have 2n + 5 prime, and 324 also have 3n + 10 prime. The n ≡ 3 (6) enrichment is
  mod-3 admissibility. So the "not finite-looking" failure set comes from primality at low levels, and Pass 1's Poisson comparison was mis-specified.
* **Z1927** (Assessment): the maximum-cardinality subgroups of (ℤ/4B)^× avoiding −1 are odd-quadratic kernels (index 2), so heuristically δ_B = 1/2.
  Inclusion-maximal ones can be smaller ({1, 11} mod 20). The subgroup criterion is exact only for 4B | 24.
* **Z1926 = P00 Z0216**: the B = 1 slice of (★) and the chain world x | y | z have the same Landau criterion ((p + 1)/2 has a prime ≡ 3 mod 4).
**Corrections.** Z1398: "min max-denominator ≤ p^{1+o(1)}" is false at every prime (≥ p^{3/2}/2). Z2332: ES does have multiplicative closure.
Z1457: "C_min ≪ log²p" is false for (★). Z2102 (GRH ⇒ ES) is recorded as "unclear": no implication is known, which is not a refutation.
**Assessment.** No architecture in Q19 escapes B1/B2/B3/M1–M5. The siblings (Z1982, Z2047) only sharpen calibration.
