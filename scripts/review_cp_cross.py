"""R203 independent recheck of COMPOSITION_ES §5 EVIDENCE (pair products in Z[sqrt(-n)]).
(A, B) is a V_n point at some mu iff D(2 lam A B - 1) = nA^2 + B^2 for some lam >= 1 (mu = lam D).
usage: review_cp_cross.py X n1 n2 ...
"""
import sys
from math import gcd, isqrt

def divisors(m):
    ds = [1]; q = 2
    while q * q <= m:
        if m % q == 0:
            e = 0
            while m % q == 0: m //= q; e += 1
            ds = [d * q**k for d in ds for k in range(e + 1)]
        q += 1
    if m > 1: ds += [d * m for d in ds]
    return ds

def vn(n, A, B):
    A, B = abs(A), abs(B)
    if A == 0 or A % 2 or B % 2 == 0 or gcd(A, B) != 1 or gcd(B, n) != 1:
        return None
    M = n * A * A + B * B
    for D in divisors(M):
        g = M // D
        if (g + 1) % (2 * A * B) == 0:
            lam = (g + 1) // (2 * A * B); mu = lam * D
            assert n * A * A + B * B + D == 2 * mu * A * B
            return mu
    return False

X = int(sys.argv[1])
for n in map(int, sys.argv[2:]):
    P = [(A, B) for A in range(2, X + 1, 2) for B in range(1, X + 1, 2) if vn(n, A, B)]
    adm = hit = 0
    for i, (A1, B1) in enumerate(P):
        for (A2, B2) in P[i:]:
            for s in (1, -1):
                A, B = A1 * B2 + s * A2 * B1, B1 * B2 - s * n * A1 * A2
                r = vn(n, A, B)
                if r is not None:
                    adm += 1; hit += bool(r)
    print(f"n={n} X={X}: {len(P)} V_n points; pair products admissible {adm}, V_n points among them {hit}")
