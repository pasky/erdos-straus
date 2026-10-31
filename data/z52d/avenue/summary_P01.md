# z52d avenue — batch P01 (100 items) summary
ES is OPEN. Rows: `out_P01.jsonl`; labels are Assessments unless a PROVED/CERTIFIED source is cited. Mostly unit-fraction literature, sign laws, rings.

**Status × plausibility** (columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration) | 48 | 0 | 0 | 1 | 49 |
| circular | 31 | 0 | 0 | 0 | 31 |
| known-false (5 CONDITIONAL on H/Dickson) | 12 | 0 | 0 | 0 | 12 |
| unclear | 4 | 1 | 0 | 0 | 5 |
| open-plausible | 0 | 2 | 1 | 0 | 3 |
No harder-than-open. Novelty: 0 → 55, 1 → 42, 2 → 3 (Z0163, Z1121, Z1358; all dead or calibration).

**Plausibility ≥ 2 AND novelty ≥ 1:** one item, no ES yield.
* **Z0251**: *positive ES over ℤ[1/ℓ] holds for every n ≥ 2 and every ℓ ≥ 2* (ℤ[1/ℓ] = ℤ[1/rad ℓ]). PROVED here (elementary, no GRH).
  For non-square ℓ ≥ 3 take a prime q ≡ 3 (4) with (ℓ/q) = −1. Then ord_q(ℓ) = 2k with k odd, so q | 1+ℓ^k, and with x = (n+q)/4,
  4/n = 1/x + qℓ^k/((1+ℓ^k)nx) + q/((1+ℓ^k)nx). This extends other_rings Prop 3.2 (ℓ = 3, 5) to every ℓ. Unlike
  POWER_LADDER Thm 5.1, which puts the mute prime in one numerator, it needs no Artin condition. Checked by
  `scripts/z52d_avenue_zl_check.py`. It is a relaxation; transport back to cap 0 is blocked (B-fin). (Plaus 2, novelty 0: Z0075.)

**Recurring missing theorems**
1. *Growing-window lower tail* (X_win / X_QNR; one B2 event per window; bounded windows false under Dickson): Z0942, Z0708, Z2206, Z2170, Z2145.
2. *A fixed finite menu of slices always fires* (false i.o. under H/Dickson, n = 1 shadow): Z0548, Z0996, Z1443, Z1352, Z1306; Z1283 (fixed S-units: false unconditionally, by counting);
   disproof mirror Z3065 (finite coverings empty finitely many slices; Sierpiński small factors give ES by scaling).
3. *Many-term density/Fourier methods at k = 3* (B3, addcomb memo §3.1): Z1260, Z1421, Z1422, Z2447, Z1317, Z2165, Z2205, Z2136.
4. *Restatements of the e-slice / divisor-class event*: Z1360, Z1361, Z0226, Z0078, Z0981, Z2185, Z1438, Z1491, Z1358, Z2107,
   Z0218 = Z2079 (the field moves with d, so there is no single class group).
5. *Local/theta/spinor steps (true at odd squares) or power-size detectors (B3)*: Z0219, Z2120, Z2344, Z0314, Z2391.
6. *Sign laws give parity, never class*: Z1054, Z1471, Z1483, Z1342, Z1008, Z1352.
7. *Relaxation without transport*: Z0126, Z0251, Z0256, Z0137, Z0323, Z1638, Z2883.
8. *Calibration only*: Erdős cluster Z2153–Z2208, numerator models (Z0527, Z0734, Z2215), strata/valuation lemmas (Z0259 = Z1271,
   Z0868, Z0872, Z0319 = Z0994 = Z1010, Z0973), census items (Z0943, Z0949), FF/ring items (Z0004, Z0006, Z0099, Z0352).

**Cheap checks / proofs** (timeout 60, ulimit 4 GB). Z0251: identity checked for all primes ℓ < 3000 and n ≡ 1 (4) < 400. Z1471: every (★) divisor a ≡ −1 (mod 4C) of 4Cp+1 has
  (a/p) = −1 (3-line Jacobi proof; this is T1 at the divisor level). Z1483: if gcd(p, cd) = 1, Type I hits at (c, d) force (d/p) = −1, because χ_{−4d} is odd and f ≡ −p. Check over 30 primes ≈ 10⁴, d ≤ 15: no hit with (d/p) = +1
  (`scripts/z52d_avenue_typeI_dsign.py`). Pass 1's 'surprise' (no hits at d = 1) is this genus/BM factor (1 − (d/p)).
**Corrections:** Z0226/Z1491/Z2107 need p > p₀ ((★) fails at 409). Z1471 was 'not proved' in Pass 1 and is now proved. Z0110: the 17/241 coincidence is a one-sided inclusion plus
the rarity of E₈. Z0099: no Gaussian T1 is expected (no real place, T1_TEMPLATE Cor 2.2). Z3065: the Sierpiński analogy points the wrong way.

**Assessment.** No P01 item points outside the repo's B2 / B3 / T1 / relaxation-transport picture; the only new theorem (Z0251) is ring-side.
