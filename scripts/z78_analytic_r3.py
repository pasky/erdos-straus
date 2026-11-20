"""Exact affine LP for inverse phase spacing; every maximum is at a triangle vertex."""
from fractions import Fraction as F

print('R3 exact affine vertex checks: inverse spacing, quartic bands, numerator M')

def audit(t):
    for a,b,g in [(t,1-2*t,t),(t,t,1-2*t),((1-t)/2,(1-t)/2,t)]:
        r=b-t;j=2*(r+g-t);d=1-b+2*r+j-2*g;K=max(0,d+4*j+8*r-3*g);goal=g-j
        terms=[g/2+d/4,(19*g+27*d+22*j)/60,3*g/4+d/4-j/2-r,(g+d)/2-r]
        assert g>j+2*r and g>2*j and 2*g<1 and min(d,j,r,2*r+g-b)>=0
        terms.append((27*g+55*d+58*j)/112)  # Titchmarsh's second term on the full band
        assert max(terms)+K<=goal and g+2*r<=2*t and b-2*r<=t and b-g<=t
        print('block',a,b,g,'residual',K,'slacks',*[goal-x-K for x in terms])
    print('exponent',t,'improvement on R2',F(20,63)-t)

audit(F(1472,4637))

# Global inverse spacing with J frozen quartic subbands pays J^(1/4).
# Local fourth derivative on subbands removes this penalty from the leading term.
for t,local in [(F(286,901),False),(F(272,857),True)]:
    for a,b,g in [(t,1-2*t,t),(t,t,1-2*t),((1-t)/2,(1-t)/2,t)]:
        r=b-t; j=2*(r+g-t); d=1-b+2*r+j-2*g
        K=max(F(0),d+4*j+8*r-3*g); goal=g-j
        terms=[g/2+d/4,(19*g+27*d+22*j)/60,3*g/4+d/4-j/2-r,(g+d)/2-r]
        extra=(27*g+55*d+58*j)/112
        terms=(terms+[extra+K/16] if local else [x+K/4 for x in terms+[extra]])
        assert g+2*r<=2*t
        assert max(terms)<=goal and d+6*j+12*r-5*g<0
        assert g>j+2*r and g>2*j and 2*g<1 and min(d,j,r,2*r+g-b)>=0
        assert 2*j+8*r-2*g+max(F(0),4*(d+2*j-g)/15)<0 and b-2*r<=t and b-g<=t
        print('t',t,'vertex',a,b,g,'J exponent',K,'slacks',*[goal-x for x in terms])
    print('improvement on R2',F(20,63)-t)

# Variable numerator: base X=n/M; length L=MNW/V. Test even the larger
# triangle without beta>=alpha. Convexity reduces checks to 2*3 vertices.
th=F(272,857)
for mu in (F(0),F(1,3)):
    t=th+(1-3*th)*mu
    for a,b,g in [(t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t)]:
        r=b-t;j=2*(r+g-t);d=1+mu-b+2*r+j-2*g
        K=max(F(0),d+4*j+8*r-3*g); goal=g-j
        terms=[g/2+d/4,(19*g+27*d+22*j)/60,3*g/4+d/4-j/2-r,(g+d)/2-r,(27*g+55*d+58*j)/112+K/16]
        assert max(terms)<=goal and d+6*j+12*r-5*g<0 and 2*j+8*r-2*g+max(F(0),4*(d+2*j-g)/15)<0
        assert g>j+2*r and g>2*j and 2*g<1 and min(d,j,r,2*r+g-b)>=0 and b-2*r<=t and b-g<=t
        assert g+2*r<=2*t
        print('R_M endpoint',mu,'vertex',a,b,g,'min slack',goal-max(terms))
