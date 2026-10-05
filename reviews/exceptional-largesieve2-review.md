# Hostile review R27 of EXCEPTIONAL_LARGESIEVE2.md (task O27)

Reviewer: side-agent/review-largesieve2. Reviewed: branch
`side-agent/ls-escapes` (checkpoint 1). From-scratch scripts:
`scripts/review_ls2_*.py`. Status: **in progress**.

## Verdict per claim

| claim | verdict |
|---|---|
| Lemma 1.1 (comparison measure) | SOUND (conditional on K2 Thm 5.1, as labelled) |

## Claim-by-claim notes

### Lemma 1.1

Re-derived. Primal: `min E_U ν` over the subspace `V_𝒟` (free
coordinates) subject to `ν(x) ≥ 1_𝒜(x)` for all `x ∈ ℤ/M'` (the `ν ≥ 0`
constraints on 𝒜 are implied, off 𝒜 they are the same family). Finite LP,
feasible (`ν ≡ 1`), bounded below by 0, so strong duality: there is
`μ ≥ 0` on `ℤ/M'` with `Σ_x μ(x)ν(x) = E_U ν` for all `ν ∈ V_𝒟` (equality
because ν is free in a subspace) and `μ(𝒜) = m*`. Signs are right. Since
`1 ∈ V_𝒟`, μ is itself a probability (not stated, harmless). π = μ|_𝒜/m* is
supported on `𝒜 mod M'` by construction; for `f ≥ 0` the dropped mass off 𝒜
only helps. No compactness issue (finite dimension). K2 Thm 5.1's
majorant class (`ν = Σ a_i 1[n≡b_i (d_i)] ≥ 0` on ℤ, `≥ 1` on 𝒜, each
`d_i` of W-rough level `≤ λ`, `λ ≥ λ₀`) contains every primal-feasible ν
(the d ∈ 𝒟 divide M', so "on ℤ/M'" = "on ℤ"), hence `m* ≥ e^{−S(λ)}`.
Remark (iii) / (1.2): checked; the lifted `F(n) = f((n−c)/Q₀)1[n≡c (Q₀)]`
needs `Q₀d | M'`, which holds as `Q₀d ∈ 𝒟`. Converse direction (Remark
(i)) correct.

Numerical check from scratch: see `scripts/review_ls2_lp.py` (pending).
