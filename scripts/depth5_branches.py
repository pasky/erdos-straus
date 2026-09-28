"""Certificates for the sieve branches of DEPTH3.md Theorem 3 (distance <= 2 and <= 5).

uv run python scripts/depth5_branches.py LO HI

For every prime p=4t+1 in [LO,HI) this checks the elementary sufficient
branches used in Theorem 3. Each success is turned into an explicit path
from the seed, and every vertex and edge is verified with exact rationals.

  H(h), h|36, h|t^2 : ph-t has a prime factor l = -1/4 (mod 4h-1)
                      -> seed, (t, p(ph-t), -t(ph-t)/h), positive     [2 edges]
  X(d), d|36, d|t^2 : t+d has a prime factor l = -1/4 (mod 4d-1)
                      -> seed, B1, B2, (2t,2t,-pt), (t+d,-pt,t(t+d)/d), positive  [5 edges]
  X2(1), p=2 (mod 3): Type II exit at t+1 with D=1 (forced)           [5 edges]

It reports primes where no branch applies (the sieve's exceptional set, which
is a superset of {dist>5}), and the counts per residue class of p mod 24.
"""
from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction

from sympy import factorint, primerange


def check_path(p, path):
    for v in path:
        assert all(v) and sum(Fraction(1, z) for z in v) == Fraction(4, p), v
    for u, v in zip(path, path[1:]):
        assert set(u) & set(v), (u, v)
    assert min(path[-1]) > 0 and all(min(v) < 0 for v in path[:-1])
    return len(path) - 1


def branches(p):
    t = (p - 1) // 4
    seed = (t, -2 * p * t, -2 * p * t)
    bridge = [seed, (t, -t * (p + 1), -p * t * (p + 1)), (2 * t, 2 * t + 1, -p * t * (p + 1)),
              (2 * t, 2 * t, -p * t)]
    out = []
    for h in (1, 2, 3, 4, 6, 9, 12, 18, 36):
        if (t * t) % h:
            continue
        m, K = p * h - t, 4 * h - 1
        target = (-pow(4, -1, K)) % K
        for ell in factorint(m):
            if ell % K == target:
                D = ell  # D=-h mod K since -h = -1/4 mod K
                y, z = (m + D) // K, (m + m * m // D) // K
                path = [seed, (t, p * m, -t * m // h), (p * m, y, z)]
                out.append(("H", h, check_path(p, path)))
                break
    for d in (1, 2, 3, 4, 6, 9, 12, 18, 36):
        if (t * t) % d:
            continue
        x, K = t + d, 4 * d - 1
        target = (-pow(4, -1, K)) % K
        anchor = (x, -p * t, t * x // d)
        for ell in factorint(x):
            if ell % K == target:
                D = ell
                P = (x, (p * p * D + p * x) // K, (x * x // D + p * x) // K)
                out.append(("X", d, check_path(p, bridge + [anchor, P])))
                break
    if p % 3 == 2:
        x, K = t + 1, 3
        P = (x, p * (x + 1) // K, p * (x + x * x) // K)
        out.append(("X2", 1, check_path(p, bridge + [(x, -p * t, t * x), P])))
    return out


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    fail, fail2, tot = Counter(), Counter(), Counter()
    for p in primerange(max(lo, 13), hi):
        if p % 4 != 1:
            continue
        b = branches(p)
        tot[p % 24] += 1
        if not any(x[0] == "H" for x in b):
            fail2[p % 24] += 1
        if not b:
            fail[p % 24] += 1
            print("no branch:", p, flush=True)
    print("primes by p mod 24:", dict(tot))
    print("no H-branch (superset of dist>2 among branch-tested):", dict(fail2))
    print("no branch at all (superset of dist>5):", dict(fail))


if __name__ == "__main__":
    main()
