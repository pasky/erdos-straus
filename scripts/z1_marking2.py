"""z1: mixed isometry classes for S_M restricted to n coprime to M (odd n < N)."""
import sys
from math import gcd
from cf_lib import words
from ce_classes import canon
N = int(sys.argv[1]); Ms = list(range(2, 31))
mixed = {M: 0 for M in Ms}; ex = {}; trivial = {M: True for M in Ms}
for n in range(3, N, 2):
    cls = {}
    for w in words(n):
        t, u, v = w
        cls.setdefault(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]), []).append(w)
    for M in Ms:
        if gcd(n, M) > 1: continue
        for k, ws in cls.items():
            s = {any(x % M == 0 for x in (t, u, v, t*u-1, t*v-1)) for (t, u, v) in ws}
            if s != {True}: trivial[M] = False
            if len(s) > 1:
                mixed[M] += 1; ex.setdefault(M, (n, ws))
for M in Ms:
    print(M, 'mixed', mixed[M], 'S_M = all words' if trivial[M] else '', ex.get(M, ''))
