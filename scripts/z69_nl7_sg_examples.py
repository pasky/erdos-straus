import sys
sys.path.insert(0,'scripts')
from sympy import isprime
from math import isqrt
Z7 = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425}
ex = []; cnt = 0; npr = 0
for s in range(1, 200000):
    if s % 126 not in (18, 108): continue
    n = 16*s**4 + 1
    eps = 1 if s % 126 == 18 else -1
    x, y, z = 4*(s*s - 2*eps*s + 2), (4*s*s + 8*eps*s + 9)//63, 63
    assert (4*s*s + 8*eps*s + 9) % 63 == 0 and x*y*z - x - z == n and x*y % 8 == 0 and min(x,y,z) > 0
    assert isqrt(n)**2 != n and n not in Z7
    cnt += 1
    if s % 5 == 0 and isprime(n):
        npr += 1
        assert n % 840 == 121
        if len(ex) < 5: ex.append((s, n))
print("s<2e5, s≡±18 (126):", cnt, "identities verified; primes with 5|s (n≡121 mod 840):", npr, "first:", ex)
