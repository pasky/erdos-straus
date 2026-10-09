"""R98: validate review_r98_xss.c against DIRECT ET class membership (ET Prop 1.9 class definitions, CRT
lift of x(u11,u13)), brute force over a,d<=AD, e<=X, at several points.  Engine hits restricted to a,d<=AD
must equal brute-force hits."""
import sys, subprocess, random
from math import gcd
AD=int(sys.argv[1]); X=int(sys.argv[2]); npts=int(sys.argv[3]); seed=int(sys.argv[4])
def vpart(M,q):
    r=1
    while M%q==0: M//=q; r*=q
    return r
def lift(M,u11,u13):
    m11=vpart(M,11); m13=vpart(M,13); Mp=M//(m11*m13)
    # CRT
    n=0; mod=1
    for (res,m) in ((1,Mp),(u11,m11),(u13,m13)):
        res%=m
        # solve n ≡ cur mod mod, n ≡ res mod m
        t=((res-n)*pow(mod,-1,m))%m if m>1 else 0
        n=n+mod*t; mod*=m
    return n%M
def brute(u11,u13):
    hits=set()
    for a in range(1,AD+1):
        for d in range(1,AD+1):
            for e in range(1,X+1):
                # II3 (a,d,e)
                if gcd(4*a*d,e)==1:
                    M=4*a*d*e; n=lift(M,u11,u13)
                    if (n+4*a*a*d+e)%M==0: hits.add(('II3',a,d,e))
                    # I3 (c=a,d,f=e): n≡-f (4cd), n^2≡-4c^2d (f)
                    if (n+e)%(4*a*d)==0 and (n*n+4*a*a*d)%e==0: hits.add(('I3',a,d,e))
                # I1 (a,d,f=e): f|4a^2d+1, n≡-f (4ad)
                if (4*a*a*d+1)%e==0:
                    M=4*a*d; n=lift(M,u11,u13)
                    if (n+e)%M==0: hits.add(('I1',a,d,e))
                # II2 (a,d,f=e): 4ad|f+1, n≡-4a^2d (f)
                if (e+1)%(4*a*d)==0:
                    n=lift(e,u11,u13)
                    if (n+4*a*a*d)%e==0: hits.add(('II2',a,d,e))
    return hits
random.seed(seed)
pts=[(2,2),(2,15)]
while len(pts)<npts:
    u=(random.randrange(1,300),random.randrange(1,300))
    if u[0]%11 and u[1]%13: pts.append(u)
tot=0; bad=0
for (u11,u13) in pts:
    B=brute(u11,u13)
    out=subprocess.run(['/tmp/r98xss',str(u11),str(u13),str(X)],capture_output=True,text=True).stdout
    E=set()
    for line in out.split():
        pass
    for line in out.strip().splitlines():
        fam,p1,p2,p3=line.split(); a=int(p1.split('=')[1]); d=int(p2.split('=')[1]); e=int(p3.split('=')[1])
        if a<=AD and d<=AD: E.add((fam,a,d,e))
    tot+=len(B)
    if B!=E:
        bad+=1; print('MISMATCH',(u11,u13),'brute-only',sorted(B-E)[:5],'engine-only',sorted(E-B)[:5])
    else: print((u11,u13),'ok',len(B))
print('points',len(pts),'brute hits',tot,'mismatching points',bad)
