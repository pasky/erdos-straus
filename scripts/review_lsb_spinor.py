# R136 from-scratch: spinor exceptions of 3x^2+4y^2+9z^2 (Earnest 2203.02620 B6, Prop 5.1(i): M_3^2).
# Genus of B6 per Earnest Table 3 = {(3,4,9), (1,3,36)} (one class per spinor genus); genus-represented n
# = represented by some class. Exceptions = rep by (1,3,36) but not by (3,4,9).
import sys
import numpy as np
N=int(sys.argv[1]) if len(sys.argv)>1 else 50000
def reps(a,b,c):
    r=np.zeros(N+1,bool)
    for x in range(int((N/a)**.5)+1):
        for y in range(int(((N-a*x*x)/b)**.5)+1):
            s=a*x*x+b*y*y
            zmax=int(((N-s)/c)**.5)
            z=np.arange(zmax+1); r[s+c*z*z]=True
    return r
A=reps(3,4,9); B=reps(1,3,36)
exc=[n for n in range(1,N+1) if B[n] and not A[n]]
def M3(w):
    if w<1: return False
    q=w; p=2
    while p*p<=q:
        while q%p==0:
            if p%3!=1: return False
            q//=p
        p+=1
    return q==1 or q%3==1
pred=[w*w for w in range(1,int(N**.5)+1) if M3(w)]
print("exceptions:",len(exc),exc[:12]); print("predicted M3^2:",len(pred),pred[:12]); print("equal:",exc==pred)
# also: does (3,4,9) represent anything (1,3,36) misses?
print("A not B:", int((A[1:]&~B[1:]).sum()))
