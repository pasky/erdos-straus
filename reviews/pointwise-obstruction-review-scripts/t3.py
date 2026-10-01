import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from gp import *
from sympy import isprime, divisors, primerange
from fractions import Fraction as Fr
pos=lambda v: all(x>0 for x in v)
# Mordell classes
cls=sorted({p%840 for p in primerange(5,200000) if p%24==1 and pow(p,2,5)==1 and pow(p,3,7)==1})
print('remaining classes',cls)
# forced exits table
bad=0
for p in primerange(5,300000):
    if p%4!=1: continue
    t=(p-1)//4
    def ok(h,D):
        m=p*h-t
        return (t*t)%h==0 and D>0 and (m*m)%D==0 and (D+h)%(4*h-1)==0
    if p%8==5: r=ok(1,2)
    elif p%24==17: r=ok(2,12)
    elif p%24==1:
        if p%5==3: r=ok(1,5)
        elif p%5==2: r=ok(2,5)
        elif p%7==3: r=ok(6,63)
        elif p%7==5: r=ok(3,63)
        elif p%7==6: m=4*p-t; r=(m%14==0) and ok(4,m//14)
        else: r=True
    else: r=True
    if not r: bad+=1; print('forced fail',p)
print('forced exits bad',bad)
# sieve classes distinct
H=divisors(36)
Ks=[4*h-1 for h in H]; Kd=[4*d-1 for d in H]
print('K_h',Ks,'K_d',Kd, 'any K_h*K_d==1?',any(a*b==1 for a in Ks for b in Kd))
# p=97,193 counts of unordered positive solutions
def npos(p):
    S=set()
    for x in range(p//4+1, 3*p//4+1):
        R=Fr(4,p)-Fr(1,x)
        if R<=0: continue
        for y in range(max(x,int(1/R)), int(2/R)+1):
            R2=R-Fr(1,y)
            if R2>0 and R2.numerator==1 and R2.denominator>=y: S.add((x,y,R2.denominator))
    return len(S)
print('npos 97',npos(97),'193',npos(193))
# windmill (4): ordered positive solutions of 1/x+1/y+2/z=4/p
def oddset(p):
    tot=0; zeven=0
    for z in range(1,10**9):
        R=Fr(4,p)-Fr(2,z)
        if z> 2*p*p: break
        if R<=0: continue
        # 1/x+1/y=R, ordered positive
        r,s=R.numerator,R.denominator
        for D in divisors(s*s):
            if (s+D)%r==0 and (s+s*s//D)%r==0:
                tot+=1; zeven+= (z%2==0)
    return tot,zeven
for p in (13,17,29,37,41):
    tot,ze=oddset(p); print('oddset',p,tot,ze,6*npos(p))
