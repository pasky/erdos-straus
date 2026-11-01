# z52d pass2 TO4 lint-fix E: Z1666 virtual-m test (Pomerance–Weingartner, arXiv:2511.16817: m=8 exceptions 131, 241).
# m/n = 1/x+1/y+1/z with x | nM  <=>  e1+e2+e3 = mM with e_i = nM/x_i dividing nM (e_i ≥ 1).  Minimal M ≤ MMAX.
# Also Z1101-type: same test for m=4 (controls). And the PW Type I/II parametrisation with m for the exceptions.
import math, itertools, statistics
from sympy import divisors, primerange
def solvable_within(m,n,M):
    L=n*M; D=divisors(L); T=m*M; Ds=set(D)
    for i,e1 in enumerate(D):
        if 3*e1>T: break
        for e2 in D:
            if e2<e1: continue
            e3=T-e1-e2
            if e3<e2: break
            if e3 in Ds: return True
    return False
def minM(m,n,MMAX=300):
    for M in range(1,MMAX+1):
        if solvable_within(m,n,M): return M
    return None
for n in [131,241]:
    print("Z1666 n=%d: minimal M with 8/n = sum of 3 unit fractions with denominators | nM : %s ; for m=4 at same n: %s"%(n, minM(8,n), minM(4,n)))
ctrl=[p for p in primerange(5,400) if p%4==1][:30]
m8=[minM(8,p,200) for p in ctrl]; m4=[minM(4,p,200) for p in ctrl]
print("Z1666 controls (primes ≡1 mod 4, p<400, first 30): m=8 minimal M: %s ; m=4 minimal M: %s"%(m8,m4))
# PW Type I/II parametrisation for m: Type II(m;c,d): f f' − m c² d n = 1, f≡f'≡−1 (mod m c d)  (their Prop 2.x analogue)
def typeII_m(m,n,c,d):
    N=m*c*c*d*n+1; mod=m*c*d
    out=[]
    for f in divisors(N):
        if f%mod==mod-1 and (N//f)%mod==mod-1 and f>1 and N//f>1: out.append(f)
    return out
for n in [131,241]:
    hits=[(c,d) for c in range(1,21) for d in range(1,41) if typeII_m(8,n,c,d)]
    print("Z1666 PW Type II analogue for m=8, n=%d, c≤20, d≤40: solutions %s"%(n, hits[:5]))
