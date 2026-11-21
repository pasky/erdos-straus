"""Negative controls for the coverage routine of opus_r3_cover.py (must DETECT gaps)."""
import json, random
from opus_r3_cover import coverage, R
def gaps(rows, L):
    try: coverage(rows, L); return None
    except AssertionError as e: return e.args[0] if e.args else 'assert'
c11 = json.loads((R / 'r2/cover-11.json').read_text()); L = c11['period']
print('r2/cover-11 (known sole gap 0 mod P9):', gaps(c11['rows'], L))
print('r2/cover-11 + dummy [P9,0]:', gaps(c11['rows'] + [[L, 0]], L))
rng = random.Random(5)
for m in range(22, 31):
    c = json.loads((R / f'cover-{m}.json').read_text()); rows = c['rows']; L = c['period']
    noX = [r for r in rows if r[2] != 'X']
    out = [f'm={m} drop X: {gaps(noX, L)}']
    if m == 22:
        out.append(f'drop X2 only: {gaps([r for r in rows if not (r[2]=="X" and r[3]==218243025)], L)}')
        out.append(f'drop X1 only: {gaps([r for r in rows if not (r[2]=="X" and r[3]==34459425)], L)}')
    # drop a few random single fixed rows; report how many are individually necessary
    nec = 0; tried = 0
    for i in rng.sample(range(len(rows)), min(25, len(rows))):
        tried += 1; g = gaps(rows[:i] + rows[i + 1:], L)
        if g is not None: nec += 1
    out.append(f'{nec}/{tried} random single-row deletions create a detected gap')
    print('; '.join(out), flush=True)
