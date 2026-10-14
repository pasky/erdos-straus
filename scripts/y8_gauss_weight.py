# y8: exact weighting of words by representation numbers of T_w = [[A*,1],[1,A]] by I_3 (sum of three squares).
# For each word of prime p: r(T), r*(T) (primitive: x×y primitive), chi; checks
#   r*(T_w,I3)/|SO(T_w)| == chi_plus * C(tp)  with C(D) = r3*(D)/(#proper classes in Gauss's three-squares genus)
# computed directly as the number of primitive z, |z|^2 = D, with z^perp properly equivalent to T_w.
import sys, math
from math import gcd, isqrt
from sympy import isprime, legendre_symbol as L
def vecs(n):
    out=[]; r=isqrt(n)
    for a in range(-r,r+1):
        m=n-a*a; s=isqrt(m)
        for b in range(-s,s+1):
            c2=m-b*b; c=isqrt(c2)
            if c*c==c2: out.extend({(a,b,c),(a,b,-c)})
    return out
def cross(x,y): return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])
def words(p):
    for t in range(1,p+3):
        umax = p+2 if t==1 else (p+1)//(t-1)
        for u in range(1,umax+1):
            A=t*u-1
            if A>0 and (p+u)%A==0: yield t,u,(p+u)//A
def reps(As,A):
    VX=vecs(As); VY=vecs(A); r=rs=0; zs=set()
    for x in VX:
        for y in VY:
            if x[0]*y[0]+x[1]*y[1]+x[2]*y[2]==1:
                r+=1; z=cross(x,y)
                if gcd(gcd(*z[:2]),z[2])==1: rs+=1; zs.add(z)
    return r,rs,len(zs)
P=int(sys.argv[1]); bad=0; tot=0
for p in range(5,P+1,4):
    if not isprime(p): continue
    Np=0; S=0; Sp=0
    for t,u,v in words(p):
        A=t*u-1; As=t*v-1; chi=L(A%p,p)
        r,rs,nz=reps(As,A); tot+=1
        if (r>0)!=(chi==1): bad+=1; print("MISMATCH",p,t,u,v,chi,r)
        Np+=chi==1; S+=r; Sp+=nz
    print(p,"N+",Np,"sum r/48 = %.2f"%(S/48),"sum #z (primitive normals) =",Sp)
print("words",tot,"mismatches",bad)
if len(sys.argv)>2:
    from sympy import primefactors
    p=int(sys.argv[2]); from collections import Counter; C=Counter()
    for t,u,v in words(p):
        A=t*u-1; As=t*v-1; chi=L(A%p,p)
        if chi==1:
            r,rs,nz=reps(As,A); D=t*p; om=len(primefactors(D)); C[(D%8, om, r)]+=1
    for k in sorted(C): print("D mod 8, omega(D), r(T_w):",k,"x",C[k])
