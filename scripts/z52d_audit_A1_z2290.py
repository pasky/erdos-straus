# Z2290: where do (*) solutions sit relative to Lenstra's regime (modulus 4C >= N^{1/3}, N=4Cp+1)?
import numpy as np, sys, math
from sympy import isprime
def sols(p):
    out=[]
    u=1
    while 4*u*1*1-u-1<=p:
        B=np.arange(1,(p+u)//(4*u-1)+2,dtype=np.int64)
        num=p+u+B; den=4*u*B
        ok=(num%den==0)
        for b in B[ok]:
            C=(p+u+int(b))//(4*u*int(b)); out.append((u,int(b),C))
        u+=1
    return out
for base in [10**5,10**6,10**7]:
    ps=[q for q in range(base+1,base+4000,4) if isprime(q)][:15]
    tot=0; len_=0; maxper=0
    for p in ps:
        S=sols(p); tot+=len(S)
        from collections import Counter
        cnt=Counter(C for _,_,C in S)
        L=[C for C in cnt if (4*C)**3>=4*C*p+1]
        len_+=sum(cnt[C] for C in L)
        maxper=max([maxper]+[cnt[C] for C in L])
    print(base, "primes",len(ps),"ordered sols",tot,"share in Lenstra regime (4C)^3>=N:",round(len_/tot,3),"max sols per such level",maxper)
