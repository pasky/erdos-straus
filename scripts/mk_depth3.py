"""O202: check Q_1 = 4mu-1-4n, Q_2 = 4n, Q_3 = 4tj-1 (mu = t+nj, 1<=t<=n) for mu > 2n, that depth-3 hits are
exactly the B = 1 points, and that no hit has n | lam (RD subfamily) when n = 1 mod 4.
Usage: mk_depth3.py MU n [n ...]"""
import sys
from math import isqrt
from mk_depth import hits

MU = int(sys.argv[1])
for n in map(int, sys.argv[2:]):
    nh = nb1 = 0
    for mu in range(2 * n + 1, MU + 1):
        N = 4 * (mu * mu - n)
        a0 = isqrt(N)
        m, d, a, Q = 0, 1, a0, []
        for _ in range(3):
            m = d * a - m; d = (N - m * m) // d; a = (a0 + m) // d; Q.append(d)
        t = mu % n or n
        j = (mu - t) // n
        assert Q == [4 * mu - 1 - 4 * n, 4 * n, 4 * t * j - 1], (n, mu, Q)
        for (k, D, A, B) in hits(n, mu):
            nh += 1
            assert (k == 3) == (B == 1 or B == 4 * mu * j - 1), (n, mu, k, B)
            nb1 += B == 1
            if n % 4 == 1:
                assert (mu // D) % n != 0, (n, mu, D)
    print(f"n={n}: mu in (2n, {MU}]: Q1..Q3 formula ok, {nh} hit-branches, {nb1} with B=1 (all at k=3), no n|lam")
