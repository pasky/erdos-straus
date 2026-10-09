"""O98: brute check of M17C Lemma 2.1 on all N-points of Sigma^I_F (a<=b), for given F.
Enumerates (a,c,d) with F/4 < acd <= 3F/4, f = 4acd-F | 4a^2 d+1 (M17 §3 definition of Q data, without 17|e filter),
checks 4abd = eF+1, f | aF+c, f | F^2+4c^2 d, and that each (a,d) carries <= 2 points.
Usage: m17c_qcheck.py F
"""
import sys
from collections import Counter
F = int(sys.argv[1]); per = Counter(); n = 0
for a in range(1, 3 * F // 4 + 1):
    for d in range(1, 3 * F // (4 * a) + 1):
        t = 4 * a * a * d + 1
        for c in range(F // (4 * a * d) + 1, 3 * F // (4 * a * d) + 1):
            f = 4 * a * c * d - F
            if f <= 0 or t % f: continue
            e = t // f
            num = F * a + c
            if num % f: continue
            b = num // f
            if b < a: continue
            assert (a + b) % c == 0 and (a + b) // c == e
            assert 4 * a * b * d == e * F + 1 and (F * F + 4 * c * c * d) % f == 0
            assert 4 * a * b * c * d == F * (a + b) + c
            per[(a, d)] += 1; n += 1
print(F, "points", n, "max per (a,d)", max(per.values()) if per else 0)
