"""U04 pass-1 batch of precise tests (Z0562, Z0612, Z0991, Z1369, Z1484, Z0993). Memory-bounded, small loops."""
import json, math
from math import gcd
from fractions import Fraction as F
from sympy import primerange, factorint, isprime
def divs_of(n):
    fac = factorint(n); ds = [1]
    for q, e in fac.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def egypt3(num, den):
    """all (y<=z) with num/den = 1/y+1/z (two-term), y>=1."""
    out = []
    if num <= 0: return out
    # (num*y - den) | den^2 ; y > den/num
    g = gcd(num, den); a, b = num // g, den // g
    for d in divs_of(b * b):
        if (d + b) % a: continue
        y = (d + b) // a
        dd = b * b // d
        if (dd + b) % a: continue
        z = (dd + b) // a
        if y <= z: out.append((y, z))
    return out
def U_all(n, m=4):
    """unordered triples x<=y<=z with m/n = sum 1/x"""
    res = []
    for x in range(-(-n // m), (3 * n) // m + 1):
        a, b = m * x - n, n * x
        if a <= 0: continue
        for y, z in egypt3(a, b):
            if x <= y: res.append((x, y, z))
    return res
out = {}
# --- Z0562: Pell candidate test. minimal solution of x^2 - p y^2 = -1, candidates for a denominator of 4/p
def pell_minus1(p, maxterms=10000):
    # continued fraction of sqrt(p): look for convergent with p*y^2 - x^2 = -(-1)... standard: x^2 - p y^2 = (-1)^k Q_k
    a0 = math.isqrt(p); m, d, a = 0, 1, a0
    h0, h1 = 1, a0; k0, k1 = 0, 1
    Q = [0, 1]
    m_, d_, a_ = 0, 1, a0
    h_prev, h = 1, a0; k_prev, k = 0, 1
    for _ in range(maxterms):
        if h * h - p * k * k == -1: return h, k
        m_ = d_ * a_ - m_; d_ = (p - m_ * m_) // d_; a_ = (a0 + m_) // d_
        h_prev, h = h, a_ * h + h_prev; k_prev, k = k, a_ * k + k_prev
    return None
rows = []
hit_pell = 0; hit_base = 0; tot = 0; examples = []
for p in primerange(5, 1500):
    if p % 4 != 1: continue
    tot += 1
    pl = pell_minus1(p)
    if pl is None: continue
    x, y = pl
    cands = set()
    for c in (x - 1, x + 1, y, 2 * y, 4 * y, (x - 1) // 2, (x + 1) // 2, (x - 1) // 4, (x + 1) // 4):
        if c > 0: cands.add(c)
    sols = U_all(p)
    # does some solution have a denominator in cands (Pell-derived set)?
    ok = any(c in cands for s in sols for c in s)
    hit_pell += ok
    # baseline: random-like control set of same size, shifted: {c+1}
    base = any((c + 1) in cands for s in sols for c in s)
    hit_base += base
    if len(examples) < 4 and ok: examples.append((p, (x, y), sorted(cands)[:6]))
out['Z0562'] = dict(n_primes=tot, pell_defined_hits=hit_pell, control_shift_hits=hit_base, examples=examples,
                    note='solutions with a denominator in the Pell-derived candidate set {x±1,y,2y,4y,(x±1)/2,(x±1)/4}; control uses c+1')
# --- Z0612: non-scaled solutions of 4/(pq) = U(pq) - U(p) - U(q); compare with U(p)
rows = []
ps = [p for p in primerange(5, 60) if p % 4 == 1]
qs = [q for q in primerange(3, 200)]
for p in ps:
    up = len(U_all(p))
    vals = []
    for q in qs:
        if q == p: continue
        uq = len(U_all(q)); upq = len(U_all(p * q))
        vals.append(upq - up - uq)
    rows.append((p, up, round(sum(vals) / len(vals), 2), min(vals), max(vals)))
out['Z0612'] = dict(rows=rows[:20], note='nonscaled(pq)=U(pq)-U(p)-U(q), averaged over primes q<200; columns p,U(p),mean,min,max')
# --- Z0991: chart comparison. Markoff-type chart of the cayley memo P2 applied to ES triples (y=(4x,4y,4z,-p)):
# X=2(y0+y1-y2-y3)/e1 etc., e1=sum y_i. Count integral chart points per prime.
integral = 0; total = 0; denoms = {}
for p in primerange(5, 300):
    if p % 4 != 1: continue
    for (x, y, z) in U_all(p):
        Y = [4 * x, 4 * y, 4 * z, -p]
        e1 = sum(Y)
        if e1 == 0: continue
        vals = [F(2 * (Y[0] + Y[1] - Y[2] - Y[3]), e1), F(2 * (Y[0] - Y[1] + Y[2] - Y[3]), e1), F(2 * (Y[0] - Y[1] - Y[2] + Y[3]), e1)]
        total += 1
        if all(v.denominator == 1 for v in vals): integral += 1
        for v in vals: denoms[v.denominator] = denoms.get(v.denominator, 0) + 1
out['Z0991'] = dict(n_solutions=total, n_chart_integral=integral, top_denominators=sorted(denoms.items(), key=lambda kv: -kv[1])[:6])
# --- Z1369: greedy numerator potential. x1=ceil(p/4): numerator a1=4x1-p; remainder a1/(p x1).
greedy = {'a1_hist': {}, 'two_term_ok_after_greedy': 0, 'n': 0}
for p in primerange(5, 2000):
    if p % 4 != 1: continue
    x1 = -(-p // 4); a1 = 4 * x1 - p
    greedy['a1_hist'][a1] = greedy['a1_hist'].get(a1, 0) + 1
    greedy['n'] += 1
    if egypt3(a1, p * x1): greedy['two_term_ok_after_greedy'] += 1
    else: greedy.setdefault('fail_primes', []).append(p)
out['Z1369'] = greedy
# --- Z1484: Kronecker-Hurwitz check: sum_t H(4n-t^2) = 2 sigma(n) - sum_{d|n} min(d,n/d) (verify small n)
def Hcount(D):
    # Hurwitz class number H(D) for D<0 (weighted by 1/2 for forms equivalent to 2x of ...); use reduced forms count
    if D >= 0 or D % 4 not in (0, 1): return 0
    h = 0.0; a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a: continue
            if c == a and b < 0: continue
            w = 1.0
            if a == b == c: w = 1 / 3
            elif a == c and b == 0: w = 1 / 2
            h += w
        a += 1
    return h
kh_ok = []
for n in range(1, 13):
    lhs = sum((-1/12 if 4 * n - t * t == 0 else Hcount(-(4 * n - t * t))) for t in range(-2 * int(math.isqrt(n)) - 1, 2 * int(math.isqrt(n)) + 2) if 4 * n - t * t >= 0 and (4 * n - t * t) % 4 in (0, 3))
    sig = sum(divs_of(n))
    rhs = 2 * sig - sum(min(d, n // d) for d in divs_of(n))
    kh_ok.append((n, round(lhs, 3), rhs))
out['Z1484'] = dict(KH_check_n_lhs_rhs=kh_ok, note='Kronecker-Hurwitz identity checked on n<=12 with lhs computed by reduced-form count')
json.dump(out, open('data/z52b/pass1/U04/scriptA.json', 'w'), indent=1, default=str)
print(json.dumps(out['Z0562'], default=str)[:1500]); print(json.dumps(out['Z1484'], default=str)[:600])
