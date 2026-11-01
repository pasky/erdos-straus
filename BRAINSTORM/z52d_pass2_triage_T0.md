# z52d Pass-2 triage, shard T0 (52 "interesting" items; Opus)

**ES is OPEN; nothing here proves or claims it.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Input `data/z52b/pass2/triage_input_T0.jsonl`; verdicts `data/z52b/pass2/triage_interesting_T0.json`; per-item notes (why, what
was re-run) `data/z52b/pass2/triage_notes_T0.jsonl`; new check scripts `scripts/z52d_tri_T0_*.py`.

## Counts
| verdict | n | items |
|---|---|---|
| REDISCOVERY | 20 | Z0276 Z0284 Z0510 Z0534 Z0559 Z0673 Z0719 Z0739 Z0849 Z0931 Z1415 Z1725 Z1821 Z2003 Z2035 Z2123 Z2941 Z3004 Z3040 Z3065 |
| EXPLAINED-BY | 17 | Z0353 Z0513 Z0616 Z0692 Z0756 Z0824 Z0835 Z0840 Z0863 Z0879 Z0896 Z1686 Z1927 Z2639 Z2783 Z2997 Z3077 |
| ARTIFACT | 3 | Z0733 Z0781 Z2966 |
| ARTIFACT/WEAK | 11 | Z0157 Z0922 Z1468 Z1620 Z1677 Z2357 Z2596 Z2624 Z2720 Z3069 Z3134 |
| NEW-CALIBRATION | 1 | Z0666 |
| NEW-STRUCTURAL | 0 | — |
| DEPTH | 0 | — |

**Assessment.** None of the 52 bears on a proof mechanism. As in Pass 1, the "interesting" label mostly marks residue-class
or χ_p effects already in RESIDUE_HARDNESS / BM_LVALUE, or numbers that were already in the repo.

## NEW-* items
* **Z0666 (NEW-CALIBRATION).** First run of the general-m Type I/II residue model (PW Props 2.1, 2.3). Survivors at X = 1000:
  m = 5: 0, 6: 1e-7, 7: 2.6e-6, 4: 1.2e-4, 8: 7.4e-3, 15: 4e-3, 12: 4.8e-2. They become sizeable first at m = 8, as in PW Table 1,
  but m = 4 ranks above 5–7 and has no exception (numerator blindness). Calibration only.

## Re-checks that changed a Pass-2 conclusion (EVIDENCE; scripts in `scripts/z52d_tri_T0_*`)
* Z1686/Z0692: the residual partial correlation h(−4p) ↔ R(p) (0.105) goes to **0.001** (null sd 0.008) on a log scale with
  Legendre controls q < 1000 and p mod 32, 27, 25, 49, 121, 169 dummies. It is the small-prime pattern (BM_LVALUE Thm A).
* Z1927: joint failure of slices B = 1..6 is 3.7× the product of marginals overall but **0.80×** within classes mod 840, so the
  whole excess is residue-class correlation.
* Z0616: E₁/E₂ correlation −0.139 → **−0.030** within p mod 3. E₁ holds at every p ≡ 2 (3), since 3 | 4p+1.
* Z2783: the ζ₈ q-rational phase predicts the word sign out of sample at 91.6% (vs 68.9%), but the sign is an exact function
  of (t,u,v) mod 8 (0 conflicts). The phase is a lossy mod-8 CF statistic.
* Z0840: λ(p) = 3 forces p ≡ 1 (24). Within that class the λ gap in median U/log²p shrinks from 0.26 to 0.06.
* Z0781: zeros vs the swap-Poisson e^{−M/2} (the correct reference, FRONTIER §2.4): 2.6–4.8 expected vs 3 observed, not "30–400×".
* Z0733: PW's heuristic with constant K ≈ 0.16 (inside MODEL_SPECIFIC §5.3's K_eff 0.09–0.27) matches the 659 window
  failures. The "four orders of magnitude" came from K = 1.
* Z0513: the exceptions 3, 5, 6 495 105 to p + 2^a + 2^b are OEIS A156695, so there is no conflict with Crocker/Pan.
* Z3077: the m = 6 exact fit is elementary. For p ≡ 5 (6), k = (p+1)/6 gives 6/p = 1/k + 1/(p(k+1)) + 1/(pk(k+1)).
* Z0863: 4/241 has only 8 solutions, the 9th-lowest count among primes < 3000. The no-3 count is exactly 1 at p = 11, 17, 23,
  1249 and 2161. So 241 is lottery-typical.

## Corrections to Pass-2 records (for whoever merges)
* Z0835: the claim that the mod-16 effect is "global, not local" is wrong. It is the certificate-family density
  (RESIDUE_HARDNESS Lemma 2, F₁₆), which RESIDUE_HARDNESS §2.2 already absorbs.
* Z0824: the "29/68 sign agreement" test is degenerate. The indicators 1[q | p+s] are collinear for s ≡ s′ (mod q).
* Z0673: the sign layer is recorded, as Lemma CT (FRONTIER B5; PARITY_AUDIT Lemma 3.2), not under "T1_TEMPLATE".
* Z2966: the "stuck at 54%" result is an artefact of never adding a new prime to M. Mod 9240, Pass-1 H06 leaves only 4 non-square classes uncovered.
* Z2003: the finite-p failure of 0.1402 L² is already stated in BM_LVALUE §3.2 (observed min 0.0969).
