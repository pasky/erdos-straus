"""R201 from-scratch check of GROWING_MUTE Prop 1.1 (cap hierarchy, (A,B) form, T1).

Usage: PYTHONPATH=scripts uv run python scripts/review_gm_dict.py NMAX QMAX ABMAX
Independent of scripts/gm_*.  Everything exact (Fraction / integer divisibility).
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt


def factor(m):
    f, d = {}, 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(m):
    ds = [1]
    for p, e in factor(m).items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds


def rad(m):
    r = 1
    for p in factor(m):
        r *= p
    return r


def sqfree(m):
    return all(e == 1 for e in factor(m).values())


def classify(n, x, y, z):
    """Classify a solution 4/n = 1/x+1/y+1/z (x,y int, z rational) per Def 1.0 / EXPONENT_CAP Def 1.1.
    Returns dict of booleans; 'adm' = den z is q^2 with q odd, gcd(q,n)=1."""
    assert F(4, n) == F(1, x) + F(1, y) + 1 / z, (n, x, y, z)
    den = z.denominator
    q = isqrt(den)
    adm = q * q == den and q % 2 == 1 and gcd(q, n) == 1
    return dict(adm=adm, q=q,
                ES=den == 1,
                y1=adm and y % q == 0 and sqfree(q),
                y2=adm and y % q == 0,
                yy=adm and y % rad(q) == 0)


def shot_solution(n, Q, g):
    m = (n + 4 * Q * Q) // g
    assert m * g == n + 4 * Q * Q
    assert (n + m) % 4 == 0 and (g + 1) % 4 == 0
    x = (n + m) // 4
    y = n * (g + 1) // 4
    z = F(n * x * (g + 1), 4 * Q * Q)
    return x, y, z


def partA(NMAX, QMAX):
    """All shot data (Q odd, gcd(Q,n)=1, g=3 mod 4, g | n+4Q^2): compare direct classification with
    the divisibility criteria of Prop 1.1(a),(b) and map to (A,B,g) when Q | K^2."""
    cnt = dict(shots=0, K2=0, y1=0, ES=0, yy=0)
    for n in range(3, NMAX + 1, 2):
        for Q in range(1, QMAX + 1, 2):
            if gcd(Q, n) != 1:
                continue
            for g in divisors(n + 4 * Q * Q):
                if g % 4 != 3:
                    continue
                cnt['shots'] += 1
                x, y, z = shot_solution(n, Q, g)
                c = classify(n, x, y, z)
                K = (g + 1) // 4
                Q0 = gcd(Q, K)
                Q1 = Q // Q0
                assert c['adm'] and c['q'] == Q1, (n, Q, g)
                assert c['ES'] == (K % Q == 0)
                assert c['y1'] == ((K * rad(K)) % Q == 0), (n, Q, g)
                assert c['y2'] == ((K * K) % Q == 0) == (Q0 % Q1 == 0)
                assert c['yy'] == (K % rad(Q) == 0)
                # hierarchy
                assert (not c['ES'] or c['y1']) and (not c['y1'] or c['y2']) and (not c['y2'] or c['yy'])
                if c['y2']:
                    cnt['K2'] += 1
                    k = K // Q0
                    A, B = 2 * k, Q1
                    assert A % 2 == 0 and B % 2 == 1 and gcd(A, B) == 1 and gcd(B, n) == 1
                    assert (n * A * A + B * B) % g == 0 and (g + 1) % (2 * A * B) == 0
                    assert Q0 == (g + 1) // (2 * A)
                cnt['y1'] += c['y1']
                cnt['ES'] += c['ES']
                cnt['yy'] += c['yy']
    print('partA', NMAX, QMAX, cnt)


def partB(NMAX, ABMAX):
    """All (A,B,g) with A even, B odd <= ABMAX, gcd(A,B)=gcd(B,n)=1, g | nA^2+B^2, g = -1 mod 2AB.
    Build Q0=(g+1)/(2A), Q=Q0*B (= lam*B^2), the shot formulas, and classify directly.
    Track lam even (Q even: NOT a shot datum in the Notation) and gcd(lam,n)>1."""
    cnt = dict(triples=0, lam_even=0, lam_n=0, bad_adm=0, bad_q=0, y1=0, sq_B=0, T1viol=0)
    for n in range(3, NMAX + 1, 2):
        sq = isqrt(n) ** 2 == n
        for A in range(2, ABMAX + 1, 2):
            for B in range(1, ABMAX + 1, 2):
                if gcd(A, B) != 1 or gcd(B, n) != 1:
                    continue
                N = n * A * A + B * B
                for g in divisors(N):
                    if (g + 1) % (2 * A * B):
                        continue
                    cnt['triples'] += 1
                    if sq:
                        cnt['T1viol'] += 1
                    lam = (g + 1) // (2 * A * B)
                    Q = lam * B * B
                    cnt['lam_even'] += lam % 2 == 0
                    cnt['lam_n'] += gcd(lam, n) > 1
                    x, y, z = shot_solution(n, Q, g)
                    c = classify(n, x, y, z)
                    if not c['adm']:
                        cnt['bad_adm'] += 1
                        continue
                    if c['q'] != B or not c['y2']:
                        cnt['bad_q'] += 1
                    if sqfree(B):
                        cnt['sq_B'] += 1
                        assert c['y1']
                    cnt['y1'] += c['y1']
    print('partB', NMAX, ABMAX, cnt)


if __name__ == '__main__':
    NMAX, QMAX, ABMAX = (int(a) for a in sys.argv[1:4])
    partA(NMAX, QMAX)
    partB(NMAX, ABMAX)
