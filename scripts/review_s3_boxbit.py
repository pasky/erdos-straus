"""R207: s3_box_bit item 2 and s3_eps_mu_sieve identity, from scratch.
(i) primes p = 1 (4) < P, primes g = 3 (4) < G, g != p: box hit (-p = 4c^2 d mod g, cd | (g+1)/4) => (p/g) = -1;
    and [exists Q odd, g | p + 4Q^2] <=> (p/g) = -1.
(ii) d | lambda counterexample: V_26 point (A,B,D,mu) = (2,1,35,35).
(iii) 4tj-1 | nj+t <=> 4tj-1 | n+4t^2, odd n < 400, t, j < 40.  Usage: P G"""
import sys
from sympy import primerange, jacobi_symbol as J, divisors
P, G = map(int, sys.argv[1:3])
hit = {1: 0, -1: 0}; tot = {1: 0, -1: 0}; shotbad = 0
for p in primerange(5, P):
    if p % 4 != 1: continue
    for g in primerange(3, G):
        if g % 4 != 3 or g == p: continue
        s = J(p, g); tot[s] += 1
        k = (g + 1) // 4; t = (-p) % g
        if any(4 * c * c * (m // c) % g == t for m in divisors(k) for c in divisors(m)): hit[s] += 1
        shot = any((p + 4 * Q * Q) % g == 0 for Q in range(1, 2 * g, 2))
        if shot != (s == -1): shotbad += 1
print("(i) box hits by (p/g):", {s: f"{hit[s]}/{tot[s]}" for s in hit}, "shot<=>(p/g)=-1 mismatches:", shotbad)
n, A, B, D, mu = 26, 2, 1, 35, 35
print("(ii) V_26 eq:", n*A*A + B*B + D == 2*mu*A*B, "D|mu:", mu % D == 0, "g = 2*lambda*A-1 =", 2*(mu//D)*A-1,
      "-13 mod 3 in Box(1)={4}:", (-13) % 3 == 4 % 3)
bad = sum(1 for n in range(1, 400, 2) for t in range(1, 40) for j in range(1, 40)
          if ((n*j + t) % (4*t*j - 1) == 0) != ((n + 4*t*t) % (4*t*j - 1) == 0))
print("(iii) mismatches:", bad)
