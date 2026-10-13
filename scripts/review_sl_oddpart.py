"""R175 from-scratch: bsB_redei_oddpart numerics. Primes n = 1 mod 4 in [A,B); t in list; divisors m'' of tn+1
with 4 | (tn+1)/m''. Check (m''/n) = (m''/t) (Jacobi) and tabulate classes m'' mod t among (m''/t) = -1."""
import sys
from collections import Counter
from review_sl_rayclass import jac  # own Jacobi (R175 file)
def primes(a, b):
    s = bytearray([1]) * b; s[0] = s[1] = 0
    for i in range(2, int(b ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [x for x in range(a, b) if s[x]]
def divisors(m):
    f = {}; d = 2
    while d * d <= m:
        while m % d == 0: f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    ds = [1]
    for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
    return ds
A, B = int(sys.argv[1]), int(sys.argv[2])
ns = [n for n in primes(A, B) if n % 4 == 1]
for t in [7, 11, 19, 23, 31]:
    viol = 0; cl = Counter()
    for n in ns:
        M = t * n + 1
        for d in divisors(M):
            if (M // d) % 4: continue
            if jac(d, n) != jac(d, t): viol += 1
            if jac(d, t) == -1: cl[d % t] += 1
    tot = sum(cl.values())
    sh = {k: round(v / tot, 3) for k, v in sorted(cl.items())}
    print(f"t={t} violations={viol} class shares {sh}  share(-1)={sh.get(t-1)} max={max(sh.values())} min={min(sh.values())}")
