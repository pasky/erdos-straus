"""Independent consistency checks for paper/es-hc-note.tex.

Run:  timeout 900 uv run --with sympy python paper/es-hc-note.check.py

Every check is a finite computation; output is printed and should end with
'ALL CHECKS PASSED'.  Nothing here is used in any proof of the note; the
checks only guard against algebraic slips in the statements.
"""
from fractions import Fraction
from math import gcd
import random
import sys

from sympy import divisors, factorint, isprime, jacobi_symbol, primerange

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def in_C(x, n):
    return x % 4 == 0 or (x - (-n)) % 8 == 0


def words(n):
    """All (t,u,v) in N^3 with t*u*v - u - v = n (Lemma 2.1: u <= n+2)."""
    out = []
    for u in range(1, n + 3):
        # v*(t*u-1) = n+u ; d = t*u-1 runs over divisors of n+u with d = -1 mod u
        for d in divisors(n + u):
            if (d + 1) % u == 0:
                t = (d + 1) // u
                v = (n + u) // d
                if t >= 1:
                    out.append((t, u, v))
    return out


def es_solution(t, u, v, n):
    """Explicit solution of 4/n = 1/x+1/y+1/z from a slot (Prop 2.2)."""
    A, As = t * u - 1, t * v - 1
    if t % 4 == 0:
        s = t // 4
        return (s * u * v, n * s * v, n * s * u)
    if u % 4 == 0:
        r = u // 4
        return (r * As, t * n * r, t * n * r * As)
    if v % 4 == 0:
        r = v // 4
        return (r * A, t * n * r, t * n * r * A)
    if A % 4 == 0:
        a = A // 4
        return (a * v, a * v * As, n * a * As)
    if As % 4 == 0:
        a = As // 4
        return (a * u, a * u * A, n * a * A)
    return None


def line_fires(c, n):
    """Lemma 2.3: c is a coordinate iff n+c or c*n+1 has a divisor = -1 mod c."""
    return any((d + 1) % c == 0 for d in divisors(n + c)) or any(
        (d + 1) % c == 0 for d in divisors(c * n + 1)
    )


def HC(n, cmax=None):
    cmax = cmax or (n + 2)
    for c in range(3, cmax + 1):
        if in_C(c, n) and line_fires(c, n):
            return c
    return None


# 1. Words, slots, explicit identities, lines, HC, reciprocity (small n)
nwords = nslots = 0
for n in range(5, 1200, 4):  # all n = 1 mod 4 (primes and composites)
    W = words(n)
    coords = set()
    for (t, u, v) in W:
        check(t * u * v - u - v == n, f"word {n}")
        nwords += 1
        A, As = t * u - 1, t * v - 1
        slot = any(z % 4 == 0 for z in (t, u, v, A, As))
        coord = any(in_C(z, n) for z in (t, u, v))
        check(slot == coord, f"Prop2.2 equivalence n={n} {(t,u,v)}")
        if slot:
            nslots += 1
            x, y, z = es_solution(t, u, v, n)
            check(Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n),
                  f"identity n={n} {(t,u,v)}")
        coords.update((t, u, v))
    for c in range(2, n + 3):
        check((c in coords) == line_fires(c, n), f"Lemma2.3 n={n} c={c}")
    hc_words = min([c for c in coords if in_C(c, n)], default=None)
    check(hc_words == HC(n), f"HC def n={n}")
print(f"[1] words/slots/identities/lines: {nwords} words, {nslots} slot words, n<1200")

# 2. Lemma 2.7 (Jacobi (d/n) = -1 for every certificate divisor), all n = 1 mod 4
ncert = 0
for n in range(5, 3000, 4):
    for c in range(3, 80):
        if not in_C(c, n):
            continue
        for N in (n + c, c * n + 1):
            for d in divisors(N):
                if (d + 1) % c == 0:
                    ncert += 1
                    check(jacobi_symbol(d, n) == -1, f"reciprocity n={n} c={c} d={d}")
print(f"[2] reciprocity: {ncert} certificate divisors, n<3000, c<80")

