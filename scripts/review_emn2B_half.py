"""R102B: from-scratch L_{1/2}(m): log N at which the proportion of m-representable primes in
(N/2, N] (all primes, p not | m, no sampling unless stride>1) first reaches 1/2 on the grid
N = 2^(j/4); linear interpolation in L = log N. Uses review_emn2B_brute.representable.
Usage: review_emn2B_half.py m1,m2,... [stride]"""
import sys, math
from review_emn2B_brute import representable, primes_in

ms = [int(x) for x in sys.argv[1].split(',')]
stride = int(sys.argv[2]) if len(sys.argv) > 2 else 1
for m in ms:
    j = max(16, int(4 * math.log2(m / 2))); prev = None; rows = []
    while True:
        N = int(2 ** (j / 4)); L = math.log(N)
        ps = [p for p in primes_in(N // 2, N) if m % p][::stride]
        f = sum(representable(m, p) for p in ps) / len(ps)
        rows.append('%.2f:%.3f' % (L, f))
        if f >= 0.5:
            Lh = L if prev is None else prev[0] + (L - prev[0]) * (0.5 - prev[1]) / max(f - prev[1], 1e-9)
            break
        prev = (L, f); j += 1
    print('%4d L_.5=%.3f ratio=%.3f  grid %s' % (m, Lh, Lh / m ** (1 / 3), ' '.join(rows[-3:])), flush=True)
