"""R274 from-scratch refit of DISPROOF_AVENUES §4.2-4.3 (zero law, NB falsification, crossover, floor test)
on counts produced by scripts/review_r274_ladder.c (all primes <= 1e8, m = 4..24), stored as /tmp/r274/f{m}.npy.
Units (as defined in §4.2): (m, p mod lcm(840,4m), dyadic bin [2^k, 2^{k+1})), >= 10 primes; mu = unit mean."""
import math, sys
import numpy as np
from scipy.optimize import minimize

P = np.load('/tmp/r274/primes_1e8.npy').astype(np.int64)
MS = [m for m in range(4, 25)]

def units(m, kmin=10, kmax=26):
    f = np.load(f'/tmp/r274/f{m}.npy').astype(np.int64)
    ok = (P > 3) & (m % P != 0); p, f = P[ok], f[ok]
    C = math.lcm(840, 4*m); cell = p % C; kk = np.floor(np.log2(p)).astype(int)
    out = []
    for k in range(kmin, kmax + 1):
        s = kk == k
        if not s.any(): continue
        cc, ff = cell[s], f[s]
        o = np.argsort(cc, kind='stable'); cc, ff = cc[o], ff[o]
        b = np.flatnonzero(np.diff(cc)) + 1; st = np.r_[0, b]; en = np.r_[b, len(cc)]
        for a, e in zip(st, en):
            if e - a < 10: continue
            g = ff[a:e]; out.append((m, k, g.mean(), g.var(), e - a, int((g == 0).sum())))
    return out, p, f

def nll(th, mu, n, z):
    a, b = th
    if a <= 0 or b <= 0: return 1e18
    lp0 = -a*mu**b; p0 = np.exp(lp0)
    return -(z*lp0 + (n - z)*np.log1p(-np.minimum(p0, 1 - 1e-15))).sum()

def fit(R):
    r = minimize(nll, [0.5, 0.9], args=(R[:, 2], R[:, 4], R[:, 5]), method='Nelder-Mead',
                 options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 4000})
    return r.x

