"""review_r248_ztree.py (R248, own code): r = 17 alive tree of cell C_v WITHOUT materialising the alive set.
Boxes: R83 engine scripts/review_m17_enum.c outputs (S k: "S a m d" -> II2 boxes -4a^2d, -4m^2d and I2 boxes -m/a, -a/m mod 17^k;
U k: "U e ..." -> -e, -1/e mod 17^k; P K: "P f j a' d' i" -> -f, -f* (f* = 4a'd'j - 1) mod 17^((K+1)/2)), or stored data/m17b p{K}.txt
("a b c d", f = 4acd-1, f* = 4bcd-1) for P files not regenerated.  A level-L box is *new* iff no box of lower level contains it;
dead mass at depth n = sum over new boxes of 17^(1-L) (cell has mass 1 at depth 1); sibling histogram at depth n = new
level-n boxes grouped by parent (parents of new boxes are alive).
usage: python3 scripts/review_r248_ztree.py DIR DMAX v   (DIR has S{k}.txt U{k}.txt P{K}.txt or p{K}.txt)"""
import sys, os
from collections import Counter, defaultdict
D, DMAX, v = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); R = 17
boxes = defaultdict(set)
def add(L, r):
    r %= R ** L
    if r % R == v: boxes[L].add(r)
def inv(x, m): return pow(x % m, -1, m) if x % R else None
for k in range(1, DMAX + 1, 2):
    F = R ** k
    for line in open(os.path.join(D, f"S{k}.txt")):
        t = line.split()
        if t[0] != "S": continue
        a, m, d = map(int, t[1:4])
        add(k, -4 * a * a * d); add(k, -4 * m * m * d)
        if a % R: add(k, -m * inv(a, F))
        if m % R: add(k, -a * inv(m, F))
    for line in open(os.path.join(D, f"U{k}.txt")):
        t = line.split()
        if t[0] != "U": continue
        e = int(t[1]); add(k, -e)
        if e % R: add(k, -inv(e, F))
src = {}
for K in range(1, 2 * DMAX, 2):
    L = (K + 1) // 2; fP = os.path.join(D, f"P{K}.txt")
    if os.path.exists(fP) and os.path.getsize(fP) > 0:
        src[K] = "R83"
        for line in open(fP):
            t = line.split()
            if t[0] == "P":      # R83 format "P f j a' d' i": f = 4a'd'i - 1, f* = 4a'd'j - 1
                    fz, j, ap, dp, i = map(int, t[1:6]); assert fz == 4 * ap * dp * i - 1 and 4 * ap * dp * i * j == i + j + R ** K * ap
                    add(L, -fz); add(L, -(4 * ap * dp * j - 1))
    else:
        src[K] = "stored"; N = R ** K
        for line in open(os.path.join(D, f"p{K}.txt")):
            a, b, c, d = map(int, line.split()); assert 4 * a * b * c * d == a + b + N * c and c % R and d % R
            add(L, -(4 * a * c * d - 1)); add(L, -(4 * b * c * d - 1))
print("P sources:", src)
dead = 0.0; alive_prev = 1
for n in range(1, DMAX + 1):
    new = [r for r in boxes.get(n, ()) if not any((r % R ** L) in boxes.get(L, ()) for L in range(1, n))]
    par = Counter(r % R ** (n - 1) for r in new) if n > 1 else Counter()
    hist = Counter(par.values()); hist[0] = alive_prev - len(par)
    dead += len(new) * R ** (1 - n)
    alive = round((1 - dead) * R ** (n - 1))
    print(f"depth {n}: boxes {len(boxes.get(n, ()))}, new {len(new)}, alive {alive} (frac {1 - dead:.4f}), "
          f"max boxed children {max(par.values()) if par else 0}, hist {dict(sorted(hist.items()))}")
    alive_prev = alive
