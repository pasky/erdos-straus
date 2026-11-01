# z52d Pass 2 — batch TO3 (101 "touched" items, never worked in Pass 1)

- Counts: nothing 92 · interesting 9 · covered 0 · needs-compute 0 · skipped 0 (101/101 input lines have one outcome in `data/z52b/pass2/outcome_TO3.jsonl`).
- Interesting: Z0700 (residual ρ(U, log ε_p) = −0.51), Z0719 (Mordell class order reproduced), Z0729 (ES_k ladders keep failing past 10⁵), Z0781 (Poisson-with-M_BM zero model fails by ~100×), Z0824 (mod-3 weight split only half explained by (−3/q)), Z0827 (L-exponent sign flip p≡1 vs 3 mod 4), Z0836 (count law ranks Schinzel failures, in-sample AUC 0.93), Z0843 (R-zeros at large L(1,χ_p), AUC 0.91, n=7), Z0879 (exponent −0.30 → −0.22 at 10⁶/10⁷).
- Premise errors recorded: Z0787 (cubic has 3 A1 nodes; no genus-one fibration), Z0881 (0.019/0.025 not ≤0.016), Z0831 (median 0.47–0.74, not 0.92), Z0766 (0.30% R-zero rate is odd squares), Z0778 (greedy failures not multiplicatively closed), Z0724 (6/n ⇐ 3/n not a formal implication), Z0947 (item numbers are for ordered counts O = 6U).
- Method, reproduction and all numbers below; "not done" per item in the outcome file.

## Method
- Base table for all primes ≤ 2·10⁵ (U, k1, k2, k3, minz, maxx, minx, nx from the repo count output + PARI: h(−4p), h(p), log ε_p, L(1,χ_p)=2hR/√p, L(1,χ_{−4p})): `scripts/z52d_p2_TO3_base.py` → `data/z52b/pass2/TO3/base_primes_2e5.tsv` (1.9 MB).
- Exact enumerator `scripts/z52d_p2_TO3_lib.py` (divisor method, validated vs the count program), existence scanner `scripts/z52d_p2_TO3_exists.c` (early-exit, validated: 0 mismatches vs f4 data ≤3·10⁴).
- Word census (I3, R, Uv, ESC) to 3·10⁶ via `scripts/z52b_fingerprint_words.c` (8.6 s); minwords via `scripts/z52b_fingerprint_minwords.c`.
- Regenerate the scratch inputs first: `gcc -O2 -o /tmp/z52/count4 scripts/z52b_fingerprint_count.c`, `gcc -O2 -o /tmp/z52/words scripts/z52b_fingerprint_words.c && /tmp/z52/words 3000000 > /tmp/z52/words3e6.txt`, `gcc -O2 -o /tmp/z52/minwords scripts/z52b_fingerprint_minwords.c && /tmp/z52/minwords 3000000 > /tmp/z52/minwords3e6.txt`, `scripts/z52d_p2_TO3_ladder.sh` (writes `/tmp/z52/ex_m*_1e7.txt`).
- Residual convention: log U − OLS fit on (1, log p, log log p) unless stated; Spearman ρ.

## Interesting items

### Z0700 — regulator carries the L-value signal (residual ρ = −0.51)
- Raw ρ(U, log ε_p) = −0.03, but after removing (log p, loglog p): ρ(resU, res log ε) = −0.51; ρ(resU, res h(p)) = −0.01; ρ(resU, res L(1,χ_p)) = −0.69. h(p)=1 for 79.5% of p ≤2·10⁵, so the L-value effect is the regulator.
- Repro: `scripts/z52d_p2_TO3_base_analysis.py` (Z0700 keys) and `scripts/z52d_p2_TO3_final_checks.py` (residual decomposition).
- Next: per-prime five-slice counts vs log ε_p (not done here).

### Z0719 — Mordell's six classes are the six hardest mod-840 classes, in the item's order
- Residual means over p≡1 (4), 100<p≤2·10⁵: 1: −0.742, 121: −0.688, 361: −0.644, 169: −0.633, 529: −0.590, 289: −0.581; the next classes 481, 601, 649, 241 lie well above; easiest 557, 277, 653.
- Repro: `scripts/z52d_p2_TO3_base_analysis.py` (keys Z0719_*).

