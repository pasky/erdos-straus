# AGENT REPORT O66 — verify.py blocks (dg)–(dm)

Branch `side-agent/verify-blocks-4`. Full `uv run --with scipy python verify.py` under
`ulimit -v 8000000`, `OMP_NUM_THREADS=2`: **all checks passed**, 4 min 25 s wall (new blocks ≈ 33 s).
The new blocks were also run without scipy: the scipy parts skip cleanly, the rest passes.

| block | document | what is replayed | s |
|---|---|---|---|
| (dg) | POINTWISE_OMEGA14 §1 | Lemma 1.1 planting, exact rationals: 45 instances (15/15/10/5 for k = 0..3, n ≤ 8+3k): ν ≥ 0, ν(0) = 0, k-marginals of ρ vanish, control ((k+1)-marginals move); [scipy] R49 symmetrised-LP thresholds R ≈ 1.111, 1.250, 2.514, below (1.1) | 14.6 |
| (dh) | POINTWISE_OMEGA15 | Lemma 1.1 closed form = brute force (40), bound `(4r*)^{k+1}` and zero for `|I| ≤ k` (215 reduced products, k ≤ 2), R57's definition-based toy systems (40 trials), Lemma 2.3 (a)/(b) on 37 (Q, r, x, q) | 4.8 |
| (di) | POINTWISE_OMEGA16 §6 | W(133050918961) = 5935 by direct divisor search (prime, 121 mod 840); least p ≡ 1 (24) with W > 31/127/511/1023/2047 = 2521/33289/2031121 (exhaustive below 2031122); N1 Buchstab ratios at u = 2: 10⁷ (κ=3: 0.958) and 10⁸ (0.950, 0.910, 0.881 = data file) | 0.7 |
| (dj) | EXCEPTIONAL_LARGESIEVE3 | Thm 1.1 core inequality (author toys + R59 multi-rough/spiky/equality ratio 1), Thm 3.1 local bound, Lemma 4.1; Lemma 4.2: −4 ∈ ℛ(M) and exact (16.1) solutions for all M ≡ 3 (4) ≤ 2000, n = kM−4 | 1.5 |
| (dk) | EXCEPTIONAL_SPW2 §2 | Lemma 2.2 (24 (N, C)), Lemma 9.3 thresholds 3/2 (C=2), 4 (C=3/2); Lemma 2.3 exact kernel dimensions (D ≤ 6), cyclotomic witnesses (D ≤ 12), Φ(N//2) ≥ 3N+2 iff N ≥ 38 (N < 2000); [scipy] RSPW LP η = 1, 0.955, 2/3, 2/3 | 1.2 |
| (dl) | CEILINGS_UNIFIED §4.4 | the full threshold table (least k with E B > 0: 3/7/11/15; with ≥ 90 % majorant saving: 6/8/12/14) by R60's exact dual simplex; author's sympy primal agrees exactly at 6 cases | 2.7 |
| (dm) | POINTWISE_WINDOW3 §3, §8.1 | [scipy+mpmath] one-window LP 0.48929 = dual bound (cert); K = 2.5 fake re-verified at 50 digits (support 628, min ν/μ 0.0566, family excess −1.0e−3) | 7.4 |

Docstring of verify.py and the STATUS.md verify.py bullet updated.

## Deviations and findings for the parent

1. **(dg) is smaller than the document's numerics.** `omega14_planting.py`'s own Lemma 1.1 check
   (100 instances, n ≤ 22) did not finish in 300 s here (the k = 3, n ≈ 22 marginal loop is
   heavy); POINTWISE_OMEGA14's Replay line says "~1 min". The block uses n ≤ 8+3k, 45 instances.
   The parent may want to fix the "~1 min" claim (not touched here).
2. **(di), Buchstab at 10⁷:** the ratios are 0.965, 0.926, 0.958 (κ = 1, 2, 3), so at 10⁷ they are
   *not* monotone in κ. The document's "visibly multiplicative" claim is about 10⁹ (and 10⁸ is
   monotone: 0.950, 0.910, 0.881, r₃/r₁³ within 3 %). The block asserts monotonicity only at 10⁸. The 10⁹ table is not
   replayed. "Least" for p = 133050918961 (scan to 2.382·10¹¹) is not replayed; only W(p) = 5935.
3. **(dm), minor doc inconsistency:** POINTWISE_WINDOW3 §3 says "Window configs 197, joint 38809";
   `window3_lp.py` reports `nW = 195`, `cols = 38025 = 195²` (both for `--one` and the two-window
   runs). The values (0.4893; support 628 etc.) match the document. Not edited.
4. (dj)/(dk)/(dl)/(dh) import or `runpy` the authors' and reviewers' scripts (fixed seeds); they
   assert internally, and the block additionally checks the reported numbers.
