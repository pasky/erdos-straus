"""Independent CROSSU review audit; stdlib only, bounded and streaming.
Usage: timeout 900s uv run python scripts/z55_xrev_crossu_check.py ARCHIVE ENGINE
Run with ulimit -v 6000000. ARCHIVE contains the reviewed branch's files.
Replays all TSV rows, regenerates pair dumps, and checks selected shells by
scanning w (not the engine's factorisation of n+u). No ES claim is tested.
"""
import csv
from fractions import Fraction
import math
from pathlib import Path
import resource
import statistics
import subprocess
import sys

limit = 6_000_000 * 1024
soft, hard = resource.getrlimit(resource.RLIMIT_AS)
resource.setrlimit(resource.RLIMIT_AS, (min(limit, soft) if soft >= 0 else limit, hard))
root, engine = Path(sys.argv[1]), sys.argv[2]
with (root / 'data/z55/crossu/main.tsv').open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
classes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 25, -1, -2, -3, -4)
pairdir = root / 'pairs_replay'
pairdir.mkdir(exist_ok=True)
checkdir = root / 'direct_replay'
checkdir.mkdir(exist_ok=True)
by = {}
for row in rows:
    by.setdefault(row['tag'], []).append(row)
print('populations:', {tag: len(rs) for tag, rs in by.items()}, flush=True)
# Keep independent direct scans below 2 million w's apiece.
selected = {int(rs[0]['n']) for rs in by.values() if int(rs[0]['X']) <= 2_000_000}
selected.add(int(rows[1]['n']))
for i, row in enumerate(rows):
    n = int(row['n'])
    dump = pairdir / f'{n}.txt' if row['tag'] in ('p1e12', 'p1e13') else checkdir / f'{n}.txt'
    args = [row[k] for k in ('n', 'U0', 'U1', 'Y', 'X')]
    save = row['tag'] in ('p1e12', 'p1e13') or n in selected
    out = subprocess.check_output(['timeout', '45s', engine, *args, *([str(dump)] if save else [])],
                                  text=True, timeout=50)
    fresh = dict(token.split('=') for token in out.split())
    assert all(row[k] == value for k, value in fresh.items()), (n, fresh)
    if (i + 1) % 100 == 0:
        print('all fields reproduced:', i + 1, flush=True)
print('all fields reproduced:', len(rows), 'S3 points:', sum(int(r['nsh3']) for r in rows), flush=True)


def squarefree_table(bound):
    flags = bytearray(b'\1') * (bound + 1)
    flags[0] = 0
    for q in range(2, math.isqrt(bound) + 1):
        square = q*q
        flags[square::square] = b'\0' * (bound // square)
    return flags


def direct(row):
    n, lo, hi, y, cap = (int(row[k]) for k in ('n', 'U0', 'U1', 'Y', 'X'))
    flags = squarefree_table(cap)
    groups = {}
    for u in range(lo + 1, hi + 1):
        if u % 4 == 1 and flags[u] and math.gcd(n, u) == 1:
            units = [a for a in range(1, u) if math.gcd(a, u) == 1]
            groups[u] = (len(units), {a*a % u for a in units})
    shell = 0
    points = set()
    sums = {f'{prefix}{c}': Fraction(0) for c in classes for prefix in 'NGEV'}
    for w in range(y + 1 + (y % 2), cap + 1, 2):
        u = -n % w
        if u not in groups or not flags[w] or math.gcd(w, n*u) != 1:
            continue
        shell += 1
        d = (n + u) // (2*w)
        if d % 4 != 3:
            continue
        phi, squares = groups[u]
        j = -pow(d, -1, u) % u
        points.add((u, w, d, j, int(j in squares)))
        for c in classes:
            if math.gcd(c, u) != 1:
                continue
            sums[f'N{c}'] += 2 * (j == c % u)
            sums[f'E{c}'] += Fraction(2, phi)
            if j * pow(c, -1, u) % u in squares:
                sums[f'G{c}'] += Fraction(2, len(squares))
                sums[f'V{c}'] += 4 * Fraction(len(squares)-1, len(squares)**2)
    dump = checkdir / f'{n}.txt'
    saved = {tuple(map(int, line.split())) for line in dump.read_text().splitlines()}
    assert points == saved, (n, len(points), len(saved))
    assert shell == int(row['nshell'])
    assert all(abs(float(value)-float(row[key])) <= 5.01e-7 for key, value in sums.items())
    print('independent w-scan and all 18 rational twisted layers:', n, shell, len(points), flush=True)


for row in rows:
    if int(row['n']) in selected:
        direct(row)

primes = [r for r in rows if r['tag'].startswith('p1e')]
for c in (1, -1, 2, 4, 12, 25):
    delta = [float(r[f'N{c}']) - float(r[f'G{c}']) for r in primes]
    z = sum(delta) / math.sqrt(sum(float(r[f'V{c}']) for r in primes))
    print('pooled z:', c, z)
means, ratios, zs = [], [], []
for tag, rs in by.items():
    if not tag.startswith('p1e'):
        continue
    for c in classes:
        delta = [float(r[f'N{c}']) - float(r[f'G{c}']) for r in rs]
        variance = sum(float(r[f'V{c}']) for r in rs)
        means.append(statistics.mean(delta))
        ratios.append(statistics.stdev(delta)/math.sqrt(variance/len(rs)))
        zs.append(sum(delta)/math.sqrt(variance))
print('prime-sample mean / sd-ratio / z ranges:', *((min(v), max(v)) for v in (means, ratios, zs)))
for tag, rs in by.items():
    if all(math.isqrt(int(r['n']))**2 == int(r['n']) for r in rs):
        vanishing = [c for c in classes if all(float(r[f'{key}{c}']) == 0 for r in rs for key in 'NGV')]
        print('square zero classes:', tag, vanishing)
        assert set(vanishing) == {1, 4, 9, 16, 25, -1, -4}

out = subprocess.check_output(['timeout', '90s', 'uv', 'run', 'python',
                               str(root/'scripts/z55_crossu_pairs.py'), str(pairdir), '20', '200'],
                              text=True, timeout=100)
assert out == (root/'data/z55/crossu/pairs_1e12_1e13.txt').read_text()
print('pair replay agrees byte-for-byte:\n' + out)
