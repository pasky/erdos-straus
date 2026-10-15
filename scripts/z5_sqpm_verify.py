"""z5_sqpm_verify.py — independent exact check: for random non-square n ≡ 1 (mod 8), find a prime-modulus word
by direct search over u (factor n+u) and verify tuv − u − v = n, A = tu − 1 = ±prime, Jacobi(−A, n) = −1.
usage: z5_sqpm_verify.py N trials seed"""
import sys, math, random
from sympy import factorint, jacobi_symbol, isprime
N, T, seed = map(int, sys.argv[1:4]); random.seed(seed); ok = 0; worst = 0
for _ in range(T):
    while True:
        n = random.randrange(9, N, 8)
        if math.isqrt(n) ** 2 != n: break
    found = None
    for absu in range(1, 10 ** 6):
        for u in (absu, -absu):
            if n + u == 0: continue
            for l in factorint(abs(n + u)):
                for A in (l, -l):
                    if (A + 1) % u: continue
                    t = (A + 1) // u; v = (n + u) // A
                    if t * u * v != 0 and t * u * v - u - v == n and jacobi_symbol(-A, n) == -1 and isprime(abs(A)):
                        found = (t, u, v); break
                if found: break
            if found: break
        if found: break
    assert found, n
    ok += 1; worst = max(worst, abs(found[1]))
print(f"verified {ok} random n <= {N}; max |u| needed = {worst}")
