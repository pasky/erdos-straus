# z53 NONCRTSMOOTH checks: Prop 3.2 (compact inverse-graph form) vs brute force; Thm A2 construction for p ≡ 1 (4) < 2*10^4.
from sympy import isprime, legendre_symbol as leg, primerange
def R(n):
    c=0
    for u in range(1,n+1):
        if 4*u-1>n+u: break
        for x in range(4*u-1,n+u+1,4*u):
            if (n+u)%x==0: c+=1
    return c
def Rcompact(p):
    m=4*p; c=0; mx=0
    for x in range(2,m):
        if x%2==0 or x%p==0: continue
        xb=pow(x,-1,m); D=(x*xb-1)//p
        if (x+1)%D==0:
            c+=1; mx=max(mx,x,xb); assert (xb+1)%D==0 and D%4==0
    return c,mx
for p in [p for p in primerange(5,3000) if p%4==1][:60]+[3361,2521,409]:
    r=R(p); rc,mx=Rcompact(p)
    assert r==rc,(p,r,rc)
    assert mx<=(4*p+1)//3
print("compact form OK")
# A2 construction
for p in [p for p in primerange(5,20000) if p%4==1]:
    l=next(l for l in primerange(3,10**6) if l%4==3 and leg(l,p)==-1)
    s=next(s for s in range(2,2*l+2,2) if (p*s*s+1)%l==0)
    num=p*s*s+1+l; assert num%(4*l)==0; C=num//(4*l)
    assert 4*1*l*C-1-l==s*s*p
    assert s<2*l
print("A2 OK")
