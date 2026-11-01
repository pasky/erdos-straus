# z52d Pass 2 NC0, item Z0651 — least certificate-family size s(p) for hard-class primes p in [LO,HI) (chunked version of z52b_dividing_leastfam.py)
import numpy as np, sys, time, json
from sympy import divisors
LO=int(sys.argv[1]); HI=int(sys.argv[2]); X_MAX=int(sys.argv[3]) if len(sys.argv)>3 else 5000
t0=time.time()
seg=np.ones(HI-LO,dtype=bool)
r=int(HI**0.5)+1
base=np.ones(r+1,dtype=bool); base[:2]=False
for i in range(2,int(r**0.5)+1):
    if base[i]: base[i*i::i]=False
for q in np.nonzero(base)[0]:
    q=int(q); st=max(q*q,((LO+q-1)//q)*q)
    seg[st-LO::q]=False
idx=np.arange(LO,HI,dtype=np.int64)
mask=seg & (idx>=2) & np.isin(idx%840,[1,121,169,289,361,529])
ps=idx[mask]
print('hard primes in chunk:',len(ps),'sieve time',round(time.time()-t0,1),flush=True)
fams=[]
for a in range(1,X_MAX+1):
    for d in range(1,X_MAX//a+1):
        if a*d>X_MAX: break
        fams.append((a*d,4*a*d,'I',a,d))
for a in range(1,X_MAX+1):
    for b in range(a,X_MAX//a+1):
        fams.append((a*b,4*a*b,'II',a,b))
fams.sort(key=lambda t:(t[0],t[1]))
alive=ps.copy(); least={}
for s,m,typ,a,b in fams:
    if len(alive)==0: break
    if typ=='I': res={(-f)%m for f in divisors(4*a*a*b+1)}
    else: res={(-e)%m for e in divisors(a+b)}
    tab=np.zeros(m,dtype=bool); tab[list(res)]=True
    hit=tab[alive%m]
    for p in alive[hit]: least[int(p)]=s
    alive=alive[~hit]
print('unsolved within X_MAX:',len(alive),'time',round(time.time()-t0,1),flush=True)
vals=np.array([least[int(p)] for p in ps if int(p) in least])
qs={q:float(np.quantile(vals,q)) for q in (0.5,0.9,0.99,0.999,1.0)} if len(vals) else {}
order=np.argsort(-vals)[:8]
top=[(int(ps[i]),int(vals[i])) for i in order] if len(vals) else []
print('quantiles',qs); print('top (p,s)',top)
json.dump({'LO':LO,'HI':HI,'n_hard':int(len(ps)),'unsolved':int(len(alive)),'quantiles':qs,'top':top,'time_s':round(time.time()-t0,1)},open(f'data/z52b/pass2/NC0/leastfam_{LO}_{HI}.json','w'),indent=1)
