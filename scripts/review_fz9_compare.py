"""R221: compare per-pattern counts of review_fz9_enum (stdin file) with fz_enum's data/fz/enum9/e_<s>.txt.gz."""
import gzip, sys
from fractions import Fraction
mine = {}
for line in open(sys.argv[1]):
    if line.startswith('#'): continue
    f = line.split()
    if f[5] == 'SKIP': continue
    mine[tuple(map(int, f[:5]))] = int(f[5])
levels = sorted({k[0] for k in mine})
bad = 0; tot = Fraction(0)
for s in levels:
    theirs = {}
    for line in gzip.open(f'data/fz/enum9/e_{s}.txt.gz', 'rt'):
        f = line.split(); theirs[tuple(map(int, f[:5]))] = f[5]
    mk = {k: v for k, v in mine.items() if k[0] == s}
    if set(mk) - set(theirs): print('patterns missing in theirs', s, set(mk) - set(theirs)); bad += 1
    allpat = set(theirs) == set(mk)
    m_s = Fraction(0)
    for k, v in mk.items():
        if theirs.get(k) != str(v): print('MISMATCH', k, v, theirs.get(k)); bad += 1
        a, z, y, t = k[1:]; b = s - a - z
        m_s += (1 if a == b else 2) * v * Fraction(9) ** (1 - (s + 1) // 2)
    tot += m_s
    print(f's={s} patterns compared {len(mk)}/{len(theirs)} complete={allpat} mass={float(m_s):.6e} cum={float(tot):.6f}')
print('mismatches', bad)
