# From-scratch checks for POINTWISE_MN Cor 6.1 (OMEGA12 substitution m -> general), review R63.
from math import gcd
from sympy import divisors, factorint
def sqfree_split(D):
    d=1;a=1
    for p,e in factorint(D).items():
        a*=p**(e//2)
        if e%2: d*=p
    return d,a
bad=dict(cls1=0,param=0,inj=0,invol=0); natoms=0
for m in range(4,31):
    seen=set()
    for A in range(1,3000//m+1):
        M=m*A-1
        if M<3: continue
        for D in divisors(A*A):
            natoms+=1
            if (m*D+1)%M==0: bad['cls1']+=1            # class of one is an event class?
            g=gcd(M,m*D+1)
            Dp=A*A//D
            if gcd(M,m*Dp+1)!=g: bad['invol']+=1
            if D>A: continue
            d,a=sqfree_split(D)
            if A%(d*a): bad['param']+=1; continue
            b=A//(d*a)
            if b<a or (a+b)%g: bad['param']+=1; continue
            P=m*a*a*d+1; e=g; f=P//e; c=(a+b)//e; N=M//e
            if P%e or M%e or m*a*c*d!=f+N or N<a*c*d or N*e!=M: bad['param']+=1
            key=(a,c,d,f)
            if key in seen: bad['inj']+=1
            seen.add(key)
print("atoms",natoms,"defects",bad)
# root counts of m d x^2+1 mod 2^k and odd prime powers
mx2=0; mxodd=0
for md in range(1,400):
    for k in range(1,12):
        r=sum(1 for x in range(2**k) if (md*x*x+1)%(2**k)==0); mx2=max(mx2,r)
    for p in [3,5,7,11,13]:
        for k in range(1,4):
            q=p**k; r=sum(1 for x in range(q) if (md*x*x+1)%q==0); mxodd=max(mxodd,r)
print("max roots mod 2^k:",mx2,"odd p^k:",mxodd)
M=464;D=3;m=5;A=(M+1)//m
print("M=464 ex: A",A,"D|A^2",A*A%D==0,"gcd(M,840)",gcd(M,840),"(5D+1)",5*D+1,"class mod 16",(-m*D)%16)
