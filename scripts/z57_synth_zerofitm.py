# z57 SYNTH §3.I (Assessment-level model, same binned Poisson-ML fit as scripts/z56_famdesign_zerofit.py): zero rates of the
# high-margin sub-families F_mu (data/z57/synth/trimargin_1e8.txt, columns mu = 0, 0.0533, 0.1, 0.2179) on [1e5, 1e8],
# extrapolated expected number of zeros beyond 1e10, 1e17, and the crossover x* (E(x*) = 1).  Also the observed mean
# hits/L^2 is not available from the zero file; only zero rates are fitted.
# usage: uv run --with numpy --with scipy python scripts/z57_synth_zerofitm.py data/z57/synth/trimargin_1e8.txt
import sys, math, numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
N = 10**8
s = np.ones(N + 1, dtype=bool); s[:2] = False
for q in range(2, int(N ** 0.5) + 1):
    if s[q]: s[q*q::q] = False
pr = np.nonzero(s)[0]; pr = pr[(pr % 4 == 1) & (pr >= 10**5)]
NB = 60; lo, hi = math.log(1e5), math.log(1e8)
L = np.log(pr.astype(float)); idx = np.minimum(((L - lo) / (hi - lo) * NB).astype(int), NB - 1)
cnt = np.bincount(idx, minlength=NB).astype(float); L2 = np.bincount(idx, weights=L * L, minlength=NB) / np.maximum(cnt, 1)
MU = ['0 (F4L)', '0.0533 (90%)', '0.1', '0.2179 (50%)']
z = np.zeros((4, NB))
for line in open(sys.argv[1]):
    t = line.split(); p = int(t[0])
    i = min(int((math.log(p) - lo) / (hi - lo) * NB), NB - 1)
    for j in range(4):
        if t[j + 1] == '0': z[j, i] += 1
for j in range(4):
    def nll(th):
        b, cc = th; lam = cnt * np.exp(np.minimum(b - cc * L2, 0.0))
        return float(np.sum(lam - z[j] * np.log(np.maximum(lam, 1e-300))))
    r = minimize(nll, [0.0, 0.03], method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-9, 'maxiter': 4000})
    b, cc = r.x
    Ef = lambda lx: quad(lambda u: math.exp(u + b - cc * u * u) / (2 * u), lx, 6000, limit=500)[0]
    a_, b_ = math.log(1e5), 6000.0
    for _ in range(200):
        m = (a_ + b_) / 2
        if Ef(m) >= 1: a_ = m
        else: b_ = m
    print(f'mu={MU[j]:13s} zeros[1e5,1e8]={int(z[j].sum()):6d} b={b:7.3f} c_eff={cc:.5f} E(>1e10)={Ef(10*math.log(10)):.3g} '
          f'E(>1e17)={Ef(17*math.log(10)):.3g} log10 x*={a_/math.log(10):.1f}')
