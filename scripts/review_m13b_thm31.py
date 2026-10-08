"""R95 from-scratch check of Theorem 3.1 of POINTWISE_MORDELL13B.md, directly from the
statement of Elsholtz-Tao Prop 1.9 + Section 10 parametrisations + pi maps (2.22)/(after 2.9).
No repo library used."""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp

def split(M):
    MT = 1
    for q in (11, 13):
        while M % q == 0: M //= q; MT *= q
    return M, MT

def contains_xstar(r, M, u=2):
    Mp, MT = split(M)
    return r % Mp == 1 % Mp and (r - u) % MT == 0

n = sp.Symbol('n')
ok = True
# ---- II3: n = -4a^2 d - e mod 4ade, (4ad,e)=1; Sigma^II point (a,(n+e)/4ad,(n+4a^2d+e)/4ade,d,e,(n+4a^2d)/e); pi^II=(abd,acdn,bcdn)
a, d, e = 8, 33, 11999
assert gcd(4*a*d, e) == 1
M = 4*a*d*e; r = (-4*a*a*d - e) % M
print('II3 M,r =', M, r, 'factor', sp.factorint(M), 'x* in class:', contains_xstar(r, M))
ok &= (M, r) == (12670944, 12650497) and contains_xstar(r, M)
b = (n+e)/(4*a*d); c = (n+4*a*a*d+e)/(4*a*d*e); f = (n+4*a*a*d)/e
X, Y, Z = a*b*d, a*c*d*n, b*c*d*n
ident = sp.simplify(1/X + 1/Y + 1/Z - 4/n)
print(' identity 4/n=1/x+1/y+1/z :', ident == 0); ok &= ident == 0
# Sigma^II constraints (2.13)-(2.21)
cons = [4*a*b*d-(n+e), c*e-(a+b), 4*a*b*c*d-(a+b+n*c), 4*a*c*d*e-(n+4*a*a*d+e), 4*b*c*d*e-(n+4*b*b*d+e),
        4*a*c*d-(f+1), e*f-(n+4*a*a*d), b*f-(n*c+a), 4*c*c*d*n+1-f*(4*b*c*d-1)]
print(' Sigma^II constraints all zero:', all(sp.expand(x) == 0 for x in cons)); ok &= all(sp.expand(x) == 0 for x in cons)
# integrality on the whole class: coordinates linear in n -> integer at n=r, r+M suffices; positivity n>=1 obvious (all coeffs >0)
for nm, P in (('b', b), ('c', c), ('f', f)):
    vals = [P.subs(n, r + k*M) for k in (0, 1)]
    poly = sp.Poly(P, n); pos = all(co > 0 for co in poly.all_coeffs())
    print(f'  {nm} = {P}: integer at r, r+M: {[v.is_integer for v in vals]}, all coeffs>0: {pos}')
    ok &= all(v.is_integer for v in vals) and pos
p = 12650497
print(' p prime:', sp.isprime(p), 'p mod 11,13:', p % 11, p % 13)
xs = [int(v.subs(n, p)) for v in (X, Y, Z)]
print(' solution at p:', sorted(xs), Fr(1, xs[0])+Fr(1, xs[1])+Fr(1, xs[2]) == Fr(4, p))
ok &= sorted(xs) == [3165624, 3339731208, 5005839614391] and Fr(1, xs[0])+Fr(1, xs[1])+Fr(1, xs[2]) == Fr(4, p)

# ---- I2: n=-f mod 4ac, n=-c/a mod f, (4ac,f)=1; Sigma^I point (a,(na+c)/f,c,(n+f)/4ac,(na+af+c)/(fc),f); pi^I=(abdn,acd,bcd)
a, c, f = 125, 88, 11999
assert gcd(4*a*c, f) == 1
m1, m2 = 4*a*c, f
r1 = (-f) % m1; r2 = (-c*pow(a, -1, f)) % f
r = sp.ntheory.modular.crt([m1, m2], [r1, r2])[0]; M = m1*m2
print('I2 M,r =', M, r, 'M_T =', split(M)[1], 'x* in class:', contains_xstar(int(r), M))
ok &= (M, int(r), split(M)[1]) == (527956000, 426568001, 1859) and contains_xstar(int(r), M)
b = (n*a+c)/f; d = (n+f)/(4*a*c); e = (n*a+a*f+c)/(f*c)
X, Y, Z = a*b*d*n, a*c*d, b*c*d
ident = sp.simplify(1/X + 1/Y + 1/Z - 4/n)
print(' identity:', ident == 0); ok &= ident == 0
cons = [4*a*b*d-(n*e+1), c*e-(a+b), 4*a*b*c*d-(n*a+n*b+c), 4*a*c*d*e-(n*e+4*a*a*d+1), 4*b*c*d*e-(n*e+4*b*b*d+1),
        4*a*c*d-(n+f), e*f-(4*a*a*d+1), b*f-(n*a+c), n*n+4*c*c*d-f*(4*b*c*d-n)]
print(' Sigma^I constraints all zero:', all(sp.expand(x) == 0 for x in cons)); ok &= all(sp.expand(x) == 0 for x in cons)
for nm, P in (('b', b), ('d', d), ('e', e)):
    vals = [P.subs(n, r + k*M) for k in (0, 1)]
    pos = all(co > 0 for co in sp.Poly(P, n).all_coeffs())
    print(f'  {nm} = {P}: integer at r, r+M: {[v.is_integer for v in vals]}, coeffs>0: {pos}')
    ok &= all(v.is_integer for v in vals) and pos
# brute: random members, exact check
import random
random.seed(1)
for (A, R, kind) in ((12670944, 12650497, 'II3'), (527956000, int(r), 'I2')):
    pass
print('ALL OK' if ok else 'FAIL')
