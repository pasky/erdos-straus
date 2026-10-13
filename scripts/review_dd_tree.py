"""R176: count maximal orders of M2(Q_l) containing the Eichler order O_n=[[Z,Z],[l^n Z,Z]].
Maximal orders = End(L), L a lattice up to homothety. Enumerate primitive L with l^K Z^2 c L c Z^2
(all vertices within distance K of Z^2) via Hermite bases, test O_n-stability. Expect n+1 (=> tau(e) globally)."""
import itertools, sys
def lattices(l, K):
    # L = span{(l^i, x), (0, l^j)} columns as vectors (u1,u2); HNF: vectors (l^i, x), (0, l^j), 0<=x<l^j, i+j<=K
    out=set()
    for i in range(K+1):
        for j in range(K+1-i):
            for x in range(l**j):
                # primitive: not all of lattice inside l Z^2
                if i>0 and j>0 and x%l==0: continue
                out.add((i,j,x))
    return out
def contains(L, v, l):
    i,j,x=L; a,b=v
    if a % l**i: return False
    t=a//l**i
    return (b - t*x) % l**j == 0
def stable(L, n, l):
    i,j,x=L; basis=[(l**i, x),(0, l**j)]
    gens=[((1,0),(0,0)),((0,1),(0,0)),((0,0),(l**n,0)),((0,0),(0,1))]  # rows
    for g in gens:
        for (a,b) in basis:
            v=(g[0][0]*a+g[0][1]*b, g[1][0]*a+g[1][1]*b)
            if not contains(L,v,l): return False
    return True
for l in (3,5):
    for n in range(0,5):
        K=n+2
        c=sum(stable(L,n,l) for L in lattices(l,K))
        print(f"l={l} n={n}: maximal orders containing O_n within radius {K}: {c} (expect {n+1})")
