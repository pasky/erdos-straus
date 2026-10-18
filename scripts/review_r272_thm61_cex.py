"""R272: counterexample to Thm 6.1 / HC as stated.
Omega = Q(zeta_q), q prime > B, q = 3 mod 4, C = Frobenius class of p == -4 (mod q).
C is compatible with p == 1 (mod M) (Omega ∩ Q(zeta_M) = Q), yet every p in C has the
certificate w = q | p+4, w == -1 (mod 4) at level d = 1. Verify the ES solution exactly."""
from fractions import Fraction as F
from sympy import isprime
D, B, q = 1, 6, 7          # B >= 4D+2 = 6, q = 7 > B, q = 3 mod 4
cnt = 0
for p in range(5, 200000):
    if not (isprime(p) and p % 4 == 1 and p % q == (-4) % q):
        continue
    d = 1; w = q; assert (p + 4*d) % w == 0 and w % (4*d) == 4*d - 1
    c = (w + 1)//(4*d); a = (p + (p + 4*d)//w)//(4*d)
    assert 4*a*d - p == (p + 4*d)//w
    x, y, z = a*d, a*c*d*p, c*d*p
    assert F(4, p) == F(1, x) + F(1, y) + F(1, z), p
    cnt += 1
print("primes p=1(4), p=-4 (mod 7), p<2e5, all certified at d=1:", cnt)
# also some with p == 1 mod M (M built from primes <= 6 only)
M = 4 * 2**6 * 3**4 * 5**3   # q^{e_q} > 16*D*(D+1)=32
hits = [p for p in range(1, 10**8, M) if isprime(p) and p % q == 3][:5]
print("p == 1 (mod M) and in C (first 5):", hits)
