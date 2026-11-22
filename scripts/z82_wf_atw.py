"""Use complete z81 ET list and the exact linear equation for planes through W.
Give every symmetric hit and the smallest primitive normal heights for general
planes (bounded search for the latter; each minimum preceded by complete boxes).
"""
from math import gcd
from itertools import permutations,product
from z81_dual_family import pts

for p in (409,577,2521,3361,102001,8813281):
    b=(p+1)//2;g=p*b;trips=sorted(t for T in pts(p) for t in permutations(T))
    sym=set();best=None
    for x,y,z in trips:
        m,r=divmod(x+y-b-g,2*z-p)
        if not r and x<y:sym.add((2*m,x,y,z))
    # Impose a>0 by sign normalization; all three coefficients nonzero.
    for h in range(1,101):
        candidates=[]
        # Chebyshev shells; try a,c and solve for the (nonzero) b-weight.
        for a in range(1,h+1):
            for c in range(-h,h+1):
                if not c or c%2:continue
                for x,y,z in trips:
                    e,r=divmod(a*(b-x)-c//2*(2*z-p),y-g)
                    if not r and e and max(a,abs(c),abs(e))==h and gcd(a,gcd(e,c))==1:
                        candidates.append((a,e,c,x,y,z))
        if candidates:
            best=min(candidates);break
    print('p',p,'symmetric sorted',sorted(sym),'least normal through H=100',best,flush=True)
