# AGENT REPORT O133 — Part A: verify.py blocks for DISCOVERIES section (I)

Branch `side-agent/verify-automorphic`. Seven new blocks (es)–(ey) at the end of `verify.py` (header docstring
updated). Each block runs the REVIEWERS' from-scratch scripts as subprocesses (author code only as the object of a
comparison), asserts exact output strings/counts and prints one summary line. All blocks ≤ 2 cores, ran under
`ulimit -v 8000000`. Timings are from standalone runs.

| block | ledger | reviewer scripts | what is checked | s |
|---|---|---|---|---|
| (es) | (I)1 POINTWISE_TERNARY (R124) | review_tern_sweep, review_tern_qd | Comp 6.1 sweep reproduced byte-for-byte against `logs/review_tern_sweep.out.txt` (30 subsets, 22 with n ∈ ℚ(V), 57 quadratic pieces, ranks {2:54, 3:1, 1:2}, 56 isotropic, unique rank 3 = Type II `(a,d,e,f)`, d fixed: `ef − 4a²d`). Step 4 at (10⁶, 4, 100): failures exactly {3361, 7681}. At (10⁷, 8, 200): 20513 primes, R124's histogram, worst 13 at 733321. `a_min(84525841) = (22, d=3)` | 7 |
| (et) | (I)2 CONDITIONAL_ES (R127) | review_r127_lemma11 200, _diag, _counts.c | Lemma 1.1: three forms + dual + remainder agree for n < 200 (600 solutions, 0 mismatches). Prop 7.2 diagonal: p_j avoid all classes m ≤ 20000. ET f(2..8). S(13, 29, 193) = 2, 3, 3. S(5101441) = 1 with (c,f,g) = (890,39,147), f = 798, f_I = 188, f_II = 78 | 4 |
| (eu) | (I)3 POINTWISE_SPECTRAL (R123) | review_r123_lemmas 1000 300, _areas, _prop53, _count.c, _cmp, _windows | Lemmas 2.1–2.4: routes agree for p ≤ 1000. Lemma 2.4: 11581 quadruples, 0 violations, no odd square. Raw brute force for p ≤ 300. Props 3.1/3.2: areas, widths, point-in-wedge = Type I (1962 hits; needs scipy). Prop 5.3: 3630 primes, target empty. f_I ≥ 1 and Type II exist for all primes ≤ 10⁶. C = Python for p ≤ 3000. Dyadic minima and min/mean as in R123 | 41 |
| (ev) | (I)4 POINTWISE_TYPEII_SPECTRAL (R128, R128b) | review_t2s_{brute.c, param, sieve.c, geom, genus}, review_r128b_{lattice, eis, count.c} | Lemma 1.1: forms 1–5 vs raw brute force; form 1 for n ≤ 2000 (Σ 30610), forms 2–5 for p ≤ 150. Sieve = brute for n ≤ 2000. f_II(odd square) = 0. Geometry: 671 points, min cosh 3, det-p 4, incidence error < 1e−10. Genus lemma: 29678 moduli. Props 7.1–8.3 (p < 300). Props 9.1–9.2 (332176 triples). Two independent counters at 10⁷ reproduce their stored outputs byte-for-byte | 72 |
| (ew) | (I)5 EXACT_FORMULA (R131), elementary | review_r131_brute.c, _compare, _slices (+ author exf_engine.c as comparand) | Lemma 1.1: brute-force sets = engine + expand_T1 for n ≤ 3000 (4 families, 515766 tuples). Zero sets recomputed from the brute file: T2⁺ = squares ∪ {288, 336}, T1± = powers of 2, T2⁻ = 12 values. §3.2, Prop 4.1 (support and full box n ≤ 60), Thm 5.2 at n ≤ 1500: 0 failures | 30 |
| (ex) | (I)5 EXACT_FORMULA CERTIFIED rank (R131) | review_r131_rank (+ author pipeline exf_hurwitz/exf_engine/exf_columns, run in a tempdir) | `data/exf/columns_2e4.npz` is git-ignored, so it is regenerated in a tempdir. Spot checks: 0 mismatches. Exact ℚ-ranks for all six row sets equal R131's table. dim ∩ = 0, and the restriction is injective | 116 |
| (ey) | (I)6 QUATERNION_ES (R130) | review_quat_{hilbert 3000, brute 200, symbolic, fixed_de} | All four outputs are byte-identical to the stored R130 logs. Prop 1.3: ramification exactly {p, ∞} on 26007 Type I solutions. Brute force = parametrisations (45 primes). Lemmas 1.2/3.1 and the isogeny det, symbolically. §3.4 counts 40/93, 120/450 | 2 |

Scope notes (what is NOT covered):
* (I)1: the Step-4 10⁸ claim is checked only through the worst-case spot value. The 1/20 sample at 10⁸ is not re-run.
* (I)3: the 10⁷/10⁸ f_I runs are not repeated; the check stops at 10⁶. Lemmas run at n ≤ 1000 instead of R123's 3000 (10.6 min).
* (I)4: forms 2–5 are checked only for p ≤ 150 (R128: 400). Geometry at p < 250 (R128: 600, 3 min).
* (I)5: the §3.3–3.4 genus numerics (`review_r131_genus.py`) are not included. They are EVIDENCE only, with no stored reference output.
* (ex) is the slowest block (~2 min). It relies on the author's column-generation pipeline. The ES columns are cross-checked inside R131's script against its own brute force (n ≤ 3000), and 12H against its own reduced-form count.
* Every block degrades gracefully without gcc (C parts skipped with a message). Without scipy, (eu) skips the areas part.

Full `verify.py` run (`(ulimit -v 8000000; OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 3000 uv run --with scipy
--with mpmath python verify.py)`, nohup, about 14 min wall time): **`all checks passed`, exit 0**. There are 154 section headers, and no
block was SKIPPED. New-block seconds in the full run: es 7.2, et 4.3, eu 38.5, ev 72.3, ew 30.2, ex 118.1,
ey 2.3, about 4.5 min in total.

Part B (STATUS.md / CAMPAIGN_SUMMARY.md refresh) is waiting for the parent's go-ahead.
