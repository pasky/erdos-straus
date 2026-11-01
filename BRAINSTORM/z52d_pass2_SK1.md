# z52d Pass 2 — batch SK1 (86 items, skip-redo) — summary

Counts: nothing 73 · covered 5 · interesting 5 · needs-compute 0 · skipped 3 (outcomes in data/z52b/pass2/outcome_SK1.jsonl).
Interesting: Z0815 (weak: R-zeros have low h(-4p)/√p, z≈-1.9), Z0833 (U(pq)=U(p)+U(q) inherited exactly, ~88% new),
Z0849 (46 boundary-only (★) primes to 1e8 vs 14 R-zeros, all R-zeros ≡ 1 mod 24), Z0931 (U−D = 2·[p≡3 mod 4] exactly),
Z1035 (mixed divisor counts C=1,D=2 anticorrelated, corr −0.22, no collisions).
ES is OPEN; nothing here is progress on ES itself. Outputs are EVIDENCE/CERTIFIED-by-computation unless labelled Assessment.

## Z0815 — class number proxy vs R-zeros (EVIDENCE, proxy)
- Proxy used: h(−4p) of Q(√−p) (imaginary). NOT the item's Q(√p); that was not computed.
- Corrected (fix round): the 8 R-zeros ≥ 1e5 have mean percentile 0.310 of a random sample of 2000 primes 1 mod 4 in [1e5,1e8] (uniform null 0.5, sd 0.10, z ≈ −1.9). The 6 R-zeros < 1e5 have mean 0.255 among p=1 mod 4 ≤ 1e5. Earlier text (14 R-zeros in the range, z ≈ −2.8) was wrong: 6 of the 14 lie below 1e5.
- Same direction as fingerprint-0121 (corr −0.19 of log(minz/p) with h/√p). Sample is small (n = 8 + 6).
- Caveat: for p ≡ 3 (4), −4p is not fundamental, so h(−4p) there is the class number of the order of conductor 2 (the side correlation +0.49 on p ≡ 3 (4) is for that object).
- Reproduce: `scripts/z52d_p2_SK1_hneg.c` (h for p ≤ 1e5), `scripts/z52d_p2_SK1_hneg_list.c` (+ sample list), `scripts/z52d_p2_SK1_hneg_corr.py`; data `data/z52b/pass2/SK1/Z0815_*`.
- Side result: corr(resid log U(p), resid log h(−4p)) = +0.15 on p ≡ 1 (4), +0.49 on p ≡ 3 (4) (p ≤ 1e5).

## Z0833 — inherited vs new solutions at odd semiprimes pq ≤ 3·10⁴ (EXACT split)
- Solutions of 4/(pq) with all denominators divisible by q are exactly the scaled solutions of 4/p (and symmetrically for p); the two families are disjoint (all divisible by pq would force 4 = Σ 1/y_i, impossible). So inherited = U(p)+U(q) exactly.
- Over 5706 semiprimes: non-inherited = U(pq) − U(p) − U(q) ≥ 4 always; median 88 % of U(pq) is new; log(new) ≈ 2.73 + 0.19 log U(p) − 0.01 log U(q) + 0.32 log n (p < q).
- Reproduce: `scripts/z52d_p2_SK1_semiprime.py` on `data/z52b/pass2/SK1/Z0833_count4_all_3e4.txt`.
- Next: characterise the new solutions (which denominators are divisible by p or q).

## Z0849 — boundary-only (★) primes (EVIDENCE, certified by computation to 1e8)
- Word census (u,B,C): n = 4CuB − u − B. Boundary-only: R(n) > 0 and every word has u=1 or B=1.
- To 10⁸: 14 R-zeros (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 — all ≡ 1 mod 24), and 46 boundary-only primes (spread over 1,5,13,17 mod 24; 20 are ≡ 5 mod 8).
- Includes 184837 (R=2, Cmin=23105) and 46237 (R=4, Cmin=95).
- Reproduce: `scripts/z52d_p2_SK1_star.c` (args: N out); data `data/z52b/pass2/SK1/Z0849_star_1e8_primes.txt`.
- Next: test whether the 5 mod 8 boundary-only primes acquire interior I3 words.

## Z0931 — exact U(p) − D(p) = 2·[p ≡ 3 (4)] (PROVED here from fingerprint-0229; checked 3244 primes ≤ 3·10⁴)
- Non-distinct solutions are multisets {u,u,v}, u ≠ v, i.e. pairs with 2/u + 1/v = 4/p. By (4u−2p)(4v−p) = 2p² there are exactly two such pairs iff p ≡ 3 (4), none otherwise: ((p+1)/2, p(p+1)/4) and (p(p+1)/2, (p+1)/4).
- Hence the orbit formulas O = 6U−6 (p ≡ 3) and O = 6U (p ≡ 1) at all primes, and the 'p > 7' restriction of fingerprint-0266 is unnecessary (p = 3 also satisfies it).
- Reproduce: `scripts/z52d_p2_SK1_isosceles.py` (429 primes ≤ 3000), U−D check on `data/z52b/pass2/SK1/Z0833_count4_all_3e4.txt`.

## Z1035 — mixed divisor counts for C=1, D=2 (EVIDENCE)
- R1(p) = #{d | 4p+1 : d ≡ 3 (4)}, R2(p) = #{e | 8p+1 : e ≡ 7 (8)}, over 4783 primes p ≡ 1 (4) ≤ 1e5.
- Common divisors of 4p+1 and 8p+1 other than 1: none (gcd = 1), so there are no collisions.
- But corr(R1,R2) = −0.22; E[R1R2] = 4.18 vs E[R1]E[R2] = 6.10. Within p mod 24 classes the correlation is −0.07 to −0.13; in both size halves −0.22 and −0.24.
- Reproduce: `scripts/z52d_p2_SK1_fix_mixed.py`. Mechanism not identified; next test against Kronecker-symbol controls.
