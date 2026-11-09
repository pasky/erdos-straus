# Coverage of "least non-residue" rules: does p have a witness f divisible by n_p (least QNR), by nq7 (least prime
# q = 7 mod 8 with (p/q) = -1), or by some prime q <= Y with (p/q) = -1 (the inert-prime menu)?
import sys, json, collections
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit
from sympy import primerange
tags = {int(l.split()[0]): l.split()[1] for l in open('data/z69/mine/H.txt')}
for wf, ff, name in (('/tmp/z69mine/H.wit', '/tmp/z69mine/H.feat.jsonl', 'H'), ('/tmp/z69mine/C.wit', '/tmp/z69mine/C.feat.jsonl', 'C')):
    W = load_wit(wf); n = 0; c = collections.Counter()
    for l in open(ff):
        F = json.loads(l); p = F['p']
        if p < 10**4: continue
        n += 1; fs = [f for f, r, y, t in W[p]]
        c['f % np == 0'] += any(f % F['np'] == 0 for f in fs)
        c['f % nq7 == 0'] += any(f % F['nq7'] == 0 for f in fs)
        c['f == nq7'] += F['nq7'] in fs
        inert = [q for q in primerange(3, 60) if pow(p % q, (q - 1) // 2, q) == q - 1]
        c['f has inert prime <= 59'] += any(f % q == 0 for f in fs for q in inert)
        c['least inert prime divides some f'] += bool(inert) and any(f % inert[0] == 0 for f in fs)
    print(name, n, {k: '%.3f' % (v / n) for k, v in c.items()})
