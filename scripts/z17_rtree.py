"""z17_rtree.py (O242): alive tree of every non-residue cell C_v of the r-generic line, without listing alive cylinders.
Boxes as in scripts/z16_ztree.py (P-data DIR/p{K}.txt both boxes -(4acd-1), -(4bcd-1) mod r^((K+1)/2); Q/U box files
DIR/{Q,U}{k}.txt with inverses).  A box is NEW if no box of lower level contains it; covered mass = sum of new boxes.
For every parent holding >= 1 new box of level n we test aliveness (no box of level <= n-1 contains it) and histogram the
number of boxed children over ALIVE parents (17 = r would kill the parent).  Complete through depth DMAX when P files exist
for K <= 2 DMAX - 1 and Q/U for k <= DMAX.  Exact rationals for the alive fraction.
usage: python3 scripts/z17_rtree.py DIR DMAX r"""
import sys, os
from fractions import Fraction
from collections import defaultdict, Counter
D, DMAX, R = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
boxes = defaultdict(set)
def add(L, x):
    if L <= DMAX: boxes[L].add(x % R ** L)
for K in range(1, 2 * DMAX, 2):
    L, n = (K + 1) // 2, R ** K
    for line in open(os.path.join(D, f"p{K}.txt")):
        a, b, c, d = map(int, line.split()); assert 4 * a * b * c * d == a + b + n * c and c % R and d % R
        add(L, -(4 * a * c * d - 1)); add(L, -(4 * b * c * d - 1))
for T in "QU":
    for k in range(1, DMAX + 1, 2):
        for line in open(os.path.join(D, f"{T}{k}.txt")):
            x = int(line.split()[1]); add(k, x)
            if x % R: add(k, pow(x, -1, R ** k))
def covered_below(x, n):          # is the class x mod R^n inside a box of level <= n ?
    return any(x % R ** L in boxes[L] for L in range(1, n + 1))
nonres = sorted(set(range(1, R)) - {i * i % R for i in range(1, R)})
print(f"r = {R}: non-residues {nonres}; level-1 boxes {sorted(boxes[1])}")
for v in nonres:
    if v in boxes[1]: print(f"  cell C_{v}: covered at level 1"); continue
    alive = Fraction(1); line = []
    for n in range(2, DMAX + 1):
        new = [x for x in boxes[n] if x % R == v and not covered_below(x, n - 1)]
        alive -= Fraction(len(new), R ** (n - 1))
        par = Counter(x % R ** (n - 1) for x in new)
        hist = Counter(par.values()); mx = max(par.values()) if par else 0
        line.append(f"d{n}: new {len(new)}, alive {float(alive):.5f}, max {mx}, hist {dict(sorted(hist.items()))}")
    print(f"  cell C_{v}:"); [print("    " + s) for s in line]
