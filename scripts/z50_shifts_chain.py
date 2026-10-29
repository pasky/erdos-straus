# z50 shifts: chain-of-ratios evidence. Along the 𝒞-shifts v <= 128 (n ≡ 1 mod 8, n <= 1e8), compare the
# conditional hit probability among surviving non-squares with the marginal hit probability among non-squares.
# Squares fail at every shift, so non-square marginal fail = (mf - s)/(1 - s), non-square joint = (J - s)/(1 - s),
# where s = 5000/12500000 is the square fraction.
import sys
fn = sys.argv[1] if len(sys.argv) > 1 else 'data/z50_shifts/joint_N1e8.txt'
rows = []; cls = None
for l in open(fn):
    if l.startswith('# class'):
        cls = int(l.split('≡')[1].split()[0]); continue
    if l.startswith('#') or cls != 1: continue
    v, inC, mf, J = l.split()
    if int(inC): rows.append((int(v), float(mf), float(J)))
s = 5000 / 12500000
prev = 1.0; below = above = equal = 0
for v, mf, J in rows:
    Jn = (J - s) / (1 - s); mfn = (mf - s) / (1 - s)
    ch = 1 - Jn / prev; mh = 1 - mfn
    if abs(ch - mh) < 1e-9: equal += 1
    elif ch < mh: below += 1
    else: above += 1
    print(v, round(mh, 4), round(ch, 4))
    prev = Jn
print("# conditional hit vs non-square marginal hit: below", below, "above", above, "equal", equal, "of", len(rows))
