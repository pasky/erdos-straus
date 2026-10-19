#!/usr/bin/env python3
# c1_expfam_verify.py -- self-contained verification of every certificate in paper/es-exponential-families.tex
# (task O277).  Uses only sympy + the Python standard library; imports nothing from the campaign code.
#
# Every certificate is a finite list of RULES for a family n_s = c0*B^s + k (B in {2, 4}).  A rule is
#     s = s0 + sigma*t   (t >= 0),   Y = 2^(omega*t),   n = c0*B^s0*Y^D + k   (D = sigma*log2(B)/omega),
# together with x, y, z in Q[Y].  For each rule the script
#   (1) checks the identity 4xyz = n(xy + yz + zx) in Q[Y]                                    [symbolic]
#   (2) DERIVES the exact set of residues t mod T for which x, y, z are integers for all large t:
#       write R = R1/N with R1 in Z[Y], N = 2^a N' (N' odd).  For omega*t >= a, R1(2^(omega t)) = R1(0) mod 2^a,
#       and R1(2^(omega t)) mod N' is periodic in t with period ord_{N'}(2^omega); so one period decides all t >= t*.
#   (3) checks positivity: numerators have no real root >= 2^(omega t*) (Sturm, exact) and positive leading terms.
# Coverage: L = lcm of the rule periods in s; every residue s mod L is covered by a rule for all s >= S*; every
# 0 <= s < S* is solved explicitly (by a rule evaluated at that s, or by an exhaustive divisor search).
# Numerics: an exact solution is built from the covering rule and checked for every s <= SMAX.
# Further finite checks of the paper: Theorem W's limit enumeration (Computation 5.6), the boxed equation of
# Lemma 5.10, and the derived class tables (printed with --tables).
# Usage: PYTHONPATH=scripts uv run python scripts/c1_expfam_verify.py [--tables] [--smax N]
import sys, time
from fractions import Fraction as Fr
from math import gcd, lcm, prod, isqrt
from functools import reduce
from itertools import product as iprod
from sympy import (symbols, Poly, Rational, expand, cancel, fraction, together, cyclotomic_poly, divisors,
                   n_order, factorint, factor_list, Integer)

Y = symbols('Y')
T0 = time.time()
TABLES = '--tables' in sys.argv
SMAX = int(sys.argv[sys.argv.index('--smax') + 1]) if '--smax' in sys.argv else 1000


def log(*a):
    print(*a, flush=True)


# ----------------------------------------------------------------------------------------------------------
# small exact helpers
def es_brute(n):
    """an explicit solution of 4/n = 1/x+1/y+1/z (divisor method on 4/n - 1/x = m/(nx)); None if not found."""
    for x in range(n // 4 + 1, n // 4 + 3000):
        m, M = 4 * x - n, n * x
        g = gcd(m, M); m //= g; M //= g
        if m == 1:
            return (x, 2 * M, 2 * M)
        # m/M = 1/y + 1/z  <=>  d1, d2 | M with m | d1 + d2  (y = M(d1+d2)/(m d2), z = M(d1+d2)/(m d1))
        fM = factorint(M)
        ds = sorted(divisors(M)) if M < 10 ** 30 else None
        if ds is None:
            continue
        S = set(d % m for d in ds)
        for d1 in ds:
            if (-d1) % m in S:
                for d2 in ds:
                    if (d1 + d2) % m == 0:
                        y, z = M * (d1 + d2) // (m * d2), M * (d1 + d2) // (m * d1)
                        assert Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z)
                        return (x, y, z)
    return None


def check_sol(n, sol):
    x, y, z = sol
    return min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)


def two_adic(N):
    a = 0
    while N % 2 == 0:
        N //= 2; a += 1
    return a, N


