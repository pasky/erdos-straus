"""R126 from-scratch re-run of GEOMETRY_ES §5.3 fixed-level experiments (independent code).
(1) level sets (all d occurring) of Type I / Type II solutions for named primes, via full enumeration
    from review_geo_genus.solutions;
(2) Type II level d=1: p ≡ 1 (24), p < PMAX2: exists a <= sqrt(p)/2+1, f | p+4a^2, f ≡ -1 (mod 4a)?
(3) Type I level d: p ≡ 1 (24), p < PMAX1, (-d/p) = -1: exists a,c with acd <= 3p/4, f = 4acd-p > 0,
    f | 4a^2 d + 1, gcd(c,p) = 1?   (complete by ET Lemma 2.8)
Also checks Prop 4.1 counterexample: c = 0 integral points on Sigma^I_{p,d}."""
import sys
from math import gcd, isqrt
import numpy as np
from sympy import primerange
from review_geo_genus import solutions, legendre

def levels(p):
    I, II = set(), set()
    for u in solutions(p):
        div = [x % p == 0 for x in u]
        if sum(div) == 1:
            x = u[div.index(True)]; y, z = [u[m] for m in range(3) if not div[m]]
            I.add(gcd(gcd(x // p, y), z))
        else:
            x = u[div.index(False)]; y, z = [u[m] for m in range(3) if div[m]]
            II.add(gcd(gcd(x, y // p), z // p))
    # normalise by squares is unnecessary: d = gcd(...) is ET's d (a,b,c without common factor)
    return sorted(I), sorted(II)

for p in (73, 97, 193, 673):
    print('levels', p, 'TypeI', levels(p)[0], 'TypeII', levels(p)[1])

PMAX2 = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
N = PMAX2 + 4 * (isqrt(PMAX2) // 2 + 2) ** 2 + 10
spf = np.zeros(N, dtype=np.int64)
for q in range(2, isqrt(N) + 1):
    if spf[q] == 0:
        blk = spf[q * q::q]; blk[blk == 0] = q
spf_l = spf.tolist()
def divs(m):
    out = [1]
    while m > 1:
        q = spf_l[m] or m; k = 0
        while m % q == 0: m //= q; k += 1
        out = [x * q ** i for x in out for i in range(k + 1)]
    return out
fails2 = []; cnt = 0
for p in primerange(5, PMAX2):
    if p % 24 != 1: continue
    cnt += 1
    ok = False
    for a in range(1, isqrt(p) // 2 + 2):
        if any((f + 1) % (4 * a) == 0 for f in divs(p + 4 * a * a)):
            ok = True; break
    if not ok: fails2.append(p)
print('TypeII d=1: primes', cnt, 'failures', len(fails2), fails2[:12], '...', fails2[-3:])

PMAX1 = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
for d in (5, 7, 11, 13):
    tot = 0; fl = []
    for p in primerange(5, PMAX1):
        if p % 24 != 1 or legendre(-d, p) != -1: continue
        tot += 1; ok = False
        for a in range(1, 3 * p // (4 * d) + 1):
            cmax = 3 * p // (4 * a * d)
            if cmax < 1: break
            c = np.arange(1, cmax + 1, dtype=np.int64)
            f = 4 * a * c * d - p
            m = 4 * a * a * d + 1
            good = (f > 0) & (np.mod(m, np.maximum(f, 1)) == 0) & (np.mod(c, p) != 0)
            if good.any(): ok = True; break
        if not ok: fl.append(p)
    print(f'TypeI d={d}: primes {tot} failures {len(fl)}', fl[:8])

# Prop 4.1 check: integral points with c = 0 on Sigma^I_{p,d}
p, d = 5, 1
pts = [(-(4*d*a*a+1)//p, -p, a) for a in range(1, 40) if (4*d*a*a+1) % p == 0]
assert all(e*f - 4*d*a*a == 1 for e, f, a in pts)
print('Sigma^I_{5,1}(Z) with c=0 (e,f,a):', pts[:6], '... (infinite family a ≡ ±1 mod 5)')
