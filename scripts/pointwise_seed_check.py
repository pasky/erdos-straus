"""Exact regression checks for SIGNED_REFACTOR.md, not a proof of ES.

uv run python scripts/pointwise_seed_check.py
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import gcd
import unittest

from sympy import divisors, primerange

from pointwise_incidence import (
    dual_hub_path,
    incidence_solutions,
    incidence_vertex,
    type_i_vertex,
)
from pointwise_refactor import components, seed, seed_path, signed_solutions


def reciprocal_sum(vertex):
    return sum((Fraction(1, x) for x in vertex), Fraction())


def independent_fibre(p: int, x: int):
    """Use the original reduced residual, with all signed divisors of s^2."""
    residual = Fraction(4, p) - Fraction(1, x)
    r, s = residual.numerator, residual.denominator
    vertices = set()
    for d in divisors(s * s):
        for signed_d in (int(d), -int(d)):
            if (signed_d + s) % r:
                continue
            cofactor = s * s // signed_d
            if (cofactor + s) % r:
                continue
            y, z = (signed_d + s) // r, (cofactor + s) // r
            if y and z:
                vertices.add(tuple(sorted((x, y, z))))
    return vertices


class SeedChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graphs = {p: signed_solutions(p) for p in (5, 13, 17, 29, 73, 97, 1009)}

    def test_unconditional_dual_hub_path(self):
        for p in primerange(5, 2001):
            if p % 4 != 1:
                continue
            t = (p - 1) // 4
            path = dual_hub_path(p)
            self.assertEqual(path[0], seed(p))
            self.assertEqual(path[-1], (-p * t, 2 * t, 2 * t))
            self.assertEqual(len(set(path)), 4)
            for vertex in path:
                self.assertNotIn(0, vertex)
                self.assertEqual(reciprocal_sum(vertex), Fraction(4, p))
            for before, after in zip(path, path[1:]):
                self.assertTrue(set(before) & set(after))

    def test_complete_hubs_and_private_seed_denominator(self):
        for p, vertices in self.graphs.items():
            t = (p - 1) // 4
            tau = len(divisors(t * t))
            first = {v for v in vertices if t in v}
            second = {v for v in vertices if -p * t in v}
            self.assertEqual(len(first), 3 * tau)
            self.assertEqual(len(second), tau)
            self.assertFalse(first & second)
            self.assertEqual(first, independent_fibre(p, t))
            self.assertEqual(second, independent_fibre(p, -p * t))
            self.assertEqual(independent_fibre(p, -2 * p * t), {seed(p)})
            reachable = set(next(c for c in components(vertices) if seed(p) in c))
            self.assertTrue(first | second <= reachable)
            repeated = {v for v in vertices if len(set(v)) < 3}
            self.assertEqual(repeated, {seed(p), (-p * t, 2 * t, 2 * t)})

    def test_p_colours_incidence_and_anchor_bound(self):
        for p, vertices in self.graphs.items():
            t = (p - 1) // 4
            bucket_types = {}
            sector_one = set()
            for vertex in vertices:
                self.assertEqual(reciprocal_sum(vertex), Fraction(4, p))
                free = [x for x in vertex if x % p]
                multiples = [x for x in vertex if x % p == 0]
                self.assertIn(len(multiples), (1, 2))
                self.assertTrue(all(x % (p * p) for x in multiples))
                self.assertTrue(any(0 < x <= 2 * t for x in free))
                for w in multiples:
                    kind = len(multiples)
                    self.assertEqual(bucket_types.setdefault(w, kind), kind)
                    for x in free:
                        self.assertEqual(incidence_vertex(p, x, w // p), vertex)
                if len(multiples) == 1:
                    self.assertEqual((4 * (multiples[0] // p) - 1) % p, 0)
                else:
                    m, n = (w // p for w in multiples)
                    self.assertGreater(free[0], 0)
                    self.assertEqual(((4 * m - 1) * (4 * n - 1)) % p, 1)
                    if (4 * m - 1) % p == 1:
                        sector_one.add(vertex)
            self.assertEqual(sector_one, {seed(p)})

    def test_incidence_component_correspondence(self):
        # Eligible but unused denominators are not isolated incidence components.
        self.assertEqual(independent_fibre(5, -1), set())
        self.assertTrue(all(-1 not in v for v in self.graphs[5]))
        for p, vertices in self.graphs.items():
            adjacency = defaultdict(set)
            edge_owner = {}
            for vertex in vertices:
                free = {x for x in vertex if x % p}
                quotients = {x // p for x in vertex if x % p == 0}
                for x in free:
                    for m in quotients:
                        self.assertNotIn((x, m), edge_owner)
                        edge_owner[x, m] = vertex
                        left, right = ("x", x), ("m", m)
                        adjacency[left].add(right)
                        adjacency[right].add(left)
            unseen, partition = set(adjacency), set()
            while unseen:
                todo, group = [unseen.pop()], set()
                while todo:
                    node = todo.pop()
                    for other in adjacency[node]:
                        left, right = (node, other) if node[0] == "x" else (other, node)
                        group.add(edge_owner[left[1], right[1]])
                        if other in unseen:
                            unseen.remove(other)
                            todo.append(other)
                partition.add(frozenset(group))
            self.assertEqual(partition, {frozenset(c) for c in components(vertices)})

    def test_type_i_coordinates_and_both_axes(self):
        for p, vertices in self.graphs.items():
            t = (p - 1) // 4
            reachable = set(next(c for c in components(vertices) if seed(p) in c))
            actual_first_axis, actual_second_axis = set(), set()
            for vertex in vertices:
                multiples = [x for x in vertex if x % p == 0]
                if len(multiples) != 1:
                    continue
                m = multiples[0] // p
                self.assertEqual((m + t) % p, 0)
                h = (m + t) // p
                # The Farey determinant is exactly one, not just nonzero.
                self.assertEqual(4 * m - p * (4 * h - 1), 1)
                self.assertEqual(gcd(m, 4 * h - 1), 1)
                for x in set(vertex) - set(multiples):
                    a = x - t
                    e = (4 * a - 1) * h - a
                    self.assertNotEqual(e, 0)
                    self.assertEqual(x * x % e, 0)
                    self.assertEqual(type_i_vertex(p, a, h), vertex)
                    self.assertEqual(vertex[0] > 0, a >= 1 and h >= 1)
                    if a == 0:
                        actual_first_axis.add(h)
                    if h == 0:
                        actual_second_axis.add(a)
            ds = {sign * int(d) for d in divisors(t * t) for sign in (-1, 1)}
            self.assertEqual(actual_first_axis, ds)
            self.assertEqual(actual_second_axis, ds - {-t})
            for h in ds:
                self.assertIn(type_i_vertex(p, 0, h), reachable)
            for a in ds - {-t}:
                self.assertIn(type_i_vertex(p, a, 0), reachable)

    def test_independent_complete_enumeration(self):
        for p in primerange(5, 1001):
            if p % 4 == 1:
                with self.subTest(p=p):
                    self.assertEqual(incidence_solutions(p), signed_solutions(p))
        p = 297049
        vertices = incidence_solutions(p)
        self.assertEqual(vertices, signed_solutions(p))
        self.assertEqual(len(vertices), 1143)
        self.assertEqual(sum(v[0] > 0 for v in vertices), 67)
        path = seed_path(p, vertices)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 4)
        for vertex in path:
            self.assertEqual(reciprocal_sum(vertex), Fraction(4, p))

    def test_two_negative_type_ii_vertex_can_be_isolated(self):
        p = 1009
        vertex = (-366267, -6054, 242)
        self.assertIn(vertex, self.graphs[p])
        self.assertEqual(gcd(*vertex), 1)
        self.assertEqual(sum(x < 0 for x in vertex), 2)
        self.assertEqual(sum(x % p == 0 for x in vertex), 2)
        self.assertEqual(reciprocal_sum(vertex), Fraction(4, p))
        for x in vertex:
            self.assertEqual(independent_fibre(p, x), {vertex})

    def test_invalid_inputs(self):
        for bad in (1, 9, 73 * 73):
            for build in (incidence_solutions, dual_hub_path):
                with self.assertRaises(ValueError):
                    build(bad)
        with self.assertRaises(ValueError):
            incidence_solutions(5374009)
        for x, m in ((0, 1), (1, 0), (73, 1), (1, 73), (1, 1)):
            with self.assertRaises(ValueError):
                incidence_vertex(73, x, m)
        for a, h in ((0, 0), (-18, 0), (1, 1), (55, 1)):
            with self.assertRaises(ValueError):
                type_i_vertex(73, a, h)


if __name__ == "__main__":
    unittest.main(verbosity=2)
