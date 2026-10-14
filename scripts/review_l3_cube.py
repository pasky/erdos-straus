"""R205 from-scratch checks of LENGTH_THREE Cor 1.3, Thm 3.1 (Type II), Thm 4.1, Cor 4.2, §7.4.

Usage: PYTHONPATH=scripts uv run python scripts/review_l3_cube.py PMAX SQMAX
Independent of scripts/l3_*.py.
"""
import sys
from fractions import Fraction as F
from math import isqrt


def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def cube_points(n):
    """All (c,d,j) >= 1 with h = 4cdj - 1 | n j + c (brute force, bound via h | n + 4c^2 d)."""
    # bounds (valid for every n >= 1): h <= nj + c gives c(4d - 1) <= n + 1, so 3cd <= n + 1;
    # 4cd(nj + c) = (h + 1)n + 4c^2 d, so h | n + 4c^2 d and j <= (n + 4c^2 d + 1)/(4cd).
    out = []
    for c in range(1, n + 2):
        if 3 * c > n + 1:
            break
        for d in range(1, n + 2):
            if 3 * c * d > n + 1:
                break
            jmax = (n + 4 * c * c * d + 1) // (4 * c * d)
            for j in range(1, jmax + 1):
                if (n * j + c) % (4 * c * d * j - 1) == 0:
                    out.append((c, d, j))
    return out


def cf_PQ(D, K):
    """(P_k, Q_k), k = 0..K, for sqrt(D), plus convergents p_k, q_k."""
    a0 = isqrt(D)
    P, Q = 0, 1
    Ps, Qs, As = [P], [Q], []
    for _ in range(K + 1):
        a = (P + a0) // Q
        As.append(a)
        P = a * Q - P
        Q = (D - P * P) // Q
        Ps.append(P); Qs.append(Q)
    p, q = [As[0], As[0] * As[1] + 1], [1, As[1]]
    for k in range(2, K + 1):
        p.append(As[k] * p[-1] + p[-2]); q.append(As[k] * q[-1] + q[-2])
    return Qs, p, q


def main():
    PMAX = int(sys.argv[1]); SQMAX = int(sys.argv[2])
    nc = nd1 = 0
    fails = []
    for p in primes(PMAX):
        if p < 5:
            continue
        for c, d, j in cube_points(p):
            nc += 1
            h = 4 * c * d * j - 1
            s = (p * j + c) // h
            m, N = 4 * d * j, p * j
            hp = m * s - 1
            if m * c * s - c - s != N:
                fails.append(("K", p, c, d, j))
            if h * s != N + c or h * hp != m * N + 1 or c * hp != N + s:
                fails.append(("ptolemy", p, c, d, j))
            if (c + s) % j or h * ((c + s) // j) != p + 4 * c * c * d:
                fails.append(("e", p, c, d, j))
            if F(N, m) != F(p, 4 * d) or F(c * s) - F(N, m) != F(c + s, m):
                fails.append(("r2", p, c, d, j))
            # mirror point is a cube point with h' as its h
            if (p * j + s) % (4 * s * d * j - 1) or 4 * s * d * j - 1 != hp:
                fails.append(("mirror", p, c, d, j))
            # Thm 4.1 generic: m^2 Norm_mu(1/m + z) = hh' - m mu, at mu_c, mu_s
            for mu, val in ((N + c, -h), (N + s, -hp)):
                nm = m * m * (F(1, m * m) - F(mu, m) + F(N, m))
                if nm != h * hp - m * mu or nm != val or mu % (-val):
                    fails.append(("norm", p, c, d, j, mu))
            # general d: V_{pd} point (A,B)=(2j,1), D = 2 mu A - pd A^2 - 1 at mu = d*mu_s should be h'
            mu = d * (N + s)
            A = 2 * j
            if 2 * mu * A - p * d * A * A - 1 != hp or mu != c * d * hp:
                fails.append(("Vpd", p, c, d, j))
            if d == 1:
                nd1 += 1
                mu = N + c
                # omega = -mu + sqrt(mu^2 - p); 1 + 2j omega = (1 - 2 j mu) + j sqrt(4mu^2 - 4p)
                x, y, Dd = 1 - 2 * j * mu, j, 4 * mu * mu - 4 * p
                if x * x - Dd * y * y != -h:
                    fails.append(("eps", p, c, j))
                Qs, pp, qq = cf_PQ(Dd, 4)
                k = 3 if j >= 2 else 1
                if (mu > 2 * p) != (j >= 2):
                    fails.append(("mu2p", p, c, j))
                if Qs[k] != h or pp[k - 1] != 2 * mu * j - 1 or qq[k - 1] != j:
                    fails.append(("cf", p, c, j, Qs[:5]))
    # §7.4: no cube point at odd squares (and the Jacobi argument per point if any)
    sqpts = 0
    for M in range(3, isqrt(SQMAX) + 1, 2):
        sqpts += len(cube_points(M * M))
    print(f"cube points p<={PMAX}: {nc} (d=1: {nd1}); fails={len(fails)} {fails[:5]}")
    print(f"cube points at odd squares 9..{SQMAX}: {sqpts}")


if __name__ == "__main__":
    main()
