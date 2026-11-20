Result: Exact sparse L1+P3+Q3+P5 unions for every prime 5≤r≤211 and finite branch histograms through depth 3 for r=29,…,211 (plus existing r=17 depth 8). Label: CERTIFIED (exact enumeration; tree histograms replayed from stored exact box lists)
Scope: Finite r-adic boxes on the r-generic Mordell line only; no claim of r=17 sterility or ES. M17D already tested the (r,u)=(17,5) point through P level 10 and Q level 15. A new two-orientation deep-point extension was not attempted: the P-level-10 engine enumerated 1.44×10¹² candidates, while level 11 has 27,249,694,841,049 candidates (counted under the engine's congruence and hyperbola bound); no rigorous practical cutoff for the proposed split was established.
Review: internal hostile (review of 566025ff)
Triage: DATA
STATUS delta: none

# z78 Lane 2 — exact sparse unions and branch histograms

## Sparse union format and results

`data/z78/exact/union.tsv` keeps the requested header `r l1 p3 q3 p5`. Each entry is the marginal number of distinct nonsquare residue cylinders newly covered by that ordered family; rows are normalized to depth 3 only at output. The full exact table covers every prime 5 ≤ r ≤ 211 (45 rows); family residue sets are stored alongside it.

The union implementation is sparse-native-depth: it stores box sets modulo r, r² and r³, tests a deeper box against only its possible ancestors, and never constructs the `r³` nonsquare universe or lifts boxes to depth 3 during intersection. A surviving native-depth box contributes `r^(3-depth)` only in the final output scaling. `L1` is P₁∪Q₁ (mod r), `P3` is P at exponent 3 (mod r²), `Q3` is Q at exponent 3 (mod r³), and `P5` is P at exponent 5 (mod r³). These are exact marginal counts, not multiplicity sums.

The four primes r = 5, 7, 11, 13 have complete level-1 coverage of the nonsquare classes. At r = 17, the L1 union covers 6/8 nonresidue classes, while P3/Q3/P5 add 182 depth-3 cells beyond L1 (396 of 2312 nonsquare depth-3 cells remain after these four families). The L1 counts agree with `data/z77/level1.txt`. The P5 ET enumerator was extended through 211; the 45-row table preserves the specified family ordering and marginal-count interpretation.

### P5 enumerator and work bounds

`P5` uses `scripts/z78_exact_et.cpp`, an exact C++ implementation of the four-regime ET cover (e, ad, ac, cd), with GNU coreutils `factor` batched once per regime. For N=r⁵ it chooses Xcd ≥ N^0.3 and a sufficient Xo satisfying Xo⁴Xcd ≥ N²; completeness follows from the standard ET inequality e²(ad)(ac)(cd)=(acde)²≤N² for a≤b. Every recovered tuple is checked in the original equation and the unit filters; the factored integer products are checked against the input rows. Output is the deduplicated pair of P box centres modulo r³.

The old full a,d scan for P5 would use about (π²/12)r⁵ iterations. The four-regime work through r=101 is about 2.50 million candidate factor keys total; after unit filtering, r=101 sends 371,730 keys to `factor`, and r=211 sends 2,045,569. The ET set exactly reproduces the previous exhaustive P5 residue sets at r=17, 19, and 23. Counts above are exact enumerations, not upper-bound substitutions.

## Branch histograms

`data/z78/exact/rtree17_d8.txt`, `rtree19_d6.txt`, `rtree23_d6.txt`, and `landscape_d4.txt` preserve the existing stored trees/census from `data/z17/`. Exact P/Q branch histograms through depth 3 for primes r=29,…,211 are in `rtree{r}_d3.txt` (38 primes). Their P5 data uses the ET engine; P/Q boxes were exhaustively enumerated. The U-family is omitted from the computation because M17B Lemma 1.1 gives containment in a P-box at the same or an earlier depth, so it does not change the nonsquare-cell union. Histograms count new boxes by alive parent, per nonresidue cell; the files include the exact integer counts and per-cell histograms (alive fractions are display decimals only).

Across these trees, the largest d2 parent multiplicity is 14 (r=47), and the largest d3 multiplicity is 4 (r=29, 37, 61, 139). This is finite-depth evidence only, not a uniform bound. The r=17 C₅/C₇ tree to depth 8 remains the stored exact tree: new-box counts at depths 2–8 are `4,23,34,83,100,272,326` and maximum parent multiplicities are `4,4,2,2,2,1,1`.

## Replay

```sh
ulimit -v 2000000
timeout 1800 uv run --offline --no-project python -B scripts/z78_exact_union.py 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211
timeout 1800 uv run --offline --no-project python -B scripts/z78_exact_tree.py 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211
```

Both scripts run families sequentially; the factor child is also sequential and no separate factor workers are used. Remove local `data/z78/exact/enum.bin` and `et.bin` after replay. No result here proves sterility or any infinite case.
