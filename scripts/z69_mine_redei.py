# Redei / 2-part class-number data and CF period of sqrt p: hard primes (H-low, p >= 1e4) vs controls.
import json, collections, math
tags = {int(l.split()[0]): l.split()[1] for l in open('data/z69/mine/H.txt')}
def v2(n): return (n & -n).bit_length() - 1
for fn, name in (('/tmp/z69mine/H.feat.jsonl', 'H'), ('/tmp/z69mine/C.feat.jsonl', 'C')):
    c = collections.Counter(); c8 = collections.Counter(); n = 0; Lr = []; hp = collections.Counter()
    for l in open(fn):
        F = json.loads(l)
        if F['p'] < 10**4: continue
        if name == 'H' and 'low' not in tags[F['p']]: continue
        n += 1; c[min(v2(F['hm4']), 5)] += 1; c8[min(v2(F['hm8']), 5)] += 1; hp[F['hp']] += 1
        Lr.append(F['L'] / math.sqrt(F['p']))
    Lr.sort()
    print(name, n, 'v2 h(-4p):', {k: round(v / n, 3) for k, v in sorted(c.items())}, ' v2 h(-8p):', {k: round(v / n, 3) for k, v in sorted(c8.items())},
          ' median CF period/sqrt p: %.2f' % Lr[len(Lr) // 2], ' h(p)=1: %.2f' % (hp[1] / n))
