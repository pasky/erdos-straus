"""Exact affine checks for the common-quartic-band h-average and R_M transfer."""
from fractions import Fraction as F
th=F(46,145)
for mu in (F(0),F(1,3)):
    t=th+(1-3*th)*mu
    for a,b,g in dict.fromkeys([(t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t)]):
        r=b-t;j=2*(r+g-t);d=1+mu-b+2*r+j-2*g;K=max(F(0),d+4*j+8*r-3*g);goal=g-j
        terms=[g/2+d/4,3*g/4+d/4-j/2-r,(g+d)/2-r,g/4+15*d/28+11*j/28,g/4+11*d/24+j/2+K/8]
        assert max(terms)<=goal and g+2*r<=2*t  # second inequality pays the constant in E_h after NW
        assert min(d,j,r,2*r+g-b)>=0 and b-2*r<=t and b-g<=t and g>j+2*r and 1>2*g
        assert d+6*j+12*r-5*g<0 and j+4*r<g and 6*d/7+24*j/7+8*r-3*g<0 and d+3*j+8*r-3*g<0
        print('mu',mu,'vertex',a,b,g,'slacks',*[goal-v for v in terms], 'sextic exponent',d+6*j+12*r-5*g)
print('46/145 improves R3 by',F(272,857)-th)