### Z0729 — ES_k ladder: "last failure ≤10⁵" was a range artefact
- Exact scan to 10⁷ (`scripts/z52d_p2_TO3_ladder.sh`): 8/p: 6 failures, last 241; 12/p: 22, last 12241; 16/p: 38, last 83449; 20/p: 64, last 2 763 601 (checked by the exact enumerator: 20/2763601 has no solution); 24/p: 156, last 620 929; 28/p: 158, 1 532 161; 32/p: 262, 3 991 681; 36/p: 482, 8 763 841; 40/p: 555, 6 698 009; 44/p: 684, 7 559 641; 48/p: 1208, 9 961 249.
- So k≥5 ladders keep failing beyond 10⁵; k=2,3,4 look finite up to 10⁷.
- Next: density of failures vs log p at 10⁶–10⁸.

### Z0781 — the Poisson/BM-mean model for R-zeros fails
- Exhaustive over all 4174 primes ≡1 (4) in [10⁴,10⁵) (`scripts/z52d_p2_TO3_bm_poisson.py`, `data/z52b/pass2/TO3/bm_poisson_1e4_1e5.json`): M_BM ∈ [8.2, 22.8]; Σ exp(−M_BM) = 0.0073, observed R=0: 2 (23929, 83449).
- Sample estimator (80 primes/window, `scripts/z52d_p2_TO3_bm.py`): [10⁵,10⁶) expected 0.0 vs 3 observed (102001, 329617, 712321); [10⁶,3·10⁶) expected 0.0 vs 3 (1134241, 1724209, 1726201).
- Reading: zeros are far more frequent than an exp(−M_BM) independent-event law; overdispersion is needed. Next: fit an overdispersed zero model on all primes ≤3·10⁵.

### Z0824 — (−3/q) confound explains about half of the mod-3 split
- Per-prime Legendre regression (q≤47, 8966 primes ≡1 (4)); control: indicators 1[q | p+3]. Indicator coefficients +0.05…+0.12 (SE 0.006–0.015) for every q≥5.
- Mean of q·β_q: q≡1 (mod 3): −0.014 → −0.074 with controls; q≡2 (mod 3): −0.345 → −0.243. Gap 0.33 → 0.17.
- Repro: `scripts/z52d_p2_TO3_regress.py`, `data/z52b/pass2/TO3/regress_results.json`.

### Z0827 — sign flip of the L-value exponent between p≡3 and p≡1 (mod 4)
- log U ~ slope +0.41 · log L(1,χ_{−p}) for p≡3 (4) (n=8993) versus −0.29 · log L(1,χ_p) for p≡1 (4) (n=8966); log p controls change slopes by <0.02.
- Next: joint fit with a common exponent up to sign.

### Z0836 — count law ranks Schinzel failures (in-sample)
- For each m=8..48 (primes ≤10⁵): regression log(1+U_m) on (1, log p, loglog p, log L(1,χ_p)); failures ranked lowest; median AUC 0.93 over m (1–25 failures per m). `scripts/z52d_p2_TO3_auc.py`.
- Caveat: in-sample. Next: cross-validation over prime ranges.

### Z0843 — R-zeros sit at large L(1,χ_p) (7 zeros)
- R-zeros ≤2·10⁵ (word census): 409, 577, 5569, 9601, 23929, 83449, 102001. AUC(zero ⇔ large L(1,χ_p)) = 0.91; AUC(R≤2 ⇔ large L) = 0.88; AUC(zero ⇔ small h(−4p)/√p) = 0.73.
- Too few positives for multi-feature logistic; next: extend the census to 10⁷.

### Z0879 — exponent of U on L(1,χ_p) at 10⁶ and 10⁷
- Exponent (with log p): −0.30 (≤2·10⁵, SE 0.003 naive), −0.22 ± 0.02 (10⁶ window, n=156), −0.22 ± 0.02 (10⁷ window, n=113). Spearman −0.62 / −0.71 (item: −0.62/−0.69).
- Apparent drift ≈3σ; the 2·10⁵–10⁶ gap is the obvious next check. `scripts/z52d_p2_TO3_windows.py`.

