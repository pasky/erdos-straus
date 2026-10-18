"""Brute-force cross-check of z34_scores output for small p: N1, fII, m0, S, e0 (EMAX >= 4000), and L_I.
usage: z34_check_scores.py scores.txt PMAX"""
import sys
from math import isqrt
rows = {int(l.split()[0]): list(map(int, l.split())) for l in open(sys.argv[1])}
PMAX = int(sys.argv[2])
def fac(n):
    f = {}; r = 2
    while r * r <= n:
        while n % r == 0: f[r] = f.get(r, 0) + 1; n //= r
        r += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divs(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
bad = 0
for p, (_, N1, F, M0, MP, S, E0, LI) in rows.items():
    if p > PMAX: break
    n1 = sum(1 for d in range(1, (p + 3) // 8 + 1) for w in divs(fac(p + 4 * d)) if w % (4 * d) == 4 * d - 1 and w < p + 4 * d)
    f = 0; m0 = None
    for m in range(3, p, 4):
        K = (p + m) // 4; f2 = {}
        for q, e in fac(K).items(): f2[q] = 2 * e
        c = sum(1 for dd in divs(f2) if (dd + K) % m == 0)
        f += c
        if c and m0 is None: m0 = m
    sl = set()
    for a in range(1, p + 1):
        N = p + 4 * a * a
        for g in divs(fac(N)):
            if g % (4 * a) == 4 * a - 1:
                k = (g + 1) // (4 * a); m = N // g; b = (p + m) // (4 * a)
                sl.add(g); sl.add(4 * k * b - 1)
    e0 = 0
    for e in range(3, 4000, 4):
        H = (p * e + 1) // 4; f2 = {q: 2 * v for q, v in fac(H).items()}
        if any((r + H) % e == 0 for r in divs(f2)): e0 = e; break
    li = 0
    for e in range(3, 200, 4):
        H = (p * e + 1) // 4; f2 = {q: 2 * v for q, v in fac(H).items()}
        li += any((r + H) % e == 0 for r in divs(f2))
    ok = (n1, f, m0 or -1, len(sl), e0, li) == (N1, F, M0, S, E0, LI)
    if not ok:
        bad += 1; print('MISMATCH', p, (n1, f, m0, len(sl), e0, li), (N1, F, M0, S, E0, LI))
print('checked p <=', PMAX, 'mismatches', bad)
sys.exit(1 if bad else 0)
