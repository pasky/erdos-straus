"""R80 from-scratch check of Computation 4.1 at a smaller bound: is x* (x*_11=2, x*_13=2, x*_q=1 else)
in any ET Prop 1.9 class with modulus M <= Mmax?  Class moduli (ET Prop 1.9 statement):
 I1 4ad; I2 4ac*f; I3 4cd*f; I4 4ab; II1 4ab; II2 f; II3 4ade.
Membership is a congruence condition mod M, tested exactly on X = x* mod M (CRT).
usage: review_mordell_point.py Mmax [p:u ...]   (default 11:2 13:2)"""
import sys
from math import gcd, isqrt
from sympy import divisors

Mmax = int(float(sys.argv[1]))
spec = [tuple(map(int, s.split(':'))) for s in sys.argv[2:]] or [(11, 2), (13, 2)]

def xstar(M):
    # CRT: X = u_q mod q^v_q(M) for special q, 1 mod the rest
    X, mod = 1, 1
    rest = M
    parts = []
    for q, u in spec:
        qq = 1
        while rest % q == 0: rest //= q; qq *= q
        parts.append((qq, u % qq if qq > 1 else 0))
    parts.append((rest, 1 % rest if rest > 1 else 0))
    for m, r in parts:
        if m == 1: continue
        # combine X mod mod with r mod m
        t = ((r - X) * pow(mod, -1, m)) % m
        X, mod = X + mod*t, mod*m
    return X % M

hits = []
def rep(*a):
    hits.append(a); print('HIT', *a, flush=True)

cnt = {}
# I1: modulus 4ad, f | 4a^2 d + 1, n = -f mod 4ad
for a in range(1, Mmax//4+1):
    for d in range(1, Mmax//(4*a)+1):
        M = 4*a*d; X = xstar(M)
        for f in divisors(4*a*a*d+1):
            cnt['I1'] = cnt.get('I1', 0)+1
            if (X + f) % M == 0: rep('I1', a, d, f, M)
print('I1 done', cnt, flush=True)
# I4, II1: modulus 4ab, e | a+b, (e,4ab)=1
for a in range(1, Mmax//4+1):
    for b in range(1, Mmax//(4*a)+1):
        M = 4*a*b; X = xstar(M)
        for e in divisors(a+b):
            if gcd(e, M) != 1: continue
            cnt['I4/II1'] = cnt.get('I4/II1', 0)+1
            if (X*e + 1) % M == 0: rep('I4', a, b, e, M)
            if (X + e) % M == 0: rep('II1', a, b, e, M)
print('I4/II1 done', cnt, flush=True)
# II2: modulus f, 4ad | f+1, n = -4a^2 d mod f
for f in range(3, Mmax+1, 4):
    X = xstar(f)
    for g in divisors((f+1)//4):
        a = g
        d = (f+1)//4 // g
        # all (a,d) with ad | (f+1)/4
        for dd in divisors((f+1)//4 // a):
            cnt['II2'] = cnt.get('II2', 0)+1
            if (X + 4*a*a*dd) % f == 0: rep('II2', a, dd, f, f)
print('II2 done', cnt, flush=True)
# II3: modulus 4ade, (4ad,e)=1, n = -4a^2 d - e mod 4ade
for a in range(1, Mmax//4+1):
    for d in range(1, Mmax//(4*a)+1):
        for e in range(1, Mmax//(4*a*d)+1):
            if gcd(4*a*d, e) != 1: continue
            M = 4*a*d*e; X = xstar(M); cnt['II3'] = cnt.get('II3', 0)+1
            if (X + 4*a*a*d + e) % M == 0: rep('II3', a, d, e, M)
print('II3 done', cnt, flush=True)
# I2: modulus 4ac*f, (4ac,f)=1: n=-f mod 4ac, a n + c = 0 mod f
# I3: modulus 4cd*f, (4cd,f)=1: n=-f mod 4cd, n^2+4c^2 d = 0 mod f
for u in range(1, Mmax//4+1):
    for v in range(1, Mmax//(4*u)+1):
        for f in range(1, Mmax//(4*u*v)+1):
            if gcd(4*u*v, f) != 1: continue
            M = 4*u*v*f; X = xstar(M)
            if (X + f) % (4*u*v): continue
            cnt['I2/I3'] = cnt.get('I2/I3', 0)+1
            if (u*X + v) % f == 0: rep('I2', u, v, f, M)          # (a,c)=(u,v)
            if (X*X + 4*u*u*v) % f == 0: rep('I3', u, v, f, M)    # (c,d)=(u,v)
print('I2/I3 done', cnt)
print('TOTAL HITS', len(hits))
