"""Positive-shift walk, negative composite successors allowed, literal path certificates."""
from math import isqrt
from collections import deque,Counter
from pathlib import Path
from z80_square_span import jac, primes_to
import sys

HARD=[2521,3361,21841,76441,113035442521]
PANEL=[int(x) for x in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if x and x[0].isdigit()]

def ds(n,ps):
    out=[1]
    for l in ps:
        if l*l>n:break
        if n%l==0:
            a=1; old=out.copy()
            while n%l==0:
                n//=l;a*=l;out.extend(x*a for x in old)
    if n>1:out.extend([x*n for x in out]);
    return sorted(out)

def walk(p,ps,cap):
    q=next(x for x in ps if jac(x,p)==-1); parent={q:0}; todo=deque([q]); used=0
    while todo and used<cap:
        x=todo.popleft();used+=1
        divs=ds(p+x,ps)
        for v in divs:
            if v<=1 or v>=p:continue
            d=(p+x)//v
            if (d+1)%x==0 and d+1>=2*x and jac(v,p)==1:
                t=(d+1)//x
                path=[x]
                while (z:=parent[path[-1]]):path.append(z)
                path.reverse();assert all((p+a)%b==0 for a,b in zip(path,path[1:]))
                assert t*x*v-x-v==p and jac(d,p)==-1
                return used,path,t,v
        for z in divs:
            if 1<z<p and z not in parent and jac(z,p)==-1:
                parent[z]=x;todo.append(z)
    return used,[],0,0

def main():
    inputs=sorted(set(HARD+PANEL+[x for x in primes_to(10**7) if x%840==1]));ps=primes_to(isqrt(2*max(inputs))+1)
    depth=Counter(); worst=(0,0); miss=[]
    for p in inputs:
        assert p%8==1
        used,path,t,v=walk(p,ps,50000)
        if p in HARD+PANEL:print(p,used,path,t,v,flush=True)
        if not path:miss.append(p)
        if p%840==1 and p<=10**7:
            depth[len(path)-1]+=1;worst=max(worst,(used,p))
    print('main_depth_counts',sorted(depth.items()),'worst_pops',worst,'all_misses',miss)
if __name__=='__main__':main()
