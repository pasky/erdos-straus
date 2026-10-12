# O156 spot-check of cayley_markoff_cm P2 identity and P4 D-class claim.
import sympy as sp
y0,y1,y2,y3=sp.symbols('y0:4')
e1=y0+y1+y2+y3; e3=y0*y1*y2+y0*y1*y3+y0*y2*y3+y1*y2*y3
X=2*(y0+y1-y2-y3)/e1; Y=2*(y0-y1+y2-y3)/e1; Z=2*(y0-y1-y2+y3)/e1
print("P2:", sp.simplify(X**2+Y**2+Z**2-X*Y*Z-4+64*e3/e1**3))
# P4: X^2-4 = -16(y0+y1)(y2+y3)/e1^2
print("P4a:", sp.simplify(X**2-4+16*(y0+y1)*(y2+y3)/e1**2))
