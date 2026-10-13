"""Does any simple invariant determine |E(p)| mod 2 (or mod 4)? (O164 §6)"""
import sys
from math import isqrt
from sympy import isprime, sqrt_mod
from wr_parity import counts
from collections import Counter, defaultdict

def h4(n):  # class number of disc -4n (primitive reduced forms)
    from math import gcd
    D = 4 * n; h = 0
    for a in range(1, isqrt(D // 3) + 2):
        for B in range(-a + 1, a + 1):
            if (B * B + D) % (4 * a): continue
            c = (B * B + D) // (4 * a)
            if c < a or (c == a and B < 0): continue
            if gcd(gcd(a, B), c) == 1: h += 1
    return h

def two_sq(p):
    for x in range(1, isqrt(p) + 1, 2):
        y2 = p - x * x; y = isqrt(y2)
        if y * y == y2: return x, y

N = int(sys.argv[1])
rows = []
for p in range(25, N + 1, 24):
    if not isprime(p): continue
    X, E = counts(p); x, y = two_sq(p)
    rows.append(dict(E2=E % 2, E4=E % 4, p16=p % 16, p5=p % 5, p7=p % 7, h8=h4(p) % 8, h16=h4(p) % 16,
                     x8=x % 8, y8=y % 16, q2=pow(2, (p - 1) // 4, p) == 1))
for key in ["p16", "p5", "p7", "h8", "h16", "x8", "y8", "q2"]:
    tab = defaultdict(Counter)
    for r in rows: tab[r[key]][r["E2"]] += 1
    print(key, {k: dict(v) for k, v in sorted(tab.items())})
