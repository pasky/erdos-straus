# s6_exp_classes_primes — can algebraic budget-forcing reach primes? (O238; steering after the 105 result)

## Idea
The 105 proof works because K = (n_s + m)/4 carries a moving algebraic factorisation. For primes p, ask for a window m
such that (p + m)/4 is a value of a polynomial with a forced factorisation, e.g. (p + m)/4 = F(u)G(u). Then p = 4F(u)G(u) − m
is a polynomial in u: the prime p must lie in a fixed polynomial family.
**Observation (PROVED, elementary).** Lemma 1.0's identity is an ES identity on the polynomial family n = 256u³ + 105,
u ≡ 32 (mod 151); generally every exponential class is a polynomial family in a root parameter u. For a fixed finite set of
such families, the primes covered have density 0 (polynomials of degree ≥ 2) — B1 (POINTWISE_SIZE Thm M analogue: finite
menus of families) — and at T1 the families avoid squares only globally (s6_mixed_points_cuberoots).
So algebraic budget-forcing is family-specific (H-A on thin families), and for a single prime p it is the B2 event
"(p + m)/4 has a divisor pair in the right class".

## Literature
NEAR_SQUARE Thm 2.2 (polynomial families on m² + k); Bunyakovsky/Schinzel H for primes in cubic families.

## Barrier screen
B1 (finite family menu), B2 (single p). T1 fine.

## Cheap numerics
`scripts/s6_expwin105.py 105 120 12 1`: on the family itself exp + small-prime windows give cap 0 at 105/116 exponents; nothing
analogous is definable for a generic prime.

## Assessment
Negative with exact reason: the non-formal input (a moving algebraic factorisation) exists only on thin families.
