# z52d pass2 TO1 (Z0318): for odd primes l < L, the least k <= K such that 1+l^k has an odd prime factor = 3 (mod 4)
# (the Z[1/l] unit-sum mechanism of BRAINSTORM/other_rings.md Prop 3.2 needs e | 1+l^k with e = 3 mod 4).
# Factorisation is by trial division up to 10^6 plus a sympy 'factorint(limit=)' fallback; 'unknown' means no factor >=3 mod 4 found below the limit.
# usage: uv run --with sympy python scripts/z52d_p2_TO1_zlk.py L K
import sys
from sympy import primerange, factorint
L=int(sys.argv[1]); K=int(sys.argv[2])
hist={}; unknown=[]; worst=(0,0)
for l in primerange(3,L):
    found=None; unk=False; uncert=[]
    for k in range(1,K+1):
        n=1+l**k
        m=n
        while m%2==0: m//=2
        if m%4==3:
            found=k; break
        f=factorint(m, limit=10**6)
        big=[p for p in f if p>10**6]
        if any(p%4==3 for p in f): found=k; break
        if big: unk=True; uncert.append(k)  # cofactor unfactored: may still contain a 3 mod 4 prime
    if found is None:
        if unk: unknown.append(l)
        else: unknown.append(('none',l))
        continue
    hist[found]=hist.get(found,0)+1
    if found>=9: print("  l=",l,"found k=",found,"; smaller k with unfactored cofactor (uncertified negatives):",[k for k in uncert if k<found])
    if found>worst[0]: worst=(found,l)
print("L=",L,"K=",K,"least-k histogram:",dict(sorted(hist.items())))
print("worst k=",worst[0],"at l=",worst[1])
print("primes with no certified k<=K:",len(unknown), unknown[:20])
