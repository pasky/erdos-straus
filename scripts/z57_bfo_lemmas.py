# z57 BFO: numerical sanity checks of the reformulation lemmas of Z57_BFO.md §1-§2 (small sizes, exhaustive).
# Run: uv run --with sympy python scripts/z57_bfo_lemmas.py
from sympy import isprime, jacobi_symbol, primerange
from math import gcd

def sols(n):
    """all (o, e, C) with o odd, e even, 4oeC - o - e = n (brute force over o, e)."""
    out = []
    for o in range(1, n + 1, 2):
        if 4 * o * 2 - o - 2 > n: break
        for e in range(2, n + 1, 2):
            v = n + o + e
            if 4 * o * e > v: break
            if v % (4 * o * e) == 0: out.append((o, e, v // (4 * o * e)))
    return out

# L1.1: N(n) = #{(s,t): 4st | n+s+t} equals 2 * #solutions for odd n
bad = 0
for n in range(3, 1200, 2):
    N = sum(1 for s in range(1, n + 2) for t in range(1, n + 2) if 4 * s * t <= n + s + t and (n + s + t) % (4 * s * t) == 0)
    bad += N != 2 * len(sols(n))
print("L1.1 shift form, odd n<1200: mismatches", bad)

# L1.2: R(n)>=1 iff exists s>=1 and m | n+s with m = -1 mod 4s
bad = 0
for n in range(3, 3000, 2):
    a = len(sols(n)) > 0
    b = any((n + s) % m == 0 for s in range(1, n + 1) for m in range(4 * s - 1, n + s + 1, 4 * s))
    bad += a != b
print("L1.2 divisor-in-class form, odd n<3000: mismatches", bad)

# L1.3 level form: solutions at level C <-> divisors d of 4Cn+1 with d = -1 mod 4C (d = 4Co-1 for the odd-or-even entry)
bad = 0
for n in range(5, 3000, 4):
    S = sols(n)
    Cs = set(C for (_, _, C) in S)
    for C in range(1, n + 1):
        N = 4 * C * n + 1
        ds = [d for d in range(4 * C - 1, N + 1, 4 * C) if N % d == 0]
        if len(ds) != 2 * sum(1 for x in S if x[2] == C): bad += 1
print("L1.3 level form, n=1(4)<3000, all C: mismatches", bad)

# L1.4 levels with 64C^3 <= p lie in G* (Q^4 > P p), primes p=1(4) < 200000 via level scan
bad = 0; cnt = 0
for p in primerange(5, 200000):
    if p % 4 != 1: continue
    C = 1
    while 64 * C ** 3 <= p:
        N = 4 * C * p + 1; d = 4 * C - 1
        while d * d <= N:
            if N % d == 0:
                o1, o2 = (d + 1) // (4 * C), (N // d + 1) // (4 * C)
                P, Q = min(o1, o2), max(o1, o2); cnt += 1
                if not Q ** 4 > P * p: bad += 1
            d += 4 * C
        C += 1
print("L1.4 complete levels in G*: solutions checked", cnt, "violations", bad)

# L1.5 mod-p form: R(p)>=1 iff exists o,e,C>=1 with p | 4oeC-o-e and 0 < 4oeC-o-e < 2p
bad = 0
for p in primerange(5, 1500):
    if p % 4 != 1: continue
    a = len(sols(p)) > 0
    b = False
    for o in range(1, 2 * p):
        for e in range(1, 2 * p):
            if 4 * o * e - o - e >= 2 * p + 4 * o * e: break
            for C in range(1, 2 * p):
                v = 4 * o * e * C - o - e
                if v >= 2 * p: break
                if v > 0 and v % p == 0: b = True; break
            if b or 4 * o * e - o - e >= 2 * p: break
        if b: break
    bad += a != b
print("L1.5 mod-p form, primes p=1(4)<1500: mismatches", bad)

# L1.6 Jacobi: every solution at prime p has ((4Co-1)/p) = ((4Ce-1)/p) = -1; odd squares have no solutions
bad = 0; cnt = 0
for p in primerange(5, 6000):
    if p % 4 != 1: continue
    for (o, e, C) in sols(p):
        cnt += 1
        bad += jacobi_symbol(4 * C * o - 1, p) != -1 or jacobi_symbol(4 * C * e - 1, p) != -1
sq = sum(len(sols(m * m)) for m in range(3, 80, 2))
print("L1.6 Jacobi at primes<6000: solutions", cnt, "violations", bad, "; solutions at odd squares 9..77^2:", sq)

# L2.2 genus-exact moduli: (Z/4m)^x has exponent <= 2 iff 4m | 24
def expo2(q): return all(pow(a, 2, q) == 1 for a in range(1, q) if gcd(a, q) == 1)
ex = [m for m in range(1, 2000) if expo2(4 * m)]
print("L2.2 m<2000 with (Z/4m)^x of exponent <=2:", ex)

# L2.3 Carmichael: q with lambda(q) | k are exactly the divisors of Lambda(k) (k = 2,4,6,12)
def lam_divides(q, k): return all(pow(a, k, q) == 1 for a in range(1, q) if gcd(a, q) == 1)
for k in (2, 4, 6, 12):
    qs = [q for q in range(1, 20000) if lam_divides(q, k)]
    print(f"L2.3 k={k}: moduli q<20000 with lambda(q)|k: count {len(qs)}, max {max(qs)}")
