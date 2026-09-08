"""Independent checks of exact lazy fibres and exhaustion status, not ES proof."""
from fractions import Fraction
import unittest
from unittest.mock import patch

from pointwise_fibres import FibreOracle, IncompleteSearch, explore
from pointwise_refactor import components, denominator_buckets, seed, seed_path, signed_solutions
from pointwise_seed_check import independent_fibre


class FibreChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graphs = {p: signed_solutions(p) for p in (5, 13, 17, 29, 73, 97, 193, 1009, 6089)}

    def test_every_bucket_against_independent_complete_graphs(self):
        for p, vertices in self.graphs.items():
            oracle = FibreOracle(p)
            for z, indices in denominator_buckets(vertices).items():
                self.assertEqual(oracle.fibre(z), {vertices[i] for i in indices}, (p, z))
        # Force the divisor fallback too, rather than testing only small intervals.
        oracle = FibreOracle(73, interval_budget=1)
        for z, indices in denominator_buckets(self.graphs[73]).items():
            self.assertEqual(oracle.fibre(z), {self.graphs[73][i] for i in indices})

    def test_unused_labels_and_padic_exclusions(self):
        p = 13
        oracle = FibreOracle(p)
        buckets = denominator_buckets(self.graphs[p])
        for z in range(-2 * p, 2 * p + 1):
            if z:
                self.assertEqual(oracle.fibre(z), {self.graphs[p][i] for i in buckets.get(z, [])})
        for z in (-p * p, p * p, 17 * p * p):
            self.assertEqual(oracle.fibre(z), set())

    def test_constant_candidate_bounds_without_any_factorization(self):
        for p, vertices in self.graphs.items():
            oracle, t = FibreOracle(p), (p - 1) // 4
            with patch.object(oracle, "factor", side_effect=AssertionError("must not factor")):
                for z, indices in denominator_buckets(vertices).items():
                    expected = {vertices[i] for i in indices}
                    if z % p and (z < 0 or z > 2 * t):
                        self.assertEqual(oracle.fibre(z), expected)
                        self.assertLessEqual(len(expected), 2)
                        self.assertLessEqual(sum(v[0] < 0 for v in expected), 1)
                        if z < 0 or z >= p:
                            self.assertLessEqual(len(expected), 1)
                    elif z % p == 0 and (4 * (z // p) - 1) % p:
                        self.assertEqual(oracle.fibre(z), expected)
                        self.assertLessEqual(len(expected), 2)
                        if abs(z // p) >= 2 * t:
                            self.assertLessEqual(len(expected), 1)
        # A nontrivial Type II collision is not necessarily the forced 4m ratio.
        p, m = 6089, -60
        expected = {(1516, p * m, p * 5685), (1515, p * m, -p * 404)}
        expected = {tuple(sorted(v)) for v in expected}
        self.assertEqual(FibreOracle(p).fibre(p * m), expected)
        self.assertEqual(independent_fibre(p, p * m), expected)

    def test_shortest_paths_and_actual_sterile_components(self):
        for p, vertices in self.graphs.items():
            expected = seed_path(p, vertices)
            result = explore(FibreOracle(p))
            self.assertEqual(result.status, "FOUND")
            self.assertEqual(len(result.path), len(expected))
            self.assertEqual(result.path[0], seed(p))
            for vertex in result.path:
                self.assertIn(vertex, vertices)
                self.assertEqual(sum((Fraction(1, x) for x in vertex), Fraction()), Fraction(4, p))
            for before, after in zip(result.path, result.path[1:]):
                self.assertTrue(set(before) & set(after))
            for component in components(vertices):
                if any(v[0] > 0 for v in component):
                    continue
                result = explore(FibreOracle(p), component[0])
                self.assertEqual(result.status, "STERILE")
                self.assertIsNone(result.path)
                self.assertEqual(result.visited, len(component))
                self.assertEqual(result.expanded, len({z for v in component for z in v}))
        # Includes a nontrivial cycle, so exhaustion must not assume a forest.
        p = 10477
        component = next(c for c in components(signed_solutions(p)) if len(c) == 9 and all(v[0] < 0 for v in c))
        result = explore(FibreOracle(p), component[0])
        self.assertEqual((result.status, result.visited), ("STERILE", 9))

    def test_complete_three_move_regression(self):
        p = 297049
        result = explore(FibreOracle(p))
        self.assertEqual(result.status, "FOUND")
        self.assertEqual(len(result.path), 4)
        self.assertEqual(len(result.path), len(seed_path(p, signed_solutions(p))))
        self.assertGreater(result.path[-1][0], 0)

    def test_large_intervals_and_outer_fibres_need_no_factorization(self):
        p = 2271767935369
        t = (p - 1) // 4
        oracle = FibreOracle(p)
        with patch.object(oracle, "factor", side_effect=AssertionError("must not factor")):
            # The two huge Type I axis buckets have only a=0 in their
            # provably complete intervals; this is not a guessed height cap.
            for h in (-t * t, t * t):
                vertex = tuple(sorted((t, p * (p * h - t), -p * t + t * t // h)))
                self.assertEqual(oracle.fibre(p * (p * h - t)), {vertex})
            self.assertEqual(oracle.fibre(-2 * p * t), {seed(p)})
            # The universal middle bridge has a huge negative p-free anchor.
            vertex = tuple(sorted((t, -t * (p + 1), -p * t * (p + 1))))
            self.assertEqual(oracle.fibre(-t * (p + 1)), {vertex})

    def test_cached_certificates_are_immutable_and_starts_integral(self):
        oracle = FibreOracle(73)
        certificate = oracle.fibre(18)
        self.assertIsInstance(certificate, frozenset)
        # Caller filtering/consumption cannot silently turn a complete fibre
        # into a false empty one for the subsequent component search.
        with self.assertRaises(AttributeError):
            certificate.clear()
        copied = set(certificate)
        copied.clear()
        self.assertEqual(oracle.fibre(18), certificate)
        self.assertEqual(explore(oracle).status, "FOUND")
        for vertex in ((Fraction(5, 2), 5, 5), (2.5, 5, 5)):
            with self.assertRaises(ValueError):
                explore(FibreOracle(5), vertex)
        for operation in (lambda: FibreOracle(73.0),
                          lambda: FibreOracle(73, max_fibre=1.5),
                          lambda: oracle.fibre(Fraction(1, 2)),
                          lambda: oracle.factor(25.0),
                          lambda: explore(oracle, max_vertices=1.5)):
            with self.assertRaises(ValueError):
                operation()

    def test_limits_are_unknown_never_sterile(self):
        with self.assertRaises(IncompleteSearch):
            explore(FibreOracle(73), max_vertices=1)
        oracle = FibreOracle(73, max_divisors=1)
        with self.assertRaises(IncompleteSearch):
            oracle.fibre(18)
        self.assertNotIn(18, oracle._cache)
        oracle = FibreOracle(73, max_fibre=1)
        with self.assertRaises(IncompleteSearch):
            oracle.fibre(18)
        self.assertNotIn(18, oracle._cache)
        with self.assertRaises(IncompleteSearch):
            FibreOracle(73).factor(2**64 + 1)
        oracle = FibreOracle(73)
        with patch("pointwise_fibres.factorint", return_value={25: 1}):
            with self.assertRaises(IncompleteSearch):
                oracle.factor(25)
        for p in (1, 9, 73 * 73, 2**64 + 1):
            with self.assertRaises(ValueError):
                FibreOracle(p)
        for operation in (lambda: FibreOracle(73, interval_budget=0),
                          lambda: FibreOracle(73).fibre(0),
                          lambda: explore(FibreOracle(73), (1, 2, 3)),
                          lambda: explore(FibreOracle(73), max_vertices=0)):
            with self.assertRaises(ValueError):
                operation()


if __name__ == "__main__":
    unittest.main(verbosity=2)
