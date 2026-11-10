"""Bounded independent z69 MINE audit (stdlib only).
Run under ulimit -v 6000000 and timeout 300, via uv run python.
Args: extracted branch root, regenerated census, compiled direct checker.
No files modified. Raw dictionaries are audited, not independently regenerated.
"""
import collections
import gzip
import functools
import json
import math
from pathlib import Path
import statistics
import subprocess
import sys

root, census_path, checker = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
data = root / 'data/z69/mine'

def nums(path):
    return [int(s.split()[0]) for s in path.read_text().splitlines()
            if s.strip() and not s.startswith('#')]

@functools.lru_cache(maxsize=50000)
def isprime(n):
    assert n < 2**64
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0: continue
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def witnesses(path):
    out = {}
    with gzip.open(path, 'rt') as stream:
        for line in stream:
            t = line.split()
            if t[0] == 'W':
                p, count = map(int, t[1:]); out[p] = []
            else:
                f, r, y, z = map(int, t)
                assert f % 8 == 7 and 0 < r < f and r*y == f+1
                assert f*z-r == p and (-p)%f == r
                out[p].append((f, r, y, z))
    return out

H, C = nums(data/'H.txt'), nums(data/'CTRL.txt')
HW, CW = witnesses(data/'H_witnesses.txt.gz'), witnesses(data/'CTRL_witnesses.txt.gz')
counts = {}
cz = []
with census_path.open() as stream:
    for line in stream:
        t = line.split()
        if t[0] == 'P': counts[int(t[1])] = (int(t[2]), int(t[3]))
        if t[0] == 'CZERO': cz.append(int(t[1]))
assert all(isprime(p) for p in H+C)
assert len(counts) == 1439970 and all(w >= 1 for w, f in counts.values())
assert [p for p, (w, f) in counts.items() if w == 1] == [2521]
print('census', len(counts), 'W=1', [p for p, (w, _) in counts.items() if w == 1], 'CZERO', cz)
with gzip.open(data/'W_1e7.tsv.gz', 'rt') as stream:
    rows = [tuple(map(int, line.split())) for line in stream]
assert all(counts[p] == (w, f) for p, w, f in rows)
assert len(rows) == sum(p <= 10**7 for p in counts)
print('committed census <=1e7 agrees:', len(rows))

screens = {path.stem: nums(path) for path in (root/'data/z58/screens').glob('*.txt')}
small = list(range(1, 100001, 8))
hard = [2521, 3361, 9601, 14177, 21841, 66529, 76441, 225289,
        712321, 1095481, 1381969, 2031121, 3613009, 4149601, 45553561, 96049801]
req = {n: 1 for n in small+hard}
for ns in screens.values():
    for n in ns: req.setdefault(n, 0)
result = subprocess.run([checker], input=''.join(f'{n} {full}\n' for n, full in sorted(req.items())),
                        text=True, capture_output=True, check=True, timeout=240)
