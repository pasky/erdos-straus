"""RESIDUE_HARDNESS §1–2 (MSSD = mean squared standardized discrepancy over classes; descriptive: SEs treat the class
means as independent and ignore the error of the normalising mean, and classes of different Q overlap): class factors F_Q(r) = E[count | p ≡ r (mod Q)] / (mean over classes), model vs data.

Model (local-density sum, §1.3): for each certificate family the exact tuple count at every integer v of the window, each tuple
weighted by the prime local density of its AP (factor l/(l−1) for primes l > 13 dividing the AP modulus; 0 if the AP has no
units); averaged over 13-rough v ≡ 1 (mod 4) in the class r. The small primes l ≤ 13 are handled exactly by the roughness.
The model sample excludes the primes (13-rough composites only), so model and data share no noise.
Data: the same counts at the primes p ≡ 1 (mod 4) of the window (for primes the tuple counts are the solution counts:
TI = 2k1, TII = 2k2, U = (TI + TII)/2, RS = R (★); CERTIFIED against z52b/z52c_rh_count on all primes compared).
Inputs: /tmp/rh/{t2e5full,t2e6,t1e7}_{TI,TIw,TII,TIIw,RS}.f32 (scripts/z52c_rh_types.c) and /tmp/rh/s1e7_{R,RW} (z52c_rh_star.c).
Output: data/z52c/rh/model_tables.json and a printed table.
Usage: uv run --with numpy --with scipy python scripts/z52c_rh_model.py
"""
import numpy as np, json, os
from math import gcd
from scipy.special import digamma

T = '/tmp/rh/'
WINDOWS = [('1e5', 't2e5full', 101, 200000, 100000, 200000),
           ('1e6', 't2e6', 1000001, 2000000, 1000000, 2000000),
           ('5e6', 't1e7', 5000001, 10000000, 5000000, 10000000)]
QS = [3, 5, 7, 8, 11, 13, 16, 840]
HI = 10**7
R7 = np.fromfile(T + 's1e7_R.u16', np.uint16).astype(float)
RW7 = np.fromfile(T + 's1e7_RW.f32', np.float32).astype(float)
isp = np.ones(HI + 1, bool); isp[:2] = False
for i in range(2, int(HI**.5) + 1):
    if isp[i]: isp[i*i::i] = False


def star_formula(q, r, L):
    """First-order (★) factor for an odd prime q (§1.2): 1 + 2q/((q²+1)L)·(Ψ(r) − mean Ψ)."""
    def Psi(rr):
        c = (-pow(4*rr, -1, q)) % q; b = (-rr) % q
        return -digamma(c/q) - 2*digamma(b/q)
    mean = np.mean([Psi(x) for x in range(1, q)])
    return 1 + 2*q/((q*q + 1)*L)*(Psi(r) - mean)


def classes(Q):
    return [r for r in range(Q) if gcd(r, Q) == 1 and (r - 1) % gcd(Q, 4) == 0]


