import itertools, math
from math import gcd, isqrt
def divisors(m):
    ds=[]
    for d in range(1,isqrt(m)+1):
        if m%d==0:
            ds.append(d)
            if d*d!=m: ds.append(m//d)
    return ds
def words(n):
    K=int(round((9*n/7)**(1/3)))+2
    W=set()
    for t in range(3,K+1):
        for d in divisors(t*n+1):
            if d%t==t-1:
                e=(t*n+1)//d
                u=(d+1)//t; v=(e+1)//t
                if u>=3 and v>=3 and t*u*v-u-v==n: W.add((t,u,v))
    for u in range(3,K+1):
        for A in divisors(n+u):
            if A%u==u-1:
                t=(A+1)//u; v=(n+u)//A
                if t>=3 and v>=3: W.add((t,u,v)); W.add((t,v,u))
    return W
for n in (2433600, 8813281, 36078, 6336, 42):
    print(n, len(words(n)))
# census zeros to 1e5 by enumerating triples
N=100000
import numpy as np
cnt=np.zeros(N+1,dtype=np.int32)
for t in range(3,N):
    if 9*t-6>N: break
    for u in range(3,N):
        A=t*u-1
        if 3*A-u>N: break
        # v>=3: n=A v - u
        n0=3*A-u
        cnt[n0:N+1:A]+=1
z=[n for n in range(3,N+1) if cnt[n]==0]
print("zeros<=1e5:",len(z),"last",z[-1])
# separated equal-sum check
def sqf(n): return all(n%(p*p) for p in range(2,isqrt(n)+1))
P=[(u,v) for u in range(5,11) for v in range(1000,4000) if sqf(u) and sqf(v) and gcd(u,v)==1]
bs={}
for p in P: bs.setdefault(sum(p),[]).append(p)
mx=0;c=0
for s,L in bs.items():
    for a,b in itertools.combinations(L,2):
        D=gcd(a[0]*a[1],b[0]*b[1])
        if D>1: c+=1; mx=max(mx,D/max(a[1],b[1]))
print("separated equal-sum dependent pairs",c,"max D/max v",mx)
