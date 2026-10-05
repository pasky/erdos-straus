# Hostile review R29 of O29 / POINTWISE_WINDOW2.md

Reviewer branch `side-agent/review-window2`; author branch `side-agent/window-parity` @1c7763c.
All numerical checks are from-scratch (`scripts/review_w2_*.py`); no author code reused.

Status: in progress.

## Verdicts per claim

### Prop 3.7 (certified fake at θ=1/2, discrete model ε=0.1, K=8) — SOUND (as a discrete-model statement)
`scripts/review_w2_certify.py data/window2/fake_eps0.1_K8_theta0.5.json.gz` (mpmath, 60 digits):
* independently enumerated window configurations: 113 (even count, Σg<1), 12769 joint — identical
  to the dump's set; μ agrees to 5e-14 relative.
* 89 visible correlations (all pairs of multiplicity vectors with total ≤ θ, any parity).
* dumped ν: ν≥0, ν(∅,∅)=0, max relative residual 9.0e-15; support = 89 configs, ν/μ∈[0.1542, 92506].
* 60-digit LU solve of the 89×89 square system restricted to the support: solution agrees with the
  dump to 7e-13, min ν/μ = 0.15423 > 0, cond₁ = 3.0e5. Hence the exact (real-arithmetic) system
  has a strictly positive solution with ν(∅,∅)=0: the certificate is genuine, not a float artefact.
* Fragility note: the closest visible/invisible boundary is a 4-point S (3×0.1155+0.1540 = 0.50043)
  at distance 4.3e-4 above θ. The statement is for the discrete model only (see defects).
