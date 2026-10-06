"""R82: all-ones path, level-0 step at prime ell (MN3 Lemma 5.1).
Y(ell) = #{(M,D): M = ell*M1, M1 | L(ell), M = -1 mod m, D | A^2, M1 | mD+1};
forbidden fraction = #{distinct (-mD mod ell)}/(ell-1). Also checks N = ell for all of them and
Y(ell) <= 2 R_ell(ell). Usage: review_mn3_first.py m ell1 ell2 ...
"""
import sys
from math import gcd, log
import sympy

m = int(sys.argv[1])
for ell in map(int, sys.argv[2:]):
    L = 1
    for p in sympy.primerange(2, ell):
        if m % p == 0: continue
        x = p
        while x * p < ell: x *= p
        L = L * x // gcd(L, x)
    Y = 0; Rl = 0; cls = set(); bad = 0
    for M1 in sympy.divisors(L):
        M = ell * M1
        if (M + 1) % m: continue
        A = (M + 1) // m
        for D in sympy.divisors(A * A):
            P = m * D + 1
            N = M // gcd(M, P)
            if N == ell and D <= A: Rl += 1
            if P % M1 == 0:
                Y += 1; cls.add((-m * D) % ell)
                if N != ell: bad += 1
    print(f"ell={ell}: Y={Y} 2R_ell(ell)={2*Rl} forbidden frac={len(cls)/(ell-1):.3f} "
          f"(log ell)^3={log(ell)**3:.1f} N!=ell cases={bad}")
