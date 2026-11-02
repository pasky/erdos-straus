"""z54 UPPER2 lemma checks (memo Z54_UPPER2.md §1-§2).

L1  Lemma R: x is a coordinate of a word of n  <=>  (U) n+x has a divisor = -1 mod x, or (T) xn+1 has one.
    Checked against brute-force word enumeration for all n = 1 (mod 4), n <= NMAX, all x <= n+2.
L2  Lemma J: for every word of n (n = 1 mod 8, n prime) and every coordinate x in C_n, the odd part d' of the
    corresponding level d satisfies Jacobi (n/d') = -1.  (levels: x=u -> d = t*u-1 ; x=t -> both d=tu-1, d*=tv-1.)
L3  Lemma 5: HC(p)=3 for p = 5 mod 8, HC(p) >= 4 for p = 1 mod 8; the explicit words.
L4  Word constructions used by the sieve: for prime q = -1 mod x, 4|x, n = -x mod q: ((q+1)/x, x, (n+x)/q) is a word.
"""
import sys
from sympy import divisors, isprime, jacobi_symbol, primerange

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000


def words(n):
    out = []
    for t in range(1, n + 3):
        for u in range(1, n + 3):
            A = t * u - 1
            if A < 1:
                continue
            if A > n + u:
                break
            if (n + u) % A == 0:
                out.append((t, u, (n + u) // A))
    return out


def inC(x, n):
    return x % 4 == 0 or (x + n) % 8 == 0


def U(n, x):
    return x >= 2 and any(d % x == x - 1 for d in divisors(n + x))


def T(n, x):
    return x >= 2 and any(d % x == x - 1 for d in divisors(x * n + 1))


def oddpart(d):
    while d % 2 == 0:
        d //= 2
    return d


bad = 0
nw = 0
for n in range(5, NMAX + 1, 4):
    W = words(n)
    nw += len(W)
    coords = set()
    for (t, u, v) in W:
        assert t * u * v - u - v == n
        coords |= {t, u, v}
    for x in range(2, n + 3):
        pred = U(n, x) or T(n, x)
        if pred != (x in coords):
            bad += 1
            print("L1 mismatch", n, x, pred, x in coords)
    # x = 1 is a coordinate always (t=1 words exist: d | n+1, d>=1) -- outside C_n anyway
print(f"L1: n=1 mod 4, n<={NMAX}: {nw} words, mismatches {bad}")

# L2 Jacobi law on primes
viol = 0
checked = 0
for p in primerange(17, NMAX * 3):
    if p % 8 != 1:
        continue
    for (t, u, v) in words(p):
        for (x, levels) in ((u, [t * u - 1]), (v, [t * v - 1]), (t, [t * u - 1, t * v - 1])):
            if inC(x, p):
                for d in levels:
                    checked += 1
                    if jacobi_symbol(p, oddpart(d)) != -1:
                        viol += 1
                        print("L2 violation", p, (t, u, v), x, d)
print(f"L2: primes p=1 mod 8 < {NMAX*3}: {checked} (coordinate-in-C, level) pairs, Jacobi violations {viol}")

# L3
bad3 = 0
for p in primerange(5, 200000):
    if p % 8 == 5:
        t, u, v = 1, 3, (p + 3) // 2
        bad3 += (t * u * v - u - v != p)
    if p % 8 == 1:
        bad3 += any(inC(x, p) for x in (1, 2, 3))
    if p % 24 == 17:
        bad3 += not (U(p, 4))
print(f"L3: bad {bad3}")

# L4
bad4 = 0
cnt4 = 0
for x in range(4, 101, 4):
    for q in primerange(3, 3000):
        if q % x != x - 1:
            continue
        for n in range(1, 4 * q * 8, 4):
            if (n + x) % q == 0:
                t, u, v = (q + 1) // x, x, (n + x) // q
                cnt4 += 1
                bad4 += (t * u * v - u - v != n) or min(t, u, v) < 1
print(f"L4: {cnt4} constructions, bad {bad4}")
