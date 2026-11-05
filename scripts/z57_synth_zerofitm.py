# z57 SYNTH §3.I (Assessment-level model; binned Poisson-ML fit as scripts/z56_famdesign_zerofit.py): zero rates of the
# uniform-margin sub-families F_mu (data/z57/synth/trimargin_1e8.txt, columns mu = 0, 0.0533, 0.1, 0.12, 0.2179) on
# [1e5, 1e8], fitted as P(zero) = exp(b - c L^2), and the expected number of zeros beyond x,
#   E(x) = int_{log x}^inf exp(s + b - c s^2) * rho(s) ds,  rho = 1/(2s) (all primes p = 1 (4)) or 1/(32 s) (Mordell classes,
# 6 of the 192 unit classes mod 840).  The tail is integrated in the stabilised form (second review, finding 1):
#   E = exp(s + b - c s^2) rho(s) * int_0^inf exp(-(2cs - 1) t - c t^2) * s/(s + t) dt  (valid when 2cs > 1),
# with relative tolerance.  Two domains: ALL primes p = 1 (4), and the Mordell classes {1,121,169,289,361,529} mod 840.
# usage: uv run --with numpy --with scipy python scripts/z57_synth_zerofitm.py data/z57/synth/trimargin_1e8.txt
import sys, math, numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
N = 10**8
s = np.ones(N + 1, dtype=bool); s[:2] = False
for q in range(2, int(N ** 0.5) + 1):
    if s[q]: s[q*q::q] = False
pr_all = np.nonzero(s)[0]; pr_all = pr_all[(pr_all % 4 == 1) & (pr_all >= 10**5)]
MORD = {1, 121, 169, 289, 361, 529}
NB = 60; lo, hi = math.log(1e5), math.log(1e8)
rows = [line.split() for line in open(sys.argv[1])]
ncol = len(rows[0]) - 1
MU = ['0 (F4L)', '0.0533 (90%)', '0.1', '0.12', '0.2179 (50%)'][:ncol] if ncol == 5 else [str(j) for j in range(ncol)]
def tail(b, c, lx, dens):
    if 2 * c * lx <= 1:  # integrand still increasing at lx: integrate directly with relative tolerance
        return quad(lambda u: math.exp(u + b - c * u * u) * dens(u), lx, lx + 400, epsabs=0, epsrel=1e-10, limit=1000, points=[1 / (2 * c)])[0]
    a = 2 * c * lx - 1
    inner = quad(lambda t: math.exp(-a * t - c * t * t) * lx / (lx + t), 0, math.inf, epsabs=0, epsrel=1e-11, limit=500)[0]
    return math.exp(lx + b - c * lx * lx) * dens(lx) * inner
for dom in ('all p=1(4)', 'Mordell'):
    pr = pr_all if dom.startswith('all') else pr_all[np.isin(pr_all % 840, list(MORD))]
    dens = (lambda u: 1 / (2 * u)) if dom.startswith('all') else (lambda u: 1 / (32 * u))
    L = np.log(pr.astype(float)); idx = np.minimum(((L - lo) / (hi - lo) * NB).astype(int), NB - 1)
    cnt = np.bincount(idx, minlength=NB).astype(float); L2 = np.bincount(idx, weights=L * L, minlength=NB) / np.maximum(cnt, 1)
    z = np.zeros((ncol, NB))
    for t in rows:
        p = int(t[0])
        if not dom.startswith('all') and p % 840 not in MORD: continue
        i = min(int((math.log(p) - lo) / (hi - lo) * NB), NB - 1)
        for j in range(ncol):
            if t[j + 1] == '0': z[j, i] += 1
    print(f'# domain: {dom}; primes in [1e5,1e8]: {len(pr)}')
    for j in range(ncol):
        if z[j].sum() < 5: print(f'mu={MU[j]:13s} zeros={int(z[j].sum())} (too few to fit)'); continue
        def nll(th):
            b, cc = th; lam = cnt * np.exp(np.minimum(b - cc * L2, 0.0))
            return float(np.sum(lam - z[j] * np.log(np.maximum(lam, 1e-300))))
        r = minimize(nll, [0.0, 0.03], method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-9, 'maxiter': 4000})
        b, cc = r.x
        a_, b_ = math.log(1e5), 6000.0
        for _ in range(200):
            m = (a_ + b_) / 2
            if tail(b, cc, m, dens) >= 1: a_ = m
            else: b_ = m
        print(f'mu={MU[j]:13s} zeros[1e5,1e8]={int(z[j].sum()):6d} b={b:7.3f} c_eff={cc:.5f} '
              f'E(>1e10)={tail(b, cc, 10*math.log(10), dens):.3g} E(>1e17)={tail(b, cc, 17*math.log(10), dens):.3g} log10 x*={a_/math.log(10):.2f}')
