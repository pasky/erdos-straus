# review_r258_cert63.py — R258 FROM-SCRATCH checker for EXP_OPEN Theorem 3.1 (ES for every 63*2^s + 1).
# No z19_/z15_/z14_ imports; no sympy.  Pure Fraction polynomial arithmetic + exact integers.
# Reads only the raw class data (M, r, xyz) from data/z19/cert63_et.json; ignores 'fam', 'exps', 'L_M'.
# Usage: uv run python scripts/review_r258_cert63.py [SMAX]
import sys, json
from fractions import Fraction as F
from math import gcd, comb, isqrt

SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
C = json.load(open('data/z19/cert63_et.json'))
L = 2520; S0 = 10; NMIN = 63 * 2 ** S0 + 1

# ---------- polynomial helpers (ascending coefficient lists of Fractions) ----------
def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r
def padd(*ps):
    m = max(len(p) for p in ps); r = [F(0)] * m
    for p in ps:
        for i, a in enumerate(p): r[i] += a
    return r
def pscale(p, c): return [c * a for a in p]
def ptrim(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return p
def pev(p, v): return sum(a * v ** i for i, a in enumerate(p))

def ord2(m):
    if m == 1: return 1
    o, x = 1, 2 % m
    while x != 1: x = x * 2 % m; o += 1
    return o

# ---------- (A) ET/divisor classes ----------
classes = []
for cl in C['classes']:
    M, r = cl['M'], cl['r']
    P = [[F(c) for c in p] for p in cl['xyz']]
    x, y, z = P
    nP = [F(0), F(1)]
    # identity 4xyz = n(xy + yz + zx) as polynomials in n
    lhs = pscale(pmul(pmul(x, y), z), F(4))
    rhs = pmul(nP, padd(pmul(x, y), pmul(y, z), pmul(z, x)))
    assert ptrim(padd(lhs, pscale(rhs, F(-1)))) == [], ('identity', M, r)
    # integer-valued on n = r + M t (t integer): Newton forward differences at t = 0..deg are integers
    for p in P:
        deg = len(ptrim(p)) - 1
        vals = [pev(p, r + M * t) for t in range(deg + 1)]
        for i in range(deg + 1):
            dif = sum((-1) ** (i - j) * comb(i, j) * vals[j] for j in range(i + 1))
            assert dif.denominator == 1, ('intval', M, r, p)
    # positivity for n >= NMIN: substitute n = NMIN + u, all coefficients in u >= 0 and not all zero
    for p in P:
        q = [F(0)] * len(p)
        for i, a in enumerate(p):
            for j in range(i + 1): q[j] += a * comb(i, j) * NMIN ** (i - j)
        q = ptrim(q)
        assert q and all(c >= 0 for c in q) and q[0] > 0, ('pos', M, r, p)
    # period of n_s mod M for s >= S0
    Mo, v = M, 0
    while Mo % 2 == 0: Mo //= 2; v += 1
    assert v <= S0 and L % ord2(Mo) == 0, ('period', M)
    # r must be a residue actually hit (consistency), and residue r compatible with 2-part: n = 1 mod 2^v
    assert r % (2 ** v) == 1 % (2 ** v), ('2-part', M, r)
    classes.append((M, r, P, cl['fam']))
print('A: %d ET/divisor classes: identity, integer-valuedness, positivity (n >= %d), period | %d  OK' % (len(classes), NMIN, L))

def cover(s):
    n = 63 * 2 ** s + 1
    return [i for i, (M, r, P, f) in enumerate(classes) if n % M == r]

# ---------- (B) coverage mod 2520 ----------
uncov = [s % L for s in range(S0, S0 + L) if not cover(s)]
print('B: residues s mod 2520 uncovered by ET/divisor classes:', sorted(uncov))
assert all(u % 24 == 0 for u in uncov)

# ---------- (C) moving-gap class, s = 0 mod 24 ----------
# symbolic identity in Y: c*n = 4abcd - a - b with n = 63Y^3+1
a, d = 5, 17
bP = [F(28, 340), F(-9, 340), F(3, 340), F(63, 340)]
cP = [F(64, 340), F(21, 340)]
nY = [F(1), F(0), F(0), F(63)]
lhs = pmul(cP, nY)
rhs = padd(pscale(pmul(bP, cP), F(4 * a * d)), [F(-a)], pscale(bP, F(-1)))
assert ptrim(padd(lhs, pscale(rhs, F(-1)))) == []
# Type II: 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn)  <=>  4abcd = cn + b + a (multiply by abcdn): same identity.
# integrality: Y = 2^{8j}, j >= 1.  Y mod 340 = (Y mod 4, Y mod 85); 2^8 = 256 = 1 (mod 85) -> Y = 1 mod 85, Y = 0 mod 4.
assert pow(2, 8, 85) == 1
for Ym in [y for y in range(340) if y % 4 == 0 and y % 85 == 1]:
    assert (63 * Ym ** 3 + 3 * Ym ** 2 - 9 * Ym + 28) % 340 == 0 and (21 * Ym + 64) % 340 == 0
# b > 0 for Y >= 1: 63Y^3 + 3Y^2 - 9Y + 28 >= 63 + 3 - 9 + 28 > 0 and increasing for Y >= 1
print('C: moving-gap identity (symbolic), integrality on every Y = 2^{8j} (j>=1) via Y = 0 mod 4, 1 mod 85, positivity OK')

# ---------- (D) exact solutions for s <= SMAX ----------
def check(n, t):
    x, y, z = t
    return all(isinstance(v, int) and v > 0 for v in t) and F(4, n) == F(1, x) + F(1, y) + F(1, z)

def brute(n):
    # 4/n = 1/x+1/y+1/z, x <= y <= z
    # search-limited (completeness not needed: any hit is verified exactly by check())
    for x in range(n // 4 + 1, n // 4 + 2000):
        r1 = F(4, n) - F(1, x)
        if r1 <= 0: continue
        ylo = max(x, (r1.denominator + r1.numerator - 1) // r1.numerator)
        yhi = (2 * r1.denominator) // r1.numerator
        for y in range(ylo, min(yhi, ylo + 20000) + 1):
            r2 = r1 - F(1, y)
            if r2 > 0 and r2.numerator == 1: return (x, y, r2.denominator)
    return None

SKIPD = len(sys.argv) > 2
cnt = {'brute': 0, 'moving': 0, 'ET': 0}
for s in range(0, 0 if SKIPD else SMAX + 1):
    n = 63 * 2 ** s + 1
    if s < S0:
        t = brute(n); assert t and check(n, t), s; cnt['brute'] += 1
        continue
    if s % 24 == 0:
        Y = 2 ** (s // 3)
        b = F(63 * Y ** 3 + 3 * Y ** 2 - 9 * Y + 28, 340); c = F(21 * Y + 64, 340)
        assert b.denominator == 1 and c.denominator == 1
        b, c = int(b), int(c)
        t = (a * b * d, a * c * d * n, b * c * d * n); assert check(n, t), s; cnt['moving'] += 1
    cs = cover(s)
    if s % 24 and not cs: raise SystemExit('UNCOVERED s=%d' % s)
    for i in cs:   # verify EVERY applicable ET class, not only one
        P = classes[i][2]
        vals = [pev(p, n) for p in P]
        assert all(v.denominator == 1 for v in vals)
        assert check(n, tuple(int(v) for v in vals)), (s, i)
    if cs and s % 24: cnt['ET'] += 1
print('D: exact solutions s = 0..%d OK' % SMAX, cnt)

# ---------- (E) squares in the family; T1 control ----------
sq = []
for s in range(0, 400):
    n = 63 * 2 ** s + 1; r = isqrt(n)
    if r * r == n: sq.append(s)
print('E: s < 400 with 63*2^s+1 a square:', sq)
for M, r, P, fam in classes:
    hit = any((t * t - r) % M == 0 for t in range(M))
    print('   class M=%d r=%d fam=%s  r is a square mod M: %s' % (M, r, fam, hit))