if __name__ == '__main__' and len(sys.argv) == 1:
    rows = []; data = {}
    for m in MS:
        u, p, f = units(m); rows += u; data[m] = (p, f)
        z = p[f == 0]
        print(f'm={m}: #exc={len(z)} last={int(z.max()) if len(z) else 0} beyond1e6={(z > 10**6).sum()}')
    R = np.array(rows, dtype=float)
    a, b = fit(R); print(f'\nALL units: a={a:.3f} beta={b:.3f}  (#units {len(R)})')
    # calibration by mu-bin
    edges = [0, 4, 6, 8, 10, 12, 15, 20, 25, 30, 35, 40, 50, 70, 1e9]
    print('mu-bin  primes  zeros  expected(fit)  obs/exp')
    for lo, hi in zip(edges[:-1], edges[1:]):
        s = (R[:, 2] >= lo) & (R[:, 2] < hi)
        if not s.any(): continue
        n = R[s, 4].sum(); z = R[s, 5].sum(); ex = (R[s, 4]*np.exp(-a*R[s, 2]**b)).sum()
        print(f'[{lo:g},{hi:g}) {int(n)} {int(z)} {ex:.3g} {z/ex if ex > 0 else float("nan"):.2f}')
    for kt in (18, 20, 22):
        tr = R[R[:, 1] < kt]; te = R[R[:, 1] >= kt]
        at, bt = fit(tr); print(f'\ntrain p<2^{kt}: a={at:.3f} beta={bt:.3f}; test p>=2^{kt}: m: predicted / observed')
        for m in MS:
            s = te[:, 0] == m; pr = (te[s, 4]*np.exp(-at*te[s, 2]**bt)).sum(); ob = te[s, 5].sum()
            if pr > 0.05 or ob: print(f'   m={m}: {pr:.2f} / {int(ob)}  ratio obs/pred = {ob/pr if pr else float("inf"):.2f}')
        # pooled by mu bins on test
        for lo, hi in [(0, 15), (15, 25), (25, 35), (35, 1e9)]:
            s = (te[:, 2] >= lo) & (te[:, 2] < hi); pr = (te[s, 4]*np.exp(-at*te[s, 2]**bt)).sum(); ob = te[s, 5].sum()
            print(f'   test mu in [{lo},{hi}): predicted {pr:.3g} observed {int(ob)}')
    # NB check, m = 6, 8 in [2^24, 2^26)
    for m in (6, 8):
        s = (R[:, 0] == m) & (R[:, 1] >= 24) & (R[:, 1] < 26)
        mu, var, n = R[s, 2], R[s, 3], R[s, 4]
        r = mu**2/np.maximum(var - mu, 1e-9); pnb = (1 + mu/r)**(-r)
        print(f'\nNB moment-fitted m={m} [2^24,2^26): predicted zeros {np.sum(n*pnb):.2f}, observed {int(R[s,5].sum())}, '
              f'stretched-exp predicted {np.sum(n*np.exp(-a*mu**b)):.3g}')
    # crossover law
    print('\ncrossover: q_m = 1e-3 quantile of f/L^3 over primes in [2^26, 1e8]; c0 = q_m (ln p_last)^3')
    c0s = []
    for m in MS:
        p, f = data[m]; s = p >= 2**26; L = np.log(p[s].astype(float))
        q = np.quantile(f[s]/L**3, 1e-3); z = p[f == 0]; last = int(z.max()) if len(z) else 0
        c0 = q*math.log(last)**3 if last else float('nan')
        if last and last < 5e7: c0s.append(c0)
        print(f'm={m}: q={q:.5f} median={np.median(f[s]/L**3):.4f} last={last} c0={c0:.2f}')
    g = math.exp(np.mean(np.log(c0s))); print(f'geo-mean c0 (last<5e7) = {g:.2f}, range {min(c0s):.2f}..{max(c0s):.2f}')
    # floor test m = 4
    p, f = data[4]
    print('\nm=4 floor test: k, n, min f/L^3, q1e-3, q1e-4, median')
    for k in range(14, 27):
        s = (p >= 2**k) & (p < 2**(k+1)); r_ = f[s]/np.log(p[s].astype(float))**3
        print(k, s.sum(), f'{r_.min():.4f} {np.quantile(r_,1e-3):.4f} {np.quantile(r_,1e-4):.4f} {np.median(r_):.4f}')
    # hardest m=4 cell (mod 840) mu/L^3 per bin
    s = R[:, 0] == 4
    for k in range(18, 27):
        t = s & (R[:, 1] == k); i = np.argmin(R[t, 2]); Lk = (k + 0.5)*math.log(2)
        print(f'm=4 k={k}: min cell mu={R[t,2][i]:.1f}  mu/L^3~{R[t,2][i]/Lk**3:.4f}')

def local_fits():
    """beta drift: refit on units with mu >= threshold; Poisson tail test of the mu >= 35 excess."""
    from scipy.stats import poisson
    rows = []
    for m in MS: rows += units(m)[0]
    R = np.array(rows, dtype=float)
    for lo in (0, 8, 12, 15, 20):
        s = R[:, 2] >= lo; a, b = fit(R[s]); z = int(R[s, 5].sum())
        mu0 = 229.0
        print(f'units mu>={lo}: zeros={z} a={a:.3f} beta={b:.3f}  -lnP at mu=229 (m=4 at 1e8): {a*mu0**b:.1f}')
    a, b = fit(R)
    for lo in (30, 35):
        s = R[:, 2] >= lo; ex = (R[s, 4]*np.exp(-a*R[s, 2]**b)).sum(); ob = int(R[s, 5].sum())
        print(f'global fit, mu>={lo}: expected {ex:.2f} observed {ob}  P(X>=obs)={poisson.sf(ob-1, ex):.2e}')
    for kt in (18, 20, 22):
        tr = R[R[:, 1] < kt]; te = R[(R[:, 1] >= kt) & (R[:, 2] >= 35)]
        at, bt = fit(tr); ex = (te[:, 4]*np.exp(-at*te[:, 2]**bt)).sum(); ob = int(te[:, 5].sum())
        print(f'train<2^{kt}, test mu>=35: expected {ex:.2f} observed {ob}  P(X>=obs)={poisson.sf(ob-1, ex):.2e}')

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'local':
    local_fits()
