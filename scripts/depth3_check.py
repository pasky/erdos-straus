"""Quick regression checks for DEPTH3.md (finite checks; the theorems are proved in the text).

uv run python scripts/depth3_check.py
"""
from __future__ import annotations

import unittest
from math import gcd

from sympy import primerange

import depth3
import depth3_validate
import depth5_branches

KNOWN_DIST3 = [297049, 513529, 710089, 1083289, 1103449, 1708009, 2469289, 3389929, 3942409, 4762489]


class Depth3Checks(unittest.TestCase):
    def test_classification_matches_bfs_small(self):
        for p in primerange(13, 4000):
            if p % 4 == 1:
                self.assertTrue(depth3_validate.check(p)["ok"], p)

    def test_known_distance_three(self):
        for p in KNOWN_DIST3[:4]:
            r = depth3.Depth3(p).run()
            self.assertEqual(r["dist"], 3)
            self.assertEqual(r["hits"][0]["family"], "A")
            depth3.check_path(p, r["hits"][0]["path"])

    def test_rejects_composite(self):
        with self.assertRaises(ValueError):
            depth3.Depth3(9)
        with self.assertRaises(ValueError):
            depth3.Depth3(25)

    def test_forced_branches_and_mordell_classes(self):
        for p in primerange(13, 200000):
            if p % 4 != 1:
                continue
            b = depth5_branches.branches(p)  # every returned path is verified inside
            if (p % 840) not in (1, 121, 169, 289, 361, 529):
                self.assertTrue(any(x[2] == 2 for x in b), p)

    def test_forced_constant_edges_are_axes(self):
        # e=4ah-a-h | gcd(a,6)^2 with a,h nonzero forces |a|,|h|<=12
        for a in range(-12, 13):
            for h in range(-12, 13):
                if a and h:
                    e = 4 * a * h - a - h
                    self.assertNotEqual(gcd(a, 6) ** 2 % e if e else 1, 0, (a, h))


if __name__ == "__main__":
    unittest.main()
