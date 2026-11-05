# z58 MORDELL: does refining the level L -> L*q cover the non-square uncovered classes mod L?
# Usage: python z58_mordell_refine.py L menu q1 q2 ...   (for each q: level L*q; reports, for each non-square
# uncovered class r mod L, how many of its unit lifts (≡1 mod 4) remain uncovered at L*q.)
import sys
import numpy as np
from z58_mordell_cover import uncovered, unit_squares

L = int(sys.argv[1]); menu = sys.argv[2]; qs = [int(x) for x in sys.argv[3:]]
unc = uncovered(L, menu); sq = unit_squares(L)
base = [int(r) for r in np.nonzero(unc & ~sq)[0]]
print(f"L={L} menu={menu} nonsquare uncovered: {base}")
for q in qs:
    L2 = L * q
    u2 = uncovered(L2, menu); sq2 = unit_squares(L2)
    res = []
    for r in base:
        lifts = np.arange(r, L2, L)
        nl = int(u2[lifts].sum()); nsq = int((u2 & sq2)[lifts].sum())
        res.append(f"{r}:{nl}({nsq}sq)")
    tot_ns = int((u2 & ~sq2).sum())
    print(f"  level {L2} (x{q}): remaining lifts per class {' '.join(res)}; total nonsquare uncovered at L2 = {tot_ns}", flush=True)
