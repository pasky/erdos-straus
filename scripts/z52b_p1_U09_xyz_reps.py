# z52b pass1 U09 (Z1982 follow-up): multiplicity r(n) = #{(x,y,z): x,y,z>=2, xyz-x-y-z=n} (all orders), n <= NZ.
# Compares mean r(n) with the naive log^2 heuristic (~ (1/2) log^2 n).  Usage: python3 scripts/z52b_p1_U09_xyz_reps.py NZ
import sys, math, numpy as np
NZ=int(sys.argv[1])
r=np.zeros(NZ+1,dtype=np.int64)
for x in range(2,NZ+1):
    for y in range(2,NZ+1):
        m=x*y-1
        if m<=0: continue
        # z>=2, n = z*m - (x+y) <= NZ
        zmax=(NZ+x+y)//m
        if zmax<2: 
            if x*y-1 > NZ+ 2*NZ: break
            continue
        z=np.arange(2,zmax+1)
        n=z*m-(x+y)
        ok=(n>=1)&(n<=NZ)
        np.add.at(r,n[ok],1)
for lo,hi in [(100,1000),(1000,3000),(3000,NZ)]:
    s=r[lo:hi]
    if len(s)==0: continue
    print(f"n in [{lo},{hi}): mean r(n)={s.mean():.3f}  frac r=0: {np.mean(s==0):.4f}   0.5*log^2(mid)={0.5*math.log((lo+hi)/2)**2:.2f}")
ex=np.flatnonzero(r[1:]==0)+1
print("exceptions:", len(ex), " last 10:", ex[-10:].tolist())
