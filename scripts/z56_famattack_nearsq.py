# Window profile at near-square primes p = m^2 + k vs generic primes of the same size (matched by p mod 840 class).
# Ratio per window = mean count at near-squares / mean count at generic primes in the same mod-840 classes.
import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load
ks = dict(tuple(map(int, l.split())) for l in open(sys.argv[1]))
pn, Rn, gn = load(sys.argv[2]); pg, Rg, gg = load(sys.argv[3])
Wn, Wg = gn.sum(2).astype(float), gg.sum(2).astype(float)
Vn, Vg = gn.sum(1).astype(float), gg.sum(1).astype(float)
# per-class generic means (mod 840), then expected for each near-square prime
cls_g = pg % 840
def expected(Xg, pn):
    out = np.zeros((len(pn), Xg.shape[1]))
    for i, p in enumerate(pn):
        m = cls_g == p % 840
        out[i] = Xg[m].mean(0) if m.sum() >= 20 else Xg.mean(0)
    return out
EW, EV = expected(Wg, pn), expected(Vg, pn)
ER = expected((Rg / 2)[:, None].astype(float), pn)[:, 0]
kk = np.array([ks[p] for p in pn])
print("k   n   total-ratio  u-window ratios (0..4)            C-window ratios (0..4)      zeros")
for k in sorted(set(kk)) + [None]:
    m = (kk == k) if k is not None else np.ones(len(pn), bool)
    rt = (Rn[m] / 2).sum() / ER[m].sum()
    ru = Wn[m].sum(0) / EW[m].sum(0); rv = Vn[m].sum(0) / EV[m].sum(0)
    print(f"{str(k) if k is not None else 'all':4}{m.sum():4}  {rt:.3f}   " + " ".join(f"{x:.2f}" for x in ru) + "   " + " ".join(f"{x:.2f}" for x in rv) + f"   {(Rn[m]==0).sum()}")
