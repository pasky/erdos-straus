# z52d avenue — batch P01 (100 items) summary
ES is OPEN. Rows: `out_P01.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.
Batch character: mostly unit-fraction literature (Erdős problems #299–#321, Croot/Bloom/Liu–Sawhney), sign/reciprocity items, ring analogues.

**Status × plausibility** (columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration) | 48 | 0 | 0 | 1 | 49 |
| circular | 27 | 0 | 0 | 0 | 27 |
| known-false | 16 | 0 | 0 | 0 | 16 |
| unclear | 4 | 1 | 0 | 0 | 5 |
| open-plausible | 0 | 2 | 1 | 0 | 3 |
| harder-than-open | 0 | 0 | 0 | 0 | 0 |
Novelty: 0 → 55, 1 → 42, 2 → 3 (Z0163, Z1121, Z1358; all dead or calibration).

**Plausibility ≥ 2 AND novelty ≥ 1:** one item, no ES yield.
* **Z0251** — *positive ES over ℤ[1/ℓ] holds for every n ≥ 2 and every non-square ℓ*. PROVED in this pass (elementary, no GRH):
  take a prime q ≡ 3 (4) with (ℓ/q) = −1; v₂(q−1) = 1 forces ord_q(ℓ) = 2k with k odd, so q | 1+ℓ^k, and
  4/n = 1/x + qℓ^k/((1+ℓ^k)nx) + q/((1+ℓ^k)nx), x = (n+q)/4. This extends other_rings Prop 3.2 (ℓ = 3, 5) to every ℓ, and it
  needs no Artin condition (POWER_LADDER Thm 5.1 needs one because it puts the mute prime in a single numerator).
  Exact check: `scripts/z52d_avenue_zl_check.py`. ES yield: none (relaxation; transport to cap 0 is B-fin).
* Plaus ≥ 2, novelty 0: Z0075 (prove the 'collapse' half of the discrete-cone principle for real quadratic O_K with N(ε) = +1).

**Recurring missing theorems** (items collapsing onto one statement)
1. *Growing-window lower tail* (X_win / X_QNR, one B2 event per window; bounded windows false under Dickson): Z0942, Z0708,
   Z2206, Z2170, Z2145.
2. *A fixed finite menu of slices always fires* (false i.o., CONDITIONAL on H/Dickson; n = 1 shadow): Z0548, Z0996, Z1443, Z1352,
   Z1306, Z1283; disproof-side mirror Z3065 (a finite covering empties only finitely many slices; Sierpiński divisibility helps ES).
3. *Many-term density/Fourier methods at k = 3* (collapse to B3, addcomb memo §3.1): Z1260, Z1421, Z1422, Z2447, Z1317, Z2165,
   Z2205, Z2136.
4. *Tautological restatements of the e-slice / divisor-class event*: Z1360, Z1361, Z0226, Z0078, Z0981, Z2185, Z1438, Z1491,
   Z0218 = Z2079 (moving field, no single class group), Z1358 (Dedekind sums = CF length = ES₅), Z2107 (genus split, one-sided H⁻).
5. *Local / theta / spinor steps* (true at odd squares, T1): Z0219, Z2120, Z2344, Z0314; power-size detectors (B3): Z2391, Z2344.
6. *Sign laws give parity, never class*: Z1054, Z1471, Z1483, Z1342, Z1008, Z1352.
7. *Relaxation without transport*: Z0126, Z0251, Z0256, Z0137, Z0323, Z1638, Z2883.
8. *Calibration only*: the Erdős-problem cluster Z2153–Z2208, numerator models (Z0527, Z0734, Z2215), strata/valuation lemmas
   (Z0259 = Z1271, Z0868, Z0872, Z0319 = Z0994 = Z1010, Z0973), census items (Z0943, Z0949), FF/ring items (Z0004, Z0006, Z0099, Z0352).

**Cheap checks / proofs in this pass** (timeout 60, ulimit 4 GB)
* Z0251: identity verified for all primes ℓ < 3000, n ≡ 1 (4) < 400 (`scripts/z52d_avenue_zl_check.py`).
* Z1483: Type I hits at (c, d) force (d/p) = −1 (−d is a QR mod f, f ≡ −p (mod 4d), χ_{−4d} odd); 30 primes ≈ 10⁴, d ≤ 15, c ≤ 40:
  0 hits with (d/p) = +1 (`scripts/z52d_avenue_typeI_dsign.py`).
* Z1471: every (★) divisor a ≡ −1 (mod 4C) of 4Cp+1 has (a/p) = −1 (3-line Jacobi proof; the divisor-level form of T1).

**Corrections to inputs**
* Z1483: Pass 1's "surprise" (zero Type I hits at d = 1 despite smallest h(−4)) is the genus/BM factor (1 − (d/p)), PROVED above.
* Z1471: Pass 1 "not proved" → proved. Z0110: the 17/241 coincidence follows from a one-sided inclusion plus the rarity of E₈.
* Z0099: no Gaussian T1 is expected (ℤ[i] has no real place, T1_TEMPLATE Cor 2.2); 3+4i is a low-count failure.
* Z3065: Sierpiński-type coverings force small factors, which give ES by scaling: the analogy points the wrong way.

**Assessment.** No P01 item points at a proof architecture outside the repo's B2 / B3 / T1 / relaxation-transport picture.
The only new theorem is a ring-side one (Z0251) with no ES yield.
