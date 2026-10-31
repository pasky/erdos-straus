"""Z0663 Ramsey-ES: for fixed colourings c of N, does every prime p have a monochromatic solution
4/p = 1/x+1/y+1/z (x<=y<=z)?  All solutions enumerated exactly via (ay-b)(az-b)=b^2, a=4x-p, b=px."""
import sys, random
from math import isqrt
P=int(sys.argv[1])
LIM=P
spf=list(range(LIM+1))
for i in range(2,isqrt(LIM)+1):
    if spf[i]==i:
        for j in range(i*i,LIM+1,i):
            if spf[j]==j: spf[j]=i
def fac(n):
    f={}
    while n>1:
        q=spf[n]; f[q]=f.get(q,0)+1; n//=q
    return f
def sols(p):
    out=[]
    for x in range((p+3)//4, (3*p)//4+1):
        a=4*x-p
        if a<=0: continue
        b=p*x
        f=fac(x); f[p]=f.get(p,0)+1
        ds=[1]
        for q,e in f.items(): ds=[d*q**k for d in ds for k in range(2*e+1)]
        bb=b*b
        for d in ds:
            if d>b: continue
            if (b+d)%a: continue
            y=(b+d)//a; z=(b+bb//d)//a
            if (b+bb//d)%a: continue
            if y>=x: out.append((x,y,z))
    return out
def v2(n): return (n&-n).bit_length()-1
def omega_big(n):
    c=0
    while n%2==0: n//=2; c+=1
    q=3
    while q*q<=n:
        while n%q==0: n//=q; c+=1
        q+=2
    return c+(1 if n>1 else 0)
random.seed(7)
RC={}
def rnd(n,k,seed):
    key=(n,k,seed)
    if key not in RC: RC[key]=random.Random(hash(key)).randrange(k)
    return RC[key]
cols={
 'v2 parity': lambda n: v2(n)%2,
 'v2 mod 3': lambda n: v2(n)%3,
 'n mod 3': lambda n: n%3,
 'n mod 4': lambda n: n%4,
 'n mod 5': lambda n: n%5,
 'Liouville': lambda n: omega_big(n)%2,
 'Omega mod 3': lambda n: omega_big(n)%3,
 'rand2 s1': lambda n: rnd(n,2,1),
 'rand2 s2': lambda n: rnd(n,2,2),
 'rand3 s1': lambda n: rnd(n,3,1),
 'rand4 s1': lambda n: rnd(n,4,1),
 'floor log2 parity': lambda n: n.bit_length()%2,
 'floor log2 mod 3': lambda n: n.bit_length()%3,
}
isp=[True]*(P+1); isp[0]=isp[1]=False
for i in range(2,isqrt(P)+1):
    if isp[i]:
        for j in range(i*i,P+1,i): isp[j]=False
fails={k:[] for k in cols}; nsol=[]
for p in range(5,P+1):
    if not isp[p]: continue
    S=sols(p); nsol.append(len(S))
    for k,c in cols.items():
        if not any(c(x)==c(y)==c(z) for x,y,z in S): fails[k].append(p)
print("primes 5..%d; min #solutions %d"%(P,min(nsol)))
for k in cols: print("%-18s #fail %4d  largest fails %s"%(k,len(fails[k]),fails[k][-8:]))
