"""OMEGA10: sign of X = sum_V mu^V N_A(V) N_{A+L}(V) (QM induction cross term). Usage: seed trials nmax"""
import sys, numpy as np
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def mob(n, f):
    R = np.arange(1<<n); t = f.astype(float).copy()
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    return t
def tau(n, edges):
    R = np.arange(1<<n); t = np.ones(1<<n)
    for e in edges:
        m = sum(1 << v for v in e); t *= ((R & m) != 0)
    return t
def wvec(n, mu):
    R = np.arange(1<<n); w = np.ones(1<<n)
    for i in range(n): w = np.where((R >> i) & 1, w * mu[i], w)
    return w
w1 = w2 = -9
for tr in range(trials):
    n = int(rng.integers(2, nmax+1)); kmax = int(rng.integers(1, n+1))
    re = lambda: tuple(sorted(rng.choice(n, int(rng.integers(1,kmax+1)), replace=False).tolist()))
    A = [re() for _ in range(int(rng.integers(1,2*n)))]; L = [re() for _ in range(int(rng.integers(1,2*n)))]
    a = rng.random(n)*rng.choice([0.,1.], n, p=[.15,.85])
    s = max(sum(a[v] for v in e) for e in A+L)
    if s == 0: continue
    lam = 2**(a/s*rng.choice([1.0, rng.random()])); mu = lam-1
    W = wvec(n, mu); ta = mob(n, tau(n,A)); tb = mob(n, tau(n,A+L))
    X = float(np.sum(W*ta*tb)); QA = float(np.sum(W*ta*ta))
    if -X > w1: w1 = -X; print(f"min X = {X:.4g}  QA={QA:.4f} A={A} L={L}", flush=True)
    if (QA-1)/2 - X > w2: w2 = (QA-1)/2 - X; print(f"   (QA-1)/2 - X = {w2:.4g}", flush=True)
