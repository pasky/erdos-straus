# Z2080: dispersion decomposition of S(p) = R(p)/2 by level C (buckets from z52d_p2_ZF1_Z2080_disp.c).
# Var(S) = Σ_b Var(S_b) + Σ_{b≠b'} Cov(S_b,S_b'); per-bucket Poisson index Var/Mean; same after removing class means mod 840.
import sys, numpy as np
fn=sys.argv[1]; L=open(fn).read().split('\n')
D=np.array([l.split() for l in L[1:] if l.strip()],np.int64); p=D[:,0]; S=D[:,1:]/2.0
def lab(b): return f'C={b+1}' if b<32 else f'C∈[{2**(b-27)},{2**(b-26)})'
def demean(X,cls):
    Y=X.astype(float).copy()
    for c in np.unique(cls):
        s=cls==c; Y[s]-=Y[s].mean(axis=0)
    return Y+X.mean(axis=0)
print(L[0], f'| {len(p)} primes')
for tag,cls in (('raw',np.zeros(len(p),int)),('mod840-demeaned',p%840),('mod 9240-demeaned (840*11)',p%9240)):
    X=demean(S,cls); tot=X.sum(axis=1); mu=S.mean(axis=0); v=X.var(axis=0)
    VT=tot.var(); Vd=v.sum()
    print(f'== {tag}: mean S={tot.mean():.2f}  Var S={VT:.2f}  Var/Mean={VT/tot.mean():.2f}  Σ_b Var S_b={Vd:.2f}  covariance share={(VT-Vd)/VT:.3f}')
    if tag=='raw' or tag.startswith('mod840'):
        print('   bucket       mean S_b   Var/Mean   share of Σ_b Var')
        for b in list(range(0,8))+list(range(32,S.shape[1])):
            if mu[b]>0: print(f'   {lab(b):16s} {mu[b]:7.3f}   {v[b]/mu[b]:6.2f}   {v[b]/Vd:.3f}')
    C=np.corrcoef(X.T); iu=np.triu_indices(S.shape[1],1); c=C[iu]; c=c[np.isfinite(c)]
    print(f'   pairwise corr between buckets: mean {c.mean():.4f}, max {c.max():.3f}, min {c.min():.3f}')
    # small-C vs large-C halves
    sm=X[:,:32].sum(axis=1); lg=X[:,32:].sum(axis=1)
    print(f'   corr(S_[C<=32], S_[C>32]) = {np.corrcoef(sm,lg)[0,1]:.3f}; Var/Mean small-C part {sm.var()/sm.mean():.2f}, large-C part {lg.var()/lg.mean():.2f}')
# Edge lines u=1 or B=1: (u,B,C)=(1,(p+1)/d,(d+1)/4) and ((p+1)/d,1,(d+1)/4) for d | p+1, d ≡ 3 (mod 4): E(p) = #{d|p+1: d≡3 (4)} unordered.
if len(sys.argv)>2:
    from sympy import divisors
    E=np.array([sum(1 for d in divisors(int(q)+1) if d%4==3) for q in p],float)
    tot=S.sum(axis=1); I=tot-E
    print(f'== edge lines (u=1 or B=1, governed by divisors of p+1): mean E={E.mean():.2f} VarE/meanE={E.var()/E.mean():.2f}; interior S-E: mean {I.mean():.2f}, Var/Mean {I.var()/I.mean():.2f}; corr(E, S-E)={np.corrcoef(E,I)[0,1]:.3f}; share of Var S explained by E: {1-np.var(I)/np.var(tot):.3f}')
    for tag,cls in (('mod840-demeaned',p%840),):
        Xi=I.copy(); Xe=E.copy()
        for c in np.unique(cls):
            s=cls==c; Xi[s]-=Xi[s].mean()-I.mean(); Xe[s]-=Xe[s].mean()-E.mean()
        print(f'   {tag}: interior Var/Mean {Xi.var()/I.mean():.2f}, edge Var/Mean {Xe.var()/E.mean():.2f}, corr {np.corrcoef(Xe,Xi)[0,1]:.3f}')
