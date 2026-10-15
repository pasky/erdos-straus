# R225 from-scratch family search for n = m^2 + k (independent of ns_polyfam.py).
# Enumerates every Type I / Type II degree shape (after a<=b normalisation, ET Lemma 2.8) with
# rational roots p/q (q<=QMAX, |p/q|<=RMAX) and leading coefficients from a grid; keeps algebraic families
# (all six coordinates in Q[m], positive leading coefficients) and reports those whose witness
# (d for Type I, f for Type II) is ESCAPING (D mod m^2+k has nonzero m-coefficient).
import sys, itertools
from fractions import Fraction as F
k = int(sys.argv[1]); RMAX = int(sys.argv[2]); QMAX = int(sys.argv[3])
DUMP = sys.argv[4] if len(sys.argv) > 4 else None; allfam = []
def trim(p):
    while p and p[-1] == 0: p.pop()
    return p
def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return trim(r)
def mul(p, q):
    if not p or not q: return []
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i + j] += x * y
    return trim(r)
def sc(c, p): return trim([c * x for x in p])
def divmod_(g, f):  # exact division in Q[m]; returns (quot, rem)
    g = list(g); qd = [F(0)] * max(len(g) - len(f) + 1, 1)
    while len(g) >= len(f) and g:
        c = g[-1] / f[-1]; sh = len(g) - len(f); qd[sh] = c
        for i, x in enumerate(f): g[i + sh] -= c * x
        trim(g)
    return trim(qd), g
def pos(p): return bool(p) and p[-1] > 0
N = [F(k), F(0), F(1)]
roots = sorted({F(p, q) for q in range(1, QMAX + 1) for p in range(-RMAX * q, RMAX * q + 1)})
lead = sorted({F(p, q) for p in (1, 2, 3, 4, 6, 8, 12) for q in (1, 2, 3, 4)})
consts = [F(c) for c in range(1, 13)] + [F(1, 2), F(3, 2), F(1, 3), F(1, 4)]
def lin(l, r): return [-l * r, l]
def quad(l, u, v): return [l * v, l * u, l]
def gen(deg):
    if deg == 0:
        for c in consts: yield [c]
    elif deg == 1:
        for l in lead:
            for r in roots: yield lin(l, r)
    else:
        for l in lead:
            for r1 in roots:
                for r2 in roots:
                    if r2 >= r1: yield mul([-r1, F(1)], [-r2, l])   # split quadratics only
            # irreducible over Q: m^2 + v with v>0 (+ shifts) 
            for u in roots:
                for v in consts: yield quad(l, 2 * u, u * u + v)
def escaping(D):
    _, rem = divmod_(D, N)
    return len(rem) >= 2 and rem[1] != 0
found = {'I': 0, 'II': 0}; esc = {'I': 0, 'II': 0}; ex = []
# Type I : (deg a, deg c, deg d) with deg d >= 1
for da, dc, dd in [(0, 0, 2), (1, 0, 1), (0, 1, 1)]:
    for a in gen(da):
        for c in gen(dc):
            if da + dc >= 1 and len(a) + len(c) > 3: pass
            ac = mul(a, c)
            for d in gen(dd):
                f = add(sc(4, mul(ac, d)), sc(-1, N))
                if not pos(f): continue
                b, r1 = divmod_(add(mul(N, a), c), f)
                if r1 or not pos(b): continue
                e, r2 = divmod_(add(sc(4, mul(mul(a, a), d)), [F(1)]), f)
                if r2 or not pos(e): continue
                if add(mul(c, e), sc(-1, add(a, b))): continue
                found['I'] += 1; allfam.append(('I', a, b, c, d, e, f))
                if escaping(d): esc['I'] += 1; ex.append(('I', a, b, c, d, e, f))
# Type II : (deg a, deg c, deg d, deg e) sum 2, chart f = 4acd-1, e = (n+4a^2 d)/f, b = ce - a
for da, dc, dd in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
    for a in gen(da):
        for c in gen(dc):
            ac = mul(a, c)
            for d in gen(dd):
                f = add(sc(4, mul(ac, d)), [F(-1)])
                if not pos(f): continue
                e, r1 = divmod_(add(N, sc(4, mul(mul(a, a), d))), f)
                if r1 or not pos(e) or len(e) - 1 != 2 - da - dc - dd: continue
                b = add(mul(c, e), sc(-1, a))
                if not pos(b): continue
                if add(sc(4, mul(mul(a, b), d)), sc(-1, add(N, e))): continue
                found['II'] += 1; allfam.append(('II', a, b, c, d, e, f))
                if escaping(f): esc['II'] += 1; ex.append(('II', a, b, c, d, e, f))
print('k', k, 'RMAX', RMAX, 'QMAX', QMAX, 'families', found, 'escaping', esc)
for t in ex[:5]: print('  example', t[0], [[str(x) for x in p] for p in t[1:]])
if DUMP:
    with open(DUMP, 'w') as fh:
        for t in allfam: fh.write(t[0] + ' ' + ' '.join(','.join(str(x) for x in p) for p in t[1:]) + '\n')
