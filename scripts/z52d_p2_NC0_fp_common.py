# z52d Pass 2 NC0 (G3) — shared helper: certificate graph F_p (FOREST_H4.md / FOREST_CONNECTIVITY.md §0 definition).
# vertices 1..p+2; {u,v} edge iff u!=v and uv | p+u+v.  Enumerated via: v = (p+u)/e with e = t*u-1 | p+u, t>=1.
from sympy import divisors, primerange
def fp_edges(p):
    E=[]
    for u in range(1,p+3):
        N=p+u
        for e in divisors(N):
            if (e+1)%u: continue
            v=N//e
            if u<v<=p+2: E.append((u,v))
    return E
def fp_edges_brute(p):
    return [(u,v) for u in range(1,p+3) for v in range(u+1,p+3) if (p+u+v)%(u*v)==0]
def primes14(N):
    return [q for q in primerange(5,N+1) if q%4==1]
