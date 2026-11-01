"""Z1164: adelic height bookkeeping for ES parametrisations (G4, NC0).
The cleared equation 4xyz = n(xy+yz+zx) is HOMOGENEOUS of degree 3 in (n,x,y,z), so solutions are points of
P^3 on the surface S: 4xyz = n(xy+yz+zx). The adelic (balanced) height of a rational point is
  H(P) = sum_v log max_i |w_i|_v   (product formula => independent of the chosen representative).
Two exact transformations tested on all solutions with n = p (p = 1 mod 4, p <= 300; x<=y<=z enumerated exactly):
  T1: S3 permutation of (x,y,z)                         -> H must be unchanged (exact).
  T2: rescaling (n,x,y,z) -> (n/g, x/g, y/g, z/g), g = gcd(n,x,y,z)  (valid: S is homogeneous) -> H unchanged,
      while the naive 'real size' log max(n,x,y,z) drops by log g.
Also: for n = p prime, can g = p? (then 4 = sum of three unit fractions, impossible) -> count of such solutions.
Output: per p: #solutions, #non-primitive, max |change| of archimedean-only height under T2, min naive height."""
import math
from fractions import Fraction
from math import gcd, log

PS = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149, 157, 173, 181, 193, 197, 229, 233, 241, 257, 269, 277, 281, 293]


def solutions(p):
    S = []
    for x in range(math.ceil(p / 4), (3 * p) // 4 + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        for y in range(x, math.floor(2 / r) + 1):
            r2 = r - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1:
                S.append((p, x, y, r2.denominator))
    return S


def H_arch(w):
    return log(max(abs(v) for v in w))


def primitive(w):
    g = 0
    for v in w:
        g = gcd(g, v)
    return tuple(v // g for v in w), g


rows = []
tot = 0; nonprim = 0; max_T2_naive = 0.0; max_T1 = 0.0
for p in PS:
    S = solutions(p)
    tot += len(S)
    for (n, x, y, z) in S:
        w = (n, x, y, z)
        assert 4 * x * y * z == n * (x * y + y * z + z * x)
        # T1: permutations
        for perm in [(x, z, y), (y, x, z), (z, y, x), (y, z, x), (z, x, y)]:
            w2 = (n,) + perm
            max_T1 = max(max_T1, abs(H_arch(w2) - H_arch(w)))
            assert 4 * perm[0] * perm[1] * perm[2] == n * (perm[0] * perm[1] + perm[1] * perm[2] + perm[0] * perm[2])
        # T2: primitive rescaling
        pr, g = primitive(w)
        if g > 1:
            nonprim += 1
        assert 4 * pr[1] * pr[2] * pr[3] == pr[0] * (pr[1] * pr[2] + pr[2] * pr[3] + pr[1] * pr[3])
        max_T2_naive = max(max_T2_naive, H_arch(w) - H_arch(pr))
    rows.append((p, len(S), sum(1 for s in S if primitive(s)[1] > 1)))
print("p, #solutions (x<=y<=z), #non-primitive (gcd(n,x,y,z)>1)")
for r in rows:
    print(r)
print("total solutions:", tot, " non-primitive:", nonprim)
print("T1 (S3 permutation): max |change in archimedean height| =", max_T1)
print("T2 (rescale to primitive): naive size drop max =", round(max_T2_naive, 4), "(=log g); height change of primitive rep = 0 by construction")
print("all solutions primitive (gcd(n,x,y,z)=1), so the p-adic part of H vanishes by the product formula:",
      all(primitive(s)[1] == 1 for p in PS for s in solutions(p)))
