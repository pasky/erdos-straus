"""O251 (LATTICE_MEETING §1): the d = 1 meeting locus of ASTRA_BRIDGE Thm 3.4 is the finite set
  {(a, b, k) : a + b = k (4ab - p)}  <=>  {(a, g) : g | p + 4a^2, g = -1 (mod 4a)}   (Lemma 1.1 there).
Every unordered {a, b} has min(a, b) <= A := isqrt(p) + 2 (proof in LATTICE_MEETING §1), so the a-scan below is
EXHAUSTIVE.  For each prime p = 1 (4) <= P: count meeting points (ordered (a, g)); list primes with none.
Each found point is checked exactly: 4/p = 1/(ab) + 1/(pka) + 1/(pkb).
T1 control: odd squares n = c^2 <= P (with the same scan, n in place of p) must have none.
Usage: z23_meet.py P [full]   (full: exhaustive count for all p; else quick k<=8 test then exhaustive for failures)
"""
import sys
import numpy as np
from fractions import Fraction as F
from math import isqrt
from sympy import primerange


def meet_points(n, stop_first=False):
    pts = []
    A = isqrt(n) + 2
    for a in range(1, A + 1):
        N = n + 4 * a * a
        J = (N + 1) // (4 * a)
        g = 4 * a * np.arange(1, J + 1, dtype=np.int64) - 1
        for gg in g[N % g == 0].tolist():
            m = N // gg
            assert (n + m) % (4 * a) == 0
            b = (n + m) // (4 * a)
            assert (a + b) % m == 0
            k = (a + b) // m
            assert F(4, n) == F(1, a * b) + F(1, n * k * a) + F(1, n * k * b)
            pts.append((a, b, k, gg, m))
            if stop_first:
                return pts
    return pts


def quick(n, KM=8):
    for k in range(1, KM + 1):
        N = 4 * k * k * n + 1
        J = (isqrt(N) + 1) // (4 * k) + 1
        g = 4 * k * np.arange(1, J + 1, dtype=np.int64) - 1
        if np.any(N % g == 0):
            return True
    return False


if __name__ == '__main__':
    P = int(sys.argv[1])
    full = len(sys.argv) > 2
    empty, counts, nprimes = [], [], 0
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        nprimes += 1
        if full:
            c = len(meet_points(p))
            counts.append(c)
            if c == 0:
                empty.append(p)
        elif not quick(p) and not meet_points(p, True):
            empty.append(p)
    print('primes p=1(4) <=', P, ':', nprimes, ' empty d=1 meeting locus:', len(empty))
    print('first empties:', empty[:40])
    for lo, hi in [(0, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 10**7)]:
        e = sum(lo < q <= hi for q in empty)
        print('  empties in (%d,%d]: %d' % (lo, hi, e))
    if full:
        print('mean count', np.mean(counts), 'min', min(counts))
    t1 = [c * c for c in range(3, isqrt(P) + 1, 2) if meet_points(c * c, True)]
    print('odd squares with a meeting point (must be none):', t1)
