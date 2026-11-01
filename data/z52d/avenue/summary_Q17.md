# z52d avenue — batch Q17 (113 items) summary
ES is OPEN. Rows: `out_Q17.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 58 random-model / probabilistic items and 55 catalog siblings (Goldbach family, coverings, class field theory, Waring, …).
66 rows are "calibration only", handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 61 | 61 |
| known-false | 25 | 0 | 0 | 0 | 25 |
| unclear | 9 | 1 | 0 | 0 | 10 |
| circular | 9 | 0 | 0 | 0 | 9 |
| open-plausible | 0 | 7 | 0 | 1 | 8 |
Novelty: 0 → 77, 1 → 36, 2 → 0. Plaus-3 rows are calibration facts, catalog entries or main-term statements (yield none/partial).
**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**: only **Z2981** (main term, yield partial). A second family
is unnecessary on the L(1, χ_p) axis, since M_BM ≥ 0.92·M₀ unconditionally (BM_LVALUE). The live variant is a family whose local factor F′
is large where F is small (p ≡ 1 mod many q). B3.
Open, plaus 1, with ES yield: Z0378 (Bertrand-style explicit F(p), the only row using B1's E2 escape hatch, still B2 at the end),
Z0385 (Legendre-style 'ES unit' = FRONTIER §7.2 Pell data), Z0250 (Zsigmondy replacement), Z1891 (supersaturation), Z2363 (= Z1335 window).
**Recurring missing theorems**
1. *Random/subset-product/PD models of the level event* (calibration; correct only when conditioned on ∏ ≡ 1 mod 4C):
   Z1533, Z1827, Z1828, Z1904, Z2560, Z2580; T1-blind multiplicative-rank model refuted (Z2406, Pass 1 H06).
2. *Janson / thresholds / LDP at fixed p* (no product measure; word-level Δ/μ grows): Z1725, Z2045, Z2407, Z2436, Z2437, Z2441, Z2643, Z2755.
3. *Finite shape menus / governing fields / class groups* (B1, B2(iii), moving field): Z1788, Z0217, Z0382, Z0383, Z0384, Z0386, Z0387.
4. *Quasirandom-group / pigeonhole / AKS / PFR structure* (M1a deficit ≈ p⁵; B4; divisor sets are not groups): Z2591, Z3011, Z3070, Z3034, Z3021, Z2589.
5. *T1-true inputs* (theta/forms/spinor/Demjanenko second half): Z0390, Z0395, Z0399, Z0394.
6. *Heuristic sums / zero laws* (model risk; z45_critical_chaos §3.4): Z2361, Z2842, Z3025, Z2004, Z2405, Z0368.

**New in this pass** (scripts `scripts/z52d_avenue_Q17_*.py`, timeout 60)
* **Z0143** (one square denominator, 4/p = 1/x + 1/y + 1/z²): the failures (17, 29, 41, …, 281 below 400) are explained by a *convergent*
  expected count Σ_z τ(pz²)²/z². Only 31 solvable (p, z) pairs exist for p < 400, z < 400, mostly at z ≈ √p/2, where a = 4z² − p is tiny.
  A Jacobi necessary condition holds: some factor of pz² must be a non-square mod a ≡ 3 (4). This contrasts with ES's divergent log² sum.
* **Z1631**: the 'forced QNR' that the item hoped would explain the 409 zero is automatic and already the BM layer: every (★) modulus has (M/p) = −1
  (Q16). CLASS_FORCING excludes a hidden cascade at bounded level.
* **Z2524**: the L-family of the ES character expansion is identified, namely real quadratic L(1, χ_p)² via the BM correction T(p). It is symplectic and main-term only.
* **Z0222 correction** (Pass 1 asked to reconcile log² vs log³): both hold. The average of f(p) over primes is ≍ log³p; R(p) and M_BM are ≍ log²p.
* **Z1904/Z2589**: missing −1 is the *generic* pre-cutoff case (ω ≈ log log p steps), so inverse Littlewood–Offord forces no structure.

**Assessment.** Q17 contains no architecture escaping B1/B2/B6/T1. The catalog confirms the M-pattern (§3): every proved sibling has
power-size counts, a group structure or freedom of choice. The log²-scale siblings (Sun's 2^a+2^b+2^c) are open, and Markoff shows such problems can fail i.o.
