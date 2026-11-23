"""Small exact controls for z83 R2: signs, binary endpoint tests, bit-table law."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, prod


def divs(n):
    lo = [d for d in range(1,isqrt(n)+1) if n%d==0]
    return lo + [n//d for d in reversed(lo) if d*d!=n]


def jac(a, n):
    assert n>0 and n%2
    s=1; a %= n
    while a:
        while not a%2:
            a//=2
            if n%8 in [3,5]: s=-s
        if a%4==n%4==3: s=-s
        a,n=n%a,a
    return s if n==1 else 0


def chi(a,p):
    j=pow(a,(p-1)//2,p)
    return -1 if j==p-1 else j


def audit_words():
    stats=Counter()
    for p in range(97,30000,24):
        if len(divs(p))!=2: continue
        for t in range(2,89):
            by_div=set()
            for f in divs(t*p+1):
                if (f+1)%t: continue
                x=(f+1)//t; v=((t*p+1)//f+1)//t
                if x<2 or v<x: continue
                assert p==t*x*v-x-v and gcd(x,v)==1
                fo=f//(f & -f)
                sign=chi(x,p)*chi(v,p)
                assert sign==chi(f,p)==jac(-x,fo)
                assert sign==jac(-v,x//(x & -x))*jac(-x,v//(v & -v))
                assert t%4 or sign==-1
                by_div.add((x,v,sign));stats[bool(t%4),sign]+=1
            direct=set()
            for x in range(2,2+isqrt((p+2*isqrt(p)+2)//t)):
                f=t*x-1
                if (p+x)%f==0 and (v:=(p+x)//f)>=x:
                    direct.add((x,v,chi(x*v,p)))
            assert direct==by_div
    print('interior words (4|t negative, 4∤t negative, 4∤t positive):',stats[False,-1],stats[True,-1],stats[True,1])


def audit_seed():
    count=Counter()
    band=[17,19,23,29,31]
    for t in [4,8,12,16]:
        for p in range(241,40000,24):
            if len(divs(p))!=2:continue
            tags=[r for r in band if (p*t+1)%r==0]
            seeds=[a for a in [1,3,5,7,9,11] if gcd(a,t)==1]
            labels=[(a,prod(r for r,b in zip(tags,mask) if b)) for a in seeds for mask in product([0,1],repeat=len(tags)) if any(mask)]
            matched=[(a,d) for a,d in labels if d%t==(-pow(a,-1,t))%t]
            live=[(a,d) for a,d in matched if (p*t+1)%a==0]
            for a,d in live:
                f=a*d; g=(t*p+1)//f
                assert f*g==t*p+1 and f%t==g%t==t-1
                x=(f+1)//t; v=(g+1)//t
                assert x>=2 and p==t*x*v-x-v and chi(f,p)==-1
            count[bool(live),len(matched)==1]+=1
    print('binary windows (live, uniquely live, singleton inactive):',sum(c for (live,_),c in count.items() if live),count[True,True],count[False,True])


def audit_table():
    X=5500
    qset=[3,7,11,23,31,47]
    sh=sorted({0,9,14}|{(q+1)//4 for q in qset})
    primes={j for j in range(X,2*X+max(sh)) if len(divs(j))==2}
    bits=lambda n: tuple(n+h in primes for h in sh)
    population=range(X,2*X); law=Counter(bits(n) for n in population)
    # Prescribe the root rather than searching for a prime-bit pattern.
    witnesses=[min(divs(h+6)[1:]) for h in sh]
    s=5+8*prod(set(witnesses)-{2}); t=(s*s-1)//4
    assert t in population and all((t+h)%r==0 for h,r in zip(sh,witnesses))
    assert not any(bits(t))
    for q in qset:
        ds=[d for d in divs(t+(q+1)//4) if gcd(d,q)==1]
        assert all((d+e)%q for d in ds for e in ds)
    weights=Counter(n for n in population if any(bits(n)))
    weights[t]=sum(not any(bits(n)) for n in population)
    table=Counter()
    for n,c in weights.items():table[bits(n)]+=c
    assert law==table and sum(weights.values())==X
    # Transfer just a small fraction of the zero-fibre mass as well.
    thinned=Counter({n:F(1) for n in population}); delta=F(1,100)
    for n in population:
        if not any(bits(n)):
            thinned[n]-=delta; thinned[t]+=delta
    thintable=Counter()
    for n,c in thinned.items(): thintable[bits(n)]+=c
    assert thintable==law and sum(thinned.values())==X
    print('true bit-pattern rows, patterns, constructed square, full fibre units:',X,len(law),4*t+1,weights[t])


if __name__=='__main__':
    audit_words(); audit_seed(); audit_table()
