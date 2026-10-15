"""R249: r-adic tree from review_r249_rbox output. Usage: review_r249_rtree.py r Dmax boxfile"""
import sys
from collections import defaultdict
r, D, fn = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
boxes = defaultdict(set)
for line in open(fn):
    t, lev, res = line.split()[:3]
    boxes[int(lev)].add(int(res))
qr = {(x * x) % r for x in range(1, r)}
nonres = [v for v in range(1, r) if v not in qr]
surv = [v for v in nonres if v not in boxes[1]]
print("r=%d non-residue cells %d, surviving level 1: %s" % (r, len(nonres), surv))
for v in surv:
    alive = [v]; row = []
    for d in range(2, D + 1):
        M = r ** (d - 1); new = []; mx = 0; hist = defaultdict(int)
        for x in alive:
            nb = 0
            for i in range(r):
                y = x + i * M
                if y in boxes[d]: nb += 1
                else: new.append(y)
            mx = max(mx, nb); hist[nb] += 1
        alive = new
        row.append("d%d: max %d, alive frac %.4f, hist %s" % (d, mx, len(alive) / r ** (d - 1), dict(sorted(hist.items()))))
    print(" C_%d:" % v); print("   " + "\n   ".join(row))
