"""z52b Pass-1 U03 extra checks (proxy objects; see summaries). Uses feat_P100000_K100.npz + direct computations."""
import numpy as np, math
from math import gcd
def rank(x): return np.argsort(np.argsort(np.asarray(x, float)))
def spear(a, b): return float(np.corrcoef(rank(a), rank(b))[0, 1])
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64); om = d["om"]
NP = len(pr); RK = R.sum(1); S = R == 0; L = np.log1p(RK)
print("== Z1562 stratify S1&S2 by p mod 8 and mod 3")
for r8 in [1, 5]:
    m = (pr % 8) == r8
    print(f" p%8={r8}: n={m.sum()} P(S1&S2)={(S[m,0]&S[m,1]).mean():.4f} prod={S[m,0].mean()*S[m,1].mean():.4f} P(S1)={S[m,0].mean():.3f} P(S2)={S[m,1].mean():.3f}")
print("== Z1816 largest |corr| pairs among S_C, C<=30")
X = S[:, :30].astype(float); Cm = np.corrcoef(X.T); np.fill_diagonal(Cm, 0)
i, j = np.unravel_index(np.argmax(np.abs(Cm)), Cm.shape); print(f" max pair C={i+1},{j+1} corr={Cm[i,j]:.3f}")
top = sorted([(abs(Cm[a,b]), a+1, b+1) for a in range(30) for b in range(a+1, 30)], reverse=True)[:5]
print(" top5:", [(c, a, b) for c, a, b in [(round(t[0],3), t[1], t[2]) for t in top]])
print("== Z0789/Z0788 shift spectrum: spearman(log1p R_K(p), log tau(p+s))")
N = int(pr[-1]) + 60
tau = np.zeros(N + 1, np.int32)
for dd in range(1, N + 1): tau[dd::dd] += 1
res = [(s, round(spear(L, np.log(tau[pr + s])), 3)) for s in range(1, 51)]
print(" s=1,2,3,4,12:", [r for r in res if r[0] in (1, 2, 3, 4, 12)], " max|rho| s:", max(res, key=lambda t: abs(t[1])))
print(" Z0788 sum_{d<=8} tau(p+4d):", round(spear(L, sum(np.log(tau[pr + 4*dd]) for dd in range(1, 9))), 3),
      " tau((p+3)/4):", round(spear(L, np.log(tau[(pr + 3)//4])), 3))
print("== Z0912 lag-1 corr of log1p R_K between consecutive primes (==1 mod 4), mean-removed")
Lc = L - L.mean(); print(" lag1:", round(float(np.corrcoef(Lc[:-1], Lc[1:])[0, 1]), 4))
print("== Z0960 least prime q = 1 mod p vs R_K")
from math import isqrt
Q = 3 * 10**7
sv = np.ones(Q + 1, bool); sv[:2] = False
for i in range(2, isqrt(Q) + 1):
    if sv[i]: sv[i*i::i] = False
least = []
for p in pr:
    p = int(p); q = 0
    for k in range(1, 10**6):
        c = k * p + 1
        if c > Q: break
        if sv[c]: q = c; break
    least.append(q)
least = np.array(least); okq = least > 0
print(" n with q found:", int(okq.sum()), " spearman(log q, log1p RK):", round(spear(np.log(least[okq]), L[okq]), 4))
print("== Z0916 Kloosterman K(1,1;p) vs R_K, p<=2e4")
mk = pr <= 20000; K_ = []
for p in pr[mk]:
    p = int(p); x = np.arange(1, p); inv = np.array([pow(int(a), -1, p) for a in x])
    K_.append(float(np.cos(2*np.pi*((x + inv) % p) / p).sum()))
K_ = np.array(K_); print(" spearman(K(1,1;p), log1p RK):", round(spear(K_, L[mk]), 4), " n=", int(mk.sum()))
print("== Z3156 residues of R_K mod l (all p<=1e5)")
for l in [2, 3, 5, 7]:
    cnt = np.bincount(RK % l, minlength=l) / NP; print(f" l={l}:", np.round(cnt, 3))
print("== Z1452 counts of Cmin vs ...: done in analyse.")
print("== Z2038 y=kx chains: 4/p=1/x+1/(kx)+1/z (z free), p<=1e4")
sp = [int(p) for p in pr if p <= 10**4]
for k in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]:
    hits = 0
    for p in sp:
        ok = False
        lo = -(-p*(k+1)//(4*k)); hi = p*(2*k+1)//(4*k)
        for x in range(lo, hi + 1):
            num = 4*k*x - p*(k+1)
            if num > 0 and (p*k*x) % num == 0: ok = True; break
        hits += ok
    print(f" k={k}: solvable {hits}/{len(sp)} = {hits/len(sp):.3f}")
