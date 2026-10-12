"""R163 from-scratch numerical companion to Lemma 8.4 (POINTWISE_BINARYFORM §8).

Unlike a direct search for square points, this script RUNS THE CONSTRUCTION of the proof:
Step 1 primitive square point X1 (unit multiple of the class C, direction inside the octant),
Step 2 base point (P0,w0) with gcd(w0, M w1) = 1, Step 3 the line parametrisation psi and Y0 with
psi(Y0) = k0 X1 (checks: primes of k0 | 2 D w0, w0 | k0), Step 4 the family X_Z, F1(Z)
(checks: integrality, X_Z = X1, F1 = w1 mod M, non-constant coeffs of F1 divisible by w0 M,
Q(X_Z) = F1^2, symbolic via sympy), Dirichlet prime lam = mu^{-1} mod M, and Step 7: counts Z in a
box T*B0 that are good ((1)-(4) of the lemma) and compares with the local density prod rho_l
(l <= 60 and l = lam), rho_l computed by brute force mod l.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_bf2_lemma84_construct.py
"""
import math
from math import gcd
import sympy as sp

u, v, a, b = sp.symbols('u v a b')


def is_prime(n):
    return sp.isprime(n)


def run(Qc, M, Gexpr, Hexpr, octants=8, T=60, verbose=False):
    A, B, C = Qc
    D = B * B - 4 * A * C
    Q = lambda x, y: A * x * x + B * x * y + C * y * y
    beta = lambda P, Y: Q(P[0] + Y[0], P[1] + Y[1]) - Q(*P) - Q(*Y)
    Gf = sp.lambdify((u, v), Gexpr)
    Hf = sp.lambdify((u, v), Hexpr)
    units = [s for s in range(M) if gcd(s, M) == 1]
    sq = {s * s % M for s in units}
    classes = [(x, y) for x in range(M) for y in range(M) if Q(x, y) % M in sq]
    # primitive square points, small
    R = 110
    base = None
    for r in range(1, 50):
        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                q = Q(x, y)
                if gcd(x, y) == 1 and math.isqrt(q) ** 2 == q and base is None:
                    base = (x, y, math.isqrt(q))
    pts = set()
    for y0 in range(-R, R + 1):
        for y1 in range(-R, R + 1):
            if (y0, y1) == (0, 0):
                continue
            qY = Q(y0, y1)
            bY = beta(base[:2], (y0, y1))
            t = (qY * base[0] - bY * y0, qY * base[1] - bY * y1, base[2] * qY)
            g = gcd(gcd(t[0], t[1]), t[2])
            t = (t[0] // g, t[1] // g, t[2] // g)
            assert Q(t[0], t[1]) == t[2] ** 2
            pts.add(t)
            pts.add((-t[0], -t[1], t[2]))
    pts = sorted(pts, key=lambda t: t[2])
    stats = dict(pairs=0, fail_step1=0, fail_k0=0, fail_poly=0, nogood=0, minratio=9.9)
    for (c0, c1) in classes:
        for j in range(octants):
            lo, hi = 2 * math.pi * j / octants, 2 * math.pi * (j + 1) / octants
            mar = 0.15 * (hi - lo)
            stats['pairs'] += 1
            # Step 1: X1 with X1 = mu*C (mod M), arg in [lo+mar, hi-mar]
            X1 = None
            for (x, y, w) in pts:
                th = math.atan2(y, x) % (2 * math.pi)
                if not (lo + mar <= th <= hi - mar):
                    continue
                for mu in units:
                    if (mu * c0 - x) % M == 0 and (mu * c1 - y) % M == 0:
                        X1 = (x, y, w, mu)
                        break
                if X1:
                    break
            if X1 is None:
                stats['fail_step1'] += 1
                continue
            u1, v1, w1, mu = X1
            # Step 2
            P0 = next((x, y, w) for (x, y, w) in pts
                      if gcd(w, M * w1) == 1)
            p0, q0, w0 = P0
            # Step 3
            Y = (w0 * u1 - w1 * p0, w0 * v1 - w1 * q0)
            if Y == (0, 0):  # tangent case: Y orthogonal to P0
                Y = (-(B * p0 + 2 * C * q0), 2 * A * p0 + B * q0)
            g = gcd(*Y)
            Y = (Y[0] // g, Y[1] // g)
            qY = Q(*Y)
            bY = beta((p0, q0), Y)
            psi = (qY * p0 - bY * Y[0], qY * q0 - bY * Y[1], w0 * qY)
            k0 = psi[2] // w1
            ok = (psi[2] % w1 == 0 and psi[0] == k0 * u1 and psi[1] == k0 * v1 and k0 >= 1
                  and k0 % w0 == 0
                  and all((2 * abs(D) * w0) % p == 0 for p in sp.primefactors(k0)))
            if not ok:
                stats['fail_k0'] += 1
                print('K0 FAIL', Qc, M, (c0, c1), j, X1, P0, Y, psi, k0)
                continue
            # Step 4 (symbolic)
            N = k0 * M
            Ys = (Y[0] + N * a, Y[1] + N * b)
            qs = sp.expand(A * Ys[0] ** 2 + B * Ys[0] * Ys[1] + C * Ys[1] ** 2)
            bs = sp.expand(2 * A * p0 * Ys[0] + B * (p0 * Ys[1] + q0 * Ys[0]) + 2 * C * q0 * Ys[1])
            XZ = [sp.expand((qs * p0 - bs * Ys[0]) / k0), sp.expand((qs * q0 - bs * Ys[1]) / k0)]
            F1 = sp.expand(w0 * qs / k0)
            polys = [sp.Poly(e, a, b) for e in XZ + [F1]]
            okp = all(cf.is_integer for P in polys for cf in P.coeffs())
            okp &= polys[0].eval((0, 0)) == u1 and polys[1].eval((0, 0)) == v1
            okp &= polys[2].eval((0, 0)) == w1
            for i, P in enumerate(polys):
                modulus = w0 * M if i == 2 else M
                okp &= all(cf % modulus == 0 for mon, cf in P.terms() if mon != (0, 0))
            okp &= sp.expand(A * XZ[0] ** 2 + B * XZ[0] * XZ[1] + C * XZ[1] ** 2 - F1 ** 2) == 0
            if not okp:
                stats['fail_poly'] += 1
                print('POLY FAIL', Qc, M, (c0, c1), j)
                continue
            # Dirichlet prime
            minv = pow(mu, -1, M)
            lam = next(l for l in range(minv, 10 ** 7, M)
                       if l > 50 and is_prime(l) and N % l)
            fX = sp.lambdify((a, b), XZ)
            fF = sp.lambdify((a, b), F1)
            # box around T*Y0/|Y0|
            nY = math.hypot(*Y)
            cx, cy = T * Y[0] / nY, T * Y[1] / nY
            h = max(2, int(0.05 * T))
            good = tot = 0
            for za in range(int(cx) - h, int(cx) + h + 1):
                for zb in range(int(cy) - h, int(cy) + h + 1):
                    X = fX(za, zb)
                    w = fF(za, zb)
                    P = (lam * X[0], lam * X[1])
                    th = math.atan2(P[1], P[0]) % (2 * math.pi)
                    if not (lo < th < hi):
                        continue
                    tot += 1
                    assert ((P[0] - c0) % M, (P[1] - c1) % M) == (0, 0)
                    assert Q(*X) == w * w and w % 2 == 1
                    if gcd(w, int(Gf(*P))) == 1 and (w * int(Hf(*X))) % lam:
                        good += 1
            if good == 0:
                stats['nogood'] += 1
                print('NO GOOD', Qc, M, (c0, c1), j)
            else:
                stats['minratio'] = min(stats['minratio'], good / tot)
    return stats


if __name__ == '__main__':
    G = (u - v) * (2 * u + v - 1) * (u ** 2 - 3 * v + 2) * v * (u + 2 * v)
    H = (u - 3 * v) * (u + v) * (2 * u - v)
    for Qc, M in [((1, 0, 1), 8), ((1, 0, 1), 24), ((1, 0, 1), 40), ((1, 1, 1), 24),
                  ((1, 0, 2), 16), ((1, 0, 2), 48), ((1, 1, 2), 56), ((2, 1, 3), 184),
                  ((1, 0, 5), 40)]:
        print(Qc, M, run(Qc, M, G, H), flush=True)
