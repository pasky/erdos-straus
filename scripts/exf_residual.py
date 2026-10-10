"""O131: (i) best least-squares fit of each ES family by the classical dictionary (primes 5..2e4, held-out test);
(ii) signed differences T2- - T2+, T1- - T1+ on primes."""
import numpy as np
from sympy import isprime
Z = np.load('data/exf/columns_2e4.npz'); C = [k for k in Z if k.startswith('C:')]
N = len(Z['C:1']) - 1
pr = np.array([p for p in range(5, N + 1) if isprime(p)])
X = np.stack([Z[k][pr] for k in C], 1).astype(float)
X /= np.maximum(np.abs(X).max(0), 1)
tr = pr < 10000; te = ~tr
for f in ('T1p', 'T1m', 'T2p', 'T2m', 'T1p.prim', 'T2p.prim'):
    y = Z['ES:' + f][pr].astype(float)
    coef, *_ = np.linalg.lstsq(X[tr], y[tr], rcond=None)
    r = y - X @ coef
    print(f'{f:9s} train rel.resid {np.linalg.norm(r[tr])/np.linalg.norm(y[tr]-y[tr].mean()):.3f}  test rel.resid {np.linalg.norm(r[te])/np.linalg.norm(y[te]-y[te].mean()):.3f}  (vs. centred norm) test rms {np.sqrt((r[te]**2).mean()):.1f}  mean y {y[te].mean():.1f}')
for a, b in (('T2m', 'T2p'), ('T1m', 'T1p')):
    D = Z['ES:' + a][pr] - Z['ES:' + b][pr]
    print(f'{a}-{b} on primes: min {D.min()} max {D.max()} mean {D.mean():.2f}  P(<0) {np.mean(D<0):.3f}  corr with {b}: {np.corrcoef(D, Z["ES:"+b][pr])[0,1]:.3f}')
    for m4 in (1, 3):
        s = pr % 4 == m4; print(f'   p≡{m4} mod 4: mean {D[s].mean():.2f}, P(<0) {np.mean(D[s]<0):.3f}')
