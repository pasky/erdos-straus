"""Combine integer lift bounds on P-boxes with reviewed SE/ZL tables and tails."""
from z76_lift import *
import argparse
ap=argparse.ArgumentParser(); ap.add_argument('j0',type=int); ap.add_argument('j1',type=int); ap.add_argument('--explore',action='store_true'); args=ap.parse_args()
se=Path('data/se'); zl=Path('data/zl'); our=Path('data/z76')

def load(file,q):
    T={}
    for line in file.read_text().splitlines():
        if line[0]=='#': continue
        j,v,*_=line.split(); j=int(j); v=Fraction(Decimal(v))*(1+Fraction(1,10**9)); assert v>=0 and j not in T; T[j]=ceildiv(v.numerator,v.denominator)
    return q,T
P=[load(se/'P_q4.txt',4),load(se/'P_q1.txt',1),load(zl/'P_q1_hi.txt',1)]
Q=[load(se/'Q_q4.txt',4)]

def tab(tables,i): # i in units 1/32 bit; tables have widths 1/q bits
    return min(T[j] for q,T in tables if (j:=i*q//32) in T)

@lru_cache(None)
def p(i):
    old=2*tab(P,i)
    b=i//32+1
    return min(old,boxes(b)[0]) if b<=100 else old

def edge(j): return rootup(1<<j,32)

def l1(j):
    old=j>=672; path=zl/'sweep_21.txt' if old else our/f'l1_{j//32}.txt'
    rows=[list(map(int,l.split()[1:])) for l in path.read_text().splitlines() if l.startswith('C ')]
    [(idx,lo,hi,pm,qm,ms,cnt)]=[row for row in rows if row[0]==j]
    assert lo in (edge(j),edge(j)|1) and hi==edge(j+1) and 0<cnt and 0<=max(pm,qm)<=ms<=pm+qm and max(pm,qm)<65535
    ady=2*sum(300//a for a in range(1,301)) if old else 0
    return 2*(ms+ady)

def check(j):
    r=edge(j); total=Fraction(l1(j),r); parts=[total]
    for tables,cap,ordr,mode in [(P,800,lambda k:(k+1)//2,'P'),(Q,100,lambda k:k,'Q')]:
        # Bound all terms below tail cutoff (partial cells included); infinite tails added separately.
        for k in range(3,2001,2):
            if k*j>=32*cap: break
            count=max((p(i) if mode=='P' else 2*tab(tables,i)) for i in range(k*j,min(k*(j+1),32*cap)))
            term=Fraction(count,r**ordr(k)); total+=term
            if k==3: parts.append(term)
        else: raise ValueError('tail cutoff')
    # Summed after *actual* first r^k above each cutoff. See note §4 (r>=4096).
    total+=Fraction(16,100*isqrt(r))+Fraction(1,25000)
    return total,parts

assert 384<=args.j0<=args.j1<=685
worst=Fraction(); fails=[]
for j in range(args.j0,args.j1+1):
    S,parts=check(j); r=edge(j); ok=S<Fraction(r-1,2*r)
    print(j,r,'ppm',ceildiv(10**6*S.numerator,S.denominator),*[round(float(v),5) for v in parts], 'ok' if ok else 'FAIL',flush=True)
    if not ok: fails.append(j)
    worst=max(worst,S)
print('last failing cell',max(fails,default=None),'max ppm',ceildiv(10**6*worst.numerator,worst.denominator))
if fails and not args.explore: sys.exit(1)
