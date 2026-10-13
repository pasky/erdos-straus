# ec_cert.py — independent checker for an exponent-covering certificate of ES on n_m = k*b^m + c.
# Uses ONLY the certificate data (classes r mod M with explicit rational polynomials x(n), y(n), z(n)); no ES library.
# Checks: (i) 4xyz = n(xy+yz+zx) identically; (ii) x,y,z integer-valued on r + M*t (binomial-basis test);
# (iii) positivity of x,y,z for n >= n0 (explicit root bound); (iv) periodicity hypotheses (odd part of M | b^L - 1)
# and coverage of every m mod L for m >= m0; (v) exact integer verification for m0 <= m <= MMAX; (vi) brute-force ES for m < m0.
# Usage: PYTHONPATH=scripts uv run python scripts/ec_cert.py cert.json [MMAX]
import sys, json
from fractions import Fraction as F
from math import comb


def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def padd(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, a in enumerate(p):
        r[i] += a
    for i, a in enumerate(q):
        r[i] += a
    return r


def peval(p, x):
    v = F(0)
    for a in reversed(p):
        v = v * x + a
    return v


def strip(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def es_brute(n):
    """does 4/n = 1/x+1/y+1/z have a solution in positive integers? (x<=y<=z)"""
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        num, den = 4 * x - n, n * x            # remaining 2/... = num/den
        if num <= 0:
            continue
        lo = max(x, den // num + 1)
        hi = 2 * den // num
        for y in range(lo, hi + 1):
            nn, dd = num * y - den, den * y
            if nn > 0 and dd % nn == 0:
                return (x, y, dd // nn)
    return None


def main(path, MMAX=3000):
    C = json.load(open(path))
    k, b, c, L = C['k'], C['b'], C['c'], C['L']
    n_poly = [F(0), F(1)]
    m0 = 0
    bad = 0
    for cl in C['classes']:
        M, r = cl['M'], cl['r']
        X = [[F(s) for s in p] for p in cl['xyz']]
        # (i) identity
        lhs = [4 * a for a in pmul(pmul(X[0], X[1]), X[2])]
        rhs = pmul(n_poly, padd(padd(pmul(X[0], X[1]), pmul(X[1], X[2])), pmul(X[0], X[2])))
        diff = strip(padd(lhs, [-a for a in rhs]))
        assert diff == [0], ('identity fails', cl)
        # (ii) integer-valued on r + M t: values at t = 0..d and all forward differences integral
        for p in X:
            d = len(p) - 1
            vals = [peval(p, F(r + M * t)) for t in range(d + 1)]
            for i in range(d + 1):
                delta = sum((-1) ** (i - j) * comb(i, j) * vals[j] for j in range(i + 1))
                assert delta.denominator == 1, ('not integer-valued', cl)
        # (iii) positivity: leading coeff > 0 and n > 1 + max|a_i/a_d| (Cauchy) => p(n) > 0
        npos = 0
        for p in X:
            p = strip(p)
            assert p[-1] > 0, ('negative leading coefficient', cl)
            if len(p) > 1:
                npos = max(npos, int(1 + max(abs(a / p[-1]) for a in p[:-1])) + 1)
        cl['_npos'] = npos
        # (iv) periodicity hypothesis
        Mp, s = M, 0
        bb = b
        for q in [2, 3, 5, 7]:
            if b % q == 0:
                while Mp % q == 0:
                    Mp //= q
                    s += 1
        assert (b ** L - 1) % Mp == 0, ('odd part does not divide b^L-1', cl)
        m0 = max(m0, s)
        cl['_X'] = X
    # m0 also must make n_m >= npos for all classes
    while k * b ** m0 + c < max(cl['_npos'] for cl in C['classes']):
        m0 += 1
    # coverage of each residue m mod L at representatives m0..m0+L-1
    for m in range(m0, m0 + L):
        n = k * b ** m + c
        assert any(n % cl['M'] == cl['r'] for cl in C['classes']), ('uncovered exponent', m % L)
    # (v) exact verification for m0 <= m <= MMAX
    for m in range(m0, MMAX + 1):
        n = k * b ** m + c
        ok = False
        for cl in C['classes']:
            if n % cl['M'] == cl['r']:
                x, y, z = (peval(p, F(n)) for p in cl['_X'])
                assert x.denominator == y.denominator == z.denominator == 1 and min(x, y, z) > 0
                x, y, z = int(x), int(y), int(z)
                assert 4 * x * y * z == n * (x * y + y * z + x * z)
                ok = True
                break
        assert ok, ('no class at m', m)
    # (vi) brute force for m < m0
    small = []
    for m in range(0, m0):
        n = k * b ** m + c
        if n >= 2:
            sol = es_brute(n)
            assert sol is not None, ('ES fails?!', n)
            small.append((m, n, sol))
    print('CERTIFIED: ES holds for all n = %d*%d^m %+d, m >= 0 (classes: %d, L = %d, m0 = %d, exact check to m = %d)'
          % (k, b, c, len(C['classes']), L, m0, MMAX))
    print('  small members by brute force:', small)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3000)
