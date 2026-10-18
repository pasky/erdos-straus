"""Construction test: are Gaussian-canonical integers (a, b, a+-b, X0 = least lift of sqrt(-1) mod p, N0=(X0^2+1)/p,
convergent data h,k with ak-bh=+-1) better b=1 parameters than controls?  b=1 at window m: g=(-p mod 4m) | m+1.
At level d: p+4d has divisor = -1 mod 4d.  Controls: the same canonical quantity taken from the neighbouring primes p_{i+-1}, p_{i+-2} (same size/shape distribution, independent of p).  Also T1: odd squares."""
import sys, math, collections; sys.path.insert(0,'scripts')
from z35_lib import *
N=int(sys.argv[1])
spf=spf_sieve(4*N+100)
def win(n,m):
    if m<1: return False
    g=(-n)%(4*m); return g>0 and (m+1)%g==0
def lev(n,d):
    if d<1 or n+4*d>4*N+90: return None
    t=4*d; nn=n+4*d
    return any(w<nn and w%t==t-1 for w in divisors_from(factor(nn,spf)))
def canon(p):
    a,b=rep2(p)
    # convergent: h,k with a*k-b*h=1
    k=pow(a,-1,b) if b>1 else 1; h=(a*k-1)//b
    X0=a*pow(b,-1,p)%p; X0=min(X0,p-X0); N0=(X0*X0+1)//p
    return {'a':a,'b':b,'a+b':a+b,'|a-b|':abs(a-b),'h':h,'k':k,'X0':X0,'N0':N0,'ab/2':a*b//2,'(a+b)/2':(a+b)//2 if (a+b)%2==0 else a+b}
st=collections.defaultdict(lambda:[0,0,0,0])  # canon hits, canon n, control hits, control n
PP=[p for p in primes_upto(N,spf) if p%4==1 and p>=13]
CC=[canon(p) for p in PP]
for i,p in enumerate(PP):
    C=CC[i]
    for name,v in C.items():
        for kind,f in (('win',win),('lev',lev)):
            r=f(p,v)
            if r is None: continue
            s=st[(kind,name)]; s[0]+=r; s[1]+=1
            for j in (-2,-1,1,2):   # control: same canonical quantity of neighbouring primes
                if not 0<=i+j<len(PP): continue
                r2=f(p,CC[i+j][name])
                if r2 is None: continue
                s[2]+=r2; s[3]+=1
print("p<=%d  kind name: canonical rate | control rate | z"%N)
for key,(h,n,hc,nc) in sorted(st.items()):
    r1=h/n; r2=hc/nc if nc else 0
    se=math.sqrt(max(r2*(1-r2),1e-12)/n)
    print(key, "%.4f (%d) | %.4f | z=%.1f"%(r1,n,r2,(r1-r2)/se))
