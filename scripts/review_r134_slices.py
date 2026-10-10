"""R134 referee: from-scratch check of the slice table (Lemma 3.1) and of the Type I/II dictionaries
(Lemma 2.2, Prop 2.3, Prop 2.6(a),(c),(d), Lemma 2.9 norms) of paper/es-automorphic-barrier-note.tex.
Independent of scripts/rt2_slices.py.  Brute force: all ordered ES solutions of 4/p, decomposed into
ET tuples (a,b,c,d,e)."""
import sys
from math import gcd
from fractions import Fraction
from sympy import primerange, divisors, jacobi_symbol


def es_solutions(n):
    sols = set()
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r = Fraction(4, n) - Fraction(1, x)
        if r <= 0:
            continue
        ylo = max(x, int(1 / r) + 1)
        yhi = int(2 / r)
        for y in range(ylo, yhi + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                sols.add((x, y, s.denominator))
    out = set()
    for (x, y, z) in sols:
        for t in {(x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)}:
            out.add(t)
    return out


def tuples(p):
    VI, VII = set(), set()
    for (x, y, z) in es_solutions(p):
        if x % p == 0 and y % p and z % p:      # Type I: x=abdp, y=acd, z=bcd
            g = gcd(y, z)
            for cd in divisors(g):
                for c in divisors(cd):
                    d = cd // c
                    a, b = y // cd, z // cd
                    if a * b * d * p == x and (a + b) % c == 0:
                        e = (a + b) // c
                        if 4 * a * b * d == p * e + 1:
                            VI.add((a, b, c, d, e))
        if x % p and y % p == 0 and z % p == 0:  # Type II: x=abd, y=acdp, z=bcdp
            g = gcd(y // p, z // p)
            for cd in divisors(g):
                for c in divisors(cd):
                    d = cd // c
                    a, b = y // p // cd, z // p // cd
                    if a * b * d == x and (a + b) % c == 0:
                        e = (a + b) // c
                        if 4 * a * b * d == p + e:
                            VII.add((a, b, c, d, e))
    return VI, VII


IDX = dict(a=0, b=1, c=2, d=3, e=4)


def fibre(V, k1, v1, k2, v2):
    return sum(1 for t in V if t[IDX[k1]] == v1 and t[IDX[k2]] == v2)


def table_count(typ, th, v1, v2, p):
    """number predicted by the slice table row (D rows), or None for C rows handled separately"""
    if typ == 'I' and th == 'cd':
        c, d = v1, v2
        if (c * d) % p == 0:
            return 0
        N = p * p + 4 * c * c * d
        return sum(1 for f in divisors(N) if (f + p) % (4 * c * d) == 0)
    if typ == 'I' and th == 'ac':
        a, c = v1, v2
        N = a * p + c
        return sum(1 for f in divisors(N) if (f + p) % (4 * a * c) == 0)
    if typ == 'II' and th == 'cd':
        c, d = v1, v2
        N = 4 * c * c * d * p + 1
        return sum(1 for f in divisors(N) if (f + 1) % (4 * c * d) == 0)
    if typ == 'II' and th == 'ac':
        a, c = v1, v2
        N = c * p + a
        return sum(1 for f in divisors(N) if (f + 1) % (4 * a * c) == 0)
    if typ == 'II' and th == 'ad':
        a, d = v1, v2
        N = p + 4 * a * a * d
        return sum(1 for f in divisors(N) if (f + 1) % (4 * a * d) == 0)
    if th in ('ae', 'de'):
        x, e = v1, v2
        M = p * e + 1 if typ == 'I' else p + e
        if M % (4 * x):
            return 0
        N = M // (4 * x)
        if th == 'ae':   # divisor f=b, f = -a mod e
            return sum(1 for f in divisors(N) if (f + x) % e == 0)
        return sum(1 for f in divisors(N) if gcd(f, e) == 1 and (f * f + N) % e == 0)
    if typ == 'I' and th == 'ad':
        a, d = v1, v2
        return sum(1 for f in divisors(4 * a * a * d + 1) if (f + p) % (4 * a * d) == 0)
    raise ValueError


def main(P=200, R=12):
    bad = 0
    nchk = 0
    for p in primerange(5, P):
        VI, VII = tuples(p)
        for typ, V in (('I', VI), ('II', VII)):
            rows = ['cd', 'ac', 'ae', 'de'] + (['ad'] if True else [])
            for th in rows:
                k1, k2 = th[0], th[1]
                vals = set((t[IDX[k1]], t[IDX[k2]]) for t in V)
                vals |= {(i, j) for i in range(1, R) for j in range(1, R)}
                for (v1, v2) in vals:
                    pred = table_count(typ, th, v1, v2, p)
                    got = fibre(V, k1, v1, k2, v2)
                    nchk += 1
                    if pred != got:
                        bad += 1
                        if bad < 20:
                            print('MISMATCH', p, typ, th, v1, v2, pred, got)
            # dictionary identities
            for (a, b, c, d, e) in V:
                if typ == 'I':
                    f = 4 * a * c * d - p
                    g = (p * p + 4 * c * c * d) // f
                    assert f >= 1 and (4 * a * a * d + 1) == e * f and a * p + c == b * f and g * f == p * p + 4 * c * c * d
                    assert g == 4 * b * c * d - p and c * d % p != 0
                    # Prop 2.3: Q'(x,y) = Q_-(x+2bd y, p y), Q_-=[f,-4ad,de], Q'=[f,4cd,dg]
                    for (X, Y) in ((1, 0), (0, 1), (1, 1), (2, -3)):
                        u, v = X + 2 * b * d * Y, p * Y
                        assert f * X * X + 4 * c * d * X * Y + d * g * Y * Y == f * u * u - 4 * a * d * u * v + d * e * v * v
                    assert (4 * a * d) * b - p * e == 1
                    assert jacobi_symbol(-d % p, p) == -1          # Lemma 2.5 at n=p
                else:
                    f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
                    assert f * f2 == 4 * c * c * d * p + 1
                    E = (p + 4 * a * a * d)
                    assert E % f == 0 and E // f == e        # e f = p + 4a^2 d
                    assert 16 * a * a * d * d - 4 * d * e * f == -4 * d * p
                    assert 2 * (4 * a * d) * (2 * c) - 4 * f == 4
                    assert jacobi_symbol(p, f) == -1 and jacobi_symbol(p, f2) == -1
                    assert gcd(d * p, f) == 1
    print('slice checks', nchk, 'mismatches', bad)


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
