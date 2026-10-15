# z8_cert_tree.py — independent checker for an ordered-class ("lifting") exponent covering of n_s = c0*4^s + k.
# Certificate: list of classes {M, r, xyz (polynomials in n)}.  Checks, using only the certificate:
#  (i) 4xyz = n(xy+yz+zx) in Q[n]; (ii) x,y,z integer-valued on r + MZ; (iii) positivity for n >= npos (Cauchy bound);
#  (iv) coverage: with L_M := lcm of ord_{q^e}(4) over odd q^e || M (recomputed here) and s >= s_min (4^s divisible by the
#       2-part of M), n_s mod M depends only on s mod L_M.  Replay: U = {0 mod 1}; for each class, lift U to
#       lcm(L, L_M) and delete residues with n_s = r (mod M).  Final U must be empty.
#  (v) exact check of the identity for s_min <= s <= SMAX; (vi) brute-force ES for s < s_min.
# Usage: PYTHONPATH=scripts uv run python scripts/z8_cert_tree.py cert.json [SMAX]
import sys, json
from math import lcm, comb
from fractions import Fraction as F
from sympy import n_order, factorint
from ec_cert import pmul, padd, peval, strip, es_brute

C = json.load(open(sys.argv[1]))
SMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
c0, k = C['c0'], C['k']
npos, smin = 0, 0
cls = []
for cl in C['classes']:
    M, r = cl['M'], cl['r']
    X = [[F(s) for s in p] for p in cl['xyz']]
    n = [F(0), F(1)]
    lhs = [4 * a for a in pmul(pmul(X[0], X[1]), X[2])]
    rhs = pmul(n, padd(padd(pmul(X[0], X[1]), pmul(X[1], X[2])), pmul(X[0], X[2])))
    assert strip(padd(lhs, [-a for a in rhs])) == [0], 'identity'
    for p in X:
        d = len(p) - 1
        vals = [peval(p, F(r + M * t)) for t in range(d + 1)]
        for i in range(d + 1):
            assert sum((-1) ** (i - j) * comb(i, j) * vals[j] for j in range(i + 1)).denominator == 1, 'integrality'
        p = strip(p)
        assert p[-1] > 0, 'leading coefficient'
        if len(p) > 1:
            npos = max(npos, int(1 + max(abs(a / p[-1]) for a in p[:-1])) + 1)
    fa = factorint(M)
    LM = 1
    for q, e in fa.items():
        if q != 2:
            LM = lcm(LM, n_order(4, q ** e))
    smin = max(smin, (fa.get(2, 0) + 1) // 2)
    cls.append((M, r, LM, X))
while c0 * 4 ** smin + k < npos:
    smin += 1
L, U = 1, [0]
for M, r, LM, X in cls:
    g = lcm(L, LM) // L
    rep = lambda x: x + LM * ((smin // LM) + 1) if x < smin else x
    U = [x for u in U for x in range(u, u + g * L, L) if (c0 * pow(4, rep(x), M) + k) % M != r]
    L *= g
    assert len(U) < 10 ** 7
assert not U, ('uncovered residues', U[:5], L)
for s in range(smin, SMAX + 1):
    n = c0 * 4 ** s + k
    for M, r, LM, X in cls:
        if n % M == r:
            x, y, z = (peval(p, F(n)) for p in X)
            assert min(x, y, z) > 0 and x.denominator == y.denominator == z.denominator == 1
            assert 4 * x * y * z == n * (x * y + y * z + x * z)
            break
    else:
        raise AssertionError('no class at s=%d' % s)
small = []
for s in range(0, smin):
    n = c0 * 4 ** s + k
    assert es_brute(n) is not None
    small.append(n)
print('CERTIFIED: ES holds for all n = %d*4^s + %d, s >= 0 (%d classes, lcm of periods L = %d, s_min = %d, exact to s = %d; '
      'brute force for %s)' % (c0, k, len(cls), L, smin, SMAX, small))
