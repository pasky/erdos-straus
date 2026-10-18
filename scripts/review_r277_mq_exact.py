"""R277: how 'non-circular' is M_Q (Q = 720720) at small p?  Split M_Q into the part from pairs with q | Q
(where conditioning on p mod Q makes the term exactly 1[p = a mod q], i.e. the R-hit itself) and the rest."""
import sys
from math import gcd
sys.path.insert(0, 'scripts')
from review_r277_exact import pairs, factor, phi, legendre, isprime
Q = 720720

def sgrp(g):
    s = 1
    k = 0
    while g % 2 == 0:
        g //= 2; k += 1
    s = {0: 1, 1: 1, 2: 2}.get(k, 4)
    for l in factor(g):
        s *= 2
    return s

def split(p):
    ex = nex = 0.0; hits_ex = hits = 0; mass_ex = mass = 0.0
    for u, B in pairs(p):
        q = 4 * u * B; a = -(u + B)
        if (p - a) % 8:
            continue
        if any(legendre(p * a, l) != 1 for l in factor(u * B) if l != 2):
            continue
        g = gcd(q, Q)
        if (p - a) % g:
            continue
        w = sgrp(q) * phi(g) / (sgrp(g) * phi(q))
        hit = (p - a) % q == 0
        if q == g:
            ex += w; hits_ex += hit
        else:
            nex += w
        hits += hit
    return ex, nex, hits_ex, hits

rows = []
for p in range(13, int(sys.argv[1]) if len(sys.argv) > 1 else 3000):
    if p % 4 == 1 and isprime(p):
        ex, nex, he, h = split(p)
        rows.append((p, ex, nex, he, h))
for p, ex, nex, he, h in rows:
    if p in (409, 577, 2017) or p % 1000 in range(0, 0):
        print(f"p={p}: M_Q exact part (q|Q) = {ex:.2f} (= #hits with q|Q = {he}), non-exact part = {nex:.2f}, R = {h}")
import statistics
big = [r for r in rows if r[0] > 1000]
print("p in (1000, end): mean share of M_Q that is exact (q | Q):",
      round(statistics.mean(r[1] / (r[1] + r[2]) for r in big), 3),
      "; mean share of R-hits with q | Q:", round(sum(r[3] for r in big) / sum(r[4] for r in big), 3))
print("rank by non-exact part only (smallest 6):", sorted(rows, key=lambda r: r[2])[:6])
