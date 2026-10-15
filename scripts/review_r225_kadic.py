# R225 from-scratch checks for NEAR_SQUARE §3 (j = 8 by default):
#  (1) the escaping example 4/2801;  (2) local unit-square test for pi = m - sqrt(j) in Z_l[sqrt j];
#  (3) coverage of m mod L by ET Prop 1.9 congruence families + a family file (from review_r225_famsearch.py dump);
#  compare uncovered classes (n = 1 mod 4) with the Z_K^+ prediction.
import sys
from fractions import Fraction as F
from math import gcd
from itertools import product
def isprime(n): return n > 1 and all(n % p for p in range(2, int(n**.5) + 1))
assert F(4, 2801) == F(1, 29421704) + F(1, 702) + F(1, 283608) and isprime(2801) and 2801 == 53**2 - 8
print('4/2801 identity OK, 2801 prime')
j = int(sys.argv[1]); L = int(sys.argv[2]); famfile = sys.argv[3] if len(sys.argv) > 3 else None
def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
# ---- (2) unit square test: is m - sqrt(j) a unit square in Z_l[sqrt j] (tested modulo l^P, coefficientwise) ----
def is_unit_square(m, l, P):
    M = l ** P
    if (m * m - j) % l == 0: return False
    t = (m % M, (-1) % M)
    for a in range(M):
        for b in range(M):
            if ((a * a + j * b * b - t[0]) % M == 0) and ((2 * a * b - t[1]) % M == 0): return True
    return False
