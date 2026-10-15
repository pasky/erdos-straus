# z16_mahler_points — algebraic T-adic Liouville points as explicit sterile candidates (O241)

## Idea
By z16_liouville_spectrum, a point protected from balanced non-exact tuples (R248 repair D5: exact tuples need separate analysis) at almost all levels must be T-adically Liouville. In
characteristic p such points can be *algebraic* (Mahler 1949): u = 1 + cT + Σ_{n≥1} T^{9^n} satisfies an Artin–Schreier-type
equation u⁹ − u = (1 + cT)⁹ − (1 + cT) − T⁹, and its truncations (height 9^n) agree with u to order 9^{n+1}: protected on
(3·9^n, 9^{n+1}], unprotected on (9^n, 3·9^n]. Candidates for explicit points of O(3, T²) beyond rationals, with an algebraic
handle (the Frobenius relation of z16_frobenius) that a rational point lacks.

## Literature
Mahler, Canad. J. Math. 1 (1949); Lasjaunias, Monatsh. Math. 130 (2000); Osgood, Effective bounds on the "Diophantine
approximation" of algebraic functions over fields of arbitrary characteristic, J. Number Theory 7 (1975) 66–80; Christol's
theorem (Christol–Kamae–Mendès France–Rauzy, Bull. SMF 108 (1980)).

## Barrier screen
In the unprotected windows the point is generic-looking (thirds corner allowed), so B3 returns there; the windows have
relative length 2/9 of each 9-adic scale, i.e. a positive proportion of levels — not a thin set. Faster-growing exponents
(u = Σ T^{p^{n²}}) shrink the windows' proportion to 0 but lose algebraicity. Single-point lottery in any case (B6 does
not apply: pointwise).

## Cheap numerics
`scripts/z16_points.py`: alive status to depth 9 of 1 + cT + T⁹ (+T⁸¹) and 1 + cT + T³ + T⁹ + T²⁷ (STERILE_DIOPHANTINE §6).

## Assessment
Assessment / spark. Explicit candidates; no proof mechanism beyond the polynomial case.
