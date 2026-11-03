# z55 TDCAL falsifier inputs: generic primes and special shapes near 10^10 (U = floor(p^{1/4}) ~ 316).
import sys, random
from sympy import isprime, nextprime
out = sys.argv[1]
random.seed(55)
def w(name, L):
    with open(f"{out}/{name}.txt", "w") as f:
        f.write("\n".join(map(str, L)) + "\n")
# generic: 3000 consecutive primes after 10^10
L=[]; p=10**10
while len(L)<3000: p=nextprime(p); L.append(p)
w("gen10", L)
# near-square below: p = N^2 - c with c in (2U,4U], U = floor(p^{1/4}); one prime per N
L=[]; N=100000
while len(L)<600:
    N+=1; U=int(round((N*N)**0.25))
    for c in range(2*U+1, 4*U+1):
        if isprime(N*N-c): L.append(N*N-c); break
w("nsq10", L)
# near 4th powers: p = N^4 + c, c small (U = N exactly)
L=[]
for N in range(300, 340):
    c=1; cnt=0
    while cnt<10:
        if isprime(N**4+c): L.append(N**4+c); cnt+=1
        c+=2 if N%2==0 else 1
w("n4p10", L)
# near rational multiples of squares: p = (b N^2 - c)/a for small a<b, c in (2U,4U] scaled
L=[]
for (a,b) in [(1,2),(2,3),(1,3),(3,4),(2,5)]:
    N=int((10**10*a/b)**0.5); got=0
    while got<100:
        N+=1; X=b*N*N; U=int(round((X/a)**0.25))
        for c in range(2*U*a+1, 4*U*a+1):
            if (X-c)%a==0 and isprime((X-c)//a): L.append((X-c)//a); got+=1; break
w("nrat10", L)
# odd squares control near 10^10
L=[(2*i+1)**2 for i in range(50000, 50600)]
w("sq10", L)
