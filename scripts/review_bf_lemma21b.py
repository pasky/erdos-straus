"""R159: targeted re-search of (class, octant) pairs missed by review_bf_lemma21.py in a bigger box."""
import numpy as np
from math import gcd
def missing(A,B,C,M,L,nsec=8):
    sq = {(s*s) % M for s in range(M) if gcd(s,M)==1}
    classes = [(u,v) for u in range(M) for v in range(M) if (A*u*u+B*u*v+C*v*v) % M in sq]
    worst = 0; bad = []
    for (u0,v0) in classes:
        us = np.arange(u0 - (L//M)*M, L+1, M, dtype=np.int64)
        vs = np.arange(v0 - (L//M)*M, L+1, M, dtype=np.int64)
        U, V = np.meshgrid(us, vs, indexing='ij')
        q = A*U*U + B*U*V + C*V*V
        w = np.round(np.sqrt(q.astype(np.float64))).astype(np.int64)
        ok = (w*w == q)
        ang = np.arctan2(V[ok], U[ok]) % (2*np.pi)
        ks = set((ang // (2*np.pi/nsec)).astype(int) % nsec)
        if len(ks) < nsec: bad.append(((u0,v0), sorted(set(range(nsec))-ks)))
    print(f"Q=({A},{B},{C}) M={M} L={L}: classes {len(classes)}, classes with a missing octant: {len(bad)}", bad[:5], flush=True)
missing(1,0,1,40,40000)
missing(1,0,5,40,40000)
