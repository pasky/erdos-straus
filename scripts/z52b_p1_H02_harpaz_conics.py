# residual conics of U_n: 4xyz = n(xy+yz+zx) (affine w=1) in the pencil of planes through the line {y=-x, z=n/4}
from sympy import *
x,y,z,n,l,s=symbols('x y z n lambda s')
F=4*x*y*z-n*(x*y+y*z+z*x)
# parametrize plane x+y = l*(z-n/4): y = l*(z-n/4) - x
G=expand(F.subs(y, l*(z-n/4)-x))
G=factor(G); print("restricted:",G)
# residual conic (divide by the linear factor of the line, if any)
q=cancel(G/(4*z-n)) if simplify(rem(Poly(G,z,x).as_expr(),4*z-n,z))==0 else None
print("residual:",factor(q) if q is not None else "no factor")
if q is not None:
    Q=Poly(q,x,z); 
    # quadratic part discriminant (split iff -det is a square)
    a=Q.coeff_monomial(x**2); b=Q.coeff_monomial(x*z); c=Q.coeff_monomial(z**2)
    print("quadratic part coeffs",a,b,c," disc b^2-4ac =",factor(b**2-4*a*c))