direct = {int(n): (int(w), int(f)) for n, w, f in map(str.split, result.stdout.splitlines())}
# Independent primality sieve for complete small subrange, plus direct zero classification.
prime = bytearray(b'\x01')*100001; prime[:2] = b'\x00\x00'
for q in range(2, math.isqrt(100000)+1):
    if prime[q]: prime[q*q::q] = b'\x00'*((100000-q*q)//q+1)
sp = [n for n in small if prime[n]]
assert all(direct[p] == counts[p] for p in sp+hard)
szeros = [n for n in small if direct[n][0] == 0 and math.isqrt(n)**2 != n]
assert szeros == cz
assert all(direct[n][0] == 0 for n in small if math.isqrt(n)**2 == n)
print('literal exhaustive scan: all', len(small), 'n=1 mod8 <=1e5;', len(sp), 'primes; zeros', szeros)
print('hard literal counts:', {p: direct[p] for p in hard})
for name, ns in screens.items():
    zeros = [n for n in ns if direct[n][0] == 0]
    assert zeros == (cz if name == 'composite_zeros_le8e6' else [])
    print('screen', name, 'size', len(ns), 'zeros', zeros)
    if name == 'r8_zeros_1e10': print('R8 first witnesses', [direct[n][1] for n in ns])

print('H size', len(H), 'control size', len(C), 'overlap', len(set(H)&set(C)))
print('H below1e4', [p for p in H if p < 10000], 'H above2e10', [p for p in H if p > 2*10**10])
print('H/C median p', statistics.median(H), statistics.median(C))
for stem in ['ph3_H', 'ph3_C', 'phm3_H', 'phm3_C', 'phxz3_C']:
    with gzip.open(data/f'raw_{stem}.jsonl.gz', 'rt') as stream:
        records = [json.loads(line) for line in stream if line.strip()]
    records = [r for r in records if r['p'] >= 10000]
    covered = [r for r in records if r['ph']]
    source = HW if stem.endswith('_H') else CW
    expected = sum(min(8 if stem=='ph3_H' else 4 if stem=='phm3_H' else 2 if stem=='phm3_C' else 3, len(ws))
                   for p, ws in source.items() if 10000 <= p <= 2*10**10)
    assert len(records) == expected
    qcounts = collections.Counter()
    sizes = []
    for r in records:
        p, f, x, y, z = (r[k] for k in ('p', 'f', 'r', 'y', 'z'))
        assert (f,x,y,z) in source[p]
        for ph in r['ph']:
            q = ph['q']; qcounts[q] += 1; sizes.append(q/p)
            assert q != p and q%8 == 1 and isprime(q)
            if stem.startswith('phxz'):
                assert (q-p)%(8*x*z) == 0 and abs(q-p)*2 <= p
                yq = y+(q-p)//(x*z); fq = x*yq-1
                assert 0 < x < fq and (-q)%fq == x and (fq+1)%x == 0
            else:
                assert (q-p)%(8*f) == 0 and (-q)%f == x
                if stem.startswith('ph3'): assert abs(q-p)*2 <= p
                else:
                    assert (q-p)%(840*f) == 0
                    for ell in (11,13,17,19,23):
                        assert pow(q%ell,(ell-1)//2,ell) == pow(p%ell,(ell-1)//2,ell)
    print(stem, 'sampled/covered/primes', len(records), len(covered), len({r['p'] for r in covered}),
          'q/p median', round(statistics.median(sizes),3), 'phantom occurrences/unique', sum(qcounts.values()),len(qcounts),
          'phantom in H/C occurrences', sum(v for q,v in qcounts.items() if q in set(H)|set(C)),
          'f>sqrt(p)',sum(r['f']>math.sqrt(r['p']) for r in covered),
          'f>10sqrt(p)',sum(r['f']>10*math.sqrt(r['p']) for r in covered))
    for fam, scale2 in [('G2',18), ('C2',13.5)]:
        # Cauchy-Schwarz bounds for every |alpha*a+beta*b|, |alpha|,|beta|<=3.
        impossible = [r for r in covered if r['f']**2 > scale2*r['p']]
        assert all(not r['real'].get(fam+':divf',0) for r in impossible)
        phhit = sum(any(ph['h'].get(fam+':divf',0) for ph in r['ph']) for r in impossible)
        print(' bound-impossible real', fam, len(impossible), 'phantom-positive records', phhit)
    robust = {'G1','G2','G3','G4','C1','C2','E1','E2','N37','CL','PELL'}
    for test in ('divf','divq','divxy','divz'):
        clusters = collections.defaultdict(lambda: [0.,0.])
        for r in covered:
            for fam in robust:
                if fam=='PELL' and max([r['p']]+[ph['q'] for ph in r['ph']]) >= (10**10 if stem.startswith('phm') else 10**12): continue
                key=f'{fam}:{test}'
                clusters[r['p']][0] += r['real'].get(key,0)>0
                clusters[r['p']][1] += sum(ph['h'].get(key,0)>0 for ph in r['ph'])/len(r['ph'])
        R=sum(v[0] for v in clusters.values()); P=sum(v[1] for v in clusters.values())
        if P:
            ratio=R/P; interval=2*math.sqrt(sum((r-ratio*p)**2 for r,p in clusters.values()))/P
            print(' pooled',test, f'{R}/{P}: {ratio:.3f} +- {interval:.3f}')
