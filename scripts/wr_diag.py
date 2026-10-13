"""Diagonal Type II slice (e = k in Lemma 2.4): p = k^2 - 4 g b^2 with k = -1 mod 4gb,
i.e. p is a face value of the principal river of disc 16g with a congruence (O164 §7).
k ranges over (sqrt p, sqrt(4p/3)+1].  Usage: python wr_diag.py NMAX"""
import sys
from math import isqrt, gcd
from sympy import isprime, divisors
N = int(sys.argv[1])
def diag(n):
    sols = []
    for k in range(isqrt(n) + 1, isqrt(4 * n // 3) + 3):
        M = k * k - n
        if M <= 0 or M % 4: continue
        for b in divisors(M // 4):
            if (M // 4) % (b * b): continue
            g = M // (4 * b * b)
            if (k + 1) % (4 * g * b) == 0: sols.append((k, g, b))
    return sols
ps = [p for p in range(25, N + 1, 24) if isprime(p)]
miss = [p for p in ps if not diag(p)]
print("primes", len(ps), "without diagonal certificate", len(miss), miss[:10])
sq = [m * m for m in range(3, isqrt(N) + 1, 2)]
cop = [(m2, s) for m2 in sq for s in diag(m2) if gcd(isqrt(m2), s[0] * s[1] * s[2]) == 1]
print("odd squares", len(sq), "with coprime diagonal certificate", len(cop), cop[:5])
