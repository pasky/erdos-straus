# R104 from-scratch: ET 3-way split inequality used in Prop (Type II).
# For p prime, a<=b, (a,b)=1, e|a+b, c=(a+b)/e, p+e=m*a*b*d:
#   abd <= 2p/m,  (made)(macd)(mab)^{1/2} <= 8 m^{1/2} p^2,  (e,ad)=1, (e,m)=1 (m<p).
import random, math
from sympy import isprime
random.seed(104); worst=0; cnt=0
for m in range(4,60):
    for a in range(1,25):
        for b in range(a,60):
            if math.gcd(a,b)!=1: continue
            for e in [x for x in range(1,a+b+1) if (a+b)%x==0]:
                c=(a+b)//e
                for d in range(1,30):
                    p=m*a*b*d-e
                    if p<=m or not isprime(p): continue
                    cnt+=1
                    assert a*b*d<=2*p/m
                    assert math.gcd(e,a*d)==1 and math.gcd(e,m)==1
                    lhs=(m*a*d*e)*(m*a*c*d)*math.sqrt(m*a*b)
                    worst=max(worst,lhs/(8*math.sqrt(m)*p*p))
                    mn=min(m*a*d*e,m*a*c*d,m*a*b)
                    assert mn<=8**0.4*m**0.2*p**0.8+1e-9
print("tuples",cnt,"max lhs/(8 m^1/2 p^2) =",round(worst,4))
