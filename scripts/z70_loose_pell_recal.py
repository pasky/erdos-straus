# z70 LOOSE item 4, POST-HOC null recalibration (disclosed): for p = 1 (mod 8) the negative-Pell solution has T = 0 (mod 4)
# (T^2 = pU^2 - 1 = 0 mod 8 with U odd), which the conic mod l does not see when v2(l) = 2.  The corrected exact null for
# v2(l) = 2 is the uniform measure on the conic mod l restricted to T = 0 (mod 4) (= projection of the conic mod lcm(l,8)).
# Rewrites P0 for v2 = 2 letters and decoys; other rows unchanged.  usage: recal.py in.jsonl out.jsonl
import sys, json, gzip
import numpy as np
sys.path.insert(0, 'scripts')
from z70_loose_pell import targets_T
def null_prob4(p, l):
    U = np.arange(l, dtype=np.int64)
    T4 = np.arange(0, l, 4, dtype=np.int64)
    sq = np.bincount((T4 * T4) % l, minlength=l)          # roots with T = 0 mod 4
    r = ((p % l) * ((U * U) % l) - 1) % l
    total = int(sq[r].sum())
    TT = targets_T(U, l)
    ok = ((TT * TT) % l == r[:, None]) & (TT % 4 == 0)
    TTs = np.where(ok, TT, -1); TTs.sort(axis=1)
    distinct = (TTs[:, 1:] != TTs[:, :-1]) & (TTs[:, 1:] >= 0)
    hits = distinct.sum(axis=1) + (TTs[:, 0] >= 0)
    hits[0] = sq[r[0]]
    return float(hits.sum()) / total if total else None
def v2(l): return (l & -l).bit_length() - 1
def main():
  fo = (gzip.open if sys.argv[2].endswith('.gz') else open)(sys.argv[2], 'wt')
  for line in (gzip.open if sys.argv[1].endswith('.gz') else open)(sys.argv[1], 'rt'):
    r = json.loads(line); p = r['p']
    for row in r['rows']:
        if v2(row['l']) == 2: row['P0'] = null_prob4(p, row['l'])
        for d in row.get('dec') or []:
            if v2(d[0]) == 2: d[2] = null_prob4(p, d[0])
    fo.write(json.dumps(r) + '\n')
if __name__ == '__main__':
    main()
