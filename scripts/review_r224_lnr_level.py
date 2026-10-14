# R224: success of the lnr level (Lemma 3.2 / §3 numerics), from scratch.
# Primes p with lnr(p) >= 11 are exactly p = 1,121,169,289,361,529 (mod 840) (checked in review_r224_lemmas.py), so we
# sample those classes directly (uniform random p in the range, then accept primes), giving many more q >= 11 primes.
# Success at level t: exists A = q*d, d | (tp+1)/q, A = -1 (mod t), (A/p) = -1.
import sys, random
from collections import Counter, defaultdict
from sympy import isprime, factorint
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def divs(n):
    ds = [1]
    for r, e in factorint(n).items(): ds = [d * r ** i for d in ds for i in range(e + 1)]
    return ds
lo, hi, cnt, seed = int(float(sys.argv[1])), int(float(sys.argv[2])), int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed); C = (1, 121, 169, 289, 361, 529)
st = defaultdict(lambda: [0, 0]); fk = Counter(); n = 0; pred = [0, 0]
while n < cnt:
    p = rng.randrange(lo // 840, hi // 840) * 840 + rng.choice(C)
    if not isprime(p): continue
    n += 1
    q = 11
    while leg(q, p) == 1: q += 2
    while not isprime(q) or leg(q, p) == 1: q += 2    # least non-residue is prime
    t0 = (-pow(p, -1, q)) % q
    pred[0] += 1; pred[1] += (q + 1) % t0 == 0       # d = 1 works  <=>  t0 | q+1
    first = None
    for k in range(61):
        t = t0 + k * q
        ok = any((q * d + 1) % t == 0 and leg(q * d, p) == -1 for d in divs((t * p + 1) // q))
        if ok: first = k; break
    key = 11 if q == 11 else 13
    st[key][0] += 1; st[key][1] += (first == 0)
    fk[first if first is not None else '>60'] += 1
print("range [%g, %g), %d primes with lnr >= 11" % (lo, hi, n))
for k in sorted(st): s = st[k]; print("  q %s: %d primes, lnr-level (k = 0) success %.3f +- %.3f" % ("11" if k == 11 else ">=13", s[0], s[1] / s[0], (s[1] / s[0] * (1 - s[1] / s[0]) / s[0]) ** .5))
print("  t0 | q+1 fraction %.3f" % (pred[1] / pred[0]))
print("  first k:", dict(sorted(fk.items(), key=lambda x: (isinstance(x[0], str), x[0]))))
