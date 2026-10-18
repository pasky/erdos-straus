"""O264: scores of primes with 13-smooth p-1 versus their size neighbours (p = 1 (4) <= X).
For each such p: raw scores and size-normalised percentiles u among primes in [p/2, 2p]."""
import sys
import numpy as np
A = np.loadtxt(sys.argv[1], dtype=np.int64); X = int(sys.argv[2])
A = A[A[:, 0] <= X]; p = A[:, 0]; n = len(p)
def smooth(m):
    for l in (2, 3, 5, 7, 11, 13):
        while m % l == 0: m //= l
    return m == 1
def pct(x, i):
    lo, hi = np.searchsorted(p, p[i] // 2), np.searchsorted(p, 2 * p[i], side='right'); w = x[lo:hi]
    return ((w < x[i]).sum() + 0.5 * ((w == x[i]).sum() - 1)) / (len(w) - 1)
cols = {'N1': -A[:, 1], 'fII': -A[:, 2], 'm0': A[:, 3], 'S': -A[:, 5]}
rows = [i for i in range(n) if smooth(int(p[i]) - 1) and p[i] > 50]
print(f'{len(rows)} primes p = 1 (4) <= {X} with 13-smooth p-1, p > 50 (of {n})')
print('p N1 fII m0 S | u_N1 u_fII u_m0 u_S')
U = {k: np.array([pct(v, i) for i in rows]) for k, v in cols.items()}
for j, i in enumerate(rows):
    print(int(p[i]), A[i, 1], A[i, 2], A[i, 3], A[i, 5], '|', ' '.join(f'{U[k][j]:.2f}' for k in cols))
print('mean u over smooth primes:', {k: round(float(U[k].mean()), 3) for k in cols}, '(0.5 = typical)')
print('share with u >= 0.95:', {k: round(float((U[k] >= 0.95).mean()), 3) for k in cols})
# joint extremes: smooth cell vs a random size-matched sample of all primes
rng = np.random.default_rng(1)
allidx = rng.choice(np.where(p > 50)[0], 3000, replace=False)
UA = {k: np.array([pct(v, i) for i in allidx]) for k, v in cols.items()}
for a, b in (('N1', 'S'), ('N1', 'm0'), ('fII', 'S'), ('fII', 'm0')):
    js = float(((U[a] >= 0.95) & (U[b] >= 0.95)).mean()); ja = float(((UA[a] >= 0.95) & (UA[b] >= 0.95)).mean())
    print(f'joint top-5% in {a} and {b}: smooth cell {js:.3f}, random sample {ja:.4f}; product of smooth marginals {float((U[a] >= 0.95).mean() * (U[b] >= 0.95).mean()):.3f}')
