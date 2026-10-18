"""R279 own check of Prop 4.1(a),(c): Type II hits 4abcd - a - b = cp (all c, d) and the c = 1 line m*uBC = p+u+B
for m = 8, 12, 16 (and m = 3 as the control where it must fail). BL class (-x/z, -y/z) via own Hilbert symbols."""
import sys
from fractions import Fraction as F
from math import gcd
from review_r279_hilbert import hilbert, legendre, jacobi, isprime

P = int(sys.argv[1]) if len(sys.argv) > 1 else 300
n2 = bad = 0; chis = 0
for p in range(3, P, 2):
    if not isprime(p):
        continue
    for a in range(1, p + 1):
        for b in range(1, p + 1):
            for c in range(1, a + b + 1):
                if (a + b) % c:
                    continue
                num = c * p + a + b
                if num % (4 * a * b * c):
                    continue
                d = num // (4 * a * b * c)
                x, y, z = a * b * d, p * b * c * d, p * a * c * d
                inv = hilbert(F(-x, z), F(-y, z), p)
                s = (a + b) // c
                ok = inv == -1 and (a * b % p == 0 or inv == legendre(-a * b, p))
                if gcd(s, 4 * a * b) == 1:
                    chis += 1
                    ok = ok and -jacobi(-4 * a * b, s) == -1
                n2 += 1; bad += not ok
print("TypeII hits", n2, "bad", bad, "target identities", chis)
for m in (8, 12, 16, 3):
    h = good = 0
    for p in range(5, 6000, 2):
        if not isprime(p) or p % m == 0:
            continue
        for u in range(1, p):
            if m * u - u - 1 > p:
                break
            for B in range(1, p):
                if m * u * B - u - B > p:
                    break
                if (p + u + B) % (m * u * B):
                    continue
                C = (p + u + B) // (m * u * B)
                x, y, z = u * B * C, p * B * C, p * u * C
                assert m * x * y * z == p * (x * y + x * z + y * z)
                h += 1; good += hilbert(F(-x, z), F(-y, z), p) == legendre(-u * B, p) == -1
    print(f"m={m}: hits {h}, with inv_p = (-uB/p) = -1: {good}")
