Result: Exact sparse L1+P3+Q3+P5 unions and finite branch histograms were enumerated or replayed for small r. Label: CERTIFIED (exact finite enumeration; tree histograms replayed from stored exact box lists)
Scope: Finite r-adic boxes on the r-generic Mordell line only; no claim of r=17 sterility or ES.
Review: none
Triage: DATA
STATUS delta: none

# z78 Lane 2 — sparse exact unions and branch histograms

## Exact union format and results

`data/z78/exact/union.tsv` uses the agreed header `r l1 p3 q3 p5`. Each entry is the number of distinct **nonsquare residue classes modulo r³ newly covered** by that ordered family, after removing all classes covered by earlier columns. Boxes are lifted to common depth 3 before membership and deduplication. `L1` is the union of P₁ and Q₁ boxes (mod r); `P3` is the P family at exponent 3 (mod r²); `Q3` is Q at exponent 3 (mod r³); `P5` is P at exponent 5 (mod r³). Counts therefore are marginal union increments at a shared denominator, not multiplicity sums or raw box counts.

| r | L1 | P3 | Q3 | P5 | nonsquare classes mod r³ |
|---:|---:|---:|---:|---:|---:|
| 5 | 50 | 0 | 0 | 0 | 50 |
| 7 | 147 | 0 | 0 | 0 | 147 |
| 11 | 605 | 0 | 0 | 0 | 605 |
| 13 | 1014 | 0 | 0 | 0 | 1014 |
| 17 | 1734 | 136 | 16 | 30 | 2312 |
| 19 | 1805 | 456 | 54 | 32 | 3249 |
| 23 | 4761 | 368 | 12 | 62 | 5829 |

For r = 5, 7, 11, 13, the L1 union covers every nonsquare class at depth 3. For r = 17, it covers six of eight nonresidue cells at level 1, leaving 578 depth-3 classes; P3/Q3/P5 add 182 distinct classes, leaving 396. The L1 level-1 counts agree with the stored z77 census (`data/z77/level1.txt`). No all-depth or sterility conclusion follows.

`scripts/z78_exact_union.py` calls the exact generalized enumerator in `scripts/z17_renum.c` through the tiny wrapper `scripts/z78_exact_enum.c`, sequentially for one prime/family at a time. It writes each deduplicated residue set (`r*_p1.txt`, etc.) and the union table. The P/Q enumerator checks its defining identities and unit filters; the union arithmetic itself uses integer residues and explicit lifting. All seven table rows were generated under the requested virtual-memory cap and timeout.

## Branch histograms

The finite trees are saved in `data/z78/exact/rtree17_d8.txt`, `rtree19_d6.txt`, and `rtree23_d6.txt`, copied from the existing exact tree outputs `data/z17/rtree*_d*.txt`; the shallow multi-prime census is `landscape_d4.txt` (source `data/z17/landscape_d4.txt`). These are finite-data replays, not newly extended searches.

For the key r = 17, in C₅ (and its inverse C₇) the exact new-box counts at depths 2–8 are `4, 23, 34, 83, 100, 272, 326`; the corresponding maximum numbers of new boxes in any alive parent are `4, 4, 2, 2, 2, 1, 1`. At depths 7 and 8 every new box has a distinct alive parent. Stored r = 19 data reaches depth 6 and r = 23 reaches depth 6: maxima in the surviving sample cells are respectively `7,5,1,1,1` (depths 2–6) and `8,5,3,2,1`. See the data files for per-cell histograms and exact alive fractions. These are observations at finite depth, not uniform bounds.

## Replay

```sh
ulimit -v 2000000
timeout 1800 uv run --offline --no-project python -B scripts/z78_exact_union.py 5 7 11 13 17 19 23
```

The script runs the C enumerator sequentially, with one enumeration process at a time. `union.tsv` is overwritten with exactly the primes passed on the command line. Tree histograms came from the stored z17 outputs noted above; they can be compared byte-for-byte with those source files.
