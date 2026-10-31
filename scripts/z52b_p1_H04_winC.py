#!/usr/bin/env python3
"""Z1473: for fixed prime p list the levels C with a (*) certificate (4uBC-u-B=p), gaps between winning C."""
import numpy as np, sys
def winners(p):
    Cs = {}
    u = 1
    while 4*u*u - 2*u <= p + 1:   # u<=B
        B = np.arange(u, (p + u)//(4*u - 1) + 2, dtype=np.int64)
        num = p + u + B; den = 4*u*B
        ok = (num % den == 0) & (num >= den)
        for b in B[ok]:
            C = (p + u + int(b))//(4*u*int(b)); Cs[C] = Cs.get(C, 0) + 1
        u += 1
    return Cs
for p in [int(x) for x in sys.argv[1:]]:
    W = sorted(winners(p))
    if not W: print(p, "no winners"); continue
    gaps = np.diff([0] + W)
    print(p, "nwin", len(W), "maxC", max(W), "Cmax_possible~", p//4, "winners", W[:40], "maxgap", gaps.max())
