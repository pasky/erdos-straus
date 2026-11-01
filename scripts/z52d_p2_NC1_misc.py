# z52d pass2 NC1 misc checks: purity of residue-determinacy (Z1211/Z1230), greedy-first-term Sylvester test (Z1263),
# exact gcd lemma gcd(4Cp+1,4C'p+1) | 4(C-C') (Z1210/Z1251), h(-4p) vs witness count (Z1686), Pell D tests (Z1707),
# three-square premise (Z1833), four-square count (Z1832).
import math, sys, json
from sympy import factorint, primerange, isprime
from collections import defaultdict
out = {}
def witness(p, C):
    N = 4*C*p+1; m = 4*C
    d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
def cmin(p, cap=50):
    for C in range(1, cap+1):
        if witness(p, C): return C
    return 0
P = [p for p in primerange(5, 200000) if p % 4 == 1]
# --- Z1210/Z1251: exact gcd lemma
bad = 0; cnt = 0
for p in P[:400]:
    for C in range(1, 30):
        for C2 in range(C+1, 30):
            g = math.gcd(4*C*p+1, 4*C2*p+1); cnt += 1
            if 4*(C2-C) % g != 0: bad += 1
out['gcd_lemma'] = {'pairs_checked': cnt, 'violations': bad, 'statement': 'gcd(4Cp+1,4C2p+1) divides 4(C2-C)'}
# --- Z1211/Z1230: residue determinacy of witness status (C<=2 and C_min) over classes mod M
cm = {p: cmin(p, 50) for p in P}
res = {}
for M in [24, 120, 840, 2520]:
    for name, f in [('C<=2', lambda p: cm[p] in (1, 2)), ('C_min==1', lambda p: cm[p] == 1)]:
        cls = defaultdict(lambda: [0, 0])
        for p in P:
            c = cls[p % M]; c[0] += 1; c[1] += int(f(p))
        pure = sum(1 for k, (n, s) in cls.items() if s == 0 or s == n)
        mixed_frac = sum(n for k, (n, s) in cls.items() if 0 < s < n) / len(P)
        res[f'M={M},{name}'] = {'classes': len(cls), 'pure_classes': pure, 'primes_in_mixed_classes_frac': round(mixed_frac, 4)}
out['residue_determinacy'] = res
# --- Z1263: greedy first term x=ceil(p/4), then 2-term test for remainder a/b, a=4x-p, b=p*x
def two_term(a, b):
    # does a/b = 1/y + 1/z have positive solutions? (a y - b)(a z - b) = b^2
    from sympy import divisors
    for d in divisors(b*b):
        if (d + b) % a == 0:
            dp = b*b//d
            if (dp + b) % a == 0:
                return True
    return False
g_ok = 0; g_tot = 0; byclass = defaultdict(lambda: [0, 0])
for p in [q for q in P if q < 60000 and q % 24 == 1][:600]:
    x = -(-p//4); a = 4*x-p; b = p*x
    g = math.gcd(a, b); a2, b2 = a//g, b//g
    ok = two_term(a2, b2)
    g_tot += 1; g_ok += int(ok)
    byclass[p % 840][0] += 1; byclass[p % 840][1] += int(ok)
out['greedy_first_term'] = {'primes': g_tot, 'two_term_completion_ok': g_ok, 'frac': round(g_ok/g_tot, 4)}
# --- Z1686: h(-4p) by reduced-form count vs witness count R(p)= sum_{C<=50} #{d|4Cp+1, d<=sqrt, d≡-1 (4C)}
def h_neg(D):  # D<0 discriminant, count reduced forms (primitive)
    h = 0; Dn = -D
    a = 1
    while 3*a*a <= Dn:
        for b in range(-a+1, a+1):
            if (b*b + Dn) % (4*a): continue
            c = (b*b + Dn)//(4*a)
            if c < a: continue
            if math.gcd(math.gcd(a, abs(b)), c) != 1: continue
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
import statistics
xs, ys = [], []
for p in [q for q in P if q < 100000]:
    h = h_neg(-4*p)
    r = R(p)/math.log(p)**2
    xs.append(h/math.sqrt(p)); ys.append(r)
mx, my = statistics.mean(xs), statistics.mean(ys)
cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); vx = sum((x-mx)**2 for x in xs); vy = sum((y-my)**2 for y in ys)
out['class_number_corr'] = {'primes': len(xs), 'pearson_h_over_sqrtp_vs_R_over_log2p': round(cov/math.sqrt(vx*vy), 4)}
# --- Z1707 (superseded by misc3: unmatched control) : Pell fields D in {5,8,12,13}: p = x^2 - D y^2 representations with small C candidates
tests = {}
for D in [5, 8, 12, 13]:
    hits = 0; tot = 0
    for p in [q for q in P if q < 20000]:
        # find one representation p = x^2 - D y^2 with x>y>=1 (norm of x+y sqrt D)
        found = None
        for y in range(1, 200):
            x2 = p + D*y*y; x = math.isqrt(x2)
            if x*x == x2: found = (x, y); break
        if found is None: continue
        tot += 1
        x, y = found
        # natural candidate certificate parameter: C = y (or y^2) ; test C-form witness existence
        if witness(p, y) or witness(p, y*y) : hits += 1
    tests[f'D={D}'] = {'primes_with_small_rep': tot, 'C=y or y^2 witness': hits}
out['pell_candidates'] = tests
# (Z1833/Z1832 checks moved to z52d_p2_NC1_misc2.py)
print(json.dumps(out, indent=1))
