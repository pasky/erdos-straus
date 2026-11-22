"""Finite windows, no primality library. Exact square/numerator/composite falsifiers;
output kept small. All factorizations by trial division. Run from repo root.
"""
from math import gcd,isqrt,prod
from pathlib import Path

def factor(n):
    F=[];d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0: n//=d;a+=1
            F.append((d,a))
        d+=1 if d==2 else 2
    if n>1:F.append((n,1))
    return F
def ds(F):
    D=[1]
    for q,e in F:D=[u*q**j for u in D for j in range(e+1)]
    return D
def symbol(a,k):
    return prod((1 if pow(a,(q-1)//2,q)==1 else -1)**e for q,e in factor(k) if q%2) if gcd(a,k)==1 else 0
def isprime(n):return n>=2 and factor(n)==[(n,1)]
def witness(n,x,M):
    k=M*x-n;s=n*x;d=gcd(k,s);k//=d;s//=d
    # (k y - s)(k z - s) = s^2, both factors positive
    freq={}
    for t in {q for q,_ in factor(n)+factor(x)}:
        v=0;h=s
        while h%t==0:h//=t;v+=1
        if v:freq[t]=2*v
    for e in ds(freq.items()):
        if e<=s and (s+e)%k==0 and (s+s*s//e)%k==0:
            y=(s+e)//k;z=(s+s*s//e)//k
            if x<=y<=z:return (x,y,z)
    return None
def gap(n,M=4):
    for x in range(n//M+1,3*n//M+1):
        w=witness(n,x,M)
        if w:return M*x-n,w
    return None
def genus(p):
    q=next(t for t in range(2,p) if pow(t,(p-1)//2,p)==p-1)
    for k in range(3,p,4):
        ch=[f for f in ds([(t,1) for t,e in factor(k)]) if f%4==3]
        if all(any(symbol(t,f)==-1 for t,e in factor((p+k)//4)) for f in ch):return q,k
def fg7(p):
    F=factor((p+7)//4)+[(p,1)];S={t%7 for t,e in F};cnt=sum(e for t,e in F if t%7 in (3,5))
    return 6 not in S and (cnt==0 or cnt<=2 and not S.intersection((2,4)))
if __name__=='__main__':
    Z=[105,1465,3865,4545,10305,12145,39361,67425];stars=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and s[0]!='#']
    print('F1',9,4,witness(9,4,4)); print('F2 no positive 8-triple:',[(n,gap(n,8)) for n in (11,17,131,241)])
    print('F3/F4/F2large: n g triple; prime only: least_NR Kgen')
    for n in Z+stars+[17401609,1590284203561,6955940568721]:
        print(n,gap(n),genus(n) if isprime(n) else '-')
    tot=0
    for p in range(13,50000,4):
        if not isprime(p):continue
        packet=witness(p,(p+7)//4,4) is None;assert fg7(p)==packet
        if p%8==1:assert packet==all(t%7 in (1,2,4) for t,e in factor((p+7)//4))
        tot+=1
    print('k7 exact profile agrees with literal factor search on primes 13..50000, p=1 mod4:',tot)
    for p in (47161,349801):print('profile',p,gap(p),genus(p))
    # One quadratic forcing the first four misses, with a planted hit at 19.
    D,C,T=2731,450450,11329;Ws=(391,259,209,181)
    assert all(C+D*k==k*w*w for k,w in zip((3,7,11,15),Ws));n=(T*T+C)//D
    assert n==47161 and T*T+C==n*D and gcd(T,prod(Ws))==1 and n%19+35%19==19 and ((n+19)//4)%35==0
    # Exact polynomial progression keeps this residue/primitive data; step need not be minimal.
    L=840*19*35*prod(Ws);a=D*L*L;b=2*T*L;c=n
    assert gcd(c,a*b)==1 and isprime(c); print('quadratic coefficients',a,b,c,'negative discriminant?',b*b-4*a*c<0,'g=19 seed',gap(c))
