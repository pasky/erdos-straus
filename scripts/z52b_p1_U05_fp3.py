"""z52b pass1 U05 follow-up 3: honest (cross-validated) class-mod-840 R^2 (Z0958, Z0672), Wilson-quotient controls (Z0899),
lag-840 residual correlation with CV-based class means."""
import math, numpy as np
from collections import Counter
from scipy.stats import spearmanr
D = "data/z52b/pass1/U05/2nd/"
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
N = 100000
spf = list(range(N+1))
for i in range(2, int(N**.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
isprime = lambda n: n >= 2 and spf[n] == n
UP = {}
for l in open(D+"U_primes_1e5.txt"):
    p, u, nx = map(int, l.split()); UP[p] = u
P = sorted(p for p in UP if p > 840 and p % 4 == 1)
y = {p: math.log(UP[p]/math.log(p)**2) for p in P}
rng = np.random.default_rng(7)
idx = list(P); rng.shuffle(idx)
half = len(idx)//2
A_, B_ = idx[:half], idx[half:]
def fit_means(train):
    m = {}
    g = {}
    for p in train: g.setdefault(p % 840, []).append(y[p])
    gm = np.mean([y[p] for p in train])
    return {c: (np.mean(v) if len(v) else gm) for c, v in g.items()}, gm
mA, gA = fit_means(A_)
predB = np.array([mA.get(p % 840, gA) for p in B_]); yB = np.array([y[p] for p in B_])
r2cv = 1 - ((yB-predB)**2).sum()/((yB-yB.mean())**2).sum()
log(f"Z0672/Z0958 class-mod-840 means: 2-fold CV R2 on primes≡1(4), 840<p≤1e5 (n={len(P)}) = {r2cv:.3f}  (in-sample is inflated: ~5 primes per class)")
mAll, gAll = fit_means(P)
# lag-840 correlation of residuals from class means fitted on the OTHER half (avoid self-fit leakage)
mB, gB = fit_means(B_); mA2, gA2 = fit_means(A_)
res = {}
for p in P:
    m = (mB if p in set(A_) else mA2)  # residual uses means fitted on the other half
    res[p] = y[p] - m.get(p % 840, gB if p in set(A_) else gA2)
for k in (1, 2, 5, 10):
    pr = [(p, p+840*k) for p in P if (p+840*k) in UP and isprime(p+840*k) and p+840*k in y]
    a = np.array([res[p] for p, _ in pr]); b = np.array([res[q] for _, q in pr])
    raw = np.corrcoef([y[p] for p, _ in pr], [y[q] for _, q in pr])[0,1]
    log(f"  Z0958 lag 840·{k}: pairs={len(pr)} raw corr={raw:.3f}  residual corr (cross-fitted class means)={np.corrcoef(a,b)[0,1]:.3f}")
# ---- Z0899 Wilson quotient controls
def wilson_q(p):
    f = 1
    for i in range(2, p): f = f*i % (p*p)
    return ((f + 1) // p) % p
pp = [p for p in range(5, 20001) if isprime(p) and p % 4 == 1]
W = {p: wilson_q(p)/p for p in pp}  # normalised to [0,1): raw W_p scales with p
ys = {p: math.log(UP[p]/math.log(p)**2) if p in UP else None for p in pp}
ok = [p for p in pp if ys[p] is not None]
r, pv = spearmanr([W[p] for p in ok], [ys[p] for p in ok])
r2, pv2 = spearmanr([W[p] for p in ok], [p for p in ok])
# residual on class mod 840 (cross-fitted, half split) to test non-trivial content
rc = {p: ys[p] - mAll.get(p % 840, gAll) for p in ok}
r3, pv3 = spearmanr([W[p] for p in ok], [rc[p] for p in ok])
log(f"Z0899 Wilson quotient W_p=((p-1)!+1)/p mod p vs log(U/log²p), p≡1(4), p≤2e4 (n={len(ok)}): rho={r:.3f} (p={pv:.1e}); "
    f"vs p itself rho={r2:.3f} (sanity: should be ~0 after normalisation); vs class-mod-840-residual rho={r3:.3f} (p={pv3:.2f})")
open(D+"fp3_out.txt", "w").write("\n".join(out)+"\n")
