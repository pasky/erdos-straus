# y7_split_norm — Hecke angle of π (p = N(π) in ℚ(√−7)) does not see 7's hard slices (O215, goal (a))

## Idea
By y7_free_inert, 7/p is open only at split p = ππ̄, π = x + yθ, θ = (1 + √−7)/2, N(π) = x² + xy + 2y². The ray class
of π modulo q (its "Hecke angle") is finer than p mod q. If the success of 7's hard slices depended on the angle,
7 would have a genuinely quadratic-field input (a Hecke-character fibre), which 8 (hard set not = split set) could
not share. Also: an identity family in the variables (x, y) is not killed by T1/B5 for 7 (7 lacks full T1,
y7_full_t1), unlike for 4, where specialising p = x² + y² at Pythagorean (x, y) hits odd squares.

## Computation (`scripts/y7_split_norm.py 1000000 q`)
Population: p ≡ 1 (mod 21), p ≤ 10⁶ (6 530 primes); event: double failure of the e = 6 slices (y7_order3). Cells:
p mod q × ((x, y) mod q up to ±1 and conjugation (x, y) ↦ (x + y, −y)). χ² of the double-failure rate across angle
cells within each class p mod q:
| q | angle cells used | χ² | expected under "no angle effect" |
|---|---|---|---|
| 4 | 2 | 0.0 | ≈ 0 |
| 5 | 6 | 2.0 | ≈ 2 |
| 9 | 12 | 7.6 | ≈ 9 |
(p ≡ 4 mod 5 has rate 0 for a congruence reason: 5 | (p + 6)/7 and 5 ≡ 2 mod 3.)

## Reading
No angle effect beyond p mod q (EVIDENCE). This is the expected answer: the slice events are factorisation events of
N = (p + e)/7, and p + e has no algebraic factorisation in ℤ[θ] (p + e = N(π) + e is not a norm form in π).
About identities in (x, y): B5 does not kill them for 7, but every such identity covers the profinite closure of
its (x, y)-domain, and (x, y) ≡ (1, 0) gives N ≡ 1 at every level, i.e. the class of one (ident_numerators Lemma 3.1)
is reached. Whether Lemma 3.1 extends to ET-shaped families with polynomial parameters in (x, y) was not proved
(open; Assessment: it should, by specialising at (x, y) → (1, 0) p-adically).

## Barrier screen
B2 (factorisation lottery of p + e); B1 (class of one) for any norm-form identity menu, modulo the open extension.

## Assessment
EVIDENCE (negative). The split-prime reduction gives no Hecke input for the e = 6 slices.
