"""R177 from-scratch check of bsD_brauer_cores numerics: the cubic tame symbol of alpha_zeta = (-u1/u3, -u2/u3)_zeta,
zeta = primitive cube root of 1, K = Q(zeta), at the two primes w, wbar above p = 1 (mod 3), on all ES solutions
4/p = 1/u1 + 1/u2 + 1/u3, u1 <= u2 <= u3.  Residue field F_p; w: zeta -> omega, wbar: zeta -> omega^2.
Tame symbol (a,b)_w = ((-1)^{v(a)v(b)} a^{v(b)} / b^{v(a)})^{(p-1)/3} mod p = omega^k  (k in Z/3; convention-free up to
an overall sign, which does not affect (non-)constancy).  Also: at every other prime l = 1 (mod 3) dividing u1 u2 u3, the
w-exponents over the two w | l sum to 0 (Theorem 1 for odd order, explicit form).
Run: PYTHONPATH=scripts uv run python scripts/review_ld_cubic.py P
"""
import sys
from fractions import Fraction
from collections import Counter
from sympy import primerange, factorint

P = int(sys.argv[1])


def sols(p):
    out = []
    for u1 in range(p // 4 + 1, 3 * p // 4 + 1):
        r1 = Fraction(4, p) - Fraction(1, u1)
        if r1 <= 0: continue
        lo = max(u1, int(1 / r1) + 1 if (1 / r1).denominator != 1 else int(1 / r1))
        hi = int(2 / r1)
        for u2 in range(lo, hi + 1):
            r2 = r1 - Fraction(1, u2)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= u2:
                out.append((u1, u2, r2.denominator))
    return out


def val(x, l):
    v = 0
    while x % l == 0: x //= l; v += 1
    return v


def tame_exp(a, b, l, omega):
    """a, b nonzero Fractions; returns k with symbol = omega^k in F_l."""
    va = val(a.numerator, l) - val(a.denominator, l); vb = val(b.numerator, l) - val(b.denominator, l)
    t = Fraction((-1) ** (va * vb)) * a ** vb / b ** va
    s = pow(t.numerator % l * pow(t.denominator % l, -1, l) % l, (l - 1) // 3, l)
    return {1: 0, omega: 1, omega * omega % l: 2}[s]


def cube_root_unity(l):
    for g in range(2, l):
        w = pow(g, (l - 1) // 3, l)
        if w != 1: return w


nonconst = 0; tested = 0; sumfail = 0
for p in primerange(7, P):
    if p % 3 != 1: continue
    om = cube_root_unity(p)
    S = sols(p)
    for u in S:
        assert Fraction(4, p) == sum(Fraction(1, x) for x in u)
    cnt = Counter()
    for u1, u2, u3 in S:
        a, b = Fraction(-u1, u3), Fraction(-u2, u3)
        k = tame_exp(a, b, p, om)
        kbar = tame_exp(a, b, p, om) * 2 % 3  # same F_p element read against omega^2 (embedding of wbar)
        # direct recomputation for wbar
        kb2 = {1: 0, om * om % p: 1, om: 2}[pow(om, k, p)]
        assert kbar == kb2 and (k + kbar) % 3 == 0
        cnt[k] += 1
        for l in factorint(u1 * u2 * u3):
            if l % 3 == 1 and l != p:
                ol = cube_root_unity(l)
                k1 = tame_exp(a, b, l, ol); k2 = {0: 0, 1: 2, 2: 1}[k1]
                sumfail += (k1 + k2) % 3 != 0
    tested += 1
    nonconst += len(cnt) > 1
    if p in (79, 7, 13, 601) or len(cnt) <= 1:
        print(p, '#sols', len(S), 'cube classes at w|p:', dict(cnt))
print('primes p = 1 (3), 7 <= p <', P, ':', tested, ' non-constant at w|p:', nonconst, ' sum failures at other l:', sumfail)
