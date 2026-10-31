#!/usr/bin/env python3
"""U07 interesting items. Z1917: residues of the nine E_a^4 failures ≤10^6 listed in PARITY_AUDIT.md (~line 308).
Z2347: Riemann–Hurwitz check: 2g-2 = |G|(p-4)/p for a group with ES triangle signature (x,y,z), 1/x+1/y+1/z = 4/p."""
from collections import Counter
from fractions import Fraction as F
ps = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]
print("Z1917 residues mod 24 counts:", Counter(p % 24 for p in ps))
print("Z1917 all ≡1 mod 24:", all(p % 24 == 1 for p in ps))
# Z2347: for p prime, |G| with 2g-2 integer and >=0 requires p | |G|; check on small sample of valid (p,|G|)
bad = []
for p in [5, 7, 11, 13, 17, 19, 23]:
    for G in range(1, 3 * p * 4):
        val = F(G * (p - 4), p)
        if val.denominator == 1 and val % 2 == 0 and val >= 0 and G % p != 0:
            bad.append((p, G))
print("Z2347: (p,|G|) with |G|(p-4)/p an even nonnegative integer but p ∤ |G| (should be empty):", bad)
