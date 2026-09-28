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
  F2,   p=17 (mod 24): h=2, D=12 divides (7t+2)^2, 12=-2 (mod 7) (forced) [2 edges]
  F5/F7, p=1 (mod 24) and p a non-residue mod 5 or 7: forced (9) certificates
         p=3 (5): h=1,D=5; p=2 (5): h=2,D=5; p=3 (7): h=6,D=63;
         p=5 (7): h=3,D=63; p=6 (7): h=4,D=(4p-t)/14                   [2 edges]

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
    if p % 24 == 17:
        # t even, t = 1 (mod 3): m = 2p - t = 7t + 2 is divisible by 6, D = 12 = -2 (mod 7)
        m, K, D = 2 * p - t, 7, 12
        assert (m * m) % D == 0 and (D + 2) % K == 0
        path = [seed, (t, p * m, -t * m // 2), (p * m, (m + D) // K, (m + m * m // D) // K)]
        out.append(("F2", 2, check_path(p, path)))
    if p % 24 == 1:
        # Mordell-easy classes mod 5 and 7: forced (9)-certificates (h, D)
        forced = {5: {3: (1, 5), 2: (2, 5)}, 7: {3: (6, 63), 5: (3, 63), 6: (4, None)}}
        for ell, table in forced.items():
            if p % ell in table:
                h, D = table[p % ell]
                m, K = p * h - t, 4 * h - 1
                if D is None:
                    D = m // 14
                assert (m * m) % D == 0 and (D + h) % K == 0, (p, h, D)
                path = [seed, (t, p * m, -t * m // h), (p * m, (m + D) // K, (m + m * m // D) // K)]
                out.append(("F%d" % ell, h, check_path(p, path)))
    if p % 3 == 2:
        x, K = t + 1, 3
        P = (x, p * (x + 1) // K, p * (x + x * x) // K)
        out.append(("X2", 1, check_path(p, bridge + [(x, -p * t, t * x), P])))
    return out


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    fail, fail2, tot = Counter(), Counter(), Counter()
    bad840 = 0
    for p in primerange(max(lo, 13), hi):
        if p % 4 != 1:
            continue
        b = branches(p)
        tot[p % 24] += 1
        if p % 24 == 1 and (p % 840) not in (1, 121, 169, 289, 361, 529) and \
                not any(x[0] in ("H", "F5", "F7") for x in b):
            bad840 += 1
        if not any(x[0] in ("H", "F2", "F5", "F7") for x in b):
            fail2[p % 24] += 1
        if not b:
            fail[p % 24] += 1
            print("no branch:", p, flush=True)
    print("primes by p mod 24:", dict(tot))
    print("primes p=1 (24) outside Mordell's six classes mod 840 without a (9)-exit:", bad840)
    print("no H-branch (superset of dist>2 among branch-tested):", dict(fail2))
    print("no branch at all (superset of dist>5):", dict(fail))


if __name__ == "__main__":
    main()
