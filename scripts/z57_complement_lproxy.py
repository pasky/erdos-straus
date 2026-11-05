# z57 COMPLEMENT: global (non-local) drivers. Truncated Euler-product proxies for L(1, chi_p) and L(1, chi_{-4p}),
# and the loading of every family on them after the local-data OLS (residues of p mod small prime powers).
# usage: python z57_complement_lproxy.py LABEL files...
import sys, math, functools
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z57_complement_stats import load, onehot_design, ols_resid, corr, partial, strata_resid
print = functools.partial(print, flush=True)

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, math.isqrt(n) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]

def lproxies(p, LIM=20000):
    P = primes_upto(LIM)
    Lp = np.zeros(len(p)); L4 = np.zeros(len(p))
    p8 = p % 8
    chi2 = np.where((p8 == 1) | (p8 == 7), 1.0, -1.0)            # (2/p)
    Lp += -np.log(1 - chi2 / 2.0)
    for l in P[1:]:
        l = int(l); qr = np.zeros(l, bool); qr[(np.arange(1, l) ** 2) % l] = True
        r = p % l
        leg = np.where(r == 0, 0.0, np.where(qr[r], 1.0, -1.0))   # (p/l) = (l/p) for p ≡ 1 (4)
        Lp += -np.log(1 - leg / l)
        sgn = 1.0 if l % 4 == 1 else -1.0                          # (-1/l)
        L4 += -np.log(1 - sgn * leg / l)                           # chi_{-4p}(l) = (-p/l)
    return Lp, L4

def main():
    label = sys.argv[1]; p, D = load(sys.argv[2:])
    N = len(p); sq = math.sqrt(N); L2 = np.log(p.astype(float)) ** 2
    Lp, L4 = lproxies(p)
    print(f'# {label}: N = {N}; proxies log L(1,chi_p) mean {Lp.mean():+.3f} sd {Lp.std():.3f}; log L(1,chi_-4p) mean {L4.mean():+.3f} sd {L4.std():.3f}; corr {corr(Lp, L4):+.3f}')
    mods = [8, 3, 9, 5, 25, 7, 49, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    X0 = onehot_design(p, mods)
    D['INT'] = D['W'] - D['BND']
    fams = ['STAR', 'B1', 'I1', 'QR', 'c2', 'c3', 'G', 'K', 'INT']
    # residualise proxies on local data (they are partly functions of p mod small primes)
    rLp = ols_resid(Lp, X0); rL4 = ols_resid(L4, X0)
    print('## loading on the proxies after local OLS: corr(resid family/L^2, resid proxy) (nominal z)')
    R = {}
    for c in fams:
        y = ols_resid(D[c] / L2, X0); R[c] = y
        a, b = corr(y, rLp), corr(y, rL4)
        print(f'{c:5s}  log L(1,chi_p): {a:+.3f} ({a * sq:+.1f})   log L(1,chi_-4p): {b:+.3f} ({b * sq:+.1f})')
    X1 = np.column_stack([X0, Lp, L4, Lp * Lp, L4 * L4, Lp * L4])
    print('## pair correlations of residuals: local OLS | local + L-proxies (quadratic) | local + L-proxies + INT')
    X2 = np.column_stack([X1, D['INT']])
    pairs = [('STAR', 'B1'), ('STAR', 'I1'), ('B1', 'I1'), ('STAR', 'c2'), ('STAR', 'c3'), ('c2', 'c3'), ('G', 'K'),
             ('STAR', 'QR'), ('B1', 'QR'), ('I1', 'QR')]
    R1 = {c: ols_resid(D[c], X1) for c in fams}; R2 = {c: ols_resid(D[c], X2) for c in fams}; R0 = {c: ols_resid(D[c], X0) for c in fams}
    for a, b in pairs:
        r0, r1, r2 = corr(R0[a], R0[b]), corr(R1[a], R1[b]), corr(R2[a], R2[b])
        print(f'{a:4s}-{b:4s} {r0:+.3f} | {r1:+.3f} ({r1 * sq:+.1f}) | {r2:+.3f} ({r2 * sq:+.1f})')
    # Jacobi share: certificate words / interior words, against proxies
    cert = D['INT'] - D['QR']
    share = np.where(D['INT'] > 0, cert / np.maximum(D['INT'], 1), np.nan)
    m = ~np.isnan(share); y = ols_resid(share[m], X0[m])
    print(f'## QNR share of interior words: mean {np.nanmean(share):.4f}; corr with resid log L(1,chi_p) {corr(y, rLp[m]):+.3f}, log L(1,chi_-4p) {corr(y, rL4[m]):+.3f}')

if __name__ == '__main__':
    main()
