"""z58 LIT: F3 probe suggested by the negative-Pell analogy (Legendre: x^2 - p y^2 = -1 solvable for every prime p ≡ 1 (4);
fails at squares; fails at composites with a prime factor ≡ 3 (4) and at ~42% of the others, Koymans–Pagano).

Question (EVIDENCE only): are the 285 composite (★)-zeros (R(n) = 0) enriched, relative to random non-square composites
n ≡ 1 (4) of the same size, in (a) n having a prime factor ≡ 3 (mod 4); (b) negative-Pell failure among n whose odd prime
factors are all ≡ 1 (4)?  Negative Pell: solvable iff the continued-fraction period of sqrt(n) is odd.
Run: ulimit -v 4000000; timeout 1200 uv run --with sympy python scripts/z58_lit_negpell_f3.py
"""
import random
from math import isqrt
from sympy import factorint

def cf_period_len(n):
    a0 = isqrt(n)
    m, d, a, L = 0, 1, a0, 0
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        L += 1
        if a == 2 * a0:
            return L

def classify(n):
    f = factorint(n)
    has3 = any(p % 4 == 3 for p in f)
    sqf = all(e == 1 for e in f.values())
    return has3, sqf

zeros = [int(l.split()[0]) for l in open("data/z58/screens/composite_zeros_le8e6.txt") if l.strip() and not l.startswith("#")]
assert len(zeros) == 285

def stats(ns, label):
    n3 = npell_ok = n1 = 0
    for n in ns:
        has3, sqf = classify(n)
        if has3:
            n3 += 1
        else:
            n1 += 1
            if cf_period_len(n) % 2 == 1:
                npell_ok += 1
    print(f"{label}: N={len(ns)}  frac with prime factor ≡3(4) = {n3/len(ns):.3f}  "
          f"| among all-≡1(4): {n1}, negPell solvable {npell_ok} ({npell_ok/max(n1,1):.3f})")

# sanity: Legendre on primes p ≡ 1 (4) < 2e5, and squares
from sympy import primerange
bad = [p for p in primerange(5, 200000) if p % 4 == 1 and cf_period_len(p) % 2 == 0]
print("primes p≡1(4) <2e5 with negative Pell unsolvable:", bad[:5], len(bad))

stats(zeros, "composite (★)-zeros ≤ 8e6")
big = [n for n in zeros if n >= 10**5]
stats(big, "composite (★)-zeros in [1e5, 8e6]")

random.seed(58)
def control(lo, hi, k):
    out = []
    while len(out) < k:
        n = random.randrange(lo, hi) | 1
        if n % 4 != 1:
            continue
        r = isqrt(n)
        if r * r == n:
            continue
        f = factorint(n)
        if len(f) == 1 and list(f.values())[0] == 1:
            continue  # prime
        out.append(n)
    return out
stats(control(10**5, 8 * 10**6, 20000), "control: random non-square composites ≡1(4) in [1e5, 8e6]")
