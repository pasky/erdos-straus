# checks for batch 07 small-slice items: B-slice of (★) succeeds iff p+B has a divisor s ≡ -1 (mod 4B), s>=4B-1
from sympy import primerange, factorint, divisors
def slice_ok(p,B):
    return any((s+1)%(4*B)==0 for s in divisors(p+B))
bad=0; tot=0; b1fail=0
for p in primerange(5,200000):
    if p%4!=1: continue
    tot+=1
    m=(p+1)//2
    crit=any(q%4==3 for q in factorint(m))
    if crit!=slice_ok(p,1): bad+=1
    if not crit: b1fail+=1
print("B=1 criterion mismatches:",bad,"of",tot,"; B=1 failure fraction",b1fail/tot)
for p in [409]:
    print(p,[ (B,factorint(p+B)) for B in range(1,8)], [slice_ok(p,B) for B in range(1,30)].count(True))
