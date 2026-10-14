"""O212 (BRAINSTORM/y4_oneodd_slices): Z_2-oddity of the path form Q_w on chi=-1 words of odd n <= 401, vs slice parity class.
Usage: PYTHONPATH=scripts uv run python scripts/y4_oddity.py"""
import sys
sys.path.insert(0,'scripts')
from y4_oddslice_cells import words, slice_sols
from fractions import Fraction as F
from math import gcd
from collections import defaultdict
from sympy import jacobi_symbol as J
def oddity(G):
    G=[[F(x) for x in r] for r in G]; diag=[]
    n=len(G)
    while n:
        k=next((i for i in range(n) if G[i][i].numerator%2),None)
        if k is None:
            # even unimodular block left (oddity contribution 0); record its det class mod 8
            d=G[0][0]*G[1][1]-G[0][1]**2 if n==2 else None
            diag.append(('E', (d.numerator*pow(d.denominator,-1,8))%8))
            break
        a=G[k][k]; diag.append(a)
        idx=[i for i in range(n) if i!=k]
        G=[[G[i][j]-G[i][k]*G[k][j]/a for j in idx] for i in idx]; n-=1
    s=0
    ev=[a for a in diag if isinstance(a,tuple)]
    od=[a for a in diag if not isinstance(a,tuple)]
    for a in od: s+= a.numerator*pow(a.denominator,-1,8)
    return s%8, (tuple(ev), tuple(sorted((a.numerator*pow(a.denominator,-1,8))%8 for a in od)))
tab=defaultdict(set); tab2=defaultdict(set)
for n in range(3,402,2):
    for (t,u,v) in words(n):
        A=t*u-1
        if A<1 or gcd(A,n)!=1: continue
        if J((-A)%n,n)!=-1: continue
        e=[e for _,e,_ in slice_sols(n,t,u,v)]
        c=('o' if 2 in e else '')+('e' if any(x>=3 for x in e) else '')
        G=[[v,-1,0],[-1,t,-1],[0,-1,u]]
        od,dg=oddity(G)
        tab[(n%8,od)].add(c); tab2[(n%8,dg)].add(c)
print(sorted(tab.items()))

print(sorted(tab2.items()))
