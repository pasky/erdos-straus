# Q1: how much of W(p) is "local"? Additive (multiplicative in W) model over p mod q for prime powers q,
# fitted by backfitting on half of the primes p = 1 mod 8 in (1e6,1e8], evaluated on the other half.
import numpy as np, sys
d=np.loadtxt('/tmp/z69mine/w1e8.tsv',dtype=np.int64)
p,W=d[:,0],d[:,1].astype(float)
sel=p>10**6; p,W=p[sel],W[sel]
L=np.log(p.astype(float)); mu=0.179*L*L; w=W/mu
rng=np.random.default_rng(69); tr=rng.random(len(p))<0.5; te=~tr
import sympy
mods=[16,32,64,128]+[q for q in sympy.primerange(3,int(sys.argv[1]) if len(sys.argv)>1 else 200)]
mods+= [9,27,25,49,121]
# multiplicative model E W = mu * prod_q g_q(p mod q); fit by Poisson backfitting (iterative proportional fitting)
G={q:np.ones(q) for q in mods}
logpred=np.zeros(len(p))
def pred():
    s=np.zeros(len(p))
    for q in mods: s+=np.log(G[q][p%q])
    return np.exp(s)
for it in range(6):
    for q in mods:
        P=pred()
        key=p%q
        num=np.bincount(key[tr],weights=W[tr],minlength=q); den=np.bincount(key[tr],weights=(mu*P)[tr],minlength=q)
        ratio=np.where(den>0,num/np.maximum(den,1e-300),1.0)
        G[q]=G[q]*ratio
    P=pred()
    E=mu*P
    # deviance-like: R^2 of w on test
    r2=1-np.var((W-E)[te]/mu[te])/np.var(w[te])
    # Poisson share
    print('iter',it,'test R2(w)',round(r2,4),'Poisson floor share', round(np.mean((E/mu**2)[te])/np.var(w[te]),4), flush=True)
# residual dispersion
z=(W-E)/np.sqrt(E)
print('test var of Pearson residual (Poisson=1):',np.var(z[te]))
# report largest factor ranges
for q in mods[:20]:
    g=G[q]; nz=[c for c in range(q) if np.gcd(c,q)==1]
    print(q, 'min',round(g[nz].min(),3),'max',round(g[nz].max(),3), 'g(1)',round(g[1],3))
np.save('/tmp/z69mine/localfit_E.npy',np.stack([p,W,E]))
