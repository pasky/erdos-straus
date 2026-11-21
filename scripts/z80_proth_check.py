"""Finite proof checks independent of discovery code; reuse the z78 arithmetic helpers. No factoring or search needed. Run with -B, not -O."""
import json
from pathlib import Path
from math import gcd,lcm,isqrt
from functools import cache
from z78_proth_check import small,direct
@cache
def divs(n):
    low=[i for i in range(1,isqrt(n)+1) if n%i==0]
    return low+[n//i for i in reversed(low) if i*i<n]
@cache
def mob(n):return 1 if n==1 else -sum(mob(i) for i in divs(n)[:-1])
root=Path('data/z80/proth')
def load(name):return json.loads((root/name).read_text())
S={a*a%840 for a in range(840) if gcd(a,840)==1}
def sq(n):return isqrt(n)**2==n
def good(n,t,u,v):
    assert n==t*u*v-u-v and min(t,u,v)>=2 and (n+t)*t*u*v%8==0 and not sq(n)
def triple(n,x,y,z):assert min(x,y,z)>0 and 4*x*y*z==n*(x*y+x*z+y*z)
def row(m,row):
    P,j,T,*z=row;k=4**m-1;assert 0<=j<P
    if T=='X':
        e,W=z;h=2*m-1;u=k-1;M=8*u;assert e>0 and e%2 and j==0 and P%(4*e)==0
        assert set(map(int,W))=={a for a in range(1,h) if gcd(a,h)==1}
        for a,(c,I) in W.items():
            x=pow(2,int(a)+h*4,M);assert c>0 and k%c==0 and len(I)==len(set(I));A=c
            for d in I:
                assert d>0 and e%d==0
                for b in divs(d):A=A*pow(1+pow(x,b,M),mob(d//b),M)%M
            assert (A+1-7*u)%M==0
        return
    if T=='M':M=840
    elif T in ('D','II'):M=z[0]
    elif T=='W':M=8*z[0]
    elif T=='K':
        f,K,D,E=z;M=4*f*K if D[2] or E[2] else 4*lcm(f,K)
    else:raise ValueError(T)
    s=j+max(0,(64-j+P-1)//P)*P;n=(k*pow(2,s,M)+1)%M
    assert (n-1)*(pow(2,P,M)-1)%M==0
    def test(n,full=False):
        if T=='M':assert n%840 not in S
        elif T=='D':
            assert M>=2 and n%M==0;x,y,v=direct(M)
            if full:triple(n,x*(n//M),y*(n//M),v*(n//M))
        elif T=='II':
            f,a,b=z;assert min(z)>0 and (f+1)%(4*a*b)==0 and (b*n+a)%f==0
            if full:
                d=(f+1)//(4*a*b);e=(n+4*a*a*d)//f;bp=(n+e)//(4*a*d);triple(n,a*bp*d,a*b*d*n,bp*b*d*n)
        elif T=='W':
            A,u=z;t,r=divmod(A+1,u);v,r2=divmod(n+u,A);assert min(t,u)>=2 and not(r or r2) and ((k<<64)+1+u)>=2*A and (n+t)*t*u*v%8==0 and any(c%4==0 for c in (t,u,v,A,t*v-1))
            if full:good(n,t,u,v)
        elif T=='K':
            f,K,D,E=z;assert min(f,K)>0 and f%4==3 and (n+f)%(4*K)==0
            def val(V):
                d,i,b=V;assert d>0 and K%d==0 and i in (0,1) and b in (0,1);return d*n**i*((n+f)//(4*K))**b
            A,B=val(D),val(E);assert (A+B)%f==0
            if full:
                y=(n+f)//4;triple(n,y,n*y//A*((A+B)//f),n*y//B*((A+B)//f))
    test(n)
    for s in range(64,513):
        if s%P==j:test((k<<s)+1,True)

def coverage(rows,H):
    # CRT residue tree: recurse solely on children not already contained in a row.
    # Fast path: sieve at the small base period, recurse at its surviving leaves.
    B=gcd(55440,H);left=bytearray(b'\1')*B;rest=[]
    for P,j,*_ in rows:
        assert H%P==0
        if B%P:rest.append((P,j))
        else:left[j::P]=bytes(B//P)
    @cache
    def prime(n):return next((i for i in range(2,isqrt(n)+1) if n%i==0),n)
    def split(a,b,R):
        U=[(P,j) for P,j in R if (j-a)%gcd(P,b)==0];assert U,(a,b)
        if any(b%P==0 for P,j in U):return
        p=min(prime(P//gcd(P,b)) for P,j in U);assert H%(b*p)==0
        for t in range(p):split(a+b*t,b*p,U)
    for a in range(B):
        if left[a]:split(a,B,rest)

def check(m):
    c=load(f'cover-{m}.json');assert c['m']==m and not c['left']
    for r in c['rows']:row(m,r)
    coverage(c['rows'],c['period']);print('all s:',m,c['period'],len(c['rows']),flush=True)

def primary():
    rows=load('primary.json');assert [r['h'] for r in rows]==list(range(263,400,2))
    for r in rows:
        h=r['h'];H=2**h-1;c=r['c'];S=r['T0'];assert (2*H+1)%c==0 and c%16==1 and S in ([],[1],[1,3]) and (3 not in S or h%3==0)
        v=c*3**len(S)
        for key,e in r['ratios'].items():
            a=int(key);assert 0<a<h and gcd(a,h)==1 and e>=0;v=v*pow((1+2**a)*pow(3,-1,H),e,H)%H
        assert (v+1)%H==0

def tower():
    data=load('tower-7.json');h=2187;d=729;M=2**d-1;H=2**h-1;assert (data['d'],data['j'],data['m'])==(729,7,1094)
    B=lambda a:1+pow(2,a,H);W=lambda a:B(a)*B(a+d)*B(a+2*d)*pow(B(3*a),-1,H)%H
    A=1
    for s,e in data['powers'].items():
        a=int(s);assert 0<a<d and gcd(a,3)==1 and e>=0;A=A*pow(W(a)*pow(W(1),-1,H),e,H)%H
    V=B(1)**2*pow(B(1+d)*B(1+2*d),-1,H)%H;assert A%M==729 and A*pow(V,6,H)%H==729

def layers():
    for p in range(3,201,2):
        if any(p%i==0 for i in range(2,isqrt(p)+1)):continue
        d=p
        while p*d<=200:
            h=p*d;M=2**d-1;H=2**h-1;N=H//M;assert gcd(M,N)==1
            def B(a):return 1+pow(2,a,H)
            def W(a):
                v=pow(B(p*a),-1,H)
                for t in range(p):v=v*B(a+d*t)%H
                return v
            for a in range(1,d):
                b=gcd(a,d);assert gcd(a,h)==gcd(b,h)
                L=W(a)*pow(W(b),-1,H)%H;r=B(a)*pow(B(b),-1,H)%H;rp=B(p*a)*pow(B(p*b),-1,H)%H
                assert L%N==1 and L*rp%M==pow(r,p,M)
            d*=p

def residual():
    c=load('cover-11.json');P0=3825360
    assert c['m']==11 and c['period']==P0 and c['left']==[0]
    T=int(json.loads(Path('data/z79/proth/intersection.json').read_text())['T'])
    for r in c['rows']:
        P,j,t,*z=r;assert t!='X' and j!=0
        row(11,r)
        if t=='K':
            f,K,A,B=z;M=4*f*K if A[2] or B[2] else 4*lcm(f,K)
        elif t=='W':M=8*z[0]
        elif t=='M':M=840
        else:M=z[0]
        assert M&-M<=2**64
        odd=M//(M&-M);assert pow(4,T,odd)==1%odd
    coverage(c['rows']+[[P0,0]],P0)

def transfer():
    for j in range(32):
        u=16*j+14;k=u+1
        for i in range(32):
            t=8*i+7;z=t*u-1;n=k*(z*z-1)+1;v=k*z;good(n,t,u,v);D=(t*v-1)//4;triple(n,z*D*n,u*D,z*u*D)
    for m in range(1,201):
        k=4**m-1;n=(k<<(2*m+2))+1;assert n==(2**(2*m+1)-1)**2
    for n in (105,1465,3865,4545,10305,12145,39361,67425,131,241,409,193,2521,66529):triple(n,*direct(n))
if __name__=='__main__':
    small();layers();tower();primary();transfer();residual()
    for m in range(13,31):check(m)
