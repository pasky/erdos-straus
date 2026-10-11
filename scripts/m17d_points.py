"""O139: which small-height rationals u = s/t (17-adic, in cell C_v) lie in no certified box?
Boxes: P-data DIR/p{K}.txt (K<=KP), Q/U DIR/{Q,U}{k}.txt (k<=KQ) and inverses, as in m17b_union.py.
Usage: m17d_points.py DIR KP KQ H [v]   -> prints uncovered s/t with |s|,t <= H, sorted by height.
"""
import sys, os
from math import gcd

D, KP, KQ, H = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
v = int(sys.argv[5]) if len(sys.argv) > 5 else 5
boxes = {}
def add(L, r):
    r %= 17 ** L
    if r % 17 == v: boxes.setdefault(L, set()).add(r)
for K in range(1, KP + 1, 2):
    L, n = (K + 1) // 2, 17 ** K
    for line in open(os.path.join(D, f"p{K}.txt")):
        a, b, c, d = map(int, line.split())
        assert 4 * a * b * c * d == a + b + n * c
        add(L, -(4 * a * c * d - 1)); add(L, -(4 * b * c * d - 1))
for T in "QU":
    for k in range(1, KQ + 1, 2):
        for line in open(os.path.join(D, f"{T}{k}.txt")):
            r = int(line.split()[1]); add(k, r)
            if r % 17: add(k, pow(r, -1, 17 ** k))
Lmax = max(boxes)
def covered(s, t):
    for L, S in boxes.items():
        if s * pow(t, -1, 17 ** L) % 17 ** L in S: return L
    return 0
out = []
for t in range(1, H + 1):
    if t % 17 == 0: continue
    for s in range(-H, H + 1):
        if s == 0 or gcd(s, t) != 1 or s % 17 == 0: continue
        if s * pow(t, -1, 17) % 17 != v: continue
        L = covered(s, t)
        out.append((max(abs(s), t), s, t, L))
out.sort()
unc = [(s, t) for h, s, t, L in out if L == 0]
print(f"levels<= {Lmax}: {len(out)} rationals of height<={H} in C_{v}, uncovered {len(unc)}")
print("uncovered (height order):", " ".join(f"{s}/{t}" for s, t in unc[:60]))
print("covered (s/t:level):", " ".join(f"{s}/{t}:{L}" for h, s, t, L in out if L)[:2000])
