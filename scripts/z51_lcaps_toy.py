#!/usr/bin/env python3
"""Bounded exact checks of the z51 confinement amplifier; no external packages."""
import json
from itertools import combinations
from math import comb, isqrt, prod


def primes(n):
    a = bytearray(b'\1') * (n + 1)
    a[:2] = b'\0\0'
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            a[p*p:n+1:p] = b'\0' * ((n-p*p)//p+1)
    return [p for p in range(2, n+1) if a[p]]


def factor(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = 1
    return out


def main():
    rows = []
    for N, Y in [(100, 3), (1000, 7), (10000, 19), (100000, 31)]:
        S = [q for q in primes(Y) if q % 4 == 3]
        B = {1}
        for q in S:
            B |= {a*q for a in B if a*q <= N}
        independent = {n for n in range(1, N+1)
                       if all(q in S and b == 1 for q, b in factor(n).items())}
        assert B == independent
        E = [p for p in primes(N) if p % 8 == 1
             and all(pow(q, (p-1)//2, p) == 1 for q in S)]
        assert E, 'character-sum checks must not be vacuous'
        for p in E:
            assert all(pow(a, (p-1)//2, p) == 1 for a in B)
        r = 0
        while Y**(r+1) <= N:
            r += 1
        if r <= len(S):
            low = {prod(t) for t in combinations(S, r)}
            assert len(low) == comb(len(S), r) and low <= B
        rows.append(dict(N=N, Y=Y, primes=len(S), squarefree_products=len(B),
                         confined_primes=len(E), r=r))
    print(json.dumps(dict(status='PASS', rows=rows), indent=2))


if __name__ == '__main__':
    main()
