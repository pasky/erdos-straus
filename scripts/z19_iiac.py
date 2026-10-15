# z19_iiac.py — the binomial menu (II-ac) at the unit-square point mu = 0 of n = c0*2^s + k (EXP_OPEN.md §2).
# Type II with a, c CONSTANT: c n + a = b f, f = 4acd - 1, so f is a polynomial factor (times kappa) of the binomial
# c c0 Y^D + (ck + a), Y = 2^{s/D}.  Family valid near mu = 0 iff (MENU_LADDER Lemma 2.1)
#   d = (f+1)/(4ac), b = (cn+a)/f are integral at Y=1 (in Z[1/2]) and Y=0 (in Z_(2))  [positivity is automatic].
# For each (a, c) with reducible binomial (Capelli: K = (ck+a)/(c c0) in Q^p, p odd prime, or 4Q^4), every monic factor
# product P of Y^D + K (D = p or 4, plus D = 2p, 3p, 4p optionally) and every kappa allowed by b(1) in Z[1/2], test.
# Usage: PYTHONPATH=scripts uv run python scripts/z19_iiac.py c0 k AMAX CPMAX [PMAX] [mult,list] [UVMAX]
import sys, itertools
from fractions import Fraction as Fr
from math import gcd
from sympy import integer_nthroot, divisors, symbols, factor_list, Poly, primerange
c0, k, AMAX, CMAX = map(int, sys.argv[1:5]); PMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 13
MULT = [int(t) for t in sys.argv[6].split(',')] if len(sys.argv) > 6 else [1]
Y = symbols('Y')
def v2(x):
    x = Fr(x); n, d = x.numerator, x.denominator; v = 0
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def odd(x):
    while x % 2 == 0: x //= 2
    return x
def is_pow(fr, p):
    n, d = fr.numerator, fr.denominator
    a, ea = integer_nthroot(n, p); b, eb = integer_nthroot(d, p)
    return ea and eb
hits = []; tested = 0
# generate (a, c) with reducible binomial directly: K = (ck+a)/(c c0) = beta^p (or 4 beta^4), beta = u/v:
#   a = c'(c0 u^p - k v^p), c = c' v^p   (resp. a = c'(4 c0 u^4 - k v^4), c = c' v^4)
UVMAX = int(sys.argv[7]) if len(sys.argv) > 7 else 12
pairs = {}
for p in list(primerange(3, PMAX + 1)) + ['sg']:
    e = 4 if p == 'sg' else p; mul = 4 if p == 'sg' else 1
    for u in range(1, UVMAX + 1):
        for v in range(1, UVMAX + 1):
            if gcd(u, v) != 1: continue
            num = mul * c0 * u ** e - k * v ** e
            if num <= 0: continue
            for cp in range(1, CMAX + 1):
                a, c = cp * num, cp * v ** e
                if a > AMAX: break
                pairs.setdefault((a, c), set()).update(e * t for t in MULT)
for (a, c), Dset in sorted(pairs.items()):
        Ds = sorted(Dset)
        K = Fr(c * k + a, c * c0)
        for D in sorted(set(Ds)):
            facs = [Poly(f, Y) for f, e in factor_list(Y ** D + K)[1] for _ in range(e)]
            q = odd(a) * odd(c); t2 = 2 + v2(a * c)
            for r in range(1, len(facs)):
                for sub in itertools.combinations(range(len(facs)), r):
                    P = Poly(1, Y)
                    for i in sub: P = P * facs[i]
                    P = P.monic(); P1 = Fr(P.eval(1)); P0 = Fr(P.eval(0))
                    i2 = -v2(P0)                          # kappa P(0) must be a 2-adic unit
                    e1 = i2 + v2(P1)                      # v2(f(1)) is forced
                    Bodd = odd(c * (c0 + k) + a)
                    w0 = (-pow(2, -e1, q)) % q if q > 1 else 0
                    wcands = range(w0 if w0 else q, Bodd + 1, q) if q > 1 else divisors(Bodd)
                    for wv in wcands:                      # odd part w of f(1): w = -2^{-e1} (mod q), w | Bodd
                        if wv % 2 == 0 or Bodd % wv: continue
                        tested += 1
                        P1o = Fr(P1) / Fr(2) ** v2(P1)
                        kap = Fr(2) ** i2 * Fr(wv) / P1o
                        f1 = kap * P1; f0 = kap * P0
                        # (A) f(1) = -1 mod q in Z[1/2]
                        n1, d1 = f1.numerator, f1.denominator
                        if odd(d1) != 1: continue
                        if (n1 + d1) % q: continue
                        # (B) f(0) = -1 mod 2^t2 in Z_(2)
                        n0, d0 = f0.numerator, f0.denominator
                        if d0 % 2 == 0: continue
                        if (n0 * pow(d0, -1, 2 ** t2) + 1) % (2 ** t2): continue
                        # (C) b(1) = (c(c0+k)+a)/f(1) in Z[1/2];  (D) b(0) = (ck+a)/f(0) in Z_(2)
                        b1 = Fr(c * (c0 + k) + a) / f1; b0 = Fr(c * k + a) / f0
                        if odd(b1.denominator) != 1 or b0.denominator % 2 == 0: continue
                        hits.append((a, c, D, str(P.as_expr()), kap))
print('c0=%d k=%d a<=%d cprime<=%d p<=%d uv<=%d mult=%s: %d (a,c) pairs, %d (factor,kappa) tests, %d hits' % (c0, k, AMAX, CMAX, PMAX, UVMAX, MULT, len(pairs), tested, len(hits)))
for h in hits[:30]: print('  a=%d c=%d D=%d P=%s kappa=%s' % h)
