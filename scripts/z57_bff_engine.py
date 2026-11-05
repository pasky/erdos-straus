#!/usr/bin/env python3
"""z57 BFF engine: enumerate (*) solutions p = 4 n m C - n - m via the 'defect' form.

For d = 3 (mod 4) put n_d := d - (p mod d) in [1, d-1].  HIT(d) <=> 4 n_d | d + 1.
Then m = (p + n_d)/d, C = (d+1)/(4 n_d) and (n_d, m, C) is a solution; conversely every
solution (n, m, C) arises from d = 4nC - 1 (and from d' = 4mC - 1).  G* membership:
max(n,m)^4 > min(n,m) * p.  Every solution has min(4nC-1, 4mC-1) <= p^{3/4}+O(1) when in G*
(see memo Lemma 1.3), so scanning d <= D with D >= that bound enumerates G* exactly.
"""
import sys, math
import numpy as np


def hits_by_d(p, D, chunk=1 << 22):
    """Return sorted set of solutions (n, m, C) found from d <= D, d = 3 (4)."""
    out = set()
    for start in range(3, D + 1, 4 * chunk):
        stop = min(D, start + 4 * chunk - 1)
        d = np.arange(start, stop + 1, 4, dtype=np.int64)
        r = p % d
        n = d - r
        ok = ((d + 1) % (4 * n)) == 0
        for dd, nn in zip(d[ok].tolist(), n[ok].tolist()):
            m = (p + nn) // dd
            C = (dd + 1) // (4 * nn)
            assert 4 * nn * m * C - nn - m == p
            out.add((min(nn, m), max(nn, m), C))
    return sorted(out)


def in_gstar(p, n, m):
    P, Q = min(n, m), max(n, m)
    return Q ** 4 > P * p


def dbound_gstar(p):
    # min(4nC-1, 4mC-1) <= p^{3/4} + p^{1/12} + 1 for G* solutions (Lemma 1.3); add slack
    return int(p ** 0.75 + p ** (1 / 12)) + 10


def gstar_solutions(p):
    sols = hits_by_d(p, dbound_gstar(p))
    return [s for s in sols if in_gstar(p, s[0], s[1])]


if __name__ == "__main__":
    for a in sys.argv[1:]:
        p = int(a)
        sols = gstar_solutions(p)
        print(p, len(sols), sols[:10])
