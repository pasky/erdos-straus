"""Independent subset/group checks and the finite-budget Cayley-distance toy."""
import json
from collections import Counter, deque
from pathlib import Path
from math import gcd
from flint import fmpz
P=Path('data/z45_prime_t1_dual')

def divisors(n):
    ds=[1]
    for p,e in fmpz(n).factor():
        ds=[d*int(p)**j for d in ds for j in range(int(e)+1)]
    return ds

def distance(row):
    m=row['modulus']; target=row['target']
    primes=row['primes']
    ds=[d for d in divisors(row['N']) if gcd(d,m)==1]
    dist={d % m:0 for d in ds}
    queue=deque(dist)
    while queue:
        r=queue.popleft()
        if r==target: return dist[r]
        for p in primes:
            v=r*p % m
            if v not in dist:
                dist[v]=dist[r]+1
                queue.append(v)
    return None

records=[]
for name in ['full8_11','full8_17','full8_131','full8_241','star_409','full15_8']:
    rows=json.loads((P/f'{name}.json').read_text())
    values=[]
    for row in rows:
        d=distance(row)
        assert (d is None)==(row['kind'] in ('quadratic','higher'))
        assert d is None or d>0
        # Check minimal quotient modulus using direct integer divisors, independently
        # of the scan's stripped-factor list.
        ds=[x for x in divisors(row['N']) if gcd(x,row['modulus'])==1]
        f=next(f for f in sorted(divisors(row['modulus']))
               if all(x % f != row['target'] % f for x in ds))
        assert f==row['budget_modulus']
        values.append(dict(coordinate=row.get('x',row.get('u')),distance=d))
    rec=dict(case=name,histogram=dict(Counter(str(v['distance']) for v in values)),rows=values)
    records.append(rec)
    print(name,rec['histogram'])
# Quartic example: 2791 is 9 mod 13, generating H={1,3,9}; 12 not in H.
assert {pow(2791,j,13) for j in range(12)}=={1,3,9}
assert {pow(2,j,13) for j in range(12)}==set(range(1,13))
# Complete raw divisors check for the hand-worked budget examples.
assert {d % 16 for d in divisors(413)}=={1,7,11,13}
assert 7*59**2 % 16==15
assert {d % 5 for d in divisors(2227**2)}=={1,2,4}
assert pow(17,3,5)==3
(P/'toy.json').write_text(json.dumps(records,indent=2)+'\n')
from z45_prime_t1_dual_scan import star, summary
extra=[]
for n in [113,137,233,241,281,433,449,3361,5101441]:
    row=dict(n=n,**summary(star(n)))
    extra.append(row)
    print('extra-star',n,row['counts'])
(P/'extra.json').write_text(json.dumps(extra,indent=2)+'\n')
