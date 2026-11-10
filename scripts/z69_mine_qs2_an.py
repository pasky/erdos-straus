# Analyse z69_mine_qs2.py: prime-weighted real-vs-decoy rates, cluster-by-prime z, strata.
# Usage: python z69_mine_qs2_an.py <qs2.jsonl> [pmin]
import sys, json, math, collections
fn = sys.argv[1]; pmin = int(sys.argv[2]) if len(sys.argv) > 2 else 0
KEYS = ['D', 'R', 'E', 'A']
recs = [json.loads(l) for l in open(fn)]
recs = [r for r in recs if r['p'] >= pmin and r['real']]
# pairing: real[i] <-> dec[2i], dec[2i+1]; identity rates and the informative (non-identical) subset
nid = n_both = n_one = 0
for r in recs:
    for i, row in enumerate(r['real']):
        d1, d2 = r['dec'][2 * i][0], r['dec'][2 * i + 1][0]
        nid += 1; n_both += (d1 == row[0] and d2 == row[0]); n_one += ((d1 == row[0]) != (d2 == row[0]))
print('letters %d: both decoys identical to the letter %d (%.3f), one identical %d' % (nid, n_both, n_both / nid, n_one))
def informative(recs):
    out = []
    for r in recs:
        rr = []; dd = []
        for i, row in enumerate(r['real']):
            d1, d2 = r['dec'][2 * i], r['dec'][2 * i + 1]
            if d1[0] != row[0] and d2[0] != row[0]:
                rr.append(row); dd += [d1, d2]
        if rr: out.append({'p': r['p'], 'sq': r['sq'], 'L': r['L'], 'real': rr, 'dec': dd})
    return out
def pw(recs, sel=lambda row, rec: True, key='D'):
    """prime-weighted mean real, mean decoy, cluster z of per-prime differences"""
    idx = 1 + KEYS.index(key)
    d = []; mr = []; md = []
    for rec in recs:
        R = [row[idx] for row in rec['real'] if sel(row, rec)]
        Dd = [row[idx] for row in rec['dec'] if sel(row, rec)]
        if not R or not Dd: continue
        a = sum(R) / len(R); b = sum(Dd) / len(Dd)
        mr.append(a); md.append(b); d.append(a - b)
    n = len(d)
    if n < 3: return n, 0, 0, 0
    m = sum(d) / n; s = math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1))
    return n, sum(mr) / n, sum(md) / n, m / (s / math.sqrt(n)) if s > 0 else 0
print('file %s primes %d' % (fn, len(recs)))
inf = informative(recs)
print(' INFORMATIVE subset (both decoys differ from the letter): primes %d, letters %d' % (len(inf), sum(len(r['real']) for r in inf)))
for key in KEYS:
    n, a, b, z = pw(inf, key=key)
    # prime-weighted difference with 2 s.e.
    idx = 1 + KEYS.index(key); d = []
    for rec in inf:
        R = [row[idx] for row in rec['real']]; Dd = [row[idx] for row in rec['dec']]
        d.append(sum(R) / len(R) - sum(Dd) / len(Dd))
    m = sum(d) / len(d); se = math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1) / len(d))
    print('  %s  real %.5f decoy %.5f  diff %+.5f +- %.5f (2 s.e.)  z %+.2f' % (key, a, b, m, 2 * se, z))
print(' ALL letters (identical decoys contribute zero contrast):')
for key in KEYS:
    n, a, b, z = pw(recs, key=key)
    print('  %s  real %.5f decoy %.5f  ratio %.3f  z %+.2f  (primes %d)' % (key, a, b, a / b if b else float('nan'), z, n))
print(' strata for D (letter divides some Q_i):')
strata = [('l <= sqrt p', lambda row, rec: row[0] <= rec['sq']), ('l > sqrt p', lambda row, rec: row[0] > rec['sq']),
          ('l <= 100', lambda row, rec: row[0] <= 100), ('100 < l <= 1e4', lambda row, rec: 100 < row[0] <= 10**4),
          ('l > 1e4', lambda row, rec: row[0] > 10**4)]
for name, sel in strata:
    n, a, b, z = pw(recs, sel, 'D')
    print('  %-16s real %.4f decoy %.4f ratio %.3f z %+.2f (primes %d)' % (name, a, b, a / b if b else float('nan'), z, n))
Ls = sorted(r['L'] / r['sq'] for r in recs); t1, t2 = Ls[len(Ls) // 3], Ls[2 * len(Ls) // 3]
for name, lo, hi in (('L/sqrt p low', 0, t1), ('L/sqrt p mid', t1, t2), ('L/sqrt p high', t2, 1e9)):
    sub = [r for r in recs if lo <= r['L'] / r['sq'] < hi]
    n, a, b, z = pw(sub, key='D')
    print('  %-16s real %.4f decoy %.4f ratio %.3f z %+.2f (primes %d)' % (name, a, b, a / b if b else float('nan'), z, n))
# position / parity of the first hit
pr = [row[5] for rec in recs for row in rec['real'] if row[1]]; pdc = [row[5] for rec in recs for row in rec['dec'] if row[1]]
par_r = [row[6] for rec in recs for row in rec['real'] if row[1]]; par_d = [row[6] for rec in recs for row in rec['dec'] if row[1]]
if pr and pdc:
    print(' [descriptive, pooled over hit rows] first-hit relative position: real median %.3f (n %d), decoy median %.3f (n %d); odd-index share real %.3f decoy %.3f' % (
        sorted(pr)[len(pr) // 2], len(pr), sorted(pdc)[len(pdc) // 2], len(pdc), sum(par_r) / len(par_r), sum(par_d) / len(par_d)))
