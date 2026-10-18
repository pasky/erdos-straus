# z44_one_mute_odd — one mute prime with free exponent is a finite covering (O276)

## Idea
Which ingredient made odd k trivial: the size of Q's range or the dropped parity? Restrict den z to powers of ONE prime q
(free exponent). Compare with ES^{({q})} (even exponents), an Artin-type open problem ((J)28).

## Literature
Artin's conjecture in progressions: Lenstra, Invent. Math. 42 (1977) 201–224 (GRH); Heath-Brown, Quart. J. Math. 37
(1986) 27–38 (unconditional for all but ≤ 2 primes, no specific q). Function-field analogue: Bilharz (1937), used in FF_MUTE.

## Barrier screen
T1 absent (odd exponents); B1 coverings therefore allowed and found. With parity: T1 + an n-dependent Chebotarev
condition on top of Artin — B2/B6 style lottery at fixed q.

## Cheap numerics
`scripts/z44_one_mute.py 1000000 1000000`: every prime q ≤ 10⁶ has a witness (q ≡ 3 (4), q ≡ 2 (3), or a prime
g ≡ 3 (4) with q primitive root, least g ≤ 179); q = 13, g = 11 solves all primes ≤ 10⁶ and odd squares, exponent ≤ 9.

## Assessment
PROVED per q (POWER_LADDER_ES Thm 5.1), CERTIFIED for all q ≤ 10⁶, CONDITIONAL (GRH, Lenstra) for all q. The parity
normalisation is the entire gap between a finite covering and an open Artin problem at one mute place (Prop 5.2).
