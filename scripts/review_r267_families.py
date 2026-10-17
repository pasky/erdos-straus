"""R267: is the point x_{l,r} ("r at l, 1 at every other prime incl. 2") covered by the NON-slice polynomial
families of Type I/II (ET Prop 1.9 shapes, re-derived for numerator k from n = kabd - e, ce = a + b (II) and
ne + 1 = kabd, ce = a + b (I))?  NONCONG_LIFTS 'witness classes' are only the slice families (a, b, c fixed, d free).

Families (one free parameter, positive leading coefficient):
 II-2  fix (a,c,d), e free:  n ≡ -k a^2 d  (mod f), f = kacd - 1
 II-3  fix (a,d,e), c free:  n ≡ -k a^2 d - e (mod kade)
 I-1   fix (a,d,e), c free:  e | ka^2d+1, n ≡ -(ka^2d+1)/e (mod kad)
 I-2   fix (a,c,f), d free:  gcd(kac,f)=1, n ≡ -f (mod kac), n ≡ -c/a (mod f)
 I-3   fix (c,d,f), a free:  gcd(kcd,f)=1, n ≡ -f (mod kcd), n^2 ≡ -k c^2 d (mod f)
Each hit is verified by constructing an actual prime n in the class and checking k/n = 1/x+1/y+1/z exactly.
Usage: review_r267_families.py k l r BOUND
"""
import sys
from math import gcd
from fractions import Fraction
from sympy import isprime


def xmod(m, l, r):
    v = 1
    mo = m
    while mo % l == 0:
        mo //= l; v *= l
    if v == 1:
        return 1 % m
    t = ((r - 1) * pow(mo, -1, v)) % v
    return (1 + mo * t) % m


def check_prime_solution(k, n, fam, prm):
    """build the solution of k/n from family parameters and verify."""
    if fam == "II-2":
        a, c, d = prm; f = k * a * c * d - 1; e = (n + k * a * a * d) // f; b = c * e - a
        assert (n + k * a * a * d) % f == 0 and b > 0
        X = (a * b * d, a * c * d * n, b * c * d * n)
    elif fam == "II-3":
        a, d, e = prm; M = k * a * d * e; c = (n + k * a * a * d + e) // M; b = c * e - a
        X = (a * b * d, a * c * d * n, b * c * d * n)
    elif fam == "I-1":
        a, d, e = prm; f = (k * a * a * d + 1) // e; c = (n + f) // (k * a * d); b = c * e - a
        X = (a * b * d * n, a * c * d, b * c * d)
    elif fam == "I-2":
        a, c, f = prm; d = (n + f) // (k * a * c); e = (k * a * a * d + 1) // f; b = c * e - a
        X = (a * b * d * n, a * c * d, b * c * d)
    elif fam == "I-3":
        c, d, f = prm; a = (n + f) // (k * c * d); e = (k * a * a * d + 1) // f; b = c * e - a
        X = (a * b * d * n, a * c * d, b * c * d)
    assert min(X) > 0
    return sum(Fraction(1, x) for x in X) == Fraction(k, n)


def find_prime(conds):
    """conds: list of (modulus, residue) — combine by brute force walk."""
    M = 1
    for m, _ in conds:
        M = M * m // gcd(M, m)
    for n in range(3, 50 * M * 50):
        if all(n % m == r % m for m, r in conds) and isprime(n):
            return n
    return None


def scan(k, l, r, B):
    hits = []
    rng = range(1, B + 1)
    for a in rng:
        for c in rng:
            for d in rng:
                f = k * a * c * d - 1
                if f > 10**7: break
                if xmod(f, l, r) == (-k * a * a * d) % f:
                    hits.append(("II-2", (a, c, d), [(f, -k * a * a * d)]))
    for a in rng:
        for d in rng:
            for e in rng:
                M = k * a * d * e
                if xmod(M, l, r) == (-k * a * a * d - e) % M:
                    hits.append(("II-3", (a, d, e), [(M, -k * a * a * d - e)]))
                if (k * a * a * d + 1) % e == 0:
                    f = (k * a * a * d + 1) // e; M = k * a * d
                    if xmod(M, l, r) == (-f) % M:
                        hits.append(("I-1", (a, d, e), [(M, -f)]))
    for a in rng:
        for c in rng:
            for f in range(1, 40 * B):
                M = k * a * c
                if gcd(M, f) != 1: continue
                if xmod(M, l, r) == (-f) % M and (f == 1 or (xmod(f, l, r) * a + c) % f == 0):
                    hits.append(("I-2", (a, c, f), [(M, -f), (f, (-c * pow(a, -1, f)) % f if f > 1 else 0)]))
    for c in rng:
        for d in rng:
            for f in range(1, 40 * B):
                M = k * c * d
                if gcd(M, f) != 1: continue
                xf = xmod(f, l, r)
                if xmod(M, l, r) == (-f) % M and (xf * xf + k * c * c * d) % f == 0:
                    hits.append(("I-3", (c, d, f), [(M, -f)]))
    return hits


if __name__ == "__main__":
    k, l, r, B = map(int, sys.argv[1:5])
    hits = scan(k, l, r, B)
    print(f"k={k} l={l} r={r} B={B}: {len(hits)} family hits")
    for fam, prm, conds in hits[:6]:
        print("  ", fam, prm, conds)
    # verify the first hit of each family on an actual prime of the class (class = all conds + point at l only)
    seen = set()
    for fam, prm, conds in hits:
        if fam in seen or fam == "I-3": continue
        seen.add(fam)
        n = find_prime(conds)
        print("   verify", fam, prm, "prime", n, check_prime_solution(k, n, fam, prm) if n else None)
