# Is the hard-set CFk/CFh excess (f divides some convergent of sqrt p) explained by the longer CF period of the real
# primes?  Compare observed multiplicities with the period-proportional expectation sum L/f (uniform-residue model).
import json, math, sys, gzip, collections
_L = {}
def period(p):
    if p not in _L:
        a0 = math.isqrt(p); P, Q, a = 0, 1, a0; L = 0
        while True:
            P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; L += 1
            if Q == 1: break
        _L[p] = L
    return _L[p]
for fn in sys.argv[1:]:
    obsR = obsP = expR = expP = 0.0; LR = []; LP = []
    for l in gzip.open(fn, 'rt'):
        rec = json.loads(l)
        if rec['p'] < 10**4 or not rec['ph']: continue
        f = rec['f']; K = len(rec['ph'])
        Lr = period(rec['p']); Lq = [period(ph['q']) for ph in rec['ph']]
        obsR += rec['real'].get('CFk:divf', 0); obsP += sum(ph['h'].get('CFk:divf', 0) for ph in rec['ph']) / K
        expR += Lr / f; expP += sum(L / f for L in Lq) / K
        LR.append(Lr / math.sqrt(rec['p'])); LP += [L / math.sqrt(q['q']) for L, q in zip(Lq, rec['ph'])]
    LR.sort(); LP.sort()
    print('%s: CFk divf multiplicity real %.0f vs phantom %.0f (ratio %.3f); period model sum L/f real %.0f vs phantom %.0f'
          ' (ratio %.3f); obs/model real %.3f phantom %.3f; median L/sqrt: real %.2f phantom %.2f' % (
          fn, obsR, obsP, obsR / obsP, expR, expP, expR / expP, obsR / expR, obsP / expP, LR[len(LR) // 2], LP[len(LP) // 2]))
# Same for QS divxy (x or y divides some Q_i): model multiplicity |Qset| * sum_{l in {x,y}, l >= 5} 1/l (Qset capped
# at the first 4000 period positions as in the dictionary).
_Q = {}
def qsize(p):
    if p not in _Q:
        a0 = math.isqrt(p); P, Q, a = 0, 1, a0; S = set(); n = 0
        while n < 4000:
            P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; S.add(Q); n += 1
            if Q == 1: break
        _Q[p] = len(S)
    return _Q[p]
for fn in sys.argv[1:]:
    obsR = obsP = expR = expP = 0.0
    for l in gzip.open(fn, 'rt'):
        rec = json.loads(l)
        if rec['p'] < 10**4 or not rec['ph']: continue
        K = len(rec['ph']); w = sum(1 / v for v in (rec['r'], rec['y']) if v >= 5)
        obsR += rec['real'].get('QS:divxy', 0); obsP += sum(ph['h'].get('QS:divxy', 0) for ph in rec['ph']) / K
        expR += qsize(rec['p']) * w; expP += sum(qsize(ph['q']) * w for ph in rec['ph']) / K
    print('%s: QS divxy multiplicity real %.0f vs phantom %.0f (ratio %.3f); model |Qset| sum 1/l real %.0f vs phantom %.0f'
          ' (ratio %.3f); obs/model real %.3f phantom %.3f' % (fn, obsR, obsP, obsR / obsP, expR, expP, expR / expP, obsR / expR, obsP / expP))
