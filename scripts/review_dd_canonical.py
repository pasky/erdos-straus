"""R176 from scratch: DIFF_DEEP §2.5. (i) verify Ibukiyama's O(q,r) = <1,(1+j)/2,i(1+j)/2,(r+i)j/q> in (-p,-q)
is an order of reduced discriminant p (structure constants integral, det trd-form = p^2); (ii) count primes
p = 1 (24) for which O ∩ B^0 has x,y with <x,y>=1, f=nrd x <= f'=nrd y <= BF*p, h=(ff'-1)/p >= 1, 4h | gcd(h,G)^2."""
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt
from sympy import primerange, isprime, legendre_symbol, sqrt_mod, Matrix
def mul(u,v,A,B):
    a1,b1,c1,d1=u; a2,b2,c2,d2=v
    return (a1*a2+A*b1*b2+B*c1*c2-A*B*d1*d2, a1*b2+b1*a2-B*c1*d2+B*d1*c2,
            a1*c2+c1*a2+A*b1*d2-A*d1*b2, a1*d2+d1*a2+b1*c2-c1*b2)
def check_order(p,q,r):
    A,B=-p,-q; h=Fr(1,2)
    E=[(Fr(1),Fr(0),Fr(0),Fr(0)),(h,Fr(0),h,Fr(0)),(Fr(0),h,Fr(0),h),(Fr(0),Fr(0),Fr(r,q),Fr(1,q))]
    # coordinates w.r.t. E of (t,x,y,z): solve triangular-ish system by hand
    def coords(z):
        t,x,y,w=z; c3=x/h          # i-coefficient only from e3
        c4=(w-c3*h)*q              # k-coefficient: c3/2 + c4/q
        c2=(y-c4*Fr(r,q))/h        # j-coefficient: c2/2 + c4 r/q
        c1=t-c2*h
        return (c1,c2,c3,c4)
    for u in E:
        for v in E:
            if any(c.denominator!=1 for c in coords(mul(u,v,A,B))): return False
    conj=lambda x:(x[0],-x[1],-x[2],-x[3])
    G=[[2*mul(E[a],conj(E[b]),A,B)[0] for b in range(4)] for a in range(4)]
    def det(M):
        if len(M)==1: return M[0][0]
        return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))
    return abs(det(G))==p*p
import numpy as np
def vecs(p,q,r,Bd):  # integer coords X1=2x1, X2=q x2, X3=2q x3; 4q nrd = pq X1^2 + 4 X2^2 + p X3^2
    out=[]; vm=2*isqrt(Bd//p)+1
    for v in range(-vm,vm+1):
        for w in range(-(q*vm),q*vm+1):
            X3=q*v+2*w
            if p*q*v*v+p*X3*X3>4*q*Bd: continue
            S=isqrt(q*Bd)+1
            for u in range((-S-w*r)//q-1,(S-w*r)//q+2):
                X2=q*u+w*r; n4=p*q*v*v+4*X2*X2+p*X3*X3
                if 0<n4<=4*q*Bd and n4%(4*q)==0: out.append((v,X2,X3,n4//(4*q)))
                elif 0<n4<=4*q*Bd: raise SystemExit("non-integral norm")
    return out
P0,P1,BF=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
hit=tot=0; badorder=0
for p in primerange(P0,P1):
    if p%24!=1: continue
    q=3
    while not (isprime(q) and q%8==3 and legendre_symbol(p%q,q)==-1): q+=1
    r=sqrt_mod(-p,q)
    if not check_order(p,q,r): badorder+=1
    V=vecs(p,q,r,BF*p); found=False
    Va=np.array([[v[0],v[1],v[2]] for v in V],dtype=np.int64); Nn=np.array([v[3] for v in V],dtype=np.int64)
    for X in V:
        f=X[3]
        ip=p*q*X[0]*Va[:,0]+4*X[1]*Va[:,1]+p*X[2]*Va[:,2]   # = 4q <x,y>
        for idx in np.nonzero((ip==4*q)&(Nn>=f))[0]:
            g=int(Nn[idx])
            if (f*g-1)%p: raise SystemExit("p does not divide det: %d"%p)
            hh=(f*g-1)//p; G=gcd(f+1,g+1); gg=gcd(hh,G)
            if hh>=1 and (gg*gg)%(4*hh)==0: found=True; break
        if found: break
    tot+=1; hit+=found
print(f"p=1(24) in [{P0},{P1}): canonical curve carries a Type II pair (f'<={BF}p) for {hit}/{tot}; orders failing check: {badorder}")
