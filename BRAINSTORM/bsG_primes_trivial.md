# bsG_primes_trivial — the (W) half of SQ₅ is trivial where ES needs it (O180; SHARP, deflationary)

## Idea
R174 D1: ES at primes needs only (W) at primes p ≡ 1 (4), plus (S). Check how hard (W) is there.

## Result (LORENZINI_W Prop 8.1, Cor 8.2; PROVED)
For n ≡ 1 (4), 3 ∤ n, n ≥ 13: (2, 2, (n+2)/3) if n ≡ 1 (3), and (3, (n+7)/12, 4) if n ≡ 5 (12). Hence (W)(p) for all primes p ≡ 1 (4), p ≥ 13,
and **interior-SQ₅(p) ⟺ (S)(p)**. The (3,·,4) word has sign (3/p) = −1 (the classical p ≡ 2 (3) identity). The (2,2,·) word has sign +1.
So on p ≡ 1 (12) everything rests on (S).
Global (W) residue after this and Lorenzini 6.3: n ≡ 3, 9, 11 (12) with n + 2 prime, and n = 2^m − 2 (m odd).

## Literature
Lorenzini JNT 2024 Prop 6.3 (his (c) covers only n ≡ 1 (4) with n ≡ 2, 8 (9). The (x,z) = (3,4) family covers all of n ≡ 5 (12)). Mordell's ES
identities (classical p ≡ 2 (3) case).

## Barrier screen
Not a barrier result. It removes (W) from the ES path. What remains, (S), is the sign/genus layer, where every known barrier
(T1/B5, B2, Prop 10.3) lives.

## Cheap numerics
`scripts/bsG_primes_W.py` (74 415 primes < 2·10⁶, 0 failures). `scripts/bsG_primes.c 10⁸`: x*(p) ≤ 3 for all primes p ≡ 1 (4) < 10⁸.

## Assessment
PROVED and trivial in hindsight. Its value is directional: **a T1-free (W) cannot serve as a stepping stone to ES at primes.**
Spark relays should target (S) on p ≡ 1 (12) (Mordell's residual classes) directly. Promise for ES: 0 as a route; high as a steering correction.
