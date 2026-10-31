# z52b pass 1 — batch H03 (25 items, complete)

- Outcomes (25 items): covered 13 (Z1140, Z1269, Z1330, Z1336, Z1349, Z1373, Z1378, Z1386, Z1389, Z1400, Z1421, Z1422, Z1455), nothing 12 (Z1117, Z1271, Z1328, Z1332, Z1333, Z1334, Z1371, Z1376, Z1383, Z1387, Z1446, Z1449), interesting 0, needs-compute 0, skipped 0.
- No interesting items. Repo-status corrections: Z1269 (k/n threshold across numerators) is DISPROOF_AVENUES §4 (m = 4…24 ladder to 10⁸), Z1336 is the avoider density δ*(T) of DISCOVERIES (H)7/(H)10, Z1455 is BRAINSTORM/cayley_markoff_cm.md (the surface is the 4-nodal Cayley cubic with 9 lines, not 27); all three were tagged "untried".
- Small PROVED by-products: (Z1271) at primes p ≡ 1 (4) every solution has three distinct denominators, while every p ≡ 3 (4) has a repeated one; (Z1378) every (★) solution has max denominator ≤ n²/2; (Z1449) prime divisors q ≡ −1 (mod 4C) of 4Cp+1 are exactly the (★) triples with 4uC − 1 prime.
- EVIDENCE by-products: (Z1371) C_min(p) has a power-law tail whose exponent grows with log p (1.22 → 1.65 → 1.90 per decade to 10⁸), as the lottery model predicts; (Z1446) dead (★) levels split 14% ω ≤ 1 / 28% BM character / 28% other real characters / 3% higher order / 27% subset-product, with the same mix at the hardest primes; (Z1449) prime-divisor certificates number ≈ 0.55 log p, with 0.8% zeros.
- Records: data/z52b/pass1/outcome_H03.jsonl; scripts scripts/z52b_p1_H03_*; data data/z52b/pass1/H03/.

## Notes (not "interesting"; recorded for reproducibility)

**Engine.** `scripts/z52b_p1_H03_certs.c` (`gcc -O2 -o /tmp/h03certs …`; `/tmp/h03certs p`) prints every (★) triple
(u, B, C) with 4uBC − u − B = p. It is used by the TDA, arcsine, SAT-avoid and prime-certificate scripts.
`scripts/z52b_p1_H03_rcount.c LO X` gives R(p) for all primes p ≡ 1 (4) in [LO, X] (3·10⁵ in 11 s).

**Z1371: C_min tail.** `scripts/z52b_p1_H03_cmin.c X CMAX [LO]`: C_min(p) = least C with a divisor d ≡ −1 (mod 4C) of
4Cp + 1, trial divisors d = 4Ck − 1 ≤ √N.
* All p ≡ 1 (4) ≤ 10⁸ (2 880 504 primes) in 9 s. The run fails exactly at the 14 (★)-sterile primes of the census
  (409 … 8 813 281), which serves as a cross-check. The record is C_min = 41 027 at p = 85 664 329.
* P(C_min > 2^k), k = 0…10: 2.1e-1, 6.8e-2, 2.5e-2, 6.0e-3, 1.7e-3, 4.5e-4, 1.4e-4, 5.1e-5, 2.0e-5, 8.3e-6, 4.9e-6
  (`data/z52b/pass1/H03/cmin_1e8.txt`; by decade in `cmin_by_decade.txt`).

**Z1446: anatomy of a dead (★) level.** `scripts/z52b_p1_H03_failclass.py 100000` (19 s) →
`data/z52b/pass1/H03/failclass.json`. G = (ℤ/4C)^×, H = ⟨primes of N⟩. A "BM" failure means (−C/q) = +1 for every
q | N. "Other real" means −1 ∉ H·G², but not via χ_{−4C} alone.

**Z1449: prime-divisor certificates.** `scripts/z52b_p1_H03_primecert.py`. The mean count / log p is 0.556, 0.532 and
0.576 at 10⁵, 10⁶ and 10⁷ (250 primes each). The share of primes with no prime-divisor certificate is 0.8% at 10⁵ and
10⁶, and 0 of 250 at 10⁷.

**Z1378: n² bound.** `scripts/z52b_p1_H03_n2bound.py`: the 14 (★)-sterile primes have Type II solutions (c ≥ 2) with
max ≤ 0.503 n². The worst is p = 577, at (a, b, c, d) = (1, 5, 2, 29).
