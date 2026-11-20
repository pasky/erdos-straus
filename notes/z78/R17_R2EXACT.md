Result: Exact sparse native-modulus L1/P3/Q3/P5 marginal centre lists and census for all primes 211<r<919 plus r=929. Label: CERTIFIED (exact integer enumeration; independent cell-by-cell replay against the stored exact-family sets at r=211)
Scope: The r-generic line, depth-three boxes only; counts are native-modulus marginal centres, with each deeper family excluding all preceding families. This is not an ES or sterility claim.
Review: none (parent hostile review pending)
Triage: DATA
STATUS delta: none

## Row format (defined before the census)

`data/z78/r2exact/rows.tsv` has tab-separated columns `r L1 P3marg Q3marg P5marg`. Counts are *native-modulus* distinct centre residues: L1 modulo `r`, P3 modulo `r²`, Q3 modulo `r³`, and P5 modulo `r³`. The L1 set is P1∪Q1 restricted to nonsquare unit residues. P3 contains only nonsquare centres not already covered by L1; Q3 excludes L1 and P3; P5 excludes L1, P3, and Q3. These are marginal set cardinalities, not tuple counts or common-depth-three-scaled counts.

Each `data/z78/r2exact/logs/rR.txt` is the plain-text full run for one prime and ends with its `ROW` line. The census has 111 rows for 211<r<919 plus 929; the separate `r=211` row is retained as the cross-check anchor (112 total rows). It includes primes 223, 229, 907, 911, 919 and 929. At 929 the row is `929 48 458 888 1570`.

## Independent engine and replay

`scripts/z78_r2exact.c` is a standalone C implementation of the exact P3, Q3 and P5 tuple enumerations, plus level 1. It does not call or link `z78_xr_exact.c`. It uses independent deterministic Miller–Rabin/Pollard–Brent factorization, prime-exponent allocation for complete ordered factorizations, and open-addressed sparse hash sets for all recorded centre sets. No r² or r³ bitmap/universe is allocated. The only residue-sized byte arrays are the O(r) first-digit square/alive flags. At r=929 the actual process completed in 68.1 s with 1,432 KiB reported maximum RSS; the sparse centre sets themselves are also included in this run.

Completeness split: P3 fully factors/enumerates `(r³+e)/4` for `e<4 ceil(sqrt(r³))`, then uses the complementary `a,c,d` parameterization for larger e. Q3 enumerates the complete small-e part `e<2r²`, the complementary small-f part `f<2r²`, then the exact divisor search for the both-large region with its derived `c²d` bound. P5 enumerates all `(r⁵+e)/4` factorizations for `e<16r²`, then the complementary large-e parameterization. Every recovered tuple is checked against its defining equation; unit, ordering and positivity conditions are applied before either oriented centre is marked. Distinct centres are deduplicated in their own native modulus, and parent membership is tested by reduction modulo the earlier native modulus. Arithmetic bounds in these ranges fit the checked unsigned-64-bit products; wider intermediates are used for modular multiplication and Q3 bound expressions. Factorization and divisor-allocation guards assert on overflow or excess divisor count.

Build and one-prime replay (≤2,000,000 KiB virtual memory; ≤1,800 s per prime):

```sh
gcc -O3 scripts/z78_r2exact.c -o data/z78/r2exact/z78_r2exact
timeout 1800 bash -c 'ulimit -v 2000000; data/z78/r2exact/z78_r2exact 929'
```

Resumable census chunks use only one worker, skip successfully logged primes, and put one plain-text log per prime:

```sh
timeout 1800 bash -c 'ulimit -v 2000000; uv run --offline --no-project python -B scripts/z78_r2exact.py 212 350'
timeout 1800 bash -c 'ulimit -v 2000000; uv run --offline --no-project python -B scripts/z78_r2exact.py 351 550'
timeout 1800 bash -c 'ulimit -v 2000000; uv run --offline --no-project python -B scripts/z78_r2exact.py 551 750'
timeout 1800 bash -c 'ulimit -v 2000000; uv run --offline --no-project python -B scripts/z78_r2exact.py 751 929'
```

The driver has a 1,800-second timeout per prime and a 2,000,000-KiB address-space cap on the worker. To regenerate `rows.tsv`, gather the unique `ROW` line from each successful per-prime log and sort by r; the currently committed table includes r=211 as a validation anchor. No auth/quota issues occurred.

## Replayable native centre lists

To emit all four complete *marginal* centre lists for any supported individual prime, create an output prefix in an owned data directory and run:

```sh
mkdir -p data/z78/r2exact/lists/r929
timeout 1800 bash -c 'ulimit -v 2000000; data/z78/r2exact/z78_r2exact 929 --dump-prefix data/z78/r2exact/lists/r929/centres'
```

This writes `centres.L1.tsv`, `centres.P3.tsv`, `centres.Q3.tsv`, and `centres.P5.tsv`. Each begins with a comment giving r, family and native modulus, followed by one sorted decimal residue per line. The L1 file contains only nonsquare residues; the other files are the ordered marginal sets described above. Dump mode adds only O(number of emitted centres) temporary memory and does not create an r³ bitmap. This is the exact-depth-three parent membership input for a subsequent P7 step.

