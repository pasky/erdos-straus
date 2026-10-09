"""O109 (POINTWISE_TYPEI7.md §3): fixed-(c',g) families of fibre certificates at high level.

For fixed odd c' (7 ∤ c') and odd g, TYPEI4 (1.2) with D = 4P_1X − g becomes

    P_1 · (8c'gX − 1) = 2^{L−4}·7^s + c'g²,      s = a + 2b, a odd,                       (3.1)

with 7^{a+b} | D, D > 0, X odd, 7 ∤ P_1X.  F = 8c'Xg − 1, e = 8c'Xh − 1, h = g + 2D.
For each solution print v_2(F+9), v_2(e+9) and t_min = 2 + ceil(L/2).
Usage: typei7_family.py CGMAX LMIN LMAX SMAX   (c'g² ≤ CGMAX)
"""
import sys
from sympy import factorint, divisors


def v2(x):
    x = abs(x)
    return (x & -x).bit_length() - 1


def main():
    CG, LMIN, LMAX, SMAX = map(int, sys.argv[1:5])
    nsol = 0
    best = []
    for cp in range(1, CG + 1, 2):
        if cp % 7 == 0:
            continue
        for g in range(1, CG + 1, 2):
            if cp * g * g > CG:
                break
            for L in range(LMIN, LMAX + 1):
                for s in range(1, SMAX + 1, 2):
                    Z = (1 << (L - 4)) * 7**s + cp * g * g
                    for Qp in divisors(Z):
                        if (Qp + 1) % (8 * cp * g):
                            continue
                        X = (Qp + 1) // (8 * cp * g)
                        P1 = Z // Qp
                        if X % 2 == 0 or X % 7 == 0 or P1 % 7 == 0:
                            continue
                        D = 4 * P1 * X - g
                        if D <= 0:
                            continue
                        v7 = 0
                        while D % 7**(v7 + 1) == 0:
                            v7 += 1
                        for a in range(1, s + 1, 2):
                            b = (s - a) // 2
                            if a + b > v7:
                                continue
                            delta = D // 7**(a + b)
                            h = g + 2 * D
                            F = 8 * cp * X * g - 1
                            e = 8 * cp * X * h - 1
                            N = 1 + (1 << (L + 2)) * cp * 7**(a + 2 * b) * X * X
                            assert F * e == N and F % 16 == 7
                            tmin = 2 + (L + 1) // 2
                            cl = max(v2(F + 9), v2(e + 9))
                            nsol += 1
                            print(L, s, a, b, cp, g, delta, P1, X, F, e, v2(F + 9), v2(e + 9), tmin,
                                  "HIT" if cl >= tmin else "", flush=True)
    print("solutions", nsol, file=sys.stderr)


if __name__ == "__main__":
    main()
