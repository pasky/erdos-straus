# Solve for g: cells mod 8 (odd n) -> Z/2 with chi(w)g(w) invariant under odd-numerator moves.
from cf_lib import *
from itertools import product
def K(t,u,v): return t*u*v-u-v
cells=[c for c in product(range(8),repeat=3) if K(*c)%2==1]
idx={c:i for i,c in enumerate(cells)}
def chic(c):
    # chi as cell function: use representative with letters in 1..8 (positive) 
    w=tuple(x if x>0 else 8 for x in c); n=K(*w)
    # ensure n>0
    w=tuple(x+8 for x in w); n=K(*w)
    return chi(w,n)
edges=[]
for c in cells:
    t,u,v=c
    for d in [((t,v,u)),((u,v,t)),((v,t,u))]:
        edges.append((c,d))
    for a in (3,5,7):
        edges.append((c,((a*t)%8,(u*a*pow(a,-1,8)**2)%8,v)))  # placeholder, replaced below
edges=[e for e in edges[:]]
# scaling: (a t', u, v) with middle divisible by a  <->  (t', a u, a v). mod 8 with a odd unit: cell (T,u,v) -> (T*a^-1, a u, a v)
edges=[(c,d) for (c,d) in edges if True]
E=[]
for c in cells:
    t,u,v=c
    E += [(c,(t,v,u)),(c,(u,v,t)),(c,(v,t,u))]
    for a in (3,5,7):
        ai=pow(a,-1,8)
        E.append((c,((t*ai)%8,(a*u)%8,(a*v)%8)))
E=[(c,tuple(x%8 for x in d)) for c,d in E if K(*d)%2==1]
# union-find with parity
par={c:(c,0) for c in cells}
def find(c):
    p,x=par[c]
    if p==c: return c,0
    r,y=find(p); par[c]=(r,x^y); return r,x^y
bad=0
for c,d in E:
    w=(chic(c)*chic(d)==-1)  # g(c)+g(d) must equal w
    rc,xc=find(c); rd,xd=find(d)
    if rc==rd:
        if xc^xd!=w: bad+=1
    else: par[rc]=(rd,xc^xd^w)
roots=set(find(c)[0] for c in cells)
print("cells",len(cells),"components",len(roots),"inconsistent",bad)
# does g depend only on n mod 8 within each component?
from collections import defaultdict
G=defaultdict(set)
for c in cells:
    r,x=find(c); G[(r,K(*c)%8)].add(x)
print("component/n-class with both parities:",sum(1 for s in G.values() if len(s)==2))
