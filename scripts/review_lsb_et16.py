# R136 from-scratch: enumerate all solutions 4/n = 1/x+1/y+1/z (x<=y<=z) and classify Type I/II (ET defs,
# up to permutation) for odd squares and a few primes. Checks ET Prop 1.6 numerically.
from math import gcd
def sols(n):
    out=[]
    for x in range(n//4+1, 3*n//4+1):
        # 4/n - 1/x = (4x-n)/(nx)
        a, b = 4*x-n, n*x
        if a<=0: continue
        for y in range(max(x, b//a+1), 2*b//a+1):
            num, den = a*y-b, b*y
            if num<=0: continue
            if den % num==0:
                z=den//num
                if z>=y: out.append((x,y,z))
    return out
def typ(n,s):
    t=set()
    for i in range(3):
        a=s[i]; o=[s[j] for j in range(3) if j!=i]
        if a%n==0 and gcd(n,o[0]*o[1])==1: t.add('I')
        if o[0]%n==0 and o[1]%n==0 and gcd(n,a)==1: t.add('II')
    return t
for m in [3,5,7,9,11,13,15]:
    n=m*m; S=sols(n); cI=sum('I' in typ(n,s) for s in S); cII=sum('II' in typ(n,s) for s in S)
    print(f"n={n}: #sol={len(S)} typeI={cI} typeII={cII}")
for p in [29,41,53,73,97]:
    S=sols(p); print(f"p={p}: #sol={len(S)} allI/II={all(typ(p,s) for s in S)}")
