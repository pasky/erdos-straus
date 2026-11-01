# z52d Pass 2 — batch NC1 (80 items, all Pass-1 `needs-compute`); lint-fix round

Counts (after the lint-fix round): nothing 64 · covered 4 (Z1248, Z1256, Z1263, Z1840) · interesting 2 (Z1438, Z1686) · needs-compute 10 (Z1227, Z1363, Z1391, Z1518, Z1776, Z1797, Z1887, Z1890, Z1894, Z1409) · skipped 0. `scripts/z52d_pass2_lint.py` reports 0 flagged.
Still open for the user's stricter rule ("not tested" = not done): 8 `nothing` records are blocked by source access (Z1435, Z1951, Z1952, Z1564, Z1565, Z1662, Z1637, Z1660); 10 are `needs-compute` with partial results and estimates (listed above). Not merged.

Interesting: **Z1438** (genus obstruction: Type I with d = 1 never occurs for p ≡ 1 mod 4; proof sketch and d-histogram) and **Z1686** (class number vs witness count, residual partial correlation 0.105 after controls).

## Z1438 — Type I and the genus of Q(√−d) (interesting)
* For p ≡ 1 (mod 4), every prime factor of p²+4c² is ≡ 1 (mod 4) or equals p, so every divisor f is ≡ 1 (mod 4); the Type I condition f ≡ −p (mod 4cd) needs f ≡ 3 (mod 4). So d = 1 (ℚ(i)) never gives Type I solutions. Numerically: 0 of 211 primes (c ≤ 20, d = 1).
* With d ≤ 30: every one of the 211 primes has a Type I solution; the smallest d is 2 (110 primes), 3 (34), 5 (32), 6 (10).
* Reproduce: `uv run --with numpy --with sympy python scripts/z52d_p2_NC1_fix3.py` → `data/z52b/pass2/NC1/fix3.json`.
* Next: derive the genus criterion for d ∈ {2, 3, 5, 6, 7} (class number 1) and test on p ≤ 3000.

## Z1686 — class number vs witness count (interesting)
* R(p) = Σ_{C ≤ 50} #{d | 4Cp+1, d ≤ √N, d ≡ −1 (mod 4C)}, h(−4p) by reduced-form count, over 4783 primes p ≡ 1 (mod 4), p < 10⁵.
* Raw Pearson 0.464; given log p and p mod 840: 0.216; additionally given (p/q), q = 11…47: 0.105 (within-class shuffle null sd 0.016).
* Not yet controlled: p mod 9, 16, 25, 49 and (p/q) for q ≥ 53.
* Reproduce: `scripts/z52d_p2_NC1_classnum_partial.py`.

## Other results (main step done; details in data/z52b/pass2/outcome_NC1.jsonl)
* Witness structure (p ≤ 10⁶, all C ≤ 50; `scripts/z52d_p2_NC1_wit.c`): exact gcd lemma gcd(N_C, N_C′) | 4(C′−C); resultant of the two divisor factors is 4(v−u); C-form identity checked on all witnesses; every witness is a quadratic non-residue (Lemma B), so the k = 2 tower is trivial and the quartic character is the only invariant (both values occur for 95 % of primes).
* Learned C-order policy (Z1228): 1.44 tests per prime with class-learned order vs 1.59 fixed. Family entropy (Z1223): H = 1.29 bits, 0.78 given p mod 840.
* Concentration (Z1320): witness points (C ≤ 2, p ≤ 3000) lie on no curve of degree ≤ 6.
* Mahler (Z1309) and k-kernel (Z1377) tests on the witness indicator / C_min: no 2-/3-regular or Mahler relation of the orders tested; controls validate.
* Certificate-size distribution (Z1720): median H = 132, 99th percentile 2411 (p ≤ 10⁶).
* Blind prediction (Z1889): Brier 0.056 (class model) vs 0.078 (base rate).
* Exceptional/first-moment checks: Z1814 (11.63 vs naive 9.87), Z1908 (projected area constant ≈ 0.61), Z1922 (conic bundle, singular fibres at n = 0, ∞), Z1936 (Koszul χ = 0).
* Z1518: Cao–Xu Theorem 2.1 verified for m ≤ 3000 (3000/3000); the 56 solvability polynomials not yet parsed.
* Z1776: ES verified (exact 2-term enumeration) for 4^s+297 (s ≤ 6) and 15·2^s+1 (s ≤ 11); Walnut not run.
* Z1640: Tao 2011 comment thread read (39 comments); distinct ideas listed in the outcome file.
* Z1883: a 2026 arXiv paper (2608.24035) on 'Sieve dimension and search depth for ES, n ≡ 1 (mod 24)' claims an exceptional-set bound and an unconditional obstruction at shift c = 7; read, not verified.

## Blocked by source access (not fixed)
Z1435, Z1951 (Mordell 1969 ch. 30: only chapters 1–29 retrievable), Z1952 (Dickson vol. II: no OCR text), Z1564 (Obláth 1950 not online), Z1565 / Z1662 (Guy UPINT D11 not retrievable), Z1637 (erdosproblems unit-fraction pages not fetched), Z1660 (CUNY survey PDF behind Cloudflare).

## Reproduction
* `gcc -O2 -o z52d_wit scripts/z52d_p2_NC1_wit.c && ./z52d_wit 1000000 50 > /tmp/wit_1e6.txt` (input for the witness scripts).
* Witness-based: `scripts/z52d_p2_NC1_fix_wit.py`, `fix2.py`, `fix3.py`, `fix4.py`, `fix5.py`, `fix6.py`; `ded_es.py`; `kernel.py`; `runs_model.py`; `cmin.c`.
