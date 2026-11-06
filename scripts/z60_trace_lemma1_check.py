# Check Lemma 1 (line dictionary): split points of 4Cs-w=n  <->  ES pairs (u,B>=1) and TRIV pairs (u,B<=0).
import sys
from math import isqrt
def es_pairs(C,n):
    N=4*C*n+1; out=[]
    for d in range(1,N+1):
        if d*d>N*N: break
        if N%d==0:
            e=N//d
            if d%(4*C)==4*C-1 and e%(4*C)==4*C-1: out.append((d,e))
    return out
def triv_pairs(C,n):
    N=4*C*n+1; return [(d,N//d) for d in range(1,N+1) if N%d==0 and d%(4*C)==1%(4*C) and (N//d)%(4*C)==1%(4*C)]
def split_points(C,n):
    # roots u<=B or any order: enumerate integer pairs (u,B) with 4CuB-u-B=n via d=4Cu-1 | N (u any sign)
    N=4*C*n+1; res=[]
    for d in range(1,N+1):
        if N%d: continue
        for sg in (1,-1):
            dd=sg*d; ee=sg*(N//d)
            if (dd+1)%(4*C)==0 and (ee+1)%(4*C)==0:
                u=(dd+1)//(4*C); B=(ee+1)//(4*C)
                assert 4*C*u*B-u-B==n
                s,w=u*B,u+B; assert 4*C*s-w==n and w*w-4*s>=0
                res.append((u,B))
    return res
bad=0
for C in range(1,7):
    for n in range(1,1200,2):
        sp=split_points(C,n)
        pos=[(u,B) for u,B in sp if u>=1 and B>=1]; neg=[(u,B) for u,B in sp if u<=0 and B<=0]
        assert len(pos)+len(neg)==len(sp)
        if len(pos)!=len(es_pairs(C,n)) or len(neg)!=len(triv_pairs(C,n)): bad+=1
        r=isqrt(n)
        if r*r==n: assert not pos, (C,n)
print("mismatches",bad)
import sys
sys.exit(1 if bad else 0)
