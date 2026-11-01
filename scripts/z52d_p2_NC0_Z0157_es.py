# z52d Pass 2 NC0, item Z0157 — |H_1| of Σ(x,y,z) for all ES triples with n<=NMAX (Milnor–Orlik, scripts/z52d_p2_NC0_Z0157_h1.py).
import sys, collections
from math import gcd
sys.path.insert(0,'scripts')
from z52d_p2_NC0_allsols import sols
from z52d_p2_NC0_Z0157_h1 import h1_order
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 120
tot=0; fin=0; vals=collections.Counter(); sphere=0; ex=[]
for n in range(5,NMAX+1):
    for (x,y,z) in sols(n):
        tot+=1
        v,_=h1_order((x,y,z))
        if v is None or v=='inf': vals['inf/undefined']+=1; continue
        fin+=1; vals[int(v)]+=1
        if v==1: sphere+=1
        if len(ex)<8 and int(v)>1: ex.append((n,(x,y,z),int(v),gcd(x,y),gcd(y,z),gcd(x,z)))
print('n in [5,%d]: unordered ES triples %d; finite |H1|: %d; homology spheres: %d'%(NMAX,tot,fin,sphere))
print('value distribution (top 12):',vals.most_common(12))
print('examples (n,(x,y,z),|H1|,gcd(x,y),gcd(y,z),gcd(x,z)):',ex)
