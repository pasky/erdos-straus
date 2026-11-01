# z52d triage T0, Z1468: primes p ≡ 1 (24) in [1000, 6000] lacking a word tuv − u − v = p with 4 | t, t,u,v ≥ 3, t ≤ 100; extension to all t and to boundary (u ≥ 1) words
from sympy import primerange
def words(p,tmax,umin=3):
    out=[]
    for t in range(3,tmax+1):
        N=t*p+1  # (tu-1)(tv-1)=tN... careful: t(tuv-u-v)+1=(tu-1)(tv-1)
        for u in range(umin,10**9):
            A=t*u-1
            if A*A>N: break
            if N%A==0:
                Bv=N//A
                if (Bv+1)%t==0:
                    v=(Bv+1)//t
                    if v>=u: out.append((t,u,v))
    return out
P=[p for p in primerange(1000,6001) if p%24==1]
miss=[p for p in P if not any(t%4==0 for t,u,v in words(p,100))]
print(len(P),len(miss),miss)
for p in miss:
    w=[x for x in words(p,p) if x[0]%4==0]
    star=[x for x in words(p,p,umin=1) if x[0]%4==0]  # u>=1 (v>=u) — boundary allowed
    print(p,'4|t,u,v>=3 any t:',w[:2],' (★)-type with u>=1:',star[:3])
