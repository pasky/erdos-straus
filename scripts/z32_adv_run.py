"""O262 adversarial designs at sizes X = 1e18, 1e21, 1e25 (primes BPSW-probable via flint; EVIDENCE-grade).
Designs: C0 random p ≡ 1 (24); D1 class of one p ≡ 1 (mod M_y), M_y = 24*prod_{5<=l<=y} l, largest y with
M_y <= X/1e4; D2 = D1 + (l/p) = +1 for all primes y < l <= 97; D3 = Prop 3.1 shadow on the six e-slices e = 3, 7, 11
(Types I, II): p ≡ 1 (mod M_23) and (p+e)/(1+e), (pe+1)/(e+1) prime; D4 = the 4 lowest S(127) among 300 D1 primes.
Per prime: S(E) = all Type I + II e-slice solutions with e <= E (E = 2047), W = least e, verified solution.
Output: one JSON line per prime to logs/z32_adv.jsonl.   Usage: z32_adv_run.py X [designs]"""
import sys, json, random, math, time, os
from decimal import Decimal
import numpy as np
from flint import fmpz
sys.path.insert(0, 'scripts'); from z32_adv import slices
X = int(Decimal(sys.argv[1])); designs = sys.argv[2].split(',') if len(sys.argv) > 2 else ['C0', 'D1', 'D2', 'D3', 'D4']
E = 2047; random.seed(262 + int(math.log10(X)))
isp = lambda n: fmpz(n).is_prime()
small = [l for l in range(5, 3000) if all(l % d for d in range(2, int(l**.5) + 1))]
def M(y): return 24*math.prod(l for l in small if l <= y)
ymax = max(l for l in small if M(l) <= X//10**4); My = M(ymax)
def legendre(a, l): return pow(a % l, (l - 1)//2, l)
def rec(design, p, extra=None):
    t = time.time(); r = slices(p, E)
    d = {'design': design, 'X': X, 'p': p, 'S': r['S'], 'S2': sum(r['X2'].values()), 'S1': sum(r['X1'].values()),
         'S127': sum(v for e, v in r['X2'].items() if e <= 127) + sum(v for e, v in r['X1'].items() if e <= 127),
         'W': r['W'], 'sol': [r['sol'][0], r['sol'][1]] + [str(v) for v in r['sol'][2]], 'secs': round(time.time() - t, 1)}
    if extra: d.update(extra)
    print(json.dumps(d), flush=True)
def class_of_one(n, Q, start, cond=lambda p: True, limit=10**7):
    out = []; t = start//Q + 1; tries = 0
    while len(out) < n and tries < limit:
        p = 1 + Q*t; t += 1; tries += 1
        if cond(p) and isp(p): out.append(p)
    return out
if 'C0' in designs:
    for _ in range(8):
        while True:
            p = 24*random.randrange(X//24, 2*X//24) + 1
            if isp(p): break
        rec('C0', p)
if 'D1' in designs:
    for p in class_of_one(8, My, X): rec('D1', p, {'y': ymax})
if 'D2' in designs:
    ls = [l for l in small if ymax < l <= 97]
    for p in class_of_one(4, My, X, lambda p: all(legendre(p, l) == 1 for l in ls), limit=10**8):
        rec('D2', p, {'y': ymax, 'QR_to': 97})
if 'D3' in designs:
    Q = M(23); es = (3, 7, 11)
    forms = [(1, 0, 1)] + [(1, e, 1 + e) for e in es] + [(e, 1, 1 + e) for e in es]   # (alpha, beta, gamma): (alpha p + beta)/gamma
    sieve = [l for l in small if l > 23 and l < 2000]; found = []; t0 = X//Q + 1; CH = 10**6
    while len(found) < 4:
        ok = np.ones(CH, bool)
        for l in sieve:
            for al, be, ga in forms:   # (al(1+Q t) + be)/ga ≡ 0 (mod l)  <=>  t ≡ -(al+be) (al Q)^-1 (mod l)
                r = (-(al + be)*pow(al*Q, -1, l)) % l; s = (r - t0) % l; ok[s::l] = False
        for i in np.flatnonzero(ok):
            p = 1 + Q*(t0 + int(i))
            if all(isp((al*p + be)//ga) for al, be, ga in forms): found.append(p)
            if len(found) >= 4: break
        t0 += CH
    for p in found: rec('D3', p, {'y': 23, 'shadow_e': list(es)})
if 'D4' in designs:
    POOL = int(os.environ.get('Z32_POOL', '300')); cand = class_of_one(POOL, My, 2*X); sc = []
    for p in cand:
        r = slices(p, 127); sc.append((r['S'], p))
    for s, p in sorted(sc)[:4]: rec('D4' if POOL == 300 else 'D4big', p, {'y': ymax, 'pool': len(cand)})
