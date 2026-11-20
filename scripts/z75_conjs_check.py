"""Independent integer checks of the new identities (no PARI)."""
from math import gcd
from fractions import Fraction
from collections import defaultdict,Counter
from pathlib import Path
import json

def thin(s):
    n=15*2**s+1; m=s
    while m%3==0:m//=3
    r=m if m%3==2 else m//5
    assert r%3==2 and s%(3*r)==0 and (s//(3*r))%2
    x=2**r;A=x*x-x+1;t=(A+1)//14;v=(n+14)//A
    assert A==t*14-1 and n==v*A-14 and min(t,v)>=2 and (n+t)%8==0
    B=t*v-1;assert B%4==0;D=B//4
    X,Y,Z=A*D*n,14*D,14*A*D
    assert 4*X*Y*Z==n*(X*Y+X*Z+Y*Z)

if __name__=='__main__':
    ss=sorted({60*j for j in range(1,101)}|{60*3**5,60*3**6})
    for s in ss: thin(s)
    print('integer cross multiplications',len(ss),'max s',max(ss))
    for r in [265,321,769,825]:
        for n in range(r,100001,840):
            t=(n+15)//56; assert t*56-15==n and t>=2 and (n+t)*t*56%8==0
    print('four residue witnesses verified <=100000')
    for tag in ('W1','W2','F2','F3','F4'):
        cs=defaultdict(lambda:[0,0,Fraction()]); dcounts=Counter()
        for line in Path('data/z75/conjs/'+tag+'.jsonl').read_text().splitlines():
            R=json.loads(line);d=R['d'];n=R['n']
            for (a,b,c),h,g,k in R['out'][0]:
                assert b*b-4*a*c==-4*n*d
                gap=a-abs(b);star=gap==1 and (a+1)%(4*d)==0
                if star:
                    A=a;B=(4*n*d+1)//A;s1=(A+1)//(4*d);s2=(B+1)//(4*d)
                    assert A*B==4*n*d+1 and 4*s1*s2*d==n+s1+s2 and h
                z=cs[star];z[0]+=1;z[1]+=h;z[2]+=Fraction(g,k)
            if R['anchor'] is None:dcounts['no-anchor']+=1
            if R['ac'] is None:dcounts['no-rep']+=1
        print(tag,dict(cs),dict(dcounts))
