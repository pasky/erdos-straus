"""fz1_brute.py (O220): independent brute force of the k = 1 tuples (B^{k=1}) (FF_STERILE_SMALL §6) over F_p:
all monic T-free (m', w, C) with z + a + b = s; v = m'wC - T^s must be nonzero with v(0) != 0, and w + C = g'v with g'
monic, g'(0) != 0. Prints "s a z y t count" for a <= b (a = b: both orders), to compare with fz1_enum.
usage: fz1_brute.py p SMAX"""
import sys, itertools
from collections import Counter
p = int(sys.argv[1]); SMAX = int(sys.argv[2])
def monic(d):   # T-free monic polys of degree d, coefficient lists low->high
    if d == 0: yield (1,); return
    for c in itertools.product(range(p), repeat=d):
        if c[0]: yield tuple(c) + (1,)
def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return r
def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def add(a, b):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])
def divmod_(a, b):
    a = trim(a); q = [0] * max(1, len(a) - len(b) + 1); inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a:
        f = a[-1] * inv % p; sh = len(a) - len(b); q[sh] = f
        for i, x in enumerate(b): a[sh + i] = (a[sh + i] - f * x) % p
        a = trim(a)
    return trim(q), a
for s in range(2, SMAX + 1):
    cnt = Counter()
    for a in range(0, s + 1):
        for b in range(0, s + 1 - a):
            z = s - a - b
            for m in monic(z):
                for w in monic(a):
                    mw = mul(m, w)
                    for C in monic(b):
                        P = mul(mw, C); P[s] = (P[s] - 1) % p; v = trim(P)
                        if not v or v[0] == 0: continue
                        g, r = divmod_(add(w, C), v)
                        if r or not g or g[-1] != 1 or g[0] == 0: continue
                        if a <= b: cnt[(s, a, z, len(g) - 1, len(v) - 1)] += 1
    for k in sorted(cnt): print(*k, cnt[k])
