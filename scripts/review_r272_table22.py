"""R272: recompute Table 2.2 of CLASS_FORCING.md from scratch: G=(Z/4d)^x, d<=30."""
from math import gcd
from sympy import factorint
def order(x, n):
    k, y = 1, x % n
    while y != 1: y = y*x % n; k += 1
    return k
def primary(n):  # primary decomposition of (Z/n)^x via CRT pieces
    out = []
    for q, e in factorint(n).items():
        if q == 2:
            if e == 2: out.append(2)
            elif e >= 3: out += [2, 2**(e-2)]
        else:
            m = (q-1)*q**(e-1)
            out += [r**k for r, k in factorint(m).items()]
    return sorted(x for x in out if x > 1)
for d in range(1, 31):
    n = 4*d; G = [x for x in range(n) if gcd(x, n) == 1]
    ex = 1
    for x in G: o = order(x, n); ex = ex*o//gcd(ex, o)
    sq = {x*x % n for x in G}; quad = len(G)//len(sq)
    poss = [x for x in G if x % 4 == 1]
    m1 = sum(1 for x in poss if any(pow(x, k, n) == n-1 for k in range(1, ex+1)))
    print(d, len(G), "·".join(map(str, primary(n))), ex, quad, len(poss), m1)
