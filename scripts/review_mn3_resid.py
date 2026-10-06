"""R82: share of U_1(q) (K=1) in MN3's residual region (c<q, d<fq, d<eq, a<fq), truncated at M<=MMAX.
Usage: review_mn3_resid.py m MMAX q1 q2 ..."""
import sys
from math import gcd
import sympy
m, MMAX = int(sys.argv[1]), int(sys.argv[2])
def divs_bounded(fac, bound):
    ds = [1]
    for p, k in fac.items():
        ds = [x * p ** i for x in ds for i in range(k + 1) if x * p ** i <= bound]
    return ds
for q in map(int, sys.argv[3:]):
    ell = sympy.primefactors(q)[0]
    L = {}
    for p in sympy.primerange(2, q):
        if p == ell or m % p == 0: continue
        k = 1
        while p ** (k + 1) < q: k += 1
        L[p] = k
    U = Ur = 0.0
    for M1 in divs_bounded(L, MMAX // q):
        M = q * M1
        if (M + 1) % m: continue
        A = (M + 1) // m
        for D in sympy.divisors(A * A):
            if D > A: break
            P = m * D + 1; e = gcd(M, P); N = M // e; f = P // e
            fa = sympy.factorint(D); a = 1; d = 1
            for p, k in fa.items(): a *= p ** (k // 2); d *= p ** (k % 2)
            b = A // (d * a); c = (a + b) // e
            w = 1.0 / int(sympy.totient(N)); U += w
            if c < q and d < f * q and d < e * q and a < f * q: Ur += w
    print(f"q={q} MMAX={MMAX}: residual share {Ur/U:.3f}")
