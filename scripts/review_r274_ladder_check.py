"""R274: brute-force check of review_r274_ladder.c for small p (direct a,b,d loop, c solved)."""
import sys, math, numpy as np
from sympy import primerange
def brute(m, p):
    n = 0
    for a in range(1, p + 3):
        if m*a - (a + 1) > p: break
        for b in range(1, p + 3):
            if m*a*b - (a + b) > p: break
            for d in range(1, p + 3):
                k = m*a*b*d - p
                if k > a + b: break
                if k >= 1 and (a + b) % k == 0 and math.gcd(a, (a + b)//k) == 1: n += 1
    return n
for m in (4, 5, 8, 12, 16):
    cnt = np.fromfile(f'/tmp/r274/chk{m}.bin', dtype=np.uint32)
    bad = [(p, brute(m, p), int(cnt[p])) for p in primerange(3, 600) if brute(m, p) != cnt[p]]
    print(m, 'mismatches:', bad[:5], len(bad))
