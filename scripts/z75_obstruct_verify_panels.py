"""Verify stored witnesses as equations, independently of the generator and cap.
Finish five capped composite R8 rows, and print the small-shift factor profiles of records.
"""
from math import gcd,isqrt,prod
from pathlib import Path
from collections import Counter

D=Path('data/z75/obstruct')

def factors(n):
    ret=[]; i=2
    while i*i<=n:
        while n%i==0:
            ret.append(i);n//=i
        i=3 if i==2 else i+2
    return ret+([n] if n>1 else [])

sets={}; reps=Counter()
for line in (D/'panels.txt').read_text().splitlines()[1:]:
    kind,*vals=line.split();n,m,s,R,A,Z,T,E=map(int,vals)
    if kind=='N':assert n==m*m+s and isqrt(s+1)**2==s+1 and gcd(m,isqrt(s+1))==1
    if kind=='H':assert n==m+1
    if kind in 'DCK':assert n==s*m*m and isqrt(n)**2!=n
    if kind=='K':assert gcd(n,105)==1 and n%840 in (1,121,169,289,361,529)
    if E==0:
        for f in range(5000007,200000008,8):
            r=(-n)%f
            if r and (f+1)//8%r==0:
                E=f;break
        print('long',n,E,flush=True)
    for tag,f in zip('RAZTE',[R,A,Z,T,E]):
        assert f
        u=(-n)%f
        if tag=='A' and u==1:u=f+1
        b=(n+u)//f;t=(f+1)//u
        assert min(u,t,b)>=1 and n==t*u*b-u-b
        if tag=='R':assert t%4==0
        if tag=='A':assert u%4==0
        if tag=='Z':assert f%8==7 and (u%4==0 or t%4==0)
        if tag=='T':assert min(t,u,b)>=2 and (n+t)*t*u*b%8==0
        if tag=='E':assert t%8==0
    reps[kind]+=1;sets.setdefault(kind,set()).add(n)
for k in sorted(sets):print(k,'rows',reps[k],'distinct',len(sets[k]),'min',min(sets[k]),'max',max(sets[k]))
for p in (25277866681,25606400401,27112836481,28154878561,37165786681,39919266721,179530327201,452438542081):
    vals=[p-1,*[(p+t)//4 for t in (3,7,11,15)],*[t*p+1 for t in (4,8,12)]]
    print('record',p,p%840,[factors(v) for v in vals])