out = {}
for name, pre, lo, hi, wlo, whi in WINDOWS:
    if not os.path.exists(T + pre + '_TI.f32'):
        print('missing', pre); continue
    ar = {k: np.fromfile(T + f'{pre}_{k}.f32', np.float32).astype(float) for k in ['TI', 'TIw', 'TII', 'TIIw', 'RS']}
    v = np.arange(lo, hi + 1)
    fam = {'S': (ar['RS'], RW7[lo:hi+1]), 'I': (ar['TI'], ar['TIw']), 'II': (ar['TII'], ar['TIIw']),
           'U': ((ar['TI'] + ar['TII'])/2, (ar['TIw'] + ar['TIIw'])/2)}
    win = (v >= wlo) & (v <= whi) & (v % 4 == 1)
    rough = win & (v % 3 > 0) & (v % 5 > 0) & (v % 7 > 0) & (v % 11 > 0) & (v % 13 > 0)
    pr = win & isp[lo:hi+1]
    rough = rough & ~pr   # model sample = 13-rough COMPOSITES only: disjoint from the data (no shared noise)
    L = np.log(np.sqrt(wlo*whi))
    out[name] = {'L': L, 'n_primes': int(pr.sum()), 'n_rough': int(rough.sum())}
    for Q in QS:
        cl = classes(Q); res = {}
        for f, (plain, w) in fam.items():
            mws = [w[rough & (v % Q == r)] for r in cl]
            mw = np.array([x.mean() for x in mws]); mse = np.array([x.std()/np.sqrt(len(x)) for x in mws])
            mp = np.array([plain[rough & (v % Q == r)].mean() for r in cl])
            dd = [plain[pr & (v % Q == r)] for r in cl]
            md = np.array([x.mean() for x in dd]); se = np.array([x.std()/np.sqrt(len(x)) for x in dd])
            ml = np.array([np.log(x + 1).mean() for x in dd])
            res[f] = dict(model=(mw/mw.mean()).round(4).tolist(), model_se=(mse/mw.mean()).round(4).tolist(), model_plain=(mp/mp.mean()).round(4).tolist(),
                          data=(md/md.mean()).round(4).tolist(), data_se=(se/md.mean()).round(4).tolist(),
                          data_meanlog=(ml - ml.mean()).round(4).tolist(), n=[len(x) for x in dd])
            if f == 'S' and Q in (3, 5, 7, 11, 13):
                res[f]['formula'] = [round(star_formula(Q, r, L), 4) for r in cl]
        out[name][str(Q)] = dict(classes=cl, **res)
    # print a compact table
    print(f'=== window {name}: [{wlo},{whi}], primes p≡1(4): {pr.sum()}, 13-rough n≡1(4): {rough.sum()}, L={L:.2f}')
    for Q in [5, 7, 11, 13, 8, 16]:
        d = out[name][str(Q)]
        print(f' Q={Q}')
        for i, r in enumerate(d['classes']):
            sq = 'sq' if (Q in (8, 16) or pow(r, (Q-1)//2, Q) == 1) else '  '
            s = f'  r={r:2d} {sq} '
            for f in ['S', 'I', 'II', 'U']:
                s += f"| {f}: model {d[f]['model'][i]:.3f} data {d[f]['data'][i]:.3f}±{d[f]['data_se'][i]:.3f} "
            if 'formula' in d['S']: s += f"| S formula {d['S']['formula'][i]:.3f}"
            print(s)
    # agreement summary over all Q and classes
    for f in ['S', 'I', 'II', 'U']:
        dm = []; se = []
        for Q in QS:
            d = out[name][str(Q)][f]; dm += list(np.array(d['data']) - np.array(d['model']))
            se += list(np.hypot(d['data_se'], d['model_se']))
        dm = np.array(dm); se = np.array(se)
        d1 = []; se1 = []
        for Q in QS:
            d = out[name][str(Q)][f]; d1 += list(np.array(d['data']) - 1); se1 += d['data_se']
        d1 = np.array(d1); se1 = np.array(se1)
        print(f' {f}: classes {len(dm)}, rms(data−model) {np.sqrt((dm**2).mean()):.4f}, rms(SE data⊕model) {np.sqrt((se**2).mean()):.4f},'
              f' MSSD {((dm/se)**2).mean():.2f}; null F≡1: rms {np.sqrt((d1**2).mean()):.4f}, MSSD {((d1/se1)**2).mean():.1f}')
        # without the 96 thin mod-840 classes (R-review: they dominate the 136-class average)
        dmx = []; sex = []
        for Q in QS:
            if Q == 840: continue
            d = out[name][str(Q)][f]; dmx += list(np.array(d['data']) - np.array(d['model'])); sex += list(np.hypot(d['data_se'], d['model_se']))
        dmx = np.array(dmx); sex = np.array(sex)
        print(f'    {f} without Q = 840: classes {len(dmx)}, MSSD {((dmx/sex)**2).mean():.2f}')
        out[name]['summary_' + f + '_no840'] = dict(n=len(dmx), mssd=float(((dmx/sex)**2).mean()))
        out[name]['summary_' + f] = dict(rms_model=float(np.sqrt((dm**2).mean())), rms_se=float(np.sqrt((se**2).mean())),
                                         mssd_model=float(((dm/se)**2).mean()), mssd_null=float(((d1/se1)**2).mean()))
os.makedirs('data/z52c/rh', exist_ok=True)
json.dump(out, open('data/z52c/rh/model_tables.json', 'w'), indent=0)
