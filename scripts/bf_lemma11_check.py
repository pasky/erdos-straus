"""Sanity check of POINTWISE_BINARYFORM Lemma 1.1 (square vanishing for N-points).
Enumerates N-points of ET's Sigma_I^n / Sigma_II^n with small (a,c,d) for n <= NMAX,
checks the Jacobi-symbol conclusions and that no square n occurs (n odd for Type I)."""
import sys
from sympy import jacobi_symbol as J
from math import isqrt
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
B = int(sys.argv[2]) if len(sys.argv) > 2 else 40
cntI = cntII = 0
for n in range(1, NMAX + 1):
    for a in range(1, B):
        for c in range(1, B):
            for d in range(1, B):
                # Type I: f = 4acd - n, f | 4a^2 d + 1, b = (na+c)/f
                f = 4*a*c*d - n
                if f > 0 and (4*a*a*d + 1) % f == 0 and (n*a + c) % f == 0:
                    e = (4*a*a*d + 1)//f; b = (n*a + c)//f
                    assert 4*a*b*d == n*e + 1 and c*e == a + b
                    if n % 2:
                        cntI += 1
                        assert J(-d % n, n) == -1, (n, a, b, c, d, e, f)
                        assert isqrt(n)**2 != n
                # Type II: f = 4acd - 1, e = (n + 4a^2 d)/f, b = (nc + a)/f
                f = 4*a*c*d - 1
                if (n + 4*a*a*d) % f == 0 and (n*c + a) % f == 0:
                    e = (n + 4*a*a*d)//f; b = (n*c + a)//f
                    assert 4*a*b*d == n + e and c*e == a + b
                    cntII += 1
                    assert J(n % f, f) == -1, (n, a, b, c, d, e, f)
                    assert isqrt(n)**2 != n
print(f"NMAX={NMAX} B={B}: TypeI(odd n) N-points {cntI}, TypeII N-points {cntII}; all checks passed")
