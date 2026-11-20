"""u=q/p>0 prescribed. Three-index point reconstruction; see R17_PUSH.
One engine process; leave shifts split into H,J ranges. Factor only two
consecutive 64-bit progressions; no GNÚ-factor dependency in point search."""
import sys
from math import isqrt
from z76_lift import rootup

def search(r,L,p,q,mode,lo,hi,testcut=None):
    W=r**L;N=W*W//r
    if testcut is None:assert r>=17 and p*q<=5 and p+q<=6 and W>=1000 and p!=q and (p,q) in [(1,5),(5,1),(1,3),(3,1)]
    # H <= 12 W/(17 M), J <= 5p M a/(2W); product at most .275 W².
    X=rootup((28*W*W+99)//100,4) if testcut is None else testcut
    count=tr=0;lo=max(1,lo);hi=min(X,hi)
    def hit(a,b,d):
        nonlocal count
        if not 1<=a<=b or d<1:return
        e=4*a*b*d-N
        if 0<e<=a+b and (a+b)%e==0 and (p*a+q*b)%W==0:
            c=(a+b)//e
            if (a*b*c*d)%r:
                count+=1; print('hit',r,L,p,q,a,b,c,d,flush=True)
    if mode=='Ha':
        for H in range(lo,hi+1):
            V=W*H
            for a in range(1,X//H+1):
                tr+=1;b,rem=divmod(V-p*a,q)
                if rem or b<a:continue
                s=4*a*b;dl=N//s+1;dh=(N+a+b)//s
                if dl<=dh:hit(a,b,dl) # (a+b)/(4ab)<1
    if mode=='Hd':
        for H in range(lo,hi+1):
            V=W*H;VV=V*V
            for d in range(1,X//H+1):
                tr+=1
                # d*(V-2pa)^2=dV²-pq(N+e). e<=W on W>=1000.
                upper=VV-((p*q*(N+1)+d-1)//d)
                if upper<0:continue
                up=isqrt(upper); low=isqrt(max(0,VV-(p*q*(N+W))//d));m=2*p
                for left,right in ((V-up,V-low),(V+low,V+up)):
                    for a in range(max(1,(left+m-1)//m),right//m+1):
                        b,rem=divmod(V-p*a,q)
                        if rem==0:hit(a,b,d)
    if mode=='J' and lo<=hi:
        # Each J factors A=qW/r+J and B=pW/r+J. M|A, e|B (no restriction to prime divisors).
        # Sieve the J for which A divisible by 4 only, with both A,B in step 4.
        j0=lo+(-q*(W//r)-lo)%4
        P=isqrt(max(p,q)*W//r+hi);sieve=bytearray(b'\1')*(P+1);sieve[:2]=b'\0\0'
        for i in range(2,isqrt(P)+1):
            if sieve[i]:sieve[i*i::i]=bytes(1+(P-i*i)//i)
        primes=[i for i in range(3,P+1,2) if sieve[i]]
        for start in range(j0,hi+1,4*16000):
            size=min(16000,(hi-start)//4+1)
            def divtab(v):
                xs=list(range(v,v+4*size,4)); ds=[[1] for _ in xs]
                def peel(i,t):
                    f=1;old=ds[i][:]
                    while xs[i]%t==0:
                        xs[i]//=t;f*=t;ds[i].extend(x*f for x in old)
                if v%2==0:
                    for i in range(size):peel(i,2)
                for t in primes:
                    if t*t>v+4*size:break
                    for i in range((-v*((3*t+1)//4 if t%4==1 else (t+1)//4))%t,size,t):peel(i,t)
                for i,x in enumerate(xs):
                    if x>1:ds[i]+=[d*x for d in ds[i]]
                return ds
            As=divtab(q*(W//r)+start);Bs=divtab(p*(W//r)+start)
            for i,(AA,BB) in enumerate(zip(As,Bs)):
                J=start+4*i; V=W*J;tr+=1
                for M in AA:
                    if M%4:continue
                    for e in BB:
                        if e%4!=(-N)%4 or e>W:continue
                        a,rem=divmod(V-q*e,p*M)
                        if not rem and a>0 and M%(4*a)==0:
                            b,rem=divmod(N+e,M)
                            if not rem:hit(a,b,M//(4*a))
    print('end',r,L,p,q,mode,X,lo,hi,tr,count,flush=True)
if __name__=='__main__':
    search(*map(int,sys.argv[1:5]),sys.argv[5],*map(int,sys.argv[6:]))
