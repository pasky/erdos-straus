# Analyse z69_mine_phantom.py output: real vs phantom relation-hit rates, z-scores clustered by prime.
# Usage: python z69_mine_phantom_an.py <ph.jsonl> [--pmin N] [--big B] [--did other.jsonl]
#  * per test key: total multiplicities (hitsR / hitsPh, phantom averaged), per-witness indicators (witR / witPh),
#    and the cluster score z = sum_p d_p / sqrt(sum_p d_p^2), d_p = sum over retained witnesses of p of
#    (1[real hit] - mean_phantoms 1[phantom hit])  (independent prime clusters, null-centred; Gaussian calibration is
#    unreliable for very sparse keys — 'disc' = number of primes with d_p != 0 is printed).
#  * coverage: fraction of sampled witnesses that received >= 1 phantom, by f/p scale; size ratio q/p.
#  * pooled ratio over the size-robust families with a cluster (delta-method) 2-s.e. interval.
#  * --did: difference-in-differences against another run (e.g. hard set vs controls under the same design).
import sys, json, collections, math, argparse
ap = argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--pmin', type=int, default=10 ** 4)
ap.add_argument('--big', type=float, default=1e12); ap.add_argument('--did', default=None)
a = ap.parse_args()
ROBUST = ('G1', 'G2', 'G3', 'G4', 'C1', 'C2', 'E1', 'E2', 'N37', 'CL', 'PELL')
SENS = ('CFq', 'QS', 'PELL', 'CFk', 'CFh', 'CFpA')

def load(fn):
    recs = []; cov = collections.Counter(); tot = collections.Counter(); ratios = []; ps = []
    for l in open(fn):
        rec = json.loads(l)
        if rec['p'] < a.pmin: continue
        fp = rec['f'] / rec['p']
        b = '<1e-3' if fp < 1e-3 else '<1e-2' if fp < 1e-2 else '<1/16' if fp < 1 / 16 else '>=1/16'
        tot[b] += 1
        if not rec['ph']: continue
        cov[b] += 1; ps.append(rec['p'])
        ratios += [ph['q'] / rec['p'] for ph in rec['ph']]
        recs.append(rec)
    return recs, cov, tot, ratios, ps

def available(rec, fam):
    """a family is measured in a record unless it is size-sensitive and the real prime or a phantom is >= --big
    (then CF/Pell data were not computed for that prime); applied symmetrically to real and phantoms"""
    if fam not in SENS: return True
    return rec['p'] < a.big and all(ph['q'] < a.big for ph in rec['ph'])

def per_prime(recs, universe=None):
    """D[key][p] = [sum real indicators, sum mean-phantom indicators, exposure (#records where key measurable)]
    over the covered sampled witnesses of p (record-weighted: every covered witness record counts once)."""
    if universe is None:
        universe = set()
        for rec in recs:
            universe |= set(rec['real']) | {k for ph in rec['ph'] for k in ph['h']}
    D = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0.0, 0]))
    M = collections.defaultdict(lambda: [0.0, 0.0])
    for rec in recs:
        K = len(rec['ph'])
        for k in universe:
            if not available(rec, k.split(':')[0]): continue
            rv = rec['real'].get(k, 0); pv = sum(ph['h'].get(k, 0) for ph in rec['ph']) / K
            M[k][0] += rv; M[k][1] += pv
            e = D[k][rec['p']]
            e[0] += rv > 0; e[1] += sum(ph['h'].get(k, 0) > 0 for ph in rec['ph']) / K; e[2] += 1
    return D, M, universe

recs, cov, tot, ratios, ps = load(a.file)
D, M, U = per_prime(recs)
nw = collections.Counter(rec['p'] for rec in recs)
ratios.sort()
print('file %s  p >= %d  sampled witnesses %d, with phantoms %d (%d primes, p in [%d, %d])' % (
    a.file, a.pmin, sum(tot.values()), len(recs), len(nw), min(ps), max(ps)))
print('phantom coverage by f/p:', {b: '%d/%d' % (cov[b], tot[b]) for b in ('<1e-3', '<1e-2', '<1/16', '>=1/16')},
      ' q/p: median %.3g, range [%.3g, %.3g]' % (ratios[len(ratios) // 2], ratios[0], ratios[-1]))
print('%-12s %9s %10s %7s %8s %7s %5s %6s' % ('fam:test', 'hitsR', 'hitsPh', 'witR', 'witPh', 'z', 'disc', 'expo'))
for k in sorted(D):
    dd = [r - ph for r, ph, e in D[k].values()]
    s = sum(dd); v = sum(x * x for x in dd); disc = sum(1 for x in dd if abs(x) > 1e-12)
    z = s / math.sqrt(v) if v > 0 else 0.0
    R = sum(v[0] for v in D[k].values()); P = sum(v[1] for v in D[k].values()); X = sum(v[2] for v in D[k].values())
    if R == 0 and P == 0: continue
    print('%-12s %9d %10.1f %7d %8.1f %+7.2f %5d %6d%s' % (k, M[k][0], M[k][1], R, P, z, disc, X, '  <==' if abs(z) >= 4 else ''))
print('pooled over size-robust families %s (per-witness indicators, cluster delta-method 2 s.e.):' % (ROBUST,))
for te in ('divf', 'divq', 'divxy', 'divz'):
    keys = [k for k in D if k.split(':')[0] in ROBUST and k.split(':')[1] == te]
    if not keys: continue
    Rp = collections.Counter(); Pp = collections.Counter()
    for k in keys:
        for p, (r, ph, e) in D[k].items(): Rp[p] += r; Pp[p] += ph
    R = sum(Rp.values()); P = sum(Pp.values())
    if P == 0: continue
    ratio = R / P
    se = math.sqrt(sum((Rp[p] - ratio * Pp[p]) ** 2 for p in set(Rp) | set(Pp))) / P
    print('   %-6s real %8.1f phantom %8.1f ratio %.3f +- %.3f' % (te, R, P, ratio, 2 * se))
if a.did:
    recs2, *_ = load(a.did)
    D2, M2, U2 = per_prime(recs2, U)
    print('difference-in-differences vs %s: per-measured-record (real - phantom) indicator rate, this file minus other;'
          ' exposures = records where the key is measurable; cluster (ratio-estimator) s.e.' % a.did)
    for k in sorted(set(D) & set(D2)):
        out = []
        for DD in (D, D2):
            X = sum(v[2] for v in DD[k].values())
            if X == 0: out.append((0.0, 0.0, 0)); continue
            m = sum(v[0] - v[1] for v in DD[k].values()) / X
            var = sum((v[0] - v[1] - m * v[2]) ** 2 for v in DD[k].values()) / X ** 2
            out.append((m, var, X))
        if out[0][2] == 0 or out[1][2] == 0: continue
        diff = out[0][0] - out[1][0]; se = math.sqrt(out[0][1] + out[1][1])
        z = diff / se if se > 0 else 0.0
        print('   %-12s H %+.4f (n=%d)  C %+.4f (n=%d)  diff %+.4f  z %+.2f%s' % (
            k, out[0][0], out[0][2], out[1][0], out[1][2], diff, z, '  <==' if abs(z) >= 4 else ''))
