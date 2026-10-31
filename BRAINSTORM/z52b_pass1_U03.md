# z52b Pass 1 — batch U03 (207 items)

Summary (fix round applied): nothing 130 · skipped 58 · covered 9 · interesting 5 · needs-compute 5 (total 207).
Interesting: Z0738 (m/p failures are 5-smooth-neighbour enriched ×13–33), Z0789 (τ(p+1) correlates with R_K after size/class detrending, ρ≈0.30),
Z0940 (two OEIS bilinear families cover 94% of primes ≡1 mod 4 ≤1e5; uncovered density 5.8%→4.3% to 1e7), Z1562 (joint failure of C=1,2 is 9σ below independence),
Z2051 (number of representations p=x²+ny², n≤100, anti-correlates with R_K, ρ=−0.24).
Caveat: 58 items remain `skipped` (analytic/proof-architecture or vague items without a finite test); see outcome_U03.jsonl. Proxy: R_K(p)=Σ_{C≤100} #{d|4Cp+1, d≡−1 mod 4C} (FRONTIER §2.1 divisor form, truncated at C≤100).

## Z0738 — m/p failures and 5-smooth neighbours (interesting)
Exact solver (scripts/z52b_p1_U03_exact.py, 100000) for 1/x+1/y+1/z = m/p; m=4 gives 0 failures (solver sanity check).
Failures p≤1e5: m=12: 18, m=15: 23, m=20: 58, m=24: 139 (item quotes 22/63/146; definition differs).
Fraction with p−1 or p+1 5-smooth: 0.61 / 0.48 / 0.38 / 0.23 vs 0.019 for all primes (ratio 33/26/21/13); 7-smooth ratios 17/18/15/10
(scripts/z52b_p1_U03_smooth.py). Next: condition on p mod 4m and mod 840 to see whether this is just a residue-class effect.

## Z0789 — shift spectrum of τ(p+s) (interesting)
Spearman(log1p R_K(p), log τ(p+s)) over primes ≤1e5: s=1 ρ=0.44, s=4 0.20, s=2,3,12 ≈ 0.
After size detrending (log p, log²p) and class-mod-840 removal: s=1 0.30, s=2 0.14, s=3 0.10, s≥4 ≈ 0 (scripts/z52b_p1_U03_controls.py).
Candidate mechanism: pair form p ≡ −(u+B) mod 4uB ties divisors of p+1 to u+B ≡ 1 (mod m). Next: split R(p) by (u+B) mod m for m | p+1.

## Z0940 — OEIS bilinear families (interesting)
A213340 (5+8t+12k+16kt) and A213686 (13+20t+24k+32kt), names fetched from oeis.org. Union covers 4506/4783 primes ≡1 (mod 4) ≤1e5 (94.2%).
Uncovered density by sieve (scripts/z52b_p1_U03_bilinear_sieve.py): 5.3% (1e4), 5.8% (1e5), 5.1% (1e6), 4.3% (1e7), decreasing slowly.
10 of the 11 R_100-zero primes ≤1e5 are uncovered, and 267 other uncovered primes have R_100>0.
Next: check whether the uncovered set coincides with a known line (B1_LINE b=1 / (★)), and fit the density decay.

## Z1562 — joint failure of C=1 and C=2 (interesting)
P(S_1 ∧ S_2) = 0.0983 vs product 0.1347 over primes ≤1e5 (C≤100), about 9σ deficit; same sign for p≡1 (0.095) and p≡5 (0.102) mod 8.
Other pairs: (1,4) 0.214 vs 0.180 (+), (2,4) 0.341 vs 0.368, (1,3) 0.168 vs 0.173, (2,3) 0.344 vs 0.354. Triple (1,2,3): 0.060 vs 0.091.
Reproduce: scripts/z52b_p1_U03_analyse.py, scripts/z52b_p1_U03_extra.py. Next: random-integer control replacing 4p+1, 8p+1 by independent integers of the same size and class constraints.

## Z2051 — representations p = x²+ny² (interesting)
For each prime p≤1e5 count n≤100 with p = x²+ny² (mean 21.2). corr with log1p R_K = −0.236 (scripts/z52b_p1_U03_final2.py).
Caution: likely driven by Legendre symbols (−n/p) and size. Next: control for log p and for (−n/p) before reading as signal.

## Reproduction
core/feat/analyse/extra/batch2/batch3/final/final2/skipped_fix/exact/smooth/bilinear/composite/controls/fn/m8/twistrank/rough scripts in scripts/z52b_p1_U03_*.py; data in data/z52b/pass1/U03/ (≈2.3 MB).
