"""Fix round TO3 (Z0780, Z0781): BM main term M_BM(p) (same formula as scripts/z52b_fingerprint_bm.py) for EVERY prime
p = 1 (mod 4) in [1e4, HI), multiprocessing (4 workers). R from the 1e8 word census. Output /tmp/z52/big/mbm_full.npz.
Then Poisson / negative-binomial tests of the R-zero and small-R statistics (writes data/z52b/pass2/TO3/mbm_full_results.json).
Run: uv run --with numpy --with scipy --with sympy python scripts/z52d_p2_TO3_mbm_full.py 300000"""
import sys, json, math
import numpy as np
from math import gcd
from multiprocessing import Pool
HI = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
LO = 10**4
def build_pairs(H):
    pairs = []
    for u in range(1, H + 2):
        if 4 * u - u - 1 > H: break
        for B in range(1, H + 2):
            if 4 * u * B - u - B > H: break
            if (u + B) % 2 == 1 and gcd(u, B) == 1: pairs.append((u, B))
    return np.array(pairs, dtype=np.int64)
PAIRS = None; LIM = None; WTS = None
def init():
    global PAIRS, LIM, WTS
    pr = build_pairs(HI)
    q = 4 * pr[:, 0] * pr[:, 1]
    lim = 4 * pr[:, 0] * pr[:, 1] - pr[:, 0] - pr[:, 1]
    MAX = int(q.max()); phis = np.arange(MAX + 1, dtype=np.int64)
    for i in range(2, MAX + 1):
        if phis[i] == i: phis[i::i] -= phis[i::i] // i
    w = 1.0 / phis[q]
    o = np.argsort(lim)
    PAIRS = pr[o]; LIM = lim[o]; WTS = w[o]
def mbm(p):
    k = np.searchsorted(LIM, p, side='right')
    a = (-(PAIRS[:k, 0] * PAIRS[:k, 1])) % p
    e = (p - 1) // 2
    r = np.ones(k, dtype=np.int64); base = a.copy(); ee = e
    while ee:
        if ee & 1: r = (r * base) % p
        base = (base * base) % p; ee >>= 1
    chi = np.where(r == 1, 1, -1)
    M0 = WTS[:k].sum(); T = (chi * WTS[:k]).sum()
    return M0 - T
def work(ps):
    init_ = globals()
    return [(p, mbm(p)) for p in ps]
if __name__ == '__main__':
    import sympy
    init()
    ps = [int(x) for x in sympy.primerange(LO, HI) if x % 4 == 1]
    chunks = [ps[i::32] for i in range(32)]
    with Pool(4, initializer=init) as pool:
        res = pool.map(work, chunks)
    rows = sorted([r for c in res for r in c])
    P = np.array([r[0] for r in rows], dtype=np.int64); M = np.array([r[1] for r in rows])
    np.savez('/tmp/z52/big/mbm_full.npz', p=P, M=M)
    print('primes', len(P))
