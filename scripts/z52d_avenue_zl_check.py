"""z52d avenue P01 / Z0251: positive ES over Z[1/l] for every non-square l (elementary, no GRH).

Claim (PROVED, elementary): let l >= 3 be a non-square integer and q ≡ 3 (mod 4) a prime with (l/q) = -1
(exists by Dirichlet + reciprocity). Then ord_q(l) = 2k with k odd, so q | 1 + l^k, and for every n ≡ 1 (mod 4)
with q-compatible x = (n+q)/4:
    4/n = 1/x + q l^k / ((1+l^k) n x) + q / ((1+l^k) n x),
all denominators positive elements of Z[1/l].  (n ≡ 3 (4) and even n are classical.)
This script verifies the identity exactly for primes l < 3000 and n ≡ 1 (4), n < 400.
Run: timeout 60 python3 scripts/z52d_avenue_zl_check.py
"""
from fractions import Fraction as F

def primes(a, b):
    for m in range(max(a, 2), b):
        if all(m % d for d in range(2, int(m ** .5) + 1)):
            yield m

def order(a, q):
    o, x = 1, a % q
    while x != 1:
        x = x * a % q; o += 1
    return o

for l in primes(3, 3000):
    q = next(q for q in primes(3, 10 ** 6) if q % 4 == 3 and q != l and pow(l % q, (q - 1) // 2, q) == q - 1)
    o = order(l, q); assert o % 2 == 0 and (o // 2) % 2 == 1
    k = o // 2; assert (1 + l ** k) % q == 0
    for n in range(5, 400, 4):
        if n % l == 0:
            continue
        x = F(n + q, 4); assert x.denominator == 1
        y = F(1 + l ** k, q * l ** k) * n * x
        z = F(1 + l ** k, q) * n * x
        assert F(4, n) == 1 / x + 1 / y + 1 / z
        d = y.denominator
        while d % l == 0:
            d //= l
        assert d == 1 and z.denominator == 1
print("ok: identity verified for all primes l < 3000, n ≡ 1 (mod 4) < 400")
