"""z52d_p2_TO5_janson.py — Z1725: Janson-type lower-tail bound for the certificate count in a random-residue model.
Events A_(u,B): p ≡ a (mod q), q = 4uB, a = -(u+B) (mod q), over the pairs (u,B) in P with 4uB <= X (gcd(u,B)=1, u+B odd).
Random model: p uniform mod L (L = lcm of all q); P(A_i)=1/phi(q_i); P(A_i ∧ A_j)=1/lcm(q_i,q_j) if a_i ≡ a_j mod gcd(q_i,q_j) else 0.
mu = sum P(A_i);  Dbar = sum_{ordered (i,j), i~j} P(A_i∧A_j) with i~j (i=j included) — Janson: P(X=0) <= exp(-mu^2/(2 Dbar)).
Here the 'i~j' relation is taken as 'gcd(q_i,q_j)>1' (all q are divisible by 4, so every pair is dependent in this sense).
usage: python3 scripts/z52d_p2_TO5_janson.py X1 X2 ...   (box thresholds X=4uB bound)"""
import sys, math
from math import gcd
import numpy as np
def phi(n):
    r=n; m=n; p=2
    while p*p<=m:
        if m%p==0:
            while m%p==0: m//=p
            r-=r//p
        p+=1
    if m>1: r-=r//m
    return r
for X in map(int,sys.argv[1:]):
    pairs=[]
    for u in range(1,X):
        for B in range(1,X//(4*u)+1):
            if (u+B)%2==0 or gcd(u,B)!=1: continue
            if 4*u*B>X: continue
            q=4*u*B; a=(-(u+B))%q
            pairs.append((q,a))
    q=np.array([t[0] for t in pairs],dtype=np.int64); a=np.array([t[1] for t in pairs],dtype=np.int64)
    ph=np.array([phi(int(x)) for x in q],dtype=np.float64)
    mu=float(np.sum(1.0/ph))
    n=len(pairs)
    D=0.0
    # pairs (i,j), vectorised over j for each i
    for i in range(n):
        g=np.gcd(q[i],q)
        ok=(g>1)&(((a[i]-a)%g)==0)
        lcm=q[i]*q[ok]//g[ok]
        D+=float(np.sum(1.0/lcm))
    Dbar=mu+D      # i=j terms contribute mu
    print("X=%d: #pairs=%d  mu=%.4f  Dbar=%.4f  Dbar/mu^2=%.4f  Janson bound exp(-mu^2/(2Dbar))=%.4f"%(X,n,mu,Dbar,Dbar/mu**2,math.exp(-mu*mu/(2*Dbar))))
