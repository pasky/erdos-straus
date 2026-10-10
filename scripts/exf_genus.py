"""O131 step 3 (computation): Type II at fixed (c,d) as one orbit inside its genus.
For q = 4cd, M = 4c^2 d n + 1:
  A_{c,d}(n) = #{X | M : X == -1 (mod q)}            (= ordered Type II pairs (a,b), exact)
  G_{c,d}(n) = #{X | M : X in -1*(Z/q)^{x2}} / |(Z/q)^{x2}|   (genus average: mean over the residue classes
               of the quadratic-character coset of -1; = Siegel-Weil/local-density prediction in divisor language)
Output: per-(c,d) comparison over primes, and cumulative sums over c showing the genus mass is not summable."""
import numpy as np, sys
from sympy import factorint, primerange, totient
from itertools import product
def divisors_from(f):
    ds = [1]
    for p, e in f.items(): ds = [x * p**k for x in ds for k in range(e + 1)]
    return ds
def in_minus_sq(X, q):
    y = (-X) % q
    for l, e in factorint(q).items():
        if l == 2:
            if e == 2 and y % 4 != 1: return False
            if e >= 3 and y % 8 != 1: return False
        else:
            if pow(y % l, (l - 1) // 2, l) != 1: return False
    return True
def nsq(q):
    f = factorint(q); k = sum(1 for l in f if l > 2) + (0 if f.get(2, 0) < 2 else (1 if f[2] == 2 else 2))
    return int(totient(q)) // 2**k
def AG(n, c, d):
    q = 4 * c * d; M = 4 * c * c * d * n + 1; ds = divisors_from(factorint(M))
    A = sum(1 for X in ds if X % q == q - 1)
    G = sum(1 for X in ds if in_minus_sq(X, q)) / nsq(q)
    return A, G
if __name__ == '__main__':
    P = list(primerange(5, 3000))
    print('per-(c,d) comparison over primes 5..3000: mean A, mean G, corr(A,G), mean|A-G|, P(A=0), P(A=0 | G>=1)')
    for c, d in [(1,1),(1,2),(1,3),(2,1),(1,5),(3,1),(2,3),(1,7),(5,2)]:
        r = np.array([AG(p, c, d) for p in P])
        A, G = r[:, 0], r[:, 1]
        print(f'(c,d)=({c},{d}): {A.mean():.3f} {G.mean():.3f} corr {np.corrcoef(A,G)[0,1]:.3f} mean|A-G| {np.abs(A-G).mean():.3f} P(A=0) {np.mean(A==0):.2f} P(A=0|G>=1) {np.mean(A[G>=1]==0):.2f}')
    print('cumulative over c (d=1): sum_{c<=C} A vs G')
    for p in (101, 1009, 2003):
        sa = sg = 0; out = []
        for c in range(1, 2001):
            a, g = AG(p, c, 1); sa += a; sg += g
            if c in (10, 100, 300, 1000, 2000): out.append((c, sa, round(sg, 2)))
        print(p, out)
