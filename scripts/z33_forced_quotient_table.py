"""O263 §2 table: for d<=30, G=(Z/4d)^*: structure, exponent, #quadratic chars, #odd chars,
and the 'abstract forced' outcome from total-product data at the b=1 line (N=p+4d, [N]=[p], p≡1 mod 4):
forced iff [p] = -1 (never, since -1≡3 mod 4)."""
from math import gcd
from sympy import factorint
def units(m): return [x for x in range(1,m) if gcd(x,m)==1]
def order(x,m):
    k,y=1,x%m
    while y!=1: y=y*x%m; k+=1
    return k
def inv_factors(m):
    U=units(m); n=len(U)
    # invariant factors via counting elements of each order (abelian group structure)
    from collections import Counter
    # brute: elementary divisors from counts of x with x^(q^k)=1
    ed=[]
    for q in factorint(n):
        cnt=[sum(1 for x in U if pow(x,q**k,m)==1) for k in range(0,40)]
        # cnt[k]=q^{sum_i min(k,e_i)}
        import math
        r=[round(math.log(cnt[k],q)) for k in range(40)]
        # number of e_i >= k is r[k]-r[k-1]
        for k in range(1,40):
            c=r[k]-r[k-1]; c2=(r[k+1]-r[k]) if k+1<40 else 0
            ed += [q**k]*(c-c2)
    return sorted(ed)
print("d | 4d | |G| | elementary divisors | exp | #quad chars |G/G^2| | odd chars | p-classes (x≡1 mod 4) | classes with -1 in <x>")
for d in range(1,31):
    m=4*d; U=units(m); ed=inv_factors(m)
    lam=1
    from math import lcm
    for x in U: lam=lcm(lam,order(x,m))
    sq=len(set(x*x%m for x in U)); nq=len(U)//sq
    odd=len(U)//2  # characters with psi(-1)=-1: exactly half (−1≠1 in G)
    pc=[x for x in U if x%4==1]
    hit=sum(1 for x in pc if any(pow(x,k,m)==m-1 for k in range(1,order(x,m)+1)))
    print(f"{d} | {m} | {len(U)} | {'x'.join(map(str,ed))} | {lam} | {nq} | {odd} | {len(pc)} | {hit}")
