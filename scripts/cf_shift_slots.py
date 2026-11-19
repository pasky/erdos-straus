"""One principal sqrt(p) period + its initial row; no Jacobi prefilter."""
from math import gcd, isqrt
from signed_two_shifts import divisors_sq, factors, prime


def rows(p):
    m=isqrt(p); P,Q=0,1; seen=set()
    while (P,Q) not in seen:
        seen.add((P,Q)); a=(m+P)//Q
        yield P,Q,a
        P=a*Q-P
        T,r=divmod(p-P*P,Q)
        assert not r and T>0
        Q=T
    assert (P,Q)==(m,p-m*m)


def menu(p, extra=False):
    out=set()
    for P,Q,a in rows(p):
        for n in ((Q,a*Q,a) if extra else (Q,)):
            for u in (n,n-1,n+1,4*n-1):
                if u>0:
                    c=u//(u&-u)
                    if c%4==3 and gcd(p,c)==1:
                        out.add(c)
    return sorted(out)


def triple(p,c,direct):
    k,n=(p+c)//4,(p*c+1)//4
    H,s,f=(p*k,k,((p,1),)+factors(k)) if direct else (n,p*n,factors(n))
    assert gcd(c,H)==1
    for t in divisors_sq(f):
        if t<=H and (t+H)%c==0:
            x,y,z=s,(H+t)//c,(H+H*H//t)//c
            assert min(x,y,z)>0 and 4*x*y*z==p*(x*y+x*z+y*z)
            return x,y,z
    return None


def audit():
    tested=0
    for p in range(841,176402,840):
        if not prime(p):continue
        tested+=1
        if not any(triple(p,c,d) for c in menu(p) for d in (True,False)):
            assert p==176401 and tested==79
            break
    else: raise AssertionError('no failure')
    assert list(rows(p))==[(0,1,420),(420,1,840)] and menu(p)==[3]
    print('first miss:',p,'rank',tested,'expanded:',menu(p,True))
    for c in menu(p,True):
        assert not triple(p,c,True) and not triple(p,c,False)
    for p,i,r in ((7561,64,3),(12601,15,2)):
        R=list(rows(p)); P,Q,a=R[i]; prev=R[i-1][1]
        c=4*Q-1; k=(p+c)//4; b=k//r
        assert k==r*b and Q%r==0 and (16*r*r+4*P*P+prev)%c==0
        g=gcd(r,b); A,B,D=r//g,b//g,g*g; E,rem=divmod(A+B,c)
        assert not rem and pow(B,(p-1)//2,p)==p-1
        x,y,z=k,p*A*D*E,p*B*D*E
        assert 4*x*y*z==p*(x*y+x*z+y*z)
        print('CF full split:',p,i,P,Q,prev,'r and complement:',r,b,(x,y,z))
    for p in (12601,1317961):
        assert prime(p) and p%840==1
        m=isqrt(p); Q=p-m*m; c=4*Q-1
        assert Q==57 and (4*m*m+5)%c==(4*(p+1))%c
        print('same first Q:',p,m,c,triple(p,c,True),triple(p,c,False))
    assert not triple(12601,227,True) and not triple(12601,227,False)
    p=1317961;c=227;k=(p+c)//4;v,r=divmod((p+1)*k,c)
    assert not r and 4*k*v*(p*v)==p*(k*v+k*p*v+p*v*v)


if __name__=='__main__':audit()
