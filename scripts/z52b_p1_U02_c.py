"""Z0694 follow-up: a_p(E) for E: y^2=x^3-x (conductor 32) over primes; test a_p/2 mod 4 vs (2/p) for p = 1 mod 4."""
import json
from sympy import primerange
def ap(p, a4):
    s = 0
    for x in range(p):
        r = (x**3 + a4*x) % p
        if r: s += 1 if pow(r, (p-1)//2, p) == 1 else -1
    return -s
rows = []
for p in primerange(5, 1200):
    if p % 4 != 1: continue
    a = ap(p, -1)
    leg2 = 1 if p % 8 in (1, 7) else -1
    rows.append((p, a, (a // 2) % 4, leg2))
ok = sum(1 for r in rows if (r[2] == 1 and r[3] == 1) or (r[2] == 3 and r[3] == -1))
zero3 = all(ap(p, -1) == 0 for p in primerange(3, 1200) if p % 4 == 3)
print('p=1 mod 4 tested', len(rows), 'a_p/2 mod 4 == (2/p) (as +-1 -> 1,3):', ok, 'of', len(rows), '| a_p=0 for all p=3 mod 4:', zero3)
json.dump({'n': len(rows), 'agree': ok, 'a0_p3mod4': zero3, 'examples': rows[:10]}, open('data/z52b/pass1/U02/Z0694_ap.json', 'w'))
