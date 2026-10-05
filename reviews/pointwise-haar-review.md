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
* **Theorem 1.4** — (pending brute force) proof re-derived line by line, see §T.
