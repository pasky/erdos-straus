# z52d pass2 TO1 lint-fix, part 2: residue-matched controls, T1/filter test, Bilharz-type density, composition and r4 checks.
import math, json, itertools, random
from collections import defaultdict
from fractions import Fraction
import numpy as np
from sympy import primerange
out = {}
rows = [l.split() for l in open('data/z52b/pass2/TO1/es_100000.tsv')]
P = np.array([int(r[0]) for r in rows]); CNT = np.array([int(r[1]) for r in rows])
m = P > 1000; P2 = P[m]; C2 = CNT[m]; LC = np.log(C2)
def rep_xy(p, b):
    y = 0
    while b*y*y < p:
        r = p - b*y*y; x = math.isqrt(r)
        if x*x == r: return True
        y += 1
    return False
def leg(a, p):
    a %= p
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
def ctrl(name, ind, cls_mod):
    # residue-matched comparison: within each class p mod cls_mod, mean(log #ES | ind) - mean(log #ES | not ind), averaged over classes with >=10 in each side
    diffs = []; w = []
    for r in set(P2 % cls_mod):
        mk = (P2 % cls_mod) == r
        a = LC[mk & ind]; b = LC[mk & ~ind]
        if len(a) >= 10 and len(b) >= 10:
            diffs.append(a.mean()-b.mean()); w.append(min(len(a),len(b)))
    if not diffs: return dict(name=name, note='no class with both sides >=10')
    d = np.array(diffs); w = np.array(w, float)
    return dict(name=name, cls_mod=cls_mod, classes_used=len(d), weighted_mean_diff=round(float((d*w).sum()/w.sum()),4),
                mean_diff=round(float(d.mean()),4), frac_classes_positive=round(float((d>0).mean()),3))
ind2 = np.array([rep_xy(int(p),2) for p in P2])
ind27 = np.array([rep_xy(int(p),27) for p in P2])
ind32 = np.array([rep_xy(int(p),32) for p in P2])
ind64 = np.array([rep_xy(int(p),64) for p in P2])
out['controls'] = [
  ctrl('x^2+2y^2 vs not, matched on p mod 24', ind2, 24),
  ctrl('x^2+27y^2 (2 cubic res.) vs not, matched on p mod 72', ind27, 72),
  ctrl('x^2+32y^2 (Barrucand-Cohn 8|h(-4p)) vs not, matched on p mod 96', ind32, 96),
  ctrl('x^2+64y^2 (2 quartic res.) vs not, matched on p mod 128', ind64, 128),
]
# Legendre-pattern (3,5,7) controlled by p mod 840 (Rédei-type symbols are not forced by p mod 840 alone)
L3 = np.array([leg(3,int(p)) for p in P2]); L5 = np.array([leg(5,int(p)) for p in P2]); L7 = np.array([leg(7,int(p)) for p in P2])
# residual of log count after removing p mod 24 class means, then compare by symbol pattern
res = LC.copy()
for r in set(P2 % 24):
    mk = (P2 % 24) == r; res[mk] = LC[mk] - LC[mk].mean()
pat = defaultdict(list)
for i in range(len(P2)): pat[(int(L3[i]),int(L5[i]),int(L7[i]))].append(res[i])
out['rédei_like_pattern_residuals_matched_mod24'] = sorted([(k, len(v), round(float(np.mean(v)),3)) for k,v in pat.items()], key=lambda t:t[2])
# primitive-root density phi(p-1)/(p-1) (calibration for Z0381): split at median, matched on p mod 24
from sympy import totient
pr = np.array([int(totient(int(p)-1))/(int(p)-1) for p in P2])
med = {}
hi = np.zeros(len(P2), bool)
for r in set(P2 % 24):
    mk = (P2 % 24) == r
    hi[mk] = pr[mk] > np.median(pr[mk])
diffs=[]
for r in set(P2 % 24):
    mk = (P2 % 24) == r
    if (mk&hi).sum()>=10 and (mk&~hi).sum()>=10: diffs.append(LC[mk&hi].mean()-LC[mk&~hi].mean())
out['primroot_density_split_matched_mod24'] = dict(classes=len(diffs), mean_diff=round(float(np.mean(diffs)),4), frac_pos=round(float(np.mean(np.array(diffs)>0)),3))
# class number h(-4p) vs ES count, partial out log p (both regressed on log p)
def h_neg4p(p):
    D = -4*p; h = 0; a = 1
    while 3*a*a <= -D:
        for b in range(-a+1, a+1):
            if (b*b - D) % (4*a): continue
            c = (b*b - D)//(4*a)
            if c < a or (c == a and b < 0): continue
            if math.gcd(math.gcd(a,abs(b)),c) != 1: continue
            h += 1
        a += 1
    return h
H = np.array([h_neg4p(int(p)) for p in P2])
X = np.vstack([np.ones(len(P2)), np.log(P2)]).T
def resid(y): 
    beta = np.linalg.lstsq(X, y, rcond=None)[0]; return y - X@beta
