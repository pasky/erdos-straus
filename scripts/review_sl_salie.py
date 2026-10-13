"""R175: (1) Type II certificates ff' - 4c^2 d p = 1, f = f' = -1 mod 4cd, p = 1 mod 4 prime < PMAX: check
(f'/p) = -1, hence theta multiplier eps_{f'}^{-1} (4p/f') = +i.  (2) Salie formula numerically for small primes."""
import sys, cmath
from review_sl_rayclass import jac, isprime
PMAX = int(sys.argv[1]); cnt = bad = 0; certs = set()
for p in range(5, PMAX, 4):
    if not isprime(p): continue
    for c in range(1, 2 * p):
        if 4 * c * c * p + 1 > (4 * c * p) ** 2 * 4: pass
        for d in range(1, 10 ** 9):
            q = 4 * c * d; M = 4 * c * c * d * p + 1
            if (q - 1) ** 2 > M: break
            for f in range(q - 1, int(M ** .5) + 2, q):
                if M % f == 0 and (M // f) % q == q - 1:
                    for (F, Fp) in {(f, M // f), (M // f, f)}:
                        certs.add((p, c, d, F, Fp))
                        eps_inv = -1j if Fp % 4 == 3 else 1
                        mult = eps_inv * jac(4 * p, Fp)
                        if jac(Fp, p) != -1 or abs(mult - 1j) > 1e-12: bad += 1
print("Type II certificates (ordered (f,f')) with p <", PMAX, ":", len(certs), "violations", bad)
# Salie
worst = 0
for c in [3, 5, 7, 11, 13, 17, 19, 23]:
    eps = 1 if c % 4 == 1 else 1j
    for a in range(1, c):
        for b in range(1, c):
            L = sum(jac(x, c) * cmath.exp(2j * cmath.pi * (a * x + b * pow(x, -1, c)) / c) for x in range(1, c))
            R = eps * c ** .5 * jac(b, c) * sum(cmath.exp(4j * cmath.pi * y / c) for y in range(c) if (y * y - a * b) % c == 0)
            worst = max(worst, abs(L - R))
print("Salie formula max |LHS-RHS| over c<=23 prime, a,b units:", worst)
