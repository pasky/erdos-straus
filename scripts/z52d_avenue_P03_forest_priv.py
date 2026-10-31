# Z2841 cheap check: forest edges uv | p+u+v (u<v); how many edges carry a 'private' prime
# (odd exponent in uv, appearing with odd exponent in no other edge product)?
from sympy import factorint, isprime, legendre_symbol
from collections import Counter
def edges(p):
    E=[]
    for v in range(2, p+2):
        u = (-p) % v
        if u == 0 or u >= v: continue
        if (p+u+v) % (u*v) == 0: E.append((u,v))
    return E
for p in [p for p in range(10**6+1, 10**6+20000, 24) if isprime(p)][:6]:
    E = edges(p)
    odd = []
    for u,v in E:
        f = factorint(u*v); odd.append({q for q,e in f.items() if e%2})
    cnt = Counter(q for s in odd for q in s)
    priv = sum(1 for s in odd if any(cnt[q]==1 for q in s))
    mono = sum(1 for u,v in E if legendre_symbol(u%p,p)==legendre_symbol(v%p,p))
    small_only = sum(1 for s in odd if s and max(s) <= 50)
    print(p, 'edges',len(E),'private-prime edges',priv,'monochromatic',mono,'odd-part all <=50:',small_only)
