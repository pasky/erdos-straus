# z18_primes_slices — the 2-adic-valuation parameter: the exponential ladder made positive-density, and why it collapses (O245)

## Idea
The mechanism behind O240 Thm B/C is a parameter Y with Y → 1 at odd places and Y → 0 at 2. At every odd n there is one:
Y = 2^{v₂(n−1)}, u = (n − 1)/Y, n = 1 + Yu; the exponential families are the slices u = c₀, and {v₂(n − 1) ≡ 0 mod L} has
positive density (also among primes). Could identities polynomial in (Y, u) cover all primes near a (J)54-type point?
## Result (MENU_LADDER Prop 7.1, PROVED with narrowed scope)
If a family's valid set contains a FULL slice progression (Y fixed, n in a progression), it is polynomial in n there; near a unit-square point every
such slice class contains odd squares, where Type I/II solutions do not exist (ET Prop 1.6). So (n, Y)-polynomial families
can escape Schinzel only where u is frozen or thin, i.e. on density-0 sets (MENU_STERILITY Prop 5.1).
## Literature
ET 2013 p. 7–8 (Mordell/Schinzel), Prop 1.6.
## Barrier screen
B2/B6 respected: the only parameters left at all primes are divisor data (B2 lottery) or norm-form data (T1 on
square-compatible classes, (J)3).
## Cheap numerics
None needed (the slice class contains 1 + 2^e c₀ ≡ 4^J mod M; squares ≡ 1 mod 8 at 2).
## Assessment
Prop 7.1 PROVED (full slice progressions only). "The ladder stops at the first positive-density rung" is Assessment
(R-O245: arbitrary auxiliary functions are not covered; the B2/norm-form dichotomy is a reading, not a theorem).
