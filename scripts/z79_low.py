"""Exact joint P9/Q5 marginals (and conditioned union) in the small-prime tree."""
from pathlib import Path
from math import isqrt
import sys,subprocess
base=Path('data/z79'); D=Path(sys.argv[1]); old=Path('data/z78/exact')
def run(name,*args):
    return subprocess.check_output([D/name,*map(str,args)],timeout=1700,text=True).splitlines()
for r in map(int,sys.argv[2:]):
    def fam(f):return set(map(int,(old/f'r{r}_{f}.txt').read_text().split()))
    pre=[fam('p1')|fam('q1'),fam('p3'),fam('q3')|fam('p5')]; ns=lambda x: pow(x%r,(r-1)//2,r)==r-1
    def good(x):return ns(x) and all(x%r**i not in s for i,s in enumerate(pre,1))
    def P(k):
        E=isqrt(r**k)//3;T=(r**k//E+1)//2;W=r**((k+1)//2)
        lines=run('se' if k==7 else 'p9',r,E)+run('cf',r,k,E,1,T);s=set()
        for l in lines:
            x,y=map(int,l.split());assert x*y%W==1
            if good(x):assert good(y);s.update((x,y))
        if r==17:
            ref={v for l in Path(f'data/m17b/p{k}.txt').read_text().splitlines() for a,b,c,d in [map(int,l.split())] for u in [a,b] for v in [(1-4*u*c*d)%W] if good(v)};assert s==ref
        return s
    pre.append(P(7));p=P(9);q={int(l.split()[1]) for l in run('enum',r,'Q',5) if good(int(l.split()[1]))}
    assert all(pow(x,-1,r**5) in q for x in q)
    live=((r-1)//2)*r**4-sum(len({x for x in s if ns(x) and all(x%r**j not in z for j,z in enumerate(pre[:i],1))})*r**(4-i) for i,s in enumerate(pre))-len(p|q)
    print(r,len(pre[-1]),len(p),len(q),len(p&q),live,flush=True)
    if r==17:
        for j in range(1,5):
            U=r**j;u=5;assert good(5);print('cell',u,j,len([x for x in p if x%U==u]),len([x for x in q if x%U==u]),len([x for x in p&q if x%U==u]),flush=True)
