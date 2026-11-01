# z52d avenue — batch Q04 (113 items) summary
ES is OPEN. Rows: `out_Q04.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 68 rows are calibration only (other-ring/cone twins, fingerprint correlations, category checks), handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 66 | 66 |
| known-false | 24 | 0 | 0 | 0 | 24 |
| circular | 13 | 0 | 0 | 0 | 13 |
| unclear | 1 | 5 | 0 | 0 | 6 |
| open-plausible | 0 | 1 | 0 | 3 | 4 |
Novelty: 0 → 63, 1 → 50, 2 → 0. Every plaus-3 row is a calibration lemma, a main-term statement, or an other-ring theorem (yield none).

**Plausibility ≥ 2 AND novelty ≥ 1**: 33 rows, none with an ES yield. The non-trivial ones:
* **Z0086**: *positive ES over O_K for every real quadratic K with N(ε) = +1*, via an inert ℓ ≡ 3 (4) with ε of even order in the norm-one group (Chebotarev). It is a theorem in the twin world, with no transfer to ℤ.
* **Z0215 / Z0275**: *a single lottery zero law predicts the failure rates of thinned-denominator worlds* (40/1125, 451/499, 276/499). An out-of-sample test of the B2 model; no proof role.
* **Z0554**: *Smith spin sums ⇒ density one*. This is already superseded (Vaughan / 3/4 note), and B6 blocks every-p.

**Recurring missing theorems**
1. *Gaussian-twin transfer* (unclear/known-false; every natural descent changes the numerator to 8 or collapses to 2 terms): Z0059, Z0091, Z0268,
   Z0316, Z0338, Z0564, Z0057, Z0257.
2. *Other-ring unit mechanism has no ℤ shadow* (ℕ has no element < 1; 1/ℕ + 1/ℕ ⊂ (0, 2]): Z0040, Z0056, Z0064, Z0077, Z0255 (+ calibration twins Z0063, Z0066, Z0093, Z0094, Z0267, Z0343).
3. *e-slice / merge / free-x reformulations* (circular): Z3014, Z3046, Z3073; *bounded first-step rules* (B1): Z3023.
4. *Genus/class-number/theta/Heegner identities* (T1, B3; known-false): Z0088, Z0249, Z0466, Z0467, Z0555, Z0797.
5. *Reciprocity/Rédei/Lucas class forcing* (class-not-parity; residue = §7.6): Z0536, Z0546, Z0565 (+ nulls Z0100, Z0782, Z0784, Z0881).
6. *Fingerprints = main term* (BM_LVALUE L(1, χ)², RESIDUE_HARDNESS p − 1 structure): Z0697, Z0700, Z0701, Z0727, Z0783, Z0798, Z0801, Z0813,
   Z0834, Z0835, Z0864.
7. *Strengthened targets* (stronger than ES, circular): Z3064, Z3154, Z0262, Z0356, Z0141 (growing S).

**New in this pass** (scripts `scripts/z52d_avenue_Q04_*.py`, timeout 60–120)
* **Z0762 (EVIDENCE)**: at the 11 Lehmer pseudosquares ≤ 1.1·10⁶, R/L² averages 0.07, against 0.14 for neighbouring non-squares ≡ 1 (8).
  There are zeros at 2641 and 18001. BM_LVALUE predicts this (T ∝ L(1, χ)², maximal at pseudosquares), but T = O((log log)²), so the depletion should fade.
  Pseudosquares are the natural adversarial set for any lower-tail claim. Next: R/M_BM at A002189 ≤ 10¹⁰ with a C engine.
* **Z0276 (PROVED + checked p < 700)**: in the Eisenstein-norm world all three denominators have equal 3-adic valuation K ≥ 1. So that world is
  4·3^K/p = Σ 1/m_i (numerator 12 at K = 1), which explains its 90% failure rate. **Z0564 (PROVED)**: Gaussian conjugate-pair lifts
  descend only to 2-term 4/p = 1/m + 1/z, which is impossible at p ≡ 1 (4). **Z0064**: in ℤ_{≥0}[√2], e ∈ 1/C + 1/C forces e ∈ {1, √2, 2}, so no unit mechanism.
* **Z2909**: 4/p ∉ S₂, so 4/p is isolated in the closure of the 3-term sums S₃. No continuity/pigeonhole step from near-solutions can exist.
* **Z0741**: a pointwise law U₈ ≥ c·U₄ is false at 241.

**Corrections.** Z0010: the FF T1 analogue is PROVED for U_q only, and ES_q squares are mostly solvable (ff_erdos_straus §3.2). Z0239: certificates at a
fixed level are not Chebotarev conditions on p. Z0268: norms are not additive, so a 'norm projection' does not exist. Z0093: the item's cone contains negatives.

**Assessment.** Q04 contains no proof architecture that escapes B1/B2/B3/T1. The analogue worlds split cleanly into two kinds. Unit-rich cones collapse ES to a covering, with no ℤ shadow. Discrete
cones are twin lotteries with no transfer. The one new empirical signal (pseudosquare depletion) is main-term and adversarial-test material.
