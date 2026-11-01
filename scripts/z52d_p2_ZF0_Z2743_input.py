"""Exact polar part of a concrete weight-1/2 Borcherds input for M=4,p=5."""
import json
from fractions import Fraction
J={-1:1,1:196884,2:21493760,3:864299970,4:20245856256}
def mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,0)+x*y
    return out
powers=[{0:1}]
for i in range(5):powers.append(mul(powers[-1],J))
a1,a2,a3,a4=[J[i] for i in range(1,5)]
poly={5:1,3:-5*a1,2:-5*a2,1:5*a1*a1-5*a3,0:5*a1*a2-5*a4}
series={}
for i,c in poly.items():
    for n,v in powers[i].items():series[n]=series.get(n,0)+c*v
assert {n:c for n,c in series.items() if n<=0 and c}=={-5:1}
# F=(P5(J)-2J)*Theta_4. Exponents scaled by 16.
polar={};constant={}
for n in range(-9,10):
    r=n%8
    for e,c in [(-80,1),(-16,-2)]:
        exp=e+n*n
        if exp<0:polar[(r,exp)]=polar.get((r,exp),0)+c
        elif exp==0:constant[r]=constant.get(r,0)+c
terms=[dict(component=r,exponent=str(Fraction(e,16)),coefficient=c) for (r,e),c in sorted(polar.items()) if c]
print(json.dumps(dict(P5_in_J={str(k):v for k,v in poly.items()},F='(P5(J)-2J)*Theta_4; J=j-744',polar_terms=terms,constant_terms=constant,borcherds_weight=constant.get(0,0)/2),indent=2))
