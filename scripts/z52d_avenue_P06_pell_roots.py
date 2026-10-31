import sys, math
from sympy import primerange, divisors, legendre_symbol as L
def cf_norms(p):
    # continued fraction of sqrt(p): m,d,a recurrence; d_k = |P^2 - pQ^2| values (forms in principal cycle)
    a0=math.isqrt(p); m,d,a=0,1,a0; norms=set(); pq=set()
    while True:
        m=d*a-m; d=(p-m*m)//d; a=(a0+m)//d
        norms.add(d); pq.add(a)
        if d==1: break
    return norms, pq
def nbrs(p,u):
    N=p+u
    for v in divisors(N):
        if v!=u and (p+u+v)%(u*v)==0: yield v
N=int(sys.argv[1]); fail=[]; tot=0
for p in primerange(13,N):
    if p%4!=1: continue
    tot+=1
    norms,pq=cf_norms(p)
    ok=False
    for u in sorted(norms|pq):
        if u%p==0: continue
        cu=L(u%p,p)
        for v in nbrs(p,u):
            if v%p and L(v%p,p)!=cu: ok=True;break
        if ok: break
    if not ok: fail.append(p)
print("primes",tot,"no bichromatic edge at CF-cycle roots:",len(fail),fail[:30])
