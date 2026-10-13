# bsE_sierpinski_moving_integer — N_s = q^s p + 1 as a Sierpiński/Riesel family (O178)

## Idea
For fixed p, the integers N_s = q^s p + 1 are exactly the Sierpiński-type family k·2^n + 1 with base q and multiplier
k = p. Sierpiński numbers are certified by *covering congruences*: every N_s has a factor from a fixed finite set of primes.
Could a covering of s (with p in a suitable class) force every N_s to have a divisor pair a ≡ −b (mod q^s)?
## Literature
Sierpiński, Elem. Math. 15 (1960); Erdős's covering systems; Filaseta et al. on Sierpiński/Riesel numbers.
## Barrier screen
For a prime ℓ ∤ qp, ℓ | N_s iff s ≡ −log_q p (mod ord_ℓ q), so small-prime data are periodic in s. They are congruence data
(B1). Fixed divisors a, b serve only s ≤ v_q(a + b) (DEPTH_ASPECT Lemma 1.3). Witnesses at depth s need a factor ≥ q^s/2, i.e.
a large prime factor of N_s (the lottery). T1: n/a.
## Cheap numerics
Covered by `scripts/bsE_qpow.c`: the least successful s is ≤ 7 for every prime ≤ 10⁶ in the family, and failures are
lottery failures with no congruence pattern beyond p ≡ 1 (24) dominance.
## Assessment
COLLAPSES (B1). Covering congruences produce compositeness, not divisors in a class modulo a growing power.
