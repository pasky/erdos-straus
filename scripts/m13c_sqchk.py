# empirical: does every class residue r mod M fail to be a "square" at some prime power of M?
from mordell_lib import residue_table, factor_small
from collections import Counter
def issq_local(r, q, e):
    if q == 2:
        if e == 1: return True
        if e == 2: return r % 4 == 1
        return r % 8 == 1
    return pow(r % q, (q - 1) // 2, q) == 1
bad = Counter(); nres = 0
for M in range(3, 6001):
    w = residue_table(M)
    f = factor_small(M)
    for r in w:
        nres += 1
        ns = [q for q, e in f.items() if not issq_local(r, q, e)]
        if not ns: bad['allsq'] += 1
        elif len(ns) == 1: bad[('only', ns[0])] += 1
print(nres, bad.most_common(12))
