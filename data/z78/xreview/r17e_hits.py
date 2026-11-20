"""Opus xreview of R17_ENDPOINT: exhaustive x=5 P/Q hit enumeration at chosen (r,level),
then nonvacuous checks of (2.1)-(2.3), the P/Q identities, and the Subspace-contact sizes.
P: enumerate (a,H) with aH <= C*B/2 (H<=2CB/M, M>=4a), b=(UH-pa)/q, unique d.
Q: enumerate a, m=4d == -q/(p a^2) mod F, F<mac<=2F+2."""
import sys, math
from math import gcd, isqrt
from fractions import Fraction as Fr
import numpy as np

def sqfree_kernel(n):
    k=1; x=n; f=2
    while f*f<=x:
        while x%(f*f)==0: x//=f*f
        if x%f==0: k*=f; x//=f
        f+=1
    return k*x

def isprime(n):
    if n<2: return False
    for f in range(2,isqrt(n)+1):
        if n%f==0: return False
    return True

stats={}
def bump(k,v=1): stats[k]=stats.get(k,0)+v
worst={}
def wmax(k,v,info):
    if k not in worst or v>worst[k][0]: worst[k]=(v,info)
def wmin(k,v,info):
    if k not in worst or v<worst[k][0]: worst[k]=(v,info)

