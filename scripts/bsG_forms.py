# Verify the elementary equivalent forms of (W) for 2 <= n < N against brute force:
#  (F1) exists x,z>=2: xz | n+x+z and (n+x+z)/(xz) >= 2
#  (F2) exists z>=2: q=ceil(n/z), r=qz-n, r>=2, r | q+1, (q+1)/r >= 2   [solutions x<z]  OR diagonal x=z: x|n, x | n/x+2, (n/x+2)/x>=2
#  (F3) exists d in [3,n]: rho=(-n mod d) in [2,(d+1)/2], rho | d+1, n+rho >= 2d
#  (F4) exists a in [1,n-1], gcd(a,n)=1, abar=a^-1 mod n, b=(a*abar-1)/n >= 2, b | a+1, b | abar+1, a,abar >= 2b-1
import sys
N=int(sys.argv[1]); W=[False]*N
for x in range(2,N):
    for y in range(2,N):
        if 2*x*y-x-2>=N: break
        for z in range(2,N):
            v=x*y*z-x-z
            if v>=N: break
            W[v]=True
bad=0
for n in range(2,N):
    f1=any((n+x+z)%(x*z)==0 and (n+x+z)//(x*z)>=2 for x in range(2,n+1) for z in range(2,(n+x)//x+2))
    f2=False
    for z in range(2,n+1):
        q=-(-n//z); r=q*z-n
        if r>=2 and (q+1)%r==0 and (q+1)//r>=2: f2=True; break
    f2=f2 or any(n%x==0 and (n//x+2)%x==0 and (n//x+2)//x>=2 for x in range(2,n+1))
    f3=any(2<=(-n)%d<=(d+1)//2 and (d+1)%((-n)%d)==0 and n+(-n)%d>=2*d for d in range(3,n+1))
    f4=False
    for a in range(1,n):
        try: ab=pow(a,-1,n)
        except ValueError: continue
        b=(a*ab-1)//n
        if b>=2 and (a+1)%b==0 and (ab+1)%b==0 and a>=2*b-1 and ab>=2*b-1: f4=True; break
    if not (W[n]==f1==f2==f3==f4): bad+=1; print("mismatch",n,W[n],f1,f2,f3,f4)
print("checked n<",N,"mismatches",bad)
