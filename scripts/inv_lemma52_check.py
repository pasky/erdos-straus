"""O158 Lemma 5.2 check: for primes p = 1 (8), every E-element (4 | A = tu-1) of X(p) has (delta0/p) = -1,
delta0 = odd part of A/4.  usage: inv_lemma52_check.py P"""
import sys
from sympy import primerange, divisors, jacobi_symbol
P = int(sys.argv[1]); bad = tot = 0
for p in primerange(9, P):
    if p % 8 != 1: continue
    for t in range(1, p + 3):
        N = t * p + 1
        for A in divisors(N):
            if A % 4 or (A + 1) % t or (N // A + 1) % t: continue
            d = A // 4
            while d % 2 == 0: d //= 2
            tot += 1
            if jacobi_symbol(d, p) != -1: bad += 1
print(f"primes p=1 (8) < {P}: {tot} E-elements, violations of (delta0/p)=-1: {bad}")
