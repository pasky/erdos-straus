# Hard primes vs the local multiplicative model of z69_mine_local.py: local deficit E/mu vs total deficit W/mu.
import numpy as np
p,W,E=np.load('/tmp/z69mine/localfit_E.npy')
p=p.astype(np.int64)
mu=0.179*np.log(p)**2
H=[int(l.split()[0]) for l in open('data/z69/mine/H.txt')]
idx={int(q):i for i,q in enumerate(p)}
from scipy.stats import poisson
rows=[]
for q in H:
    if q in idx:
        i=idx[q]; rows.append((q,W[i],E[i],mu[i],E[i]/mu[i],poisson.cdf(W[i],E[i])))
rows=np.array(rows)
print('H primes in (1e6,1e8]:',len(rows))
print('median E/mu over H',np.median(rows[:,4]),' all primes median',np.median(E/mu))
print('quantile of H E/mu within all:',np.median([np.mean(E/mu<x) for x in rows[:,4]]))
print('median Poisson cdf P(X<=W|E) for H:',np.median(rows[:,5]))
r=rows[np.argsort(rows[:,1]/rows[:,3])][:25]
for q,Wq,Eq,m,ratio,cdf in r: print(int(q),int(Wq),round(Eq,1),round(m,1),'E/mu=%.2f'%ratio,'cdf=%.2e'%cdf)
