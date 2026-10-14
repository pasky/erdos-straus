# R215 (hostile review of O215) — from-scratch check of SEVEN_SIBLING Thm 3.1.
# (1) symbolic identities with sympy; (2) for every n <= N in each class: integrality, positivity, exact equality;
# (3) consequence: every odd n <= N with 7∤n... and every odd prime p ≢ 1 (mod 105) gets a certificate.
import sys
from fractions import Fraction as F
import sympy as sp

n, d = sp.symbols('n d', positive=True)
def simp(expr): return sp.simplify(sp.together(expr))
# each: (name, residue test, d as function of n, denominators as functions of (n,d))
fams = [
 ("a6", lambda n: n % 7 == 6,                     lambda n: (n+1, 7),   lambda n, d: (d, 2*d*n, 2*d*n)),
 ("a5", lambda n: n % 7 == 5,                     lambda n: (n+2, 7),   lambda n, d: (d, d*n, d*n)),
 ("a3", lambda n: n % 7 == 3,                     lambda n: (2*n+1, 7), lambda n, d: (d*n, d, d)),
 ("a2", lambda n: n % 7 == 2 and n % 2,           lambda n: (3*n+1, 14), lambda n, d: (2*d*n, d, 2*d)),
 ("a4", lambda n: n % 7 == 4 and n % 2,           lambda n: (n+3, 14),  lambda n, d: (2*d, d*n, 2*d*n)),
 ("b",  lambda n: n % 3 == 2 and n % 2,           lambda n: (n+1, 6),   lambda n, d: (n, d, d*n)),
 ("c4", lambda n: n % 7 == 1 and n % 5 == 4,      lambda n: (n+6, 35),  lambda n, d: (5*d, d*n, 5*d*n)),
]
# I-c (a,d,e)=(5,2,e): Type I 7/n = 1/(abdn)+1/(acd)+1/(bcd), 70 b = n e + 1, c = (a+b)/e
def Ic(e):
    def den(n, _):
        b = (n*e+1)//70; c = (5+b)//e
        return (5*b*2*n, 5*c*2, b*c*2)
    return den
def Ic_ok(e, r):
    return lambda n: n % 70 == r
fams += [("c3", Ic_ok(13, 43), lambda n: (13*n+1, 70), Ic(13)),
         ("c2", Ic_ok(27, 57), lambda n: (27*n+1, 70), Ic(27))]

# symbolic (with d eliminated: n expressed through d)
sym = {"a6": 7*d-1, "a5": 7*d-2, "a3": (7*d-1)/2, "a2": (14*d-1)/3, "a4": 14*d-3, "b": 6*d-1, "c4": 35*d-6}
for nm, _, _, den in fams[:7]:
    N = sym[nm]; x, y, z = den(N, d)
    assert simp(1/x+1/y+1/z - 7/N) == 0, nm
# I-c symbolic: b free, n = (70b-1)/e, c = (5+b)/e
b, c = sp.symbols('b c', positive=True)
for e in (13, 27):
    # parametrize by c: b = c e - 5, n = (70 b - 1)/e
    B = c*e-5; N = (70*B-1)/e
    assert simp(1/(5*B*2*N) + 1/(5*c*2) + 1/(B*c*2) - 7/N) == 0
    assert sp.expand(70*B-1) .subs(c, 1) % e == 0 and (70*e) % e == 0  # (70(ce-5)-1)/e integral iff e | 351
    assert 351 % e == 0
print("symbolic identities OK; 7*25*2+1 =", 7*25*2+1, "= 13*27")

Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
cnt = {f[0]: 0 for f in fams}
for m in range(1, Nmax+1):
    for nm, test, dd, den in fams:
        if not test(m): continue
        num, q = dd(m)
        assert num % q == 0, (nm, m)
        D = den(m, num//q)
        if nm in ("c3", "c2"):
            e = 13 if nm == "c3" else 27
            bb = (m*e+1)//70
            assert (m*e+1) % 70 == 0 and (5+bb) % e == 0, (nm, m)
        assert min(D) > 0, (nm, m)
        assert sum(F(1, t) for t in D) == F(7, m), (nm, m, D)
        cnt[nm] += 1
print("per-class n<=%d all integral/positive/exact:" % Nmax, cnt)

# coverage: which odd n <= Nmax are hit, and which are not
cov = lambda m: any(t(m) for _, t, _, _ in fams)
miss = [m for m in range(1, Nmax+1, 2) if m % 7 and not cov(m)]
from math import gcd
bad = [m for m in miss if not (m % 105 == 1 or (m % 7 == 1 and (m % 3 == 0 or m % 5 == 0)) )]
# expectation from the statement: odd, 7∤n, uncovered  <=> n≡1 (7) and n≢2 (3) and n≡0 or 1 (5)
exp = [m for m in range(1, Nmax+1, 2) if m % 7 == 1 and m % 3 != 2 and m % 5 in (0, 1)]
print("uncovered odd 7∤n equals predicted set:", miss == exp, len(miss))
print("uncovered with gcd(n,105)=1 all ≡1 mod 105:", all(m % 105 == 1 for m in miss if gcd(m, 105) == 1))
ps = list(sp.primerange(3, Nmax+1))
print("odd primes p≢1 (105), p∉{3,5,7}, uncovered:", [p for p in ps if p % 105 != 1 and p not in (3, 5, 7) and not cov(p)])
