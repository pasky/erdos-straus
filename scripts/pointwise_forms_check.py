"""Independent exact checks for the pointwise experiment, not a proof of ES.

    uv run python scripts/pointwise_forms_check.py
    uv run python scripts/pointwise_forms_check.py --census /tmp/es-form-certificates.txt

The optional census is streamed and independently checked against sympy's primes.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import unittest

from sympy import divisors, isprime, primerange

from pointwise_refactor import components, seed_path, signed_solutions


def reduced_forms(p: int):
    for a in range(1, isqrt(4 * p // 3) + 1):
        for half_b in range(-(a // 2), a // 2 + 1):
            b = 2 * half_b
            numerator = b * b + 4 * p
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if a > c or gcd(a, b, c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            yield a, b, c


def window(p: int, a: int) -> int:
    return a * (p // (4 * a) + 1)


def reconstruct(p: int, x: int, d: int, kind: int) -> tuple[int, int, int]:
    q = 4 * x - p
    assert q > 0 and x % p and d > 0 and x * x % d == 0
    if kind == 2:
        assert (d + x) % q == 0
        numerators = p * (x + d), p * (x + x * x // d)
    else:
        assert kind == 1 and (d + p * x) % q == 0
        numerators = p * x + d, p * x + p * p * (x * x // d)
    assert all(n % q == 0 for n in numerators)
    triple = x, numerators[0] // q, numerators[1] // q
    assert all(v > 0 for v in triple)
    assert sum((Fraction(1, v) for v in triple), Fraction()) == Fraction(4, p)
    assert sum(v % p == 0 for v in triple) == kind
    return triple


def window_hit(p: int, x: int):
    q = 4 * x - p
    for d in divisors(x * x):
        if (d + x) % q == 0:
            return int(d), 2
        if (d + p * x) % q == 0:
            return int(d), 1
    return None


def independent_two_term_hit(p: int, x: int) -> bool:
    # Search the entire denominator fibre, not the two specialized targets.
    q, s = 4 * x - p, p * x
    for d in divisors(s * s):
        if (d + s) % q == 0 and (s * s // d + s) % q == 0:
            return True
    return False


def zagier(triple):
    r, s, t = triple
    if r < s - t:
        return r + 2 * t, t, s - r - t
    if r < 2 * s:
        return 2 * s - r, s, r - s + t
    return r - 2 * s, r - s + t, s


def distinguished_component(p: int):
    todo, seen = [(1, 1, (p - 1) // 4)], set()
    while todo:
        triple = todo.pop()
        if triple in seen:
            continue
        r, s, t = triple
        assert min(triple) > 0 and r * r + 4 * s * t == p
        assert zagier(zagier(triple)) == triple
        seen.add(triple)
        todo.extend((zagier(triple), (r, t, s)))
    return seen


def reduce_form(form):
    a, b, c = form
    while True:
        shift = (a - b) // (2 * a)
        a, b, c = a, b + 2 * shift * a, c + b * shift + a * shift * shift
        if a > c:
            a, b, c = c, -b, a
            continue
        if (abs(b) == a or a == c) and b < 0:
            b = -b
        return a, b, c


def square_form(form):
    a, b, c = form
    discriminant = b * b - 4 * a * c
    for shift in range(1000):
        aa, bb = a + b * shift + c * shift * shift, b + 2 * c * shift
        if gcd(aa, bb) == 1:
            a, b = aa, bb
            break
    else:
        raise ValueError("no coprime representative within the test bound")
    t = (-c * pow(b, -1, a)) % a if a > 1 else 0
    new_b = b + 2 * a * t
    assert (new_b * new_b - discriminant) % (4 * a * a) == 0
    return reduce_form((a * a, new_b, (new_b * new_b - discriminant) // (4 * a * a)))


def primitive_type_i(n: int):
    """Tuple-first enumeration, using ack <= 2n/3 and a <= b."""
    tuples = set()
    for x in range(n // 4 + 1, 2 * n // 3 + 1):
        for a in divisors(x):
            for c in divisors(x // a):
                k = x // (a * c)
                d = 4 * x - n
                if (n * a + k) % d:
                    continue
                b = (n * a + k) // d
                if b >= a and gcd(a, b) == 1 and gcd(k, n) == 1:
                    tuples.add((int(a), int(b), int(c), int(k)))
    return tuples


def primitive_type_i_from_denominators(n: int):
    tuples = set()
    for x in range(n // 4 + 1, 2 * n // 3 + 1):
        if gcd(x, n) != 1:
            continue
        q = 4 * x - n
        for d in divisors(x * x):
            if (d + n * x) % q:
                continue
            y = (n * x + d) // q
            z = (n * x + n * n * (x * x // d)) // q
            if y < x:
                continue
            assert gcd(y, n) == 1 and z % n == 0
            g = gcd(x, y)
            a, b = x // g, y // g
            assert (z // n) % (a * b) == 0
            c = (z // n) // (a * b)
            assert g % c == 0
            tuples.add((int(a), int(b), int(c), int(g // c)))
    return tuples


def product_witnesses(p: int, product: int):
    for a in divisors(product):
        b = product // a
        if a > b:
            break
        for d in divisors(a + b):
            if (p + d) % (4 * product) == 0:
                yield 2, a, b, (p + d) // (4 * product), (a + b) // d
            if (p * d + 1) % (4 * product) == 0:
                yield 1, a, b, (p * d + 1) // (4 * product), (a + b) // d


class PointwiseChecks(unittest.TestCase):
    def test_zagier_component_failures(self):
        component = distinguished_component(1129)
        self.assertEqual(len(component), 39)
        old_windows = {s * (t + 1) for r, s, t in component if 4 * s > r * r}
        self.assertEqual(len(old_windows), 14)
        self.assertTrue(all(not independent_two_term_hit(1129, x) for x in old_windows))
        self.assertTrue(any(window_hit(1129, window(1129, s)) for _, s, _ in component))
        component = distinguished_component(14401)
        self.assertEqual(len(component), 121)
        nearest = {window(14401, s) for _, s, _ in component}
        self.assertEqual(len(nearest), 61)
        self.assertTrue(all(not independent_two_term_hit(14401, x) for x in nearest))

    def test_entire_two_primary_subgroup_can_fail(self):
        p = 3049
        forms = set(reduced_forms(p))
        self.assertEqual(len(forms), 28)
        principal = (1, 0, p)
        primary = {f for f in forms if square_form(square_form(f)) == principal}
        self.assertEqual(primary, {(1, 0, p), (2, 2, 1525), (47, -20, 67), (47, 20, 67)})
        self.assertEqual(square_form((47, 20, 67)), (2, 2, 1525))
        self.assertEqual({window(p, a) for a, _, _ in primary}, {763, 764, 799})
        self.assertTrue(all(not independent_two_term_hit(p, window(p, a)) for a, _, _ in primary))
        self.assertEqual(sum(window_hit(p, window(p, a)) is not None for a, _, _ in forms), 14)
        self.assertIn((5, 2, 610), forms)
        reconstruct(p, 765, 153, 1)

    def test_failure_is_not_a_subgroup(self):
        forms = set(reduced_forms(193))
        self.assertEqual(len(forms), 4)
        self.assertIsNone(window_hit(193, window(193, 11)))
        self.assertEqual(square_form((11, 8, 19)), (2, 2, 97))
        self.assertIsNotNone(window_hit(193, window(193, 2)))

    def test_least_nonresidue_does_not_bound_product_by_its_square(self):
        p = 21841
        self.assertTrue(isprime(p))
        self.assertTrue(all(pow(a, (p - 1) // 2, p) == 1 for a in range(1, 11)))
        self.assertEqual(pow(11, (p - 1) // 2, p), p - 1)
        # No character or coprimality filtering in this exclusion.
        self.assertTrue(all(not list(product_witnesses(p, a)) for a in range(1, 134)))
        self.assertIn((2, 1, 134, 41, 1), list(product_witnesses(p, 134)))
        self.assertTrue(all(not list(product_witnesses(p, a)) for a in range(11, 7436, 11)))
        self.assertIn((1, 4, 1859, 152, 9), list(product_witnesses(p, 7436)))
        triple = (5494, 895481, 119994454)
        self.assertEqual(sum((Fraction(1, x) for x in triple), Fraction()), Fraction(4, p))

    def test_pell_principal_genus_is_sterile(self):
        p = 2521
        big_x = 8861947355238964911710285309947236168
        big_y = 176499200680758894072067730693233165
        self.assertEqual(big_x * big_x - p * big_y * big_y, -1)
        forms = set(reduced_forms(p))
        principal_genus = {f for f in forms if (f[0] if f[0] % 2 else f[2]) % 4 == 1}
        self.assertEqual(len(forms), 32)
        self.assertEqual(len(principal_genus), 16)
        self.assertEqual({a for a, _, _ in principal_genus}, {1, 2, 5, 10, 13, 25, 26, 41, 50})
        self.assertTrue(all(not independent_two_term_hit(p, window(p, a)) for a, _, _ in principal_genus))
        self.assertIn((11, 6, 230), forms - principal_genus)
        self.assertEqual(reconstruct(p, 638, 44, 2), (638, 55462, 804199))

    def test_reducing_a_witness_does_not_preserve_productivity(self):
        self.assertIsNotNone(window_hit(193, 52))
        root_divisors = {a for a in divisors(52) if any((b * b + 193) % a == 0 for b in range(a))}
        self.assertEqual(root_divisors, {1, 2})
        self.assertTrue(all(4 * a <= 15 for a in root_divisors))
        self.assertIsNotNone(window_hit(241, 69))
        self.assertEqual(reduce_form((23, 18, 14)), (14, 10, 19))
        self.assertFalse(independent_two_term_hit(241, 70))

    def test_prime_power_ratio_coverage(self):
        for ell, exponent in ((3, 1), (3, 2), (3, 3), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (17, 2), (17, 3)):
            n = ell ** exponent
            tuples = primitive_type_i(n)
            self.assertEqual(tuples, primitive_type_i_from_denominators(n))
            for a, b, c, k in tuples:
                self.assertEqual(k * (4 * a * b * c - 1), n * (a + b))
                self.assertLessEqual(3 * a * c * k, 2 * n)
                self.assertLessEqual(9 * min(a * c, a * k, c * k) ** 3, 4 * n * n)
                self.assertEqual(exponent % 2, 1)
                self.assertEqual(pow((-a * pow(b, -1, n)) % n, (ell - 1) // 2, ell), ell - 1)
                d = 4 * a * c * k - n
                self.assertGreater(d, 0)
                self.assertEqual(n * (4 * a * a * c + 1) % d, 0)
                self.assertEqual((n * a + k) % d, 0)
                self.assertEqual((n * n + 4 * c * k * k) % d, 0)
            if ell == 17 and exponent == 1:
                self.assertEqual(tuples, {(2, 5, 3, 1), (1, 6, 5, 1)})
            if ell == 17 and exponent == 2:
                self.assertFalse(tuples)
            if ell == 17 and exponent == 3:
                self.assertEqual(len(tuples), 57)
                ratios = {(-u * pow(v, -1, n)) % n for a, b, _, _ in tuples for u, v in ((a, b), (b, a))}
                self.assertEqual(len(ratios), 112)
                self.assertEqual(sum(r % 17 in {5, 7, 10, 12} for r in ratios), 46)

    def test_signed_graph_can_have_sterile_components(self):
        vertices = signed_solutions(97)
        sizes = sorted((len(c), sum(v[0] > 0 for v in c)) for c in components(vertices))
        self.assertEqual(sizes, [(1, 0), (1, 0), (114, 8)])
        self.assertIsNotNone(seed_path(97, vertices))

    def test_signed_graph_has_a_lexicographic_trap(self):
        vertices = signed_solutions(73)
        trap = (-6643, 28, 52)
        neighbors = {v for v in vertices if v != trap and set(v) & set(trap)}
        self.assertEqual(neighbors, {(-6643, -1638, 18)})
        escape = [trap, (-6643, -1638, 18), (-1260, 18, 30660), (20, 210, 30660)]
        for v in escape:
            self.assertIn(v, vertices)
        for before, after in zip(escape, escape[1:]):
            self.assertTrue(set(before) & set(after))
        plateau = {(-1314, 36, 36), (-97236, 36, 37)}
        self.assertTrue(plateau <= set(vertices))
        def score(vertex):
            return -sum(x < 0 for x in vertex), min(x for x in vertex if x > 0)
        for vertex in plateau:
            self.assertEqual(score(vertex), (-1, 36))
            for other in vertices:
                if other not in plateau and set(vertex) & set(other):
                    self.assertLess(score(other), score(vertex))

    def test_signed_graph_requires_three_moves(self):
        p = 297049
        vertices = signed_solutions(p)
        self.assertEqual(len(vertices), 1143)
        self.assertEqual(sum(v[0] > 0 for v in vertices), 67)
        path = seed_path(p, vertices)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 4)
        for vertex in path:
            self.assertEqual(sum((Fraction(1, x) for x in vertex), Fraction()), Fraction(4, p))
        for before, after in zip(path, path[1:]):
            self.assertTrue(set(before) & set(after))
        for bad in (1, 9, 97 * 97, 300001):
            with self.assertRaises(ValueError):
                signed_solutions(bad)

    def test_reduced_form_construction_through_10000(self):
        for p in primerange(73, 10001):
            if p % 24 != 1:
                continue
            for a, _, _ in reduced_forms(p):
                x = window(p, a)
                hit = window_hit(p, x)
                if hit:
                    reconstruct(p, x, *hit)
                    break
            else:
                self.fail(f"construction fails at {p}")


def check_census(path: Path):
    count, max_a = 0, 0
    with path.open() as stream:
        header = stream.readline().split()
        assert len(header) == 3 and header[:2] == ["#", "limit"]
        limit = int(header[2])
        assert 73 <= limit <= 10_000_000
        for p in primerange(73, limit + 1):
            if p % 24 != 1:
                continue
            row = list(map(int, stream.readline().split()))
            assert len(row) == 7
            given_p, a, b, c, x, d, kind = row
            assert given_p == p and 0 <= b <= a <= c and gcd(a, b, c) == 1
            assert b * b - 4 * a * c == -4 * p
            assert x == window(p, a)
            reconstruct(p, x, d, kind)
            if p <= 10000:
                first_a = next(aa for aa, _, _ in reduced_forms(p) if window_hit(p, window(p, aa)))
                assert a == first_a
            count += 1
            max_a = max(max_a, a)
        assert stream.readline().split() == ["#", "checked", str(count)]
        assert not stream.read(1), "unexpected trailing data"
    print(f"Independent census PASS: limit={limit}, primes={count}, max-first-A={max_a}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--census", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PointwiseChecks))
    if not result.wasSuccessful():
        raise SystemExit(1)
    if args.census:
        check_census(args.census)
