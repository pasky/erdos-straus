# z57 SYNTH (Assessment-level model, same method as scripts/z56_famdesign_zerofit.py): fit P(R8(p) = 0) = exp(b - c L^2)
# by binned Poisson ML over all primes p = 1 (4) in [1e5, 1e8] (zeros from data/z57/synth/tri_1e8.txt, prime counts by
# a numpy sieve), then E(x) = int_{log x}^inf e^{s+b-c s^2}/(2s) ds (expected # zeros beyond x, using pi'(e^s) ~ e^s/(2s)
# for p = 1 (4)) and the crossover x* with E(x*) = 1.  Also reports the same fit for R (full (★)) for comparison.
# usage: uv run --with numpy --with scipy python scripts/z57_synth_zerofit8.py data/z57/synth/tri_1e8.txt
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
zs = {'R8': np.zeros(NB), 'R': np.zeros(NB)}
for line in open(sys.argv[1]):
    t = line.split(); p = int(t[0])
    if p < 1e5: continue
    i = min(int((math.log(p) - lo) / (hi - lo) * NB), NB - 1)
    if t[2] == '0': zs['R8'][i] += 1
    if t[1] == '0': zs['R'][i] += 1
for name, z in zs.items():
    if z.sum() < 5: print(name, int(z.sum()), 'too few zeros'); continue
    def nll(th):
        b, cc = th; lam = cnt * np.exp(np.minimum(b - cc * L2, 0.0))
        return float(np.sum(lam - z * np.log(np.maximum(lam, 1e-300))))
    r = minimize(nll, [0.0, 0.03], method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-9, 'maxiter': 4000})
    b, cc = r.x
    # stabilised tail (second review, finding 1): E = e^{s+b-cs^2}/(2s) * int_0^inf e^{-(2cs-1)t - ct^2} s/(s+t) dt, 2cs > 1
    def Ef(lx):
        if 2 * cc * lx <= 1:  # integrand still increasing at lx: integrate directly with relative tolerance
            return quad(lambda u: math.exp(u + b - cc * u * u) / (2 * u), lx, lx + 400, epsabs=0, epsrel=1e-10, limit=1000, points=[1 / (2 * cc)])[0]
        a = 2 * cc * lx - 1
        return math.exp(lx + b - cc * lx * lx) / (2 * lx) * quad(lambda t: math.exp(-a * t - cc * t * t) * lx / (lx + t), 0, math.inf, epsabs=0, epsrel=1e-11, limit=500)[0]
    out = [f'{name}: zeros[1e5,1e8]={int(z.sum())} b={b:.3f} c_eff={cc:.5f}']
    for k in (8, 10, 12, 14, 17):
        out.append(f'E(>1e{k})={Ef(k * math.log(10)):.3g}')
    a_, b_ = math.log(1e5), 4000.0
    for _ in range(200):
        m = (a_ + b_) / 2
        if Ef(m) >= 1: a_ = m
        else: b_ = m
    out.append(f'log10 x*={a_ / math.log(10):.1f}')
    print('  '.join(out))
