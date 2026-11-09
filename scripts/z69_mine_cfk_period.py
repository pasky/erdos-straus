# Period-length diagnostic for the hard-set CF deviations (diagnostic uniform-residue model, not a null model).
#  CFk / CFh divf: multiplicity of convergents k_i (resp. h_i), 0 <= i < L, divisible by the witness modulus f;
#    model multiplicity L/f.  Reported: raw ratio real/phantom, normalised rate ratio (obs/model real)/(obs/model ph)
#    with a prime-cluster delta-method 2-s.e. interval.
#  QS divxy: x or y (>= 5) divides some Q_i (first 4000 period positions); model |Qset| * sum 1/l.
import json, math, sys, gzip, collections
_L = {}; _Q = {}
def period(p):
    if p not in _L:
        a0 = math.isqrt(p); P, Q, a = 0, 1, a0; L = 0
        while True:
            P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; L += 1
            if Q == 1: break
        _L[p] = L
    return _L[p]
def qsize(p):
    if p not in _Q:
        a0 = math.isqrt(p); P, Q, a = 0, 1, a0; S = set(); n = 0
        while n < 4000:
            P = a * Q - P; Q = (p - P * P) // Q; a = (a0 + P) // Q; S.add(Q); n += 1
            if Q == 1: break
        _Q[p] = len(S)
    return _Q[p]
def ratio_ci(rows):
    """rows: per prime (oR, eR, oP, eP); ratio of normalised rates with cluster delta-method 2 s.e."""
    oR = sum(r[0] for r in rows); eR = sum(r[1] for r in rows); oP = sum(r[2] for r in rows); eP = sum(r[3] for r in rows)
    rR, rP = oR / eR, oP / eP; R = rR / rP
    # linearisation: d log R = (oR - rR eR)/oR - (oP - rP eP)/oP per prime
    v = sum(((r[0] - rR * r[1]) / oR - (r[2] - rP * r[3]) / oP) ** 2 for r in rows)
    return oR, oP, oR / oP, eR / eP, R, 2 * R * math.sqrt(v)
for fn in sys.argv[1:]:
    for key, model in (('CFk:divf', 'L'), ('CFh:divf', 'L'), ('QS:divxy', 'Q')):
        rows = collections.defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
        for l in gzip.open(fn, 'rt'):
            rec = json.loads(l)
            if rec['p'] < 10**4 or not rec['ph']: continue
            K = len(rec['ph']); f = rec['f']
            if model == 'L':
                mR = period(rec['p']) / f; mP = sum(period(ph['q']) / f for ph in rec['ph']) / K
            else:
                w = sum(1 / v for v in (rec['r'], rec['y']) if v >= 5)
                mR = qsize(rec['p']) * w; mP = sum(qsize(ph['q']) * w for ph in rec['ph']) / K
            r = rows[rec['p']]
            r[0] += rec['real'].get(key, 0); r[1] += mR
            r[2] += sum(ph['h'].get(key, 0) for ph in rec['ph']) / K; r[3] += mP
        oR, oP, raw, mod, R, ci = ratio_ci(list(rows.values()))
        print('%s %-9s multiplicity real %.0f / phantom %.0f = %.3f; model ratio %.3f; normalised rate ratio %.4f +- %.4f' % (
            fn.split('/')[-1], key, oR, oP, raw, mod, R, ci))
