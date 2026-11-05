# Sanity checks: (L1) reformulation solution <=> exists a,b,d: rho=4abd-p>=1, rho | a+b  (brute force on 4abcd=a+b+pc)
# (L2) every solution has Legendre(ab/p) = -1 and f=4acd-1 = a/b (mod p)   (p prime = 1 mod 8)
# (L3) for odd squares n=m^2 no solution with ab <= B (sanity of the known obstruction)
from sympy import isprime, legendre_symbol as L
def sols(n, B):
    out=[]
    for a in range(1,B+1):
        for b in range(a,B//a+1):
            m=4*a*b; rho=(-n)%m
            if rho and (a+b)%rho==0:
                d=(n+rho)//m; c=(a+b)//rho
                assert 4*a*b*c*d==a+b+n*c
                out.append((a,b,c,d))
    return out
def brute(n,C):  # direct search 4abcd = a+b+nc, with a<=b, small c,d
    s=set()
    for c in range(1,C+1):
        for d in range(1,C+1):
            N=4*c*c*d*n+1; t=4*c*d
            f=t-1
            while f*f<=N:
                if N%f==0:
                    g=N//f
                    if g%t==t-1: a=(f+1)//t; b=(g+1)//t; s.add((min(a,b),max(a,b),c,d))
                f+=t
    return s
bad=0
for p in [p for p in range(1,20000) if p%24==1 and isprime(p)]:
    S=sols(p,3000)
    for (a,b,c,d) in S:
        if L(a*b%p,p)!=-1: bad+=1; print("L2 fail",p,a,b)
        f=4*a*c*d-1
        if (f*b-a)%p: bad+=1; print("f!=a/b",p,a,b)
    if p<3000:
        Bs=brute(p,6); Ss=set((a,b,c,d) for (a,b,c,d) in sols(p,p) if c<=6 and d<=6)
        if Bs!=Ss: bad+=1; print("L1 mismatch",p,len(Bs),len(Ss))
for m in range(3,150,2):
    if sols(m*m,2000): bad+=1; print("square has sol",m)
print("bad",bad)
