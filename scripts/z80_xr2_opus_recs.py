"""Opus round-2 independent check of data/z80/gap/checks.csv (EXTREME §7).
For every row: p prime (PARI isprime, proven), x=(p+g)/4, the printed triple solves
4/p=1/x+1/y+1/z with x<=y<=z, window g succeeds and every window m<g fails.
Window criterion here: divisor *pairs* u,v | s=p*x with u+v=0 mod m, from the residue
set of divisors of s (computed from the factorisation exponents, not divisors(x^2)).
Also the U7 word certificate and the 26 R8 control list. PARI used only to factor/prove primality.
"""
import csv, sys
from cypari2 import Pari
P = Pari(); P.allocatemem(256_000_000, silent=True); P.default('factor_proven', 1)
MCL = {1, 121, 169, 289, 361, 529}

def fac(n):
    f = P.factor(n); return [(int(f[0][i]), int(f[1][i])) for i in range(len(f[0]))]

def residues(fl, m):
    S = {1 % m}
    for q, e in fl:
        q %= m; new = set(S); t = 1
        for _ in range(e):
            t = t * q % m; new |= {r * t % m for r in S}
        S = new
    return S

def window(p, m):
    x = (p + m) // 4; assert (p + m) % 4 == 0
    fl = fac(x) + [(p, 1)]
    assert all(q % m for q, _ in fl)
    S = residues(fl, m)
    return any((-r) % m in S for r in S)

def explicit(p, m):
    """construct a triple at window m by an explicit coprime divisor pair"""
    x = (p + m) // 4; s = p * x
    divs = [int(d) for d in P.divisors(x)]; divs += [d * p for d in divs]
    byres = {}
    for d in divs: byres.setdefault(d % m, []).append(d)
    for u in divs:
        for v in byres.get((-u) % m, []):
            from math import gcd
            gg = gcd(u, v); a, b = u // gg, v // gg
            if s % (a * b): continue
            y = (s // a) * (a + b) // m; z = (s // b) * (a + b) // m
            if (s // a) * (a + b) % m or (s // b) * (a + b) % m: continue
            assert 4 * x * y * z == p * (x * y + x * z + y * z)
            return tuple(sorted((x, y, z)))
    return None

rows = list(csv.DictReader(open('data/z80/gap/checks.csv')))
bad = 0; tags = {}; nonM = []
for r in rows:
    p, g, x, y, z = (int(r[k]) for k in ('p', 'g', 'x', 'y', 'z'))
    ok = bool(P.isprime(p)) and p % 4 == 1 and 4 * x == p + g and x <= y <= z \
        and 4 * x * y * z == p * (x * y + x * z + y * z)
    ok = ok and window(p, g) and not any(window(p, m) for m in range(3, g, 4))
    ok = ok and explicit(p, g) is not None
    f, u = int(r['U7_f']), int(r['U7_u'])
    t, rr = divmod(f + 1, u); v, r2 = divmod(p + u, f)
    ok = ok and f % 8 == 7 and rr == 0 and r2 == 0 and t * u * v - u - v == p and (t * u) % 8 == 0 and int(r['e_star']) == 0
    if r['tag'] == 'record': ok = ok and p % 840 in MCL
    if r['tag'] == 'R8' and p % 840 not in MCL: nonM.append(p)
    tags.setdefault(r['tag'], []).append(g)
    if not ok: bad += 1; print('BAD', r, flush=True)
for t, gs in tags.items(): print(t, len(gs), 'max g', max(gs))
r8 = [int(r['p']) for r in rows if r['tag'] == 'R8']
print('R8 controls outside the six 840-classes:', len(nonM))
print('R8 distinct', len(set(r8)), 'of', len(r8))
# selection check: L40e* rows are exactly the first 16 primes 1 mod lcm(1..40) above 10^e
from math import lcm
q = lcm(*range(1, 41))
for e in (18, 24, 30, 36):
    want = []; t = (10**e - 1 + q - 1) // q
    while len(want) < 16:
        p = 1 + t * q; t += 1
        if P.isprime(p): want.append(p)
    got = [int(r['p']) for r in rows if r['tag'] == 'L40e%d' % e]
    print('L40e%d selection' % e, 'ok' if got == want else 'MISMATCH', 'first', want[0])
# L rows: the prime entries of panel.csv family L
Lp = [int(r['n']) for r in csv.DictReader(open('data/z80/extreme/panel.csv')) if r['family'] == 'L' and r['prime'] == '1']
print('L rows match panel prime entries', Lp == [int(r['p']) for r in rows if r['tag'] == 'L'])
print('rows', len(rows), 'bad', bad)
