"""zc_brute.py (O226): independent brute force of the k = 1 Case B tuples (B^{k=1}) over F_q (zc_field), all monic T-free
(m', w, C) with z + a + b = s; v = m'wC - T^s nonzero with v(0) != 0; w + C = g'v with g' monic, g'(0) != 0.
Checks Thm 1.2 (E(0)^s = eps) on every tuple and prints per pattern (a <= b) the number of tuples with E(0) in the
primitive set {x : x^4 != 1} (q = 9 primitive slices) and the total, as "s a z y t prim total".
usage: zc_brute.py q SMIN SMAX"""
import sys, itertools
from collections import Counter
from zc_field import GF

q = int(sys.argv[1]); s0 = int(sys.argv[2]); s1 = int(sys.argv[3]); F = GF(q)

def monic(d):
    if d == 0:
        yield [1]; return
    for c in itertools.product(range(q), repeat=d):
        if c[0]:
            yield list(c) + [1]

bad = 0
for s in range(s0, s1 + 1):
    prim = Counter(); tot = Counter()
    for a in range(s + 1):
        for b in range(s + 1 - a):
            z = s - a - b
            Ms = list(monic(z)); Ws = list(monic(a)); Cs = list(monic(b))
            for m in Ms:
                for w in Ws:
                    mw = F.pmul(m, w)
                    for C in Cs:
                        P = F.pmul(mw, C)
                        P[s] = F.ADD[P[s]][F.NEG[1]]
                        v = F.trim(P)
                        if not v or v[0] == 0:
                            continue
                        g, rem = F.pdivmod(F.padd(w, C), v)
                        if rem or not g or g[-1] != 1 or g[0] == 0:
                            continue
                        t = len(v) - 1; y = len(g) - 1
                        E0 = F.MUL[w[0]][F.INV[C[0]]]
                        lam = v[-1]
                        eps = F.pw(lam, (z + 2 * a - s) % (q - 1))
                        if (t + t * z + z * (1 + s) + t * s) % 2:
                            eps = F.NEG[eps]
                        if F.pw(E0, s) != eps:
                            bad += 1
                        if a <= b:
                            key = (s, a, z, y, t); tot[key] += 1
                            if E0 not in F.prime_sub and F.pw(E0, 4) != 1:
                                prim[key] += 1
    for k in sorted(tot):
        print(*k, prim[k], tot[k])
print("law failures:", bad)
