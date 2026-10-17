"""O257 Thm 2.6 independent check on actual primes n ≡ x_{3,2} (mod 60480): witnesses with H | 60480."""
from z28_witness import reps
from sympy import isprime
from sympy.ntheory.modular import crt
M = 64 * 35 * 27; r = int(crt([64 * 35, 27], [1, 2])[0])
ps = [n for n in range(r, r + M * 40, M) if isprime(n)][:4]
for k in (4, 8, 12, 16):
    for n in ps:
        R = reps(n, k); print(k, n, len(R), 'witnesses with H|M:', [w for w in R if M % w[6] == 0][:3])
