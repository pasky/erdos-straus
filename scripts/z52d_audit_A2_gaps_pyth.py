"""Check the exact lemma for Type I near-isosceles solutions: if 4/p = 1/x+1/(x+g)+1/z with p∤x(x+g), then z = p w,
4w-1 = p m, and (2mg)^2 + (pm+1)^2 is a perfect square s^2 with x = (pm+1 - 2mg + s)/(4m)."""
import sys
from fractions import Fraction as F
from math import isqrt
ok=bad=skip=0
for line in open(sys.argv[1]):
    p,U,g,x,_,_ = map(int,line.split())
    if p%4!=1 or p<100: continue
    y=x+g; r=F(4,p)-F(1,x)-F(1,y)
    assert r.numerator==1; z=r.denominator
    if x%p==0 or y%p==0: skip+=1; continue
    w,rem=divmod(z,p); assert rem==0
    m,rem=divmod(4*w-1,p); assert rem==0
    K=p*m+1; s2=(2*m*g)**2+K*K; s=isqrt(s2)
    if s*s==s2 and (K-2*m*g+s)==4*m*x: ok+=1
    else: bad+=1
print("Type I min-gap solutions checked:",ok,"failures:",bad,"min-gap attained with p|x or p|y:",skip)
