#!/usr/bin/env python3
"""z63 EUCLID: review check M3 — high short loops vs ALL loops of height <= 20 at p = 1009 (run from repo root)."""
import sys; sys.path.insert(0,'scripts')
from math import gcd
import z63_euclid_h1 as H
p=1009; HIGH=20
lev=H.Level(p)
def h_le(A,Hh):
    for b in range(1,Hh+1):
        if gcd(b,p)!=1: continue
        a=(A*b)%p
        if a<=Hh or p-a<=Hh: return True
    return False
low=[A for A in range(1,p) if h_le(A,HIGH)]
high=[A for A in range(1,p) if len(H.hj(p,A))==3 and not h_le(A,HIGH)]
basis=dict(lev.basis)
def add(v):
    v,h=lev.reduce_full(v,basis)
    if h is not None: basis[h]=v; return 1
    return 0
rk=sum(add(lev.loop_class(H.hj(p,A))) for A in low)
inc=sum(add(lev.loop_class(H.hj(p,A))) for A in high)
print("p",p,"dimH",lev.dimH,"#height<=20 loops",len(low),"their rank",rk,"#high short",len(high),"rank increment",inc)
# find combinations of high loops in span(low + relations)
E=lev.E
basis2=dict(lev.basis)
for A in low:
    v,h=lev.reduce_full(lev.loop_class(H.hj(p,A)),basis2)
    if h is not None: basis2[h]=v
for i,A in enumerate(high):
    v=lev.loop_class(H.hj(p,A)) | (1<<(E+i))
    v,h=lev.reduce_full(v,basis2)
    if h is not None: basis2[h]=v
    else:
        tags=v>>E
        combo=[high[j] for j in range(len(high)) if tags>>j&1]
        print("relation among high loops mod low span:", [(B, H.hj(p,B), H.jacobi(B,p), (pow(B,-1,p)), p-B) for B in combo])
