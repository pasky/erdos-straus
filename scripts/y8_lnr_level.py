# y8: the least-non-residue level. q = lnr(p) (p = 1 mod 4 prime), t0 = -p^{-1} mod q in [1, q-1], so q | t0 p + 1.
# Test: does level t0 carry a chi=-1 word whose A contains q (A = q d, d | (t0 p+1)/q, A = -1 mod t0)?
# Reports success rate by range and by q; lists failures (first few).
import sys, random
from sympy import legendre_symbol as L, isprime, divisors
lo, hi, cnt, seed = map(int, sys.argv[1:5]); random.seed(seed)
from collections import defaultdict
st = defaultdict(lambda: [0, 0]); fails = []
n = 0
while n < cnt:
    p = random.randrange(lo, hi) | 1
    if p % 4 != 1 or not isprime(p): continue
    n += 1
    q = next(r for r in range(2, p) if L(r, p) == -1)
    t0 = (-pow(p, -1, q)) % q
    M = (t0*p+1)//q
    ok = any((q*d+1) % t0 == 0 for d in divisors(M))   # (q d / p) = (q/p)(d/p); need (A/p)=-1: check exactly below
    ok = any((q*d+1) % t0 == 0 and L((q*d) % p, p) == -1 for d in divisors(M))
    st[min(q, 13)][0] += 1; st[min(q, 13)][1] += ok
    if not ok and len(fails) < 12: fails.append((p, q, t0))
for k in sorted(st): print("q", k, "primes", st[k][0], "lnr-level success %.3f" % (st[k][1]/st[k][0]))
print("failures (p, q, t0):", fails)
# second pass: among primes with q >= 11, first k with level t0 + k q carrying such a word (k <= 40)
from collections import Counter
fk = Counter(); n = 0; random.seed(seed + 100)
while n < cnt // 3:
    p = random.randrange(lo, hi) | 1
    if p % 4 != 1 or not isprime(p): continue
    q = next(r for r in range(2, 200) if L(r, p) == -1)
    if q < 11: continue
    n += 1; t0 = (-pow(p, -1, q)) % q
    for k in range(41):
        t = t0 + k*q; M = (t*p+1)//q
        if any((q*d+1) % t == 0 and L((q*d) % p, p) == -1 for d in divisors(M)): fk[k] += 1; break
    else: fk['>40'] += 1
print("q>=11: first k distribution:", dict(sorted(fk.items(), key=lambda x: (isinstance(x[0], str), x[0]))))
