"""review_r241_compare.py (R241): compare review_r241_enum.py output (q = 9) with the author's data/zc/p_<s>.txt and
compute the exact P8-mass from ORDERED tuples (no orientation multiplicity tricks).
P8 = {E0 : E0^4 = -1} = odd discrete logs (q = 9). Law: E0^s = eps(s; z, t).
usage: review_r241_compare.py enum_output [datadir]"""
import sys
from fractions import Fraction as Fr
q = 9
rows = {}
for l in open(sys.argv[1]):
    if not l.startswith('P '):
        continue
    f = l.split()
    s, a, b, z, y, t = map(int, f[1:7])
    h = {int(k): int(v) for k, v in (x.split(':') for x in f[7:])}
    rows[(s, a, b, z, y, t)] = h
datadir = sys.argv[2] if len(sys.argv) > 2 else 'data/zc'
svals = sorted(set(k[0] for k in rows))
total = Fr(0)
for s in svals:
    N = s // 2   # ceil((s-1)/2)
    p8_ordered = sum(c for k, h in rows.items() if k[0] == s for e, c in h.items() if e % 2 == 1)
    allt = sum(c for k, h in rows.items() if k[0] == s for c in h.values())
    by_e = {}
    for k, h in rows.items():
        if k[0] == s:
            for e, c in h.items():
                by_e[e] = by_e.get(e, 0) + c
    # symmetry check: count(a,b,...) on P8 == count(b,a,...) on P8
    asym = 0
    for (s_, a, b, z, y, t), h in rows.items():
        if s_ != s:
            continue
        c1 = sum(c for e, c in h.items() if e % 2)
        h2 = rows.get((s, b, a, z, y, t), {})
        c2 = sum(c for e, c in h2.items() if e % 2)
        asym += (c1 != c2)
    mass = Fr(p8_ordered, q ** N)
    total += mass
    msg = f's={s} all={allt} P8_ordered={p8_ordered} mass={float(mass):.6e} byE0log={dict(sorted(by_e.items()))} asym={asym}'
    # compare with author file
    try:
        lines = open(f'{datadir}/p_{s}.txt').read().split('\n')
    except FileNotFoundError:
        print(msg); continue
    au = {}
    for l in lines:
        if not l.strip():
            continue
        f = l.split()
        ss, a, z, y, t = map(int, f[:5])
        au[(a, z, y, t)] = f[5]
    mism = 0; aumass = Fr(0); nsk = 0
    mine = {}
    for (s_, a, b, z, y, t), h in rows.items():
        if s_ != s or a > b:
            continue
        mine[(a, z, y, t)] = sum(c for e, c in h.items() if e % 2)
    for k, v in au.items():
        if v == 'SKIP':
            nsk += 1; continue
        a, z, y, t = k
        b = s - a - z
        mult = 1 if a == b else 2
        aumass += Fr(mult * int(v), q ** N)
        if mine.get(k, 0) != int(v):
            mism += 1; print('  MISMATCH', s, k, 'author', v, 'mine', mine.get(k, 0))
    # P8 tuples of mine in patterns absent from author's file (must be 0: author lists all compatible patterns)
    absent = sum(c for k, c in mine.items() if k not in au and c)
    print(msg, f'| author lines={len(au)} skip={nsk} mism={mism} author_mass={float(aumass):.6e} mine_in_absent_patterns={absent}')
print(f'total exact P8 mass over s in {svals}: {float(total):.8f}')
