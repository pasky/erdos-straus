"""Data check of the Brauer–Manin main term (FRONTIER §2.2): M_BM(p) = Σ_{(u,B)∈P(p), gcd(p,4uB)=1} (1 − χ_{−4uB}(p))/φ(4uB),
P(n) = {(u,B): gcd(u,B)=1, u+B odd, 4uB−u−B ≤ n}. Correlate with R(p) and U(p) at primes p≡1(4) in [lo,hi]."""
import numpy as np, sys, json
from math import gcd
from sympy import isprime
from scipy.stats import spearmanr, pearsonr
lo, hi = int(sys.argv[1]), int(sys.argv[2])
N = 4*hi + 10
phi = np.arange(N+1, dtype=np.int64)
for i in range(2, N+1):
    if phi[i] == i:
        phi[i::i] -= phi[i::i] // i
pairs = []
for u in range(1, hi+2):
    if 4*u - u - 1 > hi: break
    for B in range(1, hi+2):
        if 4*u*B - u - B > hi: break
        if (u+B) % 2 == 1 and gcd(u, B) == 1: pairs.append((u, B))
pairs = np.array(pairs, dtype=np.int64); q = 4*pairs[:,0]*pairs[:,1]; lim = 4*pairs[:,0]*pairs[:,1] - pairs[:,0] - pairs[:,1]
w = 1.0/phi[q]
W = np.load('data/z52b/raw/words_3e6.npy')
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64); Ud = dict(zip(F[:,0], F[:,1]))
def powmod(a, e, m):
    r = np.ones_like(a); a = a % m
    while e:
        if e & 1: r = (r*a) % m
        a = (a*a) % m; e >>= 1
    return r
rows = []
for p in range(lo, hi+1):
    if p % 4 != 1 or not isprime(p): continue
    sel = lim <= p
    a = (-(pairs[sel,0]*pairs[sel,1])) % p
    leg = powmod(a, (p-1)//2, p); chi = np.where(leg == 1, 1, -1)   # Legendre(-uB/p) = Kronecker(-4uB/p)
    M0 = w[sel].sum(); T = (chi*w[sel]).sum(); Mbm = M0 - T
    rows.append((p, M0, T, Mbm, int(W[p-1,3]), int(Ud.get(p, -1))))
rows = np.array(rows)
P, M0, T, Mbm, R, U = rows.T
lp = np.log(P)
def resid(y):
    X = np.vstack([np.ones_like(lp), lp, np.log(lp)]).T; return y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
out = dict(n=len(P), mean_R_over_Mbm=float(np.mean(R/Mbm)), mean_R_over_M0=float(np.mean(R/M0)),
           spearman_R_Mbm=spearmanr(R, Mbm)[0], spearman_resR_resMbm=spearmanr(resid(np.log(R+1)), resid(np.log(Mbm)))[0],
           spearman_resU_resMbm=spearmanr(resid(np.log(U+1)), resid(np.log(Mbm)))[0] if (U>0).all() else None,
           spearman_resR_T=spearmanr(resid(np.log(R+1)), T)[0], pearson_R_Mbm=pearsonr(R, Mbm)[0],
           R_zero_primes=[int(x) for x in P[R==0]], Mbm_at_R_zero=[float(x) for x in Mbm[R==0]],
           Mbm_quantile_of_R_zeros=[float((Mbm < m).mean()) for m in Mbm[R==0]])
print(json.dumps(out, indent=1))
json.dump(out, open(f'data/z52b/bm_check_{lo}_{hi}.json', 'w'), indent=1)
