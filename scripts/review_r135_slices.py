"""R135 from-scratch check of Lemma 1.1 (e-slice parametrisation) of LONGSHOT_PIGEONHOLE.md.

(1) For primes p < PMAX_COUNT: enumerate ALL ordered (x,y,z) with 4/p = 1/x+1/y+1/z, classify by how many of
    x,y,z are divisible by p, and compare with fibre counts sum_e #{(a,b): ab | N_e, e | a+b}.
    Type I  (p divides exactly one)  <-> N = (pe+1)/4 ; ordered triples counted with the p-multiple placed in
             any of 3 positions -> 3 * fibre count.
    Type II (p divides exactly two)  <-> N = (p+e)/4 ; likewise 3 * fibre count.
(2) For all primes 3 < p < 2000: ES(p) by direct solver  <=>  some e-slice has -1 in Sigma_e(N).
No author code reused.
"""
import sys
from math import gcd, isqrt
from fractions import Fraction


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]


def all_solutions(p):
    """ordered triples (x,y,z) with 4/p = 1/x+1/y+1/z."""
    out = []
    # x <= y <= z first
    x = p // 4 + 1
    while 4 * x <= 3 * p:  # 1/x >= 4/(3p)
        r = Fraction(4, p) - Fraction(1, x)
        if r > 0:
            # 1/y + 1/z = r, y <= z: y in [1/r, 2/r]
            y = max(x, int(1 / r))
            while Fraction(2, y) >= r:
                s = r - Fraction(1, y)
                if s > 0 and s.numerator == 1 and s.denominator >= y:
                    out.append((x, y, s.denominator))
                y += 1
        x += 1
    full = set()
    from itertools import permutations
    for t in out:
        for q in permutations(t):
            full.add(q)
    return full


def divisors(n):
    ds = [1]
    m = n; f = 2
    while f * f <= m:
        if m % f == 0:
            k = 0
            while m % f == 0: m //= f; k += 1
            ds = [d * f**i for d in ds for i in range(k + 1)]
        f += 1
    if m > 1: ds = [d * m**i for d in ds for i in range(2)]
    return ds


def fibre(N, e, coprime=False):
    """#{(a,b) ordered: ab | N, e | a+b} (optionally gcd(a,b)=1)."""
    cnt = 0
    for a in divisors(N):
        for b in divisors(N // a):
            if (a + b) % e == 0 and (not coprime or gcd(a, b) == 1): cnt += 1
    return cnt


def check_counts(p):
    sols = all_solutions(p)
    nI = sum(1 for t in sols if sum(v % p == 0 for v in t) == 1)
    nII = sum(1 for t in sols if sum(v % p == 0 for v in t) == 2)
    other = len(sols) - nI - nII
    zmax = max(max(t) for t in sols)
    # bound for e: Type I x = abdp and 4abd = pe+1 -> e < 4x/p^2 <= 4 zmax/p^2 ; Type II: e <= a+b <= N+1
    fI = fII = fIall = fIIall = 0
    for e in range(1, 4 * zmax // (p * p) + 2):
        if (p * e + 1) % 4 == 0 and e % p:
            fI += fibre((p * e + 1) // 4, e, True); fIall += fibre((p * e + 1) // 4, e)
    for e in range(1, p + 5):
        if (p + e) % 4 == 0 and e % p:
            fII += fibre((p + e) // 4, e, True); fIIall += fibre((p + e) // 4, e)
    return nI, nII, other, 3 * fI, 3 * fII, 3 * fIall, 3 * fIIall


def es_direct(p):
    x = p // 4 + 1
    while 4 * x <= 3 * p:
        r = Fraction(4, p) - Fraction(1, x)
        y = max(x, r.denominator // r.numerator)
        while Fraction(2, y) >= r:
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1: return True
            y += 1
        x += 1
    return False


def es_slice(p):
    for e in range(1, p + 5):  # Type II, e <= (p+4)/3 suffices
        if (p + e) % 4 == 0 and e % p and fibre((p + e) // 4, e): return True
    e = 1
    while e < 50 * p:  # Type I
        if (p * e + 1) % 4 == 0 and fibre((p * e + 1) // 4, e): return True
        e += 1
    return False


if __name__ == "__main__":
    PC = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    bad = 0
    for p in primes_upto(PC):
        if p < 5: continue
        r = check_counts(p)
        ok = r[2] == 0 and r[0] == r[3] and r[1] == r[4]
        bad += not ok
        print(p, r, "OK" if ok else "MISMATCH")
    print("count-check mismatches:", bad)
    bad2 = 0
    for p in primes_upto(2000):
        if p < 5: continue
        a, b = es_direct(p), es_slice(p)
        if a != b or not a: bad2 += 1; print("ES mismatch", p, a, b)
    print("ES<=>slice mismatches (p<2000):", bad2)
