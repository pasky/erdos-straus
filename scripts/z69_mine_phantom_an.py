# Analyse z69_mine_phantom.py output: real vs phantom relation-hit rates, z-scores clustered by prime.
# Usage: python z69_mine_phantom_an.py <ph.jsonl> [min p]
import sys, json, collections, math
fn = sys.argv[1]; pmin = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 4
R = collections.Counter(); P = collections.Counter(); Ri = collections.Counter(); Pi = collections.Counter()
d = collections.defaultdict(lambda: collections.defaultdict(float))
nw = 0; nprime = set()
for l in open(fn):
    rec = json.loads(l)
    if rec['p'] < pmin or not rec['ph']: continue
    nw += 1; nprime.add(rec['p'])
    keys = set(rec['real']) | {k for ph in rec['ph'] for k in ph['h']}
    if any(ph['q'] >= 10 ** 12 for ph in rec['ph']):   # size-sensitive families not computed for huge phantoms
        keys = {k for k in keys if k.split(':')[0] not in ('CFq', 'QS', 'PELL', 'CFk', 'CFh')}
    K = len(rec['ph'])
    for k in keys:
        rv = rec['real'].get(k, 0); pv = sum(ph['h'].get(k, 0) for ph in rec['ph']) / K
        R[k] += rv; P[k] += pv
        Ri[k] += rv > 0; Pi[k] += sum(ph['h'].get(k, 0) > 0 for ph in rec['ph']) / K
        d[k][rec['p']] += (rv > 0) - sum(ph['h'].get(k, 0) > 0 for ph in rec['ph']) / K
print('file', fn, 'witnesses', nw, 'primes', len(nprime), 'p >=', pmin)
print('%-11s %8s %8s %9s %9s %7s' % ('fam:test', 'hitsR', 'hitsPh', 'witR', 'witPh', 'z'))
for k in sorted(R.keys() | P.keys()):
    s = sum(d[k].values()); v = sum(x * x for x in d[k].values())
    z = s / math.sqrt(v) if v > 0 else 0.0
    flag = '  <==' if abs(z) >= 4 else ''
    print('%-11s %8d %8.1f %9d %9.1f %+7.2f%s' % (k, R[k], P[k], Ri[k], Pi[k], z, flag))
