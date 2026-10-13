# ec_bases.py — quick survey of other bases: n = k*b^m + c with n odd; least L in a list admitting an ET+divisor covering.
import sys, functools
import mordell_lib as ML
import ec_cover as EC
ML.residue_table = functools.lru_cache(maxsize=4000)(ML.residue_table)
b, c, kmax, Mmax = map(int, sys.argv[1:5])
Ls = [int(x) for x in sys.argv[5:]]
res = {}
for k in range(1, kmax + 1):
    if k % b == 0 or (k * b + c) % 2 == 0:
        continue
    f = None
    for L in Ls:
        ch = EC.search(k, L, Mmax, b, c, verbose=False)
        if ch:
            f = (L, len(ch)); break
    res[k] = f
print('b=%d c=%+d: covered %d / %d; uncovered k: %s' % (b, c, sum(1 for v in res.values() if v), len(res), [k for k, v in res.items() if not v]))
