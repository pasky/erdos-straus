"""Fix round TO3 (Z0839, Z0876, Z0757): the (star)-slot image of ES solutions.
For a word (t,u,v) with t = 4C and tuv-u-v = p, the explicit solution (x,y,z) = (C u v, p C v, p C u) solves 4/p (checked).
A solution of 4/p lies in this image iff two of its denominators a,b satisfy p | a, p | b and, with C = gcd(a,b)/p,
c = a*b/(p^2 C) (the third denominator). We measure this fraction for every prime p <= PMAX, split by ET type
(Type I: p divides exactly one denominator; Type II: two). Other slots (4 | u, 4 | tu-1, 4 | tv-1 ...) are NOT mapped here.
Writes data/z52b/pass2/TO3/fiveslot_results.json"""
import json, sys
from math import gcd
from sympy import primerange
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
def in_star_image(p, s):
    x, y, z = s
    for a, b, c in ((y, z, x), (x, z, y), (x, y, z)):
        if a % p or b % p: continue
        g = gcd(a, b)
        if g % p: continue
        g //= p                      # g = C * gcd(u,v) ; allow any divisor e of g as C
        for C in [e for e in range(1, g + 1) if g % e == 0]:
            if (a * b) % (p * p * C): continue
            if a * b // (p * p * C) == c and a % (p * C) == 0 and b % (p * C) == 0: return True
    return False
def etype(p, s):
    k = sum(1 for v in s if v % p == 0)
    return k
out = {'PMAX': PMAX}
agg = {}
for p in primerange(3, PMAX + 1):
    S = sols(4, p)
    if not S: continue
    key = 'p1mod4' if p % 4 == 1 else 'p3mod4'
    d = agg.setdefault(key, dict(n_sol=0, in_image=0, typeI=0, typeI_in=0, typeII=0, typeII_in=0, primes=0))
    d['primes'] += 1
    for s in S:
        k = etype(p, s); im = in_star_image(p, s)
        d['n_sol'] += 1; d['in_image'] += im
        if k == 1:
            d['typeI'] += 1; d['typeI_in'] += im
        elif k >= 2:
            d['typeII'] += 1; d['typeII_in'] += im
out['by_class'] = agg
for k, d in agg.items():
    d['frac_in_image'] = round(d['in_image'] / d['n_sol'], 4)
    d['frac_typeII_in_image'] = round(d['typeII_in'] / max(1, d['typeII']), 4)
    d['frac_typeI_in_image'] = round(d['typeI_in'] / max(1, d['typeI']), 4)
# examples 2521 and 4/105 and 4/12601
for p in (2521, 105, 12601):
    S = sols(4, p)
    out[f'example_{p}'] = [dict(sol=list(s), in_star_image=in_star_image(p, s), n_div_by_p=etype(p, s)) for s in S]
json.dump(out, open('data/z52b/pass2/TO3/fiveslot_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1)[:3000])