## Validation

At r=211, all four sparse marginal lists were compared element-for-element with the independently stored exact-family outputs `data/z78/exact/r211_{p1,q1,p3,q3,p5}.txt`, after independently applying the nonsquare and earlier-parent exclusions. All four sets were identical: cardinalities L1/P3/Q3/P5 = 37/158/422/512. These agree with `data/z78/exact/union.tsv` after converting its common-depth-three normalization back to native moduli. The reviewer engine `scripts/z78_xr_exact.c` was also run at r=211 and returned the same four counts (37/158/422/512). The census outputs at r=223, 229 and 907, 911, 919, 929 are included as requested; no independent stored full-set oracle exists there. The exact row at 929 agrees with the existing separate level ledger for L1 and P3, while Q3/P5 are direct exact counts rather than prior bounds.

The finite enumeration certifies only these exact row values and lists. A nonzero residual at depth 3 makes no claim about all-depth survival.

## Independent native-list cross-check at 223 and 929

All four primary marginal lists were compared cell-for-cell at r=223 and r=929 against separate enumerations; machine result is `data/z78/r2exact/validation.tsv`.

* **L1 and P3:** `scripts/z78_r2exact_cf.c` is the segmented-shift P3 engine (`scripts/z78_p3_exact.c`) instrumented to emit its native sets. It uses the shift-factorization / complementary large-shift parameterization, not the pointwise reviewer engine's e split. Its P1+Q1 level-1 union and P3 cells agree exactly with the primary lists at both primes.
* **Q3:** `scripts/z78_r2exact_qalt.c` reruns exact Q3 with a genuinely different complementary partition: small `e < r²`, small `f < 3r²` subject to `e ≥ r²`, then the both-large divisor region. The primary split is `e < 2r²`, `f < 2r²` subject to `e ≥ 2r²`. It emits all four lists; its Q3 marginal list agrees cell-for-cell at both primes. It uses sparse native-modulus sets throughout. This is a changed-cut exact census, not a distinct divisor identity.
* **P5:** the R1 four-regime `scripts/z78_exact_et.cpp` was attempted at r=223, but aborts before output with `cd factor input exceeds uint64`; it cannot certify these sample rows as written. Instead `scripts/z78_r2exact_p5small.c` exactly factors/enumerates all shifts `e < E=16r²` for `N=r⁵`, and `scripts/z78_r2exact_p5cf.c` uses the convergent/continued-fraction enumeration for the complementary `e ≥ E` region. Their raw oriented centre union, after nonsquare and L1/P3/Q3 parent exclusions, matches the primary P5 marginal list element-for-element at both primes. Raw independent lists and each component's plain-text output are retained as `independent{223,929}.P5raw.tsv`, `independent{223,929}.p5small.txt`, and `independent{223,929}.p5cf.txt`.

The independent list provenance is preserved in `independent{223,929}.cf.tsv` (L1/P3) and `independent{223,929}.qalt.Q3.tsv` (Q3), alongside the primary `sample{223,929}.{L1,P3,Q3,P5}.tsv`. Counts agree as follows:

| r | L1 | P3 | Q3 | P5 |
|---:|---:|---:|---:|---:|
| 223 | 39 | 218 | 422 | 580 |
| 929 | 48 | 458 | 888 | 1570 |

Replay the independent generators from the repository root (each run sequential, with the same 2,000,000-KiB cap and ≤1,800-second timeout):

```sh
gcc -O3 scripts/z78_r2exact_cf.c -o /tmp/r2cf
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/r2cf 223 223 > data/z78/r2exact/independent223.cf.tsv'
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/r2cf 929 929 > data/z78/r2exact/independent929.cf.tsv'
gcc -O3 scripts/z78_r2exact_qalt.c -o /tmp/qalt
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/qalt 223 --dump-prefix data/z78/r2exact/independent223.qalt'
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/qalt 929 --dump-prefix data/z78/r2exact/independent929.qalt'
gcc -O3 scripts/z78_r2exact_p5small.c -o /tmp/p5small
gcc -O3 scripts/z78_r2exact_p5cf.c -o /tmp/p5cf
# For each r, E=16*r*r, N=r^5, T=(floor(N/E)+1)//2.
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/p5small 929 13808656 > data/z78/r2exact/independent929.p5small.txt'
timeout 1800 bash -c 'ulimit -v 2000000; /tmp/p5cf 929 5 13808656 1 25055159 > data/z78/r2exact/independent929.p5cf.txt'
```

(The same P5 commands use E=795664 and T=346549 for r=223.) `uv run --offline --no-project python -B scripts/z78_r2exact_validate.py` replays the eight cell-set comparisons and rewrites `validation.tsv`; it fails on any list mismatch. The report records exact set equality, not just matching cardinalities.