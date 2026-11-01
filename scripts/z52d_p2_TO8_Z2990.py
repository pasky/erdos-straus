# z52d P2 TO8 Z2990 (congruences of R(p)/2) and Z2921 (parity of half-counts H_C)
import math
from collections import defaultdict, Counter
D = 'data/z52b/pass2/TO8/'
R = {}
for l in open(D + 'R_all_1e6.txt'):
    p, r, _ = l.split(); R[int(p)] = int(r)
ps = sorted(p for p in R if p > 5)
# Z2990: is R(p)/2 mod m determined by p mod M?  Report fraction of residue classes with a single value.
for M in [24, 120, 168, 840]:
    for m in [2, 3, 4, 8]:
        cls = defaultdict(Counter)
        for p in ps:
            cls[p % M][(R[p] // 2) % m] += 1
        det = sum(1 for c in cls.values() if len(c) == 1)
        # classes with >=50 primes and value distribution spread
        big = [c for k, c in cls.items() if sum(c.values()) >= 50]
        spread = sum(1 for c in big if len(c) == m)
        print(f"M={M} m={m}: classes={len(cls)} determined={det} ; classes(n>=50) with all {m} values present={spread}/{len(big)}")
# Z2921: parity of R(p)/2 and of half-counts
cnt = Counter((R[p] // 2) % 2 for p in ps)
print("R(p)/2 mod 2 distribution:", dict(cnt), " R(p) mod 4 distribution:", Counter(R[p] % 4 for p in ps))
