"""R82 brute-force check of MN3 Lemma 1.1 / Lemma 4.1 for nu = delta_1.
Prefix: r = 1 mod Q0 = lcm{prime powers <= q0, prime not dividing m}; remaining digits Haar on units.
For each stage-A q = ell^{a+1} > q0 (q <= QMAX) and each atom in C_q, compute exactly
P(r = -mD mod M^-), M^- = M/ell, by enumeration of r mod lcm(Q0, M^-), and compare with
  formula 1[s | P] phi(s)/phi(M^-),  s = gcd(M^-, Q0)
  bound   ell/phi(N);  Lemma 4.1: ell/(phi(N) phi(g/s)) and s = gcd(g,Q0) when weight > 0.
Usage: review_mn3_lemma11.py m q0 QMAX MMAX
"""
import sys
from math import gcd
import sympy

m, q0, QMAX, MMAX = map(int, sys.argv[1:5])
phi = lambda n: int(sympy.totient(n))
def lcm(a, b): return a // gcd(a, b) * b

def ppowers(lo, hi):
    out = []
    for p in sympy.primerange(2, hi + 1):
        if m % p == 0: continue
        x = p
        while x <= hi:
            if x > lo: out.append((x, p))
            x *= p
    return sorted(out)

Q0 = 1
for x, p in ppowers(0, q0): Q0 = lcm(Q0, x)
print("Q0 =", Q0)
checked = 0; bad = []; s_ne = 0
for q, ell in ppowers(q0, QMAX):
    L = 1
    for x, p in ppowers(0, q - 1):
        if p != ell: L = lcm(L, x)
    for M1 in sympy.divisors(L):
        M = q * M1
        if M > MMAX or (M + 1) % m: continue
        Mm = M // ell
        A = (M + 1) // m
        for D in sympy.divisors(A * A):
            if D > A: break
            P = m * D + 1
            g = gcd(M, P); N = M // g
            s = gcd(Mm, Q0)
            if s != gcd(M, Q0): bad.append(("s", q, M, D))
            Lc = lcm(Q0, Mm)
            target = (-m * D) % Mm
            tot = hit = 0
            for k in range(Lc // Q0):
                r = 1 + k * Q0
                if gcd(r, Lc) != 1: continue
                tot += 1
                if r % Mm == target: hit += 1
            pr = hit / tot
            form = (P % s == 0) * phi(s) / phi(Mm)
            if abs(pr - form) > 1e-12: bad.append(("formula", q, M, D, pr, form))
            if pr > ell / phi(N) + 1e-12: bad.append(("bound", q, M, D))
            if pr > 0:
                if s != gcd(g, Q0): s_ne += 1; bad.append(("s=gcd(g,Q0)", q, M, D))
                if pr > ell / (phi(N) * phi(g // s)) + 1e-12: bad.append(("L4.1", q, M, D))
            elif s != gcd(g, Q0):
                s_ne += 1
            checked += 1
print(f"checked {checked} atoms; defects: {len(bad)} {bad[:5]}")
print(f"atoms with zero weight and s != gcd(g,Q0): {s_ne}")
