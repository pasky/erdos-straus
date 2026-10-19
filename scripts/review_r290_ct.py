"""R290: test FRONTIER §4 item 1 / Lemma CT claim: for p ≡ 1 (4) prime, in every solution of 4/p = 1/x+1/y+1/z,
every denominator prime to p has a prime factor l with (l/p) = -1. Independent code."""
import sys
from review_r290_spot import three_term, factor, primes_upto
def leg(a, p): return pow(a % p, (p - 1) // 2, p)
P = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
bad = []; nsol = 0
for p in primes_upto(P):
    if p % 4 != 1: continue
    for s in three_term(4, p):
        nsol += 1
        for w in s:
            if w % p and not any(leg(l, p) == p - 1 for l in factor(w)):
                bad.append((p, s, w))
print("primes p≡1(4) <", P, "solutions", nsol, "violations", len(bad), bad[:5])
