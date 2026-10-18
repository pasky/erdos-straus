"""R279: Prop 3.1 construction check (p = -1 mod Q_k, p = 1 mod 4; hits (1,(p+1)/d) for d | Q_k with odd #factors)."""
from itertools import combinations
from math import prod, gcd
from review_r279_hilbert import isprime, pairs

for Ps in [[3, 7], [3, 7, 11], [3, 7, 11, 19]]:
    Q = prod(Ps); p = Q - 1
    while not (isprime(p) and p % 4 == 1):
        p += Q
    sols = []
    for r in range(1, len(Ps) + 1, 2):
        for c in combinations(Ps, r):
            d = prod(c); B = (p + 1) // d; C = (d + 1) // 4
            assert d % 4 == 3 and (p + 1) % d == 0 and B % 2 == 0 and 4 * B * C - 1 - B == p
            sols.append(B)
    R = sum((p + u + B) % (4 * u * B) == 0 for u, B in pairs(p))
    print(Ps, p, "constructed", len(set(sols)), "= 2^(k-1)", 2 ** (len(Ps) - 1), "R(p) =", R)
