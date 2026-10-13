"""O197: statistics of complete solution counts f_m(p) (from ms_census c-mode files data/ms/counts_m{m}.txt).
usage: ms_stats.py m1 m2 ...  -> per window: mean f, mean f/log^3 p, min f, and m*mean relative to m=4."""
import sys, math
from collections import defaultdict


def load(m, d='data/ms'):
    out = {}
    for line in open(f'{d}/counts_m{m}.txt'):
        p, c, ce, co, t1, t2 = map(int, line.split())
        out[p] = (c, ce, co, t1, t2)
    return out


if __name__ == '__main__':
    ms = [int(a) for a in sys.argv[1:]]
    D = {m: load(m) for m in ms}
    wins = [(100, 300), (300, 1000), (1000, 3000), (3000, 10000), (10000, 20000)]
    for lo, hi in wins:
        row = []
        base = None
        for m in ms:
            ps = [p for p in D[m] if lo <= p < hi and p % 2 and m % p]
            mean = sum(D[m][p][0] for p in ps) / len(ps)
            nl3 = sum(D[m][p][0] / math.log(p) ** 3 for p in ps) / len(ps)
            mn = min(D[m][p][0] for p in ps)
            if base is None:
                base = mean * ms[0]
            row.append(f"m={m}: {mean:7.2f} {nl3:.3f} min {mn:3d} m*mean/(4*mean4) {m*mean/base:.2f}")
        print(f"[{lo},{hi}) " + " | ".join(row))
