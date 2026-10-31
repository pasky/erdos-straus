# z52b Pass 1 — batch U09 (200 untried §2 items, Z0432–Z3191); revised after pass1_U_fix.md

1. Batch U09 complete (fix round applied): 200 items in `data/z52b/pass1/outcome_U09.jsonl`. ES remains OPEN; nothing here claims progress on it.
2. Counts: nothing 120, covered 58, interesting 3, needs-compute 9, skipped 10 (skips are rule-3 restatements/meta/organisational only: Z0561, Z0573, Z0618, Z1244, Z1515, Z1870, Z2059, Z2213, Z2353, Z2711).
3. Interesting: **Z1398** (min max-denominator ~ p^{3/2}; (★) part PROVED, full family EVIDENCE), **Z1982** (non-Poisson exceptions of xyz−x−y−z, x,y,z≥2, enriched on 3|n), **Z2047** (sign flip: tuv+u+v with 4|t has only 7 failures ≤2·10⁵, all ≤449, while the (★) sign pattern tuv−u−v fails at 409, 577, 5569, …).
4. Covered (58 in total; repo already has it, literature status checked): the catalogue entries mapped to BRAINSTORM/z52b_dividing.md (#3, #7, #19, #22, #44, #84–#110, #148–#162, #224–#243, #279, #281), plus Z0446, Z0494, Z0594, Z0604, Z0670, Z0895, Z1235, Z1460, Z1494, Z1496, Z1523, Z1534, Z1609, Z1980, Z2061, Z2101, Z2129, Z2220, Z2224, Z2240, Z2254, Z2315, Z2322, Z2076, Z2022, Z0675.
5. Needs-compute (rule 4 justified, with estimates): Z0773 (ESC enumerator, >1 h coding), Z0863 (general-n no-3 search to 10⁷, 30–60 min C), Z1848 (R at 10⁷–10⁸, >30 min), Z1890 (sibling tables), Z1986 (Z[ω] port, 1–2 h), Z2027, Z2541 (>1 h coding), Z2549 (>1 h constraint derivation), Z2641 (S_{n,−4} table + classifier).

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

## Z2047 — sign flip of the ES trilinear form (interesting)

* Patterns t·u·v + s₁u + s₂v = p with 4 | t, t,u,v ≥ 1 (`scripts/z52b_p1_U09_cont.c`, output `data/z52b/pass1/U09/cont_out.txt`, primes ≤ 2·10⁵):
  * (−,−) = tuv − u − v: exactly the (★) family; failures among p≡1 (4): 409, 577, 5569, 9601, 23929, 83449, 102001 (7 = the (★) zeros, cross-checked against R7.txt).
  * (+,+) = tuv + u + v: failures among p≡1 (4): 5, 13, 17, 97, 113, 193, 449 (7 in total ≤ 2·10⁵, none above 449). Independent Python check agrees on 5, 13, 17, 97, 113, 193, 449 (no witness with t ≤ 400) and on the (−,−) failures.
  * (−,+) and (+,−): one failure each (p = 5).
* Mechanism for (+,+) at u = 1: (t+1)v = p−1, so p is represented iff p−1 has a divisor d ≡ 1 (mod 4) with 5 ≤ d ≤ (p−1)/2. The small failures are the p with p−1 having no such divisor; u ≥ 2 rescues all others up to 2·10⁵. (Witness check: 409 = 16·1·24 + 1 + 24.)
* Why it matters (assessment): the sign flip changes the failure set from a growing set (the ES zeros) to a finite list. This is the first computation in the repo that separates the two sign patterns at the level of exceptions (signature memo #69 proposed it, without a result).
* Next: extend the (+,+) test to p ≤ 10⁷; identify whether u ≥ 2 is needed for any prime > 449; if the exception set stays finite, ask why (the proof would have to handle the u=1 divisor structure of p−1).

## Other computations in this batch (all reproducible)

* `scripts/z52b_p1_U09_core.c` (C): R(p) = #{(u,B,C): 4uBC−u−B = p} for all primes ≡1 (4), p ≤ 2·10⁵ → `data/z52b/pass1/U09/R7.txt` (extended with u, B at minimal C).
* `scripts/z52b_p1_U09_fullf.py`: all ES solutions for p ≤ 1.2·10⁴ (validated vs brute force, p ≤ 400) → `data/z52b/pass1/U09/fullf_le12000.txt`.
* `scripts/z52b_p1_U09_lambda.c`: λ(p) for p ≤ 3·10⁴ (repo convention) → `lambda_le30000.txt`.
* `scripts/z52b_p1_U09_parity_no3.py`: parity patterns (only (0,0,0), (0,0,1) occur; the others are excluded 2-adically) and the no-3 check for n ≤ 400 (failures: multiples of 3 and 241).
* `scripts/z52b_p1_U09_fix*.py`, `scripts/z52b_p1_U09_fix4.py`: the fix-round computations (Z0440, Z0494, Z0593, Z0604, Z1071, Z1189, Z1235, Z1419, Z0520, Z0582, Z1543, Z1820, Z1953, Z2371, Z0622, Z0657, Z0585, Z0669).
* `scripts/z52b_p1_U09_families.c`: R for arbitrary primes (Z1848 partial; only one prime ≡1 mod 840 reached, so not a result).
