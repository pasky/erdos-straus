"""O149(b): p-adic and 2-adic valuation patterns of unordered positive solutions of 4/p = 1/x+1/y+1/z
(checks the tropical balancing statements of BRAINSTORM/tropical_newton.md)."""
import sys
from collections import Counter
from bs_padic_counts import spf_sieve

def v(n, q):
    k = 0
    while n % q == 0:
        n //= q; k += 1
    return k

def sols(p, spf):
    for x in range(p // 4 + 1, (3 * p) // 4 + 1):
        A, B = 4 * x - p, p * x
        fac = {p: 2}; n = x
        while n > 1:
            q = spf[n]; fac[q] = fac.get(q, 0) + 2; n //= q
        ds = [1]
        for q, e in fac.items():
            ds = [d * q**k for d in ds for k in range(e + 1)]
        for dl in ds:
            if dl <= B and (dl + B) % A == 0:
                y = (dl + B) // A
                if y >= x:
                    yield x, y, (B * B // dl + B) // A

P = int(sys.argv[1]); spf = spf_sieve(P)
pat, two, bal_fail = Counter(), Counter(), 0
for p in range(5, P + 1):
    if spf[p] != p: continue
    for x, y, z in sols(p, spf):
        assert 4 * x * y * z == p * (x * y + y * z + z * x)
        pat[tuple(sorted((v(x, p), v(y, p), v(z, p))))] += 1
        w = sorted((v(x, 2), v(y, 2), v(z, 2)))
        two[tuple(w)] += 1
        for q in set(spf_q for spf_q in []): pass
        # odd l != p balancing: max l-adic valuation attained >= twice
        for u in (x, y, z):
            n = u
            while n > 1 and n <= P:
                q = spf[n]; n //= q
                if q in (2, p): continue
                vs = sorted((v(x, q), v(y, q), v(z, q)))
                if vs[2] > 0 and vs[1] != vs[2]: bal_fail += 1
            
print("p-adic patterns (sorted):", dict(pat))
print("odd-l balancing failures:", bal_fail)
print("2-adic patterns (most common 12):", two.most_common(12))
