"""O99 (POINTWISE_TYPEI6.md, Lemma 1.1): check the exact identities of the gap parametrisation
on relaxed solutions (output rows of scripts/typei5_relax.c: L u a c' g delta P1 X rho j).
Usage: python scripts/typei6_identities.py file1 [file2 ...]"""
import sys
from fractions import Fraction
from mpmath import mp, mpf, sqrt

mp.dps = 80
n = nB = 0
for fn in sys.argv[1:]:
    for line in open(fn):
        L, u, a, cp, g, dl, P1, X, rho, j = map(int, line.split())
        T = 2 ** (L - 4); co = 7 ** a * cp; M = co * dl * dl + T; d = co * M
        m = cp * dl * dl; n += 1
        # (1.1) relation, Pell form, P1 | M
        assert M % P1 == 0; Q1 = M // P1; P = cp * P1; Q = 7 ** a * Q1
        assert 16 * P * X * X - Q * u * u == 1
        assert rho * P1 == T * u // 2 + j and j == T * u // 2 - cp * g * dl
        if j <= 0:
            continue
        nB += 1
        assert (rho * j - m) % u == 0; lam = (rho * j - m) // u
        sigma = 8 * 7 ** a * m * j + 4 * T * j - T * T * u
        omega = 4 * j * j - u * sigma
        assert omega == 4 * m * P1, (line, omega, 4 * m * P1)
        assert sigma == 4 * lam * P1 - 2 * T * j
        # J = 8j - mu*u = -32 c' delta P1 X, mu = 8 c_o delta^2 + 4T
        assert 8 * j - (8 * co * dl * dl + 4 * T) * u == -32 * cp * dl * P1 * X
        # j = u*theta - delta*sqrt(P)/zeta, theta = (T/2)(sqrt d - c_o delta)/(sqrt d + c_o delta)
        sd = sqrt(mpf(d)); theta = mpf(T) / 2 * (sd - co * dl) / (sd + co * dl)
        zeta = 4 * X * sqrt(mpf(P)) + u * sqrt(mpf(Q))
        assert abs(u * theta - dl * sqrt(mpf(P)) / zeta - j) < mpf(10) ** -50
        # quadratic in u
        k7 = 7 ** a
        val = (2 * k7 * T * (T * rho + 2 * lam) * u * u
               - (8 * k7 * T * rho * rho * P1 + 8 * k7 * lam * rho * P1 + 4 * T * T) * u
               + P1 * (8 * k7 * rho ** 3 * P1 + 6 * T * rho - 4 * lam))
        assert val == 0
        reg = 'v' if sigma > 0 else ('iii' if lam > 0 else 'ii')
        print(f"L={L} u={u} a={a} c'={cp} delta={dl} P1={P1} j={j} lam={lam} sigma={sigma} regime={reg}"
              f" frac(u*theta)={float(u*theta-j):.3e}")
print(f"{n} rows, {nB} case-B rows: all identities OK")
