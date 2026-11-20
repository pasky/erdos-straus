"""Independent standard-library proof checker for z77. No discovery-code imports."""
from pathlib import Path
from collections import Counter
from math import gcd,lcm
import json
from functools import cache
from z77_review_small_s import es

@cache
def explicit(n):
    x,y,z=es(n)
    assert min(x,y,z)>0 and 4*x*y*z==n*(x*y+y*z+z*x)
    return True

root=Path('data/z77/proth')

def ds(n):return [i for i in range(1,n+1) if n%i==0]

def residue_product(k,m,j,h):
    u=k-1;M=8*u
    x=next(x for x in range(0,M,16) if x%(u//2)==pow(2,j,u//2))
    # Evaluate at an integer with the required residue. Phi_{2d} has integral coefficients.
    F={};B={c%M for c in ds(k)}
    for d in ds(m):
        a=x**d+1
        for e,v in F.items():
            if d%e==0:a,rem=divmod(a,v);assert rem==0
        F[d]=a
        B |= {c*(a%M)%M for c in B}
    assert (7*u-1)%M in B,(k,m,j)

def verify(k,H0,H,h,p):
    assert all(p%i for i in range(2,p)) and h in [p,p*p] and pow(2,h,(k-1)//2)==1
    files=[f'{k}-{H0}-0.json']+([f'{k}-{H}-extra.json'] if k!=255 else []); rows=sum((json.loads((root/f).read_text())['rules'] for f in files),[])
    cover=bytearray(H); kinds=Counter();seen=set();oddQ=1;squares={i*i%840 for i in range(840) if gcd(i,840)==1}
    for P,j,R,*z in rows:
        assert H%P==0 and 0<=j<P;s=j+max(0,(32-j+P-1)//P)*P; kinds[R]+=1
        if R=='X':
            m,=z;assert m%2 and P%(4*m)==j%(4*m)==0
            v=j//m;w=P//m; js=range(1,h) if w%h or v%p==0 else [v%h]
            for a in js:
                if a%p and (m,a) not in seen:residue_product(k,m,a,h);seen.add((m,a))
        else:
            if R=='M':mod=840
            elif R=='D':mod=z[0]
            elif R=='W':mod=8*z[0]
            elif R=='II':mod=z[0]
            elif R=='K':mod=4*z[0]*z[1] if z[2][2] or z[3][2] else 4*lcm(z[0],z[1])
            else:raise ValueError(R)
            oddQ=lcm(oddQ,mod//(mod&-mod));assert (k*pow(2,s,mod)*(pow(2,P,mod)-1))%mod==0
            n=(k*pow(2,s,mod)+1)%mod
            if R=='M':assert n not in squares
            if R=='D':assert n==0 and 2<=mod<20000 and explicit(mod)
            if R=='W':
                A,u=z;t,rem=divmod(A+1,u);v,r=divmod(n+u,A)
                assert rem==r==0 and min(t,u)>=2 and (k*(1<<32)+1+u)>=2*A
                assert n%8==1 and ((n+t)*t*u*v)%8==0 and any(val%4==0 for val in [t,u,v,A,t*v-1])
            if R=='II':
                f,a,b=z;assert min(f,a,b)>0 and (f+1)%(4*a*b)==(b*n+a)%f==0 and k*(1<<32)+1>a*f
            if R=='K':
                f,K0,a,b=z;K,r=divmod(n+f,4);assert r==0 and K%K0==0 and f%4==3
                def D(args):
                    d,i,j=args;assert d>0 and K0%d==0 and i in [0,1] and j in [0,1];return d*n**i*(K//K0)**j
                assert (D(a)+D(b))%f==0
            if k==255:assert mod&-mod<=128
        cover[j::P]=b'\1'*(H//P)
    assert all(cover) and all(explicit(k*2**s+1) for s in range(32))
    print('k',k,'period',H,'rows',dict(kinds),'core checks',len(seen),'coverage',sum(cover))
    if k==255:print('odd lcm of fixed row moduli',oddQ)

if __name__=='__main__':
    verify(255,5040,5040,7,7);verify(1023,55440,55440,9,3);verify(4095,55440,720720,11,11)
