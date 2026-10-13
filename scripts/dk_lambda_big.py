"""O169 Cor 4.6 at scale: lambda(p) <= 3 for all primes p = 1 (8) <= N
(interior five-slice hit, or boundary: (p+1)/2 has a prime factor = 3 mod 4). Also T1 control on odd squares.
Usage: uv run python scripts/dk_lambda_big.py N
"""
import sys
from math import isqrt
N = int(sys.argv[1])
hit = bytearray(N + 1)
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1; v = 2
        while (n := v * A - u) <= N:
            if A % 4 == 0 or (t * v - 1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0:
                hit[n] = 1
            v += 1
        u += 1
    t += 1
sieve = bytearray([1]) * (N + 2); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N + 1) + 1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
def has3mod4(m):
    q = 3
    while q * q <= m:
        if m % q == 0:
            if q % 4 == 3: return True
            while m % q == 0: m //= q
        q += 2
    return m > 1 and m % 4 == 3
np = interior = boundary_only = fail = 0
for p in range(17, N + 1, 8):
    if not sieve[p]: continue
    np += 1
    if hit[p]: interior += 1
    elif has3mod4((p + 1) // 2): boundary_only += 1
    else: fail += 1; print("lambda>3:", p)
sqbad = sum(1 for m in range(3, isqrt(N) + 1, 2) if m * m % 4 == 1 and (hit[m*m] or has3mod4((m*m+1)//2)))
print(f"N={N}: primes p=1(8): {np}, interior hit {interior}, boundary only {boundary_only}, lambda>3: {fail}; odd squares with a hit: {sqbad}")
