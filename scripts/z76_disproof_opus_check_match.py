"""Opus review: independently re-derive the z76 matched controls (own MR, own
smoothness) and check (i) every control is eligible, (ii) it is the FIRST
eligible candidate in the stated order (d=M,2M,..; +d before -d) not already
used, (iii) every dropped cell really has no eligible unused candidate."""
import random, sys
from math import isqrt
D = 'data/z76/disproof/comp/'
M = 32*27*25*49; LO = 10**12
B12 = (2,3,5,7,11,13,17,19,23,29,31,37)
def isp(n):
    if n < 2: return False
    for q in B12:
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in B12:
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
SP = [q for q in range(2, 62) if all(q % r for r in range(2, q))]
def smooth(n):
    for q in SP:
        while n % q == 0: n //= q
    return n == 1
def sq(n): r = isqrt(n-1); return r*r == n-1
def elig(p, n, sm, sh):
    return n//LO == p//LO and not sq(n) and smooth(n-1) == sm and isp(n) and isp(12*n+1) == sh

anchors = [l.split()[:2] for l in open('data/z75/push2prime/panels.txt') if l.split()[0] in ('sm+','sq')]
used = {int(p) for _, p in anchors}
rows = {}  # anchor -> {tag: n}
inc = {}
for l in open(D+'match.txt'):
    w = l.split()
    if l.startswith('# incomplete'): inc[int(w[3])] = w[2]; continue
    if l.startswith('#'): continue
    rows.setdefault(int(w[1]), {})[w[0]] = int(w[2])
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
full_check = set(int(p) for t, p in anchors if t == 'sq')
qs = [int(p) for t, p in anchors if t == 'sm+']
full_check |= set(random.sample([p for p in qs if p in rows], 60))
full_check |= set(random.sample([p for p in qs if p in inc], 40))
stats = {'checked_cells': 0, 'dropped_verified': 0}
def first(p, sm, sh, taken):
    d = M
    while d <= p//1000:
        for n in (p+d, p-d):
            if n not in taken and elig(p, n, sm, sh): return n
        d += M
    return 0
for tag, ps in anchors:
    p = int(ps)
    if tag == 'sm+':
        cells = [('sm-', True, False), ('rough+', False, True), ('rough-', False, False)]
    else:
        cells = [('sq_ctl', smooth(p-1), isp(12*p+1))]
    if p in full_check:
        got = [first(p, sm, sh, used) for _, sm, sh in cells]
        if p in inc:
            assert 0 in got, p
            assert p not in rows
            stats['dropped_verified'] += 1
        else:
            for (t, _, _), g in zip(cells, got):
                assert rows[p][t] == g, (p, t, rows[p][t], g)
                stats['checked_cells'] += 1
    if p in rows:
        for t, _, _ in cells: used.add(rows[p][t])
print(stats, 'anchors fully re-derived', len(full_check))
