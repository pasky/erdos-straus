#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md §5 EVIDENCE: first primes p = 1 + kQ (T=1000,
y=sqrt T) passing the prime-local sieve, and their actual W(p).  Independent code.
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_primes.py [T=1000] [count=5]
"""
import sys
from math import gcd, log
from sympy import factorint, primerange, isprime


def R_set(M):
    A = (M + 1) // 4
    ds = [1]
    for p, e in factorint(A).items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return {(-4 * D) % M for D in ds}


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    y = T ** 0.5
    Q = 24
    for l in primerange(2, int(y) + 1):
        e = 1
        while l ** (e + 1) <= T:
            e += 1
        Q = Q * l ** e // gcd(Q, l ** e)
    Rs = {}

    def W(n, cap=20000):
        for M in range(3, cap, 4):
            if M not in Rs:
                Rs[M] = R_set(M)
            if n % M in Rs[M]:
                return M
        return None

    print(f"T={T} y={y:.2f} log Q={log(Q):.1f}")
    found = 0
    k = 0
    while found < cnt:
        k += 1
        p = 1 + k * Q
        w = W(p, T + 1)
        if w is not None:
            continue
        if not isprime(p):
            continue
        found += 1
        wp = W(p)
        print(f"k={k} log p={log(p):.2f} p%840={p % 840} W(p)={wp} W/log p={wp / log(p):.1f}")


if __name__ == "__main__":
    main()
