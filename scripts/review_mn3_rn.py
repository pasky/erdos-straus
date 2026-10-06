"""R82 from-scratch R(N) table for N <= X (m fixed), validated atoms only, plus the
unvalidated Lemma 2.1 upper-bound count.  Loops over (a,d) and divisors f of P = m a^2 d + 1,
then c with N = m a c d - f in [acd, X].
Usage: review_mn3_rn.py m X
"""
import sys
from math import gcd
import sympy

m, X = int(sys.argv[1]), int(sys.argv[2])
R = [0] * (X + 1); U = [0] * (X + 1)
sqf = [True] * (X + 1)
for p in range(2, int(X ** 0.5) + 2):
    for k in range(p * p, X + 1, p * p):
        sqf[k] = False
for a in range(1, X + 1):
    for d in range(1, X // a + 1):
        P = m * a * a * d + 1
        divs = sympy.divisors(P)
        for c in range(1, X // (a * d) + 1):
            base = m * a * c * d
            for f in divs:
                N = base - f
                if N < a * c * d: continue  # divisors ascending? not assumed
                if N > X: continue
                U[N] += 1
                if not sqf[d]: continue
                e = P // f
                b = c * e - a
                if b < a: continue
                if gcd(e * N, P) != e: continue
                R[N] += 1
print(f"m={m} X={X}")
print("sum R(N), N<=X:", sum(R), " sum U:", sum(U))
print("sum R(N)/N:", sum(R[N] / N for N in range(1, X + 1)))
print("max R:", max(R), "at", R.index(max(R)))
print("sum R^2 / X:", sum(r * r for r in R) / X)
primes = list(sympy.primerange(X // 2 + 1, X + 1))
print("mean R(l), l prime in (X/2,X]:", sum(R[l] for l in primes) / len(primes))
for N in (9973,):
    if N <= X: print("R(%d) =" % N, R[N])
