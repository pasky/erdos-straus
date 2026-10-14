"""fs_sum_check.py (O216): independent exact-integer re-implementation of the Case B pattern bounds of
FF_STERILE_PUSH Lemma 1.6 (written from the table, not from fs_sum.c), summed with exact rationals.
Prints per-s terms  sum_patterns mult * min_route(bound) * q^{1-ceil(s/2)}  for comparison with fs_sum.
usage: fs_sum_check.py r SMAX"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial
from functools import lru_cache


@lru_cache(maxsize=None)
def cop(n, D, rho):
    """least m+k with Delta(m,k) < (m+k+1) m D (Lemma 1.5), 0 if none with m <= 60, k <= 200"""
    X = D - rho
    best = 0
    for m in range(1, 61):
        for k in range(0, 201):
            if n * m * (m + 1) // 2 + X * (m * (m + 1) // 2 + k * m + k * (k + 1) // 2) < (m + k + 1) * m * D:
                best = m + k if not best else min(best, m + k)
                break
            if X * (m + k + 1) >= m * D:
                break
    return best


@lru_cache(maxsize=None)
def cls(n, d, rho, both):
    if d < 0 or d > n:
        return 0
    cands = [comb(n, d)]
    if d < rho or (both and n - d < rho):
        cands.append(1)
    else:
        if 3 * rho > n: cands.append(2)
        c = cop(n, d, rho)
        if c: cands.append(c)
        if both:
            c = cop(n, n - d, rho)
            if c: cands.append(c)
    return min(cands)


def run(r, SMAX):
    q = 3**r
    Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
    def Som(e):  # sum over monic v of degree e of 2^omega(v), exact rational q^e(2+(e-1)(1-1/q))
        return Fr(1) if e <= 0 else Fr(q**e) * (2 + (e - 1) * (1 - Fr(1, q)))
    out = []
    for s in range(3, SMAX + 1):
        acc = Fr(0)
        for a in range(1, s):
            for z in range(0, s - a):
                b = s - a - z
                if b < a: continue
                for y in range(0, b - 1):
                    t = b - y
                    W, WB, Z, Y, V = Ns(a - 1), Ns(b - 1), Ns(z), Ns(y), Ns(t - 2)
                    B = [Z * Y * W, Z * W * V, 2 * Y * V * Z, Y * V * W,
                         V * factorial(s - 2) // (factorial(z) * factorial(a - 1) * factorial(b - 1)),
                         Z * Y * cls(s + 2 * y + z, a + y + z, y + z + 1, 1),
                         W * Y * cls(s - 1 + y, a + y + z, a + y, 0),
                         Z * W * cls(s - 2, a + y + z, z + a, 1),
                         WB * Y * cls(s - 1 + y, b + y + z, b + y, 0),
                         Z * WB * cls(z + 2 * b - 2, b + y + z, z + b, 1),
                         V * W * cls(s - 1 - a, b - 1, t - 1, 1),
                         V * WB * cls(s - 1 - b, a - 1, t - 1, 1),
                         V * comb(s - 2, a - 1) * cls(s - 1 - a, b - 1, t - 1, 1),
                         V * comb(s - 2, b - 1) * cls(s - 1 - b, a - 1, t - 1, 1),
                         Y * V * comb(s - 2, a - 1), Y * V * comb(s - 2, b - 1),
                         Z * V * comb(a + b - 2, a - 1),
                         Z * 2 * Som(t - 2) * cls(a + b - 2, a - 1, t - 1, 1),
                         2 * Som(t - 2) * comb(s - 2, z) * cls(a + b - 2, a - 1, t - 1, 1)]
                    acc += (1 if a == b else 2) * min(B)
        out.append(acc * Fr(q)**(1 - (s + 1) // 2))
    return out


if __name__ == '__main__':
    r, S = int(sys.argv[1]), int(sys.argv[2])
    cum = Fr(0)
    for s, x in enumerate(run(r, S), start=3):
        cum += x
        print(f"s={s} term={float(x):.10e} cum={float(cum):.10e}")
