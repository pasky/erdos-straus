"""Exact difficult-input checks, not a census or an ES proof.

uv run python scripts/pointwise_escape_check.py

The large inputs are NOT fully enumerated. We exhaust the two-move seed
criterion and all possible positive neighbours of the two unit-residual
fibres, then check supplied three-edge paths. Sparse p=24q+1 inputs are
capped at 3*10^12. All newly factored integers are below 2^64.
"""
from __future__ import annotations

from fractions import Fraction
from math import prod
import unittest

from sympy import factorint, isprime, primerange

from pointwise_incidence import negative_fibre_transfer, quadratic_signature
from pointwise_refactor import seed, seed_path, signed_solutions


LIMIT = 3_000_000_000_000


def sparse_parameter(p: int) -> int:
    if not 313 <= p <= LIMIT or p % 24 != 1 or not isprime(p):
        raise ValueError("expected a prime p=24q+1 between 313 and 3*10^12")
    q = (p - 1) // 24
    if not isprime(q):
        raise ValueError("q=(p-1)/24 must also be prime")
    return q


def square_divisors(factors):
    ds = [1]
    for ell, exponent in factors.items():
        old, power = ds[:], 1
        for _ in range(2 * exponent):
            power *= ell
            ds.extend(d * power for d in old)
    return ds


def factor_with_known(n: int, q: int):
    if n < 1:
        raise ValueError("expected a positive integer to factor")
    original, factors = n, {}
    for ell in (2, 3, q):
        exponent = 0
        while n % ell == 0:
            n //= ell
            exponent += 1
        if exponent:
            factors[ell] = exponent
    if not 1 <= n < 2**64:
        raise ValueError("fresh factorization exceeds the certified input range")
    for ell, exponent in factorint(n).items():
        ell, exponent = int(ell), int(exponent)
        assert ell < 2**64 and isprime(ell)
        factors[ell] = factors.get(ell, 0) + exponent
    assert prod(ell**e for ell, e in factors.items()) == original
    return factors


def checked_positive(p, vertex):
    vertex = tuple(sorted(vertex))
    assert vertex[0] > 0
    assert sum((Fraction(1, x) for x in vertex), Fraction()) == Fraction(4, p)
    return vertex


def positive_type_i_pair(p: int, h: int, q: int):
    t, m = 6 * q, p * h - 6 * q
    if h >= q * q:
        # If positive, one p-free denominator is x=t+a with 1<=a<=t.
        # e=(4a-1)h-a divides x², hence e<=x². For h>t, e-x² strictly
        # increases on this interval. We stop only once this proved
        # necessary inequality fails, not at a guessed window cutoff.
        assert h > t
        for a in range(1, t + 1):
            x, e = t + a, (4 * a - 1) * h - a
            if e > x * x:
                return None
            if x * x % e == 0:
                assert x * m % e == 0
                return checked_positive(p, (x, x * m // e, p * m))
        return None
    # Here h is c or c*q, c|36; stripping q leaves only an O(p) integer.
    r = 4 * h - 1
    for d in square_divisors(factor_with_known(m, q)):
        if d <= m and (d + m) % r == 0:
            assert (m * m // d + m) % r == 0
            return checked_positive(p, ((d + m) // r, (m * m // d + m) // r, p * m))
    return None


def two_move_path(p: int):
    """Complete seed-to-positive test for at most TWO edges; never a full BFS."""
    q = sparse_parameter(p)
    t = 6 * q
    for h in sorted(square_divisors({2: 1, 3: 1, q: 1})):
        hit = positive_type_i_pair(p, h, q)
        if hit:
            before = tuple(sorted((t, -p * t + t * t // h, p * (p * h - t))))
            return [seed(p), before, hit]
    return None


def positive_pfree_fibre(p: int, x: int, q: int):
    r = 4 * x - p
    assert r > 0 and x % p
    for d in square_divisors(factor_with_known(x, q)):
        if (d + x) % r == 0:
            return checked_positive(p, (x, p * (x + d) // r, p * (x + x * x // d) // r))
        if (d + p * x) % r == 0:
            return checked_positive(p, (x, (p * x + d) // r, (p * x + p * p * (x * x // d)) // r))
    return None


def dual_fibre_neighbour(p: int):
    """Any positive neighbour of ANY vertex in the whole -pt fibre.

    This is not a test of all two-edge paths from the vertex (-pt,2t,2t):
    those can also start by retaining 2t instead of -pt.
    """
    q = sparse_parameter(p)
    t = 6 * q
    # The mixed pairs have their positive entry <=t, unusable in a positive
    # ES triple. All remaining positive anchors are t+d, d>0, d|t².
    for d in sorted(square_divisors({2: 1, 3: 1, q: 1})):
        hit = positive_pfree_fibre(p, t + d, q)
        if hit:
            return hit
    return None


# Both unit-residual fibres have no immediately adjacent positive vertex.
# These inputs nevertheless have the following verified three-edge escapes.
CASES = (
    (2271767935369, 4, 676,
     (567941983882, 8114964431270991607040, 222976659599006075120700160)),
    (772045387369, 2, 700,
     (193011346920, 479143151445221366840, 2114893590888712773276755822314938936570)),
)


class EscapeChecks(unittest.TestCase):
    def test_two_move_criterion_against_complete_graphs(self):
        for q in primerange(13, 151):
            p = 24 * q + 1
            if not isprime(p):
                continue
            path = seed_path(p, signed_solutions(p))
            self.assertIsNotNone(path)
            self.assertEqual(two_move_path(p) is not None, len(path) <= 3)
        self.assertIsNone(two_move_path(297049))

    def test_both_unit_fibres_can_have_no_positive_neighbour(self):
        for p, _, _, _ in CASES:
            self.assertIsNone(two_move_path(p))
            self.assertIsNone(dual_fibre_neighbour(p))

    def test_exact_three_edge_escapes_and_character_crossing(self):
        for p, c, d, positive in CASES:
            path = negative_fibre_transfer(p, c, d) + [positive]
            self.assertEqual(len(set(path)), 4)
            for vertex in path:
                self.assertEqual(sum((Fraction(1, x) for x in vertex), Fraction()), Fraction(4, p))
            for before, after in zip(path, path[1:]):
                self.assertTrue(set(before) & set(after))
            self.assertEqual([quadratic_signature(p, v) for v in path], [1, 1, 1, -1])
            t = (p - 1) // 4
            self.assertEqual(path[2][1], t + (d + c) // (4 * c + 1))
        # In the first case the final step changes Type I to Type II,
        # keeping x=t+40, and enters a nonresidue-labelled Type II bucket.
        p, _, _, positive = CASES[0]
        multiples = [x // p for x in positive if x % p == 0]
        self.assertEqual(len(multiples), 2)
        self.assertEqual(pow((4 * multiples[0] - 1) % p, (p - 1) // 2, p), p - 1)

    def test_negative_transfer_is_not_a_forcing_claim(self):
        path = negative_fibre_transfer(73, 1, 49)
        self.assertEqual(path[-2:], [(-6643, -1638, 18), (-6643, 28, 52)])
        # This is the already-known one-neighbour trap, not a positive exit.
        self.assertEqual(quadratic_signature(73, path[-1]), 1)

    def test_invalid_inputs(self):
        for p in (73, 5374009, LIMIT + 1):
            with self.assertRaises(ValueError):
                two_move_path(p)
        for c, d in ((0, 1), (5, 1), (1, 0), (1, 1)):
            with self.assertRaises(ValueError):
                negative_fibre_transfer(73, c, d)


if __name__ == "__main__":
    unittest.main(verbosity=2)
