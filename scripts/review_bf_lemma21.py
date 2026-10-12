"""R159 from-scratch check of POINTWISE_BINARYFORM Lemma 2.1/2.2.
For several definite forms Q and moduli M (8 | M, 2D | M), list square classes C mod M
(Q(C) = unit square mod M) and check that every (C, octant-sector) pair contains a point
with Q = odd square, by brute force in a box. Also Lemma 2.2 group criterion for u^2+v^2."""
import numpy as np, sys
from math import gcd, isqrt
from itertools import product
def run(A,B,C,M,L,nsec=8):
    D = B*B-4*A*C
    sq = {(s*s) % M for s in range(M) if gcd(s,M)==1}
    classes = [(u,v) for u in range(M) for v in range(M) if (A*u*u+B*u*v+C*v*v) % M in sq]
    need = {(u,v,k) for (u,v) in classes for k in range(nsec)}
    got = set()
    r = np.arange(-L, L+1, dtype=np.int64)
    for u in r:
        v = r
        q = A*u*u + B*u*v + C*v*v
        w = np.round(np.sqrt(q.astype(np.float64))).astype(np.int64)
        ok = (w*w == q) & (w % 2 == 1)
        for vv in v[ok]:
            ang = np.arctan2(vv, u) % (2*np.pi)
            k = int(ang // (2*np.pi/nsec)) % nsec
            got.add((int(u) % M, int(vv) % M, k))
    miss = need - got
    print(f"Q=({A},{B},{C}) D={D} M={M}: square classes {len(classes)}, (class,sector) pairs {len(need)}, missing in box L={L}: {len(miss)}", flush=True)
    return miss
for (A,B,C,M,L) in [(1,0,1,8,300),(1,0,1,40,1500),(1,0,1,24,1500),(1,1,1,24,1500),(1,0,2,16,1500),(1,0,5,40,2500),(2,2,3,40,800),(1,0,1,4,300)]:
    miss = run(A,B,C,M,L)
    if M == 4 or miss: print("   sample missing:", sorted(miss)[:6])
# Lemma 2.2: group criterion for Q=u^2+v^2
def l22(M):
    units = [(u,v) for u in range(M) for v in range(M) if gcd(u*u+v*v, M)==1]
    mul = lambda x,y: ((x[0]*y[0]-x[1]*y[1]) % M, (x[0]*y[1]+x[1]*y[0]) % M)
    sqs = {mul(x,x) for x in units}
    H = set()
    for lam in range(M):
        if gcd(lam,M)!=1: continue
        for j in range(4):
            ij = [(1,0),(0,1),(M-1,0),(0,M-1)][j]
            for s in sqs: H.add(mul(((lam*ij[0])%M,(lam*ij[1])%M), s))
    sqZ = {(s*s)%M for s in range(M) if gcd(s,M)==1}
    mism = sum(((x in H) != ((x[0]**2+x[1]**2)%M in sqZ)) for x in units)
    print(f"Lemma 2.2 M={M}: units {len(units)}, |H|={len(H)}, mismatches {mism}")
for M in [4,8,12,16,20,32,48,72,80,104]: l22(M)
