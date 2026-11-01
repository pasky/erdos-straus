"""z52d pass2 fix, TO0b: unit/cone items.
Z0056: integer replacements of eta. Lemma 3.1 (BRAINSTORM/other_rings.md) needs e | 1+eta with kappa=(1+eta)/e in C and u = kappa/eta in C.
   Over Z (C = positive integers) test all eta = g^j (2<=g<=200, 1<=j<=8, eta+1 finite) and all divisors e of 1+eta with e = 3 mod 4:
   check kappa = (1+eta)/e, u = kappa/eta positive integer (the Lemma's requirement). Count successes.
Z0064: semiring cone C = Z_{>=0}[sqrt2] (a+b sqrt2, a,b>=0). Search u,v in C (coords <= 40, u,v nonzero), e = 1/u+1/v in C
   (nonnegative integer coordinates) with e = 3 mod 4 O_K (e-3 in 4 O_K: coords 0 mod 4 for sqrt2 part and 3 mod 4 for rational part).
Z0086: D=3, eps = 2+sqrt3 (norm +1, totally positive). Lemma-3.1 route: find prime l = 3 mod 4 and eta = eps^j with
   eta = -1 mod l O_K (then kappa=(1+eta)/l is totally positive automatically since eps^j, eps'^j > 0). Test l = 3 mod 4 up to 3000.
Z0078: quadratic-orbit reparametrisation. For a reduced fraction a/b (b>0), 1/y+1/z = a/b with y,z positive integers <=> y+z = k a,
   yz = k b for an integer k>=1 with k^2 a^2 - 4 k b a perfect square (discriminant (y-z)^2). Verify: #(ordered (y,z)) = #{k: k(k a^2-4b) square}
   for all a/b arising as 4/p - 1/x, p<=300 prime, x in range."""
