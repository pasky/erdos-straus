import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from sympy import divisors
from fractions import Fraction as Fr
def npos(p):
    S=set()
    for x in range(p//4+1, 3*p//4+1):
        R=Fr(4,p)-Fr(1,x)
        if R<=0: continue
        for y in range(max(x,int(1/R)), int(2/R)+1):
            R2=R-Fr(1,y)
            if R2>0 and R2.numerator==1 and R2.denominator>=y: S.add((x,y,R2.denominator))
    return len(S)
def oddset(p):
    S=set()
    # case a: x<=3p/4 (or y by symmetry, add swapped)
    for x in range(1,3*p//4+1):
        R=Fr(4,p)-Fr(1,x)
        if R<=0: continue
        r,s=R.numerator,R.denominator
        # 1/y+2/z=r/s  <=> (r y - s)(r z - 2 s) = 2 s^2
        for D in divisors(2*s*s):
            if (s+D)%r==0 and (2*s+2*s*s//D)%r==0:
                y=(s+D)//r; z=(2*s+2*s*s//D)//r
                if y>0 and z>0:
                    S.add((x,y,z)); S.add((y,x,z))
    for z in range(1,3*p//2+1):
        R=Fr(4,p)-Fr(2,z)
        if R<=0: continue
        r,s=R.numerator,R.denominator
        for D in divisors(s*s):
            if (s+D)%r==0 and (s+s*s//D)%r==0:
                x=(s+D)//r; y=(s+s*s//D)//r
                if x>0 and y>0: S.add((x,y,z)); S.add((y,x,z))
    for (x,y,z) in S: assert Fr(1,x)+Fr(1,y)+Fr(2,z)==Fr(4,p)
    return len(S), sum(1 for v in S if v[2]%2==0)
for p in (13,17,29,37,41,97,193):
    tot,ze=oddset(p); print('oddset',p,'total',tot,'z-even',ze,'6f',6*npos(p))
