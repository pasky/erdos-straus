# O144: classify chain-realisable ES solutions by g (gcd of coordinates with p removed); run: uv run --with sympy python scripts/bs_farey_frieze_classify.py
import sys, math
sys.argv=['x','0']
exec(open('scripts/bs_farey_frieze.py').read().split("PMAX = int")[0])
from collections import Counter
from itertools import permutations
from sympy import primerange
C=Counter(); T=Counter()
for p in primerange(5,1500):
    for s in solutions(p):
        k=sum(1 for t in s if t%p==0)
        ch=any(is_chain(*o) for o in set(permutations(s)))
        if k==1:
            x=[t for t in s if t%p==0][0]; o=[t for t in s if t%p]
            g=math.gcd(math.gcd(x//p,o[0]),o[1])
        elif k==2:
            o=[t for t in s if t%p==0]; x=[t for t in s if t%p][0]
            g=math.gcd(math.gcd(x,o[0]//p),o[1]//p)
        else: g=-1
        sq=(math.isqrt(g)**2==g) if g>0 else None; T[(k,sq)]+=1
        if ch: C[(k,sq)]+=1
for key in sorted(T,key=str): print(key, "all",T[key],"chain",C[key])
