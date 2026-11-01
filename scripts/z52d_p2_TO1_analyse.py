# z52d pass2 TO1: analysis of the full-enumeration table produced by z52d_p2_TO1_es.c
# usage: uv run --with numpy python scripts/z52d_p2_TO1_analyse.py data/z52b/pass2/TO1/es_100000.tsv
import sys, math
from collections import Counter, defaultdict
import numpy as np
rows=[]
for l in open(sys.argv[1]):
    f=l.split()
    p,cnt,E,M,c3,c8=map(int,f[:6]); pat=(int(f[6])<<64)|int(f[7])
    rows.append(dict(p=p,cnt=cnt,E=E,M=M,c3=c3,c8=c8,pat=pat))
P=np.array([r['p'] for r in rows]); CNT=np.array([r['cnt'] for r in rows]); E=np.array([r['E'] for r in rows]); M=np.array([r['M'] for r in rows])
print("primes p = 1 mod 4 below", P.max()+1, " count", len(rows))
print("no-solution primes (should be 0):", int((CNT==0).sum()))
# Z0260: all denominators = 0 mod 3
f3=[r['p'] for r in rows if r['c3']==0]
print("Z0260 m=12 (all den = 0 mod 3) failures:", len(f3), "last 12:", f3[-12:])
print("   first 20:", f3[:20])
print("   failures above 8000:", [q for q in f3 if q>8000])
# Z0262: all even and some den = 0 mod 8
f8=[r['p'] for r in rows if r['c8']==0]
print("Z0262 (all den even, some den = 0 mod 8) failures:", len(f8), "last 15:", f8[-15:])
print("   failures above 8000:", [q for q in f8 if q>8000])
# 2-adic pattern analysis: for each sorted valuation triple code, count primes realising it
codes=[(a,b,c) for a in range(5) for b in range(5) for c in range(5)]
realised=Counter()
for r in rows:
    for code in range(125):
        if (r['pat']>>code)&1: realised[code]+=1
# for each code: realised by how many p, and max p missing it
print("Z0262 2-adic triples: code -> (#p realising, #p missing, largest p missing)")
for code in range(125):
    a,b,c=code//25,(code//5)%5,code%5
    if not (a<=b<=c): continue
    miss=[r['p'] for r in rows if not (r['pat']>>code)&1]
    if realised[code]==0 and not miss: continue
    if len(miss)>0 and realised[code]>0:
        print(f"   {(a,b,c)}: realised {realised[code]}, missing {len(miss)}, largest missing p={max(miss)}")
    elif realised[code]>0:
        print(f"   {(a,b,c)}: realised by all {len(rows)}")
# Z0263: M(p) vs p^{3/2}
lg=np.log(M)/np.log(P)
fails_cap=(M>P.astype(float)**1.5)
print("Z0263 primes with min-max-denominator > p^{3/2}:", int(fails_cap.sum()), "of", len(rows))
for lo,hi in [(0,20000),(20000,50000),(50000,100001)]:
    m=(P>=lo)&(P<hi)
    print(f"   p in [{lo},{hi}): frac M>p^1.5 = {fails_cap[m].mean():.3f}; median log M/log p = {np.median(lg[m]):.3f}; 90% quantile={np.quantile(lg[m],0.9):.3f}; max={lg[m].max():.3f}")
print("   liminf/limsup proxy: min log M/log p over p>=10^4:", round(float(lg[P>=10000].min()),3), " max:", round(float(lg[P>=10000].max()),3))
# Z0283/Z0284: E(p)=min(4x-p) ; compare with log p
print("Z0283/4 slice index E(p)=min(4x-p):")
for lo,hi in [(5,1000),(1000,10000),(10000,50000),(50000,100001)]:
    m=(P>=lo)&(P<hi)
    print(f"   p in [{lo},{hi}): median E={np.median(E[m]):.0f}, 90%={np.quantile(E[m],0.9):.0f}, max={E[m].max()} at p={P[m][E[m].argmax()]}, mean E/log p={np.mean(E[m]/np.log(P[m])):.2f}, max E/ (p^{0.5}) = {(E[m]/np.sqrt(P[m])).max():.3f}")
big=np.argsort(-E)[:8]
print("   largest E(p):", [(int(P[i]),int(E[i])) for i in big])
print("   E(p) record values (p, E) for E > (record so far):")
rec=0; recs=[]
for p,e in zip(P,E):
    if e>rec: rec=e; recs.append((int(p),int(e)))
print("   ", recs[-15:])
# Z0294: log count, Erdos-Kac-type test
lc=np.log(CNT); LL=np.log(np.log(P))
print("Z0294 log #ES(p): mean", round(float(lc.mean()),3), " var", round(float(lc.var()),3))
for lo,hi in [(5,10000),(10000,50000),(50000,100001)]:
    m=(P>=lo)&(P<hi)
    print(f"   p in [{lo},{hi}): mean log#={lc[m].mean():.3f}, var={lc[m].var():.3f}, mean #={CNT[m].mean():.1f}, mean(#)/log^2 p={np.mean(CNT[m]/np.log(P[m])**2):.3f}, mean(#)/log p={np.mean(CNT[m]/np.log(P[m])):.3f}, 2*loglog p={2*np.mean(LL[m]):.3f}")
# Z0295: isolated-vertex (zero-count) fraction vs Poisson prediction with mean lambda(p)
print("Z0295 zero-count fraction vs Poisson:")
for lo,hi in [(5,5000),(5000,20000),(20000,50000),(50000,100001)]:
    m=(P>=lo)&(P<hi)
    lam=CNT[m].mean()
    print(f"   [{lo},{hi}): mean #={lam:.1f}, observed P(#=0)={np.mean(CNT[m]==0):.4f}, Poisson-mean-matched e^-lam={math.exp(-lam):.2e}; P(#<=2) obs={np.mean(CNT[m]<=2):.4f}")
print("   primes with #=1 (up to 10^5):", [int(p) for p in P[CNT==1]][:20], "count", int((CNT==1).sum()))
print("   primes with #<=3, max p:", int(P[CNT<=3].max()) if (CNT<=3).any() else None)
