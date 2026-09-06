"""Finite signed Egyptian-fraction refactor graph; experimental, not an ES proof.

uv run python scripts/pointwise_refactor.py 297049
Vertices are sorted nonzero integer triples summing reciprocally to 4/p.
Edges join triples sharing a denominator. The search is capped and streamed:
only the SPF array, actual solution triples, and denominator buckets are stored.
"""
from __future__ import annotations

import argparse
from array import array
from collections import defaultdict, deque
from fractions import Fraction
from math import isqrt

from sympy import isprime


def signed_solutions(p: int) -> list[tuple[int, int, int]]:
    if not 5 <= p <= 300000 or p % 4 != 1 or not isprime(p):
        raise ValueError("p must be a prime congruent to 1 mod 4, with 5 <= p <= 300000")
    bound = 3 * p // 4
    spf = array("I", [0]) * (bound + 1)
    for prime in range(2, bound + 1):
        if spf[prime]:
            continue
        spf[prime] = prime
        if prime <= isqrt(bound):
            for multiple in range(prime * prime, bound + 1, prime):
                if not spf[multiple]:
                    spf[multiple] = prime

    def square_divisors(n: int):
        ds = [1]
        while n > 1:
            prime, exponent = spf[n], 0
            while n % prime == 0:
                n //= prime
                exponent += 1
            old = ds[:]
            power = 1
            for _ in range(2 * exponent):
                power *= prime
                ds.extend(d * power for d in old)
        return ds

    out = set()
    # Every signed solution has a positive denominator <= 3p/4 < p.
    # Hence gcd(4x-p, px)=1 and every divisor of (px)^2 is p^j*d, d|x^2.
    for x in range(1, bound + 1):
        q, s = 4 * x - p, p * x
        for d in square_divisors(x):
            for power in (1, p, p * p):
                absolute_d = d * power
                if absolute_d > s:  # The cofactor enumerates the swapped pair.
                    continue
                for signed_d in (absolute_d, -absolute_d):
                    if (signed_d + s) % q:
                        continue
                    y = (signed_d + s) // q
                    cofactor = s * s // signed_d
                    assert (cofactor + s) % q == 0
                    z = (cofactor + s) // q
                    if not y or not z:
                        continue
                    assert 4 * x * y * z == p * (x * y + x * z + y * z)
                    out.add(tuple(sorted((x, y, z))))
    return sorted(out)


def seed(p: int) -> tuple[int, int, int]:
    t = (p - 1) // 4
    return -2 * p * t, -2 * p * t, t


def denominator_buckets(vertices):
    buckets = defaultdict(list)
    for i, vertex in enumerate(vertices):
        for x in set(vertex):
            buckets[x].append(i)
    return buckets


def seed_path(p: int, vertices):
    buckets = denominator_buckets(vertices)
    root = vertices.index(seed(p))
    previous, todo, seen_denominators = {root: None}, deque([root]), set()
    while todo:
        i = todo.popleft()
        if vertices[i][0] > 0:
            path = []
            while i is not None:
                path.append(vertices[i])
                i = previous[i]
            return path[::-1]
        for x in vertices[i]:
            if x in seen_denominators:
                continue
            seen_denominators.add(x)
            for j in buckets[x]:
                if j not in previous:
                    previous[j] = i
                    todo.append(j)
    return None


def components(vertices):
    buckets = denominator_buckets(vertices)
    unseen = set(range(len(vertices)))
    while unseen:
        todo, component, expanded = [unseen.pop()], [], set()
        while todo:
            i = todo.pop()
            component.append(vertices[i])
            for x in vertices[i]:
                if x in expanded:
                    continue
                expanded.add(x)
                for j in buckets[x]:
                    if j in unseen:
                        unseen.remove(j)
                        todo.append(j)
        yield component


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p", type=int)
    args = parser.parse_args()
    try:
        vertices = signed_solutions(args.p)
    except ValueError as error:
        parser.error(str(error))
    path = seed_path(args.p, vertices)
    print(f"p={args.p}, signed vertices={len(vertices)}, positive vertices={sum(v[0] > 0 for v in vertices)}")
    print("components (size, positive):", sorted((len(c), sum(v[0] > 0 for v in c)) for c in components(vertices)))
    if path is None:
        print("NO positive vertex in the seed component; this alone is not an ES counterexample.")
    else:
        print(f"shortest seed-to-positive path: {len(path) - 1} moves")
        for vertex in path:
            assert sum((Fraction(1, x) for x in vertex), Fraction()) == Fraction(4, args.p)
            print(vertex)
