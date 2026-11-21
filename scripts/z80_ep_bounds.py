"""Verify the z79 four-index covering condition at the extended levels."""
from fractions import Fraction as F
from math import isqrt
import sys
L,E,J,V,Y=map(int,sys.argv[1:]);U=17**L;B=U//17;N=U*B;e=466*(isqrt(U-1)+1)
assert 500*E*J*V*Y**2>=U**2 and 5*e<U
for p in (1,5):
 q=6-p;rr=F(36,68*Y)*(1+F(e,N));h=(1+F(p,q)*rr)*(1+F(e,N));j=1/(1-F(q*e,U));z=1+F(q,p)*(h*j-1);assert 4*125*h**3*j*z*500<68**3
 assert F(p*36,16*17)*(1+F(e,N))**2<=F(p,6) and F(q*e,4*U)<1
 assert p*(q*B+J)**2<2**128
print('four-index cutoffs and grouped-window constants verified',L)
