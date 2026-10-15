# R225 independent per-prime census (subsample) for NEAR_SQUARE §4/§5.
# Words (t,u,v) in N^3 with t*u*v - u - v = p, ordered (u,v); chi = ((t*u - 1)/p).
# Level t clean: every prime r | t p + 1 has (r/p) = +1 (incl. r = 2, as in the author's census);
# T1-type: t p + 1 = c^2 + t m^2, gcd(m, c) = 1, m >= 0.
import sys
from sympy import factorint, isprime, divisors
from math import isqrt, gcd
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def t1(p, t):
    for m in range(isqrt(p), -1, -1):
        x = t * p + 1 - t * m * m
        if x <= 0: continue
        c = isqrt(x)
        if c * c == x and gcd(m, c) == 1: return True
    return False
def census(p):
    N = Nm = Ncl = Nclm = NT = NTm = 0
    clc = {}; t1c = {}
    u = 1
    while (u - 2) * u <= p:
        for v in divisors(p + u):
            if v < u or (p + u + v) % (u * v): continue
            t = (p + u + v) // (u * v)
            assert t * u * v - u - v == p
            mult = 1 if u == v else 2
            ch = leg(t * u - 1, p)
            N += mult; Nm += mult * (ch == -1)
            if t not in clc: clc[t] = all(leg(r, p) == 1 for r in factorint(t * p + 1)); t1c[t] = t1(p, t)
            if clc[t]: Ncl += mult; Nclm += mult * (ch == -1)
            if t1c[t]: NT += mult; NTm += mult * (ch == -1)
        u += 1
    return N, Nm, NT, NTm, Ncl, Nclm
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for p in range(lo, hi):
    if p % 4 == 1 and isprime(p): print(p, *census(p))
