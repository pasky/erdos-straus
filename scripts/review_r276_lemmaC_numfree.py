"""R276 from-scratch: (1) Lemma C equivalence for primes p < P (enumerate t,u,v>=2 with tuv-u-v < 3p);
(2) numerator-free rung: n <= N not of the form tuv-u-v (t,u,v >= 2), via loop over (t,u<=v)."""
import sys, math
import numpy as np
P, N = int(sys.argv[1]), int(sys.argv[2])
def isprime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n)+1))
bad = 0; checked = 0
for p in range(5, P):
    if not isprime(p): continue
    for t in range(2, 3*p):
        if 4*t - 4 >= 3*p: break
        for u in range(2, 3*p):
            if 2*t*u - u - 2 >= 3*p: break
            for v in range(2, 3*p):
                n = t*u*v - u - v
                if n >= 3*p: break
                checked += 1
                lhs = n == p
                rhs = (u % p and v % p and (t - pow(u, -1, p) - pow(v, -1, p)) % p == 0 and n < 2*p)
                if lhs != bool(rhs): bad += 1
print(f"(1) Lemma C: {checked} triples (p<{P}, tuv-u-v<3p), mismatches {bad}")
rep = np.zeros(N+1, dtype=bool)
t = 2
while 4*t - 4 <= N:
    u = 2
    while t*u*u - 2*u <= N:
        c = t*u - 1; n0 = c*u - u
        rep[n0::c] = True
        u += 1
    t += 1
exc = [n for n in range(1, N+1) if not rep[n]]
print(f"(2) N={N}: {len(exc)} exceptions: {exc}")
