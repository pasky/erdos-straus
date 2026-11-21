"""Unfitted *model*, not an evaluation of shifted-prime asymptotics.
Outputs conditional constants on each hard residue; unconditional-on-primes
normalization divides their sum by phi(840)=192. Y truncates absolutely
convergent products only. Memory O(Y + #packets)."""
import csv,itertools,math,sys
from functools import lru_cache
from pathlib import Path
from math import gcd,log,exp,sqrt,pi,prod
D=Path('data/z80/model'); RS=(1,121,169,289,361,529)
Y=int(sys.argv[1]) if len(sys.argv)>1 else 30000
N=bytearray(Y+1); qs=[]
for l in range(2,Y+1):
    if not N[l]:
        qs.append(l);N[l*l::l]=b'\x01'*len(N[l*l::l])
def factors(n):return [l for l in qs if l<=n and n%l==0]
@lru_cache(None)
def chi(f):
    Q=factors(f);return tuple(prod(0 if a%l==0 else (1 if pow(a,(l-1)//2,l)==1 else -1) for l in Q) for a in range(f))
@lru_cache(None)
def chars(k):return [f for f in range(3,k+1,4) if k%f==0 and prod(factors(f))==f]
@lru_cache(None)
def landau(k,f):
    ch=chi(f);L=-pi*sum(a*x for a,x in enumerate(ch))/f**1.5
    L*=prod(1-ch[l%f]/l for l in factors(k) if f%l)
    return sqrt(L/pi*prod(1-1/l for l in factors(k))*prod(1-1/l**2 for l in qs if k%l and ch[l%f]==-1))

def tuplecoef(K,F):
    # All local primes carrying sign characters or the input progression.
    A=sorted({2,3,5,7}.union(*(factors(k) for k in K)));J=len(K);C=prod(landau(k,f) for k,f in zip(K,F)); base=1.
    def bad(l):return [k for k,f in zip(K,F) if k%l==0 or chi(f)[l%f]!=1]
    for l in qs:
        B=bad(l);base/=(1-1/l)**len(B)
        if l not in A:base*=1-len({(-k)%l for k in B})/(l-1)
    out=[]
    for r in RS:
        v=0.
        for T in range(1<<J):
            h=1.
            for l in A:
                B=bad(l);sign=sum((T>>i)&1 for i,f in enumerate(F) if f%l==0)%2
                if l in (2,3,5,7):
                    h*=int(all((r+k)%(8 if l==2 else l)!=0 for k in B))*(chi(l)[r%l] if sign else 1)
                else:
                    # Sum local Legendre signs over units minus forbidden set.
                    V={-k%l for k in B}-{0};h*=((-sum(chi(l)[v] for v in V) if sign else l-1-len(V))/(l-1))
            v+=h
        out.append(C*base*v)
    return out

def coeff(K):return [sum(x) for x in zip(*(tuplecoef(K,F) for F in itertools.product(*(chars(k) for k in K))))]

def main():
    # 88 pairs' worth is not needed: 88 WINDOWS suffice for log n <= 86.
    S=[];B=[]
    with (D/'coeff.csv').open('w') as o:
        w=csv.writer(o,lineterminator='\n');w.writerow(['windows',*RS,'per_all_primes'])
        for j in range(88):
            k=4*j+3;v=coeff((k,));S.append(v);w.writerow([k,*[f'{x:.8f}' for x in v],f'{sum(v)/192:.8f}'])
            if j%2:
                v=coeff((k-4,k));B.append(v);w.writerow([f'{k-4}:{k}',*[f'{x:.8f}' for x in v],f'{sum(v)/192:.8f}'])
    # Inhomogeneous Poisson input locations, intensity dx/(192 log x) per r;
    # early miss law from disjoint adjacent pairs conditional on r. Late branch
    # after exactly ceil(log x) windows shares one random index and count bit.
    # The first 3-window threshold (g>=3) means zero windows tested.
    def tails(t,r,Jmax):
        j0=math.ceil(t); E=[1.]
        for j in range(j0):
            if j%2==0:E.append(E[-1]*min(1,S[j][r]/sqrt(t)))
            else:E.append(E[-2]*min(1,S[j-1][r]/sqrt(t),S[j][r]/sqrt(t),B[j//2][r]/t))
        z=exp(-3*t*t/(4*pi*pi));end=int((2*exp(t)+1)//4);nlate=end-j0
        for j in range(j0+1,Jmax+1):E.append(E[j0]*(z+(1-z)*max(0,1-(j-j0)/nlate)))
        return E[:Jmax+1],E[j0]*z
    # Integrate by midpoint in log x. Initial start 1009 is set by Mordell,
    # not by fitting heights. Report expected first-exceedance crossing of 1.
    Jmax=80;cum=[0.]*(1+Jmax);first=[None]*len(cum);zsum=0.
    start=log(1009);dx=.01;known=None
    endpoints=sorted([log(5e12),log(1e18),log(1e30),86.]);t=start
    while t<86.-1e-10:
        dt=min(dx,endpoints[0]-t,math.ceil(t+1e-9)-t);m=t+dt/2;arr=[tails(m,i,Jmax) for i in range(6)];scale=exp(m)*dt/(192*m)
        if m>log(1e18):zsum+=scale*sum(z for _,z in arr)
        for j in range(len(cum)):
            inc=scale*sum(v[j] for v,_ in arr)
            if first[j] is None and inc+cum[j]>=1:first[j]=exp(t+dt*(1-cum[j])/inc)
            cum[j]+=inc
        t+=dt
        if abs(t-endpoints[0])<1e-8:
            print('endpoint',f'{exp(t):.4g}','last threshold with mean >=1',max((4*j+3 for j,v in enumerate(cum) if v>=1),default=0),'mean >=111,119,127',*[f'{cum[j]:.5g}' for j in (27,29,31)])
            if known is not None:
                print('conditional on measured max 127 through 5e12:',max([127]+[4*j+3 for j,v in enumerate(cum) if v-known[j]>=1]))
            else:known=cum.copy()
            endpoints.pop(0)
    print('expected full failures from 1e18 to exp(86)',f'{zsum:.6g}')
    R=[(int(p),int(g)) for _,p,g in (s.split() for s in Path('data/z80/gap/deep.txt').read_text().splitlines() if s.startswith('REC'))];print('threshold,first_actual_M,first_model_mean_one')
    for j in range(32):print(4*j+3,next(p for p,g in R if g>=4*j+3),f'{first[j]:.4g}' if first[j] else 'NA',sep=',')
if __name__=='__main__':main()
