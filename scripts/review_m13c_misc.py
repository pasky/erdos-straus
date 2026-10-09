#!/usr/bin/env python3
"""R100 misc checks: (1) §1 non-square lemma for all ET classes with M <= Mmax (own enumeration);
(2) §7 claim on the open leaves of root 418321 (residues mod 17, 19, 23, 31)."""
import gzip, json, sys
from math import gcd
from sympy import factorint, divisors

Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6000

def classes_upto(Mmax):
    """all (fam, P, M, residues) with modulus M <= Mmax (ET Prop 1.9, own enumeration)"""
    out = []
    for u in range(1, Mmax // 4 + 1):
        m = 4 * u
        for a in divisors(u):
            d = u // a
            for f in divisors(4*a*a*d + 1): out.append(("I1", (a, d, f), m, [(-f) % m]))
            for e in divisors(a + d):
                if gcd(e, m) == 1:
                    out.append(("I4", (a, d, e), m, [(-pow(e, -1, m)) % m]))
                    out.append(("II1", (a, d, e), m, [(-e) % m]))
            for f in range(1, Mmax // m + 1):
                if gcd(f, m) != 1: continue
                M = m * f
                out.append(("I2", (a, d, f), M, [x for x in range((-f) % m, M, m) if (a*x + d) % f == 0]))
                R = [x for x in range((-f) % m, M, m) if (x*x + 4*a*a*d) % f == 0]
                if R: out.append(("I3", (a, d, f), M, R))
                out.append(("II3", (a, d, f), M, [(-4*a*a*d - f) % M]))
    for f in range(3, Mmax + 1, 4):
        for u in divisors((f + 1) // 4):
            for a in divisors(u):
                out.append(("II2", (a, u // a, f), f, [(-4*a*a*(u // a)) % f]))
    return out

def is_local_square(r, q, k):
    """r a unit; is r a square in Z_q^x as far as visible mod q^k (q odd: Legendre; q=2: mod 8/4/2)."""
    if q == 2:
        return r % 8 == 1 if k >= 3 else (r % 4 == 1 if k == 2 else True)
    return pow(r, (q - 1) // 2, q) == 1

bad = 0; n = 0
for fam, P, M, R in classes_upto(Mmax):
    fa = factorint(M)
    for r in R:
        if gcd(r, M) != 1: continue
        n += 1
        if all(is_local_square(r, q, k) for q, k in fa.items()):
            bad += 1
            if bad <= 5: print("SQUARE-EVERYWHERE", fam, P, M, r)
print(f"§1: Mmax={Mmax}: {n} (class,residue) unit pairs, {bad} locally square at every prime of M")

t = json.load(gzip.open("data/mordell13c/tree6_6000.json.gz"))
def opens(nd):
    if "open" in nd: yield nd["x"], nd["L"]
    for c in nd.get("children", []): yield from opens(c)
for root in t["roots"]:
    if root["x"] != 418321: continue
    O = list(opens(root))
    for q in (17, 19, 23, 31):
        print(f"§7: root 418321, {len(O)} open leaves; residues mod {q} among leaves with q | L:",
              sorted({x % q for x, L in O if L % q == 0}), "; leaves with q ∤ L:", sum(L % q != 0 for x, L in O))
print("distinct unit (M, r) classes with M <=", Mmax, ":",
      len({(M, r) for fam, P, M, R in classes_upto(Mmax) for r in R if gcd(r, M) == 1}))
