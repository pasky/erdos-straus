"""R200 from-scratch check of EXPONENT_CAP Prop 1.2, Prop 1.3 (both directions), Cor 1.4, Thm 2.1 and the
sharpness family. Independent of scripts/xc_*.  Usage: review_xc_algebra.py NMAX QMAX
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt


def divisors(N):
    ds, i = [], 1
    while i * i <= N:
        if N % i == 0:
            ds.append(i)
            if i * i != N:
                ds.append(N // i)
        i += 1
    return ds


def vp(x, p):
    c = 0
    while x % p == 0:
        x //= p; c += 1
    return c


def primefac(x):
    fs, p = {}, 2
    while p * p <= x:
        while x % p == 0:
            fs[p] = fs.get(p, 0) + 1; x //= p
        p += 1
    if x > 1:
        fs[x] = fs.get(x, 0) + 1
    return fs


def es_ye(n, x, y, z, e):
    """direct Def 1.1 test of ES^{(y,e)} (e=None means infinity)"""
    if F(4, n) != F(1, x) + F(1, y) + 1 / z:
        return False
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0):
        return False
    for l, a in primefac(z.denominator).items():
        if l == 2 or n % l == 0 or y % l or a % 2:
            return False
        if e is not None and a > 2 * e:
            return False
    return True


def main(NMAX, QMAX):
    cnt = bad = 0
    ratio_max = (0, None)
    branch = [0, 0]
    evenQ_den_bad = 0
    for n in range(3, NMAX + 1, 2):
        for Q in range(1, QMAX + 1):
            if gcd(Q, n) != 1:
                continue
            N = n + 4 * Q * Q
            for g in divisors(N):
                if g % 4 != 3:
                    continue
                cnt += 1
                m = N // g
                x = (n + m) // 4
                assert (n + m) % 4 == 0
                y = n * (g + 1) // 4
                z = F(n * x * (g + 1), 4 * Q * Q)
                assert F(4, n) == F(1, x) + F(1, y) + 1 / z
                Q0 = gcd(Q, (g + 1) // 4); Q1 = Q // Q0
                if z.denominator != Q1 * Q1:
                    if Q % 2: bad += 1; print("den", n, Q, g)
                    else: evenQ_den_bad += 1
                # Prop 1.2 for Q odd, e = 0..3 and inf
                if Q % 2:
                    for e in (0, 1, 2, 3, None):
                        Qe = 1
                        for l, c in primefac(Q).items():
                            Qe *= l ** (max(1, c - e) if e is not None else 1)
                        pred = (g + 1) % (4 * Qe) == 0
                        if pred != es_ye(n, x, y, z, e):
                            bad += 1; print("P1.2", n, Q, g, e)
                # Prop 1.3 forward
                k = (g + 1) // (4 * Q0)
                assert (m + n) % Q0 == 0
                j = (m + n) // Q0
                D = k * j - Q1 * Q1
                ok = (j > 0 and j % 4 == 0 and 4 * Q0 * (k * j - Q1 * Q1) == 4 * k * n + j
                      and D * g == 4 * k * k * n + Q1 * Q1 and D >= 1 and (D + Q1 * Q1) % (4 * k) == 0)
                if not ok:
                    bad += 1; print("P1.3", n, Q, g)
                # Cor 1.4: with K=(g+1)/4, kk=K/Q0, -n == Q0 Q1^2 / kk mod g
                K = (g + 1) // 4
                if (-n * k - Q0 * Q1 * Q1) % g != 0:
                    bad += 1; print("C1.4", n, Q, g)
                # Thm 2.1
                b1 = Q1 ** 4 * n + Q1 * Q1
                b2 = F(n * (n + 1)) * (Q1 * Q1 + F(1, 2)) + 1
                if g > max(b1, b2) or g > 2 * n * Q1 * Q1 * (n + Q1 * Q1):
                    bad += 1; print("T2.1", n, Q, g)
                if k * j < 2 * Q1 * Q1:
                    branch[0] += 1
                    if not g < b1: bad += 1; print("T2.1 case1", n, Q, g)
                else:
                    branch[1] += 1
                    if not (g <= b2 and 2 * Q0 <= n + 1): bad += 1; print("T2.1 case2", n, Q, g)
                rt = F(g, n * Q1 * Q1 * (n + Q1 * Q1))
                if rt > ratio_max[0]:
                    ratio_max = (rt, (n, Q, g))
                # completeness bound used in sec 5.1: Q0 <= Q1^2 n/2 + Q1^2/2 + 1
                if 2 * Q0 > Q1 * Q1 * n + Q1 * Q1 + 2:
                    bad += 1; print("Q0bound", n, Q, g)
    print(f"shots={cnt} bad={bad} evenQ_den_mismatch={evenQ_den_bad} branches={branch} "
          f"max g/(nQ1^2(n+Q1^2))={float(ratio_max[0]):.4f} at {ratio_max[1]}")


def converse(NMAX, Q1MAX, KMAX):
    """Prop 1.3 converse: every D | 4k^2n+Q1^2, D == -Q1^2 mod 4k gives a shot datum with overflow Q1."""
    cnt = bad = 0
    for n in range(3, NMAX + 1, 2):
        for Q1 in range(1, Q1MAX + 1, 2):
            for k in range(1, KMAX + 1):
                if gcd(Q1, k) != 1:
                    continue
                A = 4 * k * k * n + Q1 * Q1
                for D in divisors(A):
                    if (D + Q1 * Q1) % (4 * k):
                        continue
                    cnt += 1
                    g = A // D; j = (D + Q1 * Q1) // k
                    if (4 * k * n + j) % (4 * D):
                        bad += 1; print("conv Q0", n, Q1, k, D); continue
                    Q0 = (4 * k * n + j) // (4 * D)
                    Q = Q0 * Q1
                    if not (Q0 > 0 and g == 4 * Q0 * k - 1 and (n + 4 * Q * Q) % g == 0
                            and gcd(Q, (g + 1) // 4) == Q0):
                        bad += 1; print("conv", n, Q1, k, D)
    print(f"converse: cases={cnt} bad={bad}")


def sharp(QMAX):
    """sharpness family D=3, j=4, k=(Q1^2+3)/4, n == -1/k mod 3; also check gcd(Q,n)=1 requirement"""
    rows = []
    for Q1 in range(1, QMAX + 1, 2):
        if Q1 % 3 == 0:
            continue
        k = (Q1 * Q1 + 3) // 4
        for n in range(3, 200, 2):
            if (k * n + 1) % 3:
                continue
            Q0 = (k * n + 1) // 3
            Q = Q0 * Q1
            g = 4 * Q0 * k - 1
            assert (n + 4 * Q * Q) % g == 0 and g == (4 * k * k * n + Q1 * Q1) // 3
            assert gcd(Q, (g + 1) // 4) == Q0
            rows.append((Q1, n, gcd(Q, n), F(g, n * Q1 ** 4)))
    bad_gcd = [(a, b) for a, b, c, _ in rows if c != 1]
    print("sharp: n residues mod 3 seen:", sorted({b % 3 for _, b, _, _ in rows}),
          " k mod 3:", sorted({((q * q + 3) // 4) % 3 for q, _, _, _ in rows}),
          " gcd(Q,n)>1 cases (not shot data):", len(bad_gcd), bad_gcd[:3],
          " g/(nQ1^4) at Q1 max:", float(rows[-1][3]))
    # the worked example
    n, Q = 17, 200; g = 1119; m = (n + 4 * Q * Q) // g
    x = (n + m) // 4; y = n * (g + 1) // 4; z = F(n * x * (g + 1), 4 * Q * Q)
    print("example:", (n + 4 * Q * Q) % g, x, y, z, 1 / z, F(4, n) == F(1, x) + F(1, y) + 1 / z,
          "ES^(y,1):", es_ye(n, x, y, z, 1), "ES^(y,0):", es_ye(n, x, y, z, 0))


if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 151
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 151
    main(a, b)
    converse(81, 41, 40)
    sharp(61)
