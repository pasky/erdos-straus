# y7_near_misses — is 7's failure-free record lottery luck? (O215, goal (c))

## Idea
If 7/p never fails because of a mechanism, its count f₇(p) should stay away from 0. If it is luck, f₇ should drop to 1
at a few primes, at the same rate at which siblings drop to 0 or 1. Count the near misses.

## Data (complete counts, `ms_census M 3 c X` (MODEL_SPECIFIC engine, every solution re-verified in 128-bit);
`scripts/y7_lowcounts.py`; M = 4–7 to 3·10⁵, M = 8 to ≈ 2.2·10⁵, M = 9–13 to 3·10⁴)
Primes p ≥ 11 with f_M(p) ∈ {0, 1} (p = 3, 5, 7 excluded: size-trivial failures):
| M | f = 0 | f = 1 |
|---|---|---|
| 4 | — | — (min f = 6 on p ≥ 11; f(5) = 2) |
| 5 | — | — (f(11) = 3) |
| 6 | — | 13 |
| **7** | **—** | **43, 127, 211** (f = 2 at 11, 29, 631) |
| 8 | 11, 17, 131, 241 | 113, 3169, 3361 |
| 9 | 11, 19 | 29, 37, 41, 73, 113, 137, 149 |
| 10 | 11, 43, 61, 67, 181 | 13, 23, 31, 41, 101, 127, 163, 401, 601 |
| 11 | 37 | 13, 17, 23, 67, 101, 331, 631 |
| 13 | 53, 61, 67, 79, 211, 281 | 17, 29, 41, 163, 241, 601, 1097, 1777 |
The single solutions of 7/p: 7/43 = 1/10 + 1/16 + 1/3440, 7/127 = 1/20 + 1/196 + 1/62230, 7/211 = 1/32 + 1/520 + 1/438880
(all Type I, e = 13, 27, 69 — all ≡ 6 (mod 7); the e = 6 slice of p ≡ 1 (mod 7) is empty; `scripts/y7_sols.py`).
All ten S₇-empty primes ≤ 10⁵ (43, 127, 211, 421, 463, 631, 967, 4201, 9661, 12601) are ≡ 1 (mod 42), and six are
≡ 1 (mod 105): they sit in the class-of-one core of y7_mordell_levels. p − 1 is highly divisible in every case
(4200 = 2³·3·5²·7, 12600 = 2³·3²·5²·7).

## Luck estimate (Assessment)
Pooled over M = 8–11, 13 (p ≥ 11): 18 primes with f = 0 and 34 with f = 1, so P(f = 0 | f ≤ 1) ≈ 0.35. 7 has three
primes with f ≤ 1; the chance that none of them is a 0 is ≈ 0.65³ ≈ 0.27. 11 (one zero, seven ones) is the same
lottery with a worse draw. So **7's failure-free record is unremarkable luck** (about a 1-in-4 event given its
near misses), matching MODEL_SPECIFIC §5.3 (expected 1.6–3.0 failures, almost all at p < 100). For 4 the counts are
larger at every small p (min f = 6 on p ≥ 11, no f ≤ 5 above 100), so 4's record needs less luck than 7's; MODEL_SPECIFIC
§5.3 already put 4's at P ≈ 0.23–0.43 on its own curve.
Caveat: the conditional ratio ignores the dependence of f on p and M; it is a calibration, not a fit.

## Barrier screen
Not a mechanism; it is the B2 lottery measured at its low tail. It argues against any hypothetical structural
input that would make f₇(p) ≥ 2 (none exists: f₇ = 1 three times).

## Assessment
EVIDENCE (complete counts) + Assessment. **Answer to goal (c): yes, lottery-lucky.** f₇(p) = 1 at 43, 127, 211 rules
out any mechanism that gives 7 a positive margin. Whatever separates 7 from 8 and 11 empirically is count size
and where the hard primes are (class of one, y7_mordell_levels), not a hidden existence input.
