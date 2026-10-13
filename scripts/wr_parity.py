"""Parities of X-slice certificate counts (O164 §6, spark B).

X(n) = {(t,u,v) >= 1 : t u v - u - v = n};  E(n) = {x in X(n): 4 | t u - 1}  (ordered triples).
Enumerate u (any), v | n+u with u v | n+u+v.  (u <= v or not: we enumerate all u up to n+2 cheaply via
divisors of n+u only when u <= sqrt bound; the case u > v is handled by symmetry.)
Prints per class: distribution of |E| mod 2, |E| mod 4, |X| mod 2, and correlation with simple invariants.
Usage: python wr_parity.py NMAX [squares]
"""
import sys
from math import isqrt
from sympy import divisors, isprime, legendre_symbol


def counts(n):
    X = E = 0
    seen = set()
    umax = isqrt(n) + 3
    for u in range(1, umax + 1):
        for v in divisors(n + u):
            if v < u:
                continue
            s = n + u + v
            if s % (u * v):
                continue
            t = s // (u * v)
            for (a, b) in ((u, v), (v, u)) if u != v else ((u, v),):
                X += 1
                if (t * a - 1) % 4 == 0:
                    E += 1
    return X, E


def main():
    nmax = int(sys.argv[1])
    sq = len(sys.argv) > 2
    if sq:
        ns = [m * m for m in range(3, isqrt(nmax) + 1, 2)]
    else:
        ns = [p for p in range(25, nmax + 1, 24) if isprime(p)]
    from collections import Counter
    c = Counter()
    for n in ns:
        X, E = counts(n)
        key = (E % 2, X % 2) if sq else (E % 2, X % 2, legendre_symbol(2, n) if not sq else 0)
        c[key] += 1
    print("n count", len(ns), "squares" if sq else "primes 1 mod 24", dict(c))


if __name__ == "__main__":
    main()
