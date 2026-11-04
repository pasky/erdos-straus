# Near-square primes p = m^2 + k (k in K, p ≡ 1 mod 4) with p in [lo, hi]; prints "p k".
import sys
from sympy import isprime
from math import isqrt
lo, hi = int(sys.argv[1]), int(sys.argv[2]); K = [1, 5, 9, 13, 21, 45, 105]
for m in range(isqrt(lo), isqrt(hi) + 1):
    for k in K:
        p = m * m + k
        if lo <= p <= hi and p % 4 == 1 and isprime(p): print(p, k)
