"""O176 memo bsC_valence_borcherds: certificate CM points vs their Galois orbit.
Type II slice (c,d): certificates <-> divisors f | N = 1 + 4c^2 d p, f = -1 (mod 4cd) (unordered pairs {f, N/f}).
Each gives the CM point of the primitive form [f, 2, N/f] (disc -16 c^2 d p); its Galois orbit over K has size
h(-16c^2 d p) (all primitive classes of that disc).  Report max over p of (#certificate classes)/h.
Run: PYTHONPATH=scripts uv run python scripts/bsC_galois_orbit.py X
"""
import sys
from math import gcd
from sympy import primerange, divisors


def h(D):  # primitive reduced forms of disc D < 0
    cnt, a = 0, 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0) or gcd(gcd(a, b), c) != 1:
                continue
            cnt += 1
        a += 1
    return cnt


X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
worst = (0, None)
for p in primerange(5, X):
    for c, d in [(1, 1), (1, 2), (1, 3)]:
        N, M = 1 + 4 * c * c * d * p, 4 * c * d
        cert = sum(1 for f in divisors(N) if (f + 1) % M == 0 and f * f <= N)
        if cert:
            H = h(-16 * c * c * d * p)
            if cert / H > worst[0]:
                worst = (cert / H, (p, c, d, cert, H))
print('max (#certificate pairs)/h(-16c^2dp) over p <', X, ', (c,d) in {(1,1),(1,2),(1,3)}:', worst)
