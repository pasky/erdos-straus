"""z17_iota.py (O242): check that the q = 3 ball set (file "depth digits", digits = u mod T^depth, low first) is invariant
under iota(u)(T) = 1/u(-T) (SIBLING Prop 1.4), and under u -> u(-T) composed with c -> -c (slice swap), and count iota-fixed
balls.  usage: python3 scripts/z17_iota.py data/z16/balls_d9.txt"""
import sys
from collections import defaultdict
P = 3
def inv(u):            # power-series inverse mod T^len(u), u[0] != 0
    n = len(u); r = [0] * n; i0 = pow(u[0], P - 2, P)
    for i in range(n):
        s = (1 if i == 0 else 0) - sum(u[j] * r[i - j] for j in range(1, i + 1))
        r[i] = s * i0 % P
    return r
def neg(u): return [x * (-1) ** i % P for i, x in enumerate(u)]
balls = defaultdict(set)
for line in open(sys.argv[1]):
    d, s = line.split(); balls[int(d)].add(tuple(map(int, s)))
bad = fix = tot = 0
for d, S in balls.items():
    for u in S:
        tot += 1; im = tuple(inv(neg(list(u))))
        if im not in S: bad += 1
        if im == u: fix += 1
print(f"balls {tot}, iota-images missing {bad}, iota-fixed balls {fix}")
