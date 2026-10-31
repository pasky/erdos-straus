"""z52d avenue P02 / Z0647: are all solutions of 4/p² = 1/x+1/y+1/z (p prime) scalings p·(solution of 4/p)?
i.e. does p divide x, y and z in every solution? If yes, ES(p) fails ⇒ ES(p²) fails (one-step propagation).
EVIDENCE (finite check)."""
import sys
from sympy import factorint
from itertools import product
def divs_of_sq(f):
    ps=list(f.items()); out=[1]
    for q,e in ps:
        out=[d*q**k for d in out for k in range(2*e+1)]
    return out
def sols(n):
    fn=factorint(n); S=[]
    for x in range(n//4+1, 3*n//4+1):
        a=4*x-n; b=n*x
        if a<=0: continue
        from math import gcd
        g=gcd(a,b); a//=g; b//=g
        fb=factorint(b)
        for d in divs_of_sq(fb):
            if d> b: continue  # d = a*y - b <= b  (y<=z)
            if (d+b)%a==0:
                y=(d+b)//a; e=b*b//d
                if (e+b)%a==0:
                    z=(e+b)//a
                    if y>=x: S.append((x,y,z))
    return S
for p in map(int,sys.argv[1:]):
    S=sols(p*p); bad=[s for s in S if not all(t%p==0 for t in s)]
    print(p,"solutions",len(S),"non-scaled",len(bad),bad[:5])
