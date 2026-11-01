# Z2765: order complex Euler characteristic of the poset of partial certificates.
# Poset P_p = L3(p) (the A-values of level-3 words) ordered by divisibility of A (integers), with the reduced
# Euler characteristic chi~ = sum_k (-1)^k #(k-chains) - 1 (empty chain), i.e. mu(0^,1^) for the bounded version.
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
res = []
def chains_count(P):
    # count chains (all sizes) by length
    P = sorted(P)
    less = {a: [b for b in P if b != a and b % a == 0] for a in P}
    cnt = {}
    def rec(last, k):
        cnt[k] = cnt.get(k, 0) + 1
        for b in less[last]:
            rec(b, k+1)
    for a in P: rec(a, 1)
    return cnt
for p in L.primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 3000):
    if p < 17 or p % 8 != 1: continue
    P = L.L3(p)
    if not P: continue
    cnt = chains_count(P)
    chi = sum((-1)**(k-1) * c for k, c in cnt.items())  # Euler char of order complex (chains of length k -> simplex dim k-1)
    res.append((p, len(P), chi))
from collections import Counter
print("primes", len(res), "distribution of chi(order complex):", Counter(r[2] for r in res))
print("min chi/max chi:", min(r[2] for r in res), max(r[2] for r in res))
print("divisibility among L3 happens?:", sum(1 for r in res if r[1] != 0 and r[2] != r[1]))
for r in res[:15]: print(r)
