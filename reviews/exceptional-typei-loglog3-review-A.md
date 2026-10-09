# Hostile review A of EXCEPTIONAL_TYPEI_LOGLOG3.md (task R121A)

Reviewer: side agent R121A (independent of reviewer B). Branch reviewed: `side-agent/eff-di7` (merged into
`side-agent/review-ttl3-a`). Work in progress; sections filled one at a time.

## Verdicts (summary)
(to be filled)

## §2 (induction (8.19), Prop 2.1, Thm 2.2, Cor 2.3) — verdict: SOUND (relative to (P1)–(P3))

Re-derived line by line; from-scratch sweep `scripts/review_r121a_induction.py` (log-space, 2·10⁵ random
`(δ, c, K₁, K₂, Q, N)` per case, δ down to 10⁻³, constants up to e³⁰) finds no violation of cases (A), (B), (C) of
Prop 2.1 or of Cor 2.3 (max of `log log H − (B+3)/δ` over the grid is −27.6).
* (P2) is a faithful transcription of DI (8.5) (scan p. 271: `S(Q,Y,N,0) ≤ c(ε)∫S(πNYQ⁻¹,Y,N,it)dt/(t⁴+1) +
  c(ε)(YN)^ε(Q+N+NYQ⁻¹)‖a‖²`, S as in (8.4) with `Q<q≤16Q`), with ‖a‖² ≤ 2N for closed intervals absorbed.
* (M) needs only `0 < 2σ_j ≤ 1/2` (Selberg 3/16) ✓. (PS): Abel summation and Cauchy–Schwarz in `dξ/ξ` over
  `[N,N₁] ⊂ [N,2N]` give `|·|² ≤ 2|A(N₁)|² + 2t²(log 2)∫|A|²dξ/ξ`; after weighting/summing,
  `≤ 2S* + 2t²(log 2)²S*` ✓. The intervals `[N,ξ]` are admissible (closed, `ξ ≤ 2N`) ✓.
* Case (C): `Q₁ = πQ^{1−2δ}` satisfies `N ≤ Q₁ ≤ Q/2` exactly when `Q^{2δ} ≥ 2π` and `N ≤ Q^{1−2δ}` ✓; the main term
  is in fact `2√2π·π^{5δ}·cH·Q^{1+4δ−10δ²}N` (the text's `π^{1+4δ}` overestimates harmlessly), the error term
  `≤ 3cQ^{1+2δ}N` ✓, and `H/2 + 3c ≤ H` because `H ≥ 6c` ✓. **No accumulation**: the same H is reproduced at every
  dyadic step, so the number of induction steps (≍ log Q) does not enter the constant. This is the crux of the
  double-exponential claim and it is correct: `log Q₀ ≍ δ^{−2}log c(δ)`, `log H ≤ log(2K₂) + log Q₀`, so
  `log log K₇ ≤ max(log log K_i) + 2 log(1/δ) + O(1)` ✓ (Cor 2.3).
* Thm 2.2: both branches re-derived ✓ (`Y₂ = Q^{2−2δ}/N ≥ Q^{1−2δ} ≥ 1`).
* Non-circularity: (P1), (P3) are non-inductive; (P2) is applied only with `Q₁ ≤ Q/2` and `N ≤ Q₁` ✓.
Cross-check with DI's own proof (scan pp. 276–278): DI inducts with `Q₁ ≤ Q − 1`; the dyadic variant is
equivalent. DI's step "extend q from [Q,2Q] to [Q,16Q] by applying the estimate at (2^lQ, 2^lY)" (p. 273) is
the place where C is held fixed; that is inside (P2) (§4), not here.

Minor (§2): m1 below.
