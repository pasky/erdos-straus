"""z52d avenue Q04 Z0762 (extension): R(n) at Lehmer pseudosquares (OEIS A002189) <= 5e7 vs all non-square n = 1 (8)
in a +-2% window (controls). Needs R array from scripts/z52b_p1_H04_rstar.c (uint16, R(n) for n<=N). EVIDENCE only."""
import numpy as np, math, sys
R=np.fromfile(sys.argv[1],dtype=np.uint16); N=len(R)-1
ps=[73,241,1009,2641,8089,18001,53881,87481,117049,515761,1083289,3206641,3818929,9257329,22000801,48473881]
rat=[];crat=[];crat2=[]
for n in ps:
    if n>N: break
    lo,hi=int(n*0.98),int(n*1.02)
    m=np.arange(lo,hi+1); m=m[(m%8==1)]
    r=np.round(np.sqrt(m)).astype(np.int64); sq=r*r==m; m=m[~sq]
    L2=math.log(n)**2
    c=R[m].astype(float)
    sqc={(x*x)%840 for x in range(840) if math.gcd(x,840)==1}
    m2=m[np.isin(m%840,list(sqc))]; c2=R[m2].astype(float)
    rat.append(R[n]/L2); crat.append(c.mean()/L2); crat2.append(c2.mean()/L2 if len(c2) else np.nan)
    print(f"{n:>9} R={R[n]:>4}  ctrl mean={c.mean():6.1f} sd={c.std():5.1f} P(ctrl<=R)={np.mean(c<=R[n]):.4f}  R/L2={R[n]/L2:.3f} ctrl/L2={c.mean()/L2:.3f}  mordell-class ctrl/L2={(c2.mean()/L2 if len(c2) else float('nan')):.3f} (n={len(c2)}) P(c2<=R)={(np.mean(c2<=R[n]) if len(c2) else float('nan')):.3f}")
print("mean ratio R/ctrl over pseudosquares:", np.mean(np.array(rat)/np.array(crat)))
r=np.array(rat)[4:]; print("n>=8089: mean R/ctrl", np.mean(r/np.array(crat)[4:]), " mean R/mordell-ctrl", np.nanmean(r/np.array(crat2)[4:]))
