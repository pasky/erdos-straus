# (★) at power-of-2 levels C=2^j: does 4Cp+1 have a divisor d ≡ -1 (mod 4C)?
from sympy import primerange, divisors
fails=[];tot=0
for p in primerange(5,200000):
    if p%4!=1: continue
    tot+=1; ok=False; C=1
    while (4*C-1)**2 <= 4*C*p+1:
        m=4*C; N=m*p+1
        for d in divisors(N):
            if d%m==m-1: ok=True;break
        if ok: break
        C*=2
    if not ok: fails.append(p)
print(tot,len(fails),fails[:15])
