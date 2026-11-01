# z52d triage T0, Z1927: joint failure of shift slices B=1..6 vs product of marginals, overall and within residue/Legendre cells.
import math, collections
from sympy import factorint, primerange, legendre_symbol
def succ(p,B):
    f=factorint(p+B); ds=[1]
    for q,e in f.items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return any(d>1 and d%(4*B)==4*B-1 for d in ds)
P=[p for p in primerange(5,10**6) if p%4==1]
rows=[(p,tuple(succ(p,B) for B in range(1,7))) for p in P]
def ratio(rs):
    n=len(rs); jf=sum(1 for _,r in rs if not any(r))/n
    pf=1.0
    for i in range(6): pf*=sum(1 for _,r in rs if not r[i])/n
    return jf,pf
jf,pf=ratio(rows); print('overall joint %.5f prod %.5f ratio %.2f'%(jf,pf,jf/pf))
for name,key in [('p mod 840',lambda p:p%840),('mod 840 + (p/q) q=11,13,17,19',lambda p:(p%840,)+tuple(legendre_symbol(p,q) for q in (11,13,17,19)))]:
    cells=collections.defaultdict(list)
    for p,r in rows: cells[key(p)].append((p,r))
    J=0;Pr=0
    for c,rs in cells.items():
        j,pp=ratio(rs); J+=j*len(rs); Pr+=pp*len(rs)
    print(name,'cells',len(cells),'sum joint %.1f sum within-cell product %.1f ratio %.2f'%(J,Pr,J/Pr))
