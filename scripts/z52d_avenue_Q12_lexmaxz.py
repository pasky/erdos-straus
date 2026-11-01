# Z0939: for p ≡ 5 (8), max-z solution = (x0, (p x0+2)/3, p x0 y0/2), x0 = (p+3)/4 ?
from sympy import primerange
bad=0; n=0
for p in primerange(13,3000):
    if p%8!=5: continue
    best=None
    for x in range(p//4+1, 3*p//4+1):
        num=4*x-p; den=p*x
        for y in range(max(x,den//num+1), 2*den//num+1):
            zd=num*y-den
            if zd>0 and (den*y)%zd==0:
                z=den*y//zd
                if best is None or z>best[2]: best=(x,y,z)
    x0=(p+3)//4; y0=(p*x0+2)//3; z0=p*x0*y0//2
    n+=1
    if best!=(x0,y0,z0): bad+=1; print("mismatch",p,best,(x0,y0,z0))
print("checked",n,"mismatches",bad)
