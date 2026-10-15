"""R251: Prop 3.1 local check. For every odd prime l < LMAX find v mod l (v^2 = 32 mod 151 at l = 151) with
256 v^6 + 105 a NON-ZERO square mod l; also verify O238 Lemma 1.0 as a Type II (a..f) polynomial family in u."""
import sys, sympy as sp
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
bad = []
for l in sp.primerange(3, LMAX):
    ok = False
    for v in range(l):
        if l == 151 and (v*v - 32) % l: continue
        r = (256*pow(v, 6, l) + 105) % l
        if r and pow(r, (l-1)//2, l) == 1: ok = True; break
    if not ok: bad.append(l)
print('primes without local point:', bad)
u = sp.symbols('u'); n = 256*u**3 + 105
a, d, b, c = 1, 2*(u**2-u+1), 32*(u+1), (32*u+33)/sp.Integer(151)
e = sp.expand(4*a*b*d - n); f = sp.expand(4*a*c*d - 1)
print('e =', e, '; ef - (n+4a^2d) =', sp.expand(e*f - n - 4*a**2*d), '; b - (ce - a) =', sp.expand(b - c*e + a))
print('x,y,z = abd, acdn, bcdn vs Lemma 1.0:', sp.simplify(a*b*d - 64*(u**3+1)), sp.simplify(4/n - 1/(a*b*d) - 1/(a*c*d*n) - 1/(b*c*d*n)))
