# z53_thin15_iid3_selftest.py — symbolic check of the II-d D=3 parametrisation used by z53_thin15_iid3.py
import sympy as sp
from fractions import Fraction as Fr
Y=sp.symbols('Y'); n=15*Y**3+1
for al,ze in ((sp.Rational(-3,2),sp.Rational(-7,3)),(sp.Rational(-1,2),sp.Rational(-5,1))):
    nal=n.subs(Y,al); kap=-nal/(al-ze); f=kap*(Y-ze)
    d=-n.subs(Y,ze)/(4*(ze-al)**2); a=Y-al; C=4*a**2*d
    g,r=sp.div(sp.expand(n+C),f,Y); assert r==0
    b,r1=sp.div(sp.expand(f+n),4*a*d,Y); c,r2=sp.div(sp.expand(g+1),4*a*d,Y); assert r1==0 and r2==0
    x=a*b*d; y=a*c*d*n; z=b*c*d*n
    assert sp.expand(4*x*y*z-n*(x*y+y*z+z*x))==0
    assert all(sp.cancel(t)==0 for t in (x-(n+f)/4, y-n*(1+g)/4, z-n*x*(1+g)/C))
    print('ok', al, ze, sp.Poly(b,Y).degree(), sp.Poly(c,Y).degree())
