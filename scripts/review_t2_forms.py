"""R24 from-scratch check of EXCEPTIONAL_TUPLES2 Lemma 1.1 / Cor 1.2 (forms).

For every prime l = 3 mod 4 up to LMAX:
  * (r,s,m) with rsm=A, gcd(r,s)=1  <->  D=r^2 m  is a bijection onto divisors of A^2;
  * n = -4D mod l  <=>  l | n s + r  (checked on all residues n mod l);
  * -1 mod l lies in R(l).
Also: every residue of R(l) has some form (r,s) with 4rs | l+1.
"""
import sys
from math import gcd
from sympy import primerange, divisors

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
bad = 0
nprimes = 0
for l in primerange(3, LMAX + 1):
    if l % 4 != 3:
        continue
    nprimes += 1
    A = (l + 1) // 4
    divA2 = set(divisors(A * A))
    triples = []
    for r in divisors(A):
        for s in divisors(A // r):
            if gcd(r, s) != 1:
                continue
            m = A // (r * s)
            triples.append((r, s, m))
    Ds = [r * r * m for (r, s, m) in triples]
    if len(set(Ds)) != len(Ds) or set(Ds) != divA2:
        print("BIJECTION FAIL", l); bad += 1
    R = {(-4 * D) % l for D in divA2}
    if (l - 1) not in R:
        print("-1 not in R", l); bad += 1
    for (r, s, m) in triples:
        D = r * r * m
        for n in range(l):
            if ((n + 4 * D) % l == 0) != ((n * s + r) % l == 0):
                print("EQUIV FAIL", l, r, s, n); bad += 1
                break
        assert (l + 1) % (4 * r * s) == 0
print(f"primes checked: {nprimes} (l <= {LMAX}); failures: {bad}")
