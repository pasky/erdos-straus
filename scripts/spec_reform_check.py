"""O123 §2: brute-force check of the fixed-p reformulations (Lemmas 2.1-2.4) against spec_typecount output.
For each prime p<=P: enumerate (c,d) with cd<=p, divisors f of p^2+4c^2 d with f = -p mod 4cd,
a=(p+f)/(4cd), b=(pa+c)/f, normalisation a<=b, gcd(a,b,c)=1, and compare with FI[p].
Also checks e = (4a^2d+1)/f integral, 4abd - p e = 1, e | a+b, Hecke identity Q' = Q_- o [[1,2bd],[0,p]],
and Type II form (aq-1)(bq-1) = c q p + 1 (q=4cd) against FII[p]."""
import sys, math, numpy as np
from sympy import isprime, divisors
P = int(sys.argv[1]); pre = sys.argv[2]
FI = np.fromfile(pre + ".FI.bin", dtype=np.uint32); FII = np.fromfile(pre + ".FII.bin", dtype=np.uint32)
bad = 0
for p in range(5, P + 1):
    if not isprime(p): continue
    cnt = 0
    for c in range(1, p):
        for d in range(1, 2 * p // c + 2):
            if (c * d) % p == 0: continue
            q = 4 * c * d; m = p * p + 4 * c * c * d
            for f in divisors(m):
                if (f + p) % q: continue
                a = (f + p) // q; num = p * a + c
                assert num % f == 0; b = num // f
                if a > b or math.gcd(math.gcd(a, b), c) != 1: continue
                assert (4 * a * a * d + 1) % f == 0; e = (4 * a * a * d + 1) // f
                assert 4 * a * b * d - p * e == 1 and (a + b) % e == 0 and (a + b) // e == c
                # Hecke: Q_-=[f,-4ad,de]; Q'(x,y)=Q_-(x+2bd y, p y) should be [f,4cd,d(4bcd-p)]
                k = 2 * b * d; A_, B_, C_ = f, -4 * a * d, d * e
                Bp = 2 * A_ * k + B_ * p; Cp = A_ * k * k + B_ * k * p + C_ * p * p
                assert (Bp, Cp) == (4 * c * d, d * (4 * b * c * d - p))
                cnt += 1
    cII = 0  # Type II: (aq-1)(bq-1) = cqp+1, q=4cd, a<=b, gcd(a,b,c)=1, gcd(abd,p)=1
    for c in range(1, p + 1):
        for d in range(1, 10 ** 9):
            q = 4 * c * d
            if q - 1 > c * q * p + 1: break
            M = c * q * p + 1
            for X in divisors(M):
                if X % q != q - 1: continue
                Y = M // X
                if Y % q != q - 1 or X > Y: continue
                a, b = (X + 1) // q, (Y + 1) // q
                if math.gcd(math.gcd(a, b), c) != 1 or math.gcd(a * b * d, p) != 1: continue
                cII += 1
            if 4 * c * d > 4 * p * p: break
    if cnt != FI[p] or cII != FII[p]:
        bad += 1; print("MISMATCH", p, cnt, FI[p], cII, FII[p])
print("primes 5..", P, "mismatches:", bad)
