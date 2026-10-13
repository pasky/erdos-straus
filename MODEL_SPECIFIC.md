# MODEL_SPECIFIC — what makes 4/n special among m/n? (task O197, spark relay R, after B7)

Status: in progress (O197). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on TES_FINITE.md §5 (O194: Schinzel 8/n has the same ℚ-surface, real anchor and order-2 T1 as ES, no BM
obstruction at 131, 241, yet no solution there — barrier B7), BRAINSTORM/ident_numerators.md (O145),
POINTWISE_MN.md (Jacobi lemma for 4 | m), DEDEKIND_ES.md (five HJ slices), FIXED_MODULUS_SHOTS.md (certificate cube).
Scripts `scripts/ms_*`, data `data/ms/`.

Notation. f_m(n) = #{(x, y, z) ∈ ℕ³ : x ≤ y ≤ z, m/n = 1/x + 1/y + 1/z}. "m fails at n" ⟺ f_m(n) = 0.

## 0. Iteration log
(R1) Literature first: the large-m picture is Pomerance–Weingartner (PW, arXiv:2511.16817, in sources/): a first-moment
count gives mean ≍ (log p)³/m; failures exist for all large m. Their Table 1 lists all failures for m ≤ 15 up to
10¹²–10¹⁸. So "why do 4, 5 have no failures while 8 fails at 241" has a first, purely quantitative answer (mean ∝ 1/m)
that must be separated from any structural one. Plan: measure the structure that survives normalisation by the mean.

## 1. Censuses (CERTIFIED by complete search; cross-checked against PW Table 1)

Engine `scripts/ms_census.c` (written from scratch): x ≤ y ≤ z, n/m < x ≤ 3n/m, A = mx − n, B = nx reduced by
g = gcd(A, B), (A'y − B')(A'z − B') = B'², all divisors d ≤ B' of B'² with d ≡ −B' (mod A'); every solution is
re-verified in 128-bit integers ((mxy − ny − nx)·z = nxy). Complete for every n (Prop 1.1 of TES_FINITE).
Checks: 4/131 = 32, 4/241 = 8, 8/127 = 23, 8/239 = 58 solutions (TES_FINITE's numbers); m = 12, all n ≤ 3000: the
19 failures of PW Table 1 below 3000.

**Failing primes p ≤ 10⁸ (m ≤ 20, m = 24; `data/ms/prime_fail_1e8.txt`; m = 21–23 to 10⁷ in `prime_fail_1e7.txt`).**
| m | # failing primes | largest failing prime ≤ 10⁸ | | m | # | largest |
|---|---|---|---|---|---|---|
| 4 | 0 | — | | 15 | 23 | 20521 |
| 5 | 0 | — | | 16 | 37 | 83449 |
| 6 | 0 | — | | 17 | 16 | 2081 |
| 7 | 0 | — | | 18 | 47 | 35281 |
| 8 | 5 | 241 | | 19 | 15 | 353 |
| 9 | 3 | 19 | | 20 | 62 | **2763601** |
| 10 | 7 | 181 | | 21 | 26 | 14051 (≤10⁷) |
| 11 | 2 | 37 | | 22 | 53 | 14543 (≤10⁷) |
| 12 | 20 | 12241 | | 23 | 45 | 31771 (≤10⁷) |
| 13 | 9 | 281 | | 24 | 154 | 620929 |
| 14 | 8 | 353 | | | | |
Agreement with PW Table 1 (prime entries, m ≤ 15) is exact. New here (to my knowledge; PW stop at 15): m = 16–24 lists;
m = 20 fails at the prime 2763601 ≡ 1 (mod 840), after a gap from 90001.
**T1 control (odd squares k² ≤ 10⁸, gcd(k, 2m) = 1):** all solvable for m = 4–11, 13, 15; exceptions 25 (m = 12),
841 = 29² (m = 14), 9, 121 (m = 16) — all in PW's table or small. (Squares are solvable by "other-shape" solutions.)

**Observation 1.1 (EVIDENCE).** The multiples of 4 have far longer failure tails than their neighbours:
last failure 241 (m = 8) vs 2 / 19 (m = 7, 9); 12241 (12) vs 37 / 281 (11, 13); 83449 (16) vs 20521 / 2081;
2763601 (20) vs 353 / 14051; 620929 (24) vs 31771 (23). Among m ≡ 0 (mod 4), m = 4 is the only one with no failure.
