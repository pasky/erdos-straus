# PROOF CERTIFICATE: (W) holds for every square n = m^2 except n = 1, 9.
#  * m even, m >= 2: n = 0 (mod 4), (x,y,z) = (2, n/4+1, 2).
#  * m odd: m^2 mod M depends on m mod M/2 (M = 360, since (m+180)^2 = m^2 + 360m + 32400, 32400 = 90*360).
#    For each odd class m mod 180 we exhibit a fixed-pair family (modulus | M) containing m^2, and its size threshold.
#  * small odd m below the largest threshold are checked directly.
import sys
from sympy import divisors
M=360; fams=[]
for d in divisors(M):
    if d<3: continue
    for x in divisors(d+1):
        if 2<=x<=(d+1)//2: fams.append(('xy',x,(d+1)//x,d,(-x)%d, 2*d-x))       # n=-x mod d; z=(n+x)/d>=2 iff n>=2d-x
    for x in divisors(d):
        z=d//x
        if x>=2 and z>=2 and x<=z: fams.append(('xz',x,z,d,(-(x+z))%d, 2*x*z-x-z))  # y=(n+x+z)/(xz)>=2
classes=[m for m in range(1,180,2)]
# greedy: smallest set of families covering all odd classes
unc=set(classes); chosen=[]
while unc:
    best=max(fams,key=lambda f: (sum(1 for m in unc if (m*m-f[4])%f[3]==0), -f[3]))
    cov={m for m in unc if (m*m-best[4])%best[3]==0}
    if not cov: print("NOT COVERED",sorted(unc)); sys.exit(1)
    chosen.append(best); unc-=cov
print("families used (type, a, b, modulus, class n = c mod d, threshold n >=):")
for f in chosen: print("  ",f)
T=max(f[5] for f in chosen); print("max threshold",T)
def W(n):
    for x in range(2,int((n/2)**0.5)+3):
        N=n+x
        for d in divisors(N):
            if d%x==x-1 and d>=2*x-1 and N//d>=2: return (x,(d+1)//x,N//d)
    return None
# verify family solutions explicitly for odd m up to 20001 and brute force below threshold
for m in range(1,20001,2):
    n=m*m
    if n<T:
        print("  small m",m,"n",n,"->",W(n)); continue
    ok=False
    for (ty,a,b,d,c,th) in chosen:
        if (n-c)%d==0 and n>=th:
            if ty=='xy': x,y,z=a,b,(n+a)//d
            else: x,z=a,b; y=(n+x+z)//(x*z)
            assert x*y*z-x-z==n and min(x,y,z)>=2; ok=True; break
    assert ok,m
print("odd m < 20001 with m^2 >= threshold: explicit solutions verified")
