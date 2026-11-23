"""Independent Python interval and literal closure check at 178481. Also check
all eight higher-threshold 2p/5 orbits at the second example, not the full
2p/9 threshold (use the memory-bounded disjoint C recursion for that census).
"""
from collections import deque
from pathlib import Path
from sympy import divisors
from z83_jug_dyadic import prime

def sealed(p,m):
    start=2*p//m+1;ints=[(start,p-1)]
    while sum(b-a+1 for a,b in ints)>25000:
        out=[]
        for shift in [0,p]:
            for a,b in ints:
                u=max(start,(a+shift+1)//2);v=(b+shift)//2
                if u>v:continue
                if out and out[-1][1]+1>=u:out[-1]=(out[-1][0],v)
                else:out.append((u,v))
        if out==ints:break
        ints=out
        assert len(ints)<2000000
    ans=[]
    for a,b in ints:
        for x in range(a,b+1):
            # Require the orbit minimum to be x. It then stays in the high range.
            r=2*x%p;h=1
            while r>x:r=2*r%p;h+=1
            if r==x and pow(x,(p-1)//2,p)==p-1:ans.append((x,h))
    return ans

if __name__=='__main__':
    for p in [178481,164511353]:print('p',p,'above 2p/5',sealed(p,5))
    p=178481;aa=sealed(p,5);assert prime(p)
    neg=set(range(1,p))-{i*i%p for i in range(1,p//2+1)};q=min(neg);R={q};todo=deque(R)
    while todo:
        x=todo.popleft();new=(neg.intersection(divisors(p+x)))-R;todo.extend(new);R.update(new)
    assert neg-R=={i*pow(2,j,p)%p for i,h in aa for j in range(h)}
    for v in divisors(p+q):
        d=(p+q)//v
        if 1<v<p and (d+1)%q==0 and (d+1)//q>=2 and v not in neg:
            print('literal',p,'q',q,'reachable',len(R),'missing',len(neg-R),'exit (q,t,v)',(q,(d+1)//q,v));break
    else:raise ValueError('no root exit')
