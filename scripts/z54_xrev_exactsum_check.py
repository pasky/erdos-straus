"""Independent z54 EXACTSUM audit; stdlib only, bounded inputs, no repo writes.
Usage: timeout 180s uv run --no-project scripts/z54_xrev_exactsum_check.py /tmp/xrev_EXACTSUM
Run under ulimit -v 6000000 and ulimit -t 180. Compile cond/wsum in ROOT first.
"""
import csv
import math
import statistics as st
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

root = Path(sys.argv[1])
data = root / 'data/z54/exactsum'

def rows(name):
    with (data / name).open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def run(name, args):
    return subprocess.run(['timeout', '20s', str(root / name), *map(str, args)],
                          check=True, text=True, capture_output=True, timeout=25).stdout

def factors(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = 1
    return out

def prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

# Exact rational independent shell enumeration (small hard cases and controls).
def exact(n, lo, hi, y, x):
    assert hi <= 300 and n < 2 * 10**9  # bound trial factoring/enumeration
    R, G, P = 0, F(0), F(0)
    D = defaultdict(F)
    shell = 0
    for u in range(lo + 1, hi + 1):
        if u % 4 != 1 or math.gcd(u, n) != 1:
            continue
        fu = factors(u)
        if any(e != 1 for e in fu.values()):
            continue
        phi = math.prod(p - 1 for p in fu)
        divs = [1]
        for p in factors(n + u):
            if p != 2:
                divs += [d * p for d in divs]
        for w in divs:
            if not y < w <= x or math.gcd(w, n * u) != 1:
                continue
            shell += 1
            v = (n + u) // (2 * w)
            if v % 4 != 3:
                continue
            s = -v
            cls = 2 * (v % (4 * u) == 4 * u - 1)
            gen = F(2 * 2**len(fu), phi) * all(
                s % p in {a*a % p for a in range(1, p)} for p in fu)
            R += cls
            G += gen
            local, freq = F(0), F(0)
            primes = list(fu)
            for mask in range(1 << len(primes)):
                subset = [p for j, p in enumerate(primes) if mask >> j & 1]
                f = math.prod(subset)
                leg = math.prod(1 if pow(s, (p-1)//2, p) == 1 else -1 for p in subset)
                raw = math.prod(p - 2 if s % p == 1 else -1 for p in subset)
                term = F(2 * (raw - leg), phi)
                local += term
                D[f] += term
                # Exact sum over reduced additive frequencies = Ramanujan sum.
                freq += F(math.prod(p-1 if (v+1) % p == 0 else -1 for p in subset), u)
            assert local == cls - gen
            assert freq == F(cls, 2)
            P += freq
    assert sum(D.values()) == R - G and P == F(R, 2)
    return R, G, D, shell

k, l = F(1, 30), F(13, 15)
a0, a1, b, g, eps = map(F, ('0.200', '0.204', '0.7925', '0.7955', '0.00001'))
tau = F(101, 400) + 100 * eps
slacks = [1-a1-g, b-tau*(1+a1)-4*eps, a0-tau*tau*(1+a1)-3*eps,
          b-2*a1-tau-4*eps, (F(1,2)-eps)*(b-a1)-a1-eps/2,
          g-b, a1-a0, a0*(1+k)-k-(l-k)*(1-b)]
assert all(v > 0 for v in slacks)
eta = slacks[-1] / (1+k)
power = (2+k-l)/(1+k)
print('WINDOW slacks', [str(v) for v in slacks])
print('eta', eta, 'conductor power', power, 'endpoint', eta/power,
      'claimed .00036 slack', eta-power*F('0.00036'))
assert eta == F(1,2480) and eta/power == F(1,2800)

all_profiles = {}
maxerr = 0.0
for win in ('std', 'thx', 'dyad', 'dyad16'):
    rr = rows(f'prof_{win}.tsv')
    all_profiles[win] = rr
    groups = defaultdict(list)
    for row in rr:
        groups[row['tag']].append(row)
        maxerr = max(maxerr, float(row['maxerr']))
    for tag, group in groups.items():
        if len(group) < 2:
            continue
        col = lambda key: [float(r[key]) for r in group]
        rg = col('RG')
        v = st.variance(rg)
        if v == 0:
            assert all(float(r['R']) == float(r['G']) == 0 for r in group)
            print('SQUARES', win, tag, len(group), 'mean triangle', st.mean(col('sumAbsDf')))
            continue
        frac = lambda keys: st.variance([sum(float(r[key]) for key in keys) for r in group])/v
        print('PROFILE', win, tag, len(group), 'var', round(v, 6),
              'low/top/one/three/long', *(round(frac(keys), 6) for keys in
              [('A0','A1'), ('Atop',), ('B1',), ('B1','B2'), ('B4','B5')]))
print('PROFILE max pointwise identity roundoff', maxerr)
primes = [int(r['n']) for r in all_profiles['std'] if r['tag'].startswith('R1e')]
assert len(primes) == len(set(primes)) == 1000
assert all(n % 24 == 1 and prime(n) for n in primes)
print('PRIMES 1000 distinct, deterministic Miller-Rabin < 2^64, all 1 mod 24')

# Rerun engine on one saved row per scale/window; integer outputs and rounded floats agree.
nruns = 0
for win, rr in all_profiles.items():
    for tag in ('R1e10', 'R1e12', 'R1e14'):
        row = next(r for r in rr if r['tag'] == tag)
        out = dict(t.split('=') for t in run('cond', [row[k] for k in ('n','U0','U1','Y','X')]).split())
        for key, value in out.items():
            if key in row:
                assert math.isclose(float(value), float(row[key]), rel_tol=1e-8, abs_tol=1e-6), (win, tag, key)
        nruns += 1
print('ENGINE', nruns, 'reruns at 1e10/1e12/1e14 agree in all saved columns')

hard = rows('prof_hard_std.tsv')
for row in hard:
    args = [int(row[k]) for k in ('n','U0','U1','Y','X')]
    R, G, D, shell = exact(*args)
    assert R == int(row['R']) and shell == int(row['shell'])
    assert abs(float(G)-float(row['G'])) <= 0.00000051
print('EXACT', len(hard), 'hard cases: rational R,G, conductor and full frequency identities agree')
for row in [r for r in all_profiles['std'] if math.isqrt(int(r['n']))**2 == int(r['n'])][:5]:
    R, G, D, shell = exact(*[int(row[k]) for k in ('n','U0','U1','Y','X')])
    assert R == G == 0
print('EXACT 5 square controls: R=G=0; all pointwise identities hold')
R, G, D, shell = exact(1000223521, 10, 200, 1000, 625000)
assert D[197] >= 1
# For prime f=197, D_f=2R_hits-4G_hits/(f-1), computed separately below.
wf = [w for w in range(1001, 625001, 2) if (1000223521+197) % w == 0
      and all(e == 1 for e in factors(w).values()) and math.gcd(w, 197*1000223521) == 1
      and ((1000223521+197)//(2*w)) % 4 == 3]
Pf = sum((F(196,197) if (((1000223521+197)//(2*w))+1) % 197 == 0 else -F(1,197)) for w in wf)
assert Pf >= F(1,2)
print('NO-GO n=1000223521 D197=', D[197], float(D[197]), 'P197=', Pf, float(Pf))

for win in ('std','dyad'):
    rr = rows(f'diag_{win}.tsv')
    for tag in ('R1e10','R1e12','R1e14'):
        group = [r for r in rr if r['tag'] == tag]
        ratio = st.variance(float(r['RG']) for r in group)/st.mean(float(r['sumTu2']) for r in group)
        print('CROSSU', win, tag, round(ratio, 6))

freq = [line.split() for line in (data/'wsum_std.tsv').read_text().splitlines()]
groups = defaultdict(list)
for row in freq:
    n, q, nu, nt = map(int, row[:4])
    if q == 1 or nt == 0 or math.isqrt(n)**2 == n:
        continue
    group = (len(str(n))-1, '3-9' if q < 10 else '11-29' if q < 30 else '31-99')
    groups[group].append(float(row[7])/float(row[5]))
for group, values in sorted(groups.items()):
    print('FREQUENCY', group, 'median rms/benchmark', round(st.median(values), 6))
for scale in (12,14):
    n = next(int(r[0]) for r in freq if len(r[0])-1 == scale and math.isqrt(int(r[0]))**2 != int(r[0]))
    saved = [r for r in freq if int(r[0]) == n]
    row = next(r for r in all_profiles['std'] if int(r['n']) == n)
    new = [line.split() for line in run('wsum', [row[k] for k in ('n','U0','U1','Y','X')] + [99]).splitlines()]
    assert len(saved) == len(new)
    for old, got in zip(saved, new):
        assert all(math.isclose(float(x), float(y), rel_tol=1e-6, abs_tol=1e-7) for x,y in zip(old,got))
print('FREQUENCY 2 full q<=99 engine reruns agree')
print('ALL CHECKS PASSED (cutoff correction identified, not silently accepted)')
