"""R265 from-scratch checks: R(p) brute force, odd-square T1 control, p=427249 least u."""
import math, sys
def divisors(n):
    s=[];i=1
    while i*i<=n:
        if n%i==0: s+= [i] if i*i==n else [i,n//i]
        i+=1
    return s
def R_brute(p):  # #{(u,B,C): 4uBC-u-B=p} by direct (u,B) loop: C=(p+u+B)/(4uB)
    c=0
    for u in range(1,p+1):
        for B in range(1,(p+u)//(4*u-1)+1 if 4*u-1>0 else 1):
            s=p+u+B
            if s%(4*u*B)==0: c+=1
    return c
if __name__=="__main__":
    for p in (409,577,5569):
        print("R_brute",p,R_brute(p))
    # least u for (a4) at 427249
    p=427249
    print("least u a4 at",p,next(u for u in range(1,700) if any(f%(4*u)==4*u-1 for f in divisors(p+u))))
    # T1: odd squares, (a4) any u<=m+2 ; (a) any u<=m+2 with A=-1 mod u and (A/n) Jacobi=-1? (a) needs prime p; we test (a4) only + class part
    bad=0;cnt=0
    for m in range(3,1001,2):
        n=m*m;cnt+=1
        for u in range(1,m+3):
            if any(f%(4*u)==4*u-1 for f in divisors(n+u)): bad+=1;print("hit",n,u);break
    print("odd squares tested",cnt,"a4 hits",bad)

def check_typeII_injection(P=2000):
    """(u,B,C) -> (uBC, pBC, puC) is an injective map into ES Type II solutions (R265 Claim 8)."""
    from fractions import Fraction as F
    n=0
    for p in range(5,P):
        if any(p%d==0 for d in range(2,int(p**.5)+1)): continue
        seen=set()
        for u in range(1,(p+1)//3+1):
            for f in range(4*u-1,p+u+1,4*u):
                if (p+u)%f: continue
                B=(p+u)//f; C=(f+1)//(4*u); t=(u*B*C,p*B*C,p*u*C)
                assert F(4,p)==F(1,t[0])+F(1,t[1])+F(1,t[2]) and t[0]%p and t not in seen
                seen.add(t); n+=1
    return n
