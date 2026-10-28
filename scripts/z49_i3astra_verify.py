"""Exact, bounded checks of the new I3 identities; run with uv run python.
No analytic asymptotic is certified by this script. Uses only the standard library.
"""
from fractions import Fraction
from math import isqrt, lcm
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/z49_i3astra'
rows = (OUT / 'census.txt').read_text().splitlines()
N = int(rows[0].split()[1])
zeros = [int(r.split()[1]) for r in rows if r.startswith('ZERO ')]
reference = [int(r.split()[1]) for r in
             (ROOT / 'data/z48_ltfable/big_1e9.txt').read_text().splitlines()
             if r.startswith('I30 ') and int(r.split()[1]) <= N]
assert zeros == reference

# Independent direct triple enumeration, not factorization of n+u.
limit = 3000
counts = [0] * (limit + 1)
words = [[] for _ in range(limit + 1)]
for u in range(3, (limit + 3) // 8 + 1):
    for v in range(3, (limit + u) // (3*u - 1) + 1):
        for t in range(3, (limit + u + v) // (u*v) + 1):
            n = t*u*v-u-v
            assert (t*u-1)*(t*v-1) == t*n+1
            assert 7*t*u*v <= 9*n
            counts[n] += 1
            words[n].append((t,u,v))
for r in rows:
    if r.startswith('SMALL '):
        _, n, c = r.split()
        assert counts[int(n)] == int(c)

# Exact three-wedge interval inequality and disjointness, before asymptotics.
interval_checks = 0
for h in range(3, 41):
    pairs = [(a,b) for a in range(3,h+1) for b in range(3,h//a+1)]
    s0 = sum((Fraction(1,a*b) for a,b in pairs), Fraction())
    s1 = sum((Fraction(1,a*b-1) for a,b in pairs), Fraction())
    bound = h*(s0+2*s1)-3*len(pairs)
    for n in (h*h, h*h+1, h*h+17, 2500):
        total = sum(counts[n+1:n+h+1])
        selected = 0
        for m in range(n+1,n+h+1):
            for t,u,v in words[m]:
                k = (t*u <= h)+(t*v <= h)+(u*v <= h)
                assert k <= 1
                selected += k
        assert total >= selected >= bound
        interval_checks += 1

# Prime-modulus classes: rho(q)=tau(q+1)-4 and explicit interior witnesses.
prime_classes = 0
for q in range(7,2000):
    if any(q%d == 0 for d in range(2,isqrt(q)+1)):
        continue
    divs = [d for d in range(1,q+2) if (q+1)%d == 0]
    ds = [d for d in divs if 3 <= d <= (q+1)//3]
    assert len(ds) == len(divs)-4
    assert len({(-d)%q for d in ds}) == len(ds)
    for u in ds:
        n = 4*q-u
        t,v = (q+1)//u, 4
        assert min(t,u,v) >= 3 and t*u*v-u-v == n
        prime_classes += 1

# Exact all-integer CRT laws, including diagonals; H<=7 keeps period <=176400.
crt = []
for h in range(3,8):
    L = lcm(*range(1,h+1)); period=L*L
    hits = bytearray(period)
    mean = Fraction()
    for u in range(3,h+1):
        for v in range(u,h+1):
            mean += Fraction(1,u*v)
            for r in range((-u-v)%(u*v),period,u*v):
                hits[r] = 1
    assert not hits[0] and not hits[1]
    avoided = hits.count(0)
    crt.append({'H':h, 'period':period, 'avoiders':avoided,
                'density':str(Fraction(avoided,period)), 'unordered_mean':str(mean)})

# Balanced cube coverage bound, counting ordered words is an upper bound on images.
boxes = []
for B in (5,10,20,40):
    image = {t*u*v-u-v for t in range(B,2*B)
             for u in range(B,2*B) for v in range(B,2*B)}
    covered = sum(2*B**3 <= n < 4*B**3 for n in image)
    assert covered <= B*B*(B+1)//2
    boxes.append({'B':B,'central_integers':2*B**3,'covered':covered})

report = {'census_bound':N,'census_zeros':len(zeros),'last_subrange_zero':zeros[-1],
          'reference_matches':True,'direct_count_checks':498,
          'interval_checks':interval_checks,'prime_class_witnesses':prime_classes,
          'crt':crt,'balanced_boxes':boxes,
          'controls':[r for r in rows if r.startswith('CONTROL ')]}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
