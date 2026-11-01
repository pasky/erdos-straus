# z52d Pass 2 NC0, item Z0814 (second control): Proth primes vs controls matched on (p mod 105, v2(p-1)) — isolates the 2-adic depth of p-1.
import sys, random, subprocess, math, json, collections, statistics as st
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from sympy import isprime
PMAX=10**7; random.seed(11)
def v2(n):
    k=0
    while n%2==0: n//=2; k+=1
    return k
prot=set()
for k in range(1,16,2):
    n=2
    while k*2**n+1<=PMAX:
        p=k*2**n+1
        if isprime(p): prot.add((p,k,n))
        n+=1
prot=sorted(prot)
sv=np.ones(PMAX+1,dtype=bool); sv[:2]=False
for i in range(2,int(PMAX**0.5)+1):
    if sv[i]: sv[i*i::i]=False
pool=collections.defaultdict(list)
for q in np.nonzero(sv[PMAX//2:])[0]+PMAX//2:
    q=int(q)
    if q%4==1: pool[(q%105,v2(q-1))].append(q)
ctrl=[]
for p,k,n in prot:
    lst=pool.get((p%105,v2(p-1)),[])
    if lst: ctrl+=random.sample(lst,min(6,len(lst)))
def U(p):
    out=subprocess.run(['/tmp/z52b_count','4',str(p),str(p)],capture_output=True,text=True,timeout=900).stdout.split()
    return int(out[1])
with ThreadPoolExecutor(4) as ex:
    pu=list(ex.map(U,[p for p,_,_ in prot])); cu=list(ex.map(U,ctrl))
L=lambda p,u: u/math.log(p)**2
rows=[(p,k,n,L(p,u)) for (p,k,n),u in zip(prot,pu)]
cr=[(p,L(p,u)) for p,u in zip(ctrl,cu)]
cm=collections.defaultdict(list)
for p,r in cr: cm[(p%105,v2(p-1))].append(r)
ratio=[r/st.median(cm[(p%105,v2(p-1))]) for p,k,n,r in rows if cm.get((p%105,v2(p-1)))]
print('Proth n=',len(rows),' controls n=',len(cr))
print('median ratio Proth / control matched on (p mod 105, v2(p-1)):',round(st.median(ratio),3),'n=',len(ratio))
print('Proth median U/log^2 by v2(p-1)=n: ', {n:(round(st.median([r for p,k,nn,r in rows if nn==n]),3), sum(1 for p,k,nn,r in rows if nn==n)) for n in sorted({n for _,_,n,_ in rows})})
print('control median U/log^2 by v2:', {n:round(st.median([r for p,r in cr if v2(p-1)==n]),3) for n in sorted({v2(p-1) for p,_ in cr})})
json.dump({'proth':rows,'control':cr,'ratio_median':st.median(ratio)},open('data/z52b/pass2/NC0/proth_v2matched.json','w'),indent=0)
