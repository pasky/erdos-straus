"""Choose matched units for costly exact R8 counts using anchor IDs only.
Also summarize the counts when supplied; thresholds refer to ordered R8."""
from collections import defaultdict
from hashlib import sha256
from statistics import median
from pathlib import Path
import sys

D = Path(sys.argv[1]); arms = defaultdict(dict)
for l in (D/'match.txt').read_text().splitlines():
    if not l.startswith('#'):
        tag,p,n,*_ = l.split(); arms[tag][int(p)] = int(n)
selected = []
for group in [('sm+','sm-','rough+','rough-'), ('sq','sq_ctl')]:
    for j in range(1,7):
        # Keep all selected n below 7e12 for inherited factor table capacity.
        ids = [p for p in arms[group[0]] if p//10**12 == j]
        chosen = sorted(ids, key=lambda p:sha256(str(p).encode()).digest())[:8]
        assert len(chosen)==8
        for p in chosen:
            for t in group:
                selected.append((t,p,arms[t][p]))
if len(sys.argv)==2:
    for _,_,n in selected:print(n)
else:
    counts,ws={},defaultdict(set)
    for l in (D/'subfactor.txt').read_text().splitlines():
        if l.startswith('W '):
            _,n,u,b,c=l.split();n,u,b,c=map(int,(n,u,b,c))
            assert 8*u*b*c-u-b==n and 1<=u<=b and c>=1 and (u,b,c) not in ws[n]
            ws[n].add((u,b,c))
        else:
            n,lab,kind,num=l.split(); n=int(n)
            assert lab=='unordered' and kind=='R8' and n not in counts
            assert len(ws[n])==int(num)>0
            counts[n]=2*int(num) # n odd, hence u != b
    assert counts.keys()=={n for _,_,n in selected}
    vals=defaultdict(dict)
    for t,p,n in selected:vals[t][p]=counts[n]
    print('subsample exact ordered R8 per arm: n sum min median <=20')
    for t,pv in vals.items():
        v=list(pv.values());print(t,len(v),sum(v),min(v),median(v),sum(x<=20 for x in v))
    for t,u in [('sm+','rough+'),('sm-','rough-'),('sm+','sm-'),('rough+','rough-'),('sq','sq_ctl')]:
        d=[x-vals[u][p] for p,x in vals[t].items()]
        print(t,u,'R8 less/equal/greater',sum(v<0 for v in d),d.count(0),sum(v>0 for v in d))
