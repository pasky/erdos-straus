"""zt_rate_lop.py (O227): FF_STERILE_PUSH fs_rate continuum exponent (route bounds of Lemma 1.6, grid; steering/EVIDENCE only)
restricted to the patterns that can cover x*_c (FF_THIRDS_CORNER Cor 1.3 + Cor 3.2), in normalised coordinates
(a <= b = y + t, a + z + y + t = 1): b >= 1/2 and max(z + 2a, t) >= 1/2.  usage: zt_rate_lop.py r[,r..] [G]"""
import sys
import numpy as np
from math import log
import fs_rate as F

def opt(lq, G, restrict):
    best = (-9, None); g = np.linspace(0, 1, G + 1)
    for a in g:
        for z in g:
            if a + z > 1: continue
            for y in g:
                t = 1 - a - z - y
                if t < -1e-12 or a > y + t + 1e-12: continue
                if restrict and not (y + t >= 0.5 - 1e-12 and max(z + 2 * a, t) >= 0.5 - 1e-12): continue
                v = min(F.routes(a, z, y, t, lq).values())
                if v > best[0]: best = (v, (a, z, y, t))
    return best
G = int(sys.argv[2]) if len(sys.argv) > 2 else 60
for r in [int(x) for x in sys.argv[1].split(',')]:
    lq = r * log(3)
    for restrict in (False, True):
        v, p = opt(lq, G, restrict)
        print(f"r={r} {'lopsided+Liouville2' if restrict else 'all patterns      '}: max_p min_route - 1/2 = {v-0.5:+.4f} at (a,z,y,t) = {[round(float(x),3) for x in p]}", flush=True)
