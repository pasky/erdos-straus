"""Round 2 arithmetic replay, standalone of discovery. Run with -B and assertions."""
from math import gcd,prod,isqrt
from pathlib import Path
import json
from z80_proth_check import row,coverage,good,triple
D=Path('data/z80/proth/r2')
def read(p):return json.loads(p.read_text())
def order(x,n):
    y=x%n;e=1
    while y!=1:y=y*x%n;e+=1
    return e

def orbit(h):
    H=2**h-1; units=[a for a in range(1,h) if gcd(a,h)==1];o=order(2,h);coords={};O=[]
    for a in units:
        if a in coords:continue
        cyc=[a*pow(2,j,h)%h for j in range(o)];coords.update({b:(len(O),j) for j,b in enumerate(cyc)});O.append(cyc)
    for a in units:
        t,j=coords[a];rep=O[t][0];v=2**rep-1
        for i in range(j):v=v*(1+2**O[t][i])%H
        assert v==(2**a-1)%H
    # In the formal quotient by (sigma-1)I, differences within the orbit
    # have phase difference mod o; verify lifts for a basis of its kernel.
    def solve(v):
        y=[0]*h
        for C in O:
            assert sum(v[a] for a in C)==0
            for a,b in zip(C,C[1:]):y[b]=y[a]-v[b]
        t=sum(y);assert t%o==0
        for a in O[0]:y[a]-=t//o
        assert sum(y)==0 and all(v[a]==y[a*pow(2,-1,h)%h]-y[a] for a in units)
    for a in units:
        c=O[0][0];v=[0]*h
        for b,sign in ((2*a%h,1),(a,-1),(2*c%h,-1),(c,1)):v[b]+=sign
        solve(v)
    if h%3 and len(O)==1:assert (1+2**3)*pow(3,-1,H)%H==3%H

def primitive(h):
    p=next((p for p in range(3,h+1,2) if h%p==0),h);d=h
    while d%p==0:d//=p
    if d!=1:return
    N=(2**h-1)//(2**(h//p)-1);S={a for a in range(1,h) if a%p};Q={pow(2,i,h) for i in range(order(2,h))}
    for a in range(1,h):
        t=gcd(a,h);v=prod(1+pow(2,a//t+k*(h//t),N) for k in range(t));assert v%N==(1+pow(2,a,N))%N
    if len(S)==2*len(Q) and h-1 not in Q:
        assert prod(2**a-1 for a in S)%N==p%N
        norm=prod(2**a-1 for a in Q)%N
        assert norm**2*pow(2,-sum(Q),N)%N==(-p)%N

def old(h):
    F=read(D.parent/'indices.json')[(h-3)//2]['factors'];H=2**h-1
    for d in range(3,h+1,2):
        if h%d:continue
        M=2**d-1;A=prod(q**e for q,e,_ in F if M%q==0);K=A//M
        assert pow(2,d*K,A)==1 and all(pow(2,d*(K//q),A)!=1 for q,e,_ in F if K%q==0)
        for a in range(1,d):
            g=gcd(a,d);assert any(gcd(b,h)==g for b in range(a,h,d))
        assert 3*pow(1+pow(2,h-1,H),-1,H)%H==2

def extensions(h):
    for p in range(3,h,2):
        if h%p or any(p%i==0 for i in range(2,isqrt(p)+1)):continue
        d=h//p;M=2**d-1;H=2**h-1;N=H//M
        if gcd(p,d)>1 or M%p==0:continue
        f=order(p,d);B=lambda a:1+pow(2,a,H)
        def W(a):return prod(B(a+t*d) for t in range(p))*pow(B(p*a),-1,H)%H
        for a in range(1,d):
            b=gcd(a,d);u=a;v=b;s=1
            for _ in range(f):
                assert sorted(gcd(u+t*d,h) for t in range(p))==sorted(gcd(v+t*d,h) for t in range(p))
                s=pow(s,p,H)*W(u)*pow(W(v),-1,H)%H;u=p*u%d;v=p*v%d
            assert s%N==1 and s%M==pow(B(a)*pow(B(b),-1,M),p**f-1,M)

def residual():
    c=read(D/'cover-11.json');r=read(D/'transfer.json');T=int(r['T']);O=int(r['O']);M=T//(T&-T);z=21-2**14;P0=c['period'];assert P0==497943285840 and c['m']==11 and c['left']==[0]
    assert T==3*int(read(Path('data/z79/proth/intersection.json'))['T']) and T%36==0 and O>0 and O%4==0 and pow(2,O,M)==1 and r['b']==14 and gcd(z,M)==gcd(z-1,gcd(M,O))==1
    for R in c['rows']:
        P,j,t,*a=R;assert t!='X' and j!=0;row(11,R)
        if t=='W':Q=8*a[0]
        elif t=='M':Q=840
        elif t=='K':
            f,k,A,B=a;from math import lcm
            Q=4*k*f if A[2] or B[2] else 4*lcm(f,k)
        else:Q=a[0]
        assert Q&-Q<=2**64 and pow(4,T,Q//(Q&-Q))==1%(Q//(Q&-Q))
    coverage(c['rows']+[[P0,0]],P0)

def moving():
    for m in range(1,101):
        k=4**m-1
        for s in range(1,501):
            g=gcd(s-1,2*m+1)
            if g>1:
                q=2**g-1;n=(k<<s)+1;assert n%q==0
                # 4/q = 1/a + 2/(2aq), with a=(q+1)/4.
                a=(q+1)//4;c=n//q;triple(n,c*a,2*a*n,2*a*n)

def poly():
    for k in range(3,65,2):
        u=k-1
        for t in range(7,129,8):
            z=t*u-1
            for e in range(2,13,2):
                n=k*(z**e-1)+1;v=k*z**(e-1);good(n,t,u,v);U=(t*v-1)//4;triple(n,z*U*n,u*U,z*u*U)
    # Check actual words for every prime-row hit; including polynomials with
    # odd-degree shifted factor and ones deliberately failing that hypothesis.
    qs=[q for q in range(97,8192,112) if all(q%i for i in range(2,isqrt(q)+1))];tot=0
    for x in range(1,257):
        for n in (840*x+1,840*x**3+1,8*x**5+1,(8*x+1)**2,840*x**4+1):
            for q in qs:
                if (n+14)%q==0:
                    t=(q+1)//14;v=(n+14)//q;good(n,t,14,v);U=(t*v-1)//4;triple(n,q*U*n,14*U,q*14*U);tot+=1
    assert tot>0
if __name__=='__main__':
    for h in range(3,201,2):orbit(h);old(h);extensions(h);primitive(h)
    residual();moving();poly();print('formal and evaluated orbit, thickness and distribution tests through h=199; refined transfer and polynomial boxes OK')
