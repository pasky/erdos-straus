# Z2902 analysis: X_w(p) = R_w(p)/M_w(p) for the weights of z52d_p2_ZF1_Z2902_rw.c; variance, Poisson-null ratio,
# left-tail quantiles, z-score of the left tail, and the same after removing p mod 840 class means (residue effect).
import sys, numpy as np
import gzip
fn=sys.argv[1]; L=(gzip.open(fn,"rt") if fn.endswith(".gz") else open(fn)).read().split('\n')
names=L[0].split('weights:')[1].split(); P0=int(L[0].split()[2]); H=int(L[0].split()[4])
M0=np.array(L[1].split()[1:],float); M1=np.array(L[2].split()[1:],float); V0=np.array(L[3].split()[1:],float); V1=np.array(L[4].split()[1:],float)
D=np.array([l.split() for l in L[5:] if l.strip()],float); p=D[:,0]; R=D[:,1:]
t=((p-P0)/H)[:,None]; M=M0+(M1-M0)*t; V=V0+(V1-V0)*t
X=R/M
print(f'# {fn}: {len(p)} primes p≡1(4) in [{P0},{P0+H}]')
print('weight        M_w     mean X  sd X   CV_pois  var/pois  q.001  q.01   min    z(q.001)  P(R_w=0)  sd_X|840  hard1/all')
cls=(p%840).astype(int); hard=np.isin(cls,[1,121,169,289,361,529])
rows=[]
for k,nm in enumerate(names):
    x=X[:,k]; m=x.mean(); sd=x.std(); cvp=np.sqrt(V[:,k]/M[:,k]**2).mean()
    q1,q2=np.quantile(x,[0.001,0.01]); mn=x.min()
    # remove mod-840 class means
    xr=x.copy()
    for c in np.unique(cls):
        s=cls==c; xr[s]=x[s]-x[s].mean()+m
    sdr=xr.std()
    print(f'{nm:12s} {M[:,k].mean():7.2f}  {m:.3f}  {sd:.3f}  {cvp:.3f}   {(sd/cvp)**2:6.2f}   {q1:.3f}  {q2:.3f}  {mn:.3f}  {(m-q1)/sd:6.2f}   {np.mean(R[:,k]==0):.5f}   {sdr:.3f}   {x[hard].mean()/m:.3f}')
    rows.append(x)
X=np.array(rows)
print('corr(X_w, X_sharp):',' '.join(f'{np.corrcoef(X[0],X[k])[0,1]:.3f}' for k in range(len(names))))
# primes in the bottom 1% of sharp: how many stay bottom-1% under each weight
b=X[0]<=np.quantile(X[0],0.01)
print('bottom-1% sharp primes: mean X_w rank-quantile under each weight:',' '.join(f'{np.mean([np.mean(X[k]<=v) for v in X[k][b]]):.3f}' for k in range(len(names))))
