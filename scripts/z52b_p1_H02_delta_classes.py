"""Z0501: residue-class concentration Δ_m(N) = max_a #{d | N : d ≡ a (mod m)} for N = 4Cp+1, m = 4C,
versus control N' = 4Cn+1 for random odd n of the same size (not restricted to primes), and the ES class count
D^-(N) = #{d | N : d ≡ -1 (mod 4C)}. Prints mean Δ/τ, P(D^- > 0), and the correlation between max-class size and D^-."""
import random, sys
from sympy import factorint, primerange, isprime
random.seed(1)
def divisors(N):
    ds=[1]
    for q,e in factorint(N).items():
        ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def stats(Ns, m):
    out=[]
    for N in Ns:
        ds=divisors(N); cnt={}
        for d in ds: cnt[d%m]=cnt.get(d%m,0)+1
        D=max(cnt.values()); Dm=cnt.get(m-1,0)
        out.append((len(ds),D,Dm, cnt.get(1,0)))
    n=len(out)
    return (sum(o[1]/o[0] for o in out)/n, sum(o[1] for o in out)/n, sum(o[0] for o in out)/n, sum(1 for o in out if o[2]>0)/n,
            sum(1 for o in out if o[1]==o[3])/n)
X=int(sys.argv[1]) if len(sys.argv)>1 else 10**7
ps=[p for p in primerange(X, X+40000) if p%24==1][:300]
ctrl=[]
while len(ctrl)<300:
    n=random.randrange(X, X+40000)
    if n%24==1 and not isprime(n): ctrl.append(n)
print("X",X,"#primes",len(ps))
print("C  | primes: meanΔ/τ meanΔ meanτ P(D^->0) P(argmax=class1) | composites n≡1(24) same")
for C in [1,2,3,5,6,10,15,30]:
    m=4*C
    a=stats([4*C*p+1 for p in ps],m); b=stats([4*C*n+1 for n in ctrl],m)
    print(C, " ".join("%.3f"%x for x in a), "|", " ".join("%.3f"%x for x in b))
