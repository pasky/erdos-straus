import numpy as np
from math import isqrt
LO,HI=10**6,10**7
def cnt_class(lo,hi,modc,resc,X):
    # exact mean # ordered interior words with larger endpoint <= X over n in [lo,hi] with n ≡ resc mod modc
    tot=0.0; cnt=(hi//modc)-((lo-1)//modc)  # approx count of n in class
    for u in range(3,X+1):
        for v in range(u,X+1):
            m=u*v; r=(-u-v)%m
            # n ≡ r mod m and n ≡ resc mod modc: count solutions in [lo,hi]
            from math import gcd
            g=gcd(m,modc)
            if (r-resc)%g: continue
            L=m*modc//g
            # find n0 via brute search over k: n = r + m k, k < modc/g
            for k in range(modc//g):
                n0=r+m*k
                if n0%modc==resc: break
            c=(hi-n0)//L-(lo-1-n0)//L if n0<=hi else 0
            tot+=(2 if u<v else 1)*c
    return tot/cnt
for name,modc,resc in [("odd",2,1),("even",2,0),("n=1 mod 8",8,1),("n=5 mod 8",8,5),("n=7 mod 8",8,7)]:
    print(name, "mean words v<=256:", round(cnt_class(LO,HI,modc,resc,256),3))
# squares
def words_le(n,X):
    c=0
    for v in range(3,X+1):
        a=(-n)%v
        if a==0:
            if (n+2*v)%(v*v)==0: c+=1
        elif a>=3 and (n+a+v)%(a*v)==0: c+=2
    return c
for par,name in [(1,"odd squares"),(0,"even squares")]:
    ms=[m for m in range(1000,10000) if m%2==par]
    vals=[words_le(m*m,256) for m in ms]
    print(name,"m in [1000,10000): mean words v<=256:",round(np.mean(vals),3),"count",len(ms))
