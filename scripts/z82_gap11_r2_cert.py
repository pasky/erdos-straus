"""Outward-rounded sieve certificates. Scaled integers (S units); no libm signs.
At g=2000 the two main grids hold 2*1000*776 signed 64-bit entries (~12 MiB total), besides lookup tables and the bounded function cache.
The exp(γ) and π brackets are independently checked at startup.
"""
from fractions import Fraction as Q
from math import isqrt
from functools import lru_cache
from array import array
S=10**12

def ceildiv(a,b):return -((-a)//b)
def down(a,b):return a*b//S
def up(a,b):return ceildiv(a*b,S)
def sq(n,d=1):return isqrt(n*S*S//d)
def loglo(x): # rational positive x>=1, log by range reduction and atanh
    assert x>=1
    p=x.numerator; q=x.denominator; k=p.bit_length()-q.bit_length()
    if p<q<<k:k-=1
    y=x/(1<<k); z=(y-1)/(y+1); t=Q(1,3)
    return 2*sum((k*t**(2*j+1)+z**(2*j+1))/(2*j+1) for j in range(17))
# loglo error for x <= 10^12 is < 1e-14 (z<=1/3, k<40).
# Standard harmonic integral: 0 < H_n-log n-gamma < 1/n.
HH=sum((Q(1,i) for i in range(1,20001)),Q(0)); ln=loglo(Q(20000)); gam=HH-ln
assert Q(57718,100000)<gam-Q(1,20000)-Q(1,10**14)<gam<Q(57725,100000)
from math import factorial
elo=sum((gam-Q(1,20000)-Q(1,10**14))**j/factorial(j) for j in range(12));ehi=sum(gam**j/factorial(j) for j in range(12))+Q(2, factorial(12))*gam**12
# Machin identity, alternating arctan at 1/5 and 1/239
at=lambda z,m:sum((-1)**i*z**(2*i+1)/(2*i+1) for i in range(m))
pl=16*at(Q(1,5),10)-4*at(Q(1,239),11);ph=16*at(Q(1,5),11)-4*at(Q(1,239),10)
assert Q(31415926,10**7) < pl < ph < Q(31415927,10**7)
El=17810*S//10000; Eu=17812*S//10000
assert El<S*elo<S*ehi<Eu
Al=2*sq((elo/ph).numerator,(elo/ph).denominator);Au=2*(1+sq((ehi/pl).numerator,(ehi/pl).denominator))
N=1000; MAX=25; T=N*MAX
# E,F in this block are sums of even/odd H_h, before multiplying by A/sqrt(s).
de=[S]*(T+1); odd=[0]*(T+1); Hhi={}; prev=[S]*(T+1);prevlow=prev
W=[]
for i in range(N,T):
    dl=max(0,sq(i+1-N,N)-sq(i-N,N)-1);du=dl+3
    W.append((dl*S//(sq(i+1,N)+1),ceildiv(du*S,sq(i,N))))
for h in range(1,MAX+1):
    cur=[0]*(T+1);low=[0]*(T+1)
    for i in range(N*h,T):
        wl,wh=W[i-N]; low[i+1]=low[i]+down(wl,prevlow[i-N]);cur[i+1]=cur[i]+up(wh,prev[i+1-N]);
    if h%2==0:de=[a+b for a,b in zip(de,cur)];Hhi[h]=cur
    else:odd=[a+b for a,b in zip(odd,low)]
    prev=cur;prevlow=low
# Lookup monotone sieve functions at rounded-down argument. For s<1/N use
# the exact initial A/sqrt(s) upper. No positive f used below s=1.
@lru_cache(200000)
def half(n,d):
    assert n>0 and d>0
    i=min(T,n*N//d)
    if i==0:return 0,ceildiv(Au*S,sq(n,d))
    return (down(Al,odd[i])*S//(sq(i,N)+1),ceildiv(up(Au,de[i])*S,sq(i,N)))
# Normalized sF1/(2exp(gamma)), sf1/(2exp(gamma)); increasing; DDE.
LL=[0]*(T+1); UU=[S]*(T+1); Lhi=LL.copy(); Ulo=UU.copy()
for i in range(2*N,T):
    LL[i+1]=LL[i]+Ulo[i-N]//(i+1-N);Lhi[i+1]=Lhi[i]+ceildiv(UU[i+1-N],i-N)
    if i>=3*N:Ulo[i+1]=Ulo[i]+LL[i-N]//(i+1-N);UU[i+1]=UU[i]+ceildiv(Lhi[i+1-N],i-N)

def lin(n,d):
    i=min(n*N//d,T);assert i>0
    return down(2*El,LL[i])*N//i,ceildiv(up(2*Eu,UU[i])*N,i)

def arraytable(b,g,imax):
    """b, j, i are integer grid indices, physical exponents divided by g."""
    top=g//2-1;INF=10**18
    LO=[array('q',[0])*(imax+1) for _ in range(top+1)];HI=[array('q',[INF])*(imax+1) for _ in range(top+1)]
    # 1/2 log(1+1/i). Bound by alternating Taylor terms through x^3,x^4.
    I=[(0,0)]
    for i in range(1,imax+1):
        x=Q(1,i);hi=(x-x*x/2+x**3/3)/2;I.append(((S*(hi-x**4/8)).__floor__(),(S*hi).__ceil__()))
    for j in range(1,top+1):
        l,u=lin(j,b)
        for i in range(b,imax+1):
            if i>b:
                rl,ru=I[i-1];k=j-i # minimum remaining level j-(i-1+1)
                l=max(0,LO[j][i-1]-up(ru,HI[k][i-1])) if k>0 else 0
                u=HI[j][i-1]-down(rl,LO[k][i]) if k>0 else HI[j][i-1]
            # Vector sum after common small-prime presieve; density relative to V(b,b) is sqrt(b/i).
            root=sq(b,i)
            for num,den in [(v,5) for v in (5,7,9,10,11,12,13,14,15,17,20)]+[(j,2*b)]:
                if num*b>=j*den:continue
                l3,u3=half(j*den-num*b,i*den);l7,u7=half(num,den)
                su=up(u3,u7);ml=down(l3,u7)+down(u3,l7)-su
                l=max(l,down(root,max(0,ml)));u=min(u,up(root+1,su))
            HI[j][i]=u;LO[j][i]=l
    return LO[-1],HI[-1],top

def uncond(b,g,a):
    L,_,top=arraytable(b,g,a)
    # normalize in U0(a,b); J1(a)=2 H2(1/a), and smaller switched cutoff X^b.
    A=sq(a,g);vlo=down(sq(a,b),L[a]);J=2*Hhi[2][ceildiv(g*N,a)]
    cost=min(ceildiv(up(up(up(Au,A+1),J),half(s,10)[1])*g*10,top*10-s*b) for s in range(16,34) if s*b<top*10)
    u=ceildiv(g*N,b);assert u<=T
    hsum=sum(H[u] for h,H in Hhi.items() if h>=6)
    fac=up(up(3*Eu//2,sq(2*g,top)+1),sq(a*b,g*g)+1)
    extra=ceildiv(up(fac,hsum)*2*g,top)
    print('unconditional grid (a,b,tau):',Q(a,g),Q(b,g),Q(top,g),'lower, cost3, cost7(>=6), net (1e-12 units):',vlo,cost,extra,vlo-cost-extra,flush=True)
    return vlo-cost, vlo-cost-extra

def ordinary():
    # Extra-prime inclusion series: V'(w)=(w-1)V(w-1)/(2w^2).
    g=1000;cap=300;V=array('q',[S])*(cap*g+1)
    for i in range(g,cap*g): V[i+1]=V[i]+V[i-g]*(i-g)//(2*(i+1)**2)
    G=100000;start=35000; tau_i=95690; cost=0
    for i in range(start,G//2):
        j=min(cap*g,(tau_i-i-1)*g//(2*(G-2*i)))
        cost+=ceildiv(2*G*S*S,i*(tau_i-i-1)*V[j])
    L=(2*S*G*loglo(Q(tau_i,start)-1)/tau_i).__floor__()
    print('ordinary conditional tau,z0, enhanced cost and margin (1e-12 units):',Q(tau_i,G),Q(start,G),cost,L-cost,flush=True)
    assert L-cost>10**8

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        g,b,a=map(int,sys.argv[1:]);uncond(b,g,a)
    else:
        assert uncond(114,2000,775)[1]>10**9
        assert uncond(115,2000,775)[0]>4*10**9
        g,top,a,b=10000,4999,3710,338
        lowers=[];costs=[];J=2*Hhi[2][ceildiv(g*N,a)]
        for i in range(180,271):
            l,u=half(top*100-b*i,a*100);ll,uu=half(i,100)
            lowers.append(down(l,uu)+down(u,ll)-up(u,uu))
            costs.append(ceildiv(up(up(up(Au,sq(a,g)+1),J),uu)*g*100,top*100-i*b))
        print('bare asymmetric full-convolution switch, b=0.0338, lower minus cost:',max(lowers)-min(costs))
        assert max(lowers)-min(costs)>10**9
        ordinary()
