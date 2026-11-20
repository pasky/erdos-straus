"""Certify at individual primes. All inequalities in integer/rational arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal
from functools import lru_cache
z=Path('data/z77'); se=Path('data/se'); zl=Path('data/zl')
def rows(p):return [list(map(int,s.split())) for s in p.read_text().splitlines()]
def tab(p,q):
    a={}
    for l in p.read_text().splitlines():
        if l.startswith('#'):continue
        j,v,*_=l.split();v=F(Decimal(v))*(1+F(1,10**9)); assert v>0 and int(j) not in a
        a[int(j)]=-(-v.numerator//v.denominator)
    return q,a
P=[tab(se/'P_q4.txt',4),tab(se/'P_q1.txt',1),tab(zl/'P_q1_hi.txt',1),tab(zl/'P_q32.txt',32)]
Q=[tab(se/'Q_q4.txt',4),tab(zl/'Q_q32.txt',32)]
Rt={b:v for b,j,v in rows(z/'routes.txt')}
Fine={b:v for b,j,v in rows(z/'fine.txt')}; Qt={b:v for b,i,v in rows(z/'q.txt')}
L={r:(p,q,c) for r,p,q,c in rows(z/'level1.txt')}; S={r:ss for r,*ss in rows(z/'p3.txt')}
isprime=lambda r: r>=2 and all(r%p for p in range(2,isqrt(r)+1))
assert set(L)=={r for r in range(17,181392) if isprime(r)}
assert set(S)=={r for r in L if r<=50000}
for r,t,s,*_ in rows(zl/'level1_survivors.txt'):
    if r>=17:assert L[r][-1]==t-s

def bound(T,n):
    # binary logarithms by powering rather than libm
    vals=[2*a[j] for q,a in T if (j:=(n**q).bit_length()-1) in a]
    if T is P:
        b=n.bit_length(); vals+=[v for bb,v in Rt.items() if bb>=b and bb<=b+5]
        if b in Fine: vals.append(Fine[b]) # restricted to this octave
    elif n.bit_length() in Qt: vals.append(Qt[n.bit_length()])
    assert vals and min(vals)>0
    return min(vals)

def ppm(v):return -(-(v*1000000).numerator//(v*1000000).denominator)

def budget(r):
    # Simultaneous tail bound (z76 §4).
    ps=[];qs=[]
    for T,cap,ls in [(P,800,ps),(Q,100,qs)]:
        for k in range(3,801,2):
            n=r**k
            if n>=1<<cap:break
            ct=bound(T,n)
            if k==3 and T is P and r in S:
                for j,s in enumerate(S[r]):
                    e=r<<j; t=(n//e+1)//2; full,rem=divmod(t,r)
                    ct=min(ct,s+2*(full*((r-1)//2)+min(rem,(r-1)//2)))
            ls.append(F(ct,r**((k+1)//2 if T is P else k)))
    return [F(L[r][-1],r),ps[0],qs[0],ps[1],sum(ps[2:]),sum(qs[1:]),F(16,100*isqrt(r))+F(1,25000)]

if __name__=='__main__':
    groups={}; fails=[]; stats=[]
    for r in L:
        if not 4096<=r<177505:continue
        part=budget(r); v=sum(part); ok=v<F(r-1,2*r)
        if not ok:fails.append(r)
        stats.append((r,v)); key=r.bit_length(); groups[key]=max(groups.get(key,(0,)),(v,r,part))
    for k,(v,r,part) in groups.items():print(k,r,ppm(v),*[ppm(x) for x in part]);
    last=max(fails,default=4095); print('last failure',last,'first certified prime',min(r for r,v in stats if r>last),'maximum ppm after last failure',max(ppm(v) for r,v in stats if r>last))
