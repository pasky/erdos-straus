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

### Thm P1 (§2) — one window: SOUND-AFTER-REPAIRS (minor); joint "four sign classes" sentence: GAP
`scripts/review_w2_p1.py 3e6` (sympy factorisation, all primes ≤3·10⁶):
* `A^+ = {p≡1 (840)}` exactly (W1's set), `A^- = {p≡281 (840)}`. |A⁺|=1115, |A⁻|=1138.
* `A^-`: n₃ clean for **0** primes (as claimed; trivially, `n₃≡p≡2 (3)`). `A^+`: 640 clean.
* `(−1)^{Ω₃⁻(n₃)}=(p/3)` (with multiplicity) for every p≡1 (8) ≤3·10⁶: 0 violations.
* `|A^±_d|` for d∈{11,17,23,29,41,47,53,187,253,391} agree to sampling noise; for 5|d both are 0.
* The proof is correct: the conditions are one residue class mod 840d, BV with modulus ≤840·x^{1/2}(log x)^{−B}.
  The A⁻ half (S=0, identical data) is all that "parity is necessary" needs, and it is unconditional
  (BV is a theorem); only the A⁺ lower bound inherits W1's dependence on S1–S3.
* Joint version (last sentence of the theorem): the three "wrong" classes indeed have 0 both-clean
  elements (brute force: (−,−) 0/3390, (−,+) 0/3374, (+,−) 0/3417; (+,+) 1262/3309), and
  `(−1)^{Ω₇⁻(n₇)}=(p/7)` holds without exception. **But the joint sieve data are not identical across
  all four classes:** 3 is a window-7 bad prime ((3/7)=−1) and `3 | n₇=(p+7)/4` for *every* p with
  (p/3)=−1 and for *no* p with (p/3)=+1 (brute force: 3390/3390, 3374/3374 vs 0, 0). So
  `|A_{d₁·3}|` distinguishes (p/3)=−1 from +1. See defect M1.

### Lemma 1.1/1.2 (norm-form reformulation) — SOUND
* `scripts/review_w2_norms.py 2e5`: for all n≤2·10⁵ with 3∤n (resp. 7∤n), "no prime factor ≡2 (3)"
  ⟺ primitive representation by a²+ab+b² (resp. "no r with (r/7)=−1" ⟺ primitive rep. by c²+cd+2d²):
  0 mismatches. `n₇=n₃+1`, 3∤n₃, 7∤n₇ for p≡1 (21): correct.
* Note: Lemma 1.2 is about "both F1-clean", which by POINTWISE_WINDOW Lemma 1.1 is *sufficient* for
  a_min≥11 (the converse is only asserted at q=3). The doc only uses sufficiency; fine.

### External citations (§1) — SOUND
* FI09 (archived txt): Thm 2 is conditional on A(θ) for some θ<1 "sufficiently close to 1"; upper
  bound unconditional; semi-linear sieve with level D<√x (their §6–7). Matches the doc.
* Sedunova (arXiv 2609.28200, archived): abstract — FI09 lower bound conditional; unconditional
  asymptotic for square-free distances; ≤7 prime factors via level x^{1/6} of r(n−2)r(n+2). Matches.
* Nath–Xie (arXiv 2501.16723, archived): Thm 1.1 `#{p=m²+n²+1, Ω(p+2)≤9} ≫ x/(log x)^{3/2}`. Matches.
