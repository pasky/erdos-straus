#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 11 (Step 3): the certificate modulus
   L(T) = lcm{ M : M <= T, M = 3 (mod 4) }
for the class of one.  Part 1: log L(T)/T -> 2/3 (exact computation).  Part 2: for small T the least
prime p = 1 (mod lcm(24, L(T))) and its W(p) (must exceed T; Thm 17.3(c)), compared with the
notes-54.1 modulus lcm(1..T).
Usage: PYTHONPATH=scripts uv run python scripts/pointwise_size_omega.py"""
from math import log, gcd
from sympy import primerange, isprime
from pointwise_size_wtail import build_rows


def logL(T):
    """log lcm{M<=T, M=3 mod 4}: for odd prime l, exponent e = max{e: l^e <= T if l^e = 3 (4),
    l^e <= T/3 otherwise}; never 2."""
    s = 0.0
    for l in primerange(3, T + 1):
        e, best = 1, 0
        while l ** e <= T:
            if (l ** e) % 4 == 3 or 3 * l ** e <= T:
                best = e
            e += 1
        s += best * log(l)
    return s


def lcm_list(ms):
    L = 1
    for m in ms:
        L = L * m // gcd(L, m)
    return L


print("T, log L(T)/T, log lcm(1..T)/T")
for T in (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
    lt = logL(T)
    full = sum(log(l) * int(log(T) / log(l) + 1e-12) for l in primerange(2, T + 1))
    print(T, round(lt / T, 4), round(full / T, 4))

rows = build_rows(4096)
print("T, Q=lcm(24,L(T)), least prime p = 1 mod Q, W(p), W(p)/log p, T/log p")
for T in range(7, 64, 8):
    Q = lcm_list([24] + [M for M in range(3, T + 1, 4)])
    k = 1
    while not isprime(k * Q + 1):
        k += 1
    p = k * Q + 1
    W = next((M for M, _, t in rows if t[p % M]), None)
    assert W is None or W > T
    print(T, Q, p, W, None if W is None else round(W / log(p), 3), round(T / log(p), 3))
