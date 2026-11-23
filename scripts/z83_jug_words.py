"""Divisor enumeration for the fixed middle levels of Section 5; not a
search for unrestricted words. 2,3 genus criteria have different domains.
"""
from pathlib import Path
from z83_jug_dyadic import prime, divisors, factors

def row(p):
    assert p%4==1 and prime(p)
    counts=[]
    for m in [2,3,4,6,8,12,24]:
        N=m*p+1;count=0
        for a in divisors(N):
            b=N//a
            if a>b or a<2*m-1 or (a+1)%m:continue
            assert (b+1)%m==0
            r=(a+1)//m;t=(b+1)//m
            assert m*r*t-r-t==p
            neg=pow(r*t,(p-1)//2,p)==p-1
            assert neg==(pow(a,(p-1)//2,p)==p-1)==any(v%4==0 for v in [r,t,m,a,b])
            count+=neg
        hit=count>0; fs=list(factors(N))
        if m==2:assert hit==any(l%8 in [5,7] for l in fs)
        if m==3 and p%8==1:assert hit==any(l>2 and l%3==2 for l in fs)
        if m==6:
            B={1}
            for l in fs:B|={b*l%24 for b in B}
            assert hit==(17 in B)==(23 in B)
        counts.append(count)
    return counts

if __name__=='__main__':
    star=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and s[0].isdigit()]
    other=[17,37,241,2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929,1590284203561,6955940568721]
    print('p #good interior words (up to reversal) at middle 2 3 4 6 8 12 24')
    for p in star+other:
        n=row(p);print(p,*n)
        if p in star:assert n[2]==n[4]==n[5]==n[6]==0
        if p in other[-2:]:assert n[4]==n[6]==0
