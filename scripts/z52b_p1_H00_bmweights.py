"""Z0042 pass-1: do the per-prime weights β_q of the BM-corrected main term M_BM(p) (BM_CORRECTED_COUNT §2)
match the fitted β_q of log U(p) (data/z52b/qweights.json)?  p ≡ 1 (4), 100 < p < 30000.
Regress log M_BM(p) and log(U+1) on (q/p), q < 80, with controls 1, log p, log log p."""
import numpy as np, json
from math import gcd
from sympy import isprime, legendre_symbol, primerange
hi = 30000
N = 4*hi + 10
phi = np.arange(N+1, dtype=np.int64)
for i in range(2, N+1):
    if phi[i] == i: phi[i::i] -= phi[i::i]//i
pairs = []
for u in range(1, hi):
    if 3*u - 1 > hi: break
    B = 1
    while 4*u*B - u - B <= hi:
        if (u+B) % 2 and gcd(u, B) == 1: pairs.append((u, B))
        B += 1
pairs = np.array(pairs, dtype=np.int64); uB = pairs[:,0]*pairs[:,1]; lim = 4*uB - pairs[:,0] - pairs[:,1]
w = 1.0/phi[4*uB]
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64); Ud = dict(zip(F[:,0].tolist(), F[:,1].tolist()))
def powmod(a, e, m):
    r = np.ones_like(a); a = a % m
    while e:
        if e & 1: r = (r*a) % m
        a = (a*a) % m; e >>= 1
    return r
P, M0, MBM, U = [], [], [], []
for p in range(101, hi+1):
    if p % 4 != 1 or not isprime(p): continue
    s = lim <= p; a = (-uB[s]) % p
    chi = np.where(powmod(a, (p-1)//2, p) == 1, 1, -1)
    P.append(p); M0.append(w[s].sum()); MBM.append(((1-chi)*w[s]).sum()); U.append(Ud[p])
P = np.array(P); lp = np.log(P.astype(float))
qs = list(primerange(2, 80))
Xc = np.array([[int(legendre_symbol(q, int(p))) for q in qs] for p in P], float)
X = np.hstack([np.vstack([np.ones_like(lp), lp, np.log(lp)]).T, Xc])
out = {}
for name, y in (('logMBM', np.log(np.array(MBM))), ('logM0', np.log(np.array(M0))), ('logU1', np.log(np.array(U)+1.0))):
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    out[name] = {q: round(float(q*b[3+i]), 3) for i, q in enumerate(qs)}
print('n =', len(P))
print('q    q*beta(logMBM)  q*beta(logU+1)')
for q in qs: print(f'{q:3d} {out["logMBM"][q]:+8.3f} {out["logU1"][q]:+8.3f}   (M0: {out["logM0"][q]:+.3f})')
a = np.array([out['logMBM'][q] for q in qs]); c = np.array([out['logU1'][q] for q in qs])
out['corr_qbeta_MBM_vs_U'] = float(np.corrcoef(a, c)[0, 1])
out['corr_qbeta_MBM_vs_U_q_ge_5'] = float(np.corrcoef(a[2:], c[2:])[0, 1])
print('corr', out['corr_qbeta_MBM_vs_U'], out['corr_qbeta_MBM_vs_U_q_ge_5'])
json.dump(out, open('data/z52b/pass1/H00/bmweights.json', 'w'), indent=1)
