"""RESIDUE_HARDNESS §3: split the model class factor mod q0 = 7 (window [1e6, 2e6]) into the 'pair term' (tuples whose AP
modulus 4ab resp. 4ad is divisible by 7: the AP is constant mod 7) and the 'level term' (all other tuples).
Input /tmp/rh/q7e6_* from `z52c_rh_types 1000001 2000000 /tmp/rh/q7e6 7`.  F_r = pair_r/mean_total + level_r/mean_total."""
import numpy as np, json
lo, hi = 1000001, 2000000; v = np.arange(lo, hi + 1)
A = {k: np.fromfile(f'/tmp/rh/q7e6_{k}.f32', np.float32).astype(float) for k in ['TIw', 'TIIw', 'TIwq', 'TIIwq']}
isp = np.ones(hi + 1, bool); isp[:2] = False
for i in range(2, int(hi**.5) + 1):
    if isp[i]: isp[i*i::i] = False
rough = (v % 4 == 1) & (v % 3 > 0) & (v % 5 > 0) & (v % 7 > 0) & (v % 11 > 0) & (v % 13 > 0) & ~isp[lo:]
out = {}
for fam, tot, pq in [('I', 'TIw', 'TIwq'), ('II', 'TIIw', 'TIIwq'), ('U', None, None)]:
    if fam == 'U': T = (A['TIw'] + A['TIIw'])/2; Pq = (A['TIwq'] + A['TIIwq'])/2
    else: T = A[tot]; Pq = A[pq]
    mt = np.mean([T[rough & (v % 7 == r)].mean() for r in range(1, 7)])
    rows = {r: dict(pair=round(Pq[rough & (v % 7 == r)].mean()/mt, 4), level=round((T - Pq)[rough & (v % 7 == r)].mean()/mt, 4)) for r in range(1, 7)}
    out[fam] = rows
    print(fam, ' '.join(f"r={r}: pair {x['pair']:.3f} level {x['level']:.3f} total {x['pair']+x['level']:.3f} |" for r, x in rows.items()))
json.dump(out, open('data/z52c/rh/decomp_q7.json', 'w'), indent=1)
