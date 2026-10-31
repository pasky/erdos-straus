"""z52d audit A2, item Z1993: (★) via two-part restricted partitions (Popoviciu = Sylvester waves for 2 parts).
Check: R(p) = #{(u,B): gcd=1, 4uBC-u-B=p, C>=1} equals #{(u,B) coprime: both Popoviciu periodic parts maximal at p
and p_{u,B}(p) = 3 mod 4}, where p_{u,B}(n) = n/(uB) - {B'n/u} - {u'n/B} + 1, B'B=1 (u), u'u=1 (B)."""
from fractions import Fraction as F
from math import gcd
def denum(n,u,B):  # brute-force number of (s,t)>=0 with us+Bt=n
    return sum(1 for s in range(n//u+1) if (n-u*s)%B==0)
def popov(n,u,B):
    Bi = pow(B,-1,u) if u>1 else 0; ui = pow(u,-1,B) if B>1 else 0
    fr = lambda a,m: F((a%m),m) if m>1 else F(0)
    return F(n,u*B) - fr(Bi*n,u) - fr(ui*n,B) + 1
bad=0
for p in [409,433,601,1009,2521,4801,8641]:
    R=0; W=0
    for u in range(1,p+1):
        for B in range(1,(p+u)//(3*u)+2):
            if gcd(u,B)!=1: continue
            if 4*u*B-u-B>p: break
            if (p+u+B)%(4*u*B)==0: R+=1
            pv=popov(p,u,B)
            if u*B<=60 and pv!=denum(p,u,B): bad+=1
            ext = (u==1 or (pow(B,-1,u)*p)%u==u-1) and (B==1 or (pow(u,-1,B)*p)%B==B-1)
            if ext and pv%4==3: W+=1
    print(p,"R(p)=",R,"wave-count=",W)
print("Popoviciu mismatches (uB<=60):",bad)
