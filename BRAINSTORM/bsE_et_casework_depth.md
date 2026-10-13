# bsE_et_casework_depth — Elsholtz–Tao divisor casework beats O173's square root at depth T^s (O178)

## Idea
O173 (FUNCTIONFIELD_ES3 §3) bounded the Case B slice families of parameter s by q^{s/2} (square root) and called the needed
saving "a Kloosterman problem mod T^s". Two further identities, E | g'T^s + w and E | T^s + m'w² (DEPTH_ASPECT Lemma 2.1),
give four reconstruction maps. Their minimum is ≤ q^{2(s−3)/5} (Lemma 2.2, PROVED). Case A at generic slice points is ≤ q^{(α−1)/2}
(Lemma 2.4, PROVED).
## Literature
Elsholtz–Tao, arXiv:1107.1010 §3 (the n^{3/5}, n^{2/5} casework); Browning–Elsholtz, Illinois J. Math. 55 (2011).
## Barrier screen
This is a count of covering families, not an ES existence statement. B3 (scale) is respected: it bounds *coverings*. It has nothing
to do with ES at a given P. T1: n/a (F_q[T] has no odd-square obstruction for odd q, FUNCTIONFIELD_ES Prop 4.1).
## Cheap numerics
`scripts/bsE_famcount.c` (all tuples s ≤ 15 at q = 3, 0 identity failures) agrees with O173's `ff3_caseB` at 300 random slice points
in both directions (`scripts/bsE_crosscheck.py`: 1064 hits, 446 covering tuples, 0 mismatches). `scripts/bsE_caseA.py`: two
independent Case A enumerations agree (q = 3, α ≤ 6; q = 5).
## Assessment
**LIVE as a function-field theorem (PROVED); it gives Theorem 2.5 and, via the ℤ dictionary, Theorem 3.1.** At q = 3 itself the
exponents suffice but the constants do not (the union bound is 1.74 + 0.09 > 1).
