"""z52d pass2 TO6 Z2032/Z2216: existence of a/n = sum of T unit fractions (T=4), for numerators a in {5,6}, n <= NMAX.
Recursion: pick smallest denominator x1 in [n/a, T n/a]; remainder A1/B1 (A1=a x1-n, B1=n x1); recurse with T-1 terms.
Base T=2: 1/y+1/z = A/B solvable iff some divisor d of B^2 with d ≡ -B (mod A) and (B^2/d + B) ≡ 0 (mod A).
Exact, existence only. Memory small (sympy factorint of B)."""
import sys, time
from sympy import divisors
from math import ceil
def two(A,B):
    if A<=0: return False
    for d in divisors(B*B):
        if d>B: continue           # y<=z symmetry
        if (d+B)%A==0 and ((B*B//d)+B)%A==0: return True
    return False
def rep(A,B,T,lo):
    # is A/B a sum of T unit fractions with all denominators >= lo ?
    if A<=0: return False
    if T==1: return B%A==0 and B//A>=lo
    if T==2: return two(A,B)
    x_lo=max(lo, -(-B//A)); x_hi = (T*B)//A + 1
    for x in range(x_lo, x_hi+1):
        if A*x<=B: continue
        A2=A*x-B; B2=B*x
        if rep(A2,B2,T-1,x): return True
    return False
a=int(sys.argv[1]); T=int(sys.argv[2]); NMAX=int(sys.argv[3])
fails=[]; t0=time.time()
for n in range(2,NMAX+1):
    ok=False
    for x1 in range(max(1,-(-n//a)), (T*n)//a+1):
        if a*x1<=n: continue
        if rep(a*x1-n, n*x1, T-1, x1): ok=True; break
    if not ok: fails.append(n)
print(f"a={a} T={T} NMAX={NMAX} fails={fails} time={time.time()-t0:.1f}s")
