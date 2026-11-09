# Matched control for rule G: each Gaussian candidate letter L (divisor of a, b, a+-b; p = a^2+b^2) is paired with
# random L' within +-25% of L (L >= 600) and L' = L (mod 120) (same 2,3,5-adic type).  Compares per-letter hit rates.
import sys, random, math
from sympy import divisors
sys.setrecursionlimit(10000)
def v2(n):
    v=0
    while n%2==0: n//=2; v+=1
    return v
def is_letter(p,L):
    Lx=8*L//math.gcd(8,L); N1=p+L
    for d in divisors(N1):
        if (d+1)%Lx==0: return True
        if (d+1)%L==0 and v2(N1//d)+v2((d+1)//L)>=3: return True
    for D in divisors(L*p+1):
        if (D+1)%Lx==0: return True
    return False
def twosq(p):
    for a in range(1,math.isqrt(p)+1,2):
        b2=p-a*a; b=math.isqrt(b2)
        if b*b==b2: return a,b
random.seed(int(sys.argv[1]))
ps=[int(l.split()[0]) for l in sys.stdin if l.strip()]
hG=hC=n=0
for p in ps:
    a,b=twosq(p); lim=math.isqrt(2*p); S=set()
    for v in (a,b,a+b,abs(a-b)):
        for d in divisors(v):
            if 600<=d<=lim: S.add(d)      # L >= 600: window +-25% has >= 2 numbers = L mod 120
    for L in S:
        lo=int(L*0.75); hi=int(L*1.25)
        while True:
            Lp=random.randrange(lo,hi+1)
            Lp=Lp-((Lp-L)%120)
            if Lp>=lo and Lp!=L: break
        hG+=is_letter(p,L); hC+=is_letter(p,Lp); n+=1
print(f"letters>=600: n={n}  Gaussian hit rate {hG/n:.4f} ({hG})  matched control {hC/n:.4f} ({hC})")
