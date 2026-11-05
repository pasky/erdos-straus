# z59 MSPLUS: evaluate structured-search outputs (scripts/z59_msplus_struct.sh) against the zero law (model B of
# z59_msplus_zerofit.py): per family, distinct non-square inputs, UNK count, mean m(n), and the model's expected number
# of zeros sum_n P0(n).  Usage: python z59_msplus_structeval.py COEF THETA_B(comma-sep) FILES...
import sys, math
import numpy as np
sys.path.insert(0, 'scripts')
from z59_msplus_zerofit import mval, kbucket, design
coef = {}
for line in open(sys.argv[1]):
    a, l, c1, c0 = line.split(); coef[int(a)] = (float(l), float(c1), float(c0))
th = np.array([float(x) for x in sys.argv[2].split(',')])
for fn in sys.argv[3:]:
    seen = set(); unk = 0; sq = 0; P0 = 0.0; ms = []; mus = []
    for line in open(fn):
        t = line.split(); n = int(t[0])
        if n in seen: continue
        seen.add(n)
        r = math.isqrt(n)
        if r * r == n:
            sq += 1; continue
        if t[1] == 'UNK': unk += 1
        else: mus.append(int(t[1]))
        kb = kbucket(n)
        if kb == 0: continue
        m = mval(n, coef); ms.append(m)
        x = design(np.array([m]), np.array([math.log10(n)]), np.array([kb]), True)[0]
        P0 += math.exp(x @ th)
    ms.sort(); mus.sort()
    print(f"{fn}: distinct={len(seen)} squares(T1 controls)={sq} nonsq_UNK={unk} m: min={ms[0]:.1f} median={ms[len(ms)//2]:.1f} "
          f"| mu median={mus[len(mus)//2]} max={mus[-1]} | model-B expected zeros={P0:.3g}")
