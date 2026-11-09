# z68_sign_kt3.py — KT3: do length-4/5 sign statistics predict the length-3 sign deficit?  (EVIDENCE only)
import numpy as np, sys
from scipy.stats import spearmanr
d = np.loadtxt('data/z68/sign/kt3_lengths_2e5.txt', dtype=np.int64)
p, L2, n2, L3, n3, L4, n4, L5, n5 = d.T
for lo in [10_000, 50_000]:
    m = (p > lo) & (L3 >= 10) & (L4 >= 10) & (L5 >= 10)
    f3, f4, f5 = n3[m] / L3[m], n4[m] / L4[m], n5[m] / L5[m]
    r34 = spearmanr(f3, f4); r35 = spearmanr(f3, f5); r45 = spearmanr(f4, f5)
    # also: does f4 rank the "hard" primes (bottom 1% of f3) differently?
    q = np.quantile(f3, 0.01); hard = f3 <= q
    print(f"p>{lo}: N={m.sum()}  rho(f3,f4)={r34.statistic:+.3f} (p={r34.pvalue:.2g})  rho(f3,f5)={r35.statistic:+.3f} (p={r35.pvalue:.2g})  rho(f4,f5)={r45.statistic:+.3f}")
    print(f"   mean f3={f3.mean():.3f} f4={f4.mean():.3f} f5={f5.mean():.3f};  hardest 1% by f3 (f3<={q:.3f}, n={hard.sum()}): mean f4={f4[hard].mean():.3f} vs all {f4.mean():.3f}; mean f5={f5[hard].mean():.3f}")
    # counts rather than fractions: rho(N3-, N4-) partial on sizes
    r = spearmanr(n3[m] - 0.7 * L3[m], n4[m] - f4.mean() * L4[m])
    print(f"   rho(excess N3-, excess N4-) = {r.statistic:+.3f} (p={r.pvalue:.2g})")
i = np.where(p == 21841)[0][0]
print("21841:", d[i].tolist(), "f4=%.3f f5=%.3f" % (n4[i] / L4[i], n5[i] / L5[i]))

# --- control for congruence data: residualise f3, f4, f5 on the class of p mod M (class means), then correlate
def resid(f, cls):
    out = f.copy()
    for c in np.unique(cls):
        k = cls == c; out[k] = f[k] - f[k].mean()
    return out
m = (p > 10_000) & (L3 >= 10) & (L4 >= 10) & (L5 >= 10)
f3, f4, f5 = n3[m] / L3[m], n4[m] / L4[m], n5[m] / L5[m]
pm = p[m]
for M in [24, 120, 840, 9240]:
    cls = pm % M
    r = spearmanr(resid(f3, cls), resid(f4, cls)); r5 = spearmanr(resid(f3, cls), resid(f5, cls))
    print(f"within classes mod {M} ({len(np.unique(cls))} classes): rho(f3,f4)={r.statistic:+.3f} (p={r.pvalue:.2g})  rho(f3,f5)={r5.statistic:+.3f}")
# quadratic characters of small primes as the class variable
from sympy import legendre_symbol
qs = [3, 5, 7, 11, 13, 17, 19, 23]
key = np.array([sum((1 << i) for i, q in enumerate(qs) if legendre_symbol(int(x) % q, q) == 1) for x in pm])
r = spearmanr(resid(f3, key), resid(f4, key))
print(f"within classes of (q/p), q<=23 ({len(np.unique(key))} classes): rho(f3,f4)={r.statistic:+.3f} (p={r.pvalue:.2g})")

# --- is the f3~f4 correlation a shared "chi_p on small integers" effect?  Residualise on character statistics.
from sympy import primerange
Q = list(primerange(3, 3000))
def chi(a, q): return 1 if pow(int(a) % q, (q - 1) // 2, q) == 1 else -1   # here q is the prime p, a the small integer
feats = []
for x in pm:
    x = int(x)
    v = [chi(q, x) for q in Q]          # (q/x) Legendre
    w = np.array(v, dtype=float)
    lq = np.log(Q) / np.array(Q)
    feats.append([w[:8] @ lq[:8], w[8:40] @ lq[8:40], w[40:150] @ lq[40:150], w[150:] @ lq[150:],
                  sum(chi(n, x) for n in range(1, int(x ** 0.5))) / x ** 0.25])
F = np.column_stack([np.ones(len(pm)), np.array(feats)])
def ols_resid(y):
    beta, *_ = np.linalg.lstsq(F, y, rcond=None); return y - F @ beta
r = spearmanr(ols_resid(f3), ols_resid(f4)); r5 = spearmanr(ols_resid(f3), ols_resid(f5))
print(f"after regressing out weighted sums of (q/p) over q<3000 in 4 bands + S(sqrt p)/p^(1/4): rho(f3,f4)={r.statistic:+.3f} (p={r.pvalue:.2g}) rho(f3,f5)={r5.statistic:+.3f}")
for j, name in enumerate(['q<=23', '29..173', '179..863', '877..3000', 'S(sqrtp)']):
    print(f"   corr with feature {name}: f3 {spearmanr(f3, F[:, j+1]).statistic:+.3f}  f4 {spearmanr(f4, F[:, j+1]).statistic:+.3f}  f5 {spearmanr(f5, F[:, j+1]).statistic:+.3f}")
