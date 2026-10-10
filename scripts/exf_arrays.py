"""O131: build count arrays (n<=N) for T1±, T2±, total and per-d, save npz."""
import numpy as np
from exf_load import load_full
N = 20000; DMAX = 40
out = {}
for pre, s in (('n2e4', 'p'), ('m2e4', 'm')):
    T1, T2 = load_full('data/exf/'+pre, N)
    for nm, T in (('T1'+s, T1), ('T2'+s, T2)):
        out[nm] = np.bincount(T['n'], minlength=N+1)
        out[nm+'_diag'] = np.bincount(T['n'][T['a'] == T['b']], minlength=N+1)
        out[nm+'_a1'] = np.bincount(T['n'][T['a'] == 1], minlength=N+1)
        byd = np.zeros((DMAX+1, N+1), np.int64)
        for d in range(1, DMAX+1): byd[d] = np.bincount(T['n'][T['d'] == d], minlength=N+1)
        out[nm+'_byd'] = byd
        byc = np.zeros((DMAX+1, N+1), np.int64)
        for c in range(1, DMAX+1): byc[c] = np.bincount(T['n'][T['c'] == c], minlength=N+1)
        out[nm+'_byc'] = byc
np.savez_compressed('data/exf/arrays_2e4.npz', **out)
sq = [m*m for m in range(1, 30)]
for k in ('T1p', 'T1m', 'T2p', 'T2m'):
    print(k, 'n=1..30:', out[k][1:31].tolist())
    print('   squares:', [int(out[k][s]) for s in sq])
    z = np.nonzero(out[k][1:] == 0)[0] + 1
    print('   zeros (first 30):', z[:30].tolist(), ' #zeros', len(z))
