"""Exact rational margin for §11. Log lower by alternating series at 0<h<1;
upper squared coefficient rational after factoring U^3 out of the integral.
"""
from fractions import Fraction as F
for t,b,z,lo,hi in [(F(99078,100000),F(99078,100000),F(48615,100000),F(7531,100000),F(7523,100000)),
                    (F(99885,100000),F(4999,10000),F(498259,1000000),F(9349,1000000),F(9305,1000000))]:
    h=t/z-2;assert 0<h<1
    lower=(2/t)*sum((-1)**(j+1)*h**j/j for j in range(1,5));U2=1/z-2
    # integrand <= 4s² - (14/3)s⁴/(1+U²)²
    v=F(4,3)-F(14,15)*U2/(1+U2)**2
    upper2=F(9,4)*(2/b)**3*U2**3*v**2
    assert v>0 and lower>lo and upper2<hi**2
    print('direct level',t,'switched',b,'zeta',z,'normalized lower >',lo,'upper <',hi,'margin >',lo-hi,'(exact rational)')
