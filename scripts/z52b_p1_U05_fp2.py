"""z52b pass1 U05 follow-ups: Z0777 (U-certificate zero set, definition of fingerprint-0178: v≥3, v∈4Z∪(8Z−n),
n+v has a divisor ≡ −1 mod v), Z0899 (Wilson quotient, corrected mod p² arithmetic), Z0958 (lag correlations after
removing mod-840 class means), Z0962 (size-normalised), Z0672 (class-mod-840 R² as comparison)."""
import math, numpy as np
from collections import Counter
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
def fac(n):
    f = Counter()
    while n > 1:
        q = spf[n]; f[q] += 1; n //= q
    return f
def divs(n):
    ds = [1]
    for q, e in fac(n).items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def isprime(n): return n >= 2 and spf[n] == n
U = {}; NX = {}
for l in open(D+"U_2_30000.txt"):
    n, u, nx = map(int, l.split()); U[n] = u; NX[n] = nx
UP = {}
for l in open(D+"U_primes_1e5.txt"):
    p, u, nx = map(int, l.split()); UP[p] = (u, nx)
# ---- Z0777
def Uv(n, V=1500):
    c = 0
    for v in range(3, V):
        if not (v % 4 == 0 or (v + n) % 8 == 0): continue   # v ∈ 4Z ∪ (8Z − n)
        if any(d % v == v-1 for d in divs(n+v)): c += 1
    return c
zs = [n for n in range(2, 301) if Uv(n) == 0]
log("Z0777 U-certificate zeros (fingerprint-0178 def, V=1500), n≤300:", zs)
log("  claimed list starts 12,28,60,96,105,124,156,204,228,288 — reproduced:", [z for z in [12,28,60,96,105,124,156,204,228,288] if z in zs])
log("  zeros ≡1 mod 4 in range:", [z for z in zs if z % 4 == 1], " even zeros:", sum(1 for z in zs if z % 2 == 0), "of", len(zs))
log("  check 2961 (claimed zero):", Uv(2961, 3000) == 0)
# ---- Z0899 corrected Wilson quotient
def wilson_q(p):
    f = 1
    for i in range(2, p): f = f*i % (p*p)       # (p-1)! mod p^2
    assert (f + 1) % p == 0
    return ((f + 1) // p) % p
primes = [p for p in range(5, 20001) if isprime(p)]
W = {p: wilson_q(p) for p in primes}
from scipy.stats import spearmanr
pp = [p for p in primes if p % 4 == 1]
nrm = lambda p: UP[p][0]/math.log(p)**2 if p in UP else float('nan')
r, pv = spearmanr([W[p] for p in pp], [nrm(p) for p in pp])
log(f"Z0899 Spearman(Wilson quotient mod p, U/log²p) over p≡1(4), 5<p≤2e4 ({len(pp)}): {r:.3f} (p={pv:.2f})")
# ---- Z0958: residual after removing mod-840 class means
prim = {p: math.log(nrm(p)) for p in UP if p > 840 and isprime(p)}
cls = {}
for p, v in prim.items(): cls.setdefault(p % 840, []).append(v)
cm = {c: np.mean(v) for c, v in cls.items()}
resc = {p: prim[p] - cm[p % 840] for p in prim}
tot = np.var(list(prim.values())); within = np.var([resc[p] for p in prim])
log(f"Z0958 mod-840 class means explain R2 = {1-within/tot:.3f} of var(log U/log²p) over primes ≤1e5")
for k in (1, 2, 5, 10):
    pr = [(p, p+840*k) for p in prim if (p+840*k) in prim]
    a = np.array([resc[p] for p, _ in pr]); b = np.array([resc[q] for _, q in pr])
    raw_a = np.array([prim[p] for p, _ in pr]); raw_b = np.array([prim[q] for _, q in pr])
    log(f"  lag 840·{k}: n={len(pr)} corr raw={np.corrcoef(raw_a,raw_b)[0,1]:.3f} after class-mean removal={np.corrcoef(a,b)[0,1]:.3f}")
# ---- Z0962 size-normalised
ps7 = [p for p in range(5, 7501) if isprime(p) and p % 4 == 1]
g = lambda n: U[n]/math.log(n)**2
x1 = [g(p) for p in ps7]; x2 = [g(4*p+1) for p in ps7]; x3 = [g((p+3)//4) for p in ps7]
log("Z0962 normalised (U/log²n): Spearman(p, 4p+1) = %.3f ; Spearman(p, (p+3)/4) = %.3f (n=%d)" % (
    spearmanr(x1, x2)[0], spearmanr(x1, x3)[0], len(ps7)))
# ---- Z0672 comparison: class mod 840 R^2 vs character-based R^2 (same primes)
P1 = [p for p in UP if p % 4 == 1 and p > 840 and isprime(p)]
ys = np.array([math.log(nrm(p)) for p in P1])
mu = {}
for c in set(p % 840 for p in P1):
    mu[c] = np.mean([math.log(nrm(p)) for p in P1 if p % 840 == c])
pred = np.array([mu[p % 840] for p in P1])
log("Z0672 comparison: R2 of class-mod-840 means (in-sample) = %.3f" % (1 - ((ys-pred)**2).sum()/((ys-ys.mean())**2).sum()))
open(D+"fp2_out.txt", "w").write("\n".join(out)+"\n")
