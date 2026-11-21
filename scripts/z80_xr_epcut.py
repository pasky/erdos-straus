"""Opus cross-review of R17_WALK (NOT a certificate): reviewer's own rational check of the z79 four-index
cover for ALTERNATIVE cutoffs (E,J0,V,Y), re-derived (see review §4):
  outside Hd<=Y:  rho=a/b <= 36(1+e0/N)/(4rY),  H <= h q U/(4r a d),  J <= j 4p a^2 d/U,  eZ <= z p^2 a
  => e*HZ*J*(Hd)^2 <= 4 (pq)^3 h^3 j z U^2/(4r)^3 ;  need this < U^2/500 and 500 E J0 V Y^2 >= U^2.
Also the grouped-window constants used by scripts/z80_xr_ep.c part B:  q e0/(4U) < 1, 5 e0 < U.
usage: python scripts/z80_xr_epcut.py r L E J0 V Y
"""
import sys
from fractions import Fraction as F
from math import isqrt
r,L,E,J0,V,Y=map(int,sys.argv[1:]);U=r**L;B=U//r;N=U*B;e0=466*(isqrt(U-1)+1)
assert 500*E*J0*V*Y*Y>=U*U,'product of cutoffs too small'
assert 5*e0<U and F(5*e0,4*U)<1
for p in (1,5):
    q=6-p
    rho=F(36,4*r*Y)*(1+F(e0,N))
    h=(1+F(p,q)*rho)*(1+F(e0,N)); j=1/(1-F(q*e0,U)); z=1+F(q,p)*(h*j-1)
    lhs=4*(p*q)**3*h**3*j*z/F((4*r)**3)
    assert lhs<F(1,500),(p,float(lhs))
    print('p',p,'constant',float(lhs*500),'(<1 required)')
print('alternative cutoffs OK',r,L,E,J0,V,Y,'ratio 500EJVY^2/U^2 =',float(F(500*E*J0*V*Y*Y,U*U)))
