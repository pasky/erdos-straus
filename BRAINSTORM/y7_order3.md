# y7_order3 — the order-3 slices of 4 and 7 and cubic residue patterns (O215, goal (d); O212 spark 3)

## Idea
For 4, p ≡ 1 (mod 12) has two e = 3 slices, N_II = (p+3)/4 and N_I = (3p+1)/4; both fail iff all their prime
factors are ≡ 1 (mod 3) (O212 §3.2: 9.1 % below 10⁶). For 7 the analogous slices sit at p ≡ 1 (mod 7) with e = 6
(both types: e ≡ −p ≡ −p⁻¹ ≡ 6 mod 7); (ℤ/6)^* = {±1}, so the e = 6 slice fires iff the (odd, 3-free) N has a prime
≡ 2 (mod 3). O212 spark 3 asks whether the double failure is a cube-residue pattern in ℚ(ω).

## Facts
* (PROVED) For M = 7, p ≡ 1 (mod 7): if p ≡ 2 (mod 3) then N_II = (p+6)/7 ≡ 2 (mod 3), so the e = 6 slice fires.
  Double failure needs p ≡ 1 (mod 21) (a necessary congruence; only 27.8 % of these primes doubly fail). There N_II ≡ N_I ≡ 1 (mod 3), both odd and prime to 3.
* (PROVED) For M = 4 the e = 3 slice with N even always fires (b = 2 ≡ −1 mod 3, a = 1). This is why 4's double-failure
  rate is lower: 7's N are always odd.
* Double failure ⟺ N_II and N_I are both norms of primitive elements of ℤ[ω] (all primes split in ℚ(ω)).

## Computation (`scripts/y7_order3.py 1000000`)
| M | primes considered | double failures | rate |
|---|---|---|---|
| 4 | p ≡ 1 (12), 19 564 | 1 771 | 9.05 % |
| 7 | p ≡ 1 (21), 6 530 | 1 817 | 27.8 % |
Split by the Boolean indicators "2, 3, 7 is a cube mod p" (8 cells each; the two nontrivial values of each cubic
character are merged, so this is not a test of the full characters): the rates are 8.3–9.3 % (M = 4) and
25.4–30.7 % (M = 7). Every cell is within ≈ 2σ of the mean; the cells have 207–5 824 primes. **No detected association with these indicators.**

## Reading
Each N is ≈ ep/M or p/M, so its event "all primes ≡ 1 (mod 3)" has probability ≍ (log p)^{−1/2} (Landau–type, the
multiplicative function supported on split primes). Heuristically (independence of the two
shifted-prime events, not proved) the double failure has probability ≍ 1/log p. This is the same law as for 4, with a larger constant for 7 (odd N). The cubic characters of
small primes mod p are independent of it. That is expected: "all primes of N split in ℚ(ω)" is a property of
N = (p + e)/M, not of p in ℚ(ω).

## Barrier screen
B2/B3: these are single e-slices with a polylog survival law. B1: "both e = 3/e = 6 slices fail" is not a congruence
class. Nothing passes.

## Assessment
EVIDENCE (negative): no detected cube-residue association, for 4 or for 7. The PROVED part: 7's e = 6 slices can only
doubly fail at p ≡ 1 (mod 21), a necessary congruence (not a sub-core of n ≡ 1 mod 105: 43 is a double failure). The 28 % double failure at p ≡ 1 (mod 21)
is consistent with near misses like 43, 127, 211 (all ≡ 1 mod 21), where the e = 6 slices fail and e = 13, 27, 69
rescue.
