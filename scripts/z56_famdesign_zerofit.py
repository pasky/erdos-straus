# Assessment-level model: fit P(hits_F(p) = 0) = exp(b - c L^2), L = log p, by binned Poisson ML on all primes p = 1 (4)
# in [1e5, 1e8] (exhaustive raw scans, regenerable with z56scan 5 1e7 and z56scan 1e7 1e8), then the model's expected
# number of zeros beyond x, E(x) = int_{log x}^inf e^{s+b-c s^2}/(2s) ds, and the crossover x* with E(x*) = 1.
# usage: uv run --with numpy --with scipy python scripts/z56_famdesign_zerofit.py rawfile1 rawfile2 ...
import sys, math, numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
COLS = ['all', 'F0', 'F1', 'F2U', 'F2S', 'F3U', 'F3S', 'F4', 'F4L', 'K', 'H3', 'HC']
NB = 60; lo, hi = math.log(1e5), math.log(1e8)
cnt = np.zeros(NB); z = np.zeros((len(COLS), NB)); sL2 = np.zeros(NB)
for f in sys.argv[1:]:
    for line in open(f):
        t = line.split()
        p = int(t[0]);
        if p < 1e5: continue
        L = math.log(p); i = min(int((L - lo) / (hi - lo) * NB), NB - 1)
        cnt[i] += 1; sL2[i] += L * L
        for j in range(len(COLS)):
            if t[j + 1] == '0': z[j, i] += 1
L2 = sL2 / np.maximum(cnt, 1)
print('family  zeros[1e5,1e8]  b       c_eff    E(>1e8)     log10 x*   (E(x*)=1)')
for j, c in enumerate(COLS):
    if z[j].sum() < 5: print(f'{c:5s} {int(z[j].sum()):8d}  (too few zeros to fit)'); continue
    def nll(th):
        b, cc = th; lam = cnt * np.exp(np.minimum(b - cc * L2, 0.0))
        return float(np.sum(lam - z[j] * np.log(np.maximum(lam, 1e-300))))
    r = minimize(nll, [0.0, 0.03], method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-8, 'maxiter': 4000})
    b, cc = r.x
    E = lambda x: quad(lambda s: math.exp(s + b - cc * s * s) / (2 * s), math.log(x), 2000, limit=400)[0]
    # crossover: largest x with E(x) >= 1
    lx = math.log(1e8)
    if E(1e8) < 1: xs = '<8 (E(1e8)<1)'
    else:
        a_, b_ = math.log(1e8), 2000.0
        for _ in range(200):
            m = (a_ + b_) / 2
            if quad(lambda s: math.exp(s + b - cc * s * s) / (2 * s), m, 2000, limit=400)[0] >= 1: a_ = m
            else: b_ = m
        xs = '%.1f' % (a_ / math.log(10))
    print(f'{c:5s} {int(z[j].sum()):8d}  {b:7.3f} {cc:8.5f}  {E(1e8):10.3g}  {xs}')
