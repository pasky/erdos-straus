"""O262: extrapolate the universal zero law to m = 4 (ES, Type II only => conservative for ES).
mu_cell(p) for m = 4: cell means (p mod 840) per dyadic bin from the ladder; the hardest cell's mu/L^3 is
extrapolated as constant (and, pessimistically, as mu ~ L^2 from 2^26).  Expected #primes with f_II = 0 in [X, inf)
= sum over dyadic bins of sum_cells n_cell(bin) * exp(-a mu^beta), n_cell from PNT/phi(840).
Also: the break-even beta* making the expected count beyond 10^18 equal to 1."""
import math, numpy as np
R = np.load('/tmp/z32/units.npy'); s = R[:, 0] == 4
for k in range(18, 27):
    t = s & (R[:, 1] == k); L = (k + 0.5)*math.log(2)
    print(f'k={k}: min cell mu={R[t,2].min():.1f} (mu/L^3={R[t,2].min()/L**3:.4f}), mean={np.average(R[t,2],weights=R[t,3]):.1f}')
t = s & (R[:, 1] == 26); L26 = 26.5*math.log(2)
cmu = np.sort(R[t, 2]/L26**3)                 # per-cell mu/L^3 at the top bin (192 cells)
def expected(X, a, beta, mode='L3', Xmax=1e300):
    tot = 0.0; x = X
    while x < Xmax:
        L = math.log(x*1.5); nprim = x/L     # primes in [x, 2x)
        mus = cmu*L**3 if mode == 'L3' else cmu*L26**3*(L/L26)**2
        lp = -a*mus**beta
        if lp.max() < -745 and x > 1e30: break
        tot += nprim/len(cmu)*np.exp(lp).sum(); x *= 2
    return tot
for a, b, tag in ((0.535, 0.91, 'fit'), (0.535*0.7, 0.91, 'a-30%'), (0.4, 0.80, 'flatter')):
    for mode in ('L3', 'L2'):
        print(f'{tag} a={a:.3f} beta={b} mu~{mode}: E#[1e8,1e18)={expected(1e8,a,b,mode,1e18):.3g}  E#[1e18,inf)={expected(1e18,a,b,mode):.3g}')
for mode in ('L3', 'L2'):
    lo, hi = 0.05, 0.91
    for _ in range(40):
        mid = (lo + hi)/2
        if expected(1e18, 0.535, mid, mode) > 1: lo = mid
        else: hi = mid
    print(f'break-even beta* (a=0.535, mu~{mode}) for E#[1e18,inf)=1: {hi:.3f}')
