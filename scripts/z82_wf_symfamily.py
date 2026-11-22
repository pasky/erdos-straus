"""Constant congruences preserving two independent sections mod 5, §4 test."""
from fractions import Fraction as F
from sympy import primerange,isprime
from z82_wf_fibres import image

def certify(p,s):
    b=(p+1)//2;g=p*b;z=(p+s)//4;x=z*(p+1)//s;T=tuple(map(F,(x,p*x,z)));W=tuple(map(F,(b,g,F(p,2))))
    w=(p+1)**2//s;K=sum(W[:2])+w*W[2];N=4*K/p;A=(N-w)**2-4*(N+w);B=16*w*N
    assert sum(1/v for v in T)==F(4,p) and sum(T[:2])+w*T[2]==K
    pairs=[image(R,-w,N) for R in (W,T)];O=4*w,4*w*(N-w)
    rem={(0,1)}|{(1,i) for i in range(5)};rows=[];nt=None
    for l in primerange(7,500):
        if p*s*(p+1)*(p+1+s)*(p+s)%l==0:continue
        def red(n):return n.numerator*pow(n.denominator,-1,l)%l
        try:a,e=red(A),red(B);o=tuple(map(red,O));P,Q=[tuple(map(red,u)) for u in pairs]
        except ValueError:continue
        if e*(a*a-4*e)%l==0:continue
        def add(P,Q):
            if P is None:return Q
            if Q is None:return P
            x,y=P;u,v=Q
            if x==u and (y+v)%l==0:return None
            h=((v-y)*pow(u-x,-1,l) if x!=u else (3*x*x+2*a*x+e)*pow(2*y,-1,l))%l
            r=(h*h-a-x-u)%l;return r,(h*(x-r)-y)%l
        def mul(n,P):
            R=None
            while n:
                if n&1:R=add(R,P)
                n//=2;P=add(P,P)
            return R
        n=1+l+sum(0 if not(f:=x*(x*x+a*x+e)%l) else (1 if pow(f,(l-1)//2,l)==1 else -1) for x in range(l))
        if n%5 and nt is None:nt=(l,n)
        if n%5==0:
            o=(o[0],-o[1]%l);U,V=[mul(n//5,add(R,o)) for R in (P,Q)]
            cut={c for c in rem if add(mul(c[0],U),mul(c[1],V)) is not None}
            if cut:rows.append((l,n,U,V));rem-=cut
        if not rem and nt:return nt,rows
for p in range(841,1000000,840):
    if (p+1)%11 or not isprime(p):continue
    if (res:=certify(p,11)):
        print('p0',p,'s',11,'no5 and rows',res);break
else:raise AssertionError
