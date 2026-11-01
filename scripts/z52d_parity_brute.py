"""Independent brute-force check of scripts/z52d_parity_counts.c for small p (z52d PARITY lane).
X(p) by direct (t,u) loops; Type II by direct enumeration of 4/p = 1/x + 1/y + 1/z with p | y, p | z, p ∤ x
(unordered {y,z}: y <= z; the C counter's f_II is ordered = 2x this); h(-4p) by a naive reduced-form count.  Usage: python z52d_parity_brute.py OUT.txt PMAX"""
import sys
from math import isqrt

def legendre(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r

def words(p):
    W = []
    for t in range(1, p + 3):
        u = 1
        while t * u - 1 <= p + u and u <= p + 2:
            A = t * u - 1
            if A > 0 and (p + u) % A == 0:
                v = (p + u) // A
                W.append((t, u, v))
            u += 1
    return W

def type2_ordered(p):
    c = 0
    for x in range(p // 4 + 1, p // 2 + 1):
        if x % p == 0:
            continue
        m = 4 * x - p  # 1/y' + 1/z' = m/x, y = p y', z = p z'
        for y1 in range(1, 2 * x // m + 2):
            num = m * y1 - x
            if num <= 0:
                continue
            if (x * y1) % num == 0 and (x * y1) // num >= y1:
                c += 1
    return c

def hform(p):
    D = -4 * p
    h = 0
    for a in range(1, isqrt(-D // 3) + 2):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if a == c and b < 0:
                continue
            h += 1
    return h

def main():
    out, pmax = sys.argv[1], int(sys.argv[2])
    rows = {}
    for line in open(out):
        f = list(map(int, line.split()))
        if f[0] <= pmax:
            rows[f[0]] = f
    bad = 0
    for p, f in sorted(rows.items()):
        W = words(p)
        nX = len(W)
        nE = (nX - 1) // 2
        r4 = sum(1 for (t, u, v) in W if t % 4 == 0) // 2
        nEA = sum(1 for (t, u, v) in W if (t * u - 1) % 4 == 0)
        nB = sum(1 for (t, u, v) in W if u < v and legendre(u, p) * legendre(v, p) == -1)
        f2 = type2_ordered(p)
        h = hform(p)
        got = (nE, nB, r4, nEA, f2, h)
        exp = (f[1], f[2], f[3], f[4], f[5] // 2, f[6])
        if got != exp or nX % 2 == 0:
            bad += 1
            print("MISMATCH", p, got, exp)
    print(f"checked {len(rows)} primes <= {pmax}; mismatches {bad}")

main()
