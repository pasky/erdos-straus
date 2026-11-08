"""Independent Astra checks of SDEEPF words, residue cells, screens and 57-word cover.
Run: ulimit -v 4000000; timeout 600 uv run --no-project --python .venv/bin/python \
    python scripts/xrev_retro_sdeepf_checks.py
Uses sympy's Jacobi implementation, not the memo's routine. The largest allocation
is a bytearray of length L=1441440; no word-by-class matrix is constructed.
"""
import ast
import itertools
from pathlib import Path
import re
from sympy import factorint, jacobi_symbol


def good(n, t, u, v):
    assert min(t, u, v) >= 2 and t*u*v-u-v == n
    return jacobi_symbol(t*u-1, n) == -1


# Compare all residue predicates, without selecting a particular value of n.
positive = {(1,2,3), (1,3,2), (2,1,2), (2,2,1), (3,1,1)}
cells = 0
for t,u,v in itertools.product(range(16), repeat=3):
    n = t*u*v-u-v
    if n % 4 != 1:
        continue
    a = (n+t)*t*u*v % 8 == 0
    b = any(x % 4 == 0 for x in (t,u,v,t*u-1,t*v-1))
    c = (t%4,u%4,v%4) not in positive
    assert a == b == c
    cells += 1
print('admissible mod-16 cells:', cells, 'product = DK five slots = SDEEP cell function')

count = [0, 0, 0]
for n in range(5, 300001, 4):
    if n % 8 == 5 and n >= 13:
        assert good(n,3,3,(n+3)//8)
        count[0] += 1
    if n % 3 == 2 and n >= 17:
        assert good(n,(n+7)//12,4,3)
        count[1] += 1
    if n % 9 == 3 and n >= 57:
        assert good(n,(n+15)//36,3,12)
        count[2] += 1
assert good(21,3,3,3)  # missing small-case sentence in 3.1(c)
print('Thm 3.1 direct Jacobi witnesses through 300000:', count, 'and n=21 via (a)')

# §5's "exactly when ... prime factor" is not true at general fixed levels.
n,t,u,v = 21841,64,9,38
assert good(n,t,u,v)
factors = factorint(t*n+1)
assert all(q % t != t-1 for q in factors)
print('prime-only necessity counterexample:', n, (t,u,v), 'A/B', t*u-1, t*v-1,
      'factor(tn+1)', factors)

text = Path('data/z64/sdeepf/f4_witnesses.txt').read_text()
witnesses = re.findall(r'n=(\d+).*?good word t,u,v=(\d+),(\d+),(\d+) A=(\d+)', text)
values = set()
for entry in witnesses:
    n,t,u,v,A = map(int, entry)
    assert A == t*u-1 and good(n,t,u,v)
    values.add(n)
for filename in ('star_prime_zeros.txt','gstar_zeros.txt','r8_zeros_1e10.txt',
                 'composite_zeros_le8e6.txt'):
    source = Path('data/z58/screens', filename).read_text().splitlines()
    ns = {int(line.split()[0]) for line in source if line and line[0].isdigit()}
    assert ns - values <= {105}
    print('screen', filename, 'inputs', len(ns), 'witnessed', len(ns & values),
          'vacuous', sorted(ns-values))
print('witness rows', len(witnesses), 'distinct n', len(values))

# Read the actually used 57 words, not the original greedy 77 candidates.
lines = Path('data/z64/sdeepf/cover_check.txt').read_text().splitlines()
Aw = ast.literal_eval(lines[2].split('A-words ')[1])
UVw = ast.literal_eval(lines[3].split('uv-words ')[1])
L = 1441440
E = {1,9,25,49,81,105,121,169,225,249,265,289,321,345,361,385,441,505,529,561,585,609,
     625,681,721,729,769,825}
assert E == {m*m % 840 for m in range(1,840,2)} | {265,321,769,825}
covered = bytearray(L)
threshold = 0
for A,u in Aw:
    assert L % A == 0 and (A+1) % u == 0 and 2 <= u <= (A+1)//2
    odd = A
    while odd % 2 == 0:
        odd //= 2
    assert L % (8*odd) == 0
    threshold = max(threshold, 2*A-u)
    for n0 in range((-u)%A,L,A):
        if n0 % 4 != 1:
            continue
        t = (A+1)//u
        vals = [good(n0+k*L,t,u,(n0+k*L+u)//A) for k in (3,7)]
        assert vals[0] == vals[1]
        if vals[0]:
            covered[n0] = 1
for u,v in UVw:
    assert min(u,v) >= 2 and L % (8*u*v) == 0
    threshold = max(threshold, 2*u*v-u-v)
    for n0 in range((-(u+v))%(u*v),L,u*v):
        if n0 % 4 != 1:
            continue
        vals = [good(n0+k*L,(n0+k*L+u+v)//(u*v),u,v) for k in (3,7)]
        assert vals[0] == vals[1]
        if vals[0]:
            covered[n0] = 1
outside_count = 0
for n in range(1,L,4):
    if n % 840 not in E:
        outside_count += 1
        assert covered[n]
inside_missing = sum(not covered[n] for n in range(1,L,4) if n % 840 in E)
print('57-word cover: outside E', outside_count, 'all covered; threshold', threshold,
      'uncovered inside E', inside_missing)
