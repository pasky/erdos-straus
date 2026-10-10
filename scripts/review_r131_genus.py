"""R131 from scratch: spot-check §3.3 (q=20,28,40 means/corr) and §3.4 (sums over c of A_{c,1}, G_{c,1})."""
import numpy as np
from math import gcd
from sympy import divisors, isprime
def AG(n, c, d):
    q = 4*c*d; M = 4*c*c*d*n + 1; dv = divisors(M)
    sq = {(u*u) % q for u in range(1, q) if gcd(u, q) == 1}
    A = sum(1 for X in dv if X % q == q - 1); G = sum(1 for X in dv if (-X) % q in sq) / len(sq)
    return A, G
for p in (101, 1009, 2003):
    sA = sG = 0; out = []
    for c in range(1, 2001):
        A, G = AG(p, c, 1); sA += A; sG += G
        if c in (10, 100, 300, 1000, 2000): out.append((sA, round(sG, 1)))
    print(p, out, flush=True)
P = [p for p in range(5, 3000) if isprime(p)]
for (c, d) in ((1, 5), (1, 7), (5, 2)):
    v = np.array([AG(p, c, d) for p in P], float); A, G = v[:, 0], v[:, 1]
    print((c, d), 'meanA %.3f meanG %.3f corr %.2f mabs %.2f P(A=0) %.2f P(A=0|G>=1) %.2f' % (A.mean(), G.mean(),
          np.corrcoef(A, G)[0, 1], abs(A - G).mean(), (A == 0).mean(), (A[G >= 1] == 0).mean()))
