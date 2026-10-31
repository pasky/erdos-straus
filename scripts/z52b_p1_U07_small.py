#!/usr/bin/env python3
"""U07 quick checks: Z0159 (discriminant group of star trees T_{x,y,z}), Z0160 (det with central weight k, Schur identity),
Z1994 (p+1 = (u-1)(B-1)+(4C-1)uB from p+u=(4uC-1)B), Z0855 (factorisations of the six known U-failures)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (2_000_000_000, 2_000_000_000))
from sympy import Matrix, factorint
from sympy.matrices.normalforms import smith_normal_form, ZZ
from fractions import Fraction as F
def star(x, y, z, k=2):
    arms = [x - 1, y - 1, z - 1]; N = 1 + sum(arms); M = [[0] * N for _ in range(N)]
    M[0][0] = k; idx = 1
    for a in arms:
        prev = 0
        for _ in range(a):
            M[idx][idx] = 2; M[prev][idx] = M[idx][prev] = -1; prev = idx; idx += 1
    return Matrix(M)
res = []
cyc = tot = 0
for x in range(2, 9):
    for y in range(x, 9):
        for z in range(y, 9):
            S = F(1, x) + F(1, y) + F(1, z)
            if S == 1: continue
            M = star(x, y, z); d = abs(M.det())
            assert d == abs(x * y * z * (S - 1)) if S != 1 else True
            snf = smith_normal_form(M, domain=ZZ); inv = [abs(snf[i, i]) for i in range(M.shape[0]) if abs(snf[i, i]) != 1]
            tot += 1; cyc += (len(inv) <= 1)
            if len(inv) > 1 and len(res) < 5: res.append(((x, y, z), d, inv))
print("Z0159: triples 2<=x<=y<=z<=8 (S!=1):", tot, "cyclic disc group:", cyc, "examples non-cyclic:", res)
# Z0160: det(central k) = xyz(k-3+S) for k=2..4 on a few triples
ok = all(abs(star(x, y, z, k).det()) == abs(x * y * z * (k - 3 + F(1, x) + F(1, y) + F(1, z)))
         for (x, y, z) in [(2, 3, 5), (2, 2, 2), (3, 4, 7), (2, 5, 9)] for k in (2, 3, 4))
print("Z0160: Schur identity det = xyz(k-3+S) holds:", ok)
# Z1994: p+u=(4uC-1)B  =>  p+1 = (u-1)(B-1)+(4C-1)uB
bad = [(u, B, C) for u in range(1, 30) for B in range(1, 30) for C in range(1, 30)
       if (4*u*C-1)*B - u + 1 != (u-1)*(B-1) + (4*C-1)*u*B]
print("Z1994: identity failures:", len(bad))
# Z0855: factorisations of the six known U failures
for n in [105, 2961, 3985, 25305, 111969, 978145]:
    f = factorint(n); print("Z0855", n, f, "#factors = 3 mod 4 (with mult):", sum(e for p, e in f.items() if p % 4 == 3))
