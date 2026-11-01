# z52d Pass 2 NC0, item Z0814 — Proth-type primes k*2^n+1 (k odd<=15, p<=PMAX) as U(p) test bed; control = random primes ≡1 (4) in same range.
import sys, random, subprocess, math, json
import statistics as st
from concurrent.futures import ThreadPoolExecutor
from sympy import isprime
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 10**7
prot=set()
for k in range(1,16,2):
    n=2
    while k*2**n+1<=PMAX:
        p=k*2**n+1
        if isprime(p): prot.add((p,k,n))
        n+=1
prot=sorted(prot)
random.seed(7)
import numpy as np
sv=np.ones(PMAX+1,dtype=bool); sv[:2]=False
for i in range(2,int(PMAX**0.5)+1):
    if sv[i]: sv[i*i::i]=False
pool={}
for q in np.nonzero(sv[PMAX//2:])[0]+PMAX//2:
    q=int(q)
    if q%4==1: pool.setdefault(q%840,[]).append(q)
# residue-matched controls: for each Proth prime, 6 random primes ≡1 (4) in [PMAX/2,PMAX] with the same p mod 840
ctrl=[]
for p,k,n in prot:
    lst=pool.get(p%840,[])
    if lst: ctrl+= [(p,c) for c in random.sample(lst,min(6,len(lst)))]
ctrl=[c for _,c in ctrl]
def U(p):
    out=subprocess.run(['/tmp/z52b_count','4',str(p),str(p)],capture_output=True,text=True,timeout=900).stdout.split()
    return int(out[1])
def run(lst):
    with ThreadPoolExecutor(4) as ex: return list(ex.map(U,[p for p,_,_ in lst] if lst and isinstance(lst[0],tuple) else lst))
pu=run(prot); cu=run(ctrl)
rows=[]
for (p,k,n),u in zip(prot,pu): rows.append(dict(p=p,k=k,n=n,U=u,U_over_log2=u/math.log(p)**2,U_over_log3=u/math.log(p)**3))
cr=[dict(p=p,U=u,U_over_log2=u/math.log(p)**2,U_over_log3=u/math.log(p)**3) for p,u in zip(ctrl,cu)]
# ratio of Proth median to matched-control median, per Proth prime
import collections
mc=collections.defaultdict(list)
for c in cr: mc[c['p']%840].append(c['U_over_log2'])
ratio=[r['U_over_log2']/st.median(mc[r['p']%840]) for r in rows if mc.get(r['p']%840)]
print('residue-matched: median ratio Proth/control =',round(st.median(ratio),3),'n=',len(ratio))
print('residue-matched control median U/log^2 =',round(st.median([c['U_over_log2'] for c in cr]),3))
print('Proth primes <=',PMAX,':',len(prot))
print('Proth median U/log^2 =',round(st.median([r['U_over_log2'] for r in rows]),3),' control (random p≡1(4) in [PMAX/2,PMAX]) median U/log^2 =',round(st.median([r['U_over_log2'] for r in cr]),3))
print('Proth min U =',min(rows,key=lambda r:r['U'])['U'],min(rows,key=lambda r:r['U']))
print('control min U =',min(cr,key=lambda r:r['U']))
print('Proth by k: median U/log^2 p')
for k in range(1,16,2):
    v=[r['U_over_log2'] for r in rows if r['k']==k]
    if v: print(' k=',k,'n=',len(v),round(st.median(v),3))
json.dump({'proth':rows,'control':cr},open(f'data/z52b/pass2/NC0/proth_{PMAX}.json','w'),indent=1)
