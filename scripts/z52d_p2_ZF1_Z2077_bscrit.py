# Z2077: Bach–Sorenson-type "main term minus triangle inequality over characters" detector on the divisor form of R(p):
#   D_{-1}(N) = #{d | N : d ≡ -1 (mod 4C)} = (1/φ(4C)) Σ_χ χ(-1) σ_χ(N),  N = 4Cp+1.
# BS-type certificate at level C:  Σ_{χ≠1} |σ_χ(N)| < τ(N)  (⇒ every class of G=(Z/4C)^× contains a divisor, in particular -1).
# Necessary: τ(N) ≥ φ(4C) (covering) ; we also record actual hits D_{-1}(N) > 0 and full coverage.
import sys, numpy as np, sympy
from sympy import factorint, totient, primerange
def group_struct(m):
    """return list of (modulus component, generator list, orders) to compute discrete-log vectors mod m via CRT."""
    comps=[]
    for l,k in factorint(m).items():
        q=l**k
        if l==2:
            if k==1: continue
            if k==2: comps.append((q,[(q-1,2)])) ; continue
            comps.append((q,[(q-1,2),(5,q//4)]))
        else:
            g=sympy.primitive_root(q); comps.append((q,[(g,q-q//l)]))
    return comps
def dlog_tables(m):
    comps=group_struct(m); tabs=[]; shape=[]
    for q,gens in comps:
        if len(gens)==1:
            g,o=gens[0]; t={}; x=1
            for e in range(o): t[x]=(e,); x=x*g%q
            tabs.append((q,t)); shape.append(o)
        else:  # 2^k, k>=3: ±5^e
            (_,o1),(g,o2)=gens; t={}; x=1
            for e in range(o2):
                t[x]=(0,e); t[(q-x)%q]=(1,e); x=x*g%q
            tabs.append((q,t)); shape+= [2,o2]
    return tabs, tuple(shape)
cache={}
def analyse(p,C):
    m=4*C; N=m*p+1; f=factorint(N); tau=1
    for e in f.values(): tau*=e+1
    ph=int(totient(m))
    divs=sympy.divisors(N)
    hit=sum(1 for d in divs if d%m==m-1)>0
    if tau<ph: return tau,ph,hit,False,False,None
    if m not in cache: cache[m]=dlog_tables(m)
    tabs,shape=cache[m]
    H=np.zeros(shape)
    for d in divs:
        idx=[]
        for q,t in tabs: idx+=list(t[d%q])
        H[tuple(idx)]+=1
    F=np.fft.fftn(H); l1=np.abs(F).sum()-abs(F.flat[0])
    cover=bool((H>0).all())
    return tau,ph,hit,cover,bool(l1<tau-1e-9),l1/tau
if __name__=="__main__":
    lo,hi,Cmax=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    extra=[int(x) for x in sys.argv[4].split(',')] if len(sys.argv)>4 else []
    ps=[p for p in primerange(lo,hi) if p%4==1]+extra
    from collections import Counter
    hist=Counter(); minC=Counter()
    tot=dict(primes=0,anyhit=0,anycover=0,anyBS=0,levels_eligible=0,levels_BS=0,levels_cover=0)
    rows=[]
    for p in ps:
        ah=ac=ab=False; first=None
        for C in range(1,Cmax+1):
            tau,ph,hit,cover,bs,r=analyse(p,C)
            ah|=hit
            if tau>=ph:
                tot['levels_eligible']+=1; tot['levels_cover']+=cover; tot['levels_BS']+=bs; ac|=cover; ab|=bs
                if bs: hist[C]+=1; first = C if first is None else first
        minC[first]+=1; tot['primes']+=1; tot['anyhit']+=ah; tot['anycover']+=ac; tot['anyBS']+=ab
        if p in extra: rows.append((p,ah,ac,ab))
    print(f"range [{lo},{hi}) p≡1(4) + extra, C≤{Cmax}:",tot)
    print('BS-certified levels by C:',sorted(hist.items())); print('least certifying C per prime (None = not certified):',sorted(minC.items(),key=lambda x:(x[0] is None, x[0] or 0)))
    for r in rows: print("extra p=%d: hit(C≤Cmax)=%s fullcover=%s BScert=%s"%r)
