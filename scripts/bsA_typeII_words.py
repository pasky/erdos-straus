"""bsA_typeII_words: every Type II solution (ET: 4abd = n+e, a+b = ce) is the length-3 word K(a, 4cd, b) = c*n,
i.e. n*c/A = [[b, 4cd, a]] with A = 4cd*a - 1 (outer letters >= 1). Checks: exact ES identity, word identity, the sign
law (A/p) = -(-1/p) for primes, and T1 (no words at odd squares).  Usage: ... NMAX"""
import sys
from fractions import Fraction as F
from sympy import isprime, jacobi_symbol
from math import isqrt
def typeII(n):
    out = []
    d = 1
    while 4*d - 2 <= n:
        a = 1
        while 4*a*a*d - 2*a <= n + 0:  # a <= b, 4abd - a - b <= n
            b = a
            while 4*a*b*d - a - b <= n:
                e = 4*a*b*d - n
                if e > 0 and (a + b) % e == 0:
                    out.append((a, b, (a + b)//e, d))
                b += 1
            a += 1
        d += 1
    return out
N = int(sys.argv[1]); bad = 0; signs = {}; nsol = 0; sq = 0
for n in range(3, N, 2):
    sols = typeII(n)
    if isqrt(n)**2 == n: sq += len(sols); continue
    if not isprime(n): continue
    for a, b, c, d in sols:
        nsol += 1
        x, y, z = a*b*d, a*c*d*n, b*c*d*n
        t = 4*c*d
        ok = F(4, n) == F(1, x) + F(1, y) + F(1, z) and t*a*b - a - b == c*n
        for (u, v) in ((a, b), (b, a)):
            A = t*u - 1
            # HJ check when outer letters >= 2: (c n)/A = [[v, t, u]]
            if u >= 2 and v >= 2:
                ok &= F(c*n, A) == v - F(1, t - F(1, u))
            s = jacobi_symbol(A % n, n); key = (n % 4, s); signs[key] = signs.get(key, 0) + 1
        bad += not ok
print("primes<%d: Type II solutions (a<=b) %d, identity failures %d" % (N, nsol, bad))
print("sign table (p mod 4, (A/p)) -> count over both orientations:", signs)
print("Type II words at odd squares <", N, ":", sq)
