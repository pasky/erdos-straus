"""Z0409 side check: does the odd-square obstruction T1 (no Type I/II solutions at n = odd square) persist for m/n,
m ≥ 5?  Type I: n | x, gcd(n,y)=gcd(n,z)=1; Type II: n | y, n | z, gcd(n,x)=1 (ET convention).  Brute force over
all x<=y<=z (via (ay-b)(az-b)=b^2), any order of roles."""
from math import gcd, isqrt
from fractions import Fraction
def divisors(N):
    ds=[]; i=1
    while i*i<=N:
        if N%i==0: ds.append(i); ds.append(N//i)
        i+=1
    return ds
def sols(m,n):
    out=[]
    for x in range(n//m+1, 3*n//m+2):
        a=m*x-n
        if a<=0: continue
        b=n*x
        for d in divisors(b*b):
            if d>b or (b+d)%a or (b+b*b//d)%a: continue
            y=(b+d)//a; z=(b+b*b//d)//a
            if y>=x: out.append((x,y,z))
    return out
def types(n,s):
    t1=t2=0
    for tri in s:
        div=[v%n==0 for v in tri]; cop=[gcd(v,n)==1 for v in tri]
        if sum(div)==1 and all(cop[i] for i in range(3) if not div[i]): t1+=1
        if sum(div)==2 and all(cop[i] for i in range(3) if not div[i]): t2+=1
    return t1,t2
for m in range(4,17):
    row=[]
    for k in (3,5,7,9,11,13):
        n=k*k
        if gcd(n,m)!=1: row.append("  -  "); continue
        s=sols(m,n); t1,t2=types(n,s); row.append("%2d/%-2d"%(t1,t2))
    print("m=%2d  TypeI/TypeII counts at n=9,25,49,81,121,169: %s"%(m," ".join(row)))
