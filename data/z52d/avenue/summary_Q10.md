# z52d avenue — batch Q10 (113 items) summary
ES is OPEN. Rows: `out_Q10.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 10 | 0 | 0 | 21 | 31 |
| known-false | 49 | 1 | 0 | 0 | 50 |
| circular | 24 | 2 | 0 | 0 | 26 |
| open-plausible | 0 | 1 | 1 | 0 | 2 |
| unclear | 2 | 0 | 2 | 0 | 4 |
Novelty: 0 → 94, 1 → 18, 2 → 1 (Z0135, no proof role). ≈ 30 modular/theta items, ≈ 30 generic search-tool items; plaus 3 = calibration.

**Plausibility ≥ 2 AND novelty ≥ 1:** none with a proof yield (calibration only: Z0920, Z2453, Z2523, Z3068, Z0135, Z0686,
Z0915, Z1110, Z1212). Best proof-relevant row: **Z0721** (plaus 2, nov 0) = Z0671's floor *inf F(p) ≥ c at p ≡ 1 mod smooth L*.

**Recurring missing theorems**
1. *Modular/theta generating function decides one coefficient* — answered by METAPLECTIC Thm K (Eisenstein-only) +
   SIGN_IDENTITY Thm 2.2/Prop 2.4: Z0471, Z1340, Z1679, Z1683, Z2044, Z2325, Z2326, Z2345, Z2533, Z2915, Z3043, Z3123, Z2528,
   Z2530, Z2734, Z2936, Z3041, Z3082; Tunnell/Waldspurger zero-set criteria Z2030, Z2088, Z2733, Z1300, Z1297.
2. *Hecke/transport from ℓp, ℓ²p to p* (dead: f(ℓp) > 0 always by scaling ES(ℓ); T1 kills Hecke shapes): Z1508, Z2514,
   Z2726, Z2977, Z3143. 3. *Count congruences / parity laws* (M5/T1): Z2990, Z2527, Z3026, Z1078, Z0442, Z1388.
4. *Subset-product / zero-sum / Kneser forcing* (B4, LONGSHOT Prop 1.4): Z0124, Z0545, Z1021, Z1055, Z1385, Z1343, Z1050.
5. *Fixed-p second moment over levels* (cannot certify, see below): Z2511, Z3144. 6. *Fibration/torsor/BM*: Z2939, Z3088, Z3139.
7. *Finite menus/escalation/identity search* (B1/B2(iii)): Z2935, Z0470, Z1079, Z1080, Z1086, Z1087, Z1088, Z1181.

**New in this pass** (scripts `scripts/z52d_avenue_Q10_*`, timeout 60)
* Z3144 (PROVED, one line): a fixed-p level-aspect second moment can never certify — the deterministic Chebyshev form needs
  Σ_C (D_C − E_C)² < Σ E_C² = O(1), but the left side is ≥ R(p)(1 − o(1)) ≫ log²p whenever certificates exist.
* Z0920 (EVIDENCE, 6420 primes ≡ 1 (8) ≤ 3·10⁵): Tunnell counts A, B correlate 0.52 with R/log²p (main-term layer), the cusp
  part A − 2B correlates −0.016; R/2 mod 2 is independent of (A, B) mod 8 (Z2030).
* Z2990/Z3026: R(p)/2 mod 2, 3, 4 is not constant on any class mod 24/120/840; Z2527: R/2 mod 2 is not in the F₂-span of the
  level-1 mod-2 forms Δ^k (k < 64). Z0915: partition parity p(p) mod 2 is a null (corr 0.004).
* Z0686: 232792561 = lcm(1..19)+1 is prime with R = 22 vs 24–84 (mean 50.8) at the next 12 primes ≡ 1 (840): 0.43×, the
  hardest of 13 but saturating like RESIDUE_HARDNESS designs; not a (★) or b = 1 failure (censuses).
* Z1109/Z1110: tuv − u − v = det [[u,1,0],[1,t,1],[0,1,v]], Smith form diag(1,1,n); Z1357: #bichromatic edges of F_p = ¼χᵀLχ;
  Z3166: a = ck − 1, d = cl − 1 turns the SL₂ quadric back into the cubic word equation.
* Z1212: Lenstra 1984 decides each level C ≳ √p/4 in poly time (≤ 11 divisors ≡ −1 mod 4C of 4Cp+1) — census tool only.

**Corrections.** Z2985: (★)-descent to smaller primes fails at 409. Z2935: fixed-level escalation is false only under H.
**Assessment.** Nothing in Q10 escapes Thm K (Eisenstein-only counts), T1 and B2/B4. No new proof architecture.
