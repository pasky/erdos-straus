"""R247: re-optimise min_route - 1/2 (FF_STERILE_PUSH Lemma 1.6 routes, as implemented in fs_rate.routes) over the
patterns allowed at x*_c, with a finer grid + random local refinement, and list near-maximisers.
Allowed (normalised, a <= b = y + t): b >= 1/2 and max(z + 2a, t) >= 1/2.  usage: review_r247_rate.py r G"""
import sys, random
from math import log
sys.path.insert(0, 'scripts')
import fs_rate as F
r, G = int(sys.argv[1]), int(sys.argv[2]); lq = r * log(3)
def allowed(a, z, y, t, eps=1e-12):
    return min(a, z, y, t) >= -eps and a <= y + t + eps and y + t >= 0.5 - eps and max(z + 2 * a, t) >= 0.5 - eps
def val(a, z, y): t = 1 - a - z - y; return min(F.routes(a, z, y, t, lq).values()) - 0.5
pts = []
for i in range(G + 1):
    for j in range(G + 1 - i):
        for k in range(G + 1 - i - j):
            a, z, y = i / G, j / G, k / G; t = 1 - a - z - y
            if allowed(a, z, y, t): pts.append((val(a, z, y), a, z, y))
pts.sort(reverse=True)
print(f"r={r} G={G} allowed grid points {len(pts)}; best {pts[0][0]:+.5f} at a,z,y={pts[0][1:]}")
near = [p for p in pts if p[0] > -0.01]
print('grid points within 0.01 of 0:', len(near), 'sample', [tuple(round(x, 3) for x in p) for p in near[:8]])
random.seed(1); best = pts[0]
for start in pts[:30]:
    cur = start
    for it in range(3000):
        st = 0.02 * (0.999 ** it)
        a, z, y = (cur[1] + random.gauss(0, st), cur[2] + random.gauss(0, st), cur[3] + random.gauss(0, st))
        t = 1 - a - z - y
        if not allowed(a, z, y, t, 0): continue
        v = val(a, z, y)
        if v > cur[0]: cur = (v, a, z, y)
    if cur[0] > best[0]: best = cur
print(f"refined best {best[0]:+.6f} at a,z,y,t = {[round(x, 4) for x in best[1:]] + [round(1 - sum(best[1:]), 4)]}")
