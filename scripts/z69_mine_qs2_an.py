# Analyse z69_mine_qs2.py: prime-weighted real-vs-decoy rates, cluster-by-prime z, strata.
# Usage: python z69_mine_qs2_an.py <qs2.jsonl> [pmin]
import sys, json, math, collections
fn = sys.argv[1]; pmin = int(sys.argv[2]) if len(sys.argv) > 2 else 0
KEYS = ['D', 'R', 'E', 'A']
recs = [json.loads(l) for l in open(fn)]
recs = [r for r in recs if r['p'] >= pmin and r['real']]
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
    print(' first-hit relative position: real median %.3f (n %d), decoy median %.3f (n %d); odd-index share real %.3f decoy %.3f' % (
        sorted(pr)[len(pr) // 2], len(pr), sorted(pdc)[len(pdc) // 2], len(pdc), sum(par_r) / len(par_r), sum(par_d) / len(par_d)))
# Injection power check: in a fraction phi of the primes, force ONE real letter with D = 0 to D = 1 ("one informative
# witness letter per hard prime") and recompute the cluster z of D.
import random
rng = random.Random(5)
for phi in (1.0, 0.5, 0.2):
    inj = []
    for rec in recs:
        rr = [list(row) for row in rec['real']]
        if rng.random() < phi:
            zero = [i for i, row in enumerate(rr) if not row[1]]
            if zero: rr[rng.choice(zero)][1] = True
        inj.append({'real': rr, 'dec': rec['dec'], 'sq': rec['sq'], 'L': rec['L'], 'p': rec['p']})
    n, a, b, z = pw(inj, key='D')
    print(' injection (one letter forced to divide a Q_i in %d%% of primes): real %.4f decoy %.4f z %+.2f' % (100 * phi, a, b, z))
