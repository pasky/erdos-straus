import sys; sys.path.insert(0,'scripts')
import z53_genusredei_twist as Z
from sympy import factorint
from collections import Counter
cnt=Counter(); cntP=Counter()
rows=[l.split()[0] for l in open('data/z53/genusredei/twist_X100_1e7_1.04e7.txt') if not l.startswith('#')]
X=100
for ps in rows:
    p=int(ps)
    for C in range(1,X+1):
        t=4*C; N=4*C*p+1; f=factorint(N)
        tw=[q for q,e in f.items() if q>X and e==1]; sm=[(q,e) for q,e in f.items() if not (q>X and e==1)]
        if (t-1) not in Z.sigma(list(f.items()),t): continue
        Ss=Z.sigma(sm,t); g=1
        for q in tw: g=g*q%t
        if (t-1) in Ss or (t-1) in {x*g%t for x in Ss}: continue
        r=Z.exact_twist(t,Ss,[q%t for q in tw],cap=10**6)
        (cnt if r is False else cntP)[C]+=1
print("Q-determined levels C:",sorted(cnt.items()))
print("protected levels C (count):",sorted(cntP.items())[:40])