# 3. Odd squares: no coordinate in C at all
for m in range(3, 46, 2):
    check(HC(m * m) is None, f"square {m}^2 has a certificate")
print("[3] odd squares m^2, m<46: no certificate")

# 4. HC=3 iff p=5 mod 8; HC=4 criterion; Prop 3.1 words
for p in primerange(11, 200000):
    if p % 4 != 1:
        continue
    if p % 8 == 5:
        check(HC(p, 3) == 3, f"HC=3 p={p}")
        continue
    h4 = line_fires(4, p)
    crit = any(q % 4 == 3 for q in list(factorint(p + 4)) + list(factorint(4 * p + 1)))
    check(h4 == crit, f"HC=4 criterion p={p}")
    nonres = (p % 3 == 2) or (p % 5 in (2, 3)) or (p % 7 in (3, 5, 6))
    check(nonres == (p % 840 not in (1, 121, 169, 289, 361, 529)), f"Mordell classes p={p}")
    if nonres:
        h = HC(p, 8)
        check(h is not None and h <= 8, f"Prop3.1 p={p}")
print("[4] p<2e5: HC=3 / HC=4 criterion / Prop 3.1")

# 5. Theorem Q members: p = 5m^2+1, 4|m prime => 12|m, p+4, 4p+1 in S, HC >= 7
cnt = 0
for m in range(4, 20000, 4):
    p = 5 * m * m + 1
    if isprime(p):
        cnt += 1
        check(m % 12 == 0 and p % 8 == 1, f"ThmQ m={m}")
        check(all(q % 4 == 1 for q in factorint(p + 4)) and
              all(q % 4 == 1 for q in factorint(4 * p + 1)), f"ThmQ S m={m}")
        check(not line_fires(4, p), f"ThmQ line4 m={m}")
print(f"[5] Theorem Q: {cnt} members with m<20000")

# 6. Records of the census (independent recomputation of HC, incl. minimality)
REC = {21841: 64, 691681: 56, 407188321: 52, 3014346241: 55, 33257638801: 55,
       424252771849: 52, 511526736361: 55, 712917322849: 55, 818789590249: 60,
       828405178561: 52, 844772955601: 56, 915805615201: 55}
for p, h in REC.items():
    check(isprime(p) and p % 8 == 1, f"record prime {p}")
    check(HC(p, 200) == h, f"record HC({p})={h}")
print(f"[6] {len(REC)} census records with HC>=52 recomputed")

# 7. Theorem N (no small-support certificate on a non-square class): random primes
#    p = 1 mod M, p = R mod l^J, every certificate (c,d), c <= C, has a prime factor
#    of d outside S u {primes <= Y}.  (Probable primes: evidence only.)
random.seed(1)
for (ell, R, C, Y) in [(11, 2, 24, 13), (13, 2, 24, 13), (17, 3, 20, 11)]:
    small = [q for q in primerange(2, Y + 1) if q != ell]
    M = 1
    for q in small:
        a = 1
        while q ** a <= C + 1:
            a += 1
        if q == 2:
            a = max(a, 3)
        M *= q ** a
    J = 1
    while ell ** J <= R * (C + 1):
        J += 1
    mod = M * ell ** J
    # CRT: p = 1 mod M, p = R mod ell^J
    base = (1 + M * ((R - 1) * pow(M, -1, ell ** J) % ell ** J)) % mod
    found = 0
    k = random.randrange(1, 10 ** 3)
    while found < 3:
        p = base + k * mod
        k += 1
        if not isprime(p):
            continue
        found += 1
        allowed = set(small) | {ell}
        for c in range(3, C + 1):
            if not in_C(c, p):
                continue
            for N in (p + c, c * p + 1):
                for d in divisors(N):
                    if (d + 1) % c == 0:
                        check(not set(factorint(d)) <= allowed,
                              f"ThmN ell={ell} p={p} c={c} d={d}")
print("[7] Theorem N random samples (probable primes)")

if FAIL:
    print(f"{len(FAIL)} FAILURES")
    sys.exit(1)
print("ALL CHECKS PASSED")
