# R265 — hostile review of O255 (PARITY_AUDIT.md, branch side-agent/parity-audit)

Reviewer: R265 side agent. Reviewed commit: 282afc57. Scripts: `scripts/review_pa_*` (from scratch).
Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim 7 — census EVIDENCE (§5): **SOUND**

Recomputed from scratch in C (`scripts/review_pa_census.c`, log `logs/review_pa_census_1e6.txt`, 5.4 s, 1 core)
and Python (`scripts/review_pa_small.py`), using only the definitions in §0 (not the author's scripts).
All numbers reproduce exactly:
* (a⁴) fails (u ≤ √p + 2, which suffices by the u ↔ B symmetry of 4uBC − u − B = p) at exactly the 9 primes
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321 among the 39 175 primes p ≡ 1 (4) ≤ 10⁶. Independent
  O(p log p) brute force over (u, B) confirms R(409) = R(577) = R(5569) = 0. Least u: median 1, 99th pct 5, max 131
  at p = 427249 (confirmed).
* ES-five u-side, p ≡ 1 (8): 19 552 primes, 0 failures, 17 573 with least u ≤ 2 (89.88 %), median 1, 99th pct 5,
  99.9th pct 11, max 17 at p = 196561. p ≡ 1 (840): 395 primes, 238 at u ≤ 2 (60.25 %). Exactly 3 primes need
  u ≥ n_p.
* Windows (q < 3p; note neither event can hold for q > (p+4)/3 since d ≥ q − 1 and u + v ≤ K_q + 1): sub-event
  fails at 8272 primes, full target −1 event at 2458; max least q for the sub-event 141 971.
* T1 control: 499 odd squares 9 ≤ m² ≤ 10⁶, no (a⁴) hit at u ≤ m + 2.

Minor: "(a) hit" at odd squares (§5 T1 bullet) is undefined for composite n (ψ = Jacobi? the class layer alone?).
State which symbol was used (defect m1).

