# O156 independent spot-check of graph_cayley_moves Thm A.1: chord through two points of
# Omega (sign type (1,3), arbitrary special index) on sigma3=0 never has its third point in Omega.
import numpy as np
rng=np.random.default_rng(1)
def s3(X): a,b,c,d=X; return a*b*c+a*b*d+a*c*d+b*c*d
def rand_omega():
    while True:
        n=rng.uniform(0.1,10); x,y=rng.uniform(0.1,10,2)
        r=1/n-1/x-1/y
        if r>0:
            X=np.array([-n,x,y,1/r]); i=rng.integers(4)
            X[[0,i]]=X[[i,0]]
            return X*rng.choice([-1,1])
def typ(X):
    k=(X<0).sum(); return min(k,4-k)
bad=0;N=200000;cnt={0:0,1:0,2:0}
for _ in range(N):
    P,Q=rand_omega(),rand_omega()
    # f(t)=s3(P+tQ)= c1 t + c2 t^2 ; get c1,c2 by evaluation
    f1=s3(P+Q); fm=s3(P-Q)
    c2=(f1+fm)/2; c1=(f1-fm)/2
    if abs(c2)<1e-12: continue
    R=P+(-c1/c2)*Q
    if np.min(np.abs(R))<1e-9*np.max(np.abs(R)): continue
    t=typ(R); cnt[t]+=1
    if t==1: bad+=1
print("types of third point:",cnt,"in Omega:",bad)
