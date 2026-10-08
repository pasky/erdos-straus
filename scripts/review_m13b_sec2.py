"""R95: from-scratch check of Lemmas 2.1-2.4 / Cor 2.5 (forward maps -> ES identity, M_T<=N<=M_T^2,
and recoverability by the reviewer's inverse maps in review_m13b_enum.invert).  usage: N seed"""
import sys, random
from fractions import Fraction as Fr
sys.path.insert(0, __import__('os').path.dirname(__file__))
import review_m13b_lem11 as L
from review_m13b_enum import invert, ok_family
tp = L.tpart
def fwd(fam, P):
    if fam in ('II3', 'I3', 'I1'):
        a, d, e = P; aT, dT = tp(a), tp(d); ap, dp = a // aT, d // dT; lam = aT*aT*dT
        B = 1 if fam == 'I1' else tp(e); g = e // B
        assert (e+1) % (4*ap*dp) == 0; m = (e+1) // (4*ap*dp)
        assert (lam*ap + m) % g == 0, ('j not integral', fam, P); j = (lam*ap + m) // g
        return B*lam, (dp*m*j, lam*ap*dp*j, B*lam*ap*dp*m)
    if fam in ('II1', 'I4'):
        a, b, e = P; F = tp(a*b); c = (a+b) // e; assert ((e+1)*F) % (4*a*b) == 0; i = (e+1)*F // (4*a*b)
        return F, (i*a*b, i*a*c, i*b*c)
    if fam == 'II2':
        a, d, f = P; F = tp(f); fp = f // F; m = (f+1) // (4*a*d); assert (a+m) % fp == 0; j = (a+m) // fp
        return F, (a*m*d*F, a*j*d, m*j*d)
    if fam == 'I2':
        a, c, f = P; A, B = tp(a*c), tp(f); acp = a*c // A; fp = f // B
        assert (f+1) % (4*acp) == 0 and (a+c) % fp == 0; t = (f+1) // (4*acp); h = (a+c) // fp
        return A*B, (c*t*h, a*t*h, B*a*c*t)
n = int(sys.argv[1]); random.seed(int(sys.argv[2])); L.BIAS = True
bad = 0; tested = {}
for fam in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
    tested[fam] = 0; tries = 0
    while tested[fam] < n and tries < 50 * n:
        tries += 1; P = L.gen(fam); r = ok_family(fam, P)
        if not r: continue
        M, MT, rs = r
        N, (X, Y, Z) = fwd(fam, P)
        okid = Fr(1, X) + Fr(1, Y) + Fr(1, Z) == Fr(4, N)
        okb = MT <= N <= MT * MT
        okinv = (fam, P) in {(f, Q) for f, Q, _ in invert(N, tuple(sorted((X, Y, Z))))}
        tested[fam] += 1
        if not (okid and okb and okinv): bad += 1; print('FAIL', fam, P, N, MT, okid, okb, okinv)
print('Section 2 forward/inverse test: failures', bad, 'tested', tested)