rH = resid(np.log(H)); rC = resid(LC)
out['h(-4p)_partial_corr_given_logp'] = round(float(np.corrcoef(rH, rC)[0,1]),4)
# ---------- T1 / filter check on uniform divisor mechanisms at odd squares n=m^2 ----------
def divisors(n):
    ds = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            ds.append(i)
            if i*i != n: ds.append(n//i)
        i += 1
    return ds
hits_I_coprime = 0; hits_I_any = 0; hits_II = 0; tested = 0
for mm in range(1, 100, 2):
    n = mm*mm
    for c in range(1, 13):
        for d in range(1, 13):
            M = n*n + 4*c*c*d
            for f in divisors(M):
                if (f + n) % (4*c*d) == 0:
                    hits_I_any += 1
                    if math.gcd(f, mm) == 1: hits_I_coprime += 1
            M2 = 4*c*c*d*n + 1   # Type II: f f' = 1 + 4c^2 d n  (the item form ff' - 4c^2 d n = 1)
            for f in divisors(M2):
                fp = M2//f
                if (f+1) % (4*c*d) == 0 and (fp+1) % (4*c*d) == 0: hits_II += 1
            tested += 1
out['T1_uniform_divisor_forms_at_odd_squares'] = dict(odd_m_le_99=tested, typeI_hits_any_f=hits_I_any, typeI_hits_with_gcd_f_m_1=hits_I_coprime, typeII_hits=hits_II)
# ---------- Bilharz-type: density of monic irreducibles P over F_3 of degree d with T a primitive root mod P ----------
def polymulmod(a, b, mod, p=3):
    # a,b lists low->high
    r = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j] = (r[i+j] + x*y) % p
    # reduce mod (monic) mod
    dm = len(mod)-1
    for k in range(len(r)-1, dm-1, -1):
        c = r[k]
        if c:
            for j in range(dm+1): r[k-dm+j] = (r[k-dm+j] - c*mod[j]) % p
    r = r[:dm] + [0]*(dm-len(r[:dm]))
    return r
def powmod(a, e, mod, p=3):
    res = [1] + [0]*(len(mod)-2); base = a[:]
    while e:
        if e & 1: res = polymulmod(res, base, mod, p)
        base = polymulmod(base, base, mod, p); e >>= 1
    return res
def is_irred(poly, p=3):
    d = len(poly)-1
    for k in range(1, d//2+1):
        for coeffs in itertools.product(range(p), repeat=k):
            g = list(coeffs)+[1]
            # polynomial division remainder
            r = poly[:]
            for i in range(len(r)-1, len(g)-2, -1):
                c = r[i]
                if c:
                    for j in range(len(g)): r[i-len(g)+1+j] = (r[i-len(g)+1+j] - c*g[j]) % p
            if all(x == 0 for x in r[:len(g)-1]): return False
    return True
def factor_int(n):
    f = []; x = 2
    while x*x <= n:
        while n % x == 0: f.append(x); n //= x
        x += 1
    if n > 1: f.append(n)
    return sorted(set(f))
bil = {}
for dd in range(2, 7):
    tot = 0; prim = 0
    for coeffs in itertools.product(range(3), repeat=dd):
        P_ = list(coeffs) + [1]
        if P_[0] == 0: continue
        if not is_irred(P_): continue
        tot += 1
        N = 3**dd - 1
        T = [0,1] + [0]*(dd-2) if dd >= 2 else [0]
        ok = True
        for r in factor_int(N):
            if powmod(T, N//r, P_) == [1] + [0]*(dd-1):
                ok = False; break
        if ok: prim += 1
    bil[dd] = (tot, prim, round(prim/tot,3))
out['bilharz_T_primitive_root_density_F3'] = bil
# ---------- composition test: naive product of certificates (Z0393, Z0464) ----------
random.seed(1)
def sols_small(p):
    res = []
    for x in range(p//4+1, 3*p//4+2):
        a = 4*x-p; b = p*x
        if a <= 0: continue
        g = math.gcd(a,b); a//=g; b//=g
        for d in range(1, b+1):
            if b % 1: break
            if (b*b) % d: continue
            if d > b: continue
            if (d+b) % a: continue
            e = b*b//d
            if (e+b) % a: continue
            y = (d+b)//a; z = (e+b)//a
            if y >= x: res.append((x,y,z))
        if len(res) > 40: break
    return res
pr_list = [p for p in primerange(5, 400) if p % 4 == 1]
ok_prod = 0; tried = 0; ok_prod_ES = 0
for _ in range(300):
    p, q = random.sample(pr_list, 2)
    Sp = sols_small(p); Sq = sols_small(q)
    if not Sp or not Sq: continue
    s1 = random.choice(Sp); s2 = random.choice(Sq)
    tried += 1
    tgt = Fraction(4, p*q)
    cand = sum(Fraction(1, a*b) for a, b in zip(s1, s2))
    if cand == tgt: ok_prod += 1
out['composition_naive_triple_product'] = dict(pairs_tried=tried, product_triple_hits_4_over_pq=ok_prod)
# ---------- quaternion slices: Lipschitz quaternions of norm m vs r4 (Z0314) ----------
def r4_brute(m):
    c = 0; R = math.isqrt(m)
    for a in range(-R, R+1):
        for b in range(-R, R+1):
            for cc in range(-R, R+1):
                rem = m - a*a - b*b - cc*cc
                if rem < 0: continue
                d = math.isqrt(rem)
                if d*d == rem: c += 1 if d == 0 else 2
    return c
def sigma(n): return sum(k for k in range(1, n+1) if n % k == 0)
chk = []
for mm in range(1, 61):
    odd = mm
    while odd % 2 == 0: odd //= 2
    formula = 8*sigma(mm) if mm % 2 == 1 else 24*sigma(odd)
    chk.append(r4_brute(mm) == formula)
out['r4_formula_checked_m<=60'] = dict(all_ok=all(chk), n=len(chk))
out['r4_at_primes_1mod4'] = {str(p): r4_brute(p) for p in [5, 13, 17, 29]}
json.dump(out, open('data/z52b/pass2/TO1/fix_numerics2.json','w'), indent=1, ensure_ascii=False, default=lambda o: o.item() if hasattr(o,'item') else str(o))
print(json.dumps(out, indent=1, ensure_ascii=False, default=lambda o: o.item() if hasattr(o,'item') else str(o)))
