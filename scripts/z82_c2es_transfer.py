"""Replay the squarefree-denominator constructions, not analytic estimates."""
from fractions import Fraction as F
from math import gcd, prod
from z82_c2es_panel import check, prime


def transfer():
    at={}; count=0; fixed=0; mixed=None; multi=0
    for a in (1,3,5,7,11):
        for r in (3,5,7,11,13,15):
            for v in range(1,14,2):
                if gcd(a,r)*gcd(v,a*r)>1: continue
                q=4*a*r*v
                for w in range(1,101):
                    if gcd(w,r)>1:continue
                    f=q*w-1
                    for k in (1,3,5,7):
                        if k>=q or f%k:continue
                        l=f//k
                        if l<=11*15**2*13 or not prime(l): continue
                        n=-a*r*r*pow(v,-1,f)%f
                        while gcd(n,r)>1 or n<=1:n+=f
                        S=(n*v+a*r*r)//f
                        xyz=(a*r*w*S,n*a*r*v*w,F(n*v*w*S,r))
                        check(n,4,xyz)
                        assert xyz[2].denominator==r and xyz[0]%r==xyz[1]%r==0
                        key=(l,n%l)
                        assert key not in at
                        at[key]=a,r,v,k;count+=1;fixed+=r==3;multi+=k>1
                        if r==15 and k>1 and mixed is None:mixed=(n,a,r,v,k,l,w,xyz)
    assert mixed and fixed and multi
    print('half-level tags identity and no reduced-class collision; total, r=3, k>1',count,fixed,multi)
    print('composite r sample (n,a,r,v,k,l,w,triple)',mixed)


def extremum():
    g=lambda n:((n*n+34*n+49)*(n*n-34*n+1681));p=13441;k=287;c=13872;H=4*c*k
    assert prime(p) and p%840==1 and gcd(p,840*H*960*5568*68*1441)==1
    for n in (p, p+4*840*H,p+8*840*H):
        a=(n*n+k)//4; d=g(n)//H;b=c*d-a;z=(n*d+1)//4
        assert H*d==g(n) and c*k*d==n*c+4*a*a and d%4==3 and gcd(n*d,z)==1
        check(n,4,(d*a,d*b,F(z,d)))
        if n==p:
            support=[7,11,13,113,18119]
            assert all(prime(s) for s in support) and prod(support)==d
            print('split quartic (p,D,prime factors)',p,d,support)
    for p in (3361,2521,13441,21841,234361):
        assert p%840==1
        possibilities=[]
        for C in range(1,12):
            for T in range(1,12):
                for k in range(1,12):
                    if C*T*k>11 or (p*p+k)%(4*T):continue
                    a=(p*p+k)//(4*T)
                    num=p*T*C+4*T*a*a
                    if num%(k*C):continue
                    D=num//(k*C)
                    if (p*D+T)%4==0 and D%2==1:
                        possibilities.append((k,C,T))
        assert set(possibilities)<={(11,1,1)}
        print('TCk<=11',p,possibilities)

if __name__=='__main__': transfer();extremum()
