"""Independent verifier. No generator imports. Intersect all candidate bad lifts
for every ordinary residue mod 176400, independently for each q and q digit.
Rows can be discarded for smaller E; never needs to factor the large windows.
"""
import gzip
import re
from functools import lru_cache
from itertools import groupby
from math import gcd, isqrt
from pathlib import Path
import numpy as np

ROOT=Path('data/z83/cap_pointwise')
P=[n for n in range(2,380) if not any(n%d==0 for d in range(2,isqrt(n)+1))]
base=np.array([n for n in range(1,176400,8) if all(pow(n,(s-1)//2,s)==1 for s in (3,5,7))])
assert len(base)==1260

def vj(n,s):
    i=0
    while n%s==0: i+=1; n//=s
    return i

@lru_cache(None)
def allowed(mod,res): return base%mod==res

def run(q,E,records):
    # -2: no restrictions on a hypothetical missing lift; -1: contradiction.
    req=np.full((q,1260),-2,np.int32)
    nr=[r for r in range(1,q) if r not in {x*x%q for x in range(1,q)}]
    for _,e,tag,u,v,m in records:
        assert e<=E and m%4==3 and gcd(u,v)==1
        hit=np.ones(1260,dtype=bool); exc=None
        if tag in ('D','I'):
            A=(m+1)//4; assert m%q==0 and 176400%(m//q)==0 and gcd(q,m//q)==1
            D=u; assert v==1
            rem=A; s=2
            while rem>1:
                if s*s>rem: s=rem
                a=vj(rem,s); rem//=s**a; j=vj(D,s); D//=s**j
                assert j<=2*a or s!=2 and a and not j%2 and j<=2*a+2*e
                s+=1
            assert D==1
            r=(-4*u)%m
            if tag=='I': r=pow(r,-1,m)
            c=r%q; f=m//q; hit=allowed(f,r%f)
        else:
            c=(-m)%q
            assert tag in ('plus','minus','N')
            val={'plus':4*u+1,'minus':u+4*v,'N':u+v}[tag]; assert val%m==0 and (tag!='plus' or v==1)
            U,V=u,v
            for s in (2,3,5,7,q):
                j=vj(U,s)-vj(V,s); U//=s**max(j,0); V//=s**max(-j,0)
                if not j: continue
                # b = valuation of K. Enumerate b=0,1,>=2 in the base
                # (at q, only b>=1, with the optional exclusion b>=2).
                # Test legality for ALL higher lifts, not just the least b.
                def ok(b):
                    l={'plus':j,'minus':2*b+j,'N':b+j}[tag]
                    return l>=0 and (l<=2*b or s!=2 and b>0 and l%2==0 and l<=2*b+2*e)
                good=[all(ok(b) for b in ([h] if h<2 else range(2,abs(j)+2*e+6))) for h in range(3)]
                if s==q:
                    assert good[1]; exc=m%(q*q) if not good[2] else None
                    continue
                mod=(4 if s==2 else 1)*s
                lo=allowed(mod,-m%mod); hi=allowed(mod*s,-m%(mod*s))
                hit &= ((~lo if good[0] else False)|(lo&~hi if good[1] else False)|(hi if good[2] else False))
            assert U==V==1
        assert c in nr
        row=req[c]; no=hit if exc is None else hit&(row!=-2)&(row!=exc)
        if exc is not None: row[hit&(row==-2)]=exc
        row[no]=-1
    assert (req[nr]==-1).all(),q
    return len(nr)*len(base)*q

if __name__=='__main__':
    rows=[list(map(int,l.split())) for l in (ROOT/'atlas.txt').read_text().splitlines()]
    assert [q for q,e,unused,size,n,top in rows]==P[4:]
    # Check the published table against the machine ledger, including row order.
    note=Path('notes/z83/CAP_POINTWISE.md').read_text()
    table=note.split('|q|cap bounds in the same order|\n|---|---|\n',1)[1].split('\n\n',1)[0]
    reported=[]
    for line in table.splitlines():
        m=re.fullmatch(r'\|([0-9,]+)\|([0-9,]+)\|',line); assert m
        qs,es=([int(j) for j in g.split(',')] for g in m.groups()); assert len(qs)==len(es)
        reported.extend(zip(qs,es))
    assert reported==[(q,e) for q,e,*_ in rows]
    total=0
    with gzip.open(ROOT/'witnesses.txt.gz','rt') as fh:
        def parse(l):
            q,e,t,u,v,m=l.split(); return int(q),int(e),t,int(u),int(v),int(m)
        groups=groupby(map(parse,fh),key=lambda a:a[0]); count=0
        for q,e,left,size,n,top in rows:
            key,items=next(groups); items=list(items)
            assert q==key and left==0 and size==len(base) and len(items)==n and max(i[-1] for i in items)==top
            count+=n; total+=run(q,e,items)
        assert next(groups,None) is None
    print('independently certified wheel rows',len(rows),'witness records',count,'logical CRT cells',total,'max cap',max(x[1] for x in rows))
