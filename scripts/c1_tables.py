# c1_tables.py -- print LaTeX rows of the certificate tables of paper/es-exponential-families.tex from the rule
# lists of c1_expfam_verify.py (classes are DERIVED by the verifier's analyse()).  Helper only.
import sys
from math import gcd
import c1_expfam_verify as V

def nclass(p):
    fam = p[0]
    if fam == 'D': return r'$%d\mid n$' % p[1]
    if fam == 'II2':
        a, d, f = p[1:]; return r'$n\equiv%d\ (%d)$' % ((-4 * a * a * d) % f, f)
    if fam == 'I1':
        a, d, f = p[1:]; return r'$n\equiv%d\ (%d)$' % ((-f) % (4 * a * d), 4 * a * d)
    if fam == 'II1':
        a, b, e = p[1:]; return r'$n\equiv%d\ (%d)$' % ((-e) % (4 * a * b), 4 * a * b)
    if fam == 'I2':
        a, c, f = p[1:]; r2 = (-c * pow(a, -1, f)) % f
        return r'$n\equiv%d\ (%d)$, $n\equiv%d\ (%d)$' % ((-f) % (4 * a * c), 4 * a * c, r2, f)
    if fam == 'I3':
        c, d, f = p[1:]; return r'$n\equiv%d\ (%d)$, $f\mid n^2+%d$' % ((-f) % (4 * c * d), 4 * c * d, 4 * c * c * d)

def rows(F, specs):
    out = []
    for r, p in zip(F.rules, specs):
        A = V.analyse(F, r); P = r['sigma'] * A['T']
        cls = sorted((r['s0'] + r['sigma'] * v) % P for v in A['V'])
        thr = r['s0'] + r['sigma'] * A['tstar']
        out.append('%s$(%s)$ & %s & $s\\equiv %s\\pmod{%d}$%s \\\\' % (p[0], ','.join(map(str, p[1:])), nclass(p),
                   ','.join(map(str, cls)), P, '' if thr <= 0 else ', $s\\ge%d$' % thr))
    return out

def wrows():
    F = V.Fam('7*4^s+9', 7, 4, 9)
    out = []
    for w in V.C7W:
        F.rules = []; F.z14(*w); r = F.rules[0]; A = V.analyse(F, r)
        m, j, code, ww, h, eps, i = w
        P = r['sigma'] * A['T']; cls = sorted((r['s0'] + r['sigma'] * v) % P for v in A['V'])
        if code == 0:
            Ydef = r'4^{(s-%d)/%d}' % (j, h) if h > 1 else r'4^{s-%d}' % j
            names = {1: [r'(Y+%d)' % ww], 3: ['(Y+1)', '(Y^2-Y+1)'], 9: ['(Y+1)', '(Y^2-Y+1)', '(Y^6-Y^3+1)']}[h]
        else:
            Ydef = r'2^{(s-%d)/2}' % (j + 1); names = ['f_+', 'f_-']
        pcs = ['7', 'n'] + names
        d1 = [p for p, e in zip(pcs, eps) if e == 1]; d2 = [p for p, e in zip(pcs, eps) if e == -1]
        if i > 0: d1 = ['2^{%d}' % i if i > 1 else '2'] + d1
        if i < 0: d2 = ['2^{%d}' % -i if i < -1 else '2'] + d2
        fmt = lambda L: r'\cdot '.join(L) if L else '1'
        out.append(r'$%d$ & $%d$ & %s & $%s$ & $%s$ & $%s$ & $%s\pmod{%d}$ \\' % (m, j, ['CY', 'SG', 'SG'][code] + ('$_{%d}$' % h if code == 0 and h > 1 else ''),
                   Ydef, fmt(d1), fmt(d2), ','.join(map(str, cls)), P))
    return out

which = sys.argv[1]
if which == '63':
    F = V.fam_63(); specs = [None] + [p for p in [('D', 5), ('II2', 1, 2, 15), ('II2', 2, 2, 15), ('II2', 5, 3, 119), ('II2', 5, 2, 39),
              ('II2', 1, 5, 19), ('I1', 1, 146, 39), ('D', 11), ('II2', 3, 1, 11), ('II2', 1, 1, 11), ('D', 29),
              ('II2', 1, 11, 87), ('D', 127), ('II2', 1, 32, 127), ('I1', 1, 86, 23), ('II1', 1, 254, 15),
              ('I1', 1, 1405, 511), ('I2', 2, 43, 151)]]
    F.rules = F.rules[1:]; specs = specs[1:]
elif which == '105':
    F = V.fam_105(); F.rules = F.rules[1:]
    specs = [('D', 11), ('II2', 1, 1, 11), ('II2', 1, 3, 11), ('D', 41), ('II2', 2, 53, 1271), ('II2', 3, 22, 527),
             ('II2', 1, 6, 143), ('II2', 1, 2, 151), ('D', 13), ('D', 19), ('II2', 5, 1, 19), ('II2', 2, 5, 39), ('II2', 1, 2, 39)]
elif which == '15':
    F = V.fam_15(); specs = [('II2', 1, 1, 7), ('II2', 2, 1, 7), ('II2', 2, 5, 39), ('D', 31), ('II2', 1, 8, 31), ('II2', 1, 3, 11),
              ('II2', 1, 5, 99), ('D', 11), ('II2', 3, 1, 11), ('II2', 1, 3, 287), ('II2', 1, 24, 287)]
elif which == 'c7':
    F = V.fam_c7_k9(); F.rules = F.rules[len(V.C7W):]; specs = V.C7
elif which.startswith('k'):
    k = int(which[1:]); F = V.fam_nine(k); specs = V.NINE[k]
if which != 'c7w': print('\n'.join(rows(F, specs)))

if which == 'c7w': print('\n'.join(wrows()))
