# R98b from-scratch brute force: N-points of Sigma^I_F: 4abcd = F(a+b)+c, c | a+b, a<=b (all positive ints).
# Solve b = (F a + c)/(4acd - F) directly from the defining equation; bound d via b>=a (derived independently).
import sys, math
from collections import Counter
def points(F):
    pts=[]
    a=1
    while 4*a-1/a <= 2*F:
        cmax = int(2*F/(4*a-1/a))+1
        for c in range(1, cmax+1):
            dlo = F//(4*a*c)+1
            dhi = int((2*F + c/a)/(4*a*c))+1
            for d in range(dlo, dhi+1):
                f = 4*a*c*d - F
                if f<=0: continue
                num = F*a+c
                if num % f: continue
                b = num//f
                if b < a or (a+b) % c: continue
                assert 4*a*b*c*d == F*(a+b)+c
                pts.append((a,b,c,d))
        a+=1
    return pts
F=int(sys.argv[1]); P=points(F)
per=Counter((a,d) for a,b,c,d in P)
bad=0
for a,b,c,d in P:
    e=(a+b)//c; f=4*a*c*d-F
    ok = (4*a*b*d==e*F+1) and (f*b==a*F+c) and (f*(4*b*c*d-F)==F*F+4*c*c*d) and (e*f==4*a*a*d+1) and (F<4*a*c*d<=3*F)
    bad += not ok
n17e=sum(1 for a,b,c,d in P if ((a+b)//c)%17)
# Cor 2.2 check for several c0
cor=[]
for c0 in [1,2,int(F**0.25)+1,int(math.isqrt(F))+1, F//10+1]:
    Y=3*F/(4*c0); cnt=sum(1 for p in P if p[2]>=c0)
    bound = 2*Y*(1+math.log(Y)) if Y>=1 else 0
    pairs = sum(1 for (a,d) in set((p[0],p[3]) for p in P if p[2]>=c0) if a*d<=Y)
    npairs = len(set((p[0],p[3]) for p in P if p[2]>=c0))
    cor.append((c0,cnt,round(bound,1),npairs==pairs))
print(F,"points",len(P),"17∤e",n17e,"identity-fails",bad,"max per (a,d)",max(per.values()) if per else 0,"Cor2.2 (c0,count,bound,ad<=Y ok)",cor)
