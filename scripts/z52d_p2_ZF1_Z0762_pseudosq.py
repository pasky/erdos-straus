"""Z0762 (ZF1 finisher): R, Uv, I3, W and U at all 20 pseudosquares (OEIS A002189) ≤ 10¹⁰ vs class-matched controls.
Word columns (W, I3, R, Uv): n ≤ 1e8 from the census binary (scripts/z52d_p2_TO3_census_bin.c output, /tmp/z52/big/
words1e8.bin, NOT in repo); n > 1e8 from scripts/z52d_p2_ZF1_words1.c (single-n, verified equal to the census at 5 n).
Controls for words: the 100 nearest non-square n ≡ P (mod 840) (n ≤ 1e8) or the 100 nearest primes ≡ P (840)
(n > 1e8; file data/z52b/pass2/ZF1/Z0762/words_big.txt).
U(n): primes via scripts/z52d_p2_ZF1_fastU.c, composites via scripts/z52b_fingerprint_count.c / z52d_p2_ZF1_segcount.c;
controls = primes ≡ P (mod 840) near P (U of primes; composite P compared with composite controls separately).
Run: uv run --with numpy python scripts/z52d_p2_ZF1_Z0762_pseudosq.py
"""
import numpy as np, json, os, math, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data/z52b/pass2/ZF1/Z0762')
PS = [73, 241, 1009, 2641, 8089, 18001, 53881, 87481, 117049, 515761, 1083289, 3206641, 3818929, 9257329, 22000801,
      48473881, 175244281, 427733329, 898716289, 2805544681]
COMPOSITE = {2641: '19·139', 18001: '47·383', 117049: '67·1747', 3206641: '643·4987', 2805544681: '127·859·25717'}
out = {'pseudosquares': PS}
# ---- words ----
W = None
if os.path.exists('/tmp/z52/big/words1e8.bin'):
    W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(10**8 + 1, 7))
big = {}
for line in open(os.path.join(D, 'words_big.txt')):
    t = line.split(); n = int(t[0]); big[n] = {k: int(v) for k, v in (x.split('=') for x in t[1:])}
cols = ['W', 'I3', 'R', 'Uv']
wres = {}
for P in PS:
    L2 = math.log(P) ** 2
    if P <= 10**8:
        # the 100 nearest non-square n ≡ P (mod 840), n ≠ P (at most ±5% when P is large)
        k = np.arange(-200, 201); ns = P + 840 * k; ns = ns[(ns > 1) & (ns <= 10**8) & (ns != P)]
        r = np.floor(np.sqrt(ns)).astype(np.int64); ns = ns[r * r != ns]
        ns = ns[np.argsort(np.abs(ns - P))][:100]; ns = ns[np.abs(ns / P - 1) < 0.05] if P > 2 * 10**6 else ns
        vals = {c: np.asarray(W[ns, i]).astype(float) for i, c in enumerate(cols)}
        mine = {c: float(W[P, i]) for i, c in enumerate(cols)}
        ctl = '100 nearest non-square n ≡ P (840)'
    else:
        ctrl = [n for n in big if n != P and n % 840 == P % 840 and abs(n / P - 1) < 0.05]
        vals = {c: np.array([big[n][c] for n in ctrl], float) for c in cols}
        mine = {c: float(big[P][c]) for c in cols}
        ns = np.array(ctrl); ctl = 'nearest primes ≡ P (840)'
    wres[str(P)] = dict(composite=COMPOSITE.get(P), n_ctrl=int(len(ns)), ctrl=ctl,
                        **{c: int(mine[c]) for c in cols},
                        **{f'{c}_pct': round(float((vals[c] < mine[c]).mean() + 0.5 * (vals[c] == mine[c]).mean()), 3) for c in cols},
                        **{f'{c}_ctrl_median': float(np.median(vals[c])) for c in cols})
out['words'] = wres
# ---- U ----
U = {}
def readU(fn, col=1):
    if not os.path.exists(fn): return
    for line in open(fn):
        t = line.split()
        if len(t) > col: U[int(t[0])] = int(t[col])
for fn in ('U_controls.txt',): readU(os.path.join(D, fn))
ures = {}
for P in PS:
    if P not in U: continue
    ctrl = sorted([n for n in U if n != P and n % 840 == P % 840 and n not in COMPOSITE], key=lambda n: abs(n - P))[:40]
    ctrl = [n for n in ctrl if abs(n / P - 1) < 0.5]
    v = np.array([U[n] for n in ctrl], float)
    l3 = math.log(P) ** 3
    ures[str(P)] = dict(U=U[P], U_over_log3=round(U[P] / l3, 4), composite=COMPOSITE.get(P), n_prime_ctrl=len(ctrl),
                        pct_vs_prime_ctrl=round(float((v < U[P]).mean()), 3) if len(v) else None,
                        ctrl_median=float(np.median(v)) if len(v) else None)
out['U'] = ures
# summary: prime pseudosquares only
pp = [P for P in PS if P not in COMPOSITE and P >= 1009]
out['summary'] = dict(
    prime_ps_R_pct=[wres[str(P)]['R_pct'] for P in pp], prime_ps_Uv_pct=[wres[str(P)]['Uv_pct'] for P in pp],
    prime_ps_I3_pct=[wres[str(P)]['I3_pct'] for P in pp],
    prime_ps_U_pct=[ures[str(P)]['pct_vs_prime_ctrl'] for P in pp if str(P) in ures],
    mean_R_pct=float(np.mean([wres[str(P)]['R_pct'] for P in pp])), mean_Uv_pct=float(np.mean([wres[str(P)]['Uv_pct'] for P in pp])),
    mean_I3_pct=float(np.mean([wres[str(P)]['I3_pct'] for P in pp])),
    mean_U_pct=float(np.mean([ures[str(P)]['pct_vs_prime_ctrl'] for P in pp if str(P) in ures and ures[str(P)]['pct_vs_prime_ctrl'] is not None])))
json.dump(out, open(os.path.join(D, 'pseudosq.json'), 'w'), indent=1)
print(json.dumps(out['summary'], indent=1))
for P in PS:
    w = wres[str(P)]; u = ures.get(str(P), {})
    print(P, COMPOSITE.get(P, ''), 'R', w['R'], w['R_pct'], 'Uv', w['Uv'], w['Uv_pct'], 'I3', w['I3'], w['I3_pct'], 'U', u.get('U'), u.get('pct_vs_prime_ctrl'), u.get('U_over_log3'))
