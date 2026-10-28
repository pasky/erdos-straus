#!/usr/bin/env python3
"""z48 forestfable — Lemma P probe: for each pentagon position q in {t',u,v,A,A*} and residue class of q mod 8,
count edges and bichromatic edges over primes p ≡ 1 (4) below LIM (default 30000), split by p mod 8."""
# which pentagon positions q in {t,u,v,A,A*} with q ≡ 3 or 7 (mod 8) force a certificate? (p ≡ 1 mod 4, p < LIM)
import sys
sys.path.insert(0,'scripts')
from z48_forestfable_converse import primes_upto, edges, legendre, slot
LIM=int(sys.argv[1]) if len(sys.argv)>1 else 30000
from collections import defaultdict
stat=defaultdict(lambda:[0,0])  # key (p mod 8, position, q mod 8) -> [#edges, #bichromatic]
for p in primes_upto(LIM):
    if p%4!=1: continue
    for u,v in edges(p):
        t=(p+u+v)//(u*v); A=(p+u)//v; As=(p+v)//u
        bi = legendre(u,p)*legendre(v,p)==-1
        for name,q in (("t",t),("u",u),("v",v),("A",A),("A*",As)):
            if name=="t":
                while q%4==0: q//=4
            s=stat[(p%8,name,q%8)]; s[0]+=1; s[1]+=bi
for k in sorted(stat):
    n,b=stat[k]
    if k[2] in (0,3,4,7):
        print(k, "edges",n,"bichromatic",b, "ALL-CERT" if n==b else ("ALL-MONO" if b==0 else ""))
