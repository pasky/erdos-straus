"""R95 from-scratch check of Lemma 1.1 (POINTWISE_MORDELL13B): for random family parameters P,
compare the set of u (mod M_T) with x(u) in the literal ET Prop 1.9 class against the table.
Literal classes built directly from the ET statement (no repo code)."""
import random, sys
from math import gcd
from sympy import divisors
T = (11, 13)
def tpart(m):
    t = 1
    for q in T:
        while m % q == 0: m //= q; t *= q
    return t
def crt(r1, m1, r2, m2):  # coprime moduli
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2), m1 * m2
BIAS = True
def rnd():
    x = random.choice([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 21, 25] if not BIAS else [1, 1, 1, 2, 3, 5])
    return x * random.choice([1, 1, 11, 13, 121, 169, 143])
def lit(R, M):  # set of u mod M_T s.t. some r in R: r = 1 mod M', r=u mod M_T
    MT = tpart(M); Mp = M // MT
    return {r % MT for r in R if r % Mp == 1 % Mp}, MT
def gen(fam):
    for _ in range(200000):
        P = gen0(fam)
        if not BIAS or tfree_ok(fam, P): return P
    return P
def tfree_ok(fam, P):
    x, y, f = P
    if fam == 'II2': return True
    X = tpart(x*y); Xp = x*y//X
    return (f+1) % (4*Xp) == 0
def gen0(fam):
    while True:
        if fam == 'I1':
            a, d = rnd(), rnd(); f = random.choice(divisors(4*a*a*d+1)); return (a, d, f)
        if fam in ('I2', 'I3', 'II3'):
            x, y = rnd(), rnd(); base = x+y if fam == 'I2' else 4*x*x*y+1
            fp = random.choice(divisors(base)) if BIAS else random.randrange(1, 4000)
            f = fp * random.choice([1, 1, 11, 13, 121, 169, 143])
            if gcd(4*x*y, f) == 1: return (x, y, f)
        if fam in ('I4', 'II1'):
            a, b = rnd(), rnd(); e = random.choice(divisors(a+b))
            if gcd(e, 4*a*b) == 1: return (a, b, e)
        if fam == 'II2':
            a, d = rnd(), rnd(); f = 4*a*d*random.randrange(1, 30) - 1
            if random.random() < .5:
                # bias towards f with T-part
                for k in range(1, 3000):
                    ff = 4*a*d*k - 1
                    if tpart(ff) > 1: f = ff; break
            return (a, d, f)
def classres(fam, P):
    if fam == 'I1':
        a, d, f = P; M = 4*a*d; return [(-f) % M], M
    if fam == 'I2':
        a, c, f = P; r, M = crt((-f) % (4*a*c), 4*a*c, (-c*pow(a, -1, f)) % f if f > 1 else 0, f); return [r], M
    if fam == 'I3':
        c, d, f = P; roots = [n for n in range(f) if (n*n + 4*c*c*d) % f == 0]
        out = [crt((-f) % (4*c*d), 4*c*d, s, f)[0] for s in roots]; return out, 4*c*d*f
    if fam == 'I4':
        a, b, e = P; M = 4*a*b; return [(-pow(e, -1, M)) % M], M
    if fam == 'II1':
        a, b, e = P; M = 4*a*b; return [(-e) % M], M
    if fam == 'II2':
        a, d, f = P; return [(-4*a*a*d) % f], f
    if fam == 'II3':
        a, d, e = P; M = 4*a*d*e; return [(-4*a*a*d - e) % M], M
def table(fam, P, u):
    if fam == 'I1':
        a, d, f = P; X = tpart(a*d); Xp = a*d//X
        return (f+1) % (4*Xp) == 0 and (f+u) % X == 0
    if fam == 'I2':
        a, c, f = P; X = tpart(a*c); Xp = a*c//X; fT = tpart(f); fp = f//fT
        return (f+1) % (4*Xp) == 0 and (f+u) % X == 0 and (a+c) % fp == 0 and (c+u*a) % fT == 0
    if fam == 'I3':
        c, d, f = P; X = tpart(c*d); Xp = c*d//X; fT = tpart(f); fp = f//fT
        return (f+1) % (4*Xp) == 0 and (f+u) % X == 0 and (4*c*c*d+1) % fp == 0 and (u*u+4*c*c*d) % fT == 0
    if fam == 'I4':
        a, b, e = P; X = tpart(a*b); Xp = a*b//X
        return (e+1) % (4*Xp) == 0 and (u*e+1) % X == 0
    if fam == 'II1':
        a, b, e = P; X = tpart(a*b); Xp = a*b//X
        return (e+1) % (4*Xp) == 0 and (e+u) % X == 0
    if fam == 'II2':
        a, d, f = P; fT = tpart(f); fp = f//fT
        return (4*a*a*d+1) % fp == 0 and (u+4*a*a*d) % fT == 0
    if fam == 'II3':
        a, d, e = P; X = tpart(a*d); Xp = a*d//X; eT = tpart(e); ep = e//eT
        return (e+1) % (4*Xp) == 0 and (e+u) % X == 0 and (4*a*a*d+1) % ep == 0 and (u+4*a*a*d) % eT == 0
BIAS = len(sys.argv) > 3 and sys.argv[3] == 'bias'
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
bad = 0; hits = {}; nontriv = {}
for fam in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
    hits[fam] = 0; nontriv[fam] = 0
    for _ in range(N):
        P = gen(fam); R, M = classres(fam, P)
        L, MT = lit(R, M)
        Tb = {u for u in range(MT) if table(fam, P, u)}
        if MT > 1: nontriv[fam] += 1
        hits[fam] += len(L)
        if L != Tb:
            bad += 1; print('MISMATCH', fam, P, sorted(L)[:5], sorted(Tb)[:5])
print('mismatches', bad, 'u-hits per family', hits, 'cases with M_T>1', nontriv)

# ---- Lemma 1.2 parity check: for every hit u in L with (u/q)=-1 for every q | M_T, check claimed parity
def v(m):
    s = 0
    for q in T:
        while m % q == 0: m //= q; s += 1
    return s
def leg(u, q): return pow(u % q, (q-1)//2, q)
def parity(fam, P):
    x, y, z = P
    return {'II1': v(x*y), 'I4': v(x*y), 'II2': v(z), 'I2': v(x*y)+v(z), 'I1': v(y), 'I3': v(y), 'II3': v(y)+v(z)}[fam] % 2 == 1
random.seed(99); pbad = 0; ptested = {}; pfail_res = 0
for fam in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
    ptested[fam] = 0
    for _ in range(N):
        P = gen(fam); R, M = classres(fam, P); L, MT = lit(R, M)
        qs = [q for q in T if MT % q == 0]
        for u in L:
            if gcd(u, 143) > 1: continue
            if all(leg(u, q) == q-1 for q in qs):
                ptested[fam] += 1
                if not parity(fam, P): pbad += 1; print('PARITY FAIL', fam, P, u, MT)
            elif all(leg(u, q) == 1 for q in qs) and qs and not parity(fam, P) is False:
                pass
print('Lemma 1.2: parity failures', pbad, 'tested (nonresidue-u hits) per family', ptested)
