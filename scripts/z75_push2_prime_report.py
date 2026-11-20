"""Independently validate all reported word witnesses and AP exact hits. Descriptive matched rates.
`FIRST F` denotes the scanning convention, not a necessary lower bound for (S).
"""
from collections import defaultdict
from math import isqrt
from pathlib import Path
import sys
from z75_obstruct_controls import full8

D=Path(sys.argv[1]) if len(sys.argv)>1 else Path('data/z75/push2prime')

def smooth(n):
    for q in range(2,62):
        while n%q==0:n//=q
    return n==1

def isp(n):
    # Deterministic strong MR first nine prime bases, sufficient for n<3e18.
    assert 2<n<10**16
    d=n-1;s=0
    while not d&1:d//=2;s+=1
    for b in (2,3,5,7,11,13,17,19,23):
        t=pow(b,d,n)
        if t==1:continue
        for _ in range(s):
            if t==n-1:break
            t=t*t%n
        else:return False
    return True

def profile(n):
    m=n;d=2;fac=[]
    while d*d<=m:
        while m%d==0:fac.append(d);m//=d
        d=3 if d==2 else d+2
    return fac+([m] if m>1 else [])

def main():
    records=list(map(int,(D/'records.txt').read_text().split()));hard=set()
    for f in ['r8a','r8b','r8c','A','Ab','Aall','Rall']:
        for l in (D/(f+'.txt')).read_text().splitlines():
            el=l.split()
            if el[0]=='H':
                n,a,b,c=map(int,el[1:]);k=8 if f.startswith('r8') else 4
                assert min(a,b,c)>0 and k*a*b*c-(4 if f.startswith('A') else 1)*a-b==n and isp(n)
                hard.add(n)
            elif el[0]=='MISS':
                assert f.startswith('r8') and int(el[1]) in records;hard.add(int(el[1]))
            else:assert el[0]=='#'
    rows=defaultdict(list)
    for file in ['hard','panels']:
        for l in (D/(file+'.txt')).read_text().splitlines()[1:]:
            tag,*v=l.split();p,n,R,A,Z,S,E=map(int,v);assert isp(n)
            for code,f in zip('RAZSE',(R,A,Z,S,E)):
                if code=='E' and tag=='hard':continue
                assert f>0,(n,code)
                u=(-n)%f
                if code=='A' and u==1:u=f+1
                b=(n+u)//f;t=(f+1)//u
                assert n==t*u*b-u-b and min(t,u,b)>0
                if code=='R':assert not t%4
                if code=='A':assert not u%4
                if code=='E':assert not t%8
                if code=='Z':assert f%8==7 and (u%4==0 or t%4==0)
                if code=='S':assert min(u,b,t)>=2 and (n+t)*u*b*t%8==0
            rows[tag].append((p,n,R,A,Z,S,E))
            if tag=='hard':continue
            assert 10**12<=n<9*10**12 and n%840==1
            sm=smooth(n-1);sq=isqrt(n-1)**2==n-1;sh=isp(12*n+1)
            if tag in ['sq','sq_ctl']:
                assert sq==(tag=='sq') and sm==smooth(p-1) and sh==isp(12*p+1)
            else:
                assert not sq and sm==tag.startswith('sm') and sh==(not tag.endswith('-'))
                if tag.startswith('shift'):
                    assert isp((n+3)//4)==isp((n+7)//8)==(tag=='shift3')
    assert set(x[1] for x in rows['hard'])==hard
    print('hard unique',len(hard),'max f R A U7 S',*[max(x[j] for x in rows['hard']) for j in range(2,6)])
    print('family rows | max distance to anchor | first f>1000 R A U7 S R8 (numerators; divide by rows) | max f R8')
    for tag,arr in rows.items():
        if tag=='hard':continue
        assert len(set(r[1] for r in arr))==len(arr)
        print(tag,len(arr),max(abs(r[1]-r[0]) for r in arr),*[sum(r[j]>1000 for r in arr) for j in range(2,7)],max(r[6] for r in arr))
    for a,b in [('sm+','sm-'),('sm+','rough+'),('sm-','rough-'),('shift3','shift1'),('sq','sq_ctl')]:
        x,y=rows[a],rows[b];assert [r[0] for r in x]==[r[0] for r in y];print('paired first f_R8>1000',a,b,'10',sum(r[6]>1000>=s[6] for r,s in zip(x,y)),'01',sum(s[6]>1000>=r[6] for r,s in zip(x,y)))
    for n in records:
        a,b,c,d=full8(n);assert 8*a*b*c*d==a+b+n*c
        print('record',n,'mod840',n%840,'p-1',profile(n-1),'12p+1',profile(12*n+1),'full8',a,b,c,d)

if __name__=='__main__':main()