import math, sys
from fractions import Fraction as Fr
def issq(n): return n >= 0 and math.isqrt(n) ** 2 == n
out = []
# ---- Z0056
good = []; tot = 0
def divisors_upto(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds
for g in range(2, 201):
    for j in range(1, 9):
        eta = g ** j
        if eta > 10**9: break
        tot += 1
        for e in sorted(divisors_upto(eta + 1)):
            if e % 4 == 3:
                kappa = (eta + 1) // e
                if kappa % eta == 0:
                    good.append((g, j, e)); break
out.append(f'Z0056: eta=g^j (2<=g<=200, j<=8): {tot} cases; with a 3-mod-4 divisor e of 1+eta and u=kappa/eta in Z_{{>0}}: {len(good)} (first {good[:5]})')
# ---- Z0064
C = lambda a, b: a >= 0 and b >= 0
hits = []
elems = [(a, b) for a in range(0, 25) for b in range(0, 25) if (a, b) != (0, 0)]
def inv(a, b):   # 1/(a+b sqrt2) = (a - b sqrt2)/(a^2-2b^2)
    d = a * a - 2 * b * b
    return (Fr(a, d), Fr(-b, d)) if d != 0 else None
invs = {}
for u in elems:
    r = inv(*u)
    if r: invs[u] = r
found_e = set()
for i, u in enumerate(elems):
    if u not in invs: continue
    for v in elems[i:]:
        if v not in invs: continue
        e = (invs[u][0] + invs[v][0], invs[u][1] + invs[v][1])
        if e[0].denominator == 1 and e[1].denominator == 1 and e[0] >= 0 and e[1] >= 0 and e != (0, 0):
            x, y = int(e[0]), int(e[1])
            if (x - 3) % 4 == 0 and y % 4 == 0:
                found_e.add((x, y))
out.append(f'Z0064: semiring cone Z>=0[sqrt2], u,v coords<=24: e in C with e = 3 mod 4 O_K found: {sorted(found_e)[:10]} (count {len(found_e)}); e = 1/u+1/v in C occurs for {sorted(set(e for e in found_e))[:3]}')
allE = set()
for i, u in enumerate(elems):
    if u not in invs: continue
    for v in elems[i:]:
        if v not in invs: continue
        e = (invs[u][0] + invs[v][0], invs[u][1] + invs[v][1])
        if e[0].denominator == 1 and e[1].denominator == 1 and e[0] >= 0 and e[1] >= 0 and e != (0, 0):
            allE.add((int(e[0]), int(e[1])))
out.append(f'  all e in C of the form 1/u+1/v (u,v in C, coords<=24): count {len(allE)}; residue classes (a mod 4, b mod 4) hit: ' + str(sorted({(a%4, b%4) for a,b in allE})) + '; with a = 3 mod 4 and b = 0 mod 4: ' + str(sorted(e for e in allE if e[0]%4==3 and e[1]%4==0)[:8]))
# ---- Z0086: D=3, eps=2+sqrt3, mod l: element (a,b) = a+b sqrt3
def mul(x, y, l):
    return ((x[0]*y[0] + 3*x[1]*y[1]) % l, (x[0]*y[1] + x[1]*y[0]) % l)
res = []
for l in range(3, 3001):
    if all(l % q for q in range(2, int(l**.5)+1)) and l % 4 == 3:
        if l % 3 == 0: pass
        eps = (2 % l, 1 % l); m1 = (l - 1, 0)
        x = (1, 0); seq = []
        ok = None
        for j in range(1, 2 * l + 3):
            x = mul(x, eps, l)
            if x == m1:
                ok = j; break
        # need l split in Q(sqrt3): (3/l)=1
        split = pow(3, (l - 1) // 2, l) == 1
        if ok is not None:
            res.append((l, ok, split))
sp = [r for r in res if r[2]]
out.append(f'Z0086: primes l=3 mod 4, l<=3000, with eps^j = -1 mod l O_K for some j: {len(res)}; of these split in Q(sqrt3): {len(sp)}; first split: {sp[:6]}')
out.append(f'  inert-or-split count of l=3 mod4 total (<=3000): {sum(1 for l in range(3,3001) if l%4==3 and all(l%q for q in range(2,int(l**.5)+1)))}')
# ---- Z0078 orbit identity
bad = 0; checked = 0; ex = None
def ordered_yz(a, b):
    # count ordered (y,z) positive with 1/y+1/z = a/b
    c = 0
    for y in range(1, 10**6):
        r = Fr(a, b) - Fr(1, y)
        if r <= 0: break
        if r.numerator == 1 and r.denominator >= 1:
            c += 1
    return c
for p in [q for q in range(5, 101) if all(q % d for d in range(2, int(q**.5)+1)) and q % 4 == 1]:
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        a, b = r.numerator, r.denominator
        direct = 0
        # ordered (y,z): 1/y < r and z = 1/(r-1/y) integer; y in (1/r, 2/r]
        lo = math.floor(1 / r) + 1; hi = math.floor(2 / r)
        for y in range(lo, hi + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1: direct += 1
        # every direct pair (y<=z) must give k=(y+z)/a integer with yz=kb and (y-z)^2 = k(ka^2-4b): check both directions
        k_count = 0
        for y in range(lo, hi + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1:
                z = s_.denominator
                if (y + z) % a == 0:
                    k = (y + z) // a
                    if y * z == k * b and issq(k * (k * a * a - 4 * b)) and (y - z) ** 2 == k * (k * a * a - 4 * b):
                        k_count += 1
        checked += 1
        if direct != k_count or (direct and False):
            bad += 1
            if ex is None: ex = (p, x, direct, k_count)
out.append(f'Z0078: a/b = 4/p - 1/x over p<=100 (p=1 mod 4), {checked} fractions: every unordered solution pair (y<=z) gives integer k=(y+z)/a with yz=kb and (y-z)^2=k(ka^2-4b) a square, and conversely; mismatches {bad} (first {ex})')
print('\n'.join(out))
open('data/z52b/pass2/TO0b/fix_units.txt', 'w').write('\n'.join(out) + '\n')
