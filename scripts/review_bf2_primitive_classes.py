"""R163: fraction of square classes mod M that contain a PRIMITIVE square point (Q(u,v)=w^2,
gcd(u,v)=1), found via the conic parametrisation from a base point with |Y| <= K.
Independent check of the §8.5 / Lemma 8.4-check claim '50-75% contain none'.
For each class reached by a primitive point that's a lower bound on 'reached'; unreached classes
are confirmed by a local mod-M argument only heuristically (large K)."""
import math
from math import gcd

def run(A, B, C, M, K=150):
    Q = lambda x, y: A*x*x + B*x*y + C*y*y
    units = [s for s in range(M) if gcd(s, M) == 1]
    sq = {s*s % M for s in units}
    classes = {(x, y) for x in range(M) for y in range(M) if Q(x, y) % M in sq}
    base = next((x, y, math.isqrt(Q(x, y))) for r in range(1, 50) for x in range(-r, r+1)
                for y in range(-r, r+1) if gcd(x, y) == 1 and math.isqrt(Q(x, y))**2 == Q(x, y))
    hit = set()
    for y0 in range(-K, K+1):
        for y1 in range(-K, K+1):
            if (y0, y1) == (0, 0): continue
            qY = Q(y0, y1); bY = Q(base[0]+y0, base[1]+y1) - Q(*base[:2]) - qY
            t = (qY*base[0] - bY*y0, qY*base[1] - bY*y1, base[2]*qY)
            g = gcd(gcd(t[0], t[1]), t[2]); t = (t[0]//g, t[1]//g)
            for s in (1, -1):
                hit.add((s*t[0] % M, s*t[1] % M))
    return len(classes), len(classes & hit)

for (A, B, C, M) in [(1,0,1,8), (1,0,1,24), (1,0,1,40), (1,1,1,24), (1,0,2,16), (1,0,5,40), (2,1,3,184)]:
    n, h = run(A, B, C, M)
    print((A, B, C), M, 'square classes', n, 'with primitive square point', h, 'frac without %.3f' % (1 - h/n))
