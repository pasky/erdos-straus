#!/usr/bin/env python3
"""Bounded exact checks of the z51 confinement amplifier; no external packages."""
import json
from itertools import combinations
from math import comb, isqrt, prod
from fractions import Fraction


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
    # EMV subset-moment diagonal: independent tuple coefficients and square-pair energy.
    moments = []
    for V in [[11, 19], [23, 31, 43]]:
        for j in range(1, 5):
            coeff = {1: 1}
            for _ in range(j):
                nxt = {}
                for n, c in coeff.items():
                    for q in V:
                        nxt[n*q] = nxt.get(n*q, 0)+c
                coeff = nxt
            energy = sum(Fraction(a*b, n*m) for n,a in coeff.items() for m,b in coeff.items()
                         if isqrt(n*m)**2 == n*m)
            diagonal_bound = j**j * sum(Fraction(1,q*q) for q in V)**j
            assert energy <= diagonal_bound
            for p in [101, 193, 409]:
                def chi(n):
                    t = pow(n, (p-1)//2, p)
                    return -1 if t == p-1 else t
                lhs = sum(Fraction(chi(q),q) for q in V)**j
                rhs = sum(Fraction(c*chi(n),n) for n,c in coeff.items())
                assert lhs == rhs
            moments.append(dict(V=V,j=j,energy=str(energy),upper=str(diagonal_bound)))
    print(json.dumps(dict(status='PASS', rows=rows, subset_moments=moments), indent=2))


if __name__ == '__main__':
    main()
