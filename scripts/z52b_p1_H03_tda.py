# Z1117: persistence of (★)-certificate clouds (log u, log B, log C)/log p for hard vs easy primes near 1e6.
# Features: H0 total persistence, H1 total persistence & count (ripser, Rips). Compare groups after regressing on #points.
import subprocess, numpy as np, json, sys
from sympy import isprime
from ripser import ripser
rng=np.random.default_rng(1)
lo,hi=10**6,10**6+200000
ps=[p for p in range(lo+1,hi,4) if isprime(p)]
def certs(p):
    out=subprocess.run(['/tmp/h03certs',str(p)],capture_output=True,text=True).stdout.split()
    return np.array(out,dtype=float).reshape(-1,3)
R={}; clouds={}
for p in ps[::3]:
    c=certs(p); R[p]=len(c); clouds[p]=np.log(c)/np.log(p)
items=sorted(R,key=lambda p:R[p])
hard=items[:100]; easy=items[-100:]; mid=items[len(items)//2-50:len(items)//2+50]
def feats(X):
    d=ripser(X,maxdim=1)['dgms']
    h0=d[0][np.isfinite(d[0][:,1])]; h1=d[1]
    return [len(X), (h0[:,1]-h0[:,0]).sum(), (h1[:,1]-h1[:,0]).sum() if len(h1) else 0.0, len(h1)]
F={p:feats(clouds[p]) for p in hard+easy+mid}
# null: shuffle coordinates independently within each cloud? Better: features vs N across mid group; z-score residual of hard/easy
allp=hard+easy+mid
N=np.array([F[p][0] for p in allp]); res={}
for k,name in [(1,'H0tot'),(2,'H1tot'),(3,'H1cnt')]:
    y=np.array([F[p][k] for p in allp])
    A=np.vstack([np.ones_like(N),np.log(N)]).T
    beta=np.linalg.lstsq(A,np.log(y+1e-9),rcond=None)[0]
    r=np.log(y+1e-9)-A@beta
    rh=r[:100].mean(); re=r[100:200].mean()
    # permutation test on difference of residual means hard vs easy
    pool=r[:200]; obs=rh-re; cnt=0
    for _ in range(5000):
        rng.shuffle(pool); cnt+= abs(pool[:100].mean()-pool[100:].mean())>=abs(obs)
    res[name]=dict(resid_hard=float(rh),resid_easy=float(re),perm_p=cnt/5000)
# within-hard comparison vs mid with similar N: random clouds null - same N, coordinates from pooled marginal
out=dict(nprimes=len(R),R_hard=[R[p] for p in hard[:10]],R_easy=[R[p] for p in easy[-10:]],res=res)
print(json.dumps(out,indent=1))
json.dump(out,open('data/z52b/pass1/H03/tda.json','w'),indent=1)
