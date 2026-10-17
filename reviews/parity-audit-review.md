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

## Claim 3 — Lemma 2.1 (trial count): **SOUND** (minor sharpening suggested)

Re-derivation. (u, C) ↦ B = (p + u)/(4uC − 1) is a bijection onto solutions; B ≥ 1 ⟺ 4uC − 1 ≤ p + u, which forces
u ≤ (p+1)/3 (the text's "u ≤ p" is harmless). |𝓡| = Σ_{u ≤ (p+1)/3} ⌊(p+u+1)/(4u)⌋ = (p/4) log p + O(p) ✓.
Inner sum Σ_{C ≤ X} 1/(4uC − 1) = (1/(4u))(log X + O(1)), X = (p+u+1)/(4u); summing (1/(4u)) log(p/u) over
u ≤ p/3 gives (log p)²/8 + O(log p) ✓. The Fourier split E(p) is the standard 1[m | n] − 1/m ✓.

From-scratch numerics (`scripts/review_pa_lemma21.py`): R via (u, f) divisor count equals an independent (u, B)
brute force for all 77 primes < 400 and at p = 10007. At p = 10⁴+7, 10⁵+3, 10⁶+3, 10⁷+19 I get M = 10.343, 16.172,
23.329, 31.811 and |𝓡|/((p/4) log p) = 0.922, 0.937, 0.948, 0.955, R = 22, 20, 16 (10⁷+19 not recomputed) — exactly
the author's values. M − (log p)²/8 ≈ −0.04 log p, |𝓡| − (p/4) log p ≈ −0.181 p: consistent with the O-terms.

Minor (m2): the U-version M_U(p) = (log U)(log p)/4 − (log U)²/8 + O(log p) is true but, at the polylog U where it
is used, the O(log p) error (= γ·log p/4 + …) is of the same order as the "main" term up to a factor log log p
(numerically at U = 10 the error is ≈ 0.13 log p against a main term 0.58 log p). Cleaner and sharper:
M_U(p) = (log p/4)·H_U + O((log U)² + 1), |𝓡_U| = (p/4)·H_U + O(U), H_U = Σ_{u≤U} 1/u.
Minor (m3): "restricting u does not shrink 𝓡" — it shrinks it by the factor log U/log p (≍ log log p/log p at
polylog U); the point (still ≍ p, not polylog) is right, the wording "does not shrink" is loose. Also the claim is
parametrisation-dependent: it says the *naive* (u, C) trial set stays of size ≍ p; it is not a theorem that every
complete-sum treatment of (a⁴) at polylog U must face ≍ p trials (Verdict (iii) should say "for the (u,C)/(u,B)
parametrisations", see Claim 8).