def P_hits(r,L,p,q):
    U=r**L; N=U*U//r; B=U//r; C=p+q
    X=C*B//2+1
    out=[]
    s=isqrt(X)
    def handle(aa,HH):
        num=U*HH-p*aa
        ok=(num%q==0)
        aa=aa[ok]; HH=HH[ok]; b=num[ok]//q
        ok=b>=aa; aa=aa[ok]; HH=HH[ok]; b=b[ok]
        if aa.size==0: return
        fab=4*aa*b
        d=N//fab+1; e=fab*d-N
        ok=(e<=aa+b)&((aa+b)%e==0)
        for a_,b_,d_,e_,H_ in zip(aa[ok],b[ok],d[ok],e[ok],HH[ok]):
            a_,b_,d_,e_=int(a_),int(b_),int(d_),int(e_)
            c_=(a_+b_)//e_
            if (a_*b_*c_*d_*e_)%r==0: bump('P skipped r|abcde'); continue
            out.append((a_,b_,c_,d_,e_))
    CH=4000000
    for a in range(1,s+1):
        for h0 in range(1,X//a+1,CH):
            HH=np.arange(h0,min(X//a,h0+CH-1)+1,dtype=np.int64); handle(np.full(HH.shape,a,dtype=np.int64),HH)
    for H in range(1,s+1):
        lo=s+1; hi=X//H
        if hi<lo: continue
        for a0 in range(lo,hi+1,CH):
            aa=np.arange(a0,min(hi,a0+CH-1)+1,dtype=np.int64); handle(aa,np.full(aa.shape,H,dtype=np.int64))
    return sorted(set(out))

def check_P(r,L,p,q,a,b,c,d,e):
    U=r**L; N=U*U//r; B=U//r; m=4*d; M=m*a; C=p+q; D=q-p; u=p*q; A=M*a
    assert M*b==N+e and a+b==c*e and (p*a+q*b)%U==0
    H=(p*a+q*b)//U; J,rj=divmod(p*M*a+q*e,U); S,rs=divmod(p*M*c+D,U)
    assert rj==rs==0 and min(H,J,S)>0
    Y,ry=divmod(U*S*J+D*q*B,M); assert ry==0
    assert Y==p*a*S+q*H and e*Y==U*H*J-D*p*B*a and U*S*H-Y==u*B*c and p*c*J==Y-D*H
    Z,rz=divmod(Y,B); assert rz==0 and M*Z==r*S*J+D*q
    I=m*H*Z-u*S
    assert p*M*Z+r*q*m*H*H==D*u+U*I and I>=1
    assert e*Z==r*H*J-D*p*a
    # (2.1)
    assert M*b<=2*N and M*H<=2*C*B and 5*p*A>=2*U and M>=4*C*q
    assert e<=2*p*(2*C+abs(D))*a and e*A<=4*C*C*N+D*D*A and (D*D+r*m*H*H)%e==0
    C1=p*p*(2*C+abs(D)); C2=Fr(4*q*C*C,r); C3=2*u*C+abs(D)*u
    assert I<=Fr(C1*A,U*e)+C2*U/A+Fr(C3,U)
    case1=A<=4*C2*U; case2=e*U<=2*C1*A
    assert case1 or case2
    if case1: bump('P case A<=4C2U'); assert e*e<=4*p*p*(2*C+abs(D))**2*C2*U
    if case2 and not case1:
        bump('P case e<=2C1A/U only')
        assert e<2*D*D or e*e<=16*C1*C*C*B
    assert e*e<=1100**2*U
    bump('P x=5 hits U>=1e6 full chain')
    wmax('P e/sqrt(U)',e/math.sqrt(U),(r,L,p,q,a,b,c,d,e))
    wmax('P I',I,(r,L,p,q,a,b,c,d,e))
    wmin('P pA/U',p*A/U,(r,L,p,q,a,b,c,d,e))
    # Subspace contact of Thm P: (ht)^2 == -(u e0/d0) l^2 mod N
    t=p*a-q*b; assert t!=0 and m*t*t+4*u*e==N*(r*m*H*H-4*u)
    d0=sqfree_kernel(d); h=isqrt(d//d0); e0=sqfree_kernel(e); l=isqrt(e//e0)
    assert d0*h*h==d and e0*l*l==e and gcd(d,e)==1
    assert ((h*t)**2*d0+u*e0*l*l)%N==0
    expo=math.log(abs(h*t)*l)/math.log(N)
    wmax('P log_N(|ht| l)',expo,(r,L,p,q,a,b,c,d,e,'kernel de',d0*e0))
    wmin('P log_N(|ht| l)',expo,(r,L,p,q,a,b,c,d,e,'kernel de',d0*e0))
    return d0*e0

def Q_hits(F,r,p,q):
    out=[]
    for a in range(1,(2*F+2)//4+1):
        if a%r==0: continue
        m0=(-q*pow(p*a*a,-1,F))%F
        # m == m0 mod F, m == 0 mod 4
        m=m0
        while m%4: m+=F
        if m==0: m=4*F
        while m*a<=2*F+2:
            for c in range(F//(m*a)+1,(2*F+2)//(m*a)+1):
                f=m*a*c-F
                if f<=0 or (F*a+c)%f or (m*a*a+1)%f: continue
                b=(F*a+c)//f; e=(m*a*a+1)//f
                if b<a or a+b!=c*e: continue
                d=m//4
                if (a*b*c*d*e)%r: out.append((a,b,c,d,e))
                else: bump('Q skipped r|abcde')
            m+=4*F
    return out

def check_Q(F,r,p,q,a,b,c,d,e):
    m=4*d; M=m*a; C=p+q; D=q-p; u=p*q
    assert M*b==e*F+1 and a+b==c*e
    if (p*a+q*b)%F: return None
    H=(p*a+q*b)//F; J,rj=divmod(p*M*a+q,F); S,rs=divmod(p*M*c*e+D,F); assert rj==rs==0
    Y,ry=divmod(F*S*J+D*q*e,M); assert ry==0
    assert Y==p*a*S+q*H and Y==F*H*J-D*p*e*a and F*S*H-Y==u*e*c*e and p*c*e*J==Y-D*H
    assert p*M*Y+F*q*m*H*H==D*u*e+F*(m*H*Y-u*e*S)
    f=M*c-F; fs=m*b*c-F
    assert e*f==m*a*a+1 and b*f==F*a+c and f*fs==F*F+m*c*c and 0<f<=F+2
    assert F<=p*m*a*a+q and m*(F-q)*F*F<=p*C*C*(e*F+1)**2
    assert (p*f*f+q*m*c*c)%F==0 and ((p*f-q*fs)**2+4*u*m*c*c)%(F*F)==0
    d0=sqfree_kernel(d); h=isqrt(d//d0); x=2*h*a; y=2*h*c
    assert d0*x*y==m*a*c<=2*F+2 and (p*d0*x*x+q)%F==0 and (p*f*f+q*d0*y*y)%F==0
    X3=p*f-q*fs; assert X3!=0 and (X3*X3+4*u*d0*y*y)%(F*F)==0
    lf=math.log(F)
    s1=math.log(x)/lf; s2=math.log(f*y)/lf; s3=math.log(abs(X3)*y)/(2*lf)
    bump('Q x=5 hits'); wmin('Q step1 log_F x',s1,(F,p,q,a,b,c,d,e,'d0',d0))
    wmin('Q step2 log_F(fy)',s2,(F,p,q,a,b,c,d,e,'d0',d0)); wmin('Q step3 log_F^2(|X|y)',s3,(F,p,q,a,b,c,d,e,'d0',d0))
    wmax('Q e/sqrt(dF) inverse: sqrt(dF)/e',math.sqrt(d*F)/e,(F,p,q,a,b,c,d,e))
    return d0

if __name__=='__main__':
    mode=sys.argv[1]
    kern={}
    if mode=='P':
        jobs=[]
        # depth L=2 at all primes 1009..4000; L=3 at primes 101..300; r=17 at L=5,6
        jobs+=[(r,2) for r in range(1009,4001) if isprime(r)]
        jobs+=[(r,3) for r in range(101,301) if isprime(r)]
        jobs+=[(17,5),(17,6)]
        for r,L in jobs:
            for p,q in [(1,5),(5,1)]:
                hs=P_hits(r,L,p,q); bump('P jobs')
                for t in hs:
                    k=check_P(r,L,p,q,*t); kern[k]=kern.get(k,0)+1
                    if r==17: print('r=17 hit',L,p,q,t)
                bump(f'P hits L={L}',len(hs))
        print('P distinct de-kernels',len(kern),'max multiplicity',max(kern.values()) if kern else 0)
    else:
        for F in [r for r in range(100003,100400) if isprime(r)][:20]+[17**4,17**5,13**5]:
            r=[x for x in (13,17) if F%x==0]; r=r[0] if r else F
            for p,q in [(1,5),(5,1)]:
                for t in Q_hits(F,r,p,q):
                    k=check_Q(F,r,p,q,*t)
                    if k is not None: kern[k]=kern.get(k,0)+1
                    if k is not None and r==17: print('r=17 Q hit',F,p,q,t)
        print('Q distinct d-kernels',len(kern))
    print('stats',stats)
    for k,v in sorted(worst.items()): print(k,v)
