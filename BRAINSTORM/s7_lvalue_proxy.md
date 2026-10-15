# s7_lvalue_proxy — least window vs L(1, χ_p): hardness is "quadratic-residue richness" (O247, (i)/(v))

## Idea
If m₀(p) (least cap-0 window, s7_window_lottery) is governed by congruence data, the natural single analytic invariant is
the Euler product P(p) = ∏_{ℓ ≤ 200} (1 − (p/ℓ)/ℓ)^{−1}, a proxy for L(1, χ_p) = h(p)·log ε_p/√p (class number ×
regulator of ℚ(√p)). Test whether m₀ correlates with it, beyond the Mordell-hard / non-hard split.

## Literature
Mordell's classes (p a square mod 3, 5, 7, 8); Elsholtz–Tao §1 (Mordell-hard primes are QR-rich); Granville–Soundararajan
(distribution of L(1, χ)); s7_window_lottery (shuffle test).

## Barrier screen
B6/B1: a correlation with an L-value is an average statement about congruence data; it cannot certify a single p.
It is useful only as a dictionary: ES-hardness of p ≈ "χ_p looks like the trivial character on small primes", i.e. the
same data that makes L(1, χ_p) and h(p) large (and that defines the r-generic lines of (J)70).

## Cheap numerics (scripts/s7_gauss_lvalue.py)
Primes p ≡ 1 (4) ≤ 10⁶: Spearman(m₀, P) = 0.349 overall, 0.197 inside the six Mordell-hard classes (2 370 primes)
(average ranks for ties; the first version used tie-breaking by order and reported 0.199 / 0.226 — R-O247 review fix).
Moderate and positive, as the congruence picture predicts (the shuffle test of s7_window_lottery already shows that the
congruence data account for the inter-window correlations).

## Assessment
EVIDENCE, Assessment. A clean dictionary (hard ⇔ large L(1, χ_p) on the small-prime part), no mechanism. Spark (not
pursued): primes with record L(1, χ_p) (Montgomery–Vaughan extreme values) as natural test points for m₀ records.
