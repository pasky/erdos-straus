"""O203 checks of COMPOSITION_ES §1.
(1) Thm 1.3: for odd n in [3, nmax] and n < mu <= Mf*n, brute-force all B = 1 V_n points at mu (A even up to 2mu)
    and compare with the single candidate A = 2j, D = 4tj - 1, mu = nj + t (1 <= t <= n). Also mu <= n: none.
(2) Prop 1.2(a): for random pairs of brute-force V_n points at the same mu, check the product formula and norm.
Usage: cp_law.py nmax Mf"""
import sys
import random
from math import gcd


def vn_points(n, mu, Amax):
    """brute force V_n points at mu with A <= Amax: D | mu, nA^2 + B^2 + D = 2 mu A B."""
    out = []
    for D in [d for d in range(1, mu + 1) if mu % d == 0]:
        for A in range(2, Amax + 1, 2):
            # B^2 - 2 mu A B + nA^2 + D = 0
            disc = mu * mu * A * A - n * A * A - D
            if disc < 0:
                continue
            r = int(disc ** 0.5)
            while r * r > disc:
                r -= 1
            while (r + 1) ** 2 <= disc:
                r += 1
            if r * r != disc:
                continue
            for B in (mu * A - r, mu * A + r):
                if B > 0 and B % 2 == 1 and gcd(A, B) == 1 and gcd(B, n) == 1:
                    out.append((A, B, D))
    return out


def main():
    nmax, Mf = map(int, sys.argv[1:3])
    bad = 0
    nes = 0
    for n in range(3, nmax + 1, 2):
        for mu in range(1, Mf * n + 1):
            brute = set()
            for A in range(2, 2 * mu + 2, 2):
                D = 2 * mu * A - n * A * A - 1
                if D > 0 and mu % D == 0 and gcd(D, n) == 1:
                    brute.add((A, D))
            if mu <= n:
                pred = set()
            else:
                t = mu % n or n
                j = (mu - t) // n
                D = 4 * t * j - 1
                pred = {(2 * j, D)} if mu % D == 0 else set()
                assert (mu % D == 0) == ((n + 4 * t * t) % D == 0)
            if brute != pred:
                bad += 1
                print("MISMATCH", n, mu, brute, pred)
            nes += len(brute)
    print("Thm 1.3: B=1 points", nes, "mismatches", bad)
    random.seed(1)
    checked = 0
    for n in range(3, 40, 2):
        for mu in range(n + 1, 4 * n):
            f = mu * mu - n
            P = vn_points(n, mu, 60)
            for _ in range(min(20, len(P) ** 2)):
                (A1, B1, D1), (A2, B2, D2) = random.choice(P), random.choice(P)
                A3 = A1 * B2 + A2 * B1 - 2 * mu * A1 * A2
                B3 = B1 * B2 - n * A1 * A2
                # alpha = (B - mu A) + A sqrt f
                x1, y1, x2, y2 = B1 - mu * A1, A1, B2 - mu * A2, A2
                x3, y3 = x1 * x2 + f * y1 * y2, x1 * y2 + x2 * y1
                assert (x3, y3) == (B3 - mu * A3, A3)
                assert B3 * B3 - 2 * mu * A3 * B3 + n * A3 * A3 == D1 * D2
                checked += 1
    print("Prop 1.2(a): products checked", checked)


if __name__ == "__main__":
    main()
