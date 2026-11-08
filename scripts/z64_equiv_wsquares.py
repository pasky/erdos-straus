"""z64 EQUIV Lemma R(a): the sign-free half (W) (n = tuv - u - v, t,u,v >= 2) holds at every odd square
m^2 >= 25, via a finite set of fixed pairs (t,u): m^2 = (tu-1)v - u  <=>  m^2 = -u (mod tu-1), v = (m^2+u)/(tu-1).
Search a finite pair set whose congruence conditions on m cover all odd m (mod L = lcm of moduli, with 2 | L),
then check small m directly.  Usage: python z64_equiv_wsquares.py"""
from math import gcd
from itertools import product
def lcm(a, b): return a // gcd(a, b) * b
cands = []
for t in range(2, 40):
    for u in range(2, 40):
        q = t * u - 1
        if q > 200: continue
        roots = [r for r in range(q) if (r * r + u) % q == 0]
        if roots: cands.append((t, u, q, roots))
# greedy cover of odd residues m mod L
def covered_set(pairs, L):
    cov = bytearray(L)
    for (t, u, q, roots) in pairs:
        rs = set(roots)
        for m in range(L):
            if m % q in rs: cov[m] = 1
    return cov
best = None
# try increasing L built from small moduli
chosen = []
L = 2
pool = sorted(cands, key=lambda c: c[2])
for c in pool:
    newL = lcm(L, c[2])
    if newL > 3 * 10**6: continue
    trial = chosen + [c]
    cov = covered_set(trial, newL)
    unc_old = None
    cov_old = covered_set(chosen, newL) if chosen else bytearray(newL)
    if sum(1 for m in range(1, newL, 2) if cov[m]) > sum(1 for m in range(1, newL, 2) if cov_old[m]):
        chosen, L = trial, newL
        unc = sum(1 for m in range(1, L, 2) if not cov[m])
        print("add", c[:3], "L =", L, "uncovered odd residues:", unc)
        if unc == 0: break
cov = covered_set(chosen, L)
unc = [m for m in range(1, L, 2) if not cov[m]]
print("pairs:", [(t, u) for (t, u, q, r) in chosen], "L =", L, "uncovered odd m mod L:", len(unc), unc[:10])
# v >= 2 needs m^2 + u >= 2(tu-1): check the finitely many small odd m directly by brute force
def W(n):
    for t in range(2, n + 1):
        for u in range(2, n + 1):
            q = t * u - 1
            if 2 * q - u > n: break
            if (n + u) % q == 0 and (n + u) // q >= 2: return (t, u, (n + u) // q)
        if 4 * t - 4 > n: break
    return None
bad = [m for m in range(5, 2001, 2) if W(m * m) is None]
print("odd m in [5,2000] with m^2 not a word:", bad)
maxq = max(q for (t, u, q, r) in chosen)
print("largest modulus", maxq, "; for m^2 >= 2*maxq every covering pair gives v >= 2")
