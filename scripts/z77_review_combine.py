"""Opus review (z77): independent re-implementation of the z77 combiner with source attribution.
Reads the same tables; written separately from z77_combine.py. Run from repo root."""
from pathlib import Path
from fractions import Fraction as Fr
from decimal import Decimal
from math import isqrt
from collections import Counter
import sys

def load(path):
    d = {}
    for line in Path(path).read_text().splitlines():
        if line.startswith('#'):
            continue
        parts = line.split()
        j = int(parts[0]); v = Fr(Decimal(parts[1])) * (1 + Fr(1, 10**9))
        assert j not in d
        d[j] = -((-v.numerator) // v.denominator)
    return d

PT = [(4, load('data/se/P_q4.txt'), 'SE_P4'), (1, load('data/se/P_q1.txt'), 'SE_P1'),
      (1, load('data/zl/P_q1_hi.txt'), 'ZL_P1hi'), (32, load('data/zl/P_q32.txt'), 'ZL_P32')]
QT = [(4, load('data/se/Q_q4.txt'), 'SE_Q4'), (32, load('data/zl/Q_q32.txt'), 'ZL_Q32')]
def rows(p): return [list(map(int, l.split())) for l in Path(p).read_text().splitlines()]
routes = {b: v for b, j, v in rows('data/z77/routes.txt')}
fine = {b: v for b, j, v in rows('data/z77/fine.txt')}
qtab = {b: v for b, j, v in rows('data/z77/q.txt')}
lev1 = {r: c for r, p, q, c in rows('data/z77/level1.txt')}
p3 = {r: s for r, *s in rows('data/z77/p3.txt')}

def tabidx(q, N):
    # largest j with 2^j <= N^q
    return (N**q).bit_length() - 1

def Pbound(N, r, K):
    c = []
    for q, t, nm in PT:
        j = tabidx(q, N)
        if j in t: c.append((2*t[j], nm))
    B = N.bit_length()  # 2^(B-1) <= N < 2^B
    for bb, v in routes.items():
        if B <= bb <= B + 5: c.append((v, 'routes%d' % bb))
    if B in fine: c.append((fine[B], 'fine'))
    if K == 3 and r in p3:
        for j, s in enumerate(p3[r]):
            E = r * 2**j
            T = (N // E + 1) // 2
            full, rem = divmod(T, r)
            c.append((s + 2*(full*((r-1)//2) + min(rem, (r-1)//2)), 'p3_%d' % j))
    return min(c)

def Qbound(N):
    c = []
    for q, t, nm in QT:
        j = tabidx(q, N)
        if j in t: c.append((2*t[j], nm))
    if N.bit_length() in qtab: c.append((qtab[N.bit_length()], 'zq'))
    return min(c)

def total(r, src):
    s = Fr(lev1[r], r)
    for K in range(3, 1000, 2):
        N = r**K
        if N >= 2**800: break
        v, nm = Pbound(N, r, K); src[('P', K if K <= 7 else 9, nm)] += 1
        s += Fr(v, r**((K+1)//2))
    for k in range(3, 1000, 2):
        N = r**k
        if N >= 2**100: break
        v, nm = Qbound(N); src[('Q', k, nm)] += 1
        s += Fr(v, r**k)
    s += Fr(16, 100*isqrt(r)) + Fr(4, 100000)
    return s

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    src = Counter(); worst = None; fails = []
    for r in sorted(lev1):
        if not (lo <= r < hi): continue
        s = total(r, src)
        if s >= Fr(r-1, 2*r): fails.append(r)
        if worst is None or s > worst[0]: worst = (s, r)
    print('fails', fails[-5:], 'n', len(fails))
    print('worst', float(worst[0]), worst[1])
    for k, v in sorted(src.items(), key=lambda x: (x[0][0], x[0][1], -x[1])): print(k, v)
