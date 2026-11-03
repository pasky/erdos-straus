# z55 CROSSU (v2 after hostile review): pair statistics of the firing set against a DESCRIPTIVE genus-weighted null.
# For each n (dump file named <n>.txt, lines "u w d j isq"): hits H = {(u,d): j = 1}; genus points Gp = {(u,d): j in
# squares mod u}. Null: |H| DISTINCT points of Gp drawn sequentially without replacement with probability proportional
# to the genus weight q_u^{-1} = 2^{omega(u)}/phi(u) (the G-prediction of a hit), REP independent draws per n.  This is a
# descriptive benchmark (it is not the exact conditional law of the independent-genus-Bernoulli model). Statistics over
# unordered pairs with u1 != u2: gcd(u1,u2) > 1, gcd(d1,d2) > 1, |u1-u2| <= U1/20 (U1 = window endpoint from the
# standard window of n), u1 | u2 or u2 | u1.  Uncertainty: bootstrap over primes (BOOT resamples of the prime list).
# Usage: python scripts/z55_crossu_pairs.py DUMPDIR [REP] [BOOT]
import sys, os, math, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z55_crossu_run import window
D = sys.argv[1]; REP = int(sys.argv[2]) if len(sys.argv) > 2 else 20; BOOT = int(sys.argv[3]) if len(sys.argv) > 3 else 200
random.seed(1)
KEYS = ['gu', 'gd', 'near', 'div']
def omega_phi(u):
    k = 0; ph = 1; t = u; q = 3
    while q * q <= t:
        if t % q == 0: k += 1; ph *= q - 1; t //= q
        q += 2
    if t > 1: k += 1; ph *= t - 1
    return k, ph
def pair_counts(pts, U1):
    c = dict(n=0, gu=0, gd=0, near=0, div=0)
    for (u1, d1), (u2, d2) in itertools.combinations(pts, 2):
        if u1 == u2: continue
        c['n'] += 1; c['gu'] += math.gcd(u1, u2) > 1; c['gd'] += math.gcd(d1, d2) > 1
        c['near'] += abs(u1 - u2) <= U1 / 20; c['div'] += (u1 % u2 == 0 or u2 % u1 == 0)
    return c
def wsample(items, wts, k):
    items = list(items); wts = list(wts); out = []
    for _ in range(min(k, len(items))):
        i = random.choices(range(len(items)), weights=wts, k=1)[0]
        out.append(items[i]); items.pop(i); wts.pop(i)
    return out
per = []  # per prime: (counts_H, counts_N averaged over REP, nhits, sum u hits, sum u null)
for fn in sorted(os.listdir(D)):
    n = int(fn.split('.')[0])
    pts = [tuple(map(int, l.split())) for l in open(os.path.join(D, fn))]
    if not pts: continue
    U0, U1, Y, X = window(n)
    H = [(u, d) for u, w, d, j, s in pts if j == 1]
    Gp = [(u, d) for u, w, d, j, s in pts if s == 1]
    wts = [(1 << omega_phi(u)[0]) / omega_phi(u)[1] for u, d in Gp]
    cH = pair_counts(H, U1)
    cN = dict(n=0.0, gu=0.0, gd=0.0, near=0.0, div=0.0); suN = 0.0
    if len(H) >= 1 and Gp:
        for r in range(REP):
            N = wsample(Gp, wts, len(H)); suN += sum(u for u, d in N) / REP
            c = pair_counts(N, U1)
            for k in cN: cN[k] += c[k] / REP
    per.append((cH, cN, len(H), sum(u for u, d in H), suN))
def summarize(idx):
    tot = {'H': dict(n=0, gu=0, gd=0, near=0, div=0), 'N': dict(n=0.0, gu=0.0, gd=0.0, near=0.0, div=0.0)}
    for i in idx:
        for k in tot['H']: tot['H'][k] += per[i][0][k]; tot['N'][k] += per[i][1][k]
    return {s: {k: tot[s][k] / tot[s]['n'] if tot[s]['n'] else float('nan') for k in KEYS} for s in tot}
full = summarize(range(len(per)))
nh = sum(p[2] for p in per)
print(f"files={len(per)} hits={nh} mean_u(hits)={sum(p[3] for p in per)/nh:.1f} mean_u(null)={sum(p[4] for p in per)/nh:.1f} pairs_H={sum(p[0]['n'] for p in per)} pairs_N={sum(p[1]['n'] for p in per):.0f}")
boots = {k: [] for k in KEYS}
for b in range(BOOT):
    idx = [random.randrange(len(per)) for _ in range(len(per))]
    s = summarize(idx)
    for k in KEYS: boots[k].append(s['H'][k] - s['N'][k])
for k, name in zip(KEYS, ['gcd(u1,u2)>1', 'gcd(d1,d2)>1', '|u1-u2|<=U1/20', 'u|u\'']):
    bs = sorted(boots[k]); lo, hi = bs[int(0.025 * BOOT)], bs[int(0.975 * BOOT) - 1]
    print(f"{name:16s} hits {100*full['H'][k]:6.2f}%  null {100*full['N'][k]:6.2f}%  diff {100*(full['H'][k]-full['N'][k]):+6.2f}%  bootstrap 95% CI of diff [{100*lo:+.2f}%, {100*hi:+.2f}%]")
