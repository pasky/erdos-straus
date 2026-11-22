"""Exact rank >=2 certificates for the second (positive-weight) plane u=1.
Only the standard library. Reductions each give a linear F_5 test; additionally
exclude 5-torsion at one good prime. No rank packages / numerical heights.
"""
from fractions import Fraction as F
from math import isqrt, lcm


def isp(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n)+1))


def image(xyz, k, N):
    x,y,z = xyz
    X = 4*k*((N+k)*z/(x+y)-1)
    return X,X*(N+k)*(x-y)/(x+y)


def cert(p):
    assert p%4==1 and isp(p)
    b=(p+1)//2; g=p*b; j=p+2
    k=next(t*j-1 for t in range(1,20000) if isp(t*j-1) and pow(t*j-1,(p-1)//2,p)==p-1)
    N1=4+k*(p*p-1); H=(k*p*p+4)*(k*p**4+16)
    assert all(isqrt(n)**2!=n for n in (N1,H)) and k>p
    Z=(k*g+1)//j; assert Z*j==k*g+1
    Q=(F(b),F(g*Z),F(Z,k)); W=(F(b),F(g),F(p,2))
    w=k*g*(p+1); K=b+g+w*W[2]; N=4*K/p
    for T,den in ((Q,k),(W,2)):
        assert sum(1/x for x in T)==F(4,p) and min(T)>0
        assert T[0]+T[1]+w*T[2]==K and lcm(*(x.denominator for x in T))==den
    P=(F(b),F(b-1),-F(p*b*(b-1)))
    assert P[0]+P[1]-k*P[2]==Q[0]+Q[1]-k*Q[2]
    assert (j*Q[1]-g)*(j*W[1]-g)==w*g*g
    # Symmetric weights (1,1,w), k2=-w in z81 I's birational model.
    A=(N-w)**2-4*(N+w); B=16*w*N; O0=(4*w,4*w*(N-w))
    points=[O0,image(Q,-w,N),image(W,-w,N)]
    for x,y in points: assert y*y==x*(x*x+A*x+B)
    notors=None;rows=[];remaining={(0,1)}|{(1,i) for i in range(5)}
    for l in range(7,1000):
        if not isp(l):continue
        def red(x):
            x=F(x); return x.numerator*pow(x.denominator,-1,l)%l
        try:a,e=red(A),red(B); pts=[tuple(map(red,P)) for P in points]
        except ValueError:continue
        if e*(a*a-4*e)%l==0:continue
        cnt=1+l+sum(0 if (f:=x*(x*x+a*x+e)%l)==0 else (1 if pow(f,(l-1)//2,l)==1 else -1) for x in range(l))
        def add(P,Q):
            if P is None:return Q
            if Q is None:return P
            x,y=P;s,t=Q
            if x==s and (y+t)%l==0:return None
            h=((t-y)*pow(s-x,-1,l) if x!=s else (3*x*x+2*a*x+e)*pow(2*y,-1,l))%l
            X=(h*h-a-x-s)%l;return X,(h*(x-X)-y)%l
        def mul(n,P):
            R=None
            while n:
                if n%2:R=add(R,P)
                P=add(P,P);n//=2
            return R
        if cnt%5 and notors is None:notors=(l,cnt)
        if cnt%5==0 and remaining:
            neg=(pts[0][0],-pts[0][1]%l); L,M=(mul(cnt//5,add(R,neg)) for R in pts[1:])
            cut={z for z in remaining if add(mul(z[0],L),mul(z[1],M)) is not None}
            if cut:rows.append((l,cnt,L,M));remaining-=cut
        if notors and not remaining:break
    assert notors and not remaining
    print('p',p,'k',k,'u 1 w',w,'W',*W,'no5',notors,'rows',rows,flush=True)

if __name__=='__main__':
    for p in (409,577,2521,3361,102001,8813281):cert(p)
