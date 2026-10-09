"""R108 from-scratch checks for EXCEPTIONAL_MN3 §3.

(1) brute-force Type I solutions of 4/p = 1/x+1/y+1/z (ordered, p|x, p∤y,z) and compare
    f_I(p) <= 2 * sum_c w_c(p)   (Thm 3.8 set-up)
(2) on every enumerated (a,c,d,f) point: Sigma^I_n identities, SL2 matrix, n = 2c M21 - M22,
    form [f,4ad,de] has disc -4d and is primitive, twin f' = 4bcd-n = (n^2+4c^2 d)/f
(3) the exponent table / R_bad / R** areas by exact polygon integration on a fine grid
"""
from fractions import Fraction as Fr
from math import gcd
from itertools import permutations
from sympy import primerange


def solutions(n):
    sols = set()
    four = Fr(4, n)
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        r = four - Fr(1, x)
        if r <= 0:
            continue
        ylo = max(x, int(1 / r) + 1)
        yhi = int(2 / r) + 1
        for y in range(ylo, yhi + 1):
            s = r - Fr(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                z = s.denominator
                for t in set(permutations((x, y, z))):
                    sols.add(t)
    return sols


def fI(p):
    return sum(1 for (x, y, z) in solutions(p) if x % p == 0 and y % p and z % p)


def wpoints(n):
    pts = []
    for a in range(1, n):
        for c in range(1, n):
            if a * c > 3 * n / 4:
                break
            for d in range(1, n):
                acd = a * c * d
                if acd > 3 * n / 4:
                    break
                if 4 * acd <= n:  # need n/4 < acd
                    continue
                f = 4 * acd - n
                if (4 * a * a * d + 1) % f == 0:
                    pts.append((a, c, d, f))
    return pts


def check_points(n, pts):
    bad = 0
    for (a, c, d, f) in pts:
        e = (4 * a * a * d + 1) // f
        b = c * e - a
        ok = (4 * a * b * d == n * e + 1 and b * f == n * a + c and n * n + 4 * c * c * d == f * (4 * b * c * d - n))
        M = (e, 2 * a, 2 * a * d, f)
        ok &= M[0] * M[3] - M[1] * M[2] == 1 and M[2] == d * M[1] and n == 2 * c * M[2] - M[3]
        A, B, C = f, 4 * a * d, d * e
        ok &= B * B - 4 * A * C == -4 * d and gcd(gcd(A, B), C) == 1
        if not ok:
            bad += 1
            print("IDENTITY FAIL", n, a, b, c, d, e, f)
    return bad


def areas(G=1200):
    # midpoint grid on (alpha,beta) in slice 0<=al<=1, al<=be<=1+al, gamma=eta=0
    rb = rs = tot = 0
    h = 1.0 / G
    for i in range(G):
        al = (i + 0.5) * h
        for j in range(2 * G):
            be = (j + 0.5) * h
            if not (al <= be <= 1 + al):
                continue
            tot += 1
            mods = [1, 1 + be - al, al + be, 1 + 2 * al - be, 2 - be, 1 + 2 * be - al, 2 - 2 * al + be]
            if min(mods) >= 1:
                rb += 1
                if al >= 0.5 and be >= 2 / 3 and be <= al + 1 / 3:
                    rs += 1
    return tot * h * h, rb * h * h, rs * h * h


if __name__ == "__main__":
    bad = 0
    viol = 0
    for p in primerange(3, 180):
        pts = wpoints(p)
        bad += check_points(p, pts)
        fi = fI(p)
        if fi > 2 * len(pts):
            viol += 1
        print(f"p={p:4d} f_I={fi:4d} sum_c w_c={len(pts):4d}")
    print("identity failures:", bad, " f_I > 2 sum w_c violations:", viol)
    print("areas (slice, R_bad, R**) ~", areas(), " expected (1, 1/6=%.5f, 7/72=%.5f)" % (1 / 6, 7 / 72))
