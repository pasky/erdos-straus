"""z18: Type II families a = lam (const), b = lam*r*(Y^2+pY+q), d = 15*quot(Y^D, b1)/(4 lam^2 r) / c0 scaling,
m = -n mod b1 (linear), c = (a+b)/m, for n = c0*Y^D + k, at mu = 0 (values at Y=1 must be in Z[1/2], at Y=0 in Z_(2)).
(p, q) range over rationals of bounded height.  Every hit is re-verified exactly on actual s (z18_verify).
usage: z18_quad.py c0 k D H"""
import sys, math
from fractions import Fraction as Fr
from itertools import product
c0, k, D, H = map(int, sys.argv[1:5])
def val(x, p):
    if x == 0: return math.inf
    x = Fr(x); v = 0; a, b = x.numerator, x.denominator
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v
def pf(x):
    s = set(); x = abs(x); d = 2
    while d*d <= x:
        while x % d == 0: s.add(d); x //= d
        d += 1
    if x > 1: s.add(x)
    return s
def divmod_mono(D, p, q):
    """Y^D = Q(Y)*(Y^2+pY+q) + (al*Y + be); return Q coeffs (low->high), al, be"""
    # long division
    num = [Fr(0)]*D + [Fr(1)]
    Q = [Fr(0)]*(D-1)
    for i in range(D, 1, -1):
        co = num[i]
        if co == 0: continue
        Q[i-2] = co
        num[i] -= co; num[i-1] -= co*p; num[i-2] -= co*q
    return Q, num[1], num[0]
rats = sorted({Fr(u, v) for u in range(-H, H+1) for v in range(1, H+1)})
hits = 0
for p, q in product(rats, rats):
    Q, al, be = divmod_mono(D, p, q)
    # n mod b1 = c0*(al Y + be) + k ; m = -(that)
    mA, mB = -c0*al, -c0*be - k          # m = mA*Y + mB
    if mA <= 0: continue
    Y0 = -mB/mA
    bY0 = Y0*Y0 + p*Y0 + q
    if bY0 >= 0: continue
    r = -1/bY0
    # c = lam*r*(Y + Y0 + p)/mA ; d = c0*Q/(4 lam^2 r) ; b = lam*r*b1
    Q1, Q0 = sum(Q), Q[0]
    vals = {'b': (r*(1+p+q), r*q), 'c': (r*(1+Y0+p)/mA, r*(Y0+p)/mA), 'd': (Fr(c0)*Q1/(4*r), Fr(c0)*Q0/(4*r))}
    primes = {2}
    for x in [v for pr in vals.values() for v in pr]:
        if x != 0: primes |= pf(Fr(x).numerator) | pf(Fr(x).denominator)
    ok = True; lam = Fr(1)
    for ell in primes:
        i = 1 if ell == 2 else 0
        lo = max(0, -val(vals['b'][i], ell), -val(vals['c'][i], ell))
        vd = val(vals['d'][i], ell)
        if 2*lo > vd: ok = False; break
        lam *= Fr(ell)**lo
    # constant a = lam must be integral at both specializations; also the other specialization of each prime is irrelevant
    if ok:
        hits += 1
        print(f'HIT D={D} p={p} q={q} r={r} lam={lam} m={mA}*Y+{mB}', flush=True)
print('hits', hits, 'grid', len(rats)**2)
