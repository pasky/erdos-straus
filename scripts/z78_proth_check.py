"""Standalone certificate reader. No PARI or search-code imports. -B, assertions enabled."""
import json,sys,math
from pathlib import Path
from collections import Counter
from functools import cache
R=Path('data/z78/proth')
@cache
def direct(n):
    # Reduce residual to b/d; (by−d)(bz−d)=d². Trial small divisors, including d itself.
    for x in range(n//4+1,n//4+501):
        b=4*x-n;d=n*x;g=math.gcd(b,d);b//=g;d//=g
        for l in range(1,1201):
            if d*d%l:continue
            for L in (l,d*l if d%l==0 else l):
                if (L+d)%b==0:
                    y=(L+d)//b;z=(d*d//L+d)//b
                    assert min(x,y,z)>0 and 4*x*y*z==n*(x*y+y*z+z*x);return (x,y,z)
    raise ValueError(n)

def small():
    S=json.loads((R/'small.json').read_text());assert len(S)==30
    for m,row in enumerate(S,1):
        assert len(row)==64
        for s,(x,y,z) in enumerate(row):
            n=(4**m-1)*2**s+1;assert min(x,y,z)>0 and 4*x*y*z==n*(x*y+y*z+z*x)
    print('direct triples: 30*64')

@cache
def divs(n):return [i for i in range(1,n+1) if n%i==0]
@cache
def mob(n):return 1 if n==1 else -sum(mob(i) for i in divs(n)[:-1])

def check(f):
    data=json.loads(f.read_text());m=data['m'];H=data['period'];k=4**m-1;cover=bytearray(H);cnt=Counter();S={a*a%840 for a in range(1,840) if math.gcd(a,840)==1}
    for P,j,T,*z in data['rows']:
        assert 0<=j<P and H%P==0;cnt[T]+=1;s=j+(max(0,64-j)+P-1)//P*P
        if T=='X':
            e,W=z;h=2*m-1;u=k-1;assert e>0 and e%2 and P%(4*e)==j%(4*e)==0
            assert set(map(int,W))=={i for i in range(h) if math.gcd(i,h)==1}
            for a,(c,ds) in W.items():
                M=8*u;X=pow(2,int(a)+4*h,M);A=c;assert c>0 and not k%c and len(ds)==len(set(ds))
                for d in ds:
                    assert d>0 and e%d==0
                    for b in divs(d):A=A*pow(1+pow(X,b,M),mob(d//b),M)%M
                assert (A+1-7*u)%M==0
        else:
            if T=='M':M=840
            elif T=='D':M=z[0]
            elif T=='W':M=8*z[0]
            elif T=='II':M=z[0]
            elif T=='K':
                f0,K0,D,E=z;M=4*K0*f0 if D[2] or E[2] else 4*math.lcm(f0,K0)
            else:raise ValueError(T)
            n=(k*pow(2,s,M)+1)%M;assert k*pow(2,s,M)*(pow(2,P,M)-1)%M==0
            if T=='M':assert n not in S
            elif T=='D':assert M>=2 and n==0 and direct(M)
            elif T=='II':
                f0,a,b=z;assert min(z)>0 and (f0+1)%(4*a*b)==0 and (n*b+a)%f0==0
            elif T=='W':
                A,u=z;t,R1=divmod(A+1,u);v,R2=divmod(n+u,A)
                assert min(t,u)>=2 and R1==R2==0 and k*2**64+1+u>=2*A and (n+t)*t*u*v%8==0 and any(q%4==0 for q in (u,t,v,A,t*v-1))
            elif T=='K':
                assert min(f0,K0)>0 and f0%4==3 and (n+f0)%(4*K0)==0
                def term(term):
                    d,i,b=term;assert d>0 and K0%d==0 and i in (0,1) and b in (0,1);return d*n**i*((n+f0)//(4*K0))**b
                assert (term(D)+term(E))%f0==0
        cover[j::P]=b'\1'*(H//P)
    assert [i for i,b in enumerate(cover) if not b]==data['left'];print('m',m,'period',H,'miss',cover.count(0),dict(cnt))

def groups():
    for row in json.loads((R/'groups.json').read_text()):
        h=row['h'];M=2**h-1;k=2*M+1
        if 'c' not in row:assert h in (1,9);continue
        c=row['c'];assert k%c==0 and c%16==(14*M-1)%16
        B=lambda i:1+pow(2,i,M)
        A=c
        for i,e in row['powers'].items():
            assert math.gcd(int(i),h)==1 and e>=0;A=A*pow(B(int(i))*pow(3,-1,M),e,M)%M
        a=row['terminal'];assert (A*(B(a)*pow(3,-1,M) if a is not None else 1)+1)%M==0
        assert row['unit_j']==[i for i in range(h) if math.gcd(i,h)==1]
    print('group positive product certificates verified (no discrete logs)')
if __name__=='__main__':
    for a in sys.argv[1:]:
        if a=='small':small()
        elif a=='groups':groups()
        else:check(R/a)
