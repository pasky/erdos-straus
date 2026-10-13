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

## 2. 8/n is the all-even half of 4/n (PROVED, elementary) — the "parity sub-lottery"

**Lemma 2.1.** Let n be odd. (a) Every solution of 4/n = 1/x + 1/y + 1/z has either all of x, y, z even or exactly one
of them odd. (b) (x, y, z) ↦ (2x, 2y, 2z) is a bijection from the solutions of 8/n onto the all-even solutions of 4/n;
hence f_4(n) = f_8(n) + f_4^{odd}(n), f_4^{odd} := number of solutions with exactly one odd denominator.
(c) For a prime p ∤ 6 in ET/PW coordinates (Type I: x, y, z = abdp, acd, bcd, 4abd = pe + 1, a + b = ce; Type II:
abd, acdp, bcdp, 4abd = p + e, a + b = ce; a, b, c pairwise coprime) a solution is all-even ⟺ d is even.
*Proof.* (a) v₂(4/n) = 2. Three odd denominators: the sum has odd numerator over odd denominator, v₂ = 0. Two odd
(x, y), z even: v₂(1/x + 1/y) ≥ 1 > −v₂(z) = v₂(1/z), so v₂(sum) = −v₂(z) < 0. (b) 8/n = Σ 1/u_i ⟺ 4/n = Σ 1/(2u_i).
(c) If d is even all three are even. If d is odd, all-even needs two of a, b, c even (each denominator is a product of
two of a, b, c times d, p odd), impossible for pairwise coprime a, b, c. (Pairwise coprimality: PW Prop 2.1/2.3
proof, a = gcd(x′, y′) etc. with gcd(x′, y′, z′) = 1.) ∎
EVIDENCE (`ms_census` parity filter): the all-even filter of 4/p reproduces the 8/p failure list {3, 11, 17, 131, 241}
exactly (p ≤ 10⁵), and per prime f_4^{even}(p) = f_8(p) for all 2261 primes ≤ 2·10⁴ (0 mismatches); 2 or 3 odd
denominators: 0 solutions at every prime. The all-even share of ES solutions is 0.444 (p ≤ 2·10⁴), 0.448 on
(10⁴, 2·10⁴]. **The one-odd sub-lottery alone never fails: f_4^{odd}(p) ≥ 1 for every prime 3 ≤ p ≤ 10⁸ (5 761 454
primes), and every odd square ≤ 10⁸ has a one-odd solution and an all-even one.** (For p ≡ 3 mod 4 this is trivial:
e = 1, x = (p+1)/4; the content is p ≡ 1 mod 4.)
*Reading.* ES(p) = [8/p] ∨ [one-odd 4/p]. At 131 and 241 ES lives entirely on the one-odd half (32 and 8
solutions). The sibling 8/n is not a "different equation with the same surface", it is literally a sub-lottery of ES
at the same n (d even), of about 45% of ES's mean, and B7 says this sub-lottery has non-T1 failures. The parity split
is m-specific (for m = 8 the analogous decomposition is into 16/n and the rest).
