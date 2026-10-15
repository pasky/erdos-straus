# y10_below_squares — p = m² − j: polynomial families escape the norm-level T1 (O221)

## Idea
Thm 2.2 (k > 0) dies on positivity of x² + ky². Flip the sign: p = m² − j. Then the same shapes are allowed and give
*escaping* families (witness D(√j) ∉ ℚ) — polynomial ES identities valid on m-classes where n = m² − j is a square
modulo every fixed modulus. Example (j = 8, m ≡ 53 mod 56): a = 1, c = (m + 1)/2, d = (m − 1)/2, f = 7,
b = (2m² + m − 15)/14, e = (2m − 1)/7, (x, y, z) = (abd·n, acd, bcd) (ET Type I map); m = 53 gives b = 404, e = 15 and
4/2801 = 1/29421704 + 1/702 + 1/283608 (checked exactly); the class
contains m = −3 + 56·L·t, for which n ≡ 1 (mod L).

## Literature
ET §10 (linear families only); no reference found for quadratic-family ES identities in m (web search not done —
Assessment: folklore-level for single identities, the sterile-set statement appears new).

## Barrier screen
B1: a polynomial covering is B1-type, but on a *thin* family it is not forbidden by Mordell–Schinzel; (J)3 concerns
two-variable forms. T1/B5: the T1 points of the family (m₀² − j = w², m₀ > √j) are never covered (Thm 3.3), and the
whole K-adic square set Z_K⁺ is sterile (Thm 3.4). B6: statements are about whole m-classes.

## Cheap numerics
`ns_polyfam.py -8 3` → 80 families (76 with n ≡ 1 mod 4 classes), 0 cover m ≡ 3, 8 cover m ≡ −3 (mod 8064);
`ns_padic_cover.py -8 8064`: uncovered = Z_K⁺ exactly (K = ℚ(√2)).

## Assessment
PROVED existence + PROVED obstructions; the exact sterile set is CONJECTURE Y10-S. This is the cleanest instance in the
campaign of the "archimedean anchor" ((J)52): the sign of k decides whether a moving-modulus family can exist.
