# z52d pass2 TO1 lint-fix numerics. Uses es_100000.tsv (full ES enumeration, primes = 1 mod 4 below 1e5).
# Sections: (A) sibling-count calibration for p+2q, p+x^2+y^2, p+squarefree, p+F_k, prime in (n^2,(n+1)^2), tetrahedral sums;
# (B) genus / class-field / Rédei-type splits of #ES(p); (C) Cauchy-Davenport sumset test for reciprocal sets mod q;
# (D) Artin-type triple covering by B2 classes (C<=10, d<=2000); (E) signed-cube representability by residue mod 9.
import sys, math, json
from collections import defaultdict
import numpy as np
from sympy import primerange, isprime
out = {}
rows = [l.split() for l in open('data/z52b/pass2/TO1/es_100000.tsv')]
P = np.array([int(r[0]) for r in rows]); CNT = np.array([int(r[1]) for r in rows])
# ---------- (A) sibling calibration (odd n) ----------
L = 100000
s = np.ones(L+1, bool); s[:2] = False
for i in range(2, int(L**0.5)+1):
    if s[i]: s[i*i::i] = False
sq = [False]*(L+1); 
sqfree = np.ones(L+1, bool); sqfree[0] = False
for q in range(2, int(L**0.5)+1):
    sqfree[q*q::q*q] = False
pw2 = [2**k for k in range(0, 18)]
F = [1, 1]
while F[-1] < L: F.append(F[-1]+F[-2])
ns = np.arange(9, L+1, 2)
def count_rep(terms_fn):
    c = np.zeros(len(ns), np.int64)
    for t in terms_fn():
        q = ns - t
        ok = q >= 2
        c[ok] += s[q[ok]]
    return c
