"""Are divisor-form certificates a class function?  Forms [m,2,m''] of disc -4tp (mm'' = tp+1);
certificate: m = m'' = -1 (mod t), 4 | m.  For each (p,t) group the factorisations by reduced class and
count classes containing both certificate and non-certificate forms (O164 §10).  Usage: wr_cube_class.py PMAX TMAX"""
import sys
from sympy import isprime, divisors
from collections import defaultdict
def reduce(f):
    a, b, c = f
    while True:
        if c < a: a, b, c = c, -b, a
        if not (-a < b <= a):
            k = (a - b) // (2 * a); c = a * k * k + b * k + c; b = b + 2 * a * k
            continue
        if a == c and b < 0: b = -b
        return (a, b, c)
P, T = map(int, sys.argv[1:3])
mixed = pure = tot = 0
for p in range(25, P + 1, 24):
    if not isprime(p): continue
    for t in range(3, T + 1, 4):
        N = t * p + 1; cls = defaultdict(set)
        for m in divisors(N):
            cert = m % 4 == 0 and (m + 1) % t == 0 and (N // m + 1) % t == 0
            cls[reduce((m, 2, N // m))].add(cert)
        multi = sum(1 for m in divisors(N)) - len(cls); globals()["mult"] = globals().get("mult", 0) + multi
        for v in cls.values():
            if True in v:
                tot += 1; mixed += (False in v); pure += (v == {True})
print("classes containing a certificate:", tot, "of which also contain non-certificates:", mixed, "pure:", pure, "factorisations sharing a class (total excess):", mult)
