# z52b Pass 1 — batch U01 (INCOMPLETE: 62 of 207 items processed; ES remains OPEN)

1. Counts so far: nothing 46, covered 3, interesting 9, needs-compute 4, skipped 0. Remaining 145 items have NO line in `data/z52b/pass1/outcome_U01.jsonl` (not processed, not skipped).
2. Interesting: Z0728 (20/p failures concentrate on p≡1 mod 120), Z0730 (F(m)⊆F(mk) in 39/39 nontrivial pairs), Z0746 (composite failures always inherit from a failing prime divisor, 1556/1556), Z0900 (p−1 practical ⇒ harder; 0/30 hardest), Z0969 (residual corr 0.50 for U(p) vs U((p+3)/4)), Z1416 (greedy two-term lag max at 2521 and 1201), Z0355 / Z0893 / Z0894 (FF engine: constant numerator 4 degenerate by lc lemma; twist ratio grows with degree; square-at-linear-primes lowers mean ES count ~3.6×).
3. Needs-compute: Z0752, Z0739 (extend to 1e7 needs existence-only counter), Z0949 (≈2–3 CPU-days extrapolated), Z0896 (new signed counter, 1–2 h).
4. Caveat: the redo under pass1_U_fix.md was applied to the items already processed (Z0874, Z0878, Z0892–Z0894, Z0355, Z0896, Z0739, Z0752, Z0949 were re-run or re-labelled); the rest of the batch still needs the same treatment.
5. Scripts: `scripts/z52b_p1_U01_*.py` (common, fingerprint, practical, isosceles, quick, ff, twoterm, fourterm, record, items_a/items_b). Raw outputs gzipped in `data/z52b/pass1/U01/`.

## Interesting items

### Z0728 — 20/p failures and p ≡ 1 (mod 120)
* Failures of 20/p (= 4/p with all denominators divisible by 5) at primes 5<p≤1e5: 60 (plus 2,3,5). Last 90001.
* Residue classes: 33/60 are p≡1 (mod 5) (base 25%). 21/60 are p≡1 (mod 120): 21 of 286 such primes fail (7.3%), vs 39 of ≈9300 others (0.4%).
* Reproduce: `python3 scripts/z52b_p1_U01_fingerprint.py`-style counts on `data/z52b/raw/m20_pr1e5.txt` (column 2 = U).
* Next: is the mod-120 enrichment a character-sum effect? Extend to p≡1 mod 120 up to 1e6.

### Z0730 / Z0746 — divisibility structure of failure sets
* For m|mk (m,mk ≤48, p≤1e5): F(m) ⊆ F(mk) in 39/39 nontrivial pairs (e.g. F(8)={2,3,11,17,131,241} ⊆ F(16)); the reverse inclusion fails.
* Composite n≤4000, m=5..48: 1556 composite failures, all with a prime q|n such that m/q fails (0 exceptions). The converse fails heavily (137775 composites have a failing prime divisor, 1556 fail).
* Reproduce: `gcc -O2 -o /tmp/c scripts/z52b_fingerprint_count.c -lm; /tmp/c m 2 4000 0` for each m; then compare.

### Z0900 — p−1 practical and ES hardness
* Over primes 5<p≤3e4 (3242 primes, data/z52b/raw/f4_all_30000.txt): mean residual of log(U4+1) (quadratic in log p) is −0.31 when p−1 is practical, +0.17 otherwise.
* 0 of the 30 hardest primes have practical p−1 (null ≈0.65^30 ≈ 1e−6). Effect persists in classes mod 8 and mod 24.
* Reproduce: `python3 scripts/z52b_p1_U01_practical.py`.
* Next: control for divisor-count of p−1 (compare with random n of the same ω), and test for hard primes with p−1 having a large prime factor.

### Z0969 — U(p) vs U((p+3)/4)
* 271 pairs (p, (p+3)/4 prime), p≤3e4: raw Spearman 0.657 (matches item). Pearson of residuals after a quadratic in log p: 0.50.
* Next: partial out p mod 8 and the 2-adic class of (p+3)/4; compare with random prime pairs of similar size.

### Z1416 — greedy first term and two-term completion
* For primes ≤3000, the smallest x≥⌈p/4⌉ with (4x−p)/(px) a sum of two unit fractions is found for all 428 primes checked in the window. Lag median 0, mean 0.09, max 5 at p=2521 and p=1201; then 3 at p=2689.
* Reproduce: `python3 scripts/z52b_p1_U01_twoterm.py 3000`.
* Next: run to 1e6; test whether lag≥3 concentrates on the top-30 hard primes.

### Z0355 / Z0893 / Z0894 — function-field engine (F_5[T], scripts/bs_ff_es.py)
* Constant numerator 4: 0 solutions for every monic P of degree 3 and 4 (lc(4X−P)=3 ∉{1,2}, the engine's lc condition). Constants 1,2,3 give 159240, 41070, 5000 at deg 3.
* Non-square twist A=2T vs A=T: total #ES over monic deg-3 P 4110 vs 16450 (×4.0); deg 4: 82350 vs 416223 (×5.1). Over irreducibles: mean #ES(T,P) 5.4, 25.6, 56.8 (deg 2,3,4); T/2T ratio 3.4, 6.4, 9.2.
* Square-at-linear-primes P (P(c) a nonzero square ∀c∈F_5, deg 5): mean #ES 659 vs 2361 for 200 random monic deg-5 P (A=T).
* Reproduce: `python3 scripts/z52b_p1_U01_ff.py` (takes a few minutes).
* Next: check whether the lc lemma is already in EXSET_FUNCTION_FIELD.md; if the FF "4/P" analogue is degenerate, use numerators with lc∈{2,3}.

## Notes on non-interesting outcomes (for the record)
* Z0973 isosceles criterion (m-general): m/p has x=y solutions (p≠m) iff m | p+1, m | p+2, or m | 2p+1. Verified by brute force for p≤200, m∈{4,5,7,8}, and independently by the counter's V7 column on 9592 primes for m=5.
* Z0743/Z0744: 8/p and 12/p failure sets disjoint for primes 3<p≤1e5.
* Z0740: failure counts reproduce the item's sequence; regression R²=0.974 is just growth in m.
* Z1877 (multiplicative variant): 397/400 primes ≤2000 without solution under a bounded search (x,y≤2p); caveat: bounded.
* Z3073/Z0310/Z1639: 4→3 merge is exactly the 3-term ES condition (split/merge identity), no new handle.
* Erdős-page items (Z2153–Z2203): statements read from erdosproblems.com; none is an ES-count statement.
