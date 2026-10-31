"""Z0547: at fixed p, fraction of levels C <= X with D^-_{4C}(4Cp+1) = 0 (no divisor ≡ −1 mod 4C), versus the
semi-linear-sieve set S = {C : all odd prime factors of 4Cp+1 are ≡ 1 mod 4} (the C=1-type 'Landau' condition)."""
from sympy import factorint, primerange
import sys
def divs(N):
    ds=[1]
    for q,e in factorint(N).items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
P0=int(sys.argv[1]); X=int(sys.argv[2])
ps=[p for p in primerange(P0,P0+20000) if p%24==1][:5]
for p in ps:
    rows=[]
    for C in range(1,X+1):
        N=4*C*p+1; f=factorint(N)
        hit=any(d%(4*C)==4*C-1 for d in divs(N))
        landau=all(q%4==1 for q in f)
        rows.append((C,hit,landau))
    for lo,hi in [(1,10),(11,100),(101,1000),(1001,X)]:
        sub=[r for r in rows if lo<=r[0]<=hi]
        if not sub: continue
        print(p,"C in [%d,%d]: fail frac %.3f  Landau-set frac %.3f  #hits %d"%(lo,hi,1-sum(r[1] for r in sub)/len(sub), sum(r[2] for r in sub)/len(sub), sum(r[1] for r in sub)))
