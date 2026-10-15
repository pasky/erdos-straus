# For primes p≡1(4) and prime windows q≡3(4), q∤p: least Lemma-1.1 cap (delta_n=0 slice, CAP_DOWN Lemma 1.1)
# split by Legendre (q/p). Exhaustive over exponent boxes (caps up to EMAX).
import sys
from sympy import primerange, factorint, legendre_symbol as L
N=int(sys.argv[1]); QMAX=int(sys.argv[2]); EMAX=int(sys.argv[3])
def least_cap(p,q):
    K=(p+q)//4
    if K%p==0: return None
    f=factorint(K); target=(-K)%q
    # reachable residues with cap<=e: BFS over primes, track min cap
    best={1:0}
    for s,b in f.items():
        new={}
        for r,c in best.items():
            lim=2*b if s==2 else 2*b+2*EMAX
            for cs in range(0,lim+1):
                if s!=2 and cs>2*b and cs%2: continue
                e=max(0,(cs-2*b+1)//2) if s!=2 else 0
                rr=r*pow(s,cs,q)%q; ce=max(c,e)
                if new.get(rr,10**9)>ce: new[rr]=ce
        best=new
    return best.get(target)
stats={}
for p in primerange(5,N):
    if p%4!=1: continue
    for q in primerange(3,QMAX):
        if q%4!=3: continue
        c=least_cap(p,q); key=(L(q,p),((p+q)//4)%2,c)
        stats[key]=stats.get(key,0)+1
for k in sorted(stats,key=str): print(k,stats[k])
