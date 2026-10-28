#!/usr/bin/env python3
"""z49 forestinv — numerical checks of the PROVED structural lemmas of FOREST_INVERSE.md §2.

L1 (decomposition): words (t,u,v) of n with gcd(u,v) = g  ⟷  words (gt, u/g, v/g) of n/g with coprime endpoints.
L2 (non-coprime vertex line): for g = gcd(v,n), v is an endpoint of a word of n ⟺ n/g + v/g has a divisor ≡ −1 (mod v).
L3 (factorization words): n = ab has a word (t, a, a·s) ⟺ b + 1 = (ta − 1)s;  these are all words with u | n.
L4 (diagonal words): n has a word (t,u,u) ⟺ u | n and u | n/u + 2;  then tu − 1 = (n/u) + 1.
L5 (level form): U(n) ⟺ ∃ t, ∃ A | tn+1 with A ≡ −1 (mod t) and (A+1)/t ∈ V.
Numerator-8 control: at n = 17, 241 no word has an endpoint ≡ 0 (mod 8).
"""
import sys
from math import gcd, isqrt
sys.path.insert(0, "scripts")
from z49_forestinv_words import all_words, divisors, inV, U

def main():
    bad = {k: 0 for k in "L1 L2 L3 L4 L5".split()}
    for n in range(9, 1202, 8):
        W = set(all_words(n))                       # (t,u,v) all orderings
        # L1
        for (t, u, v) in W:
            g = gcd(u, v)
            if g > 1:
                if n % g or (g * t, u // g, v // g) not in set(all_words(n // g)): bad["L1"] += 1
        for g in divisors(n):
            if g == 1 or g == n: continue
            for (t2, u2, v2) in all_words(n // g):
                if t2 % g == 0 and gcd(u2, v2) == 1 and (t2 // g, g * u2, g * v2) not in W: bad["L1"] += 1
        # L2
        ends = set(v for (_, _, v) in W)
        for v in range(1, n + 3):
            g = gcd(v, n)
            crit = any((A + 1) % v == 0 for A in divisors(n // g + v // g))
            if crit != (v in ends): bad["L2"] += 1
        # L3
        for a in divisors(n):
            if a == 1 or a == n: continue
            b = n // a
            wordsA = set((t, u, v) for (t, u, v) in W if u == a)
            pred = set()
            for D in divisors(b + 1):
                if (D + 1) % a == 0:
                    pred.add(((D + 1) // a, a, a * ((b + 1) // D)))
            if wordsA != pred: bad["L3"] += 1
        # L4
        diag = set((t, u) for (t, u, v) in W if u == v)
        pred = set()
        for u in divisors(n):
            if (n // u + 2) % u == 0:
                pred.add(((n // u + 2) // u, u))
        if diag != pred: bad["L4"] += 1
        # L5
        lvl = False
        for t in range(1, n + 3):
            for A in divisors(t * n + 1):
                if (A + 1) % t == 0 and inV((A + 1) // t, n): lvl = True; break
            if lvl: break
        if lvl != U(n): bad["L5"] += 1
    print("n ≡ 1 (mod 8), 9 ≤ n ≤ 1201:", bad)
    for n in (17, 241):
        W8 = [(t, u, v) for (t, u, v) in all_words(n) if u % 8 == 0 or v % 8 == 0]
        print(f"numerator-8 control n={n}: words with an endpoint ≡ 0 (mod 8): {W8}")

if __name__ == "__main__":
    main()
