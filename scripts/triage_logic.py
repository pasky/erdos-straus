"""Small, independent counterexample/identity checks for O157 logic triage.
Run with a memory limit, timeout, and one core; no campaign solvers imported.
"""
from fractions import Fraction
from math import gcd, isqrt

import sympy as sp


def phi(d, a, b, e):
    return ((a + b) % e == 0 and (d + e) % (4 * a) == 0
            and (d + e) % b == 0 and gcd(a, b) == 1)


# The memo's CRT substitution loses a factor at 2.
for d in (1, 9, 17, 25):
    assert phi(d, 1, 2, 3)
    assert (d + 3) % 8 != 0
    print(f"raw Phi_{d}(1,2,3): true; 4ab divisibility: false")
assert (4 * 1 - 1) * (4 * 2 - 1) > 4 * 1 + 1
print("D1's claimed product bound also fails at d=1, a=1, b=2, e=3")

# Prescribed-target membership does not require full group coverage.
e, n = 19, 113
p = 4 * n - e
assert all(p % q for q in range(2, isqrt(p) + 1))
ratios = {a * pow(b, -1, e) % e
          for a in range(1, n + 1) if n % a == 0
          for b in range(1, n // a + 1) if n % (a * b) == 0}
assert ratios == {1, 18}
assert len(ratios) < sum(gcd(r, e) == 1 for r in range(e))
a, b, c, d = 113, 1, 6, 1
solution = (a * b * d, a * c * d * p, b * c * d * p)
assert sum((Fraction(1, x) for x in solution), Fraction()) == Fraction(4, p)
print(f"p={p}, e={e}, N={n}: ratio set {sorted(ratios)}; ES witness {solution}")

# The root construction and signed identity in Theorem S/C3 are exact.
s, r, q, z = sp.symbols("s r q z", nonzero=True)
n = (s / r - 1) * q
x, y = n * s / (2 * r), q * s / (4 * r)
assert sp.cancel(2 / x + 1 / y - 4 / n) == 0
x, y = z * (1 - z) / 2, (z - 1) / 4
assert sp.cancel(2 / x + 1 / y - 4 / z) == 0
print("Theorem S root identity and C3 signed identity: exact")
