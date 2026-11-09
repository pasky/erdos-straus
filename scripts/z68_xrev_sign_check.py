"""Independent SIGN review checks; no lane functions imported.
Run: ulimit -v 6000000; timeout 300 uv run --with sympy --with scipy python
     scripts/z68_xrev_sign_check.py /tmp/xrev_SIGN
The argument is an archive of side-agent/z68-sign, plus f4_witnesses.txt
from data/z64/sdeepf/. It also needs replay_cells.txt (the memo's KT2 replay),
replay_profile41.txt / replay_profile211.txt (R=4/5, B=2000000), and
independent_interior.txt from z68_xrev_sign_interior.c. Arrays are linear
in one numerator, not Cartesian products.
"""
from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import re
import sys
from sympy import divisors, jacobi_symbol, primerange
from scipy.stats import spearmanr

root = Path(sys.argv[1])

def hj(n, a):
    w = []
    while a:
        q = (n + a - 1) // a
        w.append(q)
        n, a = a, q * a - n
    return tuple(w)

def continuants(w):
    c = [1]
    prev = 0
    for b in w:
        c.append(b * c[-1] - prev)
        prev = c[-2]
    return c

def K(w):
    return continuants(w)[-1]

def J(a, n):
    return int(jacobi_symbol(a, n))

