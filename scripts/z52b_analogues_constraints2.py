# Enumerate ALL solutions 4/p = 1/x+1/y+1/z (x<=y<=z) for primes p = 1 mod 4 up to N,
# then test which constrained variants (constraint worlds) hold for every p.
import sys
from math import gcd, isqrt
from sympy import primerange, factorint
from itertools import product
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
def divs_from_f(f):
    ds=[1]
    for q,e in f.items():
        ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def sols(p):
    out=[]
    for x in range(p//4+1, 3*p//4+2):
        a=4*x-p; b=p*x
        if a<=0: continue
        g=gcd(a,b); a//=g; b//=g
        # a/b = 1/y+1/z, y<=z, y>=x : (a y - b)(a z - b) = b^2
        fb=factorint(b); f2={q:2*e for q,e in fb.items()}
        for d in divs_from_f(f2):
            if d> b: continue  # d<=b ensures y<=z
            if (d+b)%a: continue
            y=(d+b)//a; e=b*b//d
            if (e+b)%a: continue
            z=(e+b)//a
            if y<x: continue
            out.append((x,y,z))
    return out
def sqfree(n):
    return all(e==1 for e in factorint(n).values())
def s2s(n):
    return all(e%2==0 for q,e in factorint(n).items() if q%4==3)
tests_all={
 'distinct': lambda s: len(set(s))==3,
 'all_squarefree': lambda s: all(sqfree(t) for t in s),
 'all_sum_two_squares': lambda s: all(s2s(t) for t in s),
 'chain x|y|z': lambda s: s[1]%s[0]==0 and s[2]%s[1]==0,
 'one_den_prime': lambda s: any(len(factorint(t))==1 and max(factorint(t).values())==1 for t in s),
 'all_even': lambda s: all(t%2==0 for t in s),
 'exactly_one_even': lambda s: sum(t%2==0 for t in s)==1,
 'z<=p^2/2?': lambda s: max(s)<= 0,  # placeholder replaced below
 'x,y,z pairwise gcd>1': lambda s: gcd(s[0],s[1])>1 and gcd(s[1],s[2])>1 and gcd(s[0],s[2])>1,
 'y,z both divisible by p': lambda s: s[1]%P==0 and s[2]%P==0,
 'only z divisible by p': lambda s: s[2]%P==0 and s[0]%P and s[1]%P,
 'some den = 0 mod 4': lambda s: any(t%4==0 for t in s),
 'lcm(x,y,z) = z': lambda s: s[2]%s[0]==0 and s[2]%s[1]==0,
 'all cube-free': lambda s: all(max(factorint(t).values(),default=0)<3 for t in s),
 'x even': lambda s: s[0]%2==0,
 'AP (y-x=z-y)': lambda s: s[1]-s[0]==s[2]-s[1],
}
tests={k:tests_all[k] for k in ['all_sum_two_squares','chain x|y|z','all_even','lcm(x,y,z) = z','some den = 0 mod 4']}
tests['max<=p^2/8']=lambda s: max(s)*8<=P*P
tests['y,z both div p, x not']=lambda s: s[1]%P==0 and s[2]%P==0 and s[0]%P
tests['all den = 0 or 2 mod 3? none = 1 mod 3']=lambda s: all(t%3!=1 for t in s)
fails={k:[] for k in tests}
cnt=[]
for P in primerange(5,N):
    if P%4!=1: continue
    S=sols(P); cnt.append((len(S),P))
    for k,f in tests.items():
        if k.startswith('z<='): continue
        if not any(f(s) for s in S): fails[k].append(P)
for k,v in fails.items():
    if k.startswith('z<='): continue
    print(f"{k:28s} fails at {len(v):4d} primes; first: {v[:12]}")
cnt.sort(); print("fewest solutions:", cnt[:8])
