# R98b: sweep Lemma 2.1 (i)-(iv) and F/4<acd<=3F/4 over all F in [lo,hi] (same from-scratch enumerator)
import sys
from collections import Counter
def points(F):
    a=1
    while 4*a-1/a <= 2*F:
        for c in range(1, int(2*F/(4*a-1/a))+2):
            for d in range(F//(4*a*c)+1, int((2*F + c/a)/(4*a*c))+2):
                f=4*a*c*d-F; num=F*a+c
                if f<=0 or num%f: continue
                b=num//f
                if b>=a and (a+b)%c==0: yield (a,b,c,d)
        a+=1
lo,hi=map(int,sys.argv[1:3]); tot=0; mx=0; bad=0; two=0
for F in range(lo,hi+1):
    P=list(points(F)); tot+=len(P)
    per=Counter((a,d) for a,b,c,d in P)
    if per: mx=max(mx,max(per.values())); two+=sum(1 for v in per.values() if v==2)
    for a,b,c,d in P:
        e=(a+b)//c; f=4*a*c*d-F
        bad += not((4*a*b*d==e*F+1) and (f*b==a*F+c) and (f*(4*b*c*d-F)==F*F+4*c*c*d) and (F<4*a*c*d<=3*F))
print("F in",lo,hi,"points",tot,"identity/range fails",bad,"max per (a,d)",mx,"#pairs with 2",two)
