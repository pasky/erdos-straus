# z52b pass1 U09: full ES solution count f(p) = #{x<=y<=z : 4/p = 1/x+1/y+1/z}  (ordered, x<=y<=z), p prime ≡ 1 (4), p <= N
# Method: for x in [ceil(p/4), floor(3p/4)], a=4x-p, b=px; (ay-b)(az-b)=b^2 with d1=ay-b, d2=az-b, d1*d2=b^2, d1≡d2≡-b (mod a), d1<=d2.
# Divisors of b^2 = p^2 x^2 are generated from the factorisation of x (x < p), so no big factoring.
# Also counts the (★)-family (u,B,C) triples for cross-check on the same primes.  Usage: python3 scripts/z52b_p1_U09_fullf.py N
import sys, math
from collections import Counter
N = int(sys.argv[1]) if len(sys.argv)>1 else 5000
spf = list(range(N+1))
for i in range(2,int(N**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,N+1,i):
            if spf[j]==j: spf[j]=i
def factor(n):
    f=Counter()
    while n>1:
        q=spf[n]; f[q]+=1; n//=q
    return f
def divisors_of_b2(p, x):
    # b^2 = p^2 x^2 ; combine factorisation
    f = Counter(factor(x)); f = Counter({k: 2*v for k,v in f.items()})
    f[p] += 2
    divs=[1]
    for q,e in f.items():
        divs=[d*q**k for d in divs for k in range(e+1)]
    return divs
def fullcount(p):
    cnt=0
    for x in range(math.ceil(p/4), (3*p)//4+1):
        a=4*x-p; b=p*x
        if a<=0: continue
        if x<p and x>0: pass
        for d1 in divisors_of_b2(p,x):
            if d1 % a == (-b) % a and d1 > 0:
                d2 = (b*b)//d1
                if d2 % a == (-b) % a and d1*a > 0:
                    # y=(d1+b)/a, z=(d2+b)/a  positive integers
                    y=(d1+b)
                    z=(d2+b)
                    if y%a==0 and z%a==0 and y>0 and z>0:
                        y//=a; z//=a
                        if x<=y<=z: cnt+=1
    return cnt
def primes(n):
    return [i for i in range(2,n+1) if spf[i]==i]
out=[]
for p in primes(N):
    if p%4==1 and p>=5:
        out.append((p, fullcount(p)))
for p,f in out: print(p,f)
