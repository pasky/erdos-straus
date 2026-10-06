# min n such that an exchangeable k-wise-independent law of Bernoulli(p) bits has P(no ones)=0
# (campaign convention; BGP's n_c(k,1-p)). Exact feasibility via scipy LP on S-distribution.
from fractions import Fraction as Fr
from math import comb
import numpy as np
from scipy.optimize import linprog
def feasible(n,k,p):
    A=[[comb(s,j) for s in range(1,n+1)] for j in range(k+1)]
    b=[comb(n,j)*p**j for j in range(k+1)]
    A=np.array(A,float); b=np.array(b,float)
    # scale rows
    sc=np.maximum(1,np.abs(A).max(1)); A/=sc[:,None]; b/=sc
    r=linprog(np.zeros(n),A_eq=A,b_eq=b,bounds=[(0,None)]*n,method="highs")
    return r.status==0
for q in [2,3,5,8,16]:
    p=1/q; r=p/(1-p)
    for k in [1,2,3,4,6]:
        n=k+1
        while not feasible(n,k,p): n+=1
        lem=next(m for m in range(1,10**5) if m*r>=(k+1)+(2*k+1)*r)
        bgp_lo = k/(2*p)+1 if k%2==0 else (k+1)/(2*p)
        print(f"q={q:2d} k={k}: n_c(LP)={n:4d}  Lemma1.1 suffices n>={lem:4d}  BGP lower={bgp_lo:.1f}")
