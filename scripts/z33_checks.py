"""O263 quick checks: Prop 5.1(a) chi_{-4d}(l) = (l/p) for every prime l | p+4d (p ≡ 1 mod 4 < 20000, d <= 60);
Thm 3.4: forced rule (b=1 line, both coordinates, e-slices) fails at primes p ≡ 1 mod M (D=6, B=26)."""
from sympy import factorint, primerange, jacobi_symbol as J, isprime
from math import gcd, lcm, factorial
def kron(a,n):  # Kronecker (a/n) for odd n>0
    return J(a % n, n)
bad=0; cnt=0
for p in primerange(5,20000):
    if p%4!=1: continue
    for d in range(1,61):
        if d%p==0: continue
        for l in factorint(p+4*d):
            # chi_{-4d}(l) for odd prime l not dividing d: (−4d/l) = (−d/l)
            cnt+=1
            if kron(-d,l)!=J(l,p): bad+=1
print("Prop5.1(a) checks",cnt,"violations",bad)
D=6;B=26
M=lcm(4*factorial(D), *[q**e for q in primerange(2,B+1) for e in [next(k for k in range(1,60) if q**k>16*D*(D+1))]])
def sig(fs,t):
    S={1}
    for f in fs: S|={x*f%t for x in S}
    return S
def forced_set(N,t,signed=False):
    fs=[];L=1
    for q,e in factorint(N).items():
        if q<=B: fs+=[q]*e
        else: L*=q**e
    fs=[f for f in fs if gcd(f,t)==1]
    if L>1: fs.append(L)
    if not signed: return sig(fs,t)
    S={1}
    for f in fs: S|={x*f%t for x in S}|{x*pow(f,-1,t)%t for x in S}
    return S
fired=0; tested=0; k=1
while tested<20:
    p=1+M*k; k+=1
    if not isprime(p): continue
    tested+=1
    for d in range(1,D+1):
        if 4*d-1 in forced_set(p+4*d,4*d): fired+=1
    for c in range(1,D+1):
        N=c*p+1
        if 4*c-1 in forced_set(N,4*c): fired+=1
    for e in range(3,D+1,4):
        for N in ((p+e)//4,(p*e+1)//4):
            if e-1 in forced_set(N,e,True): fired+=1
print("Thm3.4: M =",M,"primes tested",tested,"forced firings",fired)
