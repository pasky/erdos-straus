"""Analysis of z52d_fourier_scan output: window types, real layer, inverse-lemma statistics (hard vs control)."""
import sys, json, gzip
from collections import Counter, defaultdict
P = json.load(open('../data/z52d/fourier/primes.json'))
hard = set(P['hard']); star = set(P['star'])
op = gzip.open if sys.argv[1].endswith('.gz') else open
R = [json.loads(l) for l in op(sys.argv[1], 'rt')]
grp = lambda r: 'hard' if r['p'] in hard else 'ctrl'
print('windows', len(R), 'primes', len({r['p'] for r in R}))
# 1. types
T = Counter((grp(r), r['forced'], r['type']) for r in R)
for g in ('hard', 'ctrl'):
    n = len({r['p'] for r in R if grp(r) == g})
    print(g, n, 'primes; per prime:', {f"{'F' if f else 'U'}-{t}": round(T[(g, f, t)] / n, 1)
                                       for f in (True, False) for t in ('ok', 'sub', 'pov')})
# 2. real layer
bad = [r for r in R if r['type'] == 'sub' and r['kill_jac'] and r['forced']]
print('THEOREM CHECK kill_jac at forced windows (must be 0):', len(bad))
badp = [r for r in R if r['type'] == 'sub' and r['forced'] and r['prime_e']]
print('THEOREM CHECK subgroup-type at forced PRIME windows (must be 0):', len(badp))
sgn = [r for r in R if r['type'] != 'ok' and ((r['c_jac'] < 0) != r['forced'])]
print('THEOREM CHECK sign c(chi_-e) = -(e/p) (must be 0 violations):', len(sgn))
for g in ('hard', 'ctrl'):
    n = len({r['p'] for r in R if grp(r) == g})
    S = [r for r in R if grp(r) == g and r['type'] == 'sub']
    c = Counter(('F' if r['forced'] else 'U') + ':' + ('jac' if r['kill_jac'] else 'realother' if r['kill_real'] else
                                                       f"nonreal") for r in S)
    print(g, 'sub-type kill classes per prime', {k: round(v / n, 2) for k, v in sorted(c.items())})
    mo = Counter(r['kill_min_order'] for r in S if not r['kill_real'])
    print('   nonreal-only kill min orders', sorted(mo.items()))
# 3. inverse lemma
print('\nInverse lemma L(B,eta) on obstructed windows with H = G (full generated subgroup):')
for g in ('hard', 'ctrl'):
    for forced in (True, False):
        W = [r for r in R if grp(r) == g and r['type'] != 'ok' and r['Hfull'] and r['forced'] == forced]
        if not W: continue
        line = f"{g} {'forced' if forced else 'unforced'} n={len(W)}:"
        for B in (2, 4, 6, 12, 24):
            for eta in (0.1, 0.2):
                a = sum(1 for r in W if (r[f'mx{B}'] or -1) >= eta) / len(W)
                o = sum(1 for r in W if (r[f'mxo{B}'] or -1) >= eta) / len(W)
                line += f" B{B}/η{eta}: {a:.2f}|{o:.2f}"
        cm = sum(1 for r in W if r['cmax'] >= 0.2) / len(W)
        co = sum(1 for r in W if r['cmax_odd_val'] >= 0.2) / len(W)
        line += f"  ANYorder η0.2: {cm:.2f}|{co:.2f}"
        print(line)
    # dependence on M
    W = [r for r in R if grp(r) == g and r['type'] != 'ok' and r['Hfull']]
    byM = defaultdict(list)
    for r in W:
        byM[min(r['M'], 243)].append(r)
    print(g, 'by box size M (all|odd, B=12, η=0.1; any-order max c median):')
    for M in sorted(byM):
        L = byM[M]
        if len(L) < 20: continue
        a = sum(1 for r in L if (r['mx12'] or -1) >= 0.1) / len(L)
        o = sum(1 for r in L if (r['mxo12'] or -1) >= 0.1) / len(L)
        med = sorted(r['cmax'] for r in L)[len(L) // 2]
        print(f"   M={M} n={len(L)} L12: {a:.2f}|{o:.2f} median cmax {med:.3f}")
