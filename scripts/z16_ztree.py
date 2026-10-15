"""z16_ztree.py (O241): r = 17 analogue of z16_tree — alive tree of a non-residue cell C_v of the 17-generic line.
Boxes exactly as scripts/m17d_points.py / m17b_union.py: P-data DIR/p{K}.txt (K odd, level L = (K+1)/2, boxes -(4acd-1),
-(4bcd-1) mod 17^L) and Q/U box files DIR/{Q,U}{k}.txt (k odd) with their inverses. Complete through depth DMAX when
P files exist for K <= 2*DMAX - 1 and Q/U for k <= DMAX.  Prints per depth: boxes in the cell, alive count/fraction and the
histogram of #boxed children (out of 17) over alive parents (17 would kill the parent).
usage: python3 scripts/z16_ztree.py DIR DMAX [v]"""
import sys, os
from collections import Counter
D, DMAX = sys.argv[1], int(sys.argv[2]); v = int(sys.argv[3]) if len(sys.argv) > 3 else 5
R = 17; boxes = {}
def add(L, r):
    r %= R ** L
    if r % R == v: boxes.setdefault(L, set()).add(r)
for K in range(1, 2 * DMAX, 2):
    L, n = (K + 1) // 2, R ** K
    for line in open(os.path.join(D, f"p{K}.txt")):
        a, b, c, d = map(int, line.split()); assert 4 * a * b * c * d == a + b + n * c
        add(L, -(4 * a * c * d - 1)); add(L, -(4 * b * c * d - 1))
for T in "QU":
    for k in range(1, DMAX + 1, 2):
        for line in open(os.path.join(D, f"{T}{k}.txt")):
            r = int(line.split()[1]); add(k, r)
            if r % R: add(k, pow(r, -1, R ** k))
alive = [v] if v not in boxes.get(1, set()) else []
print(f"cell C_{v}: alive at depth 1: {len(alive)}")
for n in range(2, DMAX + 1):
    B = boxes.get(n, set()); hist = Counter(); new = []
    for x in alive:
        ch = [x + j * R ** (n - 1) for j in range(R)]
        nb = sum(1 for y in ch if y in B); hist[nb] += 1
        new.extend(y for y in ch if y not in B)
    alive = new
    print(f"depth {n}: boxes {len(B)} (rel.mass {len(B)/R**(n-1):.5f}), alive {len(alive)} (frac {len(alive)/R**(n-1):.4f}), "
          f"alive parents by #boxed children {dict(sorted(hist.items()))}")
