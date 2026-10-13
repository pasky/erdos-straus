"""O177 (bsD_): the cubic norm-residue class alpha_{zeta_3} = (-u1/u3, -u2/u3)_{zeta_3} of Bright-Loughran (Prop 2.6) on
ES solutions u = (x,y,z) of 4/p = 1/x+1/y+1/z, p = 1 (mod 3) prime.  At the two primes w, wbar of Q(zeta_3) above p
the tame symbol of a rational point is t resp. t^{-1} (identifying mu_3(F_p) via zeta -> omega resp. omega^2), so the
sum of invariants over w | p is 0 identically (corestriction collapse, bsD_brauer_cores Thm 1); we check that the
individual value t is NOT constant over solutions (the cubic data exist on points; no law constrains them).
Run: PYTHONPATH=scripts uv run python scripts/bsD_cubic_symbol.py PMAX
"""
import sys
from collections import Counter
from math import gcd
from sympy import primerange

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400


def sols(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        num, den = 4 * x - n, n * x            # 1/y + 1/z = num/den
        if num <= 0:
            continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            zn, zd = num * y - den, den * y
            if zn > 0 and zd % zn == 0:
                out.append((x, y, zd // zn))
    return out


def v(a, p):
    k = 0
    while a % p == 0:
        a //= p
        k += 1
    return k


def tame(a_num, a_den, b_num, b_den, p):
    """tame symbol at p of (a,b), a,b rationals; returns element of F_p^x raised to (p-1)/3."""
    va = v(a_num, p) - v(a_den, p)
    vb = v(b_num, p) - v(b_den, p)
    # u = (-1)^{va vb} a^{vb} / b^{va}, reduce mod p
    def red(nm, dn):
        while nm % p == 0:
            nm //= p
        while dn % p == 0:
            dn //= p
        return nm % p * pow(dn % p, -1, p) % p
    A, B = red(a_num, a_den), red(b_num, b_den)
    w = (pow(-1, va * vb, p) * pow(A, vb, p) * pow(pow(B, va, p), -1, p)) % p
    # remaining valuation part: a^{vb}/b^{va} has valuation 0 automatically
    return pow(w, (p - 1) // 3, p)


tot = Counter()
for p in primerange(7, PMAX):
    if p % 3 != 1:
        continue
    vals = Counter()
    for (x, y, z) in sols(p):
        vals[tame(-x, z, -y, z, p)] += 1
    nonconst = len(vals) > 1
    tot[nonconst] += 1
    if p < 120:
        print(p, 'cubic tame symbol values over ES solutions:', dict(vals))
print('primes p=1(3) <', PMAX, ': symbol non-constant over solutions for', tot[True], 'constant for', tot[False])
