# Verify the two "t varies with p" case-(i) identity families and that they are NOT subsumed by (A),(B),(C),(A'),(B') classes.
# F1: integers b,e,lam>=1: h=(p+lam)/(4be), a=(pb+e)/lam, t=(a+b)/e  (need all integers); then pt+1=4abh, t|a+b.
# F3: integers e,h,lam>=1: a=(p+lam)/(4eh), t=(4a^2h+1)/lam, b=te-a    (need integers, b>=1); then pt+1=4abh, t|a+b.
from fractions import Fraction as F
from sympy import isprime, primerange
def sol1(p,a,b,h,t):
    assert p*t+1==4*a*b*h and (a+b)%t==0 and t%4==3, (p,a,b,h,t)
    x=b*h*(a+b)//t; y=a*h*(a+b)//t; z=p*a*b*h
    assert F(1,x)+F(1,y)+F(1,z)==F(4,p)
    return (x,y,z)
cnt1=cnt3=0
for p in primerange(5,3000):
    if p%4!=1: continue
    for b in range(1,8):
        for e in range(1,8):
            for lam in range(1,60):
                if (p+lam)%(4*b*e): continue
                h=(p+lam)//(4*b*e)
                if (p*b+e)%lam: continue
                a=(p*b+e)//lam
                if (a+b)%e: continue
                t=(a+b)//e
                sol1(p,a,b,h,t); cnt1+=1
    for e in range(1,8):
        for h in range(1,8):
            for lam in range(1,60):
                if (p+lam)%(4*e*h): continue
                a=(p+lam)//(4*e*h)
                if (4*a*a*h+1)%lam: continue
                t=(4*a*a*h+1)//lam; b=t*e-a
                if b<1: continue
                sol1(p,a,b,h,t); cnt3+=1
print("F1 instances verified:",cnt1," F3 instances verified:",cnt3)
