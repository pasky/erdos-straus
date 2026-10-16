# z19_binom.py — all two-constant "binomial menus" of Type I/II at the unit-square point mu = 0 of n = c0*2^s + k
# (EXP_OPEN.md §2).  In each menu a witness f is a polynomial factor (f = kappa*P, P monic) of a binomial B = A Y^D + C
# (Y = 2^{s/D}), the cofactor is f' = B/f, and two parameters are fixed by congruences modulo a FIXED modulus Mod:
#   II-ac : (a,c) const, B = c n + a,       Mod = 4ac, f = -1,  d = (f+1)/(4ac), b = f'
#   II-ad : (a,d) const, B = n + 4a^2 d,    Mod = 4ad, f = -n,  b = (f+n)/(4ad), c = (f'+1)/(4ad)   (f = gap 4x - n)
#   I-ac  : (a,c) const, B = a n + c,       Mod = 4ac, f = -n,  d = (f+n)/(4ac), b = f'   (Type I: x = abdn, y = acd, z = bcd)
#   II-cd : (c,d) const, B = 4c^2 d n + 1,  Mod = 4cd, f = -1, f' = -1 (a = (f+1)/(4cd), b = (f'+1)/(4cd))
# (The remaining pairs give constant gap = Theorem W, constant ratio = Cor 1.7, or ET classes / Type I const (c,d), all
# dead at mu = 0.)  Validity near mu = 0 <=> integrality of every parameter at Y = 1 (Z[1/2]) and Y = 0 (Z_(2))
# (MENU_LADDER Lemma 2.1); positivity is automatic (P has no positive root, kappa > 0).  f(0) is a 2-adic unit in every
# menu (f = -1 or -n mod 4), so v2(kappa), hence e = v2(f(1)), is forced and the odd part w of f(1) runs over the
# progression w = r(1) 2^{-e} (mod odd(Mod)), w | odd(B(1)).
# Usage: PYTHONPATH=scripts uv run python scripts/z19_binom.py c0 k MENU PARMAX UVMAX PMAX [mult,list]
import sys, itertools
from fractions import Fraction as Fr
from math import gcd
from sympy import integer_nthroot, divisors, symbols, factor_list, Poly, primerange
c0, k = int(sys.argv[1]), int(sys.argv[2]); MENU = sys.argv[3]
PARMAX, UVMAX, PMAX = map(int, sys.argv[4:7]); MULT = [int(t) for t in sys.argv[7].split(',')] if len(sys.argv) > 7 else [1]
J = (c0 + k).bit_length() // 2; assert 4 ** J == c0 + k
Y = symbols('Y')
def v2(x):
    x = Fr(x); n, d = x.numerator, x.denominator; v = 0
    if n == 0: return 10 ** 9
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def odd(x):
    x = abs(x)
    while x % 2 == 0: x //= 2
    return x
def isint1(x): return odd(Fr(x).denominator) == 1          # in Z[1/2]
def isint0(x): return Fr(x).denominator % 2 == 1           # in Z_(2)
def cong1(x, r, q): x = Fr(x) - r; return isint1(x) and (q == 1 or x.numerator % q == 0)
def cong0(x, r, t): x = Fr(x) - r; return isint0(x) and v2(x) >= t
def kpow(K, e, mul=1):
    K = K / mul
    if K <= 0: return False
    return integer_nthroot(K.numerator, e)[1] and integer_nthroot(K.denominator, e)[1]
# ---- candidate parameter tuples (menu-specific); each gives (A, C, Mod, conds) ----
cands = []
def add(par, A, C, Mod):
    K = Fr(C, A); Ds = set()
    for p in primerange(3, PMAX + 1):
        if kpow(K, p): Ds |= {p * t for t in MULT}
    if kpow(K, 4, 4): Ds |= {4 * t for t in MULT}
    if Ds: cands.append((par, A, C, Mod, sorted(Ds)))
