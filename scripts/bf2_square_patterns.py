"""O163 exploration: solutions of 4/n = 1/x+1/y+1/z for odd squares n.

For each solution and each coordinate divisible by n (the "x" slot), record
g_y = gcd(n, y), g_z = gcd(n, z) and g = gcd(n, x/n, y, z) (the common factor
that a descent n -> n/g could remove).  Question: is "n | x and gcd(n, y, z) = 1"
already impossible for odd squares (a stronger form of ET Prop 1.6)?
"""
from fractions import Fraction
from math import gcd, isqrt
import sys


def solutions(n):
    """All (x, y, z), x <= y <= z, with 4/n = 1/x + 1/y + 1/z."""
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r1 = Fraction(4, n) - Fraction(1, x)
        if r1 <= 0:
            continue
        ylo = max(x, int(1 / r1) + 1)
        yhi = int(2 / r1)
        for y in range(ylo, yhi + 1):
            r2 = r1 - Fraction(1, y)
            if r2 <= 0:
                continue
            if r2.numerator == 1 and r2.denominator >= y:
                out.append((x, y, r2.denominator))
    return out


def main(mmax):
    for m in range(3, mmax + 1, 2):
        n = m * m
        pats = {}
        for sol in solutions(n):
            for i in range(3):
                if sol[i] % n:
                    continue
                x = sol[i]
                y, z = [sol[j] for j in range(3) if j != i]
                key = (gcd(n, y), gcd(n, z))
                key = tuple(sorted(key))
                g = gcd(gcd(n, x // n), gcd(y, z))
                pats.setdefault(key, []).append((x, y, z, g))
        bad = {k: v for k, v in pats.items() if k[0] == 1}
        print(f"n={n}: patterns (gcd(n,y),gcd(n,z)) -> count:",
              {k: len(v) for k, v in sorted(pats.items())},
              " with some gcd=1:", {k: v[:2] for k, v in bad.items()})
        sys.stdout.flush()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 21)
