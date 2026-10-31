"""Z0141 pass-1: which primes p ≤ X have 4/p = 1/x1 + 1/x2 + 1/x3 with every x_i ∈ U ∪ pU, U = S-units (S = {2,3,5,7})?
Reduction (PROVED in-script comments): exactly one or two x_i carry p (none: p ∤ denominators; three: 4 = Σ1/s_i ≤ 3).
 two carry p:  p = numerator of 4 − 1/s1 − 1/s2 (then x3 = its denominator, an S-unit).
 one carries p: u/v := s2 s3/(s2+s3) reduced; p = (4u − 1)/v with v | 4u − 1 (x1 = p·u).
Both are loops over pairs of S-units."""
import sys, json
from fractions import Fraction as F
from sympy import isprime
X = int(sys.argv[1]); S = [2, 3, 5, 7]; LIM = 10**10
U = [1]
for q in S:
    U = sorted({u*q**k for u in U for k in range(0, 40) if u*q**k <= LIM})
cov1, cov2 = set(), set()
for i, a in enumerate(U):
    if a > X: break
    for b in U[i:]:
        r = F(4) - F(1, a) - F(1, b)
        if r.numerator <= X and isprime(r.numerator) and r.numerator > 7: cov2.add(r.numerator)
        g = F(a*b, a+b); u, v = g.numerator, g.denominator
        if (4*u - 1) % v == 0:
            p = (4*u - 1)//v
            if p <= X and p > 7 and isprime(p): cov1.add(p)
from sympy import primerange
P = [p for p in primerange(11, X+1)]; P1 = [p for p in P if p % 4 == 1]
cov = cov1 | cov2
out = dict(X=X, S=S, n_primes=len(P), covered=len(cov & set(P)), covered_p1mod4=len(cov & set(P1)), n_p1mod4=len(P1),
           covered_by_one_p=len(cov1), covered_by_two_p=len(cov2),
           largest_covered_1mod4=sorted(cov & set(P1))[-10:], covered_1mod24=sorted(p for p in cov if p % 24 == 1)[:30])
out['frac_covered_by_block'] = {f'{lo}-{2*lo}': round(len([p for p in P if lo < p <= 2*lo and p in cov])/max(1, len([p for p in P if lo < p <= 2*lo])), 4) for lo in (1000, 4000, 16000, 64000, 250000, 500000) if 2*lo <= X}
print(json.dumps(out, indent=1)); json.dump(out, open(f'data/z52b/pass1/H00/sunits_{X}.json', 'w'), indent=1)