# p + 2q (Lemoine-Levy): count pairs (p, q prime) with n = p + 2q
c_LL = np.zeros(len(ns), np.int64)
for qq in primerange(2, L//2):
    q = ns - 2*qq
    ok = q >= 2
    c_LL[ok] += s[q[ok]]
# p + x^2 + y^2 (Linnik): sum over squares-sums t
sq2 = sorted({a*a+b*b for a in range(0, 317) for b in range(a, 317) if a*a+b*b < L})
c_L2 = count_rep(lambda: sq2)
# p + squarefree (Estermann): n - p in squarefree numbers (n - p >= 1)
c_E = np.zeros(len(ns), np.int64)
for i, n in enumerate(ns):
    pass
# vectorised: for each prime p<n count squarefree n-p -> sum over primes p of sqfree[n-p]
primes_arr = np.nonzero(s)[0]
c_E = np.zeros(len(ns), np.int64)
for p_ in primes_arr:
    if p_ >= ns[-1]: break
    q = ns - p_
    ok = q >= 1
    c_E[ok] += sqfree[q[ok]]
# p + F_k
c_F = count_rep(lambda: [f for f in F if 2 <= f < L])
# prime in (n^2,(n+1)^2): count primes in the open interval
pi = np.cumsum(s)
lo = ns.astype(np.int64)**2; hi = (ns.astype(np.int64)+1)**2
c_pp = np.array([0]*0)
Lp = 20000  # limit for this one (interval endpoints up to 4e8 -> use separate small sieve)
Mmax = int(((Lp+1)**2)) 
sb = np.ones(Mmax+1, bool); sb[:2] = False
for i in range(2, int(Mmax**0.5)+1):
    if sb[i]: sb[i*i::i] = False
pc = np.cumsum(sb)
nn = np.arange(2, Lp+1)
c_pp = pc[(nn+1)**2 - 1] - pc[nn**2]
def summarize(name, c, nvals, log2=False):
    lg = c/np.log(nvals)**2
    return dict(name=name, min_count=int(c.min()), argmin_n=int(nvals[c.argmin()]), zero_count=int((c==0).sum()),
                n_tested=int(len(c)), min_over_log2=round(float(lg.min()),3), median_over_log2=round(float(np.median(lg)),3))
out['A_calib'] = [
  summarize('p+2q (odd n<=1e5)', c_LL, ns),
  summarize('p+x^2+y^2 (odd n<=1e5)', c_L2, ns),
  summarize('p+squarefree (odd n<=1e5)', c_E, ns),
  summarize('p+F_k (odd n<=1e5)', c_F, ns),
]
pp_ok = nn[c_pp>0]
out['A_prime_in_square_interval'] = dict(n_tested=int(len(c_pp)), zero_count=int((c_pp==0).sum()), min_count=int(c_pp.min()), argmin_n=int(nn[c_pp.argmin()]), min_over_n_over_logn=round(float(min(c_pp/(nn/np.log(nn)))),3))
# tetrahedral: n = sum of at most 5 tetrahedral numbers (Pollock), n <= 2000; count min over n of #representations with <=5 terms, and compare to n^{2/3}
T = [t*(t+1)*(t+2)//6 for t in range(1, 40) if t*(t+1)*(t+2)//6 < 2001]
M = 2000
reach = [set([0])]
for k in range(1, 6):
    prev = reach[-1]
    nxt = set(prev)
    for a in prev:
        for t in T:
            if a + t <= M: nxt.add(a+t)
    reach.append(nxt)
minrep = min(len(set(range(0, 1)) ) for _ in [0])
# minimal number of tetrahedral terms needed for each n
need = {}
for n in range(1, M+1):
    for k in range(1, 6):
        if n in reach[k]: need[n] = k; break
out['A_tetrahedral'] = dict(max_terms_needed=max(need.values()), n_max=M, all_covered_by_5=len(need)==M, n_needing_5=sum(1 for v in need.values() if v==5))
# ---------- (B) genus / class field / Rédei splits of #ES(p) ----------
pp_all = P[P>1000]; cc = CNT[P>1000]
def split(name, mask):
    m1 = mask[P>1000]
    return dict(name=name, n_in=int(m1.sum()), n_out=int((~m1).sum()),
                mean_log_in=round(float(np.log(cc[m1]).mean()),3), mean_log_out=round(float(np.log(cc[~m1]).mean()),3),
                min_in=int(cc[m1].min()) if m1.any() else None, min_out=int(cc[~m1].min()) if (~m1).any() else None)
def rep_xy(p, a, b):
    # p = x^2 + b y^2 solvable?  (cheap: loop y)
    y = 0
    while b*y*y < p:
        r = p - b*y*y; x = math.isqrt(r)
        if x*x == r: return True
        y += 1
    return False
pl = [int(p) for p in P[P>1000]]
B = []
B.append(split('p = x^2+2y^2', np.array([rep_xy(int(p),0,2) for p in P])))
B.append(split('p = x^2+27y^2 (2 cubic residue)', np.array([rep_xy(int(p),0,27) for p in P])))
B.append(split('p = x^2+32y^2', np.array([rep_xy(int(p),0,32) for p in P])))
B.append(split('p = x^2+64y^2 (2 quartic residue)', np.array([rep_xy(int(p),0,64) for p in P])))
def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
Lq = np.array([[legendre(3,int(p)) for p in P], [legendre(5,int(p)) for p in P], [legendre(7,int(p)) for p in P]])
pattern = [tuple(Lq[:,i]) for i in range(len(P))]
groups = defaultdict(list)
for i, p in enumerate(P):
    if p > 1000: groups[pattern[i]].append(CNT[i])
pat_stats = sorted([(k, len(v), round(float(np.mean(np.log(v))),3), int(min(v))) for k,v in groups.items() if len(v)>=20], key=lambda t:t[2])
out['B_splits'] = B
out['B_legendre_patterns_3_5_7'] = dict(n_patterns=len(pat_stats), lowest=pat_stats[:3], highest=pat_stats[-3:])
# class number h(-4p) for p = 1 mod 4 (reduced forms of disc -4p), vs log #ES
def h_neg4p(p):
    D = -4*p; h = 0
    a = 1
    while 3*a*a <= -D:
        for b in range(-a+1, a+1):
            if (b*b - D) % (4*a): continue
            c = (b*b - D)//(4*a)
            if c < a: continue
            if c == a and b < 0: continue
            if math.gcd(math.gcd(a,abs(b)),c) != 1: continue
            h += 1
        a += 1
    return h
hs = np.array([h_neg4p(int(p)) for p in P[P>1000]])
cc2 = CNT[P>1000]
rho = float(np.corrcoef(np.log(hs), np.log(cc2))[0,1])
out['B_class_number_h(-4p)'] = dict(corr_log_h_log_ES=round(rho,3), n=int(len(hs)), h_min=int(hs.min()), h_max=int(hs.max()))
# ---------- (C) Cauchy-Davenport test: reciprocal sets mod prime q ----------
def minH_full_sumset(q):
    # smallest H such that A_H + A_H = F_q where A_H = {1/x mod q : 1<=x<=H}
    inv = {x: pow(x, q-2, q) for x in range(1, q)}
    for H in range(2, q):
        A = sorted({inv[x] for x in range(1, H+1) if x % q})
        S = set()
        for a in A:
            for b in A: S.add((a+b) % q)
        if len(S) == q: return H, len(A)
    return None, None
cd = []
for q in primerange(5, 400):
    H, sz = minH_full_sumset(q)
    cd.append((q, H, sz, round(H/math.sqrt(q),3)))
out['C_sumset_min_H'] = dict(sample=cd[:8], max_ratio_H_over_sqrt_q=max(r[3] for r in cd), q_max=cd[-1][0], H_last=cd[-1][1])
# ---------- (D) Artin-type covering by three classes C (B2, d<=2000) ----------
def covered_mask(C, Pvals, D=2000):
    m = np.zeros(len(Pvals), bool)
    for d in range(4*C-1, D+1, 4*C):
        if d > 1: m |= ((4*C*Pvals+1) % d == 0)
    return m
Pv = P.astype(np.int64)
masks = {C: covered_mask(C, Pv) for C in range(1, 11)}
best = None
import itertools
for tri in itertools.combinations(range(1, 11), 3):
    frac = float(np.mean(masks[tri[0]] | masks[tri[1]] | masks[tri[2]]))
    if best is None or frac > best[1]: best = (tri, frac)
out['D_best_three_C'] = dict(best_triple=best[0], covered_fraction=round(best[1],4), first_C_1_2_3=round(float(np.mean(masks[1]|masks[2]|masks[3])),4))
# ---------- (E) signed cubes: representability by four signed cubes, residue classes mod 9 ----------
K = 60
cubes = [x**3 for x in range(-K, K+1)]
pairs = set()
for a in cubes:
    for b in cubes:
        pairs.add(a+b)
Nmax = 3000
rep4 = np.zeros(Nmax+1, bool)
pl_ = list(pairs)
for n in range(-0, Nmax+1):
    pass
pair_arr = np.array(sorted(pairs), dtype=np.int64)
for n in range(0, Nmax+1):
    t = n - pair_arr
    idx = np.searchsorted(pair_arr, t)
    idx[idx>=len(pair_arr)] = len(pair_arr)-1
    if (pair_arr[idx] == t).any(): rep4[n] = True
cls = defaultdict(lambda: [0,0])
for n in range(0, Nmax+1):
    r = n % 9
    cls[r][0] += 1
    if not rep4[n]: cls[r][1] += 1
out['E_signed_cubes_4_unrep_by_class_mod9_n<=3000_cubes<=60'] = {str(r): dict(tested=v[0], unrep=v[1]) for r,v in sorted(cls.items())}
out['E_first_unrep'] = [n for n in range(0, Nmax+1) if not rep4[n]][:25]
json.dump(out, open('data/z52b/pass2/TO1/fix_numerics.json','w'), indent=1, default=lambda o: o.item() if hasattr(o,'item') else str(o))
print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o,'item') else str(o))[:6000])
