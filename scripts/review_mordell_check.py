"""R80 from-scratch checker for POINTWISE_MORDELL Theorem 3.1 (does not import scripts/mordell_*).

Family formulas re-derived directly from ET (arXiv:1107.1010) varieties (2.1)-(2.9), (2.13)-(2.21):
  Type I : (x,y,z) = (a b d n, a c d, b c d)
  Type II: (x,y,z) = (a b d, a c d n, b c d n)
Each family fixes three coordinates; the others are rational functions (here polynomials) of n.
"""
import json, sys
from fractions import Fraction as Fr
from math import gcd

def sol(fam, P, n):
    n = Fr(n)
    if fam == 'I1':      # a,d,f ; f | 4a^2 d+1
        a, d, f = P; e = Fr(4*a*a*d+1, f); b = (n*e+1)/(4*a*d); c = (n+f)/(4*a*d)
        return a*b*d*n, a*c*d, b*c*d
    if fam == 'I2':      # a,c,f
        a, c, f = P; d = (n+f)/(4*a*c); b = (n*a+c)/f
        return a*b*d*n, a*c*d, b*c*d
    if fam == 'I3':      # c,d,f
        c, d, f = P; a = (n+f)/(4*c*d); b = (n+(n*n+4*c*c*d)/f)/(4*c*d)
        return a*b*d*n, a*c*d, b*c*d
    if fam == 'I4':      # a,b,e ; e | a+b
        a, b, e = P; c = Fr(a+b, e); d = (n*e+1)/(4*a*b)
        return a*b*d*n, a*c*d, b*c*d
    if fam == 'II1':     # a,b,e ; e | a+b
        a, b, e = P; c = Fr(a+b, e); d = (n+e)/(4*a*b)
        return a*b*d, a*c*d*n, b*c*d*n
    if fam == 'II2':     # a,d,f ; 4ad | f+1
        a, d, f = P; c = Fr(f+1, 4*a*d); b = (n*c+a)/f
        return a*b*d, a*c*d*n, b*c*d*n
    if fam == 'II3':     # a,d,e
        a, d, e = P; c = (n+4*a*a*d+e)/(4*a*d*e); b = c*e-a
        return a*b*d, a*c*d*n, b*c*d*n
    raise ValueError(fam)

def family_ok(fam, P):
    if fam == 'I1': a, d, f = P; return (4*a*a*d+1) % f == 0
    if fam in ('I2',): a, c, f = P; return gcd(4*a*c, f) == 1
    if fam == 'I3': c, d, f = P; return gcd(4*c*d, f) == 1
    if fam in ('I4', 'II1'): a, b, e = P; return (a+b) % e == 0 and gcd(e, 4*a*b) == 1
    if fam == 'II2': a, d, f = P; return (f+1) % (4*a*d) == 0
    if fam == 'II3': a, d, e = P; return gcd(4*a*d, e) == 1

def identity_ok(fam, P):
    # each coordinate is a polynomial of degree <=4 in n (O85 correction: was "<=2"; true (x,y,z)-degrees
    # are at most (4,1,2), (3,1,2), (1,2,3)); 4xyz - n(xy+yz+zx) has degree <=7,
    # so vanishing at 12 points proves the identity.  Also check positivity for n>=2 (see notes).
    for n in range(2, 14):
        x, y, z = sol(fam, P, n)
        if 4*x*y*z != n*(x*y+y*z+z*x): return False
    return True

def covers(fam, P, t, L):
    # x,y,z polynomials of degree <=4 in s (n=t+Ls): integer-valued on Z iff integer at s=0,...,4
    # (O85 correction: was s=0,1,2, insufficient for I2/I3/II3 coordinates of degree 3-4)
    for s in range(5):
        for v in sol(fam, P, t+L*s):
            if v.denominator != 1 or v <= 0: return False
    return True

def leg(a, p): return pow(a % p, (p-1)//2, p) if a % p else 0

def target(t, variant):
    sq = lambda m: t % m in {k*k % m for k in range(1, m) if gcd(k, m) == 1}
    if not (t % 24 == 1 and sq(5) and sq(7)): return False      # Mordell-hard
    if leg(t, 13) != 12: return False
    if variant == 'np' and leg(t, 11) != 1: return False
    return True

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); L = d['L']; var = d['variant']; cls = [(c[0], tuple(c[1])) for c in d['classes']]
    exc = set(d['exceptions'])
    for c in cls:
        assert family_ok(*c), ('family condition', c)
        assert identity_ok(*c), ('identity', c)
    units = [t for t in range(1, L) if gcd(t, L) == 1]
    T = [t for t in units if target(t, var)]
    unc = [t for t in T if not any(covers(f, P, t, L) for f, P in cls)]
    print(f'{sys.argv[1]}: L={L} var={var} classes={len(cls)} targets={len(T)} uncovered={unc}')
    print('uncovered == exceptions:', set(unc) == exc)
    # also: each class used?
    used = {c: sum(covers(*c, t, L) for t in T) for c in cls}
    print('classes covering 0 targets:', [c for c, k in used.items() if k == 0])
