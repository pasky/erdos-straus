#!/usr/bin/env python3
"""z49 forestinv — the six U-failures and the 436 U_cop-failures ≤ 10⁸ (data/z49_forestinv/ucop_failures_1e8.txt):
factorisations, least QNR r(n) (least prime ℓ ∤ n with Jacobi (n/ℓ) = −1), nearest-square offsets, and the
relative-distance-to-nearest-square statistic  δ(n) := min(n − m², (m+1)² − n)/(2m), m = ⌊√n⌋  (uniform on [0, 1/2]
for n drawn uniformly from a long interval, median 1/4).  Also the r(n) histogram and the baseline P(r ≥ 11).
"""
import sys, statistics
from math import isqrt
from collections import Counter
from sympy import factorint, jacobi_symbol, primerange, isprime

def r(n):
    if n % 8 in (3, 5): return 2
    for l in primerange(3, 10 ** 6):
        if n % l == 0: continue
        if jacobi_symbol(n, l) == -1: return l
    return None

def nearest(n):
    m = isqrt(n); lo, hi = n - m * m, (m + 1) ** 2 - n
    return (f"{m}² + {lo}" if lo <= hi else f"{m+1}² − {hi}")

def main():
    six = [105, 2961, 3985, 25305, 111969, 978145]
    print("n | factorisation | r(n) | nearest square | n mod 24")
    for n in six:
        print(f"{n} | {factorint(n)} | {r(n)} | {nearest(n)} | {n % 24}")
    rows = [l.split() for l in open("data/z49_forestinv/ucop_failures_1e8.txt") if not l.startswith("#")]
    ns = [int(x[0]) for x in rows]
    print(f"\n{len(ns)} U_cop failures ≤ 1e8; divisible by 3: {sum(n%3==0 for n in ns)}, by 5: {sum(n%5==0 for n in ns)}, "
          f"by 7: {sum(n%7==0 for n in ns)}, coprime to 105: {sum(n%3 and n%5 and n%7 for n in ns)}")
    print("r(n) histogram:", sorted(Counter(r(n) for n in ns).items()))
    delta = [min(n - isqrt(n) ** 2, (isqrt(n) + 1) ** 2 - n) / (2 * isqrt(n)) for n in ns]
    print(f"relative distance to nearest square: median {statistics.median(delta):.3f} (uniform reference 0.250), "
          f"fraction < 0.05: {sum(d < 0.05 for d in delta)/len(delta):.3f} (uniform reference 0.100)")
    # baseline P(r ≥ 11) among composite non-square n ≡ 9 (24) with gcd(n,35)=1 near 1e6
    base = [n for n in range(1000017, 1000017 + 24 * 20000, 24) if n % 5 and n % 7 and not isprime(n) and isqrt(n) ** 2 != n]
    rs = [r(n) for n in base]
    print(f"baseline n ≡ 9 (24), ⊥35, composite non-square, {len(base)} values: P(r ≥ 11) = {sum(x >= 11 for x in rs)/len(rs):.3f} "
          f"(expected 1/4), P(r ≥ 13) = {sum(x >= 13 for x in rs)/len(rs):.3f} (expected 1/8)")
    sub = [n for n in ns if n % 5 and n % 7]
    print(f"the {len(sub)} failures with 3 | n, ⊥35: P(r ≥ 11) = {sum(r(n) >= 11 for n in sub)/len(sub):.3f}, "
          f"P(r ≥ 13) = {sum(r(n) >= 13 for n in sub)/len(sub):.3f}")

if __name__ == "__main__":
    main()
