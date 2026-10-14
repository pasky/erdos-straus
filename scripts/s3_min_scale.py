"""O208 memo s3_min_scale: the effective size of the ES box vs the ES^box shot scale.
For primes p = 1 (mod 4), 5 <= p <= N: h_min(p) = least Type II modulus h = 4cdj - 1 with h | p + 4c^2 d
(FIXED_MODULUS_SHOTS Lemma 1.1), versus g_box(p) = least prime g = 3 (mod 4) with (p/g) = -1 (ES^box, SYNTHESIS_SPARKS2
Prop 2.2). Usage: s3_min_scale.py N"""
import sys
import numpy as np
from sympy import primerange, divisors, jacobi_symbol
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
P = np.array([p for p in primerange(5, N) if p % 4 == 1], dtype=np.int64)
hmin = np.zeros(len(P), dtype=np.int64)
left = np.arange(len(P))
h = 3
while len(left) and h < 4 * N:
    k = (h + 1) // 4
    pairs = [(c, d) for c in divisors(k) for d in divisors(k // c)]
    pl = P[left]
    hit = np.zeros(len(left), dtype=bool)
    for c, d in pairs:
        hit |= ((pl + 4 * c * c * d) % h) == 0
    hmin[left[hit]] = h
    left = left[~hit]
    h += 4
assert len(left) == 0
G3 = [g for g in primerange(3, 10**4) if g % 4 == 3]
gbox = []
for p in P:
    gbox.append(next(g for g in G3 if g != p and jacobi_symbol(int(p), g) == -1))
gbox = np.array(gbox)
for name, a in (('h_min (ES Type II)', hmin), ('g_box (ES^box)', gbox)):
    print('%-20s mean %.1f  median %d  99%% %d  max %d (at p=%d)' % (name, a.mean(), np.median(a),
          np.percentile(a, 99), a.max(), P[a.argmax()]))
lp = np.log(P.astype(float))
print('max h_min/log^2 p = %.2f ; max h_min/log^3 p = %.3f ; max g_box/log^2 p = %.2f' % (
    (hmin / lp**2).max(), (hmin / lp**3).max(), (gbox / lp**2).max()))
print('fraction with h_min <= g_box: %.3f' % (hmin <= gbox).mean())
