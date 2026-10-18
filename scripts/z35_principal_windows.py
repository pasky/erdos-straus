"""Principal-form anti-windows: p = x^2 + D y^2 (D = 1,2,3,7).  Window m (b=1 line, (-p mod 4m) | m+1):
m = y-type windows (odd part | y, 2-adic ok) must be sterile (Lemma 3.2 / Prop 5.1); m = x odd: allowed iff (D/x) = -1.
Usage: N"""
import sys, math, collections; sys.path.insert(0,'scripts')
from z35_lib import primes_upto, spf_sieve
N=int(sys.argv[1])
spf=spf_sieve(N+10)
def win(n,m):
    g=(-n)%(4*m); return m>=1 and g>0 and (m+1)%g==0
def reps(p,D):
    out=[]
    for y in range(1,math.isqrt(p//D)+1):
        x2=p-D*y*y; x=math.isqrt(x2)
        if x*x==x2 and x>0: out.append((x,y))
    return out
def jac(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
st=collections.Counter()
for p in primes_upto(N,spf):
    if p%4!=1: continue
    for D in (1,2,3,7):
        for x,y in reps(p,D):
            # y-windows: m = y // 2^j variants with 2^(s+2) | D y^2 ... test m = odd part of y and m = y
            yo=y
            while yo%2==0: yo//=2
            st[(D,'m=odd(y)','n')]+=1; st[(D,'m=odd(y)','h')]+=win(p,yo)
            if x%2==1 and x>1:
                k='m=x,(D/x)=%d'%jac(D,x)
                st[(D,k,'n')]+=1; st[(D,k,'h')]+=win(p,x)
for key in sorted(set(k[:2] for k in st)):
    n=st[key+('n',)]; h=st[key+('h',)]
    print(key, "hits %d / %d = %.4f"%(h,n,h/n if n else 0))
