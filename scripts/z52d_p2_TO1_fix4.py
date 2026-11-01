# z52d pass2 TO1 lint-fix part 4: (a) primitive-root density control (Z0381) matched on p mod 840;
# (b) Thue/Minkowski vector check u^2+v^2=p, |u|,|v|<=sqrt p (Z0444); (c) least modulus d for the B2-uncovered primes (Z0364/Z0380).
import numpy as np, math
from sympy import totient, sqrt_mod
rows = [l.split() for l in open('data/z52b/pass2/TO1/es_100000.tsv')]
P = np.array([int(r[0]) for r in rows]); C = np.array([int(r[1]) for r in rows])
m = P > 1000; P2 = P[m]; LC = np.log(C[m])
pr = np.array([int(totient(int(p)-1))/(int(p)-1) for p in P2])
diffs = []; 
for r in set(P2 % 840):
    mk = (P2 % 840) == r
    if (mk).sum() < 20: continue
    hi = pr > np.median(pr[mk]) if False else None
    med = np.median(pr[mk])
    a = mk & (pr > med); b = mk & (pr <= med)
    if a.sum() >= 5 and b.sum() >= 5: diffs.append(LC[a].mean()-LC[b].mean())
d = np.array(diffs)
print('(a) primitive-root density control, matched on p mod 840:', dict(classes=len(d), mean_diff=round(float(d.mean()),4), frac_pos=round(float((d>0).mean()),3)))
# (b) Thue / Minkowski lattice vector: for p = 1 mod 4 find (u,v) with u = a v mod p, |u|,|v| <= sqrt p (Thue), check u^2+v^2 = p
ok = 0; tot = 0
for p in P[P > 4]:
    p = int(p); tot += 1
    a = int(sqrt_mod(-1, p))
    # lattice reduction of {(x,y): x = a y mod p}
    v1, v2 = (p, 0), (a, 1)
    # Gauss reduction
    def dot(u, w): return u[0]*w[0]+u[1]*w[1]
    u, w = v1, v2
    while True:
        if dot(w,w) < dot(u,u): u, w = w, u
        mu = round(dot(u,w)/dot(u,u))
        if mu == 0: break
        w = (w[0]-mu*u[0], w[1]-mu*u[1])
    if dot(u,u) == p or dot(w,w) == p: ok += 1
print('(b) primes p=1 mod 4 <1e5 where the reduced Thue lattice has a vector of norm p:', ok, 'of', tot)
# (c) least modulus d (B2 form) covering each B2-uncovered prime, C<=10, d<=2e6 with d = -1 mod 4C, d | 4Cp+1
def divisors_upto(n):
    ds = []
    for k in range(1, int(math.isqrt(n))+1):
        if n % k == 0: ds.append(k); ds.append(n//k) if n//k != k else None
    return sorted(set(ds))
uncov = []
Pvals = P.astype(np.int64)
masks = {}
for C in range(1, 11):
    mk = np.zeros(len(Pvals), bool)
    for dd in range(4*C-1, 2001, 4*C):
        if dd > 1: mk |= ((4*C*Pvals+1) % dd == 0)
    masks[C] = mk
cov = np.zeros(len(Pvals), bool)
for C in masks: cov |= masks[C]
un = P[~cov]
least = []
for p in un:
    p = int(p); best = None
    for C in range(1, 11):
        N = 4*C*p+1
        for dd in divisors_upto(N):
            if dd > 2000 and dd % (4*C) == 4*C-1:
                if best is None or dd < best[0]: best = (dd, C)
    least.append((p, best))
print('(c) uncovered primes (C<=10, d<=2000):', len(un), ' least d>2000 covering each (C<=10):', [ (p,b) for p,b in least[:12]], ' all covered by some d<=2e6:', all(b is not None for p,b in least))
ok_l=[(p,b) for p,b in least if b]
print('     covered-by-some-d>2000 (C<=10):', len(ok_l), 'of', len(least), ' example:', ok_l[:5])
