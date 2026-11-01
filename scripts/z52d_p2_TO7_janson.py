# Z2755 (lower tail of certificate count vs Janson), Z2842 (Borel–Cantelli tail), Z2647 (Janson Delta on slice-dependency graph, hard primes)
import sys, math
from collections import Counter
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; minI=tsv['minI']
ks=list(range(3,401,4)); K=len(ks)
m0=a['type']==0
S=np.zeros((len(P),K),np.int8)
S[np.searchsorted(P,a['p'][m0]),(a['k'][m0]-3)//4]=B['dh'][m0]
print("== Z2755: N_K = #successful Type-I slices with k<=K; Janson lower tail P(N=0) <= exp(-mu + Delta/2)")
for label,sel in [("all p",np.ones(len(P),bool)),("hard",hard)]:
    for Kc in [15,31,63,127,255,399]:
        cols=[j for j,k in enumerate(ks) if k<=Kc]
        N=S[sel][:,cols].sum(1)
        mu=N.mean(); p0=(N==0).mean()
        if p0<=0: print(label,Kc,"no zeros"); continue
        # Janson-form fit: p0 = exp(-mu/(1+Delta/mu))  => Delta/mu = mu/(-ln p0) - 1
        dm=mu/(-math.log(p0))-1
        print(f"  {label:6s} K<={Kc:3d}: mu={mu:.3f} P(N=0)={p0:.5f} Poisson exp(-mu)={math.exp(-mu):.5f}  fitted Delta/mu={dm:.3f}")
print("== Z2842: Borel–Cantelli tail P(minI > K) (type I first success index) vs K; power-law fit")
Ks=np.array([7,15,31,63,127,255]); pt=np.array([np.mean(minI[minI>0]>k) for k in Ks])
slope,inter=np.polyfit(np.log(Ks),np.log(pt),1)
print("  P(minI>K):",dict(zip(Ks.tolist(),np.round(pt,6).tolist())),"  fitted exponent alpha in P ~ K^-alpha:",round(-slope,3))
print("  Borel–Cantelli under independence across primes: sum_p (log p)^(-alpha*A) for the 'no certificate with k<=(log p)^A' event diverges for every A>0 (since sum_p 1/(log p)^c = infinity for any c)")
print("== Z2647: Janson Delta for slice dependency (hard primes, p≤1e6; events E_k = Type-I hit at k≤399; k~k' iff M_k, M_k' share a prime factor)")
def pf(n):
    s=set(); d=2
    while d*d<=n:
        while n%d==0: s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return s
sel=np.nonzero(hard)[0]
Dsum=0.0; musum=0.0; edges_tot=0; pairs_both=0
for i in sel:
    p=int(P[i]); fac=[]
    for k in ks:
        M=(k*p+1)//4
        fac.append(pf(M) if M>1 else set())
    E=S[i]
    musum+=E.sum()
    for x in range(K):
        for y in range(x+1,K):
            if fac[x] & fac[y]:
                edges_tot+=1
                both=E[x]*E[y]
                pairs_both+=both
                Dsum+=2*both   # ordered pairs
mu_avg=musum/len(sel)
print(f"  hard primes {len(sel)}: mean mu={mu_avg:.3f}; dependent unordered pairs per prime={edges_tot/len(sel):.1f}; observed Delta (sum over ordered dependent pairs of both-hit indicators) per prime = {Dsum/len(sel):.4f}; Delta/mu = {Dsum/len(sel)/mu_avg:.4f}")
print("  note: Delta here is a per-prime empirical count (pairs realised), not an exact probabilistic Delta; p≈1e7 and 1e12 not available in this run")
