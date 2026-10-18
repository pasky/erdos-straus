"""O263 §7: Haar (limiting) failure density of the forced congruence rule F_{B,D} on the b=1 line (levels d<=D,
small primes <=B, one opaque cofactor). The rule depends only on p mod a modulus built from primes <= max(B,D) (and
valuations), so we sample random large p ≡ 1 (4) coprime to all primes <= max(B,D)+1 (Haar on the units, as primes are)."""
import sys, random
from sympy import primerange
B=int(sys.argv[1]); D=int(sys.argv[2]); T=int(sys.argv[3]); random.seed(int(sys.argv[4]) if len(sys.argv)>4 else 1)
P=list(primerange(2,max(B,D)+2)); SP=[q for q in P if q<=B]
def forced(p):
    for d in range(1,D+1):
        t=4*d; N=p+4*d; s=[]; 
        for q in SP:
            while N%q==0: s.append(q); N//=q
        S={1}
        for f in s: S|={x*f%t for x in S}
        if N>1: S|={x*(N%t)%t for x in S}
        if t-1 in S: return d
    return None
fail=0; dmax=0
for _ in range(T):
    while True:
        p=random.randrange(10**15,10**16)*4+1
        if all(p%q for q in P[1:]): break
    r=forced(p)
    if r is None: fail+=1
    else: dmax=max(dmax,r)
print(f"B={B} D={D} samples={T} forced-rule failures={fail} ({fail/T:.4f}) max least level among successes={dmax}")
