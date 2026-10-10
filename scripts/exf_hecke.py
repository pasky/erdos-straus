"""O131 Approach A: does a count F(n) satisfy a Hecke-type relation at a prime l?
Least squares of F(n l^2) on {F(n), F(n/l^2), (n/l)F(n), (-n/l)F(n), F(n l), F(n/l), 1}; exact relation => residual 0."""
import numpy as np, sys
A = np.load('data/exf/arrays_2e4.npz')
N = len(A['T1p']) - 1
def leg(n, l):
    n = int(n)
    return 0 if n % l == 0 else (1 if pow(n % l, (l-1)//2, l) == 1 else -1)
def test(F, l, name):
    ns = np.arange(1, N // (l*l) + 1)
    def g(m): return np.array([F[x] if x == int(x) and 1 <= x <= N else 0 for x in m])
    cols = {'F(n)': F[ns], 'F(n/l2)': np.array([F[n//(l*l)] if n % (l*l) == 0 else 0 for n in ns]),
            '(n/l)F': np.array([leg(n, l) for n in ns]) * F[ns], '(-n/l)F': np.array([leg(-n, l) for n in ns]) * F[ns],
            'F(nl)': F[ns*l], 'F(n/l)': np.array([F[n//l] if n % l == 0 else 0 for n in ns]), '1': np.ones(len(ns))}
    X = np.stack(list(cols.values()), 1).astype(float); y = F[ns*l*l].astype(float)
    coef, res, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ coef
    print(f'{name:10s} l={l}: rel.resid {np.linalg.norm(r)/np.linalg.norm(y):.3f}  max|r| {np.abs(r).max():.1f}  coef', dict(zip(cols, np.round(coef, 3))))
for k in sys.argv[1:] or ['T1p', 'T1m', 'T2p', 'T2m']:
    F = A[k] if '_' not in k else A[k.split(':')[0]][int(k.split(':')[1])] if ':' in k else A[k]
    for l in (3, 5, 7):
        test(F.astype(np.int64), l, k)
