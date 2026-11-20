"""Check every saved witness literally and independently build the candidate set by CRT."""
from itertools import product
from math import prod,gcd
from pathlib import Path
mods=(60,7,13,17,29); M=prod(mods)
roots=([0],[0,1,6],*([x for x in range(l) if (x*x+1)%l==0] for l in mods[2:]))
expected=set()
for xs in product(*roots):
    t=sum(x*(M//l)*pow(M//l,-1,l) for x,l in zip(xs,mods))%M
    expected.update(m for m in range(t,10**9+1,M) if m*m+1>10**11)
seen=set();late=[]
for row in Path('data/z76/disproof/composite.txt').read_text().splitlines():
    m,n,R,G=map(int,row.split()); assert m in expected and m not in seen; seen.add(m)
    assert n==m*m+1 and n%840 in (1,121) and gcd(n,105)==1 and n%(13*17*29)==0
    assert R and G, ('unresolved row',n)
    for f in [R,G]:
        u=(-n)%f; v=(n+u)//f; t=(f+1)//u
        assert min(t,u,v)>0 and t*u*v-u-v==n
        if f==R: assert t%4==0 and 4*(t//4)*u*v-u-v==n
        if f==G: assert f%8==7 and (f+1)%u==0
    late.append((R,G,n))
assert seen==expected
print('CRT total',len(seen),'max R (f,n)',max((r,n) for r,g,n in late),'max U7 (f,n)',max((g,n) for r,g,n in late))
