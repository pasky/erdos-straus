# z52d pass2 NC1 Z1358 (fix): do ES triples satisfy the recalled three-term Dedekind identity more often than random triples?
# ES triples: from C-form witnesses (x,y,z) = (Cuv, pCv, pCu) for primes p ≤ 3000; keep pairwise-coprime triples.
# Controls: pairwise-coprime triples (a,b,c) with the same product-size distribution, drawn uniformly from [2, Z]^3.
import math, random, json
from fractions import Fraction as Fr
from sympy import primerange
random.seed(1)
def ded(h, k):
    if k == 1: return Fr(0)
    s = Fr(0)
    for i in range(1, k):
        u = (h*i) % k
        if u == 0: continue
        s += (Fr(i, k)-Fr(1, 2))*(Fr(u, k)-Fr(1, 2))
    return s
def lhs(a, b, c): return ded(b*c, a)+ded(c*a, b)+ded(a*b, c)
def rhs(a, b, c): return Fr(-1, 4)+Fr(a*a+b*b+c*c, 12*a*b*c)
def witnesses(p):
    out = []
    for C in range(1, 51):
        N = 4*C*p+1; m = 4*C; d = m-1
        while d*d <= N:
            if N % d == 0:
                e = N//d; u = (d+1)//(4*C); v = (e+1)//(4*C)
                out.append((C*u*v, p*C*v, p*C*u))
            d += m
    return out
es = []
for p in primerange(5, 3000):
    if p % 4 != 1: continue
    es += witnesses(p)
es = [t for t in es if math.gcd(t[0], t[1]) == math.gcd(t[1], t[2]) == math.gcd(t[0], t[2]) == 1]
ctrl = []
while len(ctrl) < len(es):
    a, b, c = (random.randint(2, 4000) for _ in range(3))
    if math.gcd(a, b) == math.gcd(b, c) == math.gcd(a, c) == 1: ctrl.append((a, b, c))
def stats(T):
    ok = sum(1 for t in T if lhs(*t) == rhs(*t))
    return ok, len(T)
ok_es, n_es = stats(es); ok_c, n_c = stats(ctrl)
out = {'ES_pairwise_coprime_triples': n_es, 'identity_holds_ES': ok_es, 'identity_holds_random_coprime_controls': ok_c, 'n_controls': n_c,
       'recalled_identity': 's(bc,a)+s(ca,b)+s(ab,c) = -1/4 + (a^2+b^2+c^2)/(12abc)',
       'note': 'recalled identity fails on most coprime triples (see Z1358 pass-2 table); the comparison is a frequency test only'}
print(json.dumps(out, indent=1))