## Selected verified numbers (nothing-outcomes)
- Z0708: 373 n ≤30000 with no first-denominator solution at x=(n+3)/4, all ≡1 (24); divisor criterion agrees on 499/499 n≡1 (4) ≤2000.
- Z0748: 4/n two-term solvable ⇔ n even or has a prime ≡3 (4) factor, 2999/2999 for n ≤3000.
- Z0751: parity lemma — every solution of 4/p (odd p) has ≥2 even denominators; 4/131 has 32 solutions, all with exactly two even ones; 8/131 unsolvable.
- Z0753/Z0771: I3 zeros 114 (max 2 433 600); Uv-zero set among odd non-squares ≡1 (4) = {105, 2961, 3985, 25305, 111969, 978145} (Uv proxy, not U).
- Z0755/Z0756/Z0757: squares with I3=0: 1,…,1225, 1600, 19600 (=140²), 2433600 (=1560²); at 1560² and 105 all of I3, R, Uv, ESC vanish.
- Z0766: R=0 at n≡1 (8) is 0.30% only because all 866 odd squares are R-zeros (T1); non-squares: 0.069%.
- Z0776: I3(p)=0 for p ∈ {2,…,23, 31, 43, 47, 59, 83, 103}; none beyond 103 ≤3·10⁶.
- Z0778: greedy failures closed under multiplication: false (49·73 = 3577).
- Z0787: ES cubic 4xyz = p(xy+yz+zx)w has three A1 nodes at the coordinate points; the minimal resolution has Pic ≅ I^{1,6} ⇒ no genus-one fibration; the pencil x=y=0 gives a line+conic.
- Z0797: best diagonal ternary form |ρ|=0.65 vs L(1,χ_p) baseline 0.73 (210 forms, 1114 primes ≤2·10⁴).
- Z0853: P(E_C) = 0.75, 0.49, 0.34, 0.31, 0.24 (C=1,2,3,4,5); |φ| ≤ 0.17 between events.
- Z0856: lemma p | z (largest denominator) verified on 7065 solutions, p ≤1000.
- Z0724/Z0726/Z0735 checks: 9/n fails exactly at {2,5,11,19} for n ≤4000; 5/n and 6/n never fail for n ≤4000 or primes ≤10⁵; 12/p fails at the 22 primes up to 10⁷.
- Z0870: 109 primes ≤10⁵ (incl. 2) have a power of 2 among the denominators.
- Z0876: 9 solutions of 4/2521; none has x | z; 6 have 2521 | z only, 3 have 2521 | y and z.
- Z0918: #ss(F_p) = h(−4p)/2 exactly (95 primes p≡1 (4) ≤1200); residual corr with U 0.14, with k2 0.37.
- Z0932: records of 4x−p = 2, 3, 7, 11, 23, 31, 59 at 2, 5, 73, 1129, 1201, 21169, 118801 (A400619 first 7). U(8 803 369)=140, R=16, Uv=11, I3=68.
- Z0935: primes ≤10⁶ of form x²+840y² = primes in the six Mordell classes (2370 primes; exact).
- Z0936: class group of disc −4D elementary 2 for D=840, 1320, 1365, 1848 (idoneal) and not for 255, 390, 1155, 2310.
- Z0959: h(−24p) mod 8 = (3/p) exactly for p≡1 (8); the mod-16 residual strata are the genus character (3/p).
- Z0966: lowest U/log³n composites ≤30 000 are 97², 113², 163², 109², 37², 67², 2·71², 173², 103², 61², 73², 89².

## Not done / limits
- Z0839 (per-solution five-slice fraction), Z0840 (λ=2 test), Z0764/Z0765 (character decomposition of R−M_BM), Z0905 (Granville–Soundararajan tail), Z0924 (negative-binomial fit), Z0970 (variant detectors), Z0888 (Jacobi derivative with SEs) — listed in each record's `not_done`.
- Literature: only arXiv:2511.16817 was checked (abstract + HTML §1); OEIS A400619 beyond its first terms not accessed.
- Words census is ≤3·10⁶ (no 3·10⁸ segmented run); U(p) table ≤2·10⁵ plus windows at 10⁶, 10⁷ (repo data).
