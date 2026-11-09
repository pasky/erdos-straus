#!/usr/bin/env python3
"""Independent delta checks. One process, small bounded lists (no Cartesian arrays).
Run after C census/direct mode and extracting branch to ROOT:
  ulimit -v 6000000; timeout 1800 uv run --with sympy python THIS ROOT
"""
import ast
from collections import Counter
from math import isqrt
from pathlib import Path
import re
import sys
from sympy import divisors, factorint, isprime, primerange

root = Path(sys.argv[1])
data = root / 'data/z68/u7f'
cs = (1, 3, 5, 7, 9, 25)
ws = {}
for line in (root / 'independent_witnesses.txt').read_text().splitlines():
    fields = line.split()
    if fields[0] == 'N':
        n = int(fields[1]); ws[n] = []
    else:
        ws[n].append(tuple(map(int, fields[1:])))

def numbers(name):
    return list(map(int, (data / name).read_text().split()))

np = numbers('noprime_primes_1e9.txt')
u8 = numbers('u8zero_primes_1e8.txt')
ind_np = [int(line.split()[1]) for line in
          (root / 'independent_census.txt').read_text().splitlines()
          if line.startswith('NOPRIME')]
assert np == ind_np
# Compare *every* listed f,r,y,z, not merely summaries.
for name in ('movingr_noprime_1e9.txt', 'movingr_u8zero.txt'):
    for line in (data / name).read_text().splitlines():
        if not line.startswith('p='):
            continue
        n = int(line.split(':')[0][2:])
        expected = [(int(f), int(r), int(y), int(z)) for f, r, y, z in
                    re.findall(r'f=(\d+) c=\d+ om=\d+ r=(\d+) y=(\d+) z=(\d+)', line)]
        assert ws[n] == expected, (name, n)

kappa = Counter(); shifts = Counter(); shifts_minr = Counter(); all_minr = Counter()
k3 = Counter(); exceptions = []
for n in set(np + u8 + [196065]):
    ranked = []; best_family = 10**20
    for f, r, y, z in ws[n]:
        factors = factorint(f); P = max(factors); c = f // P**factors[P]
        assert f % 8 == 7 and r == (-n) % f and r*y == f+1 and f*z-r == n
        ranked.append((c, f, r))
        fam = [c0 for c0 in cs if f % c0 == 0 and isprime(f // c0)]
        best_family = min([best_family] + fam)
        if n in u8:
            assert r % 8 and y % 8 and z % 8
    c, f, r = min(ranked)
    if n in np:
        kappa[c] += 1; shifts[r] += 1
        shifts_minr[min(r0 for c0, f0, r0 in ranked if c0 == c)] += 1
        all_minr[min(r0 for c0, f0, r0 in ranked)] += 1
        assert c == best_family
        if c > 3: exceptions.append(n)
    if n in u8:
        k3[best_family] += 1
        assert not any(d % 8 == 7 for d in divisors(n+1)), 'missed y=1'
assert ws[196065] == [(13079, 120, 109, 15)]
assert all(not ws[n] for n in [105,1465,3865,4545,10305,12145,39361,67425])
print('All 231 + 38 canonical witness lists match; K2/K3 and y=1 checks pass.')
print('kappa on 231:', sorted(kappa.items()))
print('least-(c,f) shift counts:', shifts.most_common(8))
print('least-(c,r) shift counts:', shifts_minr.most_common(8))
print('least r over all witnesses:', all_minr.most_common(8))
print('K3 minimum family:', sorted(k3.items()))
print('no F1/F3:', sorted(exceptions))

# Independently regenerate the hard-prime list from exact divisor conditions.
def has_outer(n, x):
    return any((x+z) % 8 == 7 and (n+x+z) % (x*z) == 0
               for z in divisors(n+x))
def has_middle(n, y):
    return any(d % 8 == 7 and d % y == y-1 and
               ((n*y+1)//d) % y == y-1 for d in divisors(n*y+1))
hard = []
for n in primerange(17, 10**6+1):
    if n % 8 != 1:
        continue
    if any(has_outer(n, x) for x in (1,2,4,8)):
        continue
    if n % 3 == 1 and has_outer(n, 3):
        continue
    if any(has_middle(n, y) for y in (2,4,8)):
        continue
    hard.append(n)
lane_source = (root / 'scripts/z68_u7f_relsearch.py').read_text()
lane_hard = next(ast.literal_eval(node.value) for node in ast.parse(lane_source).body
                 if isinstance(node, ast.Assign) and
                 any(isinstance(t, ast.Name) and t.id == 'allfail' for t in node.targets))
assert hard == lane_hard and len(hard) == 43

def words(n):
    # Unordered outer-letter enumeration, including y=1. For y>=1,
    # (x-1)^2 <= n+1; z divides n+x and y=(n+x+z)/(xz).
    out = set()
    for x in range(1, isqrt(n+1)+2):
        for z in divisors(n+x):
            if z < x or (x+z) % 8 != 7 or (n+x+z) % (x*z):
                continue
            y = (n+x+z)//(x*z)
            for r, t in ((x,z),(z,x)):
                if r*y % 8:
                    continue
                f = r*y-1
                if y == 1:
                    out.add((f,1,f+1,(n+1)//f))
                else:
                    out.add((f,r,y,t))
    return out

def reps(n, k):
    out = []
    for v in range(1, isqrt((n-1)//k)+1):
        u = isqrt(n-k*v*v)
        if u > 0 and u*u+k*v*v == n:
            out.append((u,v))
    return out

exact = Counter(); floored = Counter(); false_hits = set(); inflated = set()
for n in hard:
    W = words(n)
    brute = {(f, (-n)%f, (f+1)//((-n)%f), (n+(-n)%f)//f)
             for f in range(7,2*n+2,8) if (-n)%f and (f+1)%((-n)%f) == 0}
    assert W == brute
    letters = {kind: {w[j] for w in W} for j, kind in enumerate(('f','r','y','z'))}
    letters['f+1'] = {w[0]+1 for w in W}
    found = set(); floorfound = set()
    for tag, a, k in [('A',n+1,1),('B',n+2,2),('C',n+4,1),('D',4*n+1,1),('E',2*n+1,2)]:
        for u, v in reps(a,k):
            cand = {f'{al}u{be:+d}v': (abs(al*u+be*v),1)
                    for al in range(-3,4) for be in range(-3,4)}
            cand.update({'uv':(u*v,1),'2uv':(2*u*v,1),'u+v/2':(u+v,2),
                         'u-v/2':(abs(u-v),2),'u2-v2':(abs(u*u-v*v),1),
                         '(u2-v2)/2':(abs(u*u-v*v),2)})
            for name, (num, den) in cand.items():
                for kind, values in letters.items():
                    key = (tag,name,kind)
                    if num//den in values:
                        floorfound.add(key)
                        if num % den == 0:
                            found.add(key)
                        else:
                            false_hits.add((n,key))
    exact.update(found);floored.update(floorfound)
    inflated.update((n, key) for key in floorfound - found)
print('Independent hard primes:', len(hard))
print('Exact rational-formula maximum:', max(exact.values()),
      sorted((key,val) for key,val in exact.items() if val == max(exact.values())))
print('Lane floor-formula maximum:', max(floored.values()),
      sorted((key,val) for key,val in floored.items() if val == max(floored.values())))
print('Half-integer matches:', len(false_hits), 'inflated prime/formula counts:', len(inflated))
print('Example:', sorted(false_hits)[:3])
assert max(exact.values()) == max(floored.values()) == 6
print('PASS')
