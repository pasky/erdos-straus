# Archived verbatim (apart from this header) from board seat Fable's /tmp/a2.py,
# supplied as /tmp/z47q3/a2.py for the z47 independent implementation check.
# Its Miller–Rabin bases are not an arbitrary-size primality certificate.
# z47_q3_pivot_verify.py separately verifies every returned factor before use.
# argon-2 pivot graph: seeds p*U_q, pivots fixing one coordinate; does the depth<=2 component hit (q N)^3 ?
import sys, math
from functools import lru_cache
def primes_upto(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
SMALL=primes_upto(2000)
def factor(n):
    f={}
    for p in SMALL:
        if p*p>n: break
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
    if n>1:
        # pollard rho
        def rho(n):
            if n%2==0: return 2
            import random
            while True:
                x=random.randrange(2,n); y=x; c=random.randrange(1,n); d=1
                while d==1:
                    x=(x*x+c)%n; y=(y*y+c)%n; y=(y*y+c)%n; d=math.gcd(abs(x-y),n)
                if d!=n: return d
        def isprime(n):
            if n<2: return False
            for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
                if n%a==0: return n==a
            d=n-1; s=0
            while d%2==0: d//=2; s+=1
            for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
                x=pow(a,d,n)
                if x in (1,n-1): continue
                for _ in range(s-1):
                    x=x*x%n
                    if x==n-1: break
                else: return False
            return True
        def rec(n):
            if n==1: return
            if isprime(n): f[n]=f.get(n,0)+1; return
            d=rho(n); rec(d); rec(n//d)
        rec(n)
    return f
def divisors(f):
    ds=[1]
    for p,e in f.items():
        ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def solve3(M,N):   # all (x,y,z) positive, x<=y<=z, 1/x+1/y+1/z=M/N
    sols=set()
    x=N//M+1
    while 3*N>=M*x:   # 1/x >= M/(3N)
        num=M*x-N; den=N*x
        g=math.gcd(num,den); a=num//g; b=den//g
        if a>0:
            f=factor(b*b)
            for d in divisors(f):
                if (d+b)%a==0:
                    y=(d+b)//a; z=(b*b//d+b)//a
                    if y>=x and z>=y: sols.add((x,y,z))
        x+=1
    return sols
def pivots(n,W):  # all (U,V) with 1/U+1/V = 4/n - 1/W
    num=4*W-n; den=n*W
    if num<=0: return []
    g=math.gcd(num,den); a=num//g; b=den//g
    out=[]
    for d in divisors(factor(b*b)):
        if (d+b)%a==0:
            U=(d+b)//a; V=(b*b//d+b)//a
            out.append((U,V))
    return out
def reach(p,q,depth):
    n=q*p
    seeds=[tuple(sorted((p*x,p*y,p*z))) for (x,y,z) in solve3(4,q)]
    seen=set(seeds); frontier=list(seeds)
    def hit(v): return all(c%q==0 for c in v)
    for v in frontier:
        if hit(v): return 0
    for d in range(1,depth+1):
        nxt=[]
        for v in frontier:
            for i in range(3):
                W=v[i]
                for (U,V) in pivots(n,W):
                    w=tuple(sorted((W,U,V)))
                    if w not in seen:
                        seen.add(w); nxt.append(w)
                        if hit(w): return d
        frontier=nxt
    return None
if __name__=="__main__":
    lo,hi=int(sys.argv[1]),int(sys.argv[2])
    mord={1,121,169,289,361,529}
    ps=[p for p in primes_upto(hi) if p>=lo and p%24==1 and p%840 in mord]
    fails=[]
    for p in ps:
        best=None
        for q in range(2,12):
            r=reach(p,q,2)
            if r is not None: best=(q,r); break
        if best is None: fails.append(p)
        print(p,best,flush=True)
    print("MORDELL-HARD primes in range:",len(ps),"depth<=2,q<=11 failures:",fails)
