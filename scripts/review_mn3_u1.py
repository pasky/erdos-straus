"""R82 from-scratch U_1(q) (MN3 §1 definition, K = 1) and Lemma 1.1 brute-force check.

U_1(q) = sum over atoms (M,D), M = q*M_1, M_1 | L(q), M = -1 mod m, D | A^2, D <= A,
of 1/phi(N), N = M/gcd(M, mD+1).  Truncated at M <= MMAX.
L(q) = lcm{ q' prime power, q' < q, prime of q' not dividing m*ell }.
Usage: review_mn3_u1.py m MMAX q1 q2 ...
"""
import sys
from math import gcd, log
import sympy

m, MMAX = int(sys.argv[1]), int(sys.argv[2])
qs = [int(x) for x in sys.argv[3:]]

def phi(n):
    return int(sympy.totient(n))

def Lof(q):
    ell = sympy.primefactors(q)[0]
    L = {}
    for p in sympy.primerange(2, q):
        if p == ell or m % p == 0: continue
        k = 1
        while p ** (k + 1) < q: k += 1
        L[p] = k
    return L

def divs_bounded(fac, bound):
    ds = [1]
    for p, k in fac.items():
        ds = [x * p ** i for x in ds for i in range(k + 1) if x * p ** i <= bound]
    return ds

for q in qs:
    L = Lof(q)
    U = 0.0; UqN = 0.0; Usmall = 0.0; natoms = 0
    for M1 in divs_bounded(L, MMAX // q):
        M = q * M1
        if (M + 1) % m: continue
        A = (M + 1) // m
        fA = sympy.factorint(A)
        for D in sympy.divisors(A * A):
            if D > A: break
            g = gcd(M, m * D + 1); N = M // g
            w = 1.0 / phi(N)
            U += w; natoms += 1
            if N % q == 0: UqN += w
            if N < q * q: Usmall += w
    print(f"q={q}: atoms={natoms} q*U_1={q*U:.2f} (log q)^3={log(q)**3:.1f} "
          f"share q|N={UqN/U:.3f} share N<q^2={Usmall/U:.3f}")
