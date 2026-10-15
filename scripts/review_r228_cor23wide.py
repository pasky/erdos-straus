"""R228: Cor 2.3 explicit table vs the direct character criterion (review_r228_signfield.F_in_Sigma), wide range,
and Cor 2.2 (tk+1 square) vs criterion."""
import sys
from math import isqrt
sys.argv=['x','1','1','1','1']
src=open(__file__.replace('review_r228_cor23wide.py','review_r228_signfield.py')).read().rsplit('\nmain()',1)[0]
exec(src)
KM, UM = int(sys.argv[0] == 'x' and 60), 200
bad=0; tot=0
for k in range(1, KM+1):
    for u in range(1, UM+1):
        tot+=1
        if F_in_Sigma(sqfree(k+u), u) != cor23(k,u): bad+=1; print("u-mismatch",k,u)
    for t in range(1, 121):
        b=t*k+1
        if F_in_Sigma(sqfree(t*b), t) != (isqrt(b)**2==b): bad+=1; print("t-mismatch",k,t)
print("checked", tot, "u-levels and", KM*120, "t-levels; mismatches:", bad)
