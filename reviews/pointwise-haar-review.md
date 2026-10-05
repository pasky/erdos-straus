# Hostile review R46 of POINTWISE_HAAR.md (branch side-agent/haar-exponent)

Reviewer branch `side-agent/review-haar`. Reviewed commit: 6f4ca8b.
Status: IN PROGRESS.

## Verdicts per claim

* **Lemma 1.1** — SOUND. Re-derived: given A, each compatible C becomes
  C' ⊇ C independent of S_A; ⋂C̄' ⊂ ⋂C̄.
* **Lemma 1.3** — SOUND (re-derived). Lopsided condition P(E|Av(S')) ≤ P(E)
  for S' ∩ Γ(E) = ∅ is exactly Lemma 1.1. Split S = S1 (conflicting with A) ∪ S2;
  P(A|Av(S)) ≤ P(A|Av(S2))/P(Av(S1)|Av(S2)); numerator ≤ P(A) (Lemma 1.1),
  denominator ≥ ∏(1−x_E) by the LLL induction (valid for every subfamily S').
* **Theorem 1.4** — SOUND. Re-derived line by line: P(E_i|B_i) ≥ P(E_i)P(B_i|E_i)/P(B_i^d)
  (B_i ⊂ B_i^d); given E_i, conflicting E_j vanish, compatible E_j become E_j' independent
  of S_i; P(E_j'|B_i^d) ≤ K P(E_j') by Lemma 1.3 (conflicts with E_j' ⊂ Γ(E_j)); sum with
  −log(1−p) ≥ p. Second bound: random thinning, p = min(1, μ/(2KΔ)); K, x_E inherited
  by subfamilies. Directions of all inequalities correct.
  From-scratch exact brute force `scripts/review_haar_janson_bf.py` (Fractions, random
  non-uniform marginals, one-hot coordinates, ranges 2–6, 2–10 events, all subfamilies S
  for Lemma 1.3, plus random external atomic A): seed 1×1500 instances (454 with valid
  LLL weights x_E = tP(E)) and ADV seed 2×300 (292 valid, 6–10 events with ≥2 coordinates
  each): **0 failures** of Lemma 1.1, Lemma 1.3, both bounds of Thm 1.4. Tightest
  (μ−KΔ) − (−log P(Av)) = −2.6e-5 (single-event-like instances).
  Scope caveat (author states it): single-value atomic events only; prime-power moduli not
  covered. §2 uses squarefree y-rough M, so fine.
