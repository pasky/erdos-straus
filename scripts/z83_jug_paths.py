"""Forward-only check of the six reverse-census distance records.
Exact trial factorization of each encountered shift; FIFO with no early lookahead.
"""
from collections import deque
from math import isqrt
from pathlib import Path
from sympy import primerange

def walk(p,x):
    primes=list(primerange(2,isqrt(2*p)+1)); Q=deque([x]);parent={x:0}
    def neg(t):return pow(t,(p-1)//2,p)==p-1
    assert neg(x)
    popped=0
    while Q:
        z=Q.popleft();popped+=1;n=p+z;ds=[1]
        for l in primes:
            if l*l>n:break
            if n%l:continue
            old=ds[:];q=1
            while not n%l:
                n//=l;q*=l;ds.extend(q*d for d in old)
        if n>1:ds=ds+[n*d for d in ds]
        for v in ds:
            if 2<=v<p and ((p+z)//v+1)%z==0 and not neg(v):
                t=((p+z)//v+1)//z
                if t<2:continue
                path=[z]
                while parent[path[-1]]:path.append(parent[path[-1]])
                path.reverse();assert path[0]==x and all(neg(i) for i in path)
                assert all((p+i)%j==0 for i,j in zip(path,path[1:])) and t*z*v-z-v==p
                return popped,path,(t,v)
        for d in sorted(ds):
            if d<p and d not in parent and neg(d):parent[d]=z;Q.append(d)
        if len(parent)>250000:raise ValueError('memory budget')
    raise ValueError('no exit')
if __name__=='__main__':
    for r in [1,121,169,289,361,529]:
        line=Path(f'data/z83/es_jugular/basin-{r}.txt').read_text().splitlines()[-1]
        p,x,k=map(int,line.split()[-3:]);count,path,terminal=walk(p,x);assert len(path)==k+1
        print('p x depth',p,x,k,'popped',count,'path',path,'terminal',terminal)
