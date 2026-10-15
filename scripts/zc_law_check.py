"""zc_law_check.py (O226): check the root-product law (FF_ODD_ABSENCE Thm 1.2) on dumped Case B tuples (k = 1).
Input: lines 'T s a z y t E0 e0 | m w C g v' from zc_enum (DUMP = 1). For each tuple: re-verify m'wC = T^s + v,
w + C = g'v, T not dividing m'g'wCv, monic m', w, C, g'; E(0) = m'(0)g'(0)w(0) - 1 = w(0)/C(0); and
E(0)^s == eps := (-1)^{t + tz + z(1+s) + ts} * lam^{z + 2a - s}, lam = lc(v).
usage: zc_law_check.py q < dump"""
import sys
from collections import Counter
from zc_field import GF

q = int(sys.argv[1]); F = GF(q)
bad = 0; n = 0; dist = Counter()
for line in sys.stdin:
    if not line.startswith('T '):
        continue
    head, polys = line.split('|')
    h = head.split(); s, a, z, y, t = map(int, h[1:6]); e0d = int(h[7])
    m, w, C, g, v = [[int(c) for c in p.split(',')] for p in polys.split()]
    TS = [0] * s + [1]
    ok = (F.pmul(F.pmul(m, w), C) == F.padd(TS, v)) and (F.padd(w, C) == F.pmul(g, v))
    ok &= all(P[-1] == 1 and P[0] != 0 for P in (m, w, C, g)) and v[0] != 0
    ok &= (len(m) - 1, len(w) - 1, len(C) - 1, len(g) - 1, len(v) - 1) == (z, a, s - a - z, y, t)
    E0 = F.MUL[w[0]][F.INV[C[0]]]
    ok &= E0 == e0d == F.ADD[F.MUL[F.MUL[m[0]][g[0]]][w[0]]][F.NEG[1]]
    lam = v[-1]
    sg = (t + t * z + z * (1 + s) + t * s) % 2
    eps = F.pw(lam, (z + 2 * a - s) % (q - 1))
    if sg:
        eps = F.NEG[eps]
    ok &= F.pw(E0, s) == eps
    n += 1
    dist[(s, E0)] += 1
    if not ok:
        bad += 1
        if bad < 10:
            print("FAIL", line.strip())
print(f"q={q}: {n} tuples checked, {bad} failures")
for s in sorted(set(k[0] for k in dist)):
    print(s, dict(sorted((e, c) for (ss, e), c in dist.items() if ss == s)))
