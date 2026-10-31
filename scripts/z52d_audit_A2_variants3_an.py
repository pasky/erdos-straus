"""Failure sets of the 16 Sun-style predicates of z52d_audit_A2_variants3.c (primes only)."""
import numpy as np, sys
names=['x+y square','x+y+z square','y-x square','x+y prime','z-y square','x triangular','n | x+y+z','x+z square',
       'x=ceil(n/4)','x,y squarefree','x odd','x=1 mod 4','x=1 mod 3','z prime','y prime','y^2>=xz']
A=np.loadtxt(sys.argv[1],dtype=np.int64)
p1=A[A[:,0]%4==1]
for i,nm in enumerate(names):
    c=2+i; f=A[A[:,c]==0,0]; f1=p1[p1[:,c]==0,0]
    big=p1[p1[:,0]>A[:,0].max()//2]
    print(f"{nm:16s} fail primes={len(f):6d} (p=1(4): {len(f1):6d}, frac {len(f1)/len(p1):.4f}) last={f.max() if len(f) else None} "
          f"head={f[:10].tolist()} meanshare(top half)={np.mean(big[:,c]/big[:,1]):.3f}")
