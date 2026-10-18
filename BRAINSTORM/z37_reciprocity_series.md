# z37 — A reciprocity singular series for the five-slice count (O267)

## Idea
Write a main term for N₋(n) that vanishes at squares and test it near squares ((J)53/(J)55 deficits).

## Literature
THREE_SQUARES (clean levels, coin model), NEAR_SQUARE §5 (gradient; open spark S2), UNFORCED_WORDS; QUESTION_R §3.

## Content
Level-t slice words = divisors d ≡ −1 (mod t) of tn + 1 with χ_t(d) = −1, χ_t a character mod 4t. Reciprocity model
M_R: divisors equidistribute within their χ_t-class; level factor ∝ τ(N_t) − S_t(N_t), S_t = Σ_{d|N_t} χ_t(d) ≥ 0
("divisors minus quadratic-form representations"), zero exactly at clean levels; M_R(m²) = 0.
EVIDENCE (levels ≤ 3000, n ≈ 10⁶): generic N₋/M_R = 1.05; near-squares m² + K (K = 1, 4, 8, 16, 24) 0.89–0.97; M_R
removes ≈ 35–55 % of the deficit left by the congruence model M₀. The analytic family average (bias ∝ L(1, χ_{tK+1}))
is refuted: Spearman |ρ| ≤ 0.14, no effect.

## Barrier screen
B6/B2: the model is computed from the factorisations themselves; the unexplained part is the admissibility correlation
(B2). T1: exact. B3: no lower bound.

## Cheap numerics
`scripts/z37_rss.c`, `z37_rss_sets.py`, `z37_rss_analyse.py`, `z37_level_L.py`.

## Assessment
New heuristic object (EVIDENCE); partial explanation of the near-square deficit; the residual points to two-side
(t and u/v) cleanliness, which a one-side model cannot see. No route.
