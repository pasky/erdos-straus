"""review_zl_sample.py -- R231 round 2: pick primes from zl_sweep ZL_BIN dumps (one or more split runs over the same [X0, X1),
summed), print "n JP JQ" for: the argmax-(JP+JQ) prime of every cell j >= jmin, plus NRAND random primes (seeded), half of them in
cells >= jfocus.  Own reader of the uint16 layout (JP[M], JQ[M], index (n - X0') >> 1, X0' = X0 | 1).
Usage: review_zl_sample.py X0 X1 jmin jfocus NRAND seed bin1 [bin2 ...]"""
import sys, array, random
from sympy import isprime
X0, X1, jmin, jfocus, NR, seed = map(int, sys.argv[1:7])
X0o = X0 | 1; M = (X1 - X0o + 1) // 2 + 1
JP = [0] * M; JQ = [0] * M
for fn in sys.argv[7:]:
    a = array.array('H'); a.frombytes(open(fn, 'rb').read()); assert len(a) == 2 * M, (fn, len(a), 2 * M)
    for i in range(M): JP[i] += a[i]; JQ[i] += a[M + i]
def cp(j):
    n = max(1, int(2 ** (j / 32)) - 2)
    while n ** 32 < 2 ** j: n += 1
    return n
out = set()
j = jmin
while cp(j) < X1:
    lo, hi = max(cp(j), X0o), min(cp(j + 1), X1)
    best = max((JP[(n - X0o) >> 1] + JQ[(n - X0o) >> 1], n) for n in range(lo | 1, hi, 2) if isprime(n))
    out.add(best[1]); j += 1
random.seed(seed)
lof = cp(jfocus)
while len(out) < NR + (j - jmin):
    n = random.randrange(lof if len(out) % 2 else X0o, X1) | 1
    if isprime(n): out.add(n)
for n in sorted(out): print(n, JP[(n - X0o) >> 1], JQ[(n - X0o) >> 1])
