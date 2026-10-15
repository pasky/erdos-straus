# z7_haar_strata — "N₋/U ≈ 3/4" is a stratum mixture; Haar 3/4 holds at large min; N₋ < U/2 failures = defective p + 1 (O231, goal 3) — SHARP

## Idea
Explain O230's scale-stable N₋/U ≈ 0.75 (0.770 / 0.739 by class). Test it against the exact 2-adic Haar mass of the
certificate set, and stratify by min(t, u, v).

## Results (UNFORCED_WORDS §5)
* **Prop 5.1 (PROVED, finite computation).** The 2-adic Haar mass of the five-slice set on X_p(ℤ₂) is exactly 3/4
  for every p ≡ 1 (4): 1280 solutions mod 2⁵ per class mod 16, 960 of them five-slice. This is the pointwise local
  version of (J)39's 240/320.
* **Stratified law (EVIDENCE, windows 10⁴ → 3·10⁷).**
  * Words with min ≥ 10 (or ≥ 50) have N₋/N ≈ 0.72–0.75, with a slight upward drift (m ≥ 10: 0.719 → 0.736, saturating ≈ 0.74,
    still below 3/4; R233 repair D7).
  * The deficit and the drift of N₋/N (0.57 → 0.64 at p ≡ 1 (8)) sit almost entirely in min ≤ 2, the automatic families.
  * N₋/U is 0.59 on min = 1 and 0.90 → 0.85 on min ≥ 3. Their weighted mean is ≈ 0.77 by accident of the window.
  * (Assessment, R233 repair D7) So the "¾-stability" is not a law, and a 2-adic computation explains N₋/N at large min, not N₋/U.
* **Lemma 5.2 (PROVED).** On an automatic family with side X the certificate count is
  (τ(X)/2)(1 − ∏_{ψ(r)=−1}[e_r even]/(e_r+1)). This is exactly half if some ψ-odd prime has odd exponent, and 1/3 if the
  ψ-odd part is r².
* **SHARP (EVIDENCE + Lemma 5.2; R233 repair D6: 8/8 in range, the 3² defect is necessary in this range, not
  sufficient — 3 failures among 25 666 such primes, 6 among 49 890 n < 10⁷).** All 8 known failures of N₋ ≥ U/2 with n ≡ 1 (8) (R227's complete list < 10⁷ plus the
  primes < 3·10⁷: 110 897, 1 512 089, 2 152 097, 3 000 329, 5 270 849, 9 948 977, 17 188 937, 21 387 257) have
  ψ-odd part of n + 1 = 3². The biggest family (Div(p + 1), t = 1 and u = 1) then runs at certificate rate 1/3. At
  5 270 849 the min ≤ 2 strata give 148/333, and min ≥ 3 gives 44/56.
* By p + 1's ψ-odd profile (all primes ≡ 1 (8) < 3·10⁷), min N₋/U is:

  | profile of p + 1 | primes | min N₋/U | failures of N₋ ≥ U/2 |
  |---|---|---|---|
  | some odd exponent | 320 343 | 0.564 | 0 |
  | clean | 107 296 | 0.600 | 0 |
  | 3² | 25 666 | 0.475 | 3 |
  | other even profile | 10 983 | 0.549 | 0 |

## Literature
(J)39 Lemma 2.1 (averaged 15/64 : 5/64); SPARKS4 three-bit law; R227 D4 (defective u = 1 side, rate 1/3).

## Barrier screen
* B6: all ratio statements are averages over p, structurally informative only.
* Lemma 5.2 and Prop 5.1 are pointwise PROVED. T1: n/a.

## Cheap numerics
`scripts/z7_ratio.c`, `z7_haar2.py`, `z7_defect_p1.py`, `z7_strata_check.py`.

## Assessment
* A sharp descriptive correction of O230's scale law.
* CONJECTURE (refinement of O230's refuted inequality): N₋ ≥ U/2 holds whenever n + 1 has a ψ-odd prime of odd exponent.
  EVIDENCE: 320 343 primes, min 0.564. No mechanism; B6.
