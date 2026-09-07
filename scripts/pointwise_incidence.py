"""Two-colour denominator model of the signed ES graph (not an ES proof).

uv run python scripts/pointwise_incidence.py 297049

A p-free denominator x is incident to a p-divisible denominator p*m exactly
when f=(4*x-p)*m-x is nonzero and divides p*x*x. The third denominator is
p*x*m/f. See SIGNED_REFACTOR.md for completeness and the bound x <= (p-1)/2
on at least one positive p-free denominator of every signed vertex.
"""
from __future__ import annotations

import argparse
from array import array
from collections import Counter
from math import isqrt

from sympy import isprime

from pointwise_refactor import components, seed, seed_path


def _require_prime(p: int) -> None:
    if p < 5 or p % 4 != 1 or not isprime(p):
        raise ValueError("p must be a prime congruent to 1 mod 4, with p >= 5")


def incidence_vertex(p: int, x: int, m: int) -> tuple[int, int, int]:
    """Reconstruct an edge; m denotes the denominator p*m, not m itself."""
    _require_prime(p)
    if not x or not m or x % p == 0 or m % p == 0:
        raise ValueError("x and m must be nonzero and prime to p")
    f = (4 * x - p) * m - x
    if not f or (p * x * x) % f:
        raise ValueError("the incidence divisor must be nonzero and divide p*x^2")
    assert (p * x * m) % f == 0
    z = p * x * m // f
    return tuple(sorted((x, p * m, z)))


def type_i_vertex(p: int, a: int, h: int) -> tuple[int, int, int]:
    """Type I means exactly ONE p-divisible denominator.

    x=t+a, m=p*h-t, e=(4*a-1)*h-a. The exact condition is e|x^2.
    An admissible vertex is positive exactly when a>=1 and h>=1.
    """
    _require_prime(p)
    t = (p - 1) // 4
    x, m = t + a, p * h - t
    e = (4 * a - 1) * h - a
    if not x or x % p == 0 or not e or (x * x) % e:
        raise ValueError("inadmissible Type I coordinates")
    return incidence_vertex(p, x, m)


def quadratic_signature(p: int, vertex: tuple[int, int, int]) -> int:
    """The same-p-valuation pair has character -1 iff the triple is positive.

    This assertion concerns actual signed ES vertices, not arbitrary triples.
    For Type I take the two p-free denominators; for Type II divide the two
    p-divisible denominators by p first. See SIGNED_REFACTOR.md, section 2.
    """
    _require_prime(p)
    if len(vertex) != 3 or not all(vertex):
        raise ValueError("expected three nonzero denominators")
    x, y, z = vertex
    if 4 * x * y * z != p * (x * y + x * z + y * z):
        raise ValueError("not a signed ES vertex at p")
    free = [x for x in vertex if x % p]
    pair = free if len(free) == 2 else [x // p for x in vertex if x % p == 0]
    assert len(pair) == 2 and all(x % p for x in pair)
    value = pow((pair[0] * pair[1]) % p, (p - 1) // 2, p)
    assert value in (1, p - 1)
    return 1 if value == 1 else -1


def negative_fibre_transfer(p: int, c: int, d: int) -> list[tuple[int, int, int]]:
    """A legal two-edge path through h=-c, not a promised positive exit.

    c|t², d|(pc+t)², and d=-c mod(4c+1). The reached p-free anchor is
    t+(d+c)/(4c+1). The last vertex still has its p-divisible denominator
    negative; either positive p-free anchor may now be refactored.
    """
    _require_prime(p)
    t = (p - 1) // 4
    if c <= 0 or d <= 0 or t * t % c or (p * c + t) ** 2 % d or (d + c) % (4 * c + 1):
        raise ValueError("inadmissible negative-fibre transfer")
    a = (d + c) // (4 * c + 1)
    return [seed(p), type_i_vertex(p, 0, -c), type_i_vertex(p, a, -c)]


def dual_hub_path(p: int) -> list[tuple[int, int, int]]:
    """An unconditional three-edge path to the second unit-residual hub."""
    _require_prime(p)
    t = (p - 1) // 4
    return [
        seed(p),
        tuple(sorted((t, -t * (p + 1), -p * t * (p + 1)))),
        tuple(sorted((2 * t, 2 * t + 1, -p * t * (p + 1)))),
        (-p * t, 2 * t, 2 * t),
    ]


def incidence_solutions(p: int) -> list[tuple[int, int, int]]:
    """Enumerate the ENTIRE graph via f=+/-p^j*d, j=0,1, d|x^2.

    This is an independent enumeration from pointwise_refactor.signed_solutions:
    it uses a different divisor equation and the sharper positive-anchor bound.
    There is no height cutoff on the other two denominators.
    """
    _require_prime(p)
    if p > 300000:
        raise ValueError("complete enumeration is capped at p <= 300000")
    bound = (p - 1) // 2
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
    for x in range(1, bound + 1):
        q = 4 * x - p
        for d in square_divisors(x):
            for power in (1, p):
                for f in (power * d, -power * d):
                    if (x + f) % q:
                        continue
                    m = (x + f) // q
                    if not m:
                        continue
                    assert m % p != 0
                    assert (p * x * m) % f == 0
                    z = p * x * m // f
                    assert z and 4 * x * (p * m) * z == p * (x * (p * m) + x * z + (p * m) * z)
                    out.add(tuple(sorted((x, p * m, z))))
    return sorted(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p", type=int)
    args = parser.parse_args()
    try:
        vertices = incidence_solutions(args.p)
    except ValueError as error:
        parser.error(str(error))
    print(f"p={args.p}, positive p-free anchor bound={(args.p - 1) // 2}")
    print(f"signed vertices={len(vertices)}, positive vertices={sum(v[0] > 0 for v in vertices)}")
    counts = Counter((len(c), sum(v[0] > 0 for v in c)) for c in components(vertices))
    print("component multiplicities {(size, positive): count}:", dict(sorted(counts.items())))
    print("unconditional dual-hub path:")
    for vertex in dual_hub_path(args.p):
        print(vertex)
    path = seed_path(args.p, vertices)
    if path is None:
        print("NO positive vertex in the seed component; this alone is not an ES counterexample.")
    else:
        print(f"shortest seed-to-positive path: {len(path) - 1} moves")
        for vertex in path:
            print(vertex)