# precision: odd l: P = 1 (Hensel); l = 2: P = 4 (2^4 = (sqrt2)^8 > 4*(sqrt2)); valid since j=8: Z2[sqrt8] vs Z2[sqrt2]
# -- for l = 2 we test squares in Z_2[sqrt2] (the maximal order) by writing sqrt j = f*sqrt j0:
def is_unit_square_2(m):
    # K_2 = Q_2(sqrt j0), j = f^2 j0;  element m - f sqrt(j0); test x^2 = it modulo 2^5 in Z_2[sqrt j0] (j0 = 2 or 3 or ...)
    jf = factor(j); j0 = 1; f = 1
    for p, e in jf.items(): j0 *= p ** (e % 2); f *= p ** (e // 2)
    if (m * m - j) % 2 == 0: return False
    M = 2 ** 5
    for a in range(M):
        for b in range(M):
            if (a * a + j0 * b * b - m) % M == 0 and (2 * a * b + f) % M == 0: return True
    # also allow O_K = Z[(1+sqrt j0)/2] when j0 = 1 mod 4: test with half-integers
    if j0 % 4 == 1:
        for a in range(2 * M):
            for b in range(2 * M):
                if (a - b) % 2: continue
                if (a * a + j0 * b * b - 4 * m) % (4 * M) == 0 and (2 * a * b + 4 * f) % (4 * M) == 0: return True
    return False
Lf = factor(L)
def meets_ZK(g):
    for l, e in Lf.items():
        if l == 2:
            if e < 5: raise SystemExit('need 2^5 | L')
            if not is_unit_square_2(g % 32): return False
        else:
            if not is_unit_square(g % l, l, 1): return False
    return True
print('local condition at 2 holds for m mod 32 in', [g for g in range(32) if is_unit_square_2(g)])
for l in Lf:
    if l > 2: print('local condition at', l, ':', [g for g in range(l) if is_unit_square(g, l, 1)])
# ---- (3) congruence coverage (ET Prop 1.9), residues of n mod L ----
divs = [d for d in range(1, L + 1) if L % d == 0]
cov = set()
def add_class(r, q):  # n = r mod q, q | L
    for t in range(L // q): cov.add((r + q * t) % L)
for q in divs:
    if q % 4: continue
    Q = q // 4
    for a in range(1, Q + 1):
        if Q % a: continue
        for d in range(1, Q // a + 1):
            if (Q // a) % d: continue
            if a * d == Q:   # family 1: n = -f mod 4ad, f | 4a^2 d + 1
                N1 = 4 * a * a * d + 1
                for f in range(1, N1 + 1):
                    if N1 % f == 0: add_class(-f, q)
    for a, b in product(range(1, Q + 1), repeat=2):   # families 4 and 5: 4ab = q
        if a * b != Q: continue
        for e in range(1, a + b + 1):
            if (a + b) % e or gcd(e, 4 * a * b) != 1: continue
            add_class(-pow(e, -1, q), q); add_class(-e, q)
for q in divs:   # family 2: n = -f mod 4ac, n = -c/a mod f, (4ac,f)=1, modulus 4acf | L ; family 3 similarly
    for f in divs:
        if q % 4 or (q * f) > L or L % (q * f) or gcd(q, f) != 1: continue
        Q = q // 4
        for a in range(1, Q + 1):
            if Q % a: continue
            c = Q // a
            if gcd(a, f) != 1: continue
            r1 = (-f) % q; r2 = (-c * pow(a, -1, f)) % f if f > 1 else 0
            # CRT
            r = next(x for x in range(r2, q * f, f) if x % q == r1) if f > 1 else r1
            add_class(r, q * f)
        for c in range(1, Q + 1):     # family 3: 4cd = q, n^2 = -4c^2 d mod f
            if Q % c: continue
            d = Q // c
            for r in range(0, q * f):
                if r % q == (-f) % q and (r * r + 4 * c * c * d) % f == 0: add_class(r, q * f)
for f in divs:   # family 6: n = -4a^2 d mod f, 4ad | f + 1
    for a in range(1, f + 2):
        if (f + 1) % (4 * a): continue
        for d in range(1, (f + 1) // (4 * a) + 1):
            if ((f + 1) // (4 * a)) % d == 0: add_class(-4 * a * a * d, f)
for q in divs:   # family 7: n = -4a^2 d - e mod 4ade, (4ad, e) = 1
    if q % 4: continue
    Q = q // 4
    for a in range(1, Q + 1):
        for d in range(1, Q + 1):
            if Q % (a * d): continue
            e = Q // (a * d)
            if gcd(4 * a * d, e) == 1: add_class(-4 * a * a * d - e, q)
mcov = {g for g in range(L) if (g * g - j) % L in cov}
print('congruence families cover', len(mcov), 'of', L, 'm-classes')
# ---- polynomial families from file ----
nf = used = 0; sets = set()
if famfile:
    for line in open(famfile):
        parts = line.split(); nf += 1
        polys = [[F(x) for x in p.split(',')] for p in parts[1:]]
        den = 1
        for p in polys:
            for c in p: den = den * c.denominator // gcd(den, c.denominator)
        if L % den: continue
        used += 1
        ints = [[int(c * den) for c in p] for p in polys]
        S = [g for g in range(den) if all(sum(c * pow(g, i, den) for i, c in enumerate(q)) % den == 0 for q in ints)]
        if S: sets.add((den, tuple(S)))
    for den, S in sets:
        Sset = set(S)
        for g in range(L):
            if g % den in Sset: mcov.add(g)
print('family file:', nf, 'families,', used, 'with denominators | L; total covered', len(mcov))
unc = [g for g in range(L) if g not in mcov and (g * g - j) % 4 == 1]
pred = [g for g in range(L) if meets_ZK(g)]
print('uncovered (n = 1 mod 4):', len(unc), ' Z_K^+ classes:', len(pred), ' Z_K^+ subset of uncovered:', set(pred) <= set(unc))
extra = [g for g in unc if g not in pred]
print('uncovered minus Z_K^+ :', len(extra), 'with n unit at all l | L:', len([g for g in extra if gcd(g * g - j, L) == 1]))
print('  sample', [(g, {l: g % l ** e for l, e in Lf.items()}) for g in extra[:8]])
