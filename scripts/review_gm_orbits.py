"""R201 from-scratch check of GROWING_MUTE Prop 1.2 / 2.2 / §4.2 (V_n : nA^2 + B^2 + D = 2 lam D A B).

Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_gm_orbits.py X n1 n2 ...
  For each n: enumerate points with A even, B odd, A,B <= X, gcd(A,B)=gcd(B,n)=1, g | nA^2+B^2, g = -1 (2AB);
  group by (lam, D); test n | lam, D mod 4, mu^2 - n square; apply the Pell automorph (u even) forwards and
  backwards and the B-involution, re-check every image as a V_n point; count squarefreeness loss.
Second mode:  ... nlam NMAX ABMAX  : count points with n | lam over ALL odd n <= NMAX (both residues mod 4).
"""
import sys
from math import gcd, isqrt
from sympy import divisors
from review_gm_dict import sqfree


SMALLP = [r for r in range(3, 1000, 2) if all(r % s for s in range(3, isqrt(r) + 1, 2))]


def points(n, X):
    out = []
    for A in range(2, X + 1, 2):
        for B in range(1, X + 1, 2):
            if gcd(A, B) != 1 or gcd(B, n) != 1:
                continue
            N = n * A * A + B * B
            for g in divisors(N):
                if (g + 1) % (2 * A * B) == 0:
                    out.append((A, B, (g + 1) // (2 * A * B), N // g))
    return out


def is_point(n, A, B, lam, D):
    g = 2 * A * B * lam - 1
    return (A > 0 and B > 0 and A % 2 == 0 and B % 2 == 1 and gcd(A, B) == 1 and gcd(B, n) == 1
            and g * D == n * A * A + B * B)


def pell(d):
    """Fundamental solution of T^2 - d u^2 = 1 (d > 0 non-square) by continued fractions."""
    a0 = isqrt(d)
    m, q, a = 0, 1, a0
    p0, p1, q0, q1 = 1, a0, 0, 1
    while p1 * p1 - d * q1 * q1 != 1:
        m = a * q - m
        q = (d - m * m) // q
        a = (a0 + m) // q
        p0, p1 = p1, a * p1 + p0
        q0, q1 = q1, a * q1 + q0
    return p1, q1


def main(X, ns):
    for n in ns:
        P = points(n, X)
        groups = {}
        for A, B, lam, D in P:
            groups.setdefault((lam, D), []).append((A, B))
        nB1 = sum(1 for p in P if p[1] == 1)
        nsq = sum(1 for p in P if sqfree(p[1]))
        nlam = sum(1 for p in P if p[2] % n == 0)
        Dbad = sum(1 for p in P if p[3] % 4 != 3)
        sq_mu = 0
        orbit_ok = orbit_sqf_lost = binv_ok = 0
        for A, B, lam, D in P:
            mu = lam * D
            d = mu * mu - n
            assert d > 0
            if isqrt(d) ** 2 == d:
                sq_mu += 1
                continue
            T, u = pell(d)
            if u % 2:
                T, u = T * T + d * u * u, 2 * T * u
            for sgn in (1, -1):  # forward automorph and its inverse
                a, b = A, B
                for _ in range(3):
                    a, b = (T + mu * u * sgn) * a - u * sgn * b, n * u * sgn * a + (T - mu * u * sgn) * b
                    assert is_point(n, a, b, lam, D), (n, A, B, lam, D, a, b)
                    orbit_ok += 1
                    if sqfree(B) and any(b % (r * r) == 0 for r in SMALLP):
                        orbit_sqf_lost += 1
            assert is_point(n, A, 2 * mu * A - B, lam, D)
            binv_ok += 1
        print(f'n={n} X={X}: points {len(P)} (B=1: {nB1}, B squarefree: {nsq}); (lam,D) groups {len(groups)}, '
              f'max pts/group {max((len(v) for v in groups.values()), default=0)}; n|lam: {nlam}; D!=3(4): {Dbad}; '
              f'mu^2-n square: {sq_mu}; automorph images checked {orbit_ok} (sqfree B -> divisible by r^2, r<1000 prime: {orbit_sqf_lost}); '
              f'B-involution ok {binv_ok}')
        if len(P) <= 8:
            print('   ', P)


def nlam_mode(NMAX, X):
    hits = tot = 0
    for n in range(3, NMAX + 1, 2):
        for A, B, lam, D in points(n, X):
            tot += 1
            hits += lam % n == 0
    print(f'all odd n <= {NMAX}, A,B <= {X}: {tot} points, n | lam in {hits}')


if __name__ == '__main__':
    if sys.argv[1] == 'nlam':
        nlam_mode(int(sys.argv[2]), int(sys.argv[3]))
    else:
        main(int(sys.argv[1]), [int(a) for a in sys.argv[2:]])
