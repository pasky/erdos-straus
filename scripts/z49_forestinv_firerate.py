#!/usr/bin/env python3
"""z49 forestinv — per-line fire rates of the sign-free union by residue class of n (CERTIFIED numbers; §3.3).

For each population of 400 integers n ≈ 10⁶ (primes or composites in a fixed class mod 24 and gcd with 35), and each
line v ∈ V = 4Z ∪ (8Z+7), 4 ≤ v ≤ 200, gcd(v,n) = 1: does n+v have a divisor ≡ −1 (mod v)?  Rates are split by v mod 3.
"""
import sys
from math import gcd
from collections import Counter
from sympy import isprime
sys.path.insert(0, "scripts")
from z49_forestinv_words import words_at_vertex, inV

N0 = 1000000; r0 = N0 % 24

def seq(res, cond, k=400):
    n = N0 + ((res - r0) % 24); out = []
    while len(out) < k:
        if cond(n): out.append(n)
        n += 24
    return out

def stats(ns, label):
    fire = Counter(); tot = Counter(); allfire = 0
    for n in ns:
        f = False
        for v in range(4, 201):
            if not inV(v, n) or gcd(v, n) > 1: continue
            key = v % 3; tot[key] += 1
            if words_at_vertex(n, v): fire[key] += 1; f = True
        allfire += f
    print(f"{label:28s} fire rate by v mod 3: " + "  ".join(f"{k}: {fire[k]/tot[k]:.3f} ({tot[k]} lines)" for k in sorted(tot))
          + f"   P(some coprime line ≤ 200 fires) = {allfire/len(ns):.4f}")

def main():
    stats(seq(1, isprime), "p ≡ 1 (24) prime")
    stats(seq(17, isprime), "p ≡ 17 (24) prime")
    stats(seq(1, lambda n: not isprime(n) and n % 5 and n % 7), "n ≡ 1 (24) composite ⊥ 35")
    stats(seq(17, lambda n: not isprime(n) and n % 5 and n % 7), "n ≡ 17 (24) composite ⊥ 35")
    stats(seq(9, lambda n: not isprime(n) and n % 5 and n % 7), "n ≡ 9 (24) [3|n] ⊥ 35")
    stats(seq(1, lambda n: not isprime(n) and n % 5 == 0 and n % 7), "n ≡ 1 (24), 5|n, ⊥ 7")
    stats(seq(9, lambda n: not isprime(n) and n % 5 == 0 and n % 7 == 0), "n ≡ 9 (24), 105|n")

if __name__ == "__main__":
    main()