# ----------------------------------------------------------------------------------------------------------
# rule constructors (all return dict with s0, sigma, omega and x, y, z in Q[Y])
class Fam:
    def __init__(self, name, c0, B, k):
        self.name, self.c0, self.B, self.k = name, c0, B, k
        self.lb = {2: 1, 4: 2}[B]
        self.rules = []

    def nY(self, s0, sigma, omega):
        D, r = divmod(sigma * self.lb, omega); assert r == 0
        return self.c0 * self.B ** s0 * Y ** D + self.k

    def add(self, label, s0, sigma, omega, x, y, z):
        n = self.nY(s0, sigma, omega)
        self.rules.append(dict(label=label, s0=s0, sigma=sigma, omega=omega, n=n,
                               xyz=[cancel(expand(e)) for e in (x, y, z)]))

    # ET classes: polynomial in n (sigma = 1, Y = B^s)
    def et(self, fam, *p):
        n = self.nY(0, 1, self.lb)
        if fam == 'D':
            q, (xq, yq, zq) = p[0], DIV_ES[p[0]]
            x, y, z = xq * n / q, yq * n / q, zq * n / q
        elif fam == 'II2':           # 4ad | f+1, n = -4a^2 d (mod f)
            a, d, f = p; assert (f + 1) % (4 * a * d) == 0
            c = (f + 1) // (4 * a * d); b = (n * c + a) / f
            x, y, z = a * b * d, a * c * d * n, b * c * d * n
        elif fam == 'I1':            # f | 4a^2 d + 1, n = -f (mod 4ad)
            a, d, f = p; assert (4 * a * a * d + 1) % f == 0
            e = (4 * a * a * d + 1) // f; b = (n * e + 1) / (4 * a * d); c = (n + f) / (4 * a * d)
            x, y, z = a * b * d * n, a * c * d, b * c * d
        elif fam == 'I2':            # (4ac, f) = 1, n = -f (4ac), n = -c/a (f)
            a, c, f = p; assert gcd(4 * a * c, f) == 1
            d = (n + f) / (4 * a * c); b = (n * a + c) / f
            x, y, z = a * b * d * n, a * c * d, b * c * d
        elif fam == 'II1':           # e | a+b, (e, 4ab) = 1, n = -e (mod 4ab)
            a, b, e = p; assert (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
            c = (a + b) // e; d = (n + e) / (4 * a * b)
            x, y, z = a * b * d, a * c * d * n, b * c * d * n
        elif fam == 'I3':            # (4cd, f) = 1, n = -f (4cd), f | n^2 + 4c^2 d
            c, d, f = p; assert gcd(4 * c * d, f) == 1
            a = (n + f) / (4 * c * d); b = (n * n + 4 * c * c * d + n * f) / (4 * c * d * f)
            x, y, z = a * b * d * n, a * c * d, b * c * d
        else:
            raise ValueError(fam)
        self.add('%s%s' % (fam, p), 0, 1, self.lb, x, y, z)

    # constant-gap window rule (Lemma 3.1): x = (n+m)/4, N = n x, d1, d2 | N, m | d1 + d2
    def window(self, label, s0, sigma, omega, m, d1, d2):
        n = self.nY(s0, sigma, omega)
        x = expand((n + m) / 4); N = expand(n * x)
        for d in (d1, d2):
            assert cancel(N / d).is_polynomial(Y), (label, 'd does not divide N')
        y = N * (d1 + d2) / (m * d2); z = N * (d1 + d2) / (m * d1)
        self.add(label, s0, sigma, omega, x, y, z)

    # z14-type window leaf ('W m j code w h' with relation eps, i), see EXP_105 section 2
    def z14(self, m, j, code, w, h, eps, i):
        c0 = self.c0; assert self.B == 4
        if code == 0:       # t = w^h, s = j + h*t', Y = 4^t'
            s0, sigma, omega, tt = j, h, 2, w ** h
            pcs = []
            for e in divisors(h):
                P = Poly(cyclotomic_poly(2 * e, Y), Y)
                pcs.append(expand(sum(cf * Y ** a * w ** (P.degree() - a) for (a,), cf in P.terms())))
            Xr = Y ** h + tt
        elif code == 1:     # t = 4w^4, r = s - j even, Y = 2^(r/2)
            s0, sigma, omega, tt = j, 2, 1, 4 * w ** 4
            pcs = [Y * Y + 2 * Y * w + 2 * w * w, Y * Y - 2 * Y * w + 2 * w * w]; Xr = Y ** 4 + tt
        else:               # t = w^4, r odd, Y = 2^((r-1)/2), 4^r = 4 Y^4
            s0, sigma, omega, tt = j + 1, 2, 1, w ** 4
            pcs = [2 * Y * Y + 2 * Y * w + w * w, 2 * Y * Y - 2 * Y * w + w * w]; Xr = 4 * Y ** 4 + tt
        assert expand(prod(pcs) - Xr) == 0
        assert m == c0 * 4 ** j * tt - self.k
        n = self.nY(s0, sigma, omega)
        oc = c0
        while oc % 2 == 0: oc //= 2
        E = 2 * j - 2 + two_adic(c0)[0]
        pieces = [Integer(p) for p, v in factorint(oc).items() for _ in range(v)] + [n] + pcs
        assert len(pieces) == len(eps) and abs(i) <= E
        x = expand((n + m) / 4)
        assert expand(2 ** E * prod(pieces) - n * x) == 0
        d1 = prod([p for p, e in zip(pieces, eps) if e == 1], start=Integer(1))
        d2 = prod([p for p, e in zip(pieces, eps) if e == -1], start=Integer(1))
        if i >= 0: d1 = d1 * 2 ** i
        else: d2 = d2 * 2 ** (-i)
        self.window('W(m=%d,j=%d,%s,w=%d,h=%d;%s,%d)' % (m, j, ['cyc', 'sg', 'sg1'][code], w, h,
                    ''.join('+-0'[[1, -1, 0].index(e)] for e in eps), i), s0, sigma, omega, m, d1, d2)


# ES solutions of the primes used in divisor classes (found by search, checked exactly)
DIV_ES = {}
for q in (5, 7, 11, 13, 17, 19, 29, 41, 61, 127, 541):
    sol = es_brute(q); assert sol and check_sol(q, sol); DIV_ES[q] = sol


# ----------------------------------------------------------------------------------------------------------
# rule analysis
def int_coeffs(R):
    """R in Q[Y] -> (R1 in Z[Y] as coefficient list high->low, N) with R = R1/N."""
    num, den = fraction(together(R))
    P = Poly(num, Y); Dn = Poly(den, Y)
    assert Dn.degree() == 0, 'not a polynomial'
    dc = Rational(Dn.as_expr())
    co = [Rational(c) / dc for c in P.all_coeffs()]
    N = reduce(lcm, [c.q for c in co], 1)
    return [int(c * N) for c in co], N


def peval(co, v, mod=None):
    r = 0
    for c in co:
        r = (r * v + c) % mod if mod else r * v + c
    return r


def analyse(fam, rule):
    """returns dict: T (t-period), V (valid residues t mod T, for t >= tstar), tstar, polys."""
    n = rule['n']; x, y, z = rule['xyz']
    assert expand(4 * x * y * z - n * (x * y + y * z + z * x)) == 0, rule['label']
    om = rule['omega']
    polys = [int_coeffs(R) for R in (x, y, z)]
    # positivity threshold: every numerator > 0 for Y >= 2^(om*tpos)
    tpos = 0
    for co, N in polys:
        assert co[0] > 0, (rule['label'], 'leading coefficient')
        P = Poly(co, Y)
        while P.count_roots(Integer(2) ** (om * tpos), None) > 0 or P.eval(Integer(2) ** (om * tpos)) <= 0:
            tpos += 1
    tstar, T, conds = tpos, 1, []
    for co, N in polys:
        a, No = two_adic(N)
        tstar = max(tstar, -(-a // om))
        o = n_order(2 ** om, No) if No > 1 else 1
        T = lcm(T, o); conds.append((co, N))
    V = []
    for rho in range(T):
        t = tstar + ((rho - tstar) % T)
        if all(peval(co, pow(2, om * t, N), N) == 0 for co, N in conds):
            V.append(rho)
    return dict(T=T, V=V, tstar=tstar, polys=polys)


def eval_rule(rule, A, t):
    om = rule['omega']; v = 2 ** (om * t)
    out = []
    for co, N in A['polys']:
        r = peval(co, v)
        if r % N or r <= 0: return None
        out.append(r // N)
    return tuple(out)


def verify_family(fam, smax=SMAX, expect_L=None):
    t0 = time.time()
    infos = [analyse(fam, r) for r in fam.rules]
    for r, A in zip(fam.rules, infos):
        assert A['V'], ('rule never valid', r['label'])
    # s-period of each rule and coverage
    L = 1
    for r, A in zip(fam.rules, infos):
        L = lcm(L, r['sigma'] * A['T'])
    Sstar = max(r['s0'] + r['sigma'] * A['tstar'] for r, A in zip(fam.rules, infos))
    cover = {}
    for rho in range(L):
        for idx, (r, A) in enumerate(zip(fam.rules, infos)):
            if (rho - r['s0']) % r['sigma']: continue
            t = ((rho - r['s0']) // r['sigma']) % A['T']
            if t in A['V']:
                cover[rho] = idx; break
        else:
            raise AssertionError('%s: residue s = %d (mod %d) uncovered' % (fam.name, rho, L))
    used = sorted(set(cover.values()))
    # small s: some rule at exactly this s, else brute force
    direct = []
    for s in range(Sstar):
        n = fam.c0 * fam.B ** s + fam.k
        ok = False
        for r, A in zip(fam.rules, infos):
            if s >= r['s0'] and (s - r['s0']) % r['sigma'] == 0:
                sol = eval_rule(r, A, (s - r['s0']) // r['sigma'])
                if sol and check_sol(n, sol): ok = True; break
        if not ok:
            sol = es_brute(n); assert sol and check_sol(n, sol), (fam.name, s); direct.append(s)
    # numerics: build the solution from the covering rule for every Sstar <= s <= smax
    for s in range(Sstar, smax + 1):
        r = fam.rules[cover[s % L]]; A = infos[cover[s % L]]
        t = (s - r['s0']) // r['sigma']
        assert (s - r['s0']) % r['sigma'] == 0 and t >= A['tstar']
        n = fam.c0 * fam.B ** s + fam.k
        nco, nN = int_coeffs(r['n'])
        assert peval(nco, 2 ** (r['omega'] * t)) == n * nN      # the rule's n(Y) is n_s at this s
        sol = eval_rule(r, A, t)
        assert sol is not None and check_sol(n, sol), (fam.name, s, r['label'])
    if expect_L is not None:
        assert L == expect_L, (fam.name, L)
    log('[OK] %-14s %2d rules (%2d used), coverage period L = %d, all s >= %d covered; s < %d: %s; '
        'exact solutions checked for s <= %d  (%.1fs)' % (fam.name, len(fam.rules), len(used), L, Sstar, Sstar,
        ('brute force at s = %s' % direct) if direct else 'all by rules', smax, time.time() - t0))
    if TABLES:
        for idx in used:
            r, A = fam.rules[idx], infos[idx]
            P = r['sigma'] * A['T']
            cls = sorted((r['s0'] + r['sigma'] * v) % P for v in A['V'])
            log('      %-40s s mod %-5d in %s  (s >= %d)' % (r['label'], P, cls if len(cls) <= 24 else
                str(cls[:24]) + '... (%d)' % len(cls), r['s0'] + r['sigma'] * A['tstar']))
    return fam, infos, L


# ----------------------------------------------------------------------------------------------------------
# Theorem 4.1: n = 3*2^s + 1  (hand-checkable certificate: four Sophie-Germain window rules + six ET/divisor rules)
def fam_proth3():
    F = Fam('3*2^s+1', 3, 2, 1)
    X = Y; n = 48 * X ** 4 + 1; fp, fm = 2 * X * X + 2 * X + 1, 2 * X * X - 2 * X + 1; K = 3 * fp * fm
    assert expand(K - (n + 11) / 4) == 0
    for (a, b, c) in ((0, 2, 1), (0, 0, 2), (0, 2, 0), (0, 1, 2)):
        d = 3 ** a * fp ** b * fm ** c
        F.add('SG11 d=3^%d f+^%d f-^%d' % (a, b, c), 4, 4, 1, K, n * (K + d) / 11, n * K * (K + d) / (11 * d))
    n = 3 * Y + 1
    F.add('D7', 0, 1, 1, 2 * n / 7, 15 * n / 7, 30 * n)
    F.add('n=6 (7)', 0, 1, 1, 2 * (n + 1) / 7, 2 * n, 2 * n * (n + 1) / 7)
    F.add('n=7 (15)', 0, 1, 1, (4 * n + 2) / 15, 4 * n, 4 * n * (2 * n + 1) / 15)
    F.add('n=13 (15)', 0, 1, 1, (4 * n + 8) / 15, 4 * n, 2 * n * (n + 2) / 15)
    F.add('D5', 0, 1, 1, 2 * n / 5, 4 * n / 5, 4 * n)
    F.add('D61', 0, 1, 1, 16 * n / 61, 326 * n / 61, 2608 * n)
    return F


# second, independent certificate for 3*2^m+1 (EXP_105 Thm 2.2/2.3): trees for 3*4^s+1 and 6*4^s+1
def fam_c3_k1():
    F = Fam('3*4^s+1', 3, 4, 1)
    for p in (('II2', 7, 1, 55), ('II2', 2, 1, 55), ('II2', 1, 2, 7), ('I3', 1, 10, 7), ('D', 61), ('D', 7)):
        F.et(*p)
    F.z14(11, 1, 2, 1, 2, (-1, 0, 1, 0), 0); F.z14(11, 1, 2, 1, 2, (-1, 0, 0, 1), 0); F.z14(11, 1, 0, 1, 1, (0, -1, 0), 0)
    return F


def fam_c6_k1():
    F = Fam('6*4^s+1', 6, 4, 1)
    F.et('I3', 1, 5, 3); F.et('D', 5)
    return F


# Theorem 4.3: n = 63*2^s + 1
def fam_63():
    F = Fam('63*2^s+1', 63, 2, 1)
    n = 63 * Y ** 3 + 1; a, d = 5, 17
    b = (63 * Y ** 3 + 3 * Y ** 2 - 9 * Y + 28) / 340; c = (21 * Y + 64) / 340
    assert expand(c * n - (4 * a * b * c * d - a - b)) == 0
    F.add('II-ad (a,d)=(5,17), Y=2^(s/3)', 0, 3, 1, a * b * d, a * c * d * n, b * c * d * n)
    for p in (('D', 5), ('II2', 1, 2, 15), ('II2', 2, 2, 15), ('II2', 5, 3, 119), ('II2', 5, 2, 39),
              ('II2', 1, 5, 19), ('I1', 1, 146, 39), ('D', 11), ('II2', 3, 1, 11), ('II2', 1, 1, 11), ('D', 29),
              ('II2', 1, 11, 87), ('D', 127), ('II2', 1, 32, 127), ('I1', 1, 86, 23), ('II1', 1, 254, 15),
              ('I1', 1, 1405, 511), ('I2', 2, 43, 151)):
        F.et(*p)
    return F


# Theorem 4.5: n = 7*4^s + 9 (flattened 59-leaf tree of EXP_105, 35 distinct rules)
C7 = [('D', 11), ('D', 541), ('I3', 1, 5, 3), ('I3', 1, 11, 3), ('I3', 1, 206, 15),
      ('I3', 5, 19, 119), ('II2', 1, 2, 31), ('II2', 1, 8, 1887), ('II2', 2, 2, 111), ('II2', 7, 2, 671),
      ('II2', 19, 6, 455)]
C7W = [(19, 1, 0, 1, 1, (0, 0, -1), 0), (19, 1, 2, 1, 2, (-1, 0, 0, 1), 0), (19, 1, 2, 1, 2, (-1, 0, 1, 0), 0),
       (19, 1, 2, 1, 2, (0, 0, 0, -1), 0), (103, 1, 0, 4, 1, (-1, 0, 1), 0), (103, 1, 0, 4, 1, (0, -1, 0), 0),
       (103, 1, 0, 4, 1, (0, 0, -1), 0), (103, 2, 0, 1, 1, (-1, -1, 0), -1), (103, 2, 0, 1, 1, (-1, -1, 0), 2),
       (103, 2, 0, 1, 1, (-1, 0, -1), 2), (103, 2, 0, 1, 1, (0, 0, -1), 1), (103, 2, 0, 1, 3, (-1, -1, 0, -1), -1),
       (103, 2, 0, 1, 3, (-1, -1, 0, 1), 2), (103, 2, 0, 1, 3, (-1, 0, -1, 1), 1), (103, 2, 0, 1, 3, (-1, 0, 0, -1), 2),
       (103, 2, 0, 1, 3, (-1, 0, 1, -1), 1), (103, 2, 0, 1, 3, (-1, 1, 1, 0), -2), (103, 2, 0, 1, 3, (0, -1, 0, -1), 1),
       (103, 2, 0, 1, 3, (0, -1, 0, 1), 0), (103, 2, 0, 1, 9, (-1, -1, -1, 0, 0), -1),
       (103, 2, 0, 1, 9, (-1, -1, 0, -1, 0), 0), (663, 2, 0, 6, 1, (-1, 0, -1), 1)]


def fam_c7_k9():
    F = Fam('7*4^s+9', 7, 4, 9)
    for w in C7W: F.z14(*w)
    for p in C7: F.et(*p)
    return F


# Theorem 4.7: n = 4^s + 105 (13 ET/divisor classes + one cubic window class)
def fam_105():
    F = Fam('4^s+105', 1, 4, 105)
    u = Y; n = 256 * u ** 3 + 105; A = (64 * u ** 3 + 2 * u ** 2 - 2 * u + 66) / 151
    assert expand(4 * 64 * (u ** 3 + 1) - n - 151) == 0 and expand(151 * A - 2 * (32 * u + 33) * (u * u - u + 1)) == 0
    F.add('W151 cubic, u=4^((s-4)/3)', 4, 3, 2, 64 * (u ** 3 + 1), n * A, 32 * n * (u + 1) * A)
    for p in (('D', 11), ('II2', 1, 1, 11), ('II2', 1, 3, 11), ('D', 41), ('II2', 2, 53, 1271), ('II2', 3, 22, 527),
              ('II2', 1, 6, 143), ('II2', 1, 2, 151), ('D', 13), ('D', 19), ('II2', 5, 1, 19), ('II2', 2, 5, 39),
              ('II2', 1, 2, 39)):
        F.et(*p)
    return F


# Theorem 4.9: n = 4^s + k, nine k (z8 certificates)
NINE = {9: [('D', 5), ('II2', 2, 2, 15)],
        57: [('II2', 2, 2, 15), ('II2', 2, 1, 7), ('II2', 1, 1, 7), ('D', 11), ('II2', 1, 1, 11), ('II2', 1, 1, 31),
             ('II2', 1, 8, 31), ('II2', 7, 9, 2015)],
        81: [('D', 5), ('II2', 1, 2, 15)],
        129: [('D', 5), ('II2', 2, 2, 15)],
        153: [('II2', 1, 2, 15), ('D', 7), ('II2', 1, 1, 7), ('D', 13)],
        177: [('II2', 2, 2, 15), ('II2', 1, 1, 7), ('II2', 1, 2, 7), ('II2', 1, 2, 39)],
        201: [('D', 5), ('II2', 1, 2, 15)],
        225: [('II2', 2, 1, 7), ('II2', 1, 1, 7), ('II2', 1, 2, 39), ('D', 17), ('II2', 101, 5, 2019), ('I1', 1, 679, 19)],
        249: [('D', 5), ('II2', 2, 2, 15)]}


def fam_nine(k):
    F = Fam('4^s+%d' % k, 1, 4, k)
    for p in NINE[k]: F.et(*p)
    return F


# ----------------------------------------------------------------------------------------------------------
# Theorem 5.5 / Computation 5.6 (Theorem W): limit-level relations for constant-gap families through mu = 0.
def thmW(c0, k):
    """all (w, m, e1, a1, e2, a2) with m = 4 c0 w^4 - k, 0 < m <= B(m), a1 a2 | M = 4^J + m (a_i odd),
    e_i = -2 delta_i + nu_i (2 delta_i in {0,1,2}, 2delta_1 + 2delta_2 <= 2, nu_i in {0, 2J}, nu_1 + nu_2 <= 2J),
    m | 2^e1 a1 + 2^e2 a2 in Z[1/2].  (No parity filter: every relation is reported.)"""
    J = (c0 + k).bit_length() // 2
    assert 4 ** J == c0 + k and k % 8 == 1 and c0 % 2 == 1
    assert all(v < 4 for v in factorint(c0).values())
    E = 2 * J + 2
    def B(m):
        M = 4 ** J + m; r = Fr(M, m)
        return max(2 ** E * 4 ** J + 2 ** (2 * E + 2) * r * r, 2 ** E * 4 * r * r + 4 ** J)
    es = set()
    for t1 in (0, 1, 2):
        for t2 in (0, 1, 2 - t1):
            for nu in ((0, 0), (2 * J, 0), (0, 2 * J)):
                es.add((-t1 + nu[0], -t2 + nu[1]))
    hits, ws, w = [], [], 1
    while True:
        m = 4 * c0 * w ** 4 - k
        if m > 0 and m > B(m): break
        if m > 0:
            ws.append(w); M = 4 ** J + m; ds = [d for d in divisors(M) if d % 2]
            for a1 in ds:
                for a2 in ds:
                    if (M // a1) % a2: continue
                    for e1, e2 in es:
                        lo = min(e1, e2)
                        if (a1 * 2 ** (e1 - lo) + a2 * 2 ** (e2 - lo)) % m == 0:
                            hits.append((w, m, e1, a1, e2, a2))
        w += 2
    return J, ws, hits


def irreducible_all_D(c0, k):
    """Capelli: c0 Y^D + k irreducible over Q for every D >= 1 iff -k/c0 is not a p-th power (p prime) and not in -4Q^4."""
    from sympy import integer_nthroot
    r = Fr(k, c0)                       # -k/c0 = -r; (-r) is a p-th power for odd p iff r is; never a square (r > 0)
    for p in range(3, 2 * max(k, c0).bit_length() + 3, 2):
        a, ea = integer_nthroot(r.numerator, p); b, eb = integer_nthroot(r.denominator, p)
        if ea and eb: return False
    q = r / 4                           # -r in -4Q^4  <=>  r/4 is a 4th power
    a, ea = integer_nthroot(q.numerator, 4); b, eb = integer_nthroot(q.denominator, 4)
    return not (ea and eb)


def boxed():
    """Lemma 5.10: all positive solutions of a(m1 m2 d - 4) = m1 + 16 m2; bounds a <= 81, m1 <= 100, m1 d <= 120."""
    sols = []
    for a in range(1, 200):
        for m1 in range(1, 400):
            for d in range(1, 400 // m1 + 2):
                den = a * m1 * d - 16
                if den <= 0 or (m1 + 4 * a) % den: continue
                m2 = (m1 + 4 * a) // den
                assert a * (m1 * m2 * d - 4) == m1 + 16 * m2
                sols.append((a, d, m1, m2))
    assert all(a <= 81 and m1 <= 100 and m1 * d <= 120 for a, d, m1, m2 in sols)
    return sols


def verify_obstructions():
    t0 = time.time()
    for (c0, k) in ((15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9)):
        assert irreducible_all_D(c0, k)
        J, ws, hits = thmW(c0, k)
        assert not hits, (c0, k, hits)
        log('[OK] Theorem W  (c0,k)=(%d,%d), J=%d: windows m=4c0w^4-k checked for w in %s: no limit relation'
            % (c0, k, J, ws))
    for (c0, k), mm in (((3, 1), {11}), ((7, 9), {19}), ((23, 41), {51}), ((39, 25), {131})):
        J, ws, hits = thmW(c0, k)
        assert {h[1] for h in hits} == mm, (c0, k, hits)
        log('[OK] Theorem W positive control (c0,k)=(%d,%d): relations only at m = %s, e.g. %s'
            % (c0, k, sorted(mm), hits[0]))
    sols = boxed()
    assert len(sols) == 39
    odd = [s for s in sols if s[0] % 2 and s[1] % 2]
    div15 = [(a, d, (4 * a * a * d + 1) // 15) for a, d, m1, m2 in odd if (4 * a * a * d + 1) % 15 == 0]
    assert div15 == [(1, 11, 3)] or set(div15) == {(1, 11, 3)}, div15
    log('[OK] Lemma 5.10: a(m1 m2 d - 4) = m1 + 16 m2 has exactly %d positive solutions (%d with a, d odd, %d '
        'distinct odd pairs); 15 | 4a^2d+1 only for (a,d) = (1,11), quotient 3  (%.1fs)'
        % (len(sols), len(odd), len({(s[0], s[1]) for s in odd}), time.time() - t0))


if __name__ == '__main__':
    verify_obstructions()
    log('ES solutions used by divisor classes:', DIV_ES)
    verify_family(fam_proth3(), expect_L=120)
    verify_family(fam_c3_k1()); verify_family(fam_c6_k1())
    verify_family(fam_63())
    verify_family(fam_c7_k9())
    verify_family(fam_105())
    for k in NINE: verify_family(fam_nine(k), smax=min(SMAX, 600))
    log('total %.1fs' % (time.time() - T0))
