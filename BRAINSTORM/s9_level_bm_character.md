# s9_level_bm_character — BL's Brauer class in Theorem-K coordinates is χ_{−t} (n ≡ 1 (4); −χ_t for n ≡ 3 (4) — R282 repair), and the BM layer is free at every non-square (O271, mandatory (ii))

## Idea
O268 Thm 1.1 (now (J)100): in pair coordinates (fix (u, B), sum over C) BL's class is χ_{−4uB} evaluated at p. O269 Thm K (under
review): in level coordinates (fix t, sum over divisors of tn + 1) the count is an even + odd character divisor sum mod t. Which
character mod t is BL's class? Answer: the odd quadratic character χ_{−t} (4 | t), paired with the principal character. Then try
to turn the BM layer into an explicit positivity statement.

## Literature
O269 Thm K (Kronecker double series; Weil, *Elliptic functions according to Eisenstein and Kronecker*, Ch. VIII); Dirichlet's
formula Σ_{d|N} χ_D(d) = R_D(N)/w_D for gcd(N, D) = 1; Burgess / Ankeny–Bach for the least prime ℓ with (n/ℓ) = −1;
Bright–Loughran arXiv:1908.02526 Thm 1.8 (no BM obstruction for n ≥ 2).

## Statement (SYNTHESIS_SPARKS9 §2)
* Prop 2.1 (PROVED): D⁻_t(N) ≤ (τ(N) − σ_{χ_{−t}}(N))/2; the {1, χ_{−t}} part of the orthogonality expansion is
  M^{lev}_t(n) = (τ(N) − σ_{χ_{−t}}(N))/φ(t) ≥ 0, vanishing at n = m² since every ℓ | 1 + tm² splits in ℚ(√−t).
* Prop 2.2 (PROVED): ∃ 4 | t with M^{lev}_t(n) > 0 ⟺ n is not a square; witness t ≤ 4ℓ(n), ℓ(n) the least odd prime with (n/ℓ) = −1. (The coset {χ_{−t} = −1}
  still carries the other real genus characters mod t; only χ_{−t} is freed.)

## Barrier screen
B2: the remaining event is the class −1 inside the coset {χ_{−t} = −1} (φ(t)/2 classes) — the divisor-class lottery. T1: respected
exactly (Prop 2.1(c)). Prop 10.3 / genus theme: this is the genus/sign layer, now shown to be pointwise free in Thm-K coordinates.
B3: the BM layer has no polylog main term issue at all (it is a 0/1 existence statement); the size issue sits in the X part.
Numerator models: the same construction (8 | t, t ≤ 8ℓ) works for 8/n, while 8/131, 8/241 fail — the BM layer is numerator-blind ((J)41), as
any mechanism must be screened for.

## Cheap numerics
`scripts/s9_level_bm.py 200000 200` (`logs/s9_level_bm.txt`): 99 776 odd non-squares, 0 witness failures, max ℓ = 71; 223 odd
squares, no level t ≤ 200 with an inert prime factor; the witness level carries an actual (★) word for 72.1 % of n.

(R282 repair) The dictionary itself is SPARKS9 Lemma 2.0 (added by R282): inv_p α at the level points P(t, δ) equals
(−1/p)(−1)^{(δ−1)(p−1)/4}χ_{−t}(δ), i.e. χ_{−t}(δ) for p ≡ 1 (4) but −χ_t(δ) (even) for p ≡ 3 (4); `scripts/review_r282_blevel.py`.

## Assessment
PROVED dictionary (generic points, n ≡ 1 (4); R282 repair) + PROVED (elementary) pointwise statement for the BM relaxation. It answers (ii): the BM class is one odd
character in O_t, and the "explicit Dirichlet coefficient" it gives (τ − R_{−t}/w) is already positive at every non-square —
so no positivity theorem for it can help; Hecke/Eisenstein lower bounds for R_{−t} push against ES. No route.
