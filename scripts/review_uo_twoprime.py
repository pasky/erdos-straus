import numpy as np, sys
from fractions import Fraction
sys.path.insert(0,'.')
from review_uo_common import *
S=[3,5,7,11]; n=(13*19)**2; ls=[13,19]
ys=np.arange(1,4*n+1,dtype=np.int64)
cnt={}
for x in range(n//4+1, n//4+1500):
    A,B=4*x-n,n*x
    yy=ys[ys>=x]; num=A*yy-B; den=B*yy; ok=num>0
    yy,num,den=yy[ok],num[ok],den[ok]; g=np.gcd(num,den); num//=g
    m=num.copy()
    for q in S:
        for _ in range(40):
            d=(m%q==0)
            if not d.any(): break
            m[d]//=q
    for y in yy[m==1]:
        t=Fraction(4,n)-Fraction(1,x)-Fraction(1,int(y))
        if not is_S_square_monoid(t.numerator,S): continue
        z=1/t; check_ESS(n,x,int(y),z,S)
        sh=[]
        for l in ls:
            vs=[vp(Fraction(x),l),vp(Fraction(int(y)),l),vp(z,l)]
            u=sum(v==0 for v in vs); b=sum(v>=2 for v in vs)
            sh.append('I' if (u,b)==(2,1) else 'II' if (u,b)==(1,2) else 'o')
        cnt[tuple(sh)]=cnt.get(tuple(sh),0)+1
print(n,cnt)
