"""z52d pass2 fix, TO0b: Z0087 (|S|=1 mechanism, extended j for l = 193, 337) and Z0218 (size of M = xy+yz+zx for ES triples)."""
import math, sys
from fractions import Fraction as Fr
sys.path.insert(0, 'scripts')
out = []
import subprocess
def factor_small(n):
    # trial division up to 10^6 then Pollard rho (n up to ~1e20)
    import random
    def is_prime(n):
        if n < 2: return False
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if n % p == 0: return n == p
        d = n - 1; s = 0
        while d % 2 == 0: d //= 2; s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, n)
            if x in (1, n - 1): continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1: break
            else: return False
        return True
    def rho(n):
        if n % 2 == 0: return 2
        while True:
            c = random.randrange(1, n); f = lambda x: (x * x + c) % n
            x = y = random.randrange(2, n); d = 1
            while d == 1:
                x = f(x); y = f(f(y)); d = math.gcd(abs(x - y), n)
            if d != n: return d
    fac = {}
    def rec(n):
        if n == 1: return
        if is_prime(n): fac[n] = fac.get(n, 0) + 1; return
        d = rho(n); rec(d); rec(n // d)
    rec(n)
    return fac
def divisors_from(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def primes_upto(N):
    return [q for q in range(3, N) if all(q % d for d in range(2, int(q ** .5) + 1))]
found = {}
for l in [193, 337] + [q for q in primes_upto(400) if q not in (193, 337)][:0]:
    for j in range(1, 13):
        N = l ** j + 1
        fac = factor_small(N)
        ds = [d for d in divisors_from(fac) if d % 4 == 3]
        if ds:
            found[l] = (j, min(ds)); break
out.append(f'Z0087: l=193 -> {found.get(193)}, l=337 -> {found.get(337)} (j <= 12; divisor e=3 mod 4 of 1+l^j; Lemma 3.1 with eta=l^j, kappa=(1+l^j)/e, u=kappa/eta, v=kappa)')
# all primes below 400 with j<=12 (factoring by rho): summary
miss = []
for l in primes_upto(400):
    if l == 2: continue
    ok = False
    for j in range(1, 13):
        fac = factor_small(l ** j + 1)
        if any(d % 4 == 3 for d in divisors_from(fac)):
            ok = True; break
    if not ok: miss.append(l)
out.append(f'Z0087: odd primes l<400 with NO e=3 mod 4 divisor of 1+l^j for j<=12: {miss} (count {len(miss)})')
# Z0218: size of M for ES triples
def triples(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        for y in range(max(x, math.floor(1 / r) + 1), math.floor(2 / r) + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1 and s_.denominator >= y:
                res.append((x, y, s_.denominator))
    return res
IDON_MAX = 1848
Ms = []
for p in [q for q in range(5, 301) if all(q % d for d in range(2, int(q ** .5) + 1))]:
    for t in triples(p):
        Ms.append(t[0]*t[1]+t[1]*t[2]+t[2]*t[0])
small = [m for m in Ms if m <= IDON_MAX]
out.append(f'Z0218: M values over {len(Ms)} ES triples (p<=300): min M = {min(Ms)}, median {sorted(Ms)[len(Ms)//2]}; M <= 1848 (largest known idoneal): {len(small)} triples')
out.append(f'  for M in the known idoneal list the idoneal test is only meaningful when M<=1848 (list complete there by the literature; Weinberger: at most one more idoneal number exists)')
print('\n'.join(out))
open('data/z52b/pass2/TO0b/fix_Z0087_Z0218.txt', 'w').write('\n'.join(out) + '\n')
