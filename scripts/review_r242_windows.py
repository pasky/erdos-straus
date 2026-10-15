"""R242: independent recomputation of CAP_DOWN §5 window caps.
Usage: review_r242_windows.py N M mode   (mode = primes | all)
For each relevant n <= N, least m <= M (m = -n mod 4, gcd(K, n) = 1, K = (n+m)/4) with a Lemma-1.1 divisor
d = prod_{s|K} s^{c_s}, d = -K (mod m), c_2 <= 2 b_2, odd s: c_s <= 2 b_s or (c_s even, c_s <= 2 b_s + 2e).
Every reported solution is rebuilt as (x, y, z) = (K, nA, nKA/d) and checked against Def 1.1 independently.
"""
import sys
from math import isqrt
from fractions import Fraction
from review_r242_common import spf_sieve, factor, check_def11

N, M, MODE = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
spf = spf_sieve(N + M)


def find_d(n, m, e):
    K = (n + m) // 4
    fk = factor(K, spf)
    if any(n % s == 0 for s in fk):
        return None
    reach = {1 % m: ()}  # residue -> tuple of exponents
    items = list(fk.items())
    for s, b in items:
        cs = set(range(0, 2 * b + 1))
        if s != 2 and e > 0:
            cs |= set(range(0, 2 * b + 2 * e + 1, 2))
        new = {}
        for r, ex in reach.items():
            for c in sorted(cs):
                rr = r * pow(s, c, m) % m
                if rr not in new:
                    new[rr] = ex + (c,)
        reach = new
    tgt = (-K) % m
    if tgt not in reach:
        return None
    d = 1
    for (s, b), c in zip(items, reach[tgt]):
        d *= s ** c
    A = (K + d) // m
    assert (K + d) % m == 0
    cap = check_def11(n, K, n * A, Fraction(n * K * A, d), e, [s for s in fk])
    return cap, d


def relevant(n):
    if n % 4 != 1:
        return False
    if isqrt(n) ** 2 == n:
        return False
    f = factor(n, spf)
    if MODE == 'primes':
        return len(f) == 1 and f.get(n) == 1
    return all(p % 4 == 1 for p in f)


cnt = 0
hist = {}
worst0 = (0, 0)
worst1 = (0, 0)
bad = []
for n in range(5, N + 1, 4):
    if not relevant(n):
        continue
    cnt += 1
    w0 = None
    for m in range(3, M + 1, 4):
        if find_d(n, m, 0):
            w0 = m
            break
    if w0 is not None:
        hist[0] = hist.get(0, 0) + 1
        worst0 = max(worst0, (w0, n))
        for m in range(3, w0 + 1, 4):
            if find_d(n, m, 1):
                worst1 = max(worst1, (m, n))
                break
        continue
    best = None
    for e in range(1, 50):
        for m in range(3, M + 1, 4):
            if find_d(n, m, e):
                best = (e, m)
                break
        if best:
            break
    bad.append((n, best))
    hist[best[0]] = hist.get(best[0], 0) + 1
print('N', N, 'M', M, 'mode', MODE, 'count', cnt)
print('least-cap histogram', hist)
print('max least cap-0 window (m, n):', worst0, ' max least cap<=1 window:', worst1)
print('n without cap-0 window <= M: (n, (cap, m))', bad)
