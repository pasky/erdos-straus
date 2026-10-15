"""R244 partial from-scratch check of 'with l <= 23 only two binary patterns remain' (k = 105, labels {4,-2}).
Pool (subset of the author's): D_q (q <= 10^6 prime), II2 (prime-power-free f <= 3e5), II1 (4ab <= 3e5); only classes whose
period L_M is supported on primes <= 23.  Prints uncovered patterns (as the set of l carrying label -2)."""
import itertools
from math import gcd
import sympy as sp
K = 105; S = [2, 3, 5, 7, 11, 13, 17, 19, 23]; SS = set(S)
oc = {}
def Lsupp(m):
    L = 1
    for q, e in sp.factorint(m).items():
        if (q, e) not in oc: oc[(q, e)] = int(sp.n_order(4, q ** e))
        L = sp.ilcm(L, oc[(q, e)])
    L = int(L); f = sp.factorint(L)
    return (L, f) if set(f) <= SS else (None, None)
classes = []  # (M2, m, r, L, f)
def add(M, r):
    a = 0; m = M
    while m % 2 == 0: m //= 2; a += 1
    if m == 1 or (K - r) % 2 ** a: return
    L, f = Lsupp(m)
    if L: classes.append((m, r % m, f))
for q in sp.primerange(11, 10 ** 6):
    if K % q: add(q, 0)
for f in sp.primerange(3, 300000):
    if f % 4 == 3:
        mm = (f + 1) // 4
        for a in sp.divisors(mm):
            for d in sp.divisors(mm // a): add(f, -4 * a * a * d)
for a in range(1, 300000 // 4 + 1):
    for b in range(a, 300000 // (4 * a) + 1):
        for e in sp.divisors(a + b):
            if gcd(e, 4 * a * b) == 1: add(4 * a * b, -e)
print('classes with support <= 23:', len(classes))
unc = []
for sig in itertools.product((4, -2), repeat=len(S)):
    lab = dict(zip(S, sig)); hit = False
    for m, r, f in classes:
        mods = [l ** e for l, e in f.items()]
        mu = int(sp.ntheory.modular.crt(mods, [lab[l] % x for l, x in zip(f, mods)])[0]) if mods else 0
        if (pow(4, mu, m) + K - r) % m == 0: hit = True; break
    if not hit: unc.append([l for l in S if lab[l] == -2])
print('uncovered patterns (B-set):', len(unc), unc)
