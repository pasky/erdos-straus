# z52d pass2 TO4 lint-fix D: Z1677 (chart distance to the node of the largest coordinate: middle/largest),
# Z1149 (Vieta root switch on z-y=h slices, all ES solutions p≡1 mod 4, p<3000)
import math, statistics
from fractions import Fraction
from sympy import primerange, divisors
exec(open('scripts/z52d_p2_TO4_fix_C.py').read().split('# ---- Z1057 restricted')[0])   # reuse red(), two_term_pairs(), rows
def es_solutions(p):
    sols=[]
    for x in range(p//4+1,(3*p)//4+1):
        a,b=red(4*x-p,p*x)
        if a<=0: continue
        for y,z in two_term_pairs(a,b):
            if x<=y<=z: sols.append((x,y,z))
    return sols
# Z1677: ES triples (sorted x≤y≤z). Chart at the node P_k whose coordinate is the largest (z): distance = y/z (middle/largest)
# and the other chart (x,y small, z largest) ; report min over solutions of middle/largest, and of 1/largest (node P0 chart).
res=[]
allmin=1.0
for p in [409,577,1009,1321,2521,3001,5569,9601]:
    S=es_solutions(p)
    if not S: continue
    d=[ (y/z) for (x,y,z) in S ]
    e=[ (1/z) for (x,y,z) in S ]
    near=[ (x,y,z) for (x,y,z) in S if y/z<0.01 ]
    res.append((p,len(S),round(min(d),5),round(statistics.median(d),3),len(near)))
print("Z1677 (p, #ES triples, min middle/largest, median middle/largest, #triples with middle/largest<0.01):")
for r in res: print("  ",r)
# ---- Z1149: root switch on slice z-y=h for every ES triple with p≡1 mod 4, p<3000 (all h)
tot=0; integ=0; examples=[]
for p in primerange(5,3000):
    if p%4!=1: continue
    for (x,y,z) in es_solutions(p):
        h=z-y; A=4*x-p; Bc=4*x*h-2*p*x-p*h
        yp=Fraction(-Bc,A)-y
        tot+=1
        if yp.denominator==1 and yp>0:
            integ+=1
            if len(examples)<4: examples.append((p,(x,y,z),int(yp)))
print("Z1149 Vieta root switch on slice z=y+h, all ES triples (p≡1 mod 4, p<3000): %d triples; images integral and positive: %d"%(tot,integ), examples)
