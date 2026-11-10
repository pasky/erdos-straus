# z70 LOOSE item 4, POST-HOC null recalibration v2 (after internal review): the 2-ADIC local null.
# For p = 1 (mod 8) the 2-adic points of T^2 - p U^2 = -1 are: T uniform in 4Z_2, U = +-sqrt((T^2+1)/p) (two roots).
# Projected to Z/2^v (v >= 2): uniform on S_v = {(T,U) mod 2^v : T = 0 (4), p U^2 = T^2 + 1 (mod 2^(v+1))}
# (U mod 2^v is fixed up to sign by U^2 mod 2^(v+1); T^2 mod 2^(v+1) depends only on T mod 2^v; |S_v| = 2^(v-1)).
# Full null for l = 2^v m (m odd): uniform on {conic mod m} x S_v (CRT).  v <= 1: the plain conic mod l is already exact.
# usage: recal2.py in.jsonl(.gz) out.jsonl(.gz)
import sys, json, gzip
import numpy as np
sys.path.insert(0, 'scripts')
from z70_loose_pell import targets_T, null_prob
def v2(l): return (l & -l).bit_length() - 1
def null_prob_2adic(p, l):
    v = v2(l)
    if v <= 1: return null_prob(p, l)
    m = l >> v; P = 1 << (v + 1)
    U = np.arange(l, dtype=np.int64)
    r = ((p % l) * ((U * U) % l) - 1) % l
    TT = targets_T(U, l)
    ok = ((TT * TT) % l == r[:, None]) & (TT % 4 == 0) & ((((p % P) * ((U * U) % P))[:, None] - (TT * TT) % P - 1) % P == 0)
    TTs = np.where(ok, TT, -1); TTs.sort(axis=1)
    distinct = (TTs[:, 1:] != TTs[:, :-1]) & (TTs[:, 1:] >= 0)
    hits = distinct.sum(axis=1) + (TTs[:, 0] >= 0)
    hits[0] = 0                                   # U = 0 mod l is even: no admissible point (U must be odd)
    Um = np.arange(m, dtype=np.int64)
    sqm = np.bincount((Um * Um) % m, minlength=m) if m > 1 else np.array([1])
    Cm = int(sqm[((p % m) * ((Um * Um) % m) - 1) % m].sum()) if m > 1 else 1
    total = Cm * (1 << (v - 1))
    return float(hits.sum()) / total
def main():
    fo = (gzip.open if sys.argv[2].endswith('.gz') else open)(sys.argv[2], 'wt')
    for line in (gzip.open if sys.argv[1].endswith('.gz') else open)(sys.argv[1], 'rt'):
        r = json.loads(line); p = r['p']
        for row in r['rows']:
            if v2(row['l']) >= 2: row['P0'] = null_prob_2adic(p, row['l'])
            for d in row.get('dec') or []:
                if v2(d[0]) >= 2: d[2] = null_prob_2adic(p, d[0])
        fo.write(json.dumps(r) + '\n')
if __name__ == '__main__':
    main()
