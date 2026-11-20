"""Exact minimum adelic valuation-height passing all square tests. Congruence solver,
not a global rational-point search. A,B,C are coefficients of a ternary diagonal
unit-square equation. Tuple ordering uses obvious coordinate symmetries only."""
from functools import reduce,lru_cache
from itertools import combinations_with_replacement
from math import gcd,isqrt

@lru_cache(None)
def oddf(n):
    q=3;ps=set();n=abs(n)
    while not n%2:n//=2
    while q*q<=n:
        if not n%q:
            ps.add(q)
            while not n%q:n//=q
        q+=2
    if n>1:ps.add(n)
    return ps

@lru_cache(None)
def sq(p):return frozenset(x*x%p for x in range(1,(p+1)//2))

def accept(vec):
    g=reduce(gcd,vec);a,b,c,d=(z//g for z in vec)
    if (a+b+c-d)%8 or not (a%2 or b%2 or c%2):return False
    for p in {3,5}|oddf(a)|oddf(b)|oddf(c):
        qr=sq(p);ss=[{t*z%p for t in qr} for z in (a,b,c)];ss.sort(key=len)
        if all(z%p==0 for z in (a,b,c)) or not any((d-x-y)%p in ss[2] for x in ss[0] for y in ss[1]):return False
    return True

def xs(H):
    for a,b in combinations_with_replacement(range(1,H+1),2):
        for c in range(1,H+1):
            for d in range(1,H+1):
                if max(b,c,d)==H:yield a,b,c,d

@lru_cache(None)
def powers(t):
    d={};q=2
    while q*q<=t:
        while t%q==0:d[q]=d.get(q,0)+1;t//=q
        q+=1
    if t>1:d[t]=1
    return d

def umin(n,k):
    # At p not dividing n the largest valuation among the denominators
    # must occur twice (else k/n = sum(1/x_i) has negative valuation).
    H=n;old=0
    while True:
        best=H+1;out=None
        for g in range(n,H+1,n):
            for a in range(1,H+1):
                G=powers(g);A=powers(a);fixed=1;free=[]
                for q in G.keys()|A.keys():
                    if q==n:continue
                    e,f=G.get(q,0),A.get(q,0)
                    if e!=f:fixed*=q**max(e,f)
                    else:free.append((q,e))
                if fixed>H:continue
                bs=[fixed]
                for q,e in free:bs=[b*q**i for b in bs for i in range(e+1) if b*q**i<=H]
                for b in bs:
                    while b<=H:
                        h=max(a,b,g)
                        if a<=b and old<h<best and accept((n*a*b,n*b*g,n*a*g,k*a*b*g)):
                            best=h;out=g,a,b
                        b*=n
        if out:return best,out
        old=H;H*=2

def m2(n,k,V):
    # For solution models U below, n is prime and a local point at n
    # forces some denominator divisible by n, hence H>=n.
    if V=='U':return umin(n,k)
    for H in range(1,4*n+20):
        if V=='S':
            for a,b in combinations_with_replacement(range(1,H+1),2):
                for c in range(1,H+1):
                    if max(b,c)==H and accept((-a,-b,k*a*b*c,n)):return H,(a,b,c)
        else:
            for a,b,c,d in xs(H):
                if accept((-a,-b,k*a*b*c*d,n*c)):return H,(a,b,c,d)
    raise RuntimeError(n,k,V)

if __name__=='__main__':
    for n,k,V in [(4545,4,'X'),(4549,4,'X'),(131,8,'U'),(241,8,'U'),(137,8,'U'),(131,8,'S'),(241,8,'S'),(137,8,'S')]:
        if V=='U':assert n>2 and all(n%j for j in range(2,isqrt(n)+1)) and k%n
        print(n,k,V,m2(n,k,V),flush=True)
