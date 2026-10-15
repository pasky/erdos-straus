# AGENT_REPORT_O225 — near-square primes: sign fields, the complete clean-level classification, and why existence stays a lottery

Branch side-agent/near-square-exist. Main file NEAR_SQUARE_EXIST.md; scripts scripts/z2_words.c, z2_classify.py,
z2_hardness.c, z2_hardness_an.py. **ES is not solved; no infinite case of ES is claimed.**

## SHARP
1. **Sign-field criterion (PROVED, Thm 2.1).** For p ≡ 1 (4), an admissible odd divisor A at level M (t-side: A | tp + 1,
   A ≡ −1 mod t; u-side: A | p + u, A ≡ −1 mod u) has χ = −1 **iff its Artin symbol in Σ_M := ℚ(ζ_M, √−M) is complex
   conjugation**. Along n = m² + k (k > 0) a level is sign-clean (no χ = −1 word at generic m) **iff the family field
   F (ℚ(√−t(tk+1)) resp. ℚ(√−(k+u))) lies inside Σ_M**; otherwise Chebotarev gives χ = −1 words on a positive density of
   m-classes inside any class. T1 is "F = ℚ(√−M) ⊂ Σ_M at every level"; the obstruction is always "Frob = c_∞ is
   forbidden by an imaginary F" (positivity, (J)52).
2. **Complete classification (PROVED for A odd; Cor 2.2/2.3).** t-side: sign-clean ⟺ tk + 1 = □ (Prop 4.1's levels are
   also the *admissible* classification; uncleanness is admissible on a full class). u-side: sign-clean ⟺
   √−(k + u) ∈ ℚ(ζ_u, √−u), explicitly: K = k + u = f²K₀ with every odd prime of K₀ dividing u plus a 2-adic table — much
   richer than R225's "K a square" (k = 24: u ∈ {1, 3, 8, 12, 24, 25, 26, 30, 40, 48, 51, 57, 72, 74, 76, …}). Verified
   against brute force (k ∈ {1, 8, 9, 16, 24}, u ≤ 80, t ≤ 60).
3. **Pointwise genus form explains ≈ 40–50 % of the beyond-clean near-square gradient (EVIDENCE, §3).** If an imaginary
   quadratic F ⊂ Σ_u splits every odd prime of p + u, all odd-A words at u have χ = +1 (0 exceptions among 481 272 flagged
   words for 10⁵ < p < 10⁶, and among 5 287 430 for 10⁶ < p < 10⁷). Removing them shrinks the R225 residual −0.0093 → −0.0059 ([30, 100)), −0.0045 → −0.0025
   ([100, 300)), −0.0235 → −0.0014 ([10, 17)); K0 ∈ [5, 10) and K0 = 24 remain unexplained.

## Goals
* (1) even-u case: DONE, trivially (Prop 1.1): the hypothesis forces 4 | u, where every word has χ = −1, so there are no
  words; odd u re-proved from the DK sign table. Checked on all primes < 10⁷ (1 358 527 flagged words, 0 failures).
* (2) classification: DONE for words with odd A (Thm 2.1, Cor 2.2, 2.3); even A: t-side fully, u-side for u ≡ 3 (4)
  (Remark 2.4); u ≡ 1 (4) even-A words only EVIDENCE. Two-variable p = m² + kj²: not separately treated (the t-side
  Pell remark of NEAR_SQUARE §4 is the same criterion with c₀ = tkj² + 1).
* (3) CONJECTURE Y10-S "⊆": NOT done. Observation (Sparks S3): at inert ℓ the Z_K⁺ condition is "n is a QNR mod ℓ", i.e. the
  Mordell setting; for ℓ ≥ 2³² there are sterile Mordell points ((J)54), so "⊆" at large inert ℓ asks polynomial families
  in m to beat congruence sterility — Y10-S may be much harder (or false) at large inert primes than the j = 8 evidence
  suggests. The split-ℓ part is the genuinely new coverage; a 3-parameter Type I (1,0,1) family with
  f = κ(m − x), κ = α/λ + λn(x)/α − 2x, c = −αn(x), a = λ(m − x) + α, d = (m − x)/(4cλ) − 1/(4α²) is the natural tool.
* (4) MAIN AIM — existence on the family: NOT achieved. Precise negative content (§4): Lemma 4.2 (single-level Frobenius
  forcing produces only boundary words, i.e. congruence identities), and four moving-level attempts each dying at an
  identified point (algebraic factorisation of p + u → τ(m)/m lottery; levels from the factorisation of m → bounded
  primes; A near m → thin set of m; sieve → almost all m only, Z_k^□ avoids every fixed G_r). Assessment: all near-square
  input I could find is genus information, and genus information forces only boundary words.

## Sparks (not pursued)
* S1. Non-genus cleanness: the unexplained remainder of the gradient may be "c_∞ ∈ ⟨σ_r⟩·G² \ ⟨σ_r⟩" (Rédei/4-rank
  level) — test whether residual depletion concentrates on levels where ⟨σ_r⟩ ∌ c_∞ but no quadratic F separates.
* S2. Sign fields for other numerators M/p: the same Artin-symbol description should give the χ-analogue; check whether
  the special role of 4 ((J)46, full T1 only for 4 | M) is visible as "i ∈ the relevant sign field" (speculative).
* S3. Y10-S at large inert primes vs sterile Mordell points ((J)54): either polynomial families in m beat congruence
  sterility (would be a new B1-escape on quadratic families) or Y10-S fails; decide at a sterile r-generic point.
* S4. Exponential near-squares n = 4^s + k: m = 2^s is a moving modulus with periodic residues; a covering in s (as in
  (J)22 for k·2^m + 1) might certify ES for all s while Z_k^□ obstructs polynomial families in m — check whether the
  closure of {2^s} meets Z_k^□.
