# z19_cert63_check.py — independent checker (O246) for: ES holds for every n_s = 63*2^s + 1, s >= 0.
# Certificate = (i) ET/divisor classes in data/z19/cert63_et.json (polynomials in n on n = r mod M), covering every
# s mod 2520 with s != 0 (mod 24); (ii) the moving-gap class of EXP_OPEN Theorem 2.3 on s = 0 (mod 24):
#   Y = 2^{s/3}, a = 5, d = 17, b = (63Y^3 + 3Y^2 - 9Y + 28)/340, c = (21Y + 64)/340, (x,y,z) = (abd, acdn, bcdn).
# Uses only sympy + exact integers (no z14/z15/ec_cover imports).
# Usage: PYTHONPATH=scripts uv run python scripts/z19_cert63_check.py data/z19/cert63_et.json [SMAX]
import sys, json
from fractions import Fraction as F
from math import comb
import sympy as sp
C = json.load(open(sys.argv[1])); SMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
c0 = 63; assert C['c0'] == c0 and C['k'] == 1 and C['b'] == 2; L = 2520
n, Y = sp.symbols('n Y')
def intvalued(P, var, r, M):     # P integer-valued on var = r (mod M): forward differences in t, var = r + M t
    P = sp.expand(P); d = sp.degree(P, var) if P.has(var) else 0
    vals = [P.subs(var, r + M * t) for t in range(d + 1)]
    return all(sp.Rational(sum((-1) ** (i - j) * comb(i, j) * vals[j] for j in range(i + 1))).q == 1 for i in range(d + 1))
ET = []
for cl in C['classes']:
    P3 = [sum(sp.Rational(c) * n ** i for i, c in enumerate(p)) for p in cl['xyz']]
    assert sp.expand(4 * P3[0] * P3[1] * P3[2] - n * (P3[0] * P3[1] + P3[1] * P3[2] + P3[0] * P3[2])) == 0
    M, r = cl['M'], cl['r']
    for P in P3:
        assert intvalued(P, n, r, M)
        co = sp.Poly(P, n).all_coeffs(); assert co[0] > 0
        assert len(co) == 1 or 1 + max(abs(cc / co[0]) for cc in co[1:]) < 63 * 2 ** 10   # Cauchy: positive for s >= 10
    Mo = M
    while Mo % 2 == 0: Mo //= 2
    assert (pow(2, L, Mo) - 1) % Mo == 0 and M // Mo <= 2 ** 10          # n_s mod M has period | 2520 for s >= 10
    if cl['fam'] != 'D': assert not any((t * t - r) % M == 0 for t in range(1, 2 * M, 2)), 'odd square in ET class'
    ET.append((M, r, [[F(c) for c in pp] for pp in cl['xyz']]))
# moving-gap class (Theorem 2.3)
nY = 63 * Y ** 3 + 1; a, d = 5, 17
b = (63 * Y ** 3 + 3 * Y ** 2 - 9 * Y + 28) / sp.Integer(340); c = (21 * Y + 64) / sp.Integer(340)
x, y, z = a * b * d, a * c * d * nY, b * c * d * nY
assert sp.simplify(1 / x + 1 / y + 1 / z - 4 / nY) == 0
assert sp.expand(c * nY - (4 * a * b * c * d - a - b)) == 0
# integrality for Y = 2^{8t}, t >= 1: numerators mod 340 depend on Y mod 340, which is periodic in t
per = sp.n_order(256, 85)
for t in range(1, per + 2):
    Yv = pow(2, 8 * t, 340 * 4096) + 340 * 4096      # representative = 2^{8t} mod 340*4096, large
    assert (63 * Yv ** 3 + 3 * Yv ** 2 - 9 * Yv + 28) % 340 == 0 and (21 * Yv + 64) % 340 == 0
def etclass(s):
    N0 = c0 * 2 ** s + 1
    for M, r, f in ET:
        if N0 % M == r: return f
    return None
for s in range(2520, 2520 + L):                       # coverage of every residue mod 2520 (s >= 10)
    assert s % 24 == 0 or etclass(s), ('uncovered', s % L)
used = {}
for s in range(0, SMAX + 1):
    N0 = c0 * 2 ** s + 1; sol = None
    if s % 24 == 0 and s >= 24:
        Yv = 2 ** (s // 3); vals = [sp.Rational(v.subs(Y, Yv)) for v in (x, y, z)]
        if all(v.q == 1 and v > 0 for v in vals): sol = [int(v) for v in vals]; used['moving'] = used.get('moving', 0) + 1
    if sol is None and s >= 10:
        f = etclass(s)
        if f:
            vals = [sum(co * N0 ** i for i, co in enumerate(pp)) for pp in f]
            if all(v.denominator == 1 and v > 0 for v in vals): sol = [int(v) for v in vals]; used['ET'] = used.get('ET', 0) + 1
    if sol is None:                                   # small s: brute force (x <= y <= z, x in (n/4, 3n/4])
        for xx in range(N0 // 4 + 1, 3 * N0 // 4 + 2):
            R = F(4, N0) - F(1, xx)
            if R <= 0: continue
            for yy in range(max(xx, int(1 / R)), int(2 / R) + 2):
                R2 = R - F(1, yy)
                if R2 > 0 and R2.numerator == 1: sol = [xx, yy, R2.denominator]; break
            if sol: break
        assert sol, ('no solution', s); used['brute'] = used.get('brute', 0) + 1
    p, q, r_ = sol; assert 4 * p * q * r_ == N0 * (p * q + q * r_ + p * r_) and min(sol) > 0, s
print('CHECK OK: ES for all 63*2^s+1 (ET classes %d, moving class s=0 mod 24); exact for s <= %d %s' % (len(ET), SMAX, used))
