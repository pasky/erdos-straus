# R104 from-scratch: Bonferroni Q_r(h)=sum_{j<=r}(-1)^j C(h,j), r even:
# check 1_{h=0} <= Q_r(h) <= 1_{h=0} + C(h,r+1) for h<=200, r<=40.
from math import comb
bad=0
for r in range(0,41,2):
    for h in range(0,201):
        Q=sum((-1)**j*comb(h,j) for j in range(r+1))
        lo=1 if h==0 else 0
        if not (lo<=Q<=lo+comb(h,r+1)): bad+=1; print("FAIL",r,h,Q)
print("bonferroni checks done, failures:",bad)
