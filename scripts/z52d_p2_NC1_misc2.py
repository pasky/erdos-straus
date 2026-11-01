# z52d pass2 NC1 follow-ups: (a) greedy a=3 slice success vs p (trend); (b) within-class class-number correlation (Z1686);
# (c) Pell-candidate vs control C (Z1707); (d) three-square premise corrected (Z1833); (e) r4(p) = 8(p+1) check (Z1832).
import math, random, json, statistics
from sympy import factorint, primerange, divisors
from collections import defaultdict
random.seed(1)
def witness(p, C):
    N = 4*C*p+1; m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
def two_term_fact(a, b, fb2):
    # a/b = 1/y+1/z ; (a y - b)(a z - b) = b^2 ; enumerate divisors of b^2 from factorisation dict fb2
    ds = [1]
    for q, e in fb2.items():
        ds = [d*q**k for d in ds for k in range(2*e+1)]
    for d in ds:
        if (d+b) % a == 0:
            dp = b*b//d
            if (dp+b) % a == 0: return True
    return False
out = {}
# (a) greedy slice: x = ceil(p/4), a = 4x-p (=3 for p≡1 mod 4), remainder a/(p x)
trend = {}
for lo, hi in [(10**3, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 10**7)]:
    ps = [p for p in primerange(lo, hi) if p % 24 == 1]
    samp = random.sample(ps, min(400, len(ps)))
    ok = 0
    for p in samp:
        x = -(-p//4); a = 4*x-p; b = p*x
        g = math.gcd(a, b); a2, b2 = a//g, b//g
        f = factorint(b2)
        f2 = {q: 2*e for q, e in f.items()}  # factorisation of b2^2
        ok += two_term_fact(a2, b2, {q: e for q, e in f.items()})
    trend[f'[{lo},{hi})'] = {'primes_sampled': len(samp), 'greedy_slice_success': round(ok/len(samp), 3)}
out['greedy_a3_trend'] = trend
# (b) within-class class-number vs witness correlation, p<1e5, residue class mod 840 demeaned
def h_neg(D):
    h = 0; Dn = -D; a = 1
    while 3*a*a <= Dn:
        for b in range(-a+1, a+1):
            if (b*b + Dn) % (4*a): continue
            c = (b*b + Dn)//(4*a)
            if c < a or math.gcd(math.gcd(a, abs(b)), c) != 1: continue
            if c == a and b < 0: continue
            h += 1
        a += 1
    return h
def R(p):
    tot = 0
    for C in range(1, 51):
        N = 4*C*p+1; m = 4*C; d = m-1
        while d*d <= N:
            if N % d == 0: tot += 1
            d += m
    return tot
rows = []
for p in primerange(5, 100000):
    if p % 4 != 1: continue
    rows.append((p, h_neg(-4*p)/math.sqrt(p), R(p)/math.log(p)**2))
def corr(xs, ys):
    mx, my = statistics.mean(xs), statistics.mean(ys)
    c = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    return c/math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys))
xs = [r[1] for r in rows]; ys = [r[2] for r in rows]
out['corr_raw'] = round(corr(xs, ys), 4)
cls = defaultdict(list)
for r in rows: cls[r[0] % 840].append(r)
dx, dy = [], []
for k, lst in cls.items():
    if len(lst) < 2: continue
    mx = statistics.mean(r[1] for r in lst); my = statistics.mean(r[2] for r in lst)
    for r in lst: dx.append(r[1]-mx); dy.append(r[2]-my)
out['corr_within_mod840_classes'] = {'n': len(dx), 'pearson': round(corr(dx, dy), 4)}
# (c) Pell candidate vs control
pe = {}
P = [p for p in primerange(5, 20000) if p % 4 == 1]
for D in [5, 8, 12, 13]:
    hit = ctrl = tot = 0
    for p in P:
        rep = None
        for y in range(1, 200):
            x2 = p + D*y*y; x = math.isqrt(x2)
            if x*x == x2: rep = (x, y); break
        if rep is None: continue
        tot += 1; x, y = rep
        hit += witness(p, y)
        ctrl += witness(p, y+7)   # control: same kind of C, shifted
    pe[f'D={D}'] = {'reps': tot, 'witness_at_C=y': round(hit/tot, 3), 'control_C=y+7': round(ctrl/tot, 3)}
out['pell_vs_control'] = pe
# (d) three squares premise: odd prime p is a sum of three squares iff p ≢ 7 (mod 8)
def is3(n):
    r = math.isqrt(n)
    for a in range(r+1):
        for b in range(a, r+1):
            c2 = n - a*a - b*b
            if c2 < 0: break
            c = math.isqrt(c2)
            if c*c == c2: return True
    return False
bad = [p for p in primerange(3, 2000) if is3(p) != (p % 8 != 7)]
out['three_squares_premise'] = {'odd_primes_checked': len(list(primerange(3, 2000))), 'violations_of_p_not_7mod8_rule': bad}
# (e) r4(p) = 8(p+1) for odd primes
def r4(n):
    r = math.isqrt(n); c = 0
    for a in range(-r, r+1):
        for b in range(-r, r+1):
            for cc in range(-r, r+1):
                d2 = n - a*a - b*b - cc*cc
                if d2 < 0: continue
                d = math.isqrt(d2)
                if d*d == d2: c += 1 if d == 0 else 2
    return c
out['r4_check'] = {p: (r4(p), 8*(p+1)) for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]}
print(json.dumps(out, indent=1))
