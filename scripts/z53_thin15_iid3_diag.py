# z53_thin15_iid3_diag.py — stage counts (x(1), y(1)) for the II-d D=3 search, denominators <= 16, |values| <= 12
from fractions import Fraction as Fr
from math import gcd
rho=-(1/15)**(1/3)
def n(Y): return 15*Y**3+1
def odd(m):
    while m%2==0: m//=2
    return m
half=lambda q: odd(q.denominator)==1
vals=sorted({Fr(p,q) for q in range(1,17) for p in range(-12*q,0) if gcd(p,q)==1 and p/q<rho})
c1=c2=c3=0; ex=[]
for i,al in enumerate(vals):
    for ze in vals[:i]:
        kap=-n(al)/(al-ze); f1=kap*(1-ze); x1=(16+f1)/4
        if not half(x1): continue
        c1+=1
        d4=-n(ze)/(ze-al)**2; C1=d4*(1-al)**2; g1=(16+C1)/f1; y1=4*(1+g1)
        if not half(y1): continue
        c2+=1
        if len(ex)<5: ex.append((al,ze,x1,y1,16*x1*(1+g1)/C1))
print(len(vals),c1,c2,ex)
