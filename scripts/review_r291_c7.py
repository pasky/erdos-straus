"""R291: from-scratch check of Thm 4.6 (7*4^s+9): 22 window rules + 11 ET/divisor classes."""
import sys
from math import lcm
from fractions import Fraction as F
from review_r291_poly import *
from review_r291_et import derived_classes, et, is_sol

SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
nf = lambda s: 7 * 4 ** s + 9
OK = True
rules = []  # (applies(s), mod, res, thr)


def window(m, j, typ, d1f, d2f, mod, res):
    """typ: ('CY',h,t) or ('SG',)"""
    global OK
    if typ[0] == 'SG':
        A, B, C = 1, 2, 2
        nY = P(9, 0, 0, 0, 112)
        fp, fm = P(1, 2, 2), P(1, -2, 2)
        x = smul(7, mul(fp, fm))
        pieces = {'f+': fp, 'f-': fm, 'n': nY}
    else:
        _, h, t = typ
        A, B, C = 2, 2 * j, h
        nY = add(smul(7 * 4 ** j, Ypow(h)), P(9))
        x = smul(7 * 4 ** (j - 1), add(Ypow(h), P(t)))
        pieces = {'n': nY, 'Y+t': P(t, 1)}
        if h >= 3:
            pieces['Y2'] = P(1, -1, 1)
        if h == 9:
            pieces['Y6'] = P(1, 0, 0, -1, 0, 0, 1)
    assert add(nY, P(m)) == smul(4, x), (m, j, typ)
    N = mul(nY, x)

    def build(spec):
        p = P(spec[0])
        for name in spec[1:]:
            p = mul(p, pieces[name])
        return p
    d1, d2 = build(d1f), build(d2f)
    s12 = add(d1, d2)
    y = smul(F(1, m), mul(exdiv(N, d2), s12))
    z = smul(F(1, m), mul(exdiv(N, d1), s12))
    r = Rule(f'm={m} j={j} {typ} d1={d1f} d2={d2f}', A, B, C, nY, (x, y, z),
             params=(smul(F(1, m), s12),), nfun=nf)
    Pi, thr, S = r.period_set()
    L = lcm(Pi, mod)
    der = {s for s in range(L) if s % Pi in S}
    cl = {s for s in range(L) if s % mod in res}
    ok = cl <= der
    OK &= ok
    print(f'  {r.name}: Pi={Pi} thr={thr} {"OK" if ok else "CLAIM NOT DERIVED"}'
          f'{"" if cl == der else " (derived larger: " + str(sorted(S)) + ")"}')
    rules.append((r.applies, mod, res, thr))


print('== windows')
W = window
W(19, 1, ('CY', 1, 1), (1,), (1, 'Y+t'), 9, {6})
W(19, 1, ('SG',), (1, 'f-'), (7,), 36, {18, 26})
W(19, 1, ('SG',), (1, 'f+'), (7,), 36, {0, 8})
W(19, 1, ('SG',), (1,), (1, 'f-'), 36, {8, 32})
W(103, 1, ('CY', 1, 4), (1, 'Y+t'), (7,), 51, {44})
W(103, 1, ('CY', 1, 4), (1,), (1, 'n'), 51, {8})
W(103, 1, ('CY', 1, 4), (1,), (1, 'Y+t'), 51, {41})
W(103, 2, ('CY', 1, 1), (1,), (14, 'n'), 51, {17})
W(103, 2, ('CY', 1, 1), (4,), (7, 'n'), 51, {47})
W(103, 2, ('CY', 1, 1), (4,), (7, 'Y+t'), 51, {38})
W(103, 2, ('CY', 1, 1), (2,), (1, 'Y+t'), 51, {32})
W(103, 2, ('CY', 3, 1), (1,), (14, 'n', 'Y2'), 153, {128})
W(103, 2, ('CY', 3, 1), (4, 'Y2'), (7, 'n'), 153, {137})
W(103, 2, ('CY', 3, 1), (2, 'Y2'), (7, 'Y+t'), 153, {32, 74})
W(103, 2, ('CY', 3, 1), (4,), (7, 'Y2'), 153, {29})
W(103, 2, ('CY', 3, 1), (2, 'Y+t'), (7, 'Y2'), 153, {65, 98})
W(103, 2, ('CY', 3, 1), (1, 'n', 'Y+t'), (28,), 153, {56})
W(103, 2, ('CY', 3, 1), (2,), (1, 'n', 'Y2'), 153, {11})
W(103, 2, ('CY', 3, 1), (1, 'Y2'), (1, 'n'), 153, {20})
W(103, 2, ('CY', 9, 1), (1,), (14, 'n', 'Y+t'), 459, {146, 155})
W(103, 2, ('CY', 9, 1), (1,), (7, 'n', 'Y2'), 459, {128, 308})
W(663, 2, ('CY', 1, 6), (2,), (7, 'Y+t'), 12, {10})

print('== ET/divisor classes')
ETT = [('D', (11,), 5, {2}), ('D', (541,), 270, {110}), ('I3', (1, 5, 3), 2, {1}),
       ('I3', (1, 11, 3), 5, {4}), ('I3', (1, 206, 15), 102, {50}),
       ('I3', (5, 19, 119), 180, {14, 50, 86, 122, 158}), ('II2', (1, 2, 31), 5, {3}),
       ('II2', (1, 8, 1887), 36, {30}), ('II2', (2, 2, 111), 18, {12}),
       ('II2', (7, 2, 671), 30, {26}), ('II2', (19, 6, 455), 6, {4})]
for kind, p, mod, res in ETT:
    adm, Pi, thr, S = derived_classes(7, 4, 9, kind, p)
    L = lcm(Pi, mod)
    der = {s for s in range(L) if s % Pi in S}
    cl = {s for s in range(L) if s % mod in res}
    ok = adm and cl <= der
    OK &= ok
    print(f'  {kind}{p}: adm={adm} Pi={Pi} thr={thr} {"OK" if ok else "FAIL"}'
          f'{"" if cl == der else " (derived larger " + str(sorted(S)) + ")"}')
    M, _, mem, sol = et(kind, p)
    rules.append(((lambda s, mem=mem, sol=sol: mem(nf(s)) and is_sol(nf(s), sol(nf(s)))), mod, res, thr))

L = 1
for _, mod, _, _ in rules:
    L = lcm(L, mod)
unc = [s for s in range(L) if not any(s % mod in res for _, mod, res, _ in rules)]
print('lcm', L, 'uncovered', unc[:20], len(unc))
OK &= not unc
print('max thr', max(t for *_, t in rules))
for s in range(0, SMAX + 1):
    if not any(s % mod in res and app(s) for app, mod, res, _ in rules):
        print('  s =', s, 'not solved by any rule')
        if s:
            OK = False
print('s=0:', F(1, 8) + F(1, 12) + F(1, 24) == F(4, 16))
print('ALL OK' if OK else 'PROBLEMS')
