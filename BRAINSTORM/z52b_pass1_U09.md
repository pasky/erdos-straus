# z52b Pass 1 — batch U09 (200 untried §2 items, Z0432–Z3191)

1. Batch U09 complete: 200 items, outcomes in `data/z52b/pass1/outcome_U09.jsonl`. ES remains OPEN; nothing here claims progress on it.
2. Counts: skipped 159, covered 17, needs-compute 14, nothing 8, interesting 2. None of these is a claim about ES itself.
3. Interesting: **Z1398** (min max-denominator ~ p^{3/2}; (★) part PROVED, full family EVIDENCE) and **Z1982** (non-Poisson exceptions of xyz−x−y−z, x,y,z≥2, with 3|n enrichment).
4. Covered (repo already has it, with a reproduction here): Z0446, Z0452, Z0589, Z0594 (T1), Z0670 (QNR), Z0895 (isosceles), Z1460, Z1494, Z1496, Z1523, Z1534, Z1609, Z1980, Z2101, Z2224, Z2240, Z2291.
5. Caveat: 159 skipped is mostly catalogue entries with `first_step: None`, plus ~50 items whose first step is a **literature lookup that I did not execute** (tagged skipped with that reason). A literature pass on those is the main gap in this batch.

## Z1398 — minimal max-denominator of 4/p = 1/x+1/y+1/z (interesting)

* **(★) subfamily, PROVED.** For a (★) triple (u,B,C), 4uBC = p+u+B, the denominators are uBC, pBC, puC. Then max ≥ pC·max(u,B) ≥ pC√(uB), and with C = (p+u+B)/(4uB) and s = p+u+B: max ≥ p·s/(4√(uB)) ≥ p·s/(2√s) = p√s/2 ≥ p^{3/2}/2. So the (★) family cannot produce a max-denominator below p^{3/2}/2.
* **Full family, EVIDENCE.** Enumerated all ES solutions (divisor method, validated against brute force for p ≤ 400) for the 707 primes p≡1 (4), p≤1.2·10⁴ (`scripts/z52b_p1_U09_minmax.py`, output `data/z52b/pass1/U09/minmax_full_le12000.txt`):
  * fit log min z ≈ 1.527 log p + 0.24; median exponent 1.55; max exponent 1.89 (small p);
  * min z / p^{3/2} ∈ [0.508, 15.9], median 1.52; the lower envelope stays near 1/2, the bound from the (★) part.
  * Ratio z/p by range: median 31 (p∈[100,1000)), 74 ([1000,4000)), 136 ([4000,12000)) — consistent with exponent 3/2, not 1.
* **Why it matters for ES (assessment).** If every ES solution has max denominator ≥ c·p^{3/2}, that is a pointwise lower bound on the scale of solutions, and it would mean the Type I solutions are no smaller than the (★) family. Next: test p ≤ 10⁶ (C enumerator) and try z = pxy/(4xy − p(x+y)) (from 4xyz = p(xy+yz+zx) with z the largest denominator) for a lower bound.
* Reproduce: `python3 scripts/z52b_p1_U09_minmax.py 12000` (≈40 s).

## Z1982 — exceptions of n = xyz − x − y − z with x,y,z ≥ 2 (interesting)

* Exception counts (all n up to bound): 31 (≤10²), 113 (≤10³), 320 (≤10⁴), 821 (≤10⁵). Last exceptions up to 10⁵: 95779, 95889, …, 99936. Not finite-looking at this scale. Exceptions include 9 squares (1, 4, 9, 16, 49, 324, 361, 441, 5476): squares are not especially enriched.
* Multiplicity r(n) (all ordered (x,y,z)), n ≤ 10⁴: mean r = 13.5 on [100,1000), 21.2 on [1000,3000), 29.2 on [3000,10⁴), i.e. ≈0.75·½log²n. Under a Poisson model with that mean, P(r=0) ≈ e^{−29} at n≈5000; observed 1.9% of n∈[3000,10⁴) are unrepresented (320 exceptions in total ≤10⁴). **Non-Poisson**: representations are strongly correlated.
* Residue enrichment (n ≤ 10⁴): exception rate 10.1% at n≡3 (mod 12), 9.2% at 9 (mod 12), 3.2% overall; 3 | n gives 6.7%. So the mod-3 structure is the strongest local signal; mod 2, 4, 8, 16 show only weak effects.
* Reproduce: `python3 scripts/z52b_p1_U09_xyz_reps.py 10000`; `python3 scripts/z52b_p1_U09_misc.py 200000 100000` (exceptions and squares).
* Next: separate the 3-adic local-density effect from a residual non-Poisson structure (condition on n mod 24 and compare with the expected local densities). If the residual is real, it is an example of a thin but infinite exceptional set for a 3-variable form with polylog mean.

## Other computations in this batch (kept as data, all reproducible)

* `scripts/z52b_p1_U09_core.c` (C): R(p) = #{(u,B,C): 4uBC−u−B = p} for all primes ≡1 (4), p ≤ 2·10⁵ → `data/z52b/pass1/U09/R_primes1mod4_le2e5.txt` (4 s). Results: no odd R; 7 zeros (409, 577, 5569, 9601, 23929, 83449, 102001), all ≡1 mod 8.
* `scripts/z52b_p1_U09_analyze.py`: C=1 criterion (verified for all 8977 primes), minimal-C distribution (median 1, 99th pct 11), Hardy–Littlewood singular-series correlation (≈0.05), class means mod 840 → `data/z52b/pass1/U09/analyze_out2.txt`.
* `scripts/z52b_p1_U09_fullf.py`: full f(p) (all ES solutions) for p≤1.2·10⁴ → `data/z52b/pass1/U09/fullf_le12000.txt` (class-mean mod 8: 0.73 vs 1.05; mod 3: 0.82 vs 0.98; overall ×4 spread mod 840 — the repo's ×14 non-adelic bias, reproduced in shape, not magnitude).
* `scripts/z52b_p1_U09_qnr.py` (least QNR, Spearman −0.39) and `scripts/z52b_p1_U09_misc.py` (power-of-two denominators: 37/8977 primes; cubic character of 2 and 4: no correlation).
