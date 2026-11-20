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
    data=json.loads(f.read_text()) if isinstance(f,Path) else f;m=data['m'];H=data['period'];k=4**m-1;cover=bytearray(H);cnt=Counter();S={a*a%840 for a in range(1,840) if math.gcd(a,840)==1}
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
                f0,a,b=z;assert min(z)>0 and (f0+1)%(4*a*b)==0 and (n*b+a)%f0==0 and k*2**64+1>a*f0
            elif T=='W':
                A,u=z;t,R1=divmod(A+1,u);v,R2=divmod(n+u,A)
                assert min(t,u)>=2 and R1==R2==0 and k*2**64+1+u>=2*A and (n+t)*t*u*v%8==0 and any(q%4==0 for q in (u,t,v,A,t*v-1))
            elif T=='K':
                assert min(f0,K0)>0 and f0%4==3 and (n+f0)%(4*K0)==0
                def term(term):
                    d,i,b=term;assert d>0 and K0%d==0 and i in (0,1) and b in (0,1);return d*n**i*((n+f0)//(4*K0))**b
                assert (term(D)+term(E))%f0==0
        cover[j::P]=b'\1'*(H//P)
    left=data['left'];assert left==sorted(set(left)) and len(left)==cover.count(0) and all(not cover[j] for j in left);print('m',m,'period',H,'miss',len(left),dict(cnt))

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
    for row in json.loads((R/'exact-core.json').read_text()):
        h=row['h'];Q=2**h-1;k=2*Q+1
        if h==1:assert all(c%16!=13 for c in (1,3));continue
        c=row['c'];T=row['T0'];assert c>0 and k%c==0 and c%16==(14*Q-1)%16 and len(T)==len(set(T));A=c
        for d in T:
            assert d in divs(h)
            for b in divs(d):A=A*pow(1+(1<<b),mob(d//b),Q)%Q
        for i,e in row['ratios'].items():
            a=int(i);g=math.gcd(a,h);assert 0<=a<h and e>=0;A=A*pow((1+(1<<a))*pow(1+(1<<g),-1,Q),e,Q)%Q
        assert A==Q-1
        assert row['unit_j']==[i for i in range(1,h) if math.gcd(i,h)==1]
    print('group positive product certificates verified (no discrete logs)')
if __name__=='__main__':
    for a in sys.argv[1:]:
        if a=='small':small()
        elif a=='groups':groups()
        elif a=='shift':
            S=json.loads((R/'shift.json').read_text());tot=0
            for ms,rows in S.items():
                k=4**int(ms)-1
                for a,b,c,P,j,v in rows:
                    u=k*2**a-1;assert 3<=a<=9 and 0<=b<=a and c>0 and not k%c and v==k*2**(a-b)//c and v>=2
                    assert 0<j<P and pow(2,P,u)==1 and (c*2**b*(1+pow(2,(j-a)%P,u))+1)%u==0
                    tot+=1
            print('shifted positive rows',tot)
        elif a=='census':
            C=json.loads((R/'census.json').read_text());assert [b['m'] for b in C]==list(range(1,31))
            for b in C:
                check(b);h=2*b['m']-1;Q=2**h-1;k=2*Q+1
                for js,(c,T) in b['witnesses'].items():
                    assert len(T)==len(set(T)) and c>0 and k%c==0 and c%16==(14*Q-1)%16;A=c
                    for d in T:
                        assert d>0 and b['mask_degree']%d==0
                        for i in divs(d):A=A*pow(1+pow(2,int(js)*i,Q),mob(d//i),Q)%Q
                    assert (1+A)%Q==0
        else:check(R/a)
