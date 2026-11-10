# z69 TWIST Prop R: Type I solutions (4abd = n e + 1, c e = a + b) of n == 1 (mod 4) with e = n + 2j > n.
# (A) roots at level j: nu, eps == 3 (4), nu + eps = 2j, 4*alpha*b*d = nu*eps - 1, b - alpha = c*eps > 0.
# (B) brute force: all n == 1 (4), n <= NMAX, all odd j <= JMAX: Type I solutions with e = n + 2j.
# Check: {j with a root} == {j with a brute-force solution} up to chains that start above NMAX (reported).
import sys
from sympy import divisors
JMAX=int(sys.argv[1]); NMAX=int(sys.argv[2])
roots={}
for j in range(1,JMAX+1,2):
    for nu in range(3,2*j,4):
        eps=2*j-nu
        if eps<3 or eps%4!=3: continue
        K=(nu*eps-1)//4
        for al in divisors(K):
            for b in divisors(K//al):
                if b>al and (b-al)%eps==0:
                    c=(b-al)//eps; d=K//(al*b); n1=4*b*c*d-eps
                    roots.setdefault(j,[]).append((n1,nu,eps,al,b,c,d))
brute={}
for n in range(1,NMAX+1,4):
    for j in range(1,JMAX+1,2):
        e=n+2*j; N=(n*e+1)//4
        for a in divisors(N):
            for b in divisors(N//a):
                if b<a and (a+b)%e==0:
                    brute.setdefault(j,[]).append((n,a,b,(a+b)//e,N//(a*b),e))
ster=[j for j in range(1,JMAX+1,2) if j not in roots]
print(f"odd j <= {JMAX}: {len(ster)} sterile (no root): {ster}")
bad=[j for j in brute if j not in roots]
print("brute-force solutions (n <= %d) on a root-less gap j: %s"%(NMAX,bad))
miss=[j for j in roots if j not in brute and min(r[0] for r in roots[j])<=NMAX]
print("gaps with a root whose first chain element n1 <= NMAX but no brute-force solution:",miss)
# every brute-force solution with minimal n on its gap should be n1 of a root or a later chain element
ex=[(j,min(roots[j])) for j in sorted(roots)[:8]]
print("first roots (j,(n1,nu,eps,alpha,b,c,d)):",ex)
print("brute minimal n per gap (first 8):",[(j,min(brute[j])) for j in sorted(brute)[:8]])
assert not bad and not miss, 'Prop R cross-check FAILED'
assert all(min(brute[j])[0]==min(roots[j])[0] for j in brute if min(roots[j])[0]<=NMAX), 'minimal n mismatch'
print('Prop R cross-check PASSED (sterile gaps empty; root gaps realised; minimal n per gap = first chain element)')
