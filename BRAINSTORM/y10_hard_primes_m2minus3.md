# y10_hard_primes_m2minus3 — two of the hardest primes are m² − 3 next to the T1 point m₀ = 2 (O221)

## Idea
Polynomial T1 points (m₀ with n(m₀) = 1) are cheap generators of primes that are squares modulo every small prime.
Check the campaign's hard lists against p = m² ± small.

## Findings
3361 = 58² − 3, 1 249 921 = 1118² − 3 (m ≡ 2 mod 4 and m ≡ ±2 mod 3, 5, 7), 372 121 = 610² + 21; the other 15 (J)45 hard
primes are at generic distance from squares.

## Literature
(J)45 TRANSPORT_LAW hard list; MODEL_SPECIFIC / PW hard lists (not re-checked here).

## Barrier screen
B5/T1: the family m² − 3 carries T1 at m₀ = ±2; by Thm 3.4, m − √3 being a 2-, 3-, 5-, 7-adic square in ℚ(√3) is what
makes the prime hard for polynomial families too. B6: two primes, no statistics.

## Cheap numerics
Inline (`python3`, isqrt): see NEAR_SQUARE §5.

## Assessment
EVIDENCE (anecdotal, 2/18 at distance 3 where ~0.1 expected). Spark: rank primes by "K-adic square depth" of
m − √j over small |j| and compare with o* / N₋.
