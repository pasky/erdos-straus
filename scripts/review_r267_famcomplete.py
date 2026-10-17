"""R267: completeness of level L when ALL one-parameter Type I/II polynomial families (slice + ET Prop 1.9 shapes,
re-derived for numerator k; see review_r267_families.py) are allowed, versus slice classes only.
Usage: review_r267_famcomplete.py k L [L ...]"""
import sys
from math import gcd
import numpy as np
sys.path.insert(0, "scripts")
from review_r267_complete import divisors, covered_mod_H


def family_classes(k, L):
    """yield (modulus m | L, residue set) for non-slice families with modulus dividing L."""
    D = divisors(L)
    out = []
    for f in D:                      # II-2: f = kacd - 1 | L
        if (f + 1) % k == 0:
            acd = (f + 1) // k
            for a in divisors(acd):
                for d in divisors(acd // a):
                    out.append((f, {(-k * a * a * d) % f}))
    for M in D:                      # II-3: kade | L ; I-1: kad | L
        if M % k: continue
        q = M // k
        for a in divisors(q):
            for d in divisors(q // a):
                e = q // (a * d)
                if gcd(k * a * d, e) == 1:
                    out.append((M, {(-k * a * a * d - e) % M}))
                for e1 in divisors(k * a * a * d + 1):
                    out.append((k * a * d, {(-(k * a * a * d + 1) // e1) % (k * a * d)}))
    for M in D:                      # I-2: kac*f | L, I-3: kcd*f | L
        if M % k: continue
        for kx in divisors(M // k):
            m1 = k * kx; f = M // m1
            if gcd(m1, f) != 1: continue
            for a in divisors(kx):   # I-2 with a*c = kx
                c = kx // a
                if f == 1:
                    out.append((m1, {(-1) % m1})); continue
                if gcd(a, f) != 1: continue
                r2 = (-c * pow(a, -1, f)) % f
                out.append((M, {x for x in range(M) if x % m1 == (-f) % m1 and x % f == r2}))
            for c in divisors(kx):   # I-3 with c*d = kx
                d = kx // c
                if f == 1: continue
                out.append((M, {x for x in range(M) if x % m1 == (-f) % m1 and (x * x + k * c * c * d) % f == 0}))
    return out


def deficits(k, L):
    r = np.arange(L); unit = np.gcd(r, L) == 1
    sq = np.zeros(L, bool); sq[(r[unit] ** 2) % L] = True
    cov = np.zeros(L, bool)
    for H in divisors(L):
        S = covered_mod_H(k, H)
        if S: cov |= np.isin(r % H, np.fromiter(S, int))
    slice_def = int((unit & ~sq & ~cov).sum())
    for m, S in family_classes(k, L):
        cov |= np.isin(r % m, np.fromiter(S, int))
    bad = int((cov & sq & unit).sum())
    return slice_def, int((unit & ~sq & ~cov).sum()), bad


if __name__ == "__main__":
    k = int(sys.argv[1])
    for L in map(int, sys.argv[2:]):
        s, f, b = deficits(k, L)
        print(f"k={k} L={L}: uncovered non-square unit classes slice-only={s}, with families={f}, square classes covered={b}")
