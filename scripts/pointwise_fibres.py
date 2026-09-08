"""Exact lazy signed-ES component search; not a universal reachability proof.

uv run python scripts/pointwise_fibres.py 297049

Type II p-divisible fibres and p-free fibres outside [1,(p-1)/2] use
constant-sized, factorization-free candidate sets. Other fibres use exact
intervals or certified divisors. Budget/unsupported factorization raises
IncompleteSearch, never a sterile-component verdict. Run under an external
memory limit and timeout; an interrupted run has no exhaustion verdict.
"""
from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
import json
from math import gcd, prod

from sympy import factorint, isprime

from pointwise_refactor import seed


Vertex = tuple[int, int, int]


class IncompleteSearch(RuntimeError):
    """A resource/certification limit, not a mathematical counterexample."""


def checked_vertex(p: int, values) -> Vertex:
    vertex = tuple(sorted(values))
    if len(vertex) != 3 or not all(vertex):
        raise ValueError("expected three nonzero denominators")
    x, y, z = vertex
    if 4 * x * y * z != p * (x * y + x * z + y * z):
        raise ValueError("not a signed ES vertex")
    return vertex


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


class FibreOracle:
    def __init__(self, p: int, *, max_divisors=200_000, max_fibre=100_000,
                 interval_budget=20_001, factor_limit=100_000):
        if not 5 <= p < 2**64 or p % 4 != 1 or not isprime(p):
            raise ValueError("expected a prime p=1 mod4 below 2^64")
        if min(max_divisors, max_fibre, interval_budget, factor_limit) < 1:
            raise ValueError("all budgets must be positive")
        self.p, self.t = p, (p - 1) // 4
        self.max_divisors, self.max_fibre = max_divisors, max_fibre
        self.interval_budget, self.factor_limit = interval_budget, factor_limit
        self.known_primes = {2, 3, p}
        self.cache: dict[int, set[Vertex]] = {}

    def factor(self, n: int) -> dict[int, int]:
        if n < 1:
            raise ValueError("expected a positive integer to factor")
        original, factors = n, {}
        for ell in sorted(self.known_primes):
            exponent = 0
            while n % ell == 0:
                n //= ell
                exponent += 1
            if exponent:
                factors[ell] = exponent
        if n >= 2**64:
            raise IncompleteSearch("fresh factorization exceeds the 64-bit certification range")
        fresh = {int(ell): int(e) for ell, e in factorint(n, limit=self.factor_limit).items()}
        if not all(1 < ell < 2**64 and isprime(ell) for ell in fresh):
            raise IncompleteSearch("factorization budget left an uncertified composite factor")
        for ell, exponent in fresh.items():
            factors[ell] = factors.get(ell, 0) + exponent
        assert prod(ell**e for ell, e in factors.items()) == original
        self.known_primes.update(fresh)
        return factors

    def square_divisors(self, n: int):
        factors = list(self.factor(n).items())
        if prod(2 * exponent + 1 for _, exponent in factors) > self.max_divisors:
            raise IncompleteSearch("square-divisor budget exceeded")

        def generate(i, d):
            if i == len(factors):
                yield d
                return
            ell, exponent = factors[i]
            for _ in range(2 * exponent + 1):
                yield from generate(i + 1, d)
                d *= ell

        yield from generate(0, 1)

    def _add(self, out: set[Vertex], values) -> None:
        out.add(checked_vertex(self.p, values))
        if len(out) > self.max_fibre:
            raise IncompleteSearch("fibre-vertex budget exceeded")

    def _outer_pfree(self, z: int) -> set[Vertex]:
        # Type II is impossible here. The other p-free x is in [1,2t],
        # and the Type I quotient m lies in (-infinity,-t] or [3t+1,infinity).
        p, t = self.p, self.t
        residual = Fraction(4, p) - Fraction(1, z)
        lo = ceil_fraction(1 / (residual + Fraction(1, p * t)))
        upper = 1 / (residual - Fraction(1, p * (3 * t + 1)))
        hi = upper.numerator // upper.denominator
        assert hi <= 2 * t and hi - lo <= 1
        out = set()
        for x in range(lo, hi + 1):
            denominator = 4 * z * x - p * (z + x)
            if denominator and (p * z * x) % denominator == 0:
                self._add(out, (z, x, p * z * x // denominator))
        return out

    def _type_ii(self, m: int) -> set[Vertex]:
        # The other quotient n occupies one nonzero residue class mod p.
        # All but its centered representative force x to the nearest integer
        # to p*m/(4*m-1). This is a complete TWO-candidate test, not a window.
        p, t = self.p, self.t
        k = 4 * m - 1
        n = (m * pow(k, -1, p)) % p
        if n > 2 * t:
            n -= p
        out = set()
        denominator = 4 * m * n - m - n
        if denominator and (p * m * n) % denominator == 0:
            self._add(out, (p * m * n // denominator, p * m, p * n))
        center = Fraction(p * m, k)
        x = (2 * center.numerator + center.denominator) // (2 * center.denominator)
        d = k * x - p * m
        if d and (m * m) % d == 0:
            assert (m * x) % d == 0
            self._add(out, (x, p * m, p * (m * x // d)))
        assert len(out) <= 2
        return out

    def _divisor_fibre(self, z: int) -> set[Vertex]:
        p = self.p
        r, s = 4 * z - p, p * z
        common = gcd(r, s)
        r, s = r // common, s // common
        if s < 0:
            r, s = -r, -s
        out = set()
        for d in self.square_divisors(s):
            if d > s:  # Complementary divisors give the same unordered triple.
                continue
            for signed_d in (d, -d):
                if (signed_d + s) % r:
                    continue
                y = (signed_d + s) // r
                cofactor = s * s // signed_d
                assert (cofactor + s) % r == 0
                other = (cofactor + s) // r
                if y and other:
                    self._add(out, (z, y, other))
        return out

    def fibre(self, z: int) -> set[Vertex]:
        if z == 0:
            raise ValueError("zero is not an eligible denominator")
        if z in self.cache:
            return self.cache[z]
        p, t = self.p, self.t
        if z % (p * p) == 0:
            out = set()  # The p-adic valuation theorem excludes these labels.
        elif z % p and (z < 0 or z > 2 * t):
            out = self._outer_pfree(z)
        elif z % p == 0 and (4 * (z // p) - 1) % p:
            out = self._type_ii(z // p)
        elif z % p == 0:
            m = z // p
            h = (m + t) // p
            # |(4h-1)a-h| <= (t+a)^2 <= 4t^2, with 1-t <= a <= t.
            bound = (4 * t * t + abs(h)) // abs(4 * h - 1)
            lo, hi = max(1 - t, -bound), min(t, bound)
            if hi - lo + 1 <= self.interval_budget:
                out = set()
                for a in range(lo, hi + 1):
                    x, e = t + a, (4 * a - 1) * h - a
                    if e and (x * x) % e == 0:
                        assert (x * m) % e == 0
                        self._add(out, (x, z, x * m // e))
            else:
                out = self._divisor_fibre(z)
        else:
            out = self._divisor_fibre(z)
        self.cache[z] = out  # Never cache a partial fibre after an exception.
        return out


@dataclass
class SearchResult:
    status: str
    path: list[Vertex] | None
    visited: int
    expanded: int


def explore(oracle: FibreOracle, start: Vertex | None = None, *, max_vertices=100_000) -> SearchResult:
    """FOUND gives a shortest path; STERILE requires entire component exhaustion.

    IncompleteSearch interrupts traversal without any component verdict.
    An arbitrary valid start is supported for independent sterile-component tests.
    """
    if max_vertices < 1:
        raise ValueError("vertex budget must be positive")
    root = checked_vertex(oracle.p, seed(oracle.p) if start is None else start)
    previous: dict[Vertex, Vertex | None] = {root: None}
    todo, expanded = deque([root]), set()

    def found(vertex):
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = previous[vertex]
        return SearchResult("FOUND", path[::-1], len(previous), len(expanded))

    if root[0] > 0:
        return found(root)
    while todo:
        vertex = todo.popleft()
        for z in sorted(set(vertex), key=lambda x: (abs(4 * x - oracle.p), abs(x))):
            if z in expanded:
                continue
            neighbours = oracle.fibre(z)
            expanded.add(z)
            for other in sorted(neighbours):
                if other in previous:
                    continue
                if len(previous) >= max_vertices:
                    raise IncompleteSearch("component-vertex budget exceeded")
                previous[other] = vertex
                if other[0] > 0:
                    return found(other)
                todo.append(other)
    return SearchResult("STERILE", None, len(previous), len(expanded))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p", type=int)
    parser.add_argument("--max-vertices", type=int, default=100_000)
    args = parser.parse_args()
    try:
        result = explore(FibreOracle(args.p), max_vertices=args.max_vertices)
    except ValueError as error:
        parser.error(str(error))
    except IncompleteSearch as error:
        print(json.dumps({"status": "UNKNOWN", "reason": str(error)}))
        raise SystemExit(2)
    print(json.dumps(vars(result)))
