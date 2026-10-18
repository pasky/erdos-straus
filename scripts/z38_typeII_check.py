"""z38_typeII_check.py: Brauer character on the full Type II family and on m/n (Schinzel) c=1 lines.
(1) all Type II solutions 4abcd - a - b = c*p (a,b,c,d >= 1) at primes p < P with p not dividing ab: (-ab/p) = -1;
    and the target identity kron(-4ab, -(a+b)/c) = -1 whenever gcd((a+b)/c, 4ab) = 1;
(2) m/p c=1 line m*u*B*C = p + u + B (m = 8, 12, 16): hits have (-uB/p) = -1."""
import sys
from math import gcd
from sympy import primerange
from z38_bm_dictionary import kron
P = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
nI = nT = 0
for p in primerange(5, P):
    for a in range(1, p + 1):
        for b in range(1, p + 1):
            if 4 * a * b - a - b > p * (a + b):  # c >= 1, d >= 1 need 4abc - a - b <= cp, c <= a+b
                break
            for c in range(1, a + b + 1):
                if (a + b) % c: continue
                s = (a + b) // c
                if gcd(s, 4 * a * b) == 1:
                    assert kron(-4 * a * b, -s) == -1, (a, b, c); nI += 1
                num = c * p + a + b
                if num % (4 * a * b * c) == 0 and (a * b) % p:
                    assert kron(-a * b, p) == -1, (p, a, b, c); nT += 1
nm = 0
for m in (8, 12, 16):
    for p in primerange(5, 20 * P):
        for u in range(1, p):
            if m * u - u - 1 > p: break
            for B in range(1, (p + u) // (m * u - 1) + 1):
                if (p + u + B) % (m * u * B) == 0:
                    assert kron(-u * B, p) == -1, (m, p, u, B); nm += 1
print(f"Type II: {nT} solutions at primes < {P}, {nI} target identities; m/p c=1 lines (m=8,12,16, p<{20*P}): {nm} hits; all pass")
