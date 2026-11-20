"""Exact linear program by vertices, positive-conductor B/large-sieve bound."""
from fractions import Fraction as F

t=F(7,22)
assert t<F(7955,24966)
for a,b,g in [(t,1-2*t,t),(t,t,1-2*t),((1-t)/2,(1-t)/2,t)]:
    r=b-t; j=2*(r+g-t); d=1-b+2*r+j-2*g
    goal=g-j
    terms=(g/2+r,j+r+d/2,g-j-r,(g+d)/2-r)
    quartic=d+4*j+8*r-3*g
    print('vertex',a,b,g,'r,j,d',r,j,d,'terms',*terms,'goal',goal,'quartic exp',quartic)
    assert r>=0 and j>=0 and g>j+2*r and d>0 and 2*r+g-b>=0
    assert quartic<0 and max(terms)<=goal and 2*g<1
    assert b-2*r<=t and b-g<=t
print('at binding vertex h*sqrt(NY) <= W/H iff 7*(1-3t)<=t; old minus new:',F(7955,24966)-t)
