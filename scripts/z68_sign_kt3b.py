# z68_sign_kt3b.py — KT3 "examine" branch: is the f3~f4 correlation carried by refinements (contractible words)?
import numpy as np
from scipy.stats import spearmanr
d = np.loadtxt('data/z68/sign/kt3_contract_2e5.txt', dtype=np.int64)
p, L3, n3, L4, n4, R4, nR4, NR4, nNR4, U4, nU4 = d.T
m = (p > 10_000) & (L3 >= 10) & (R4 >= 10) & (NR4 >= 10) & (U4 >= 10)
f3 = n3[m] / L3[m]; f4 = n4[m] / L4[m]; fr = nR4[m] / R4[m]; fn = nNR4[m] / NR4[m]; fu = nU4[m] / U4[m]
pm = p[m]
def resid(f, cls):
    out = f.copy()
    for c in np.unique(cls):
        k = cls == c; out[k] = f[k] - f[k].mean()
    return out
print(f"N={m.sum()} primes p in (1e4, 2e5], p = 1 (8)")
print(f"rho(f3, f4 all)         = {spearmanr(f3, f4).statistic:+.3f}")
print(f"rho(f3, f4 refinements) = {spearmanr(f3, fr).statistic:+.3f}")
print(f"rho(f3, f4 non-refined) = {spearmanr(f3, fn).statistic:+.3f}")
cls = pm % 9240
print(f"within classes mod 9240: rho(f3,f4 all)={spearmanr(resid(f3,cls), resid(f4,cls)).statistic:+.3f}  "
      f"refined={spearmanr(resid(f3,cls), resid(fr,cls)).statistic:+.3f}  non-refined={spearmanr(resid(f3,cls), resid(fn,cls)).statistic:+.3f}")
print(f"mean fractions: f3={f3.mean():.3f} f4={f4.mean():.3f} refined={fr.mean():.3f} non-refined={fn.mean():.3f}")
i = np.where(p == 21841)[0][0]
print("21841:", d[i].tolist())
print(f"rho(f3, f4 gcd-one subset gcd(b,d)=gcd(a,c)=1 [NOT the no-move set; see kt3c]) = {spearmanr(f3, fu).statistic:+.3f}; within mod 9240: {spearmanr(resid(f3,cls), resid(fu,cls)).statistic:+.3f}; share of L4 = {U4[m].sum()/L4[m].sum():.3f}, mean {fu.mean():.3f}")
q = np.quantile(f3, 0.01); h = f3 <= q
print(f"hardest 1% by f3 (n={h.sum()}, f3<={q:.3f}): mean f4 all {f4[h].mean():.3f} (vs {f4.mean():.3f}); refined {fr[h].mean():.3f} (vs {fr.mean():.3f}); non-refined {fn[h].mean():.3f} (vs {fn.mean():.3f}); gcd-one {fu[h].mean():.3f} (vs {fu.mean():.3f})")
