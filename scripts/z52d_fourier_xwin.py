"""Cross-window test (b): is one character shared by the obstructed windows of a prime?
(1) Dirichlet sense: primitive ψ (fixed conductor f ≤ FMAX), induced to every window e ≡ 0 (mod f).
    hit(ψ) = #obstructed windows where ψ carries c ≥ ETA; opp(ψ) = #obstructed windows with f | e.
    Per prime: best share max_ψ hit/opp over ψ with opp ≥ 8 (non-BM), and best coverage max_ψ hit / #obstructed.
(2) BM family χ_{-e} (one character χ_p via the transfer lemma): share of obstructed windows with c(χ_{-e}) ≥ ETA,
    and coverage of FORCED obstructed windows (must be 0 by Lemma T/Cor 4).
Compare hard vs controls (Mann–Whitney style rank comparison by mean rank)."""
import sys, json, gzip
from collections import defaultdict, Counter
from fractions import Fraction
from math import prod
ETA = float(sys.argv[2]) if len(sys.argv) > 2 else 0.15
FMAX = 200
P = json.load(open('../data/z52d/fourier/primes.json'))
hard = set(P['hard'])
op = gzip.open if sys.argv[1].endswith('.gz') else open
by = defaultdict(list)
for l in op(sys.argv[1], 'rt'):
    r = json.loads(l)
    if r['type'] != 'ok':
        by[r['p']].append(r)
def cond(pid):
    f = 1
    for l, fr in pid:
        d = Fraction(fr).denominator; c = 1
        while d % l == 0: d //= l; c += 1
        f *= l ** c
    return f
stats = {}
for p, W in by.items():
    for scope in ('all', 'forced'):
        WW = [r for r in W if scope == 'all' or r['forced']]
        hit = Counter(); opp = Counter()
        conds = set()
        for r in WW:
            for pid, order, odd, c, isjac in r['top']:
                if isjac or c < ETA: continue
                key = tuple((l, fr) for l, fr in pid)
                if cond(key) <= FMAX: hit[key] += 1
        for key in hit:
            f = cond(key)
            opp[key] = sum(1 for r in WW if r['e'] % f == 0)
        best_share = max([hit[k] / opp[k] for k in hit if opp[k] >= 8] or [0])
        best_cov = max([hit[k] / len(WW) for k in hit] or [0])
        bk = max(hit, key=lambda k: hit[k]) if hit else None
        bm = sum(1 for r in WW if r['c_jac'] >= ETA) / max(1, len(WW))
        stats[(p, scope)] = (best_share, best_cov, bm, len(WW), bk, hit[bk] if bk else 0, opp[bk] if bk else 0)
for scope in ('all', 'forced'):
    print(f'--- scope {scope}, ETA {ETA}')
    for g in ('hard', 'ctrl'):
        S = [v for (p, s), v in stats.items() if s == scope and ((p in hard) == (g == 'hard'))]
        n = len(S)
        mean = lambda i: sum(v[i] for v in S) / n
        print(f'{g:5s} n={n} mean best_share={mean(0):.3f} mean best_cov={mean(1):.3f} BM share={mean(2):.3f} '
              f'mean #obstructed={mean(3):.1f}  max best_cov={max(v[1] for v in S):.3f}')
    # rank comparison of best_cov
    allv = sorted(((v[1], p in hard) for (p, s), v in stats.items() if s == scope))
    ranks = [i for i, (x, h) in enumerate(allv) if h]
    print('   mean rank of hard primes in best_cov (uniform expectation %.1f): %.1f' % ((len(allv) - 1) / 2, sum(ranks) / len(ranks)))
for p in sorted(hard)[:30]:
    v = stats[(p, 'forced')]
    print(p, 'forced: best ψ', v[4], f'hit {v[5]}/{v[6]} (of {v[3]} forced obstructed)', 'BM share', round(v[2], 3))
