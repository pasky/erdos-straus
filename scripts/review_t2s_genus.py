"""R128: Lemma 6.1 check (p/f) = (p/f') = -1 for all Type II f, f' with p < P (from-scratch enumeration),
and Cor 6.2: no Type II solution for odd squares (cross-check with review_t2s_brute output)."""
import sys, math
from sympy import primerange, jacobi_symbol
P = int(sys.argv[1]); n = bad = 0
for p in primerange(5, P):
    for a in range(1, p):
        if 3 * a - 1 > p: break
        for b in range(1, p):
            if 4 * a * b - a - b > p: break
            s = a + b
            for c in range(1, s + 1):
                if s % c or math.gcd(a, c) != 1: continue
                num = s + p * c
                if num % (4 * a * b * c): continue
                d = num // (4 * a * b * c)
                for f in (4 * a * c * d - 1, 4 * b * c * d - 1):
                    n += 1; bad += jacobi_symbol(p, f) != -1
print(f"primes < {P}: {n} moduli f,f'; violations of (p/f)=-1: {bad}")
