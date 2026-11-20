"""Per-term decomposition of the old z76 first cell; within-cell union comparison."""
import sys
from fractions import Fraction as F
sys.argv=['z76_sterile','558','558']
import z76_sterile as z
j=558; r=z.edge(j); parts=[('level 1',F(z.l1(j),r))]
for typ,T,cap in [('P',z.P,800),('Q',z.Q,100)]:
    for k in range(3,801,2):
        if k*j>=32*cap:break
        count=max((z.p(i) if typ=='P' else 2*z.tab(T,i)) for i in range(k*j,min(k*(j+1),32*cap)))
        parts.append((typ+str(k),F(count,r**((k+1)//2 if typ=='P' else k))))
parts.append(('tails',F(16,100*z.isqrt(r))+F(1,25000)))
assert sum(x for _,x in parts)==z.check(j)[0]
for name,x in parts: print(name,round(float(x)*1e6,3),'ppm')
a=[list(map(int,s.split())) for s in z.Path('data/z77/level1.txt').read_text().splitlines()]; a=[row for row in a if r<=row[0]<z.edge(j+1)]
print('prime,P,Q,cells (max multiplicity)',max(a,key=lambda row:row[1]+row[2])); print('prime,P,Q,cells (max union fraction)',max(a,key=lambda row:F(row[3],row[0])))
