"""O99 (POINTWISE_TYPEI6.md, Comp 4.1 regression): classify the complete per-(L,b) solution lists of
scripts/typei4_lb.c (rows: L b a c' g delta P1 X F e) by regime (TYPEI5 Prop 3.3) and check that every
regime-(v) solution appears in the output of scripts/typei6_vsearch.c (rows: L b a c' delta P1 X).
Usage: python scripts/typei6_regress.py lb.txt vs.txt"""
import sys
lb = [list(map(int, l.split())) for l in open(sys.argv[1]) if l.strip()]
vs = {tuple(map(int, l.split())) for l in open(sys.argv[2]) if l.strip()}
nv = 0
for L, b, a, cp, g, dl, P1, X, F, e in lb:
    T = 2 ** (L - 4); u = 7 ** b; j = T * u // 2 - cp * g * dl; m = cp * dl * dl
    if j < 0:
        reg = 'A'
    else:
        rho = (T * u // 2 + j) // P1; lam = (rho * j - m) // u
        sigma = 8 * 7 ** a * m * j + 4 * T * j - T * T * u
        reg = 'v' if (lam > 0 and sigma > 0) else ('iv' if lam > 0 and sigma == 0 else ('iii' if lam > 0 else 'ii'))
    key = (L, b, a, cp, dl, P1, X)
    found = key in vs
    print(L, b, a, cp, dl, P1, X, 'regime', reg, 'found_by_vsearch' if found else '-')
    if reg == 'v':
        nv += 1; assert found, key
lbkeys = {(r[0], r[1], r[2], r[3], r[5], r[6], r[7]) for r in lb}
extra = vs - lbkeys
print(f"{len(lb)} lb solutions, {nv} in regime (v), all found; vsearch extra (not in lb lists): {sorted(extra)}")
