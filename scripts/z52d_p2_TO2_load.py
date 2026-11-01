# Shared loader: primes <= N with R(n) (triples count), minC, minW from /tmp/r1e7.txt (made by z52d_p2_TO2_renum.c N=1e7)
import numpy as np, math, sys
N = 10**7
def load(path='/tmp/r1e7.txt'):
    R = np.zeros(N+1, dtype=np.int64); minC = np.zeros(N+1, dtype=np.int64); minW = np.zeros(N+1, dtype=np.int64)
    d = np.loadtxt(path, dtype=np.int64)
    n = d[:,0]; R[n] = d[:,1]; minC[n] = d[:,2]; minW[n] = d[:,3]
    return R, minC, minW
def primes(N=N):
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
