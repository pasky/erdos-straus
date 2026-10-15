# s6_witness_onesided — the forced character is not necessary for cap 0 at a window (O238; mandatory (iii))

## Idea
Is a cap-0 window the same as "an unforced word with a specific side"? A Type II solution x = abd, y = acdp, z = bcdp has
window m = 4x − p = (a + b)/c; for c = 1 it is the word (t, u, v) = (4d, a, b) of tuv − u − v = p with m = u + v and
4K = N_u + v = N_v + u (three side numbers, (J)58). The square-shot witness (CAP_POINTWISE: (g/n) = (m/n) since
gm = n + 4Q²) suggests "(m/p) = −1 is necessary". It is not, for general d (non-square shots).
**Observation (PROVED, elementary).** At a prime window q the Lemma-1.1 condition d ≡ −K (mod q) puts no constraint on
(q/p) when d is not a square: (d/q) = (−K/q) is matched by the odd-exponent primes of d.
So the forced level is one-sided: (q/p) = −1 forces firing at some cap (R245 repair: under Thm 1.1 (ii) or CAP_DOWN Thm 1.2 (E)/Addendum — n = 5, q = 67 is dead); (q/p) = +1 windows fire by lottery.

## Literature
NEAR_SQUARE Lemma 1.3 (witness f of Type II charts, gcd(n, 2ad) = 1); ET Prop 1.6; (J)58 three side numbers.

## Barrier screen
B2 throughout (cap 0 at either kind of window is a divisor-class event). T1: at squares neither kind fires at any cap (CAP_DOWN §3).

## Cheap numerics
`scripts/s6_witness_caps.py 3000 120 6` (primes p ≡ 1 (4) < 3000, prime windows q ≡ 3 (4) < 120, exhaustive Lemma-1.1 caps):
(q/p) = −1: cap 0 at 561 of 1 655 pairs, dead at cap ≤ 6 for 218; (q/p) = +1: cap 0 at 279 of 1 531 (53 of them with K odd),
dead at cap ≤ 6 for 784. (R246 repair: the pair totals are 1 635 and 1 530 — 15 windows × 211 primes — not 1 655 / 1 531;
rates 34.3 % vs 18.2 %; `scripts/review_r246_witness.py`, which also finds 14 pairs with (q/p) = −1 dead at EVERY cap, all
K even with (E) failing.) So cap-0 rate 34 % vs 18 %: the forced bit roughly doubles the odds and does not decide.

## Assessment
EVIDENCE + small PROVED observation. (iii) answered: a cap-0 window is a c-fibre word with m = (u + v)/c; "forced" is a
property of the window, "cap 0" of the word; they coincide only at m = 3 (s6_unique_forced_cap0).
