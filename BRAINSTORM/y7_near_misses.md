# y7_near_misses — is 7's failure-free record lottery luck? (O215, goal (c))

## Idea
A mechanism with a positive margin (f₇ ≥ 2) would keep f₇ away from 1; a bare existence mechanism (f₇ ≥ 1) would not
be visible this way (R-O215 D7). If it is luck, f₇ should drop to 1 at a few primes, at the same rate at which siblings drop to 0 or 1. Count the near misses.

## Data (complete counts, `ms_census M 3 c X` (MODEL_SPECIFIC engine, every solution re-verified in 128-bit);
`scripts/y7_lowcounts.py`; regenerate with `ms_census M 3 c X > /tmp/y7_cnt_M.txt` (gcc -O2 scripts/ms_census.c), then
`awk '$2<=1' /tmp/y7_cnt_M.txt` for the lists; M = 4–7 to X = 3·10⁵, M = 8 to ≈ 2.2·10⁵ (run cut by timeout), M = 9–13 to 3·10⁴)
Primes p ≥ 11 with f_M(p) ∈ {0, 1} (p = 3, 5, 7 excluded: size-trivial failures):
| M | f = 0 | f = 1 |
|---|---|---|
| 4 | — | — (min f = 6 on 11 ≤ p ≤ 3·10⁵; f(5) = 2) |
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
primes with f ≤ 1; a crude exchangeable model gives (34/52)³ ≈ 0.28 for none of them being a 0. 11 (one zero, seven ones) is the same
lottery with a worse draw. So **7's failure-free record is consistent with a crude lottery model** (about a 1-in-4 event
given its near misses; pooling different M and ranges as independent is not a calibrated model), matching MODEL_SPECIFIC §5.3 (expected 1.6–3.0 failures, almost all at p < 100). For 4 the counts are
larger at every small p (min f = 6 on 11 ≤ p ≤ 3·10⁵, no f ≤ 5 on 100 < p ≤ 3·10⁵), so 4's record needs less luck than 7's; MODEL_SPECIFIC
§5.3 already put 4's at P ≈ 0.23–0.43 on its own curve.
Caveat: the conditional ratio ignores the dependence of f on p and M; it is a calibration, not a fit.

## Barrier screen
Not a mechanism; it is the B2 lottery measured at its low tail. It refutes any structural input that would make
f₇(p) ≥ 2 at all primes (f₇ = 1 three times); it says nothing against an input giving f₇ ≥ 1.

## Assessment
EVIDENCE (complete counts) + Assessment. **Answer to goal (c): consistent with luck.** f₇(p) = 1 at 43, 127, 211 rules
out a mechanism giving f₇ ≥ 2; it does not exclude a mechanism giving f₇ ≥ 1 or one valid beyond a threshold. The data
are explained by count size and where the hard primes are (class of one, y7_mordell_levels) without any hidden input.
