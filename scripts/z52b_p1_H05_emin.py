# Z1792: minimal Type II e-slice e_min(p) (ES(p) <=> exists e ≡ -p mod 4, ab | N=(p+e)/4, e | a+b)
# for primes p ≡ 1 (24) <= X; then how much of log e_min is explained by p mod small moduli + log p (cheap
# stand-in for symbolic regression: if residual ≈ geometric-lottery noise there is no closed-form law to find).
import sys, math, numpy as np
from sympy import primerange, divisors
X=int(sys.argv[1])
def ok(p,e):
    N=(p+e)//4; D=divisors(N)
    Ds=set(D)
    for a in D:
        if a*a>N: break
        for b in D:
            if b<a: continue
            if N%(a*b)==0 and (a+b)%e==0: return True
    return False
rows=[]
for p in primerange(25,X):
    if p%24!=1: continue
    e=3
    while not ok(p,e): e+=4
    rows.append((p,e))
P=np.array([r[0] for r in rows]); E=np.array([r[1] for r in rows],float)
y=np.log(E)
print("n",len(P),"mean e",E.mean(),"max e",E.max(),"at",P[E.argmax()],"frac e=3:",(E==3).mean())
def r2(cols):
    A=np.column_stack([np.ones(len(P))]+cols); c,*_=np.linalg.lstsq(A,y,rcond=None); res=y-A@c
    return 1-res.var()/y.var()
feats=[np.log(P)]
for q in [5,7,11,13,17,19,23,29,31,37,41,43]:
    for r in range(1,q):
        feats.append((P%q==r).astype(float))
print("R2 logp:",round(r2([np.log(P)]),3)," +one-hot p mod primes<=43:",round(r2(feats),3))
# held-out
idx=np.arange(len(P)); tr=idx%2==0; te=~tr
A=np.column_stack([np.ones(len(P))]+feats); c,*_=np.linalg.lstsq(A[tr],y[tr],rcond=None)
res=y[te]-A[te]@c; print("held-out R2:",round(1-res.var()/y[te].var(),3))
np.save("data/z52b/pass1/H05/emin.npy",np.array(rows))
