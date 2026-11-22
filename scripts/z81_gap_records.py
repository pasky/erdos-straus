"""First all-quadratic break vs first subgroup vs first box on the z80 records.
Two elementary, independent quadratic-span checks: Jacobi at every odd conductor
and projection onto G/G² by adjoining every square to the subgroup in G.
No search for prime records performed here. Root cwd, python -B.
"""
import csv
from math import gcd
from pathlib import Path
from z81_gap_audit import ds,factor,symbol

def grp(k,gens):
    h={1}
    for t in gens:
        cos=h;W=set();v=1
        while v not in W:
            W.update(a*v%k for a in cos);v=v*t%k
        h=W
    return h
print('p q g Kgen Ksub missed windows: genus / no-genus-but-subgroup-miss / budget-only; first q-seeded k, hit flag')
for row in csv.DictReader(Path('data/z80/gap/checks.csv').open()):
    if row['tag']!='record':continue
    p,g=int(row['p']),int(row['g']);q=next(l for l in range(2,p) if pow(l,(p-1)//2,p)==p-1)
    # Verify all windows through the given record and the first q-seeded window.
    seed=(-p)%(4*q);assert seed%4==3;ks=range(3,max(g,seed)+1,4); first=[None]*3;counts=[0]*3;seedhit=None
    for k in ks:
        x=(p+k)//4;F=factor(x);gens=[l for l,e in F]+[p];H=grp(k,gens);squares={a*a%k for a in range(1,k) if gcd(a,k)==1}
        c=any((-a)%k in H for a in squares);h=k-1 in H
        fs=ds([(l,1) for l,e in factor(k)])
        assert c==all(any(symbol(l,f)<0 for l,e in F) for f in fs if f%4==3)
        R={a*b%k for a in ds(F) for b in (1,p)};hit=any(k-a in R for a in R)
        for i,ok in enumerate((c,h,hit)):
            if ok and first[i] is None:first[i]=k
        if k<g:counts[int(c)+int(h)]+=1
        if k==seed:seedhit=int(hit)
    assert first[-1]==g;print(p,q,g,*first[:2],*counts,seed,seedhit)
# A real obstruction not seen by *any* odd quadratic character.
p,k=60601,51;x=(p+k)//4
assert factor(p)==[(p,1)] and factor(x)==[(59,1),(257,1)]
H=grp(k,[p,59,257]);assert k-1 not in H and symbol(257,3)==symbol(257,51)==-1
print('nonquadratic subgroup obstruction',p,k,x,sorted(H))
