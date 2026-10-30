# For primes p ≡ 1 mod 4: count unordered solutions x<=y<=z of 4/p=1/x+1/y+1/z; report parity, diagonal (x=y or y=z) solutions.
from fractions import Fraction
def sols(n):
    out=[]
    for x in range(n//4+1, 3*n//4+2):
        r=Fraction(4,n)-Fraction(1,x)
        if r<=0: continue
        a,b=r.numerator,r.denominator   # a/b = 1/y+1/z, y>=x
        ylo=max(x, b//a+1)
        yhi=2*b//a
        for y in range(ylo, yhi+1):
            num=a*y-b
            if num<=0: continue
            if (b*y)%num==0:
                z=b*y//num
                if z>=y: out.append((x,y,z))
    return out
import sys
P=[p for p in range(5,int(sys.argv[1])) if all(p%q for q in range(2,int(p**.5)+1)) and p%4==1]
par={0:0,1:0}; diag=0
for p in P:
    s=sols(p); par[len(s)%2]+=1
    d=[t for t in s if t[0]==t[1] or t[1]==t[2]]
    diag+=len(d)
    if d: print('diag',p,d[:3])
print('primes',len(P),'parity counts',par,'diag sols',diag)
