#!/usr/bin/env python3
"""Z1595: classify (*) level failures (no d | 4Cp+1 with d ≡ -1 mod 4C) at Mordell-hard primes:
 (a) subgroup obstruction: -1 not in <classes of prime factors>;  (b) -1 in the subgroup but not in the divisor set D.
 Also Kneser stabiliser H = {h : hD = D} of D and |D| vs the Kneser-type bound."""
import math, collections
from sympy import factorint, primerange
hard = {1, 121, 169, 289, 361, 529}
ps = [p for p in primerange(10**6, 10**6 + 400000) if p % 840 in hard][:200]
stats = collections.Counter(); stab = collections.Counter(); ratio = []
for p in ps:
    for C in range(1, 101):
        m = 4*C; N = m*p + 1; f = factorint(N)
        D = {1}
        for q, e in f.items():
            D = {(d * pow(q, j, m)) % m for d in D for j in range(e + 1)}
        if (m - 1) in D: stats['hit'] += 1; continue
        G = {1}; frontier = [1]
        gens = [q % m for q in f]
        while frontier:
            x = frontier.pop(); 
            for g in gens:
                y = x*g % m
                if y not in G: G.add(y); frontier.append(y)
        typ = 'a: -1 not in <primes>' if (m - 1) not in G else 'b: -1 in <primes>, not in D'
        stats[typ] += 1
        H = [h for h in G if {(h*d) % m for d in D} == D]
        stab[(typ[0], 'H trivial' if len(H) == 1 else 'H nontrivial')] += 1
        if typ[0] == 'b': ratio.append(len(D) / len(G))
print("primes:", len(ps), ps[0], ps[-1], " levels C<=100")
for k, v in stats.items(): print(f"  {k}: {v}")
for k, v in sorted(stab.items()): print("  stabiliser", k, v)
ratio.sort(); print("  type b: |D|/|<primes>| quartiles", [round(ratio[int(len(ratio)*t)], 3) for t in (0.1, 0.25, 0.5, 0.75, 0.9)])
