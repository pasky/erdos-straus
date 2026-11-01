import sys, numpy as np, json, time
sys.argv=['x']
src=open('scripts/z52d_p2_TO3_bm.py').read()
# reuse pairs + Mbm definitions only (stop before the window sampling)
head=src.split('# ---- (a) window samples ----')[0]
exec(head)
from sympy import primerange
Rarr=np.loadtxt('/tmp/z52/words3e6.txt',dtype=np.int64)[:,3]
lo,hi=10**4,10**5
allp=[p for p in primerange(lo,hi) if p%4==1]
t=time.time()
M=np.array([Mbm(int(p))[0] for p in allp]); R=np.array([Rarr[p-1] for p in allp])
print('time',round(time.time()-t,1),'n',len(allp))
exp0=float(np.sum(np.exp(-np.maximum(M,0))))
print('exhaustive expected R=0 (Poisson(M_BM)):', round(exp0,4), 'observed', int((R==0).sum()))
print('M quantiles', np.percentile(M,[0,1,5,25,50,75,95,100]).round(2).tolist())
bins=[0,2,4,6,8,10,12,20,100]
for a,b in zip(bins[:-1],bins[1:]):
    s=(M>=a)&(M<b)
    if s.sum(): print(f'M in [{a},{b}): n={int(s.sum())} obs_zero={int((R[s]==0).sum())} exp_poisson={float(np.exp(-M[s]).sum()):.3f} mean_R={R[s].mean():.1f}')
json.dump(dict(lo=lo,hi=hi,n=len(allp),expected_R0=exp0,observed_R0=int((R==0).sum()),zero_primes=[int(p) for p,r in zip(allp,R) if r==0],M_at_zero=[float(m) for m,r in zip(M,R) if r==0]),open('data/z52b/pass2/TO3/bm_poisson_1e4_1e5.json','w'),indent=1)
