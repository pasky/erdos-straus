#!/usr/bin/env python3
"""U07 batch-1 checks (capped: primes <= 400). Z0288 lattice of solution vectors (index in Z^3), Z0645 residues x mod p
closed under multiplication?, Z0897 solutions with arithmetic-progression denominators (y-x = z-y)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (2_000_000_000, 2_000_000_000))
import math
from sympy import primerange, Matrix
from sympy.matrices.normalforms import hermite_normal_form
def sols(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        if num <= 0: continue
        g = math.gcd(num, den); a, b = num // g, den // g
        from sympy import divisors
        for d in divisors(b * b):
            if (b + d) % a: continue
            y = (b + d) // a
            if y < x: continue
            e = b * b // d
            if (b + e) % a: continue
            z = (b + e) // a
            if z >= y: res.append((x, y, z))
    return res
idx_hist = {}; mult_closed = 0; ap_primes = 0; nprimes = 0
for p in primerange(5, 401):
    S = sols(p); nprimes += 1
    # Z0288: lattice spanned by (L/x, L/y, L/z), L = lcm of all denominators of this prime's solutions
    L = 1
    for t in S:
        for v in t: L = L * v // math.gcd(L, v)
    vecs = [[L // v for v in t] for t in S]
    M = Matrix(vecs)
    # index in Z^3 of row lattice = gcd of 3x3 minors; use HNF
    H = hermite_normal_form(M.T)
    diag = [abs(H[i, i]) for i in range(min(H.shape)) if H[i, i] != 0]
    idx = 1
    for dd in diag: idx *= dd
    idx_hist[idx] = idx_hist.get(idx, 0) + 1
    # Z0645: residues of x mod p over solutions, closed under multiplication?
    R = {x % p for x, y, z in S}
    if all((a * b) % p in R for a in R for b in R if len(R) <= 60): mult_closed += 1
    # Z0897: AP denominators
    if any(y - x == z - y for x, y, z in S): ap_primes += 1
print("Z0288 HNF-diagonal index product histogram (primes<=400):", sorted(idx_hist.items())[:12])
print("Z0645 primes whose solution-residue set is multiplicatively closed:", mult_closed, "/", nprimes)
print("Z0897 primes with an AP-denominator solution:", ap_primes, "/", nprimes)
