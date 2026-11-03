#!/usr/bin/env python3
"""z55 HCF: numerical checks of the small PROVED statements of Z55_HCF.md.

Lemma 2.1 (2-adic box, c in {7, 15}): for p == 1 (mod 8) prime, c is a coordinate (certificate exists on the U- or
T-line) iff the odd part of p+c or of cp+1 has a prime factor q with Jacobi (q/c) = -1.
Prop 2.2 (prime cofactor): for 4 | c, if p + c = s*q with q prime, q > s... (any factorization N = s*q with q prime
not dividing s): some d | p+c with d == -1 (mod c) exists iff s has a divisor == -1 or == -p (mod c).
"""
import sys
from sympy import factorint, primerange, jacobi_symbol, divisors

def has_cert(N, c):
    return any(d % c == c-1 for d in divisors(N))

def check_lemma21(X):
    bad = 0; n = 0
    for p in primerange(17, X):
        if p % 8 != 1: continue
        for c in (7, 15):
            n += 1
            lhs = has_cert(p+c, c) or has_cert(c*p+1, c)
            rhs = False
            for N in (p+c, c*p+1):
                while N % 2 == 0: N //= 2
                if any(jacobi_symbol(q, c) == -1 for q in factorint(N)):
                    rhs = True
            if lhs != rhs:
                bad += 1; print('L2.1 mismatch', p, c, lhs, rhs)
    return n, bad

def check_prop22(X):
    bad = 0; n = 0
    for p in primerange(17, X):
        if p % 8 != 1: continue
        for c in range(4, 65, 4):
            N = p + c
            f = factorint(N)
            for q, a in f.items():
                if a != 1: continue
                s = N // q
                n += 1
                lhs = has_cert(N, c)
                rhs = any(t % c == c-1 or t % c == (-p) % c for t in divisors(s))
                if lhs != rhs:
                    bad += 1; print('P2.2 mismatch', p, c, q, s, lhs, rhs)
    return n, bad

if __name__ == '__main__':
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    print('Lemma 2.1 (c=7,15), p<%d: (cases, mismatches) =' % X, check_lemma21(X))
    print('Prop 2.2 (4|c<=64, prime cofactor), p<%d: (cases, mismatches) =' % X, check_prop22(X//4))
