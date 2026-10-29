"""z50 ncrt: is an endpoint-grouped ES5/U class a finite union of K2 classes?
For each modulus G <= GMAX build the set of residues mod G covered by K2 classes of modulus exactly G
(R(M): -4D mod M, M=3 mod 4, D | ((M+1)/4)^2;  (a,D): -(4D+a) mod 4a g(D);  Case A: -m^{-1} mod 4rh, r sqfree, m | 4rh^2+1).
Then for n in a test class, record the least G with n mod G covered.  If min-G grows without bound along the
class, the class is not covered by K2 classes of bounded modulus.
Usage: uv run python z50_ncrt_k2cover.py GMAX NMAX"""
import sys
from math import gcd
from sympy import divisors, factorint

GMAX = int(sys.argv[1]); NMAX = int(sys.argv[2])
cov = {}  # G -> set of residues
def add(G, r):
    cov.setdefault(G, set()).add(r % G)
# R(M)
for M in range(3, GMAX + 1, 4):
    A = (M + 1) // 4
    for D in divisors(A * A):
        add(M, -4 * D)
def g_of(D):
    g = 1
    for p, e in factorint(D).items():
        g *= p ** ((e + 1) // 2)
    return g
# (a,D): modulus 4 a g(D) <= GMAX ; D ranges over all D with g(D)=g, i.e. D | g^2 and g | D
for a in range(1, GMAX // 4 + 1):
    for g in range(1, GMAX // (4 * a) + 1):
        G = 4 * a * g
        for D in divisors(g * g):
            if D % g == 0 and g_of(D) == g:
                add(G, -(4 * D + a))
# Case A: d = r h^2, r squarefree, G = 4 r h
def sqfree(r):
    return all(e == 1 for e in factorint(r).values())
for r in range(1, GMAX // 4 + 1):
    if not sqfree(r):
        continue
    for h in range(1, GMAX // (4 * r) + 1):
        G = 4 * r * h
        for m in divisors(4 * r * h * h + 1):
            add(G, -pow(m, -1, G))
Gs = sorted(cov)
def minG(n):
    for G in Gs:
        if n % G in cov[G]:
            return G
    return None
tests = {
    "U class 97 mod 104 (x=7,t=2,A=13, 4|u)": (97, 104),
    "U class x=3,t=2,A=5: n=-3 mod 20, n=5 mod 8 -> 37 mod 40": (37, 40),
    "U class x=7,t=4? (4|t is R) skip; x=15,t=2,A=29, n=1 mod 8, n=-15 mod 116": None,
}
# build third: n = -15 mod 116 and n = 1 mod 8
for n0 in range(232):
    if n0 % 116 == (-15) % 116 and n0 % 8 == 1:
        tests["U class x=15,t=2,A=29, 4|u: %d mod 232" % n0] = (n0, 232)
del tests["U class x=7,t=4? (4|t is R) skip; x=15,t=2,A=29, n=1 mod 8, n=-15 mod 116"]
print("GMAX", GMAX, "NMAX", NMAX, "moduli with K2 classes:", len(Gs))
for name, (b, q) in tests.items():
    worst = 0; unc = 0; rec = []
    for n in range(b, NMAX, q):
        m = minG(n)
        if m is None:
            unc += 1
            if unc <= 5: rec.append(n)
        elif m > worst:
            worst = m
    print(name, "| uncovered (min G > GMAX):", unc, "examples", rec, "| max min-G among covered:", worst)
