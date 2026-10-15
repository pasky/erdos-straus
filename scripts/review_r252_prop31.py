"""R252: Prop 3.1 local check: for each odd prime l < 2000 find v mod l (v^2 = 32 mod 151 at l = 151)
with 256 v^6 + 105 a NONZERO square mod l (=> unit square in Z_l by Hensel). Also verify Lemma 1.0 o (u = v^2)."""
from sympy import primerange
from fractions import Fraction as F
bad = []
for l in primerange(3, 2000):
    ok = False
    for v in range(l):
        if l == 151 and (v*v - 32) % 151:
            continue
        val = (256*pow(v, 6, l) + 105) % l
        if val and pow(val, (l-1)//2, l) == 1:
            ok = True; break
    if not ok: bad.append(l)
print("odd l < 2000 with no local point:", bad)
# family check at integer v with v^2 = 32 mod 151
cnt = 0
for v in range(1, 3000):
    u = v*v
    if u % 151 != 32: continue
    m = 16*v**3; n = m*m + 105; assert n == 256*u**3 + 105
    A = F(64*u**3 + 2*u*u - 2*u + 66, 151); assert A.denominator == 1
    x, y, z = 64*(u**3+1), n*A, 32*n*(u+1)*A
    assert F(4, n) == F(1, x) + F(1, y) + F(1, z) and y % n == 0 and z % n == 0
    cnt += 1
print("family checked at", cnt, "values of v; 32 is QR mod 151:", pow(32, 75, 151) == 1)