counts = Counter()
examples = {}
for n in list(range(3, 202, 2)) + [333, 2025]:
    signs = [J(a, n) for a in range(n)]
    actual = set()
    triples = []
    lhs = rhs = 0
    for a in range(1, n):
        if gcd(a, n) != 1:
            continue
        w = hj(n, a)
        r = len(w)
        pre, suf = continuants(w), continuants(w[::-1])
        middle = continuants(w[1:])
        assert pre[-1] == n and K(w[1:]) == a
        if isqrt(n) ** 2 == n:
            assert signs[a] == 1
        if r == 3:
            triples.append((w[1], w[2], w[0]))
        for j, b in enumerate(w):
            X, Xp = pre[j], pre[j - 1] if j else 0
            Y, Yp = suf[r - j - 1], suf[r - j - 2] if j < r - 1 else 0
            assert n == b * X * Y - X * Yp - Xp * Y
            Z = middle[j - 1] if j else 0
            assert X * a == Y + Z * n
            if gcd(X, n) == 1:
                assert signs[a] == signs[X % n] * signs[Y % n]
            elif n == 21 and signs[a] != signs[X * Y % n]:
                examples.setdefault('split21', (w, j, a, X, Y))
            counts['splits'] += 1
            # Enumerate every k, not just prime factors, including empty tails.
            if Xp:
                for k in divisors(b):
                    if k < 2 or b // k < 2 or Yp % k or gcd(k, Xp) != 1:
                        continue
                    ww = hj(k * X, Xp)[::-1] + (b // k,) + hj(Y, Yp // k)
                    aa = K(ww[1:])
                    assert K(ww) == n and (k * X * aa - X * a) % n == 0
                    if gcd(k * X, n) == 1:
                        assert signs[aa] == signs[a] * signs[k % n]
                    counts['right_moves'] += 1
            if not (0 < j < r - 1 and b % (Xp * Yp) == 0 and b >= 2 * Xp * Yp):
                continue
            t, u, v = b // (Xp * Yp), Xp * Y, X * Yp
            a3 = t * u - 1
            assert min(t, u, v) >= 2 and hj(n, a3) == (v, t, u)
            assert r <= max(w) / 2 + 2
            if gcd(X * Xp * Y * Yp, n) == 1:
                assert signs[a3] == signs[a] * signs[Xp * Yp % n]
            elif signs[a3] != signs[a] * signs[Xp * Yp % n]:
                examples.setdefault(f'contract{n}', (w, j, a, (t, u, v), Xp * Yp))
            lhs += signs[a] * signs[Xp * Yp % n] == -1
            rhs += signs[a3] == -1
            actual.add((w, j))
            counts['contractions'] += 1
    # Independently enumerate refinements from the target, including the trivial ones.
    expected = set()
    for t, u, v in triples:
        for Xp in divisors(u):
            Y = u // Xp
            for Yp in divisors(v):
                X = v // Yp
                if X <= Xp or Y <= Yp or gcd(X, Xp) != 1 or gcd(Y, Yp) != 1:
                    continue
                left = hj(X, Xp)[::-1]
                ww = left + (t * Xp * Yp,) + hj(Y, Yp)
                expected.add((ww, len(left)))
    assert actual == expected, n
    counts['bijection_n'] += 1
    if n == 333:
        assert (lhs, rhs) == (32, 34)
        print('Prop8 composite counts', n, lhs, rhs)
print('independent algebra checks', dict(counts))
for key in ['split21', 'contract333', 'contract2025']:
    print(key, examples[key])
assert hj(137, 95) == (2, 2, 5, 6, 2)
assert (J(95, 137), J(3, 137), J(11, 137)) == (-1, -1, 1)

# Independent completeness of finite witness coverage, and direct Jacobi tests.
profile_files = ['profile_R5_B2e5.txt', 'profile_R5_B2e5_103_127.txt',
                 'profile_R5_B2e6_131_211.txt', 'profile_R4_B2e6.txt']
cov = {4: {}, 5: {}}
wit_counts = Counter()
for name in profile_files:
    for line in (root / 'data/z68/sign' / name).read_text().splitlines():
        if not line.startswith('W '):
            continue
        ell, r, g, X, Xp, Y, Yp = map(int, re.findall(r'\d+', line))
        assert gcd(X, Xp) == gcd(Y, Yp) == 1
        left, right = hj(X, Xp)[::-1], hj(Y, Yp)
        assert len(left) + len(right) + 1 == r
        mod, s = X * Y, Xp * Y + X * Yp
        assert mod % ell == 0 and (mod // ell) % ell != 0
        assert (s + 1) % (mod // ell) == 0 and -s % ell == g
        assert pow(g, (ell - 1) // 2, ell) == ell - 1
        # Scan b modulo 8, then use three representatives. No CRT helper.
        bs = [b for b in range(2, 10) if (b * mod - s) % 8 == 1]
        assert bs
        for b in (bs[0], bs[0] + 8, bs[0] + 80):
            w = left + (b,) + right
            nn = b * mod - s
            assert nn > 0 and K(w) == nn and J(K(w[1:]), nn) == -1
        cov[r].setdefault(ell, set()).add(g)
        wit_counts[r] += 1
assert set(cov[5]) == set(primerange(11, 212))
for ell, caught in cov[5].items():
    assert caught == {g for g in range(1, ell) if pow(g, (ell - 1) // 2, ell) == ell - 1}
branches = {}
for name in ['stree_certified.txt', 'stree_certified_small.txt']:
    for line in (root / 'data/z66/ucover' / name).read_text().splitlines():
        if line.startswith('ell='):
            ell = int(line.split(':')[0][4:])
            if ell >= 11:
                branches[ell] = set(map(int, re.findall(r'\d+', line.split('[')[1])))
assert set(branches) == set(primerange(11, 102))
assert all(cov[4][ell] & gs for ell, gs in branches.items())
print('independent profile witnesses', dict(wit_counts), '22 branch intersections verified')

# F3/F4: check the cited witnesses against the actual screen sets, not their summaries.
witnesses = {}
for line in (root / 'f4_witnesses.txt').read_text().splitlines():
    m = re.search(r'n=(\d+).*good word t,u,v=(\d+),(\d+),(\d+) A=(\d+)', line)
    if m:
        n, t, u, v, a = map(int, m.groups())
        assert t * u * v - u - v == n and t * u - 1 == a and J(a, n) == -1
        witnesses[n] = (t, u, v)
for name in ['star_prime_zeros', 'gstar_zeros', 'r8_zeros_1e10', 'composite_zeros_le8e6']:
    values = [int(line.split()[0]) for line in (root / 'data/z58/screens' / (name + '.txt')).read_text().splitlines()
              if line and not line.startswith('#')]
    assert all(n in witnesses for n in values if n != 105)
    print('screen witnesses', name, len(values), 'missing', [n for n in values if n not in witnesses])
assert all(len(hj(105, a)) != 3 for a in range(1, 105) if gcd(a, 105) == 1)

# F2: include u=1/v=1 boundary words when comparing the R/R8 screen counts.
cells = {}
for line in (root / 'replay_cells.txt').read_text().splitlines():
    if line.startswith('n='):
        cells[int(line.split()[0][2:])] = dict((k, int(v)) for k, v in re.findall(r'(\w+)=(\d+)', line))
for line in (root / 'data/z58/screens/r8_zeros_1e10.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    n, R, R8 = map(int, line.split())
    ds = divisors(n + 1)
    assert R == 2 * (cells[n]['t4'] + sum(d % 4 == 3 for d in ds))
    assert R8 == 2 * (cells[n]['t8'] + sum(d % 8 == 7 for d in ds))
print('R/R8 boundary-inclusive counts agree at all 12 screen primes')

# KT3 rank statistic recomputed separately; validate exact 21841 census by fractions.
rows = [list(map(int, s.split())) for s in (root / 'data/z68/sign/kt3_lengths_2e5.txt').read_text().splitlines()
        if s and not s.startswith('#')]
selected = [d for d in rows if d[0] > 10000 and min(d[3], d[5], d[7]) >= 10]
f3 = [d[4] / d[3] for d in selected]
f4 = [d[6] / d[5] for d in selected]
assert len(selected) == 4171
print('KT3 independent Spearman', len(selected), spearmanr(f3, f4).statistic)
row = next(d for d in rows if d[0] == 21841)
census = Counter()
for a in range(1, 21841):
    # Cap at 5: do not build unnecessarily long HJ expansions.
    N, D, r = 21841, a, 0
    while D and r < 6:
        N, D = D, ((N + D - 1) // D) * D - N
        r += 1
    if not D and 2 <= r <= 5:
        census[r] += 1
        census[-r] += J(a, 21841) == -1
assert row[1:] == [census[k] for r in range(2, 6) for k in (r, -r)]
print('21841 independent census', row)
# Corrected interior-only no-outgoing-move set, from the independent C enumerator.
interior = [list(map(int, s.split())) for s in (root / 'independent_interior.txt').read_text().splitlines()
            if s and not s.startswith('#')]
selected_i = [d for d in interior if d[1] >= 10 and d[4] >= 10]
x, y = [d[2] / d[1] for d in selected_i], [d[5] / d[4] for d in selected_i]
classes = [d[0] % 9240 for d in selected_i]
def residuals(values):
    totals, nums = Counter(), Counter()
    for c, v in zip(classes, values):
        totals[c] += v
        nums[c] += 1
    return [v - totals[c] / nums[c] for c, v in zip(classes, values)]
print('interior-only NOOUT', len(selected_i), 'share', sum(d[4] for d in interior) / sum(d[3] for d in interior),
      'rho', spearmanr(x, y).statistic, 'within9240', spearmanr(residuals(x), residuals(y)).statistic)
for d in interior:
    known = next(row for row in rows if row[0] == d[0])
    assert d[1:4] == [known[3], known[4], known[5]]
for ell, replay, original in [(41, 'replay_profile41.txt', 'profile_R4_B2e6.txt'),
                               (211, 'replay_profile211.txt', 'profile_R5_B2e6_131_211.txt')]:
    def selected_lines(path):
        return [line for line in path.read_text().splitlines()
                if line.startswith(f'{ell} ') or line.startswith(f'W {ell} ')]
    assert selected_lines(root / replay) == selected_lines(root / 'data/z68/sign' / original)
print('All independent checks passed; ES remains open.')
