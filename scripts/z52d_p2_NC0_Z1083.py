# z52d Pass 2 NC0 — Z1083 discrepancy-balanced splits of the 16 solution families (exhaustive, not heuristic).
# Incidence W[p,k] = 1 iff family k has >=1 solution at prime p (data/z52b/raw/var_pr_1e5.txt; primes ≡1 mod 4, 5<p<=1e5).
# Colouring s in {+1,-1}^16 (portfolio A = +1, B = -1); coverage discrepancy D_p(s) = c_A(p) - c_B(p) = (W s)_p.
# Exhaustive over all 2^16 colourings. Reports min over s of max_p |D_p| and of sum_p D_p^2, plus the all-primes-only-balanced count.
import numpy as np, json
A=np.loadtxt('data/z52b/raw/var_pr_1e5.txt',dtype=np.int64)
names=['0 even','1 even','2 even','3 even (all even)','primitive','x,y|z','x|y','isosceles','all squarefree','z<=n^2','z<=n^1.5','some power of 2','x or y prime','some coprime pair','no denom div 3','some denom div 4']
P=A[:,0]; sel=(P%4==1)&(P>5)
W=(A[sel,2:18]>0).astype(np.float32)          # primes x 16
K=16; n=W.shape[0]
best_max=(10**9,None); best_ss=(10**18,None); hist={}
chunk=4096
codes=np.arange(1<<K,dtype=np.int64)
for c0 in range(0,1<<K,chunk):
    cs=codes[c0:c0+chunk]
    S=(((cs[None,:]>>np.arange(K)[:,None])&1)*2-1).astype(np.float32)   # K x chunk
    D=W@S                                                             # n x chunk
    mx=np.abs(D).max(0); ss=(D.astype(np.float64)**2).sum(0)
    i=int(np.argmin(mx)); 
    if mx[i]<best_max[0]: best_max=(float(mx[i]),int(cs[i]))
    j=int(np.argmin(ss))
    if ss[j]<best_ss[0]: best_ss=(float(ss[j]),int(cs[j]))
    for v in np.unique(mx): hist[float(v)]=hist.get(float(v),0)+int((mx==v).sum())
def show(code): return {'A':[names[k] for k in range(K) if (code>>k)&1],'B':[names[k] for k in range(K) if not (code>>k)&1]}
print('primes',n,'colourings 2^16 exhaustive')
print('min over splits of max_p |D_p| =',best_max[0]); print('  split:',show(best_max[1]))
print('min over splits of sum_p D_p^2 =',best_ss[0]); print('  split:',show(best_ss[1]))
print('distribution of max|D| over splits (value: count):',sorted(hist.items())[:8])
# baseline: the trivial split with "2 even" alone in A vs everything else (for reference)
s=np.ones(K,dtype=np.float32); D0=W@s
print('baseline all-A: max|D|=',float(np.abs(D0).max()),'primes with D=0 (any split):',int((np.abs(D0)==0).sum()))
json.dump(dict(min_max=best_max[0],split_max=show(best_max[1]),min_ss=best_ss[0],split_ss=show(best_ss[1])),open('data/z52b/pass2/NC0/sub/Z1083_split.json','w'),indent=1)
