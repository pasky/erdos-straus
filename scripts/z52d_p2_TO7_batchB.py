# Lint-fix computations for TO7: Z2563, Z2569, Z2596, Z2602, Z2611, Z2625, Z2437, Z2755, Z2842, Z2647, Z2870, Z2878, Z2855
import sys, math, itertools, functools
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; minI=tsv['minI']; minII=tsv['minII']; nI=tsv['nI']
which=sys.argv[1] if len(sys.argv)>1 else 'all'
# per-prime success matrix for type I, k=3..399 (k≡3 mod 4)
ks=list(range(3,401,4))
idx_p={int(p):i for i,p in enumerate(P)}
m0=a['type']==0
SUC=np.zeros((len(P),len(ks)),bool)
kpos={k:j for j,k in enumerate(ks)}
ps=a['p'][m0]; kk=a['k'][m0]; dh=B['dh'][m0]
pi=np.searchsorted(P,ps)
SUC[pi,(kk-3)//4]=dh
# ---- Z2563: longest runs of failing type-I slices (k<=399) at hard primes; obstructing primes via P(success | l | M_k)
run=[]
for i in np.nonzero(hard)[0]:
    s=SUC[i]; best=cur=0
    for x in s:
        cur = 0 if x else cur+1; best=max(best,cur)
    run.append(best)
print("Z2563 hard primes: longest failing run of Type-I slices k<=399: median",np.median(run),"max",max(run),"mean",round(np.mean(run),2))
# P(success | l | M_k) for small primes l (type I, hard primes)
mm=m0&np.isin(a['p'],P[hard])
Mdiv=defaultdict(lambda:[0,0])
spf=np.zeros(250001,dtype=np.int64)
for i in range(2,501):
    if spf[i]==0:
        idx=np.arange(i*i,250001,i); mm2=spf[idx]==0; spf[idx[mm2]]=i
def primefac(n):
    s=set()
    while n>1:
        q=int(spf[n]) if spf[n] else n
        s.add(q)
        while n%q==0: n//=q
    return s
# M_k for type I = (k p+1)/4 up to 1e8/4 — too large for spf table; restrict to k=3,7 (M<=~2e6 on hard primes) using trial division
def pf_trial(n):
    s=set(); d=2
    while d*d<=n:
        while n%d==0: s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return s
rows=[]
for p in P[hard][:600]:
    for k in (3,7,11):
        M=(int(k)*int(p)+1)//4
        if M<2: continue
        ok=bool(SUC[idx_p[int(p)], (k-3)//4])
        for l in pf_trial(M):
            if l<=40: Mdiv[l][0]+=1; Mdiv[l][1]+=ok
res=sorted([(l,v[1]/v[0],v[0]) for l,v in Mdiv.items() if v[0]>=200], key=lambda x:x[1])
print("Z2563 P(success | l|M_k), hard primes, k in {3,7,11}, l<=40 (lowest 5 / highest 3):", [(l,round(f,3),n) for l,f,n in res[:5]], [(l,round(f,3),n) for l,f,n in res[-3:]])
