"""O131: load exf_engine dumps. Records: u32 n,a,c,d; u64 b (packed, 24 bytes)."""
import numpy as np
from math import gcd
DT = np.dtype([('n','<u4'),('a','<u4'),('c','<u4'),('d','<u4'),('b','<u8')])
def load(prefix):
    return np.fromfile(prefix+'.T1.bin', dtype=DT), np.fromfile(prefix+'.T2.bin', dtype=DT)
def gcd_arr(x, y):
    x = x.astype(np.int64).copy(); y = y.astype(np.int64).copy()
    while np.any(y):
        m = y != 0
        x[m], y[m] = y[m], x[m] % y[m]
    return x

def expand_T1(T1, N):
    """exf_engine Type I enumerates only f | 4a^2 d + 1 (complete for primes).  For composite n the general
    solution is (n,a,b,c,d) = (k m, a, b, k c', d) with (m,a,b,c',d) an engine solution (proof: EXACT_FORMULA.md §1).
    Expand by all k with k m <= N and deduplicate."""
    out = []
    for k in range(1, N + 1):
        sel = T1[T1['n'].astype(np.int64) * k <= N]
        if len(sel) == 0: break
        r = sel.copy(); r['n'] = sel['n'] * k; r['c'] = sel['c'] * k
        out.append(r)
    A = np.concatenate(out)
    key = np.stack([A['n'].astype(np.uint64), A['a'].astype(np.uint64), A['c'].astype(np.uint64), A['d'].astype(np.uint64), A['b']], 1)
    _, idx = np.unique(key, axis=0, return_index=True)
    return A[np.sort(idx)]

def load_full(prefix, N):
    T1, T2 = load(prefix)
    return expand_T1(T1, N), T2
