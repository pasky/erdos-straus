# z52d avenue — batch Q04 (113 items) summary
ES is OPEN. Rows: `out_Q04.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 68 rows are calibration only (other-ring/cone twins, fingerprint correlations, category checks), handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 66 | 66 |
| known-false | 22 | 0 | 0 | 0 | 22 |
| circular | 15 | 0 | 0 | 0 | 15 |
| unclear | 1 | 5 | 0 | 0 | 6 |
| open-plausible | 0 | 1 | 0 | 3 | 4 |
Novelty: 0 → 63, 1 → 50. Plaus-3 rows are calibration/main-term/other-ring statements. Only Z0554, Z0635 have a (partial, already known) yield.
**Plausibility ≥ 2 AND novelty ≥ 1** (32 rows; none has an ES yield). Calibration/no-yield: Z3078 Z3114 Z3116 Z0063 Z0064 Z0066 Z0076 Z0081 Z0093 Z0094
Z0229 Z0255 Z0270 Z0271 Z0276 Z0282 Z0317 Z0320 Z0329 Z0330 Z0343 Z0345 Z0346 Z0634 Z0697 Z0727 Z0751 Z0889 (one-line statements in the rows). The rest:
* **Z0086**: *positive ES over O_K for all real quadratic K with N(ε) = +1* (inert ℓ ≡ 3 (4), ε of even order mod ℓ). Twin world only, no transfer.
* **Z0215 / Z0275**: *one lottery zero law predicts thinned-world failure rates* (40/1125, 451/499, 276/499): a B2-model test, no proof role.
  **Z0554**: *Smith spin sums ⇒ density one* is superseded (Vaughan / 3/4 note), and B6 blocks every-p.
**Recurring missing theorems**
1. *Gaussian-twin transfer* (unclear/known-false): trace descent gives 8/p (⇒ ES) only under a B2 divisibility Tr | N, and a pair collapses to 2 terms: Z0059,
   Z0091, Z0268, Z0316, Z0338, Z0564, Z0057, Z0257.
2. *Other-ring unit mechanism has no ℤ shadow* (1/ℕ + 1/ℕ ⊂ (0, 2]): Z0040, Z0056, Z0064, Z0077, Z0255 (+ twins Z0063, Z0066, Z0093, Z0267, Z0343).
3. *e-slice / merge / free-x reformulations* (circular): Z3014, Z3046, Z3073; *bounded first-step rules* (B1): Z3023.
4. *Genus/class-number/theta/Heegner identities* (T1, B3): Z0088, Z0249, Z0466, Z0467, Z0555, Z0797. 5. *Reciprocity/Rédei/Lucas class
   forcing* (class-not-parity; residue = §7.6): Z0536, Z0546, Z0565 (+ nulls Z0100, Z0782, Z0784, Z0881).
6. *Fingerprints = main term* (BM_LVALUE, RESIDUE_HARDNESS): Z0697, Z0700, Z0701, Z0727, Z0783, Z0798, Z0801, Z0813, Z0834, Z0835, Z0864.
7. *Strengthened targets* (stronger than ES, circular): Z3064, Z3154, Z0262, Z0356, Z0141 (growing S).

**New in this pass** (scripts `scripts/z52d_avenue_Q04_*.py`, timeout 60–120)
* **Z0762 (EVIDENCE)**: at the Lehmer pseudosquares 8089 ≤ n ≤ 4.9·10⁷, R is 0.60× nearby non-squares ≡ 1 (8), and 0.75× Mordell-class controls.
  There are zeros at 2641 and 18001, and R is 12–40 above 5·10⁵ (no collapse). Probably main-term (QR at 11, 13, …). Next: R/M_BM at A002189 ≤ 10¹⁰.
* **Z0276 (PROVED + checked p < 700)**: in the Eisenstein-norm world all three denominators have equal 3-adic valuation K ≥ 1. So that world is
  4·3^K/p = Σ 1/m_i (numerator 12 at K = 1), which explains its 90% failure rate. **Z0564 (PROVED)**: a Gaussian conjugate pair combines
  to a unit fraction only as 2-term 4/p = 1/m + 1/z, which is impossible at p ≡ 1 (4). Otherwise the residual split is ES itself. **Z0064**: in ℤ_{≥0}[√2], e ∈ 1/C + 1/C forces e ∈ {1, √2, 2}, so no unit mechanism.
* **Z2909**: 4/p ∉ S₂, so it is not an accumulation point of S₃ and no qualitative near-solution step exists. **Z0741**: a pointwise law U₈ ≥ c·U₄ is false at 241.

**Corrections.** (Post-review: 8/n ⇒ 4/n by doubling, so Z0057 is circular, not 'wrong numerator'.) Z0010: FF T1 is PROVED for U_q only. Z0239: fixed-level certificates are not Chebotarev conditions on p. Z0268: no norm projection exists.

**Assessment.** Nothing in Q04 escapes B1/B2/B3/T1. Unit-rich cones collapse ES to a covering, with no ℤ shadow, and discrete cones are twin lotteries with no
transfer. The one new empirical signal (pseudosquare depletion) is adversarial-test material for the lower tail.
