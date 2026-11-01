"""SMN failures vs ticket count: size-matched (±10%) quantile of |SMN(p)|/sqrt p and |SM(p)|/sqrt p among primes p ≡ 1 (8)
in the census output files (z53_forestclass_forest lines).  Usage: uv run python scripts/z53_forestclass_smnquantile.py census...
Output recorded in Z53_FORESTCLASS.md §5 (census files are not stored: 500 MB; regenerate per §9)."""
import sys, bisect
fails=set(map(int,"193 457 1873 2377 2521 3361 9601 12433 19441 27073 42697 62497 129193 198937 219433 294793 360193 455953 467713 481153 595081 762721 874729 981481 1932001 2057113 2178313 3097537 3823177 5552737 5828593 5900953 6270793 9451513 10049713 12570721 12943393 16433113 19306057 20072497 20880553 22711753 51703633 57360697 59774233 89954593 93727657 98719993".split()))
P=[];V=[];W=[]
for fn in sys.argv[1:]:
    for line in open(fn):
        t=line.split(); n=int(t[0][2:])
        if n%8!=1: continue
        d={x.split('=')[0]:x.split('=')[1] for x in t if '=' in x and x.split('=')[0] in ('SM','SMN')}
        P.append(n); V.append(int(d['SMN'].split('/')[0])/n**0.5); W.append(int(d['SM'].split('/')[0])/n**0.5)
idx=sorted(range(len(P)),key=lambda i:P[i]); P=[P[i] for i in idx]; V=[V[i] for i in idx]; W=[W[i] for i in idx]
qs=[];qw=[]
for i,p in enumerate(P):
    if p not in fails: continue
    lo=bisect.bisect_left(P,p*0.9); hi=bisect.bisect_right(P,p*1.1)
    win=[V[j] for j in range(lo,hi) if P[j] not in fails]; winw=[W[j] for j in range(lo,hi) if P[j] not in fails]
    if not win: continue
    q=sum(1 for x in win if x<V[i])/len(win); qq=sum(1 for x in winw if x<W[i])/len(winw)
    qs.append(q); qw.append(qq)
print("n fails",len(qs),"mean quantile |SMN|/sqrt p:",sum(qs)/len(qs)," mean quantile |SM|/sqrt p:",sum(qw)/len(qw))
print("quantiles SMN:",' '.join(f"{x:.2f}" for x in qs))
print("count <= 0.05:", sum(1 for x in qs if x <= 0.05), "count <= 0.10:", sum(1 for x in qs if x <= 0.10))
