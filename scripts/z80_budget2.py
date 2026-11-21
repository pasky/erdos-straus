"""Unsaturated global and conditional ledgers. xreview extra P9 rows are now replayed."""
from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):from z80_xr_extend import *
from z80_mid import band
from math import ceil
from z79_r2budget import short as prev
from z78_r2ledger import globalP
import z79_pbudget as old
@lru_cache(None)
def mid(n,j):
    s=prev(n,j)
    for i in range(max(2,(rootup((n+(1<<j))//4,3)-1).bit_length()),j):
        if i>=j-4 or i==(rootup((n+(1<<j))//4,3)-1).bit_length():s=min(s,mid(n,i)+ceil(band(n,i,j)))
    return s
def seed(r,k,j,c):
    v=spbig.setdefault((r,k),[]);seeds[r**k]=r,k,v
    while len(v)<=j:v.append(r**((k+1)//2))
    v[j]=min(v[j],c)
for r,k,*v in readrows(Path('data/z80/crush2/shift33.txt'))+readrows(Path('data/z80/crush2/shift35.txt')):
    for j,c in enumerate(v):seed(r,k,j,c)
from collections import defaultdict
chunks=defaultdict(list)
for r,j,off,size,c in readrows(Path('data/z80/crush2/p11.txt')):chunks[r,j].append((off,size,c))
for (r,j),vs in chunks.items():
    pos=cnt=0
    for off,size,c in sorted(vs):assert off==pos;pos+=size;cnt+=c
    assert pos==2**(j-2);seed(r,11,j,cnt)
prev.cache_clear();old.sh=mid

def analyze(r):
    x,_,_,q,pt,qt=row(r); P=[]
    for k in range(7,2001,2):
        if r**k>=1<<320:break
        p=cost(r,k,F(1))[0] # at full mass the split's coefficient is an unconditional first-centre cap
        if r in low and k in (7,9):
            s,t,u,o,_=low[r];p=F(s,r**4) if k==7 else F(t+u-o,r**5)
        P.append((p,'P'+str(k)))
    Qs=[]
    for k in range(5,1000,2):
        f=r**k;b=f.bit_length()
        if b>=80:break
        if k!=5 or r not in low:Qs.append((min(F(1),F(Q.get(b,f),f),F(qLocal.get(r,f),f) if k==5 else F(1)),'Q'+str(k)))
    assert sum(s for s,_ in Qs)==q
    if r==17:
        tr=Path('data/z78/exact/rtree17_d8.txt').read_text();import re
        lifts=[list(map(int,re.findall(r'd(\d+): new (\d+)',s)[0])) for s in tr.split('cell C_7')[0].splitlines() if 'new ' in s];assert len(lifts)==7
        x=F(2,r);P=[(F(2*c,r**i),'PQ'+str(i)) for i,c in lifts]+[(p,n) for p,n in P if int(n[1:])>=17];Qs=[(p,n) for p,n in Qs if int(n[1:])>=9]
    costs=P+Qs+[(pt,'Pt'),(qt,'Qt')];total=sum(z for z,_ in costs);big,who=max(costs);m=x-total
    # Use the stronger of this unconditional table and the monotone parent update, but report the raw deficit too.
    a,p,t,q,h,u=row(r);m=max(m,a-sum(p)-q-h-u)
    return x,total,big,who,m,P,Qs,pt,qt

def cells(r):
    D=Path('data/z78/exact');read=lambda s:set(map(int,(D/f'r{r}_{s}.txt').read_text().split()));bad=read('p1')|read('q1')|{i*i%r for i in range(r)};d2=read('p3');d3=read('p5')|read('q3');
    # Sparse exact complement at depth 3: finer hits above dead prefixes never count.
    from collections import Counter
    l=Counter(x%(r*r) for x in d3 if x%r not in bad and x%(r*r) not in d2);d={a:r-l[a] for a in range(r*r) if a%r not in bad and a not in d2};return d

def choose(r,total,prefix):
    d=cells(r);assert F(sum(d.values()),r**3)==prefix
    # best signed margin over all first and second digits, counting inversion partners only once; no proportional allocation
    best=None
    for j in (1,2):
        from collections import Counter
        m=r**j;h=Counter()
        for a,v in d.items():h[a%m]+=v
        for b,v in h.items():
            inv=pow(b,-1,m);pair=1+(b!=inv);assert v==h[inv]
            margin=F(v,r**(3-j))-total*m/pair
            key=(margin,-j,-b)
            if best is None or key>best:best=key
    return best
if __name__=='__main__':
 for r in sorted(r for r in small if 17<=r<=83):
    x,total,big,who,m,P,Q0,pt,qt=analyze(r);init=row(r)[0]
    if r==17: # whole first-digit pair, measured through depth eight; for the second digit route use only the exact depth-three prefix
        later=total-sum(z for z,n in P if n.startswith('PQ'));c,j,b=choose(r,total-F(2,r)+init,init);prefix8=x-(total-later);better=F(17,2)*(prefix8-later);c,j,b=max((c,j,b),(better,-1,-5))
    else:c,j,b=choose(r,total,init)
    print('row',r,m*1000000//1,who,ppm(big),(x-total)*1000000//1,-j,-b,c*1000000//1,m,c,flush=True)
    if r==17:
        tail=sum(z for z,n in P if n.startswith('P') and not n.startswith('PQ') and int(n[1:])>=29)+sum(z for z,n in Q0 if int(n[1:])>=15)+pt+qt
        print('local14',17**14,ceil((17**14)*tail/2),(17**14)*tail/2,flush=True)
