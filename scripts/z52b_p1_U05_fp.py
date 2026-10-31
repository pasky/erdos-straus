"""z52b pass1 U05: data-fingerprint items (Z0688 Z0777 Z0812 Z0818 Z0821 Z0842 Z0899 Z0903 Z0910 Z0950 Z0951
Z0958 Z0962 Z0672 Z0710). Inputs: data/z52b/pass1/U05/2nd/U_2_30000.txt (n U nx), U_primes_1e5.txt (p U nx),
computed by scripts/z52b_p1_U05_ucount.c. Output printed; saved to data/z52b/pass1/U05/2nd/fp_out.txt."""
import math, sys, random
import numpy as np
from collections import Counter
D = "data/z52b/pass1/U05/2nd/"
U = {}; NX = {}
for l in open(D+"U_2_30000.txt"):
    n, u, nx = map(int, l.split()); U[n] = u; NX[n] = nx
UP = {}
for l in open(D+"U_primes_1e5.txt"):
    p, u, nx = map(int, l.split()); UP[p] = (u, nx)
N = 100000
spf = list(range(N+1))
for i in range(2, int(N**.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = Counter()
    while n > 1:
        q = spf[n]; f[q] += 1; n //= q
    return f
def isprime(n): return n >= 2 and spf[n] == n
primes = [p for p in range(5, N+1) if isprime(p)]
P1 = [p for p in primes if p % 4 == 1]
P3 = [p for p in primes if p % 4 == 3]
def leg(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
def spearman(x, y):
    from scipy.stats import spearmanr
    r, pv = spearmanr(x, y); return r, pv
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---- Z0688: least-QNR record primes and regression
lq = {}
for p in P1:
    q = 2
    while leg(q, p) != -1: q = next(r for r in range(q+1, q+200) if isprime(r))
    lq[p] = q
rec = {}
for p in P1:
    if lq[p] not in rec: rec[lq[p]] = p   # least p≡1(4) with that least QNR
vals = {q: round(UP[p][0]/math.log(p)**2, 2) for q, p in sorted(rec.items()) if q in (11,13,17,19,23,29,31,37,41,43,47)}
log("Z0688 least p≡1(4) per least-QNR q: (p, U(p)/log²p)", {q: (rec[q], round(UP[rec[q]][0]/math.log(rec[q])**2, 3)) for q in sorted(rec)[:12]})
def Lapprox(p, M=400):
    return sum(leg(n, p)/n for n in range(1, M+1))
def sigma_ratio(p):
    f = fac(p-1); s = 1.0
    m = p-1
    sig = 1
    for q, e in f.items(): sig *= (q**(e+1)-1)//(q-1)
    return sig/(p-1)
X = []; Y = []
for p in P1[:1200]:
    X.append([1.0, math.log(max(Lapprox(p), 1e-3)), math.log(sigma_ratio(p))]); Y.append(math.log(UP[p][0]))
X = np.array(X); Y = np.array(Y)
beta, res, *_ = np.linalg.lstsq(X, Y, rcond=None)
r2 = 1 - ((Y - X @ beta)**2).sum()/((Y - Y.mean())**2).sum()
log(f"Z0688 regression logU ~ 1 + logL(1,chi_p)[M=400] + log(sigma(p-1)/(p-1)) over {len(Y)} primes p≡1(4)<1e5: coef={np.round(beta,3).tolist()} R2={r2:.3f}")
# ---- Z0777: zeros of U(n), n<=30000
zeros = [n for n in range(2, 30001) if U[n] == 0]
log("Z0777 zeros U(n)=0, 2<=n<=30000: count", len(zeros), "first", zeros[:25])
log("  even zeros:", sum(1 for n in zeros if n % 2 == 0), " n≡1 mod 4 zeros:", [n for n in zeros if n % 4 == 1], " n≡3 mod 4:", sum(1 for n in zeros if n % 4 == 3))
# ---- Z0812: safe primes vs all primes ≡3 (mod 4)
safe = [p for p in P3 if isprime((p-1)//2) and (p-1)//2 > 2]
def norm(p): return UP[p][0]/math.log(p)**2
log(f"Z0812 safe primes ≤1e5: {len(safe)}, mean U/log²p = {np.mean([norm(p) for p in safe]):.3f} vs all p≡3(4): {np.mean([norm(p) for p in P3]):.3f}")
def Ppl(n):
    f = fac(n); return max(f) if f else 1
r, pv = spearman([math.log(Ppl(p-1))/math.log(p) for p in P3], [norm(p) for p in P3])
log(f"  Spearman(U/log², log P+(p-1)/log p) over p≡3(4): {r:.3f} (p={pv:.1e})")
# ---- Z0818: concentration U/nx over primes <=1e5 (nx = #distinct x), and median
ratio = [UP[p][0]/UP[p][1] for p in primes if UP[p][1] > 0]
log(f"Z0818 U/nx over primes ≤1e5: median {np.median(ratio):.2f}, 90% {np.percentile(ratio,90):.2f}")
# ---- Z0821: composite n=pq<=30000, regression log U(pq) on log U(p), log U(q)
Yc=[]; Xc=[]
for p in primes:
    for q in primes:
        if q <= p or p*q > 30000: continue
        if U[p] > 0 and U[q] > 0 and U[p*q] > 0:
            Yc.append(math.log(U[p*q])); Xc.append([1.0, math.log(U[p]), math.log(U[q])])
A = np.array(Xc); Yc = np.array(Yc)
beta = np.linalg.lstsq(A, Yc, rcond=None)[0]
rr = 1 - ((Yc - A @ beta)**2).sum()/((Yc - Yc.mean())**2).sum()
log(f"Z0821 log U(pq) ~ a + b log U(p) + c log U(q) (pq≤3e4, {len(Yc)} pairs): coef {np.round(beta,3).tolist()}, R2={rr:.3f}")
# ---- Z0842: clusters among hardest primes
hard = sorted(P1, key=norm)[:200]
qs = [q for q in primes if q <= 47]
F = []
for p in hard:
    row = [1.0 if leg(q, p) == 1 else 0.0 for q in qs]
    row += [1.0 if (p+3) % q == 0 else 0.0 for q in qs]
    row += [1.0 if (p-1) % q == 0 else 0.0 for q in qs]
    F.append(row)
F = np.array(F)
rng = np.random.default_rng(1)
def kmeans(X, k, iters=100):
    C = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        d = ((X[:, None, :] - C[None])**2).sum(-1); lab = d.argmin(1)
        C = np.array([X[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
    inertia = ((X - C[lab])**2).sum()
    return lab, inertia
base_var = ((F - F.mean(0))**2).sum()
for k in (2, 3, 4):
    best = min((kmeans(F, k) for _ in range(20)), key=lambda t: t[1])
    log(f"Z0842 k-means k={k} on 200 hardest primes (≤1e5, p≡1(4)): inertia ratio {best[1]/base_var:.3f}, sizes {np.bincount(best[0]).tolist()}")
# ---- Z0899: Wilson quotient vs U
def wilson_q(p):
    f = 1
    for i in range(2, p): f = f*i % p
    return ((f*(p-1) + 1) % (p*p)) // p   # ((p-1)!+1)/p mod p  (since (p-1)! ≡ -1 mod p)
ws = {p: wilson_q(p) for p in primes if p <= 20000}
pp = [p for p in ws if p % 4 == 1]
r, pv = spearman([ws[p] for p in pp], [norm(p) for p in pp])
log(f"Z0899 Spearman(Wilson quotient mod p, U/log²p) over p≡1(4), p≤2e4 ({len(pp)}): {r:.3f} (p={pv:.2f})")
# ---- Z0903: Sylvester-related n
log("Z0903 U(43)=%d nx=%d; U(1807)=%d nx=%d; neighbours U(1805..1809)=%s" % (U[43], NX[43], U[1807], NX[1807], [U[n] for n in range(1805,1810)]))
# ---- Z0910: Ramanujan-sum expansion, n<=30000
def mobius(n):
    f = fac(n); 
    if any(e > 1 for e in f.values()): return 0
    return -1 if len(f) % 2 else 1
def ramanujan(q, n):
    g = math.gcd(q, n); return sum(mobius(q//d)*d for d in range(1, g+1) if g % d == 0)
Qs = list(range(1, 31))
ns = [n for n in range(3, 30001) if U[n] > 0]
M = np.array([[ramanujan(q, n) for q in Qs] for n in ns], dtype=float)
y = np.array([U[n]/math.log(n)**3 for n in ns])
coef, *_ = np.linalg.lstsq(M, y, rcond=None)
r2 = 1 - ((y - M @ coef)**2).sum()/((y - y.mean())**2).sum()
log("Z0910 fit U(n)/log³n on c_q(n), q≤30: R2=%.3f; coef a_q: %s" % (r2, {q: round(c, 4) for q, c in zip(Qs[:12], coef[:12])}))
log("  multiplicativity check a_6 vs a_2*a_3: %.4f vs %.4f ; a_10 vs a_2*a_5: %.4f vs %.4f" % (coef[5], coef[1]*coef[2], coef[9], coef[1]*coef[4]))
# ---- Z0950: lowest U/log^3 composites
comp = [n for n in range(4, 30001) if not isprime(n) and U[n] > 0]
low = sorted(comp, key=lambda n: U[n]/math.log(n)**3)[:15]
log("Z0950 lowest U/log³n composites ≤3e4:", [(n, dict(fac(n)), U[n]) for n in low[:8]])
log("  of the 15 lowest: all prime factors ≡1 mod 24 (both primes):", sum(1 for n in low if all(q % 24 == 1 for q in fac(n))), "/15")
# ---- Z0951: omega1/omega3 regression
Xs = []; Ys = []
for n in comp:
    f = fac(n)
    w1 = sum(1 for q in f if q % 4 == 1); w3 = sum(1 for q in f if q % 4 == 3)
    Xs.append([1, w1, w3]); Ys.append(math.log(U[n]))
Xs = np.array(Xs, float); Ys = np.array(Ys)
b = np.linalg.lstsq(Xs, Ys, rcond=None)[0]
log(f"Z0951 log U(n) ~ 1 + ω1 + ω3 over {len(Ys)} composites ≤3e4: coef {np.round(b,3).tolist()}")
# ---- Z0958: lag-840k residual correlation among primes
resid = {p: math.log(norm(p)) for p in primes if p > 840 and p <= 100000}
lagc = {}
for k in range(1, 11):
    pairs = [(p, p+840*k) for p in resid if (p+840*k) in resid]
    if len(pairs) < 10: continue
    a = np.array([resid[p] for p, _ in pairs]); b2 = np.array([resid[q] for _, q in pairs])
    lagc[k] = (len(pairs), round(float(np.corrcoef(a, b2)[0, 1]), 3))
log("Z0958 corr(log U/log²p at p, p+840k) for primes ≤1e5:", lagc)
# ---- Z0962
ps7 = [p for p in P1 if p <= 7500]
a = [U[p] for p in ps7]; b4 = [U[4*p+1] for p in ps7]; c4 = [U[(p+3)//4] for p in ps7]
log("Z0962 Spearman(U(p),U(4p+1)) =", round(spearman(a, b4)[0], 3), "; Spearman(U(p),U((p+3)/4)) =", round(spearman(a, c4)[0], 3), f"(n={len(ps7)})")
# ---- Z0672: explained variance of log(U/log²p) by quadratic characters mod q<=100
qs100 = [q for q in primes if q <= 100]
Xc = np.array([[1.0] + [leg(q, p) for q in qs100] for p in P1], float)
Yc = np.array([math.log(norm(p)) for p in P1])
idx = np.arange(len(Yc)); rng.shuffle(idx); folds = np.array_split(idx, 5)
pred = np.zeros_like(Yc)
for f_ in folds:
    tr = np.setdiff1d(idx, f_)
    bb = np.linalg.lstsq(Xc[tr], Yc[tr], rcond=None)[0]
    pred[f_] = Xc[f_] @ bb
r2cv = 1 - ((Yc - pred)**2).sum()/((Yc - Yc.mean())**2).sum()
bb = np.linalg.lstsq(Xc, Yc, rcond=None)[0]
r2 = 1 - ((Yc - Xc @ bb)**2).sum()/((Yc - Yc.mean())**2).sum()
log(f"Z0672 log(U/log²p) on (q/p), q≤100 ({len(P1)} primes≡1(4)≤1e5): in-sample R2={r2:.3f}, 5-fold CV R2={r2cv:.3f}")
# ---- Z0710: record positions of U(n)
rec = []; best = 0
for n in range(2, 30001):
    if U[n] > best: best = U[n]; rec.append(n)
tau = lambda n: math.prod(e+1 for e in fac(n).values())
trec = []; bt = 0
for n in range(1, 30001):
    t = tau(n)
    if t > bt: bt = t; trec.append(n)
HCN = {1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040,7560,10080,15120,20160,25200,27720}
log("Z0710 record positions of U(n) ≤3e4 (strict):", rec[:30])
log("  overlap with τ-record set (highly composite): %d of %d U-records are τ-records" % (len(set(rec) & set(trec)), len(rec)))
open(D+"fp_out.txt", "w").write("\n".join(out)+"\n")
