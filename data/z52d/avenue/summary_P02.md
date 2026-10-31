# z52d avenue — batch P02 (100 items) summary
ES is OPEN. Rows: `out_P02.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-false | 37 | 0 | 0 | 0 | 37 |
| circular | 27 | 0 | 0 | 0 | 27 |
| known-true (gap named) | 1 | 0 | 1 | 17 | 19 |
| open-plausible | 0 | 10 | 0 | 0 | 10 |
| unclear | 4 | 1 | 1 | 0 | 6 |
| harder-than-open | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 69, 1 → 31, 2 → 0. Batch is mostly generic analytic templates (Burgess, dispersion, large sieve, circle method, Chebotarev).

**Plausibility ≥ 2 AND novelty ≥ 1:** two items, both calibration only (no ES yield).
* **Z1818** (Maynard on admissible {p, 4C_i p+1}): *unconditionally, infinitely many primes have ≥ m prime N_C among chosen levels, so those levels fail* — an unconditional shadow of FORMAL_CLOSURE Thm F; it only kills ≍ log k of k levels.
* **Z0758** (ESC zero set): *the even zeros (2402400 = 2⁵·3·5²·7·11·13, …) are smoothness-blocked small levels*; composite-n fingerprint only.
* Plaus ≥ 2, novelty 0: Z2882/Z1808/Z1809/Z2003 (T(p) via L(1,χ_p)² — closed by BM_LVALUE Thm A), Z2098 (Tatuzawa: live only for unconditional M_gen, FRONTIER §7.4 — try a Landau–Page 'one exceptional zero' input in LOWERTAIL_DEEP_ASTRA Thm 5.4), Z1555 (fixed exponent-2 levels: anal_moments_structured Prop B.1), Z1453 (sieve escape = BM/genus layer pointwise free).

**Recurring missing theorems** (items collapsing onto one statement)
1. *Tied divisor event (B2) in other coordinates*: Z2489, Z2667, Z2916, Z0246, Z0331, Z0541, Z1049/Z1447 (prime-modulus form: some prime q has (−(4p)⁻¹ mod q) | (q+1)/4), Z1440, Z1851, Z1914, Z2096, Z2052, Z2305, Z2078, Z1593.
   Sub-pattern *index half free, combinatorial half = lottery*: Z2952, Z1068, Z1446, Z1453, Z1597, Z1804.
2. *One-sided H⁻ in character coordinates* (non-real characters ≥ −(1−ε)·genus part): Z2510, Z1028, Z3136, Z1448, Z2026, Z2310, Z1993, Z2012.
3. *Average-only exceptional set beyond 3/4* (B6 + CRT cap): Z0334, Z2214, Z2360, Z2303, Z2304, Z0125, Z0031, Z1031 (= §7.5), Z0232, Z2356. Already-known almost-all: Z0410, Z1554, Z1555, Z1556, Z2083, Z2097.
4. *Power main term / local step* (B3, T1): Z2513, Z2742, Z3013, Z0485, Z1318, Z1319, Z1535, Z1653, Z2104, Z2335, Z1032, Z1807, Z1719.
5. *Polylog witness / single-character template* (OMEGA13, H4_NOT_POLYLOG, (J)106, duality): Z0696, Z1785, Z2024, Z2075, Z2149, Z1839, Z0643, Z1550, Z1708, Z0252.
6. *No absorption/propagation law*: Z0479, Z2081, Z2082, Z0647. *FF transfer blocked (units/mute place)*: Z0298, Z1997, Z2066.
7. *Calibration only*: Z2615, Z0758, Z2189, Z2223, Z2244, Z1027, Z2320, Z1817, Z1818, Z1517.

**Cheap checks run in this pass** (timeout 60, ulimit 4 GB; `scripts/z52d_avenue_P02_*.py`)
* Z2952: at all 14 (★)-zeros, −1 ∈ ⟨prime factors of 4Cp+1⟩ mod 4C at 480/2100 levels C ≤ 150 (23 %), with no hit; matched controls 584/2100 (28 %), 84 of which hit. So zeros are not index ('Artin') failures.
* Z0647: most solutions of 4/p² are not p·(solution of 4/p) (e.g. 4/25 = 1/7 + 1/60 + 1/2100; 65/73 at p = 97), so there is no structural implication from failure of ES(p) to failure of ES(p²).
* Z2189: erdosproblems.com/302 verified (a density problem about sets avoiding 1/a = 1/b + 1/c; no ES role).

**Corrections to inputs**
* Z1554 ('promising'): the half-dimensional sieve result (level-1 almost-all in square classes) is weaker than Vaughan, and the C = 1 failure set is infinite.
* Z1593: the claim that 'one-parameter families never suffice' is not supported. Under the zero law one family plausibly fails only finitely often, and (★) ∪ b=1 never fails ≤ 10⁸ ((J)89/(J)90).
* Z0334/Z2214: same FF-rate premise error as PILOT Z0003.
* Z1453: Pass 1 tested a different, trivial statement (it has a mod-3 covering).
* Z1555: the K-growing upgrade is false as a lemma (anal_moments_structured Remark B.2).

**Assessment.** No P02 item points to a proof architecture outside the repo's B2 / H⁻_BM / B3 / B6 picture. The only new
ingredient worth recording is Z2356's question: can the bilinear (u,B) structure give non-CRT input for the §7.12
exceptional-set line? It has an averaged yield at best.