if MENU in ('II-ac', 'I-ac'):
    # K = (ck+a)/(c c0) (II-ac) or (ak+c)/(a c0) (I-ac) = (u/v)^p or 4(u/v)^4:  generate directly
    for p in list(primerange(3, PMAX + 1)) + ['sg']:
        e = 4 if p == 'sg' else p; mul = 4 if p == 'sg' else 1
        for u in range(1, UVMAX + 1):
            for v in range(1, UVMAX + 1):
                if gcd(u, v) != 1: continue
                num = mul * c0 * u ** e - k * v ** e
                if num <= 0: continue
                for cp in range(1, PARMAX + 1):
                    X1, X2 = cp * num, cp * v ** e         # (a, c) for II-ac ; (c, a) for I-ac
                    if MENU == 'II-ac': add((X1, X2), X2 * c0, X2 * k + X1, 4 * X1 * X2)
                    else: add((X2, X1), X2 * c0, X2 * k + X1, 4 * X1 * X2)
elif MENU == 'II-ad':
    # n + 4a^2 d: K = (k + 4a^2 d)/c0 = (u/v)^p => 4a^2 d = c0 u^p/v^p - k, v^p | c0
    for p in list(primerange(3, PMAX + 1)) + ['sg']:
        e = 4 if p == 'sg' else p; mul = 4 if p == 'sg' else 1
        for v in [vv for vv in range(1, 10) if c0 % (vv ** e) == 0]:
            for u in range(1, UVMAX + 1):
                if gcd(u, v) != 1: continue
                t = mul * (c0 // v ** e) * u ** e - k
                if t <= 0 or t % 4: continue
                t //= 4
                for a in range(1, PARMAX + 1):
                    if t % (a * a): continue
                    add((a, t // (a * a)), c0, k + 4 * t, 4 * a * (t // (a * a)))
elif MENU == 'II-cd':
    for c in range(1, PARMAX + 1):
        for d in range(1, PARMAX + 1):
            add((c, d), 4 * c * c * d * c0, 4 * c * c * d * k + 1, 4 * c * d)
r1 = {'II-ac': (-1, None), 'II-ad': (-4 ** J, -1), 'I-ac': (-4 ** J, None), 'II-cd': (-1, -1)}[MENU]   # residues at Y=1
r0 = {'II-ac': (-1, None), 'II-ad': (-k, -1), 'I-ac': (-k, None), 'II-cd': (-1, -1)}[MENU]          # residues at Y=0
hits = []; tested = 0
for par, A, C, Mod, Ds in cands:
    q = odd(Mod); t2 = v2(Mod); B1 = A + C; B0 = C
    for D in Ds:
        facs = [Poly(f, Y) for f, e in factor_list(Y ** D + Fr(C, A))[1] for _ in range(e)]
        for r in range(1, len(facs) + 1):
            for sub in itertools.combinations(range(len(facs)), r):
                P = Poly(1, Y)
                for i in sub: P = P * facs[i]
                P = P.monic(); P1 = Fr(P.eval(1)); P0 = Fr(P.eval(0))
                i2 = -v2(P0); e1 = i2 + v2(P1); P1o = P1 / Fr(2) ** v2(P1)
                Bo = odd(B1.numerator if isinstance(B1, Fr) else B1)
                if q > 1:
                    w0 = (Fr(r1[0]) * Fr(2) ** (-e1)); w0 = (w0.numerator * pow(w0.denominator, -1, q)) % q
                    wc = range(w0 if w0 else q, Bo + 1, q)
                else: wc = divisors(Bo)
                for wv in wc:
                    if wv % 2 == 0 or Bo % wv: continue
                    tested += 1
                    kap = Fr(2) ** i2 * wv / P1o
                    f1, f0 = kap * P1, kap * P0; g1, g0 = Fr(B1) / f1, Fr(B0) / f0
                    ok = cong1(f1, r1[0], q) and cong0(f0, r0[0], t2) and isint1(g1) and isint0(g0)
                    if ok and r1[1] is not None: ok = cong1(g1, r1[1], q) and cong0(g0, r0[1], t2)
                    if ok: hits.append((par, D, str(P.as_expr()), kap))
print('c0=%d k=%d menu %s PARMAX=%d UV<=%d p<=%d mult=%s: %d parameter tuples, %d kappa tests, %d hits'
      % (c0, k, MENU, PARMAX, UVMAX, PMAX, MULT, len(cands), tested, len(hits)))
for h in hits[:20]: print('  params=%s D=%d P=%s kappa=%s' % h)
