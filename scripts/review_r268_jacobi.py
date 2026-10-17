"""R268: from-scratch checks of Lemma 3.1 (a)(b) and Lemma 4.1 of SYNTHESIS_SPARKS8."""
from math import gcd
from sympy import primerange, divisors, jacobi_symbol, isprime

# Lemma 3.1: p = 1 (4) prime < 2e4, prime windows q = 3 (4) < 80, K = (p+q)/4.
nc = bad_b = bad_a = nwin = forced_with = 0
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    for q in primerange(3, 80):
        if q % 4 != 3 or (p + q) % 4: continue
        K = (p + q) // 4; nwin += 1
        if jacobi_symbol(K, p) != jacobi_symbol(q, p): bad_a += 1
        D = divisors(K)
        for u in D:
            for v in D:
                if (K // u) % v == 0 and gcd(u, v) == 1 and (u + v) % q == 0:
                    nc += 1
                    if jacobi_symbol(u * v, p) != -1: bad_b += 1
print(f"Lemma 3.1: windows {nwin}, (a) exceptions {bad_a}; (b) cap-0 certificates (ordered (u,v)) {nc}, exceptions {bad_b}")

# Lemma 4.1: f | p^2 + 4c^2 d, f = -p (mod 4c|d|), gcd(p, cd) = 1.
pos = neg = bad = 0
sq_pos = {}; sq_neg = {}
for n in list(primerange(5, 3000)) + [m * m for m in range(3, 23, 2)]:
    if n % 4 != 1: continue
    prime = isprime(n)
    for c in range(1, 5):
        for d in list(range(-29, 0)) + list(range(1, 30)):
            if gcd(n, c * d) != 1: continue
            N = n * n + 4 * c * c * d
            if N <= 0: continue
            M = 4 * c * abs(d)
            for f in divisors(N):
                if (f + n) % M: continue
                if prime:
                    if d > 0:
                        pos += 1; bad += jacobi_symbol(d, n) != -1
                    else:
                        neg += 1; bad += jacobi_symbol(-d, n) != 1
                else:
                    (sq_pos if d > 0 else sq_neg)[n] = (sq_pos if d > 0 else sq_neg).get(n, 0) + 1
print(f"Lemma 4.1 (primes p=1(4)<3000, c<5, 0<|d|<30, gcd(p,cd)=1): {pos} positive, {neg} signed points, exceptions {bad}")
print("odd squares: positive points", sq_pos, " signed points", sq_neg)
