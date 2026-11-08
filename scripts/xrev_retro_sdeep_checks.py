"""Astra retro audit: independent small enumeration, KS0 slices and file statistics.
Run from repo root after compiling z64_sdeep_decide.c to the executable argument:
ulimit -v 4000000; timeout 600 uv run --no-project --python .venv/bin/python python \
    scripts/xrev_retro_sdeep_checks.py /tmp/xrev_retro_sdeep_decide
Only the selected large full-mode rows reuse the original enumerator; early rows
also get an independent sympy divisor/Jacobi check. No large Cartesian arrays.
"""
import math
from pathlib import Path
import random
import subprocess
import sys
from sympy import divisors, jacobi_symbol


def rows(name):
    return [line.split() for line in Path('data/z64/sdeep', name).read_text().splitlines()
            if line and line[0].isdigit()]


def rerun(selected, mode):
    text = ''.join(f'{r[0]} {r[1]}\n' for r in selected)
    result = subprocess.run([sys.argv[1], mode], input=text, text=True,
                            capture_output=True, check=True, timeout=500)
    actual = [line.split() for line in result.stdout.splitlines()]
    assert actual == selected, [(a, b) for a, b in zip(actual, selected) if a != b][:3]


# Independent generation by t and u, rather than factoring every n+u.
N = 20000
counts = [[0, 0, 0, 0] for _ in range(N + 1)]
words = 0
for t in range(2, (N + 4) // 4 + 1):
    u = 2
    while t*u*u - 2*u <= N:
        A = t*u - 1
        for v in range(u, (N + u)//A + 1):
            n = v*A - u
            if n % 4 != 1:
                continue
            words += 1
            row = counts[n]
            row[0] += 1
            row[3] = min(row[3] or u, u)
            j = int(jacobi_symbol(A, n))
            if j == -1:
                row[1] += 1
                row[2] = min(row[2] or u, u)
            assert (j == -1) == ((n+t)*t*u*v % 8 == 0)
            assert (j == -1) == any(x % 4 == 0 for x in (t,u,v,A,t*v-1))
            for z in (t*(u+v), t*(u+v)-4):
                if math.gcd(z, n) == 1:
                    assert int(jacobi_symbol(z, n)) == j
        u += 1
expected = [[str(n), 'small', 'F', str(int(counts[n][0] > 0)),
             *map(str, counts[n])] for n in range(5, N+1, 4)]
rerun(expected, 'F')
print(f'small independent: {len(expected)} n, {words} reversal orbits; all counts/signs/trace checks agree')

rng = random.Random(64042)
for filename in ('ks0_neardsq_full.txt', 'ks0_dm2_full.txt'):
    data = rows(filename)
    assert all(int(r[0]) % 4 == 1 and math.isqrt(int(r[0]))**2 != int(r[0]) for r in data)
    assert all(r[3] == '1' and int(r[5]) > 0 for r in data)
    chosen = [min(data, key=lambda r:int(r[0])), max(data, key=lambda r:int(r[0])),
              min(data, key=lambda r:int(r[5])), rng.choice(data)]
    rerun(chosen, 'F')
    print(filename, 'rows', len(data), 'min_pairs', min(int(r[4]) for r in data),
          'min_negative', min(int(r[5]) for r in data),
          'min_fraction', min(int(r[5])/int(r[4]) for r in data),
          'max_n', max(int(r[0]) for r in data), 'full_rerun', [r[0] for r in chosen])

early = rows('ks0_lcm_early.txt')
assert all(r[3] == '1' and int(r[5]) > 0 for r in early)
assert all(int(r[0]) % 4 == 1 and math.isqrt(int(r[0]))**2 != int(r[0]) for r in early)
# Stratify by the actual leading tag (c / d etc.) in the stored file.
for tag in sorted({r[1].split(':')[0] for r in early}):
    family = [r for r in early if r[1].split(':')[0] == tag]
    selected = rng.sample(family, min(64, len(family)))
    selected.append(max(family, key=lambda r:int(r[6])))
    rerun(selected, 'E')
    for r in selected:
        n = int(r[0])
        total = negative = first = least = 0
        for u in range(2, int(r[6])+1):
            for A in divisors(n+u):
                if A < 2*u-1 or (A+1) % u or (n+u)//A < u:
                    continue
                total += 1
                first = first or u
                if jacobi_symbol(A, n) == -1:
                    negative += 1
                    least = least or u
        assert [1, total, negative, least, first] == list(map(int, r[3:])), r
    print('early', tag, 'rows', len(family), 'independent/rerun', len(selected),
          'max_exit_u', max(int(r[6]) for r in family))

screens = rows('ks0_screens_full.txt')
rerun(screens, 'F')
print('screen full rerun', len(screens), 'vacuous', [r[0] for r in screens if r[3]=='0'])

# The trace identity cannot be evaluated at n without its coprimality clause.
t,u,v = 7,3,9
n = t*u*v-u-v
A, B = t*u-1, t*v-1
assert n == 177 and (A+B) % 4 == 2
assert math.gcd(math.gcd(n,B-A),t) == 1  # primitive form
assert jacobi_symbol(A,n) == -1 and jacobi_symbol(A+B+2,n) == 0
print('genus proof scope: primitive [177,42,-7], s=82, (20/177)=-1 but (84/177)=0')
