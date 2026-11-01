# Z1739 analysis: star discrepancy of {(n+u)/(4uC-1)} over the trial set, by modulus range, primes vs controls;
# plus the exact-zero (ES/(★)) counts vs sum 1/m and sum 1/phi(m).  Discrepancy from the 2000-bin histogram (resolution 5e-4).
import numpy as np, gzip, glob, os
D = 'data/z52b/pass2/ZF1/Z1739'
rng_name = ['m<=n^1/2', 'n^1/2<m<=n^3/4', 'm>n^3/4']
def load(fn):
    rows = {}
    for l in gzip.open(fn, 'rt'):
        a = l.split(); n, k = int(a[0]), int(a[1])
        rows.setdefault(n, {})[k] = dict(N=int(a[2]), z=int(a[3]), s1=float(a[4]), sp=float(a[5]), mf=float(a[6]), h=np.array(a[7:], float))
    return rows
def dstar(h, ref=None):
    c = np.cumsum(h) / h.sum(); t = np.arange(1, len(h) + 1) / len(h)
    if ref is not None: t = np.cumsum(ref) / ref.sum()
    return np.abs(c - t).max()
for X in ('1e6', '1e7'):
    G = {tag: load(f'{D}/frac_{X}_{tag}.txt.gz') for tag in 'PHN'}
    print(f"=== n ~ {X}: P = 12 primes = 1 (4), H = 12 primes = 1 (840), N = 12 random composites = 1 (4)")
    for k in range(3):
        pooledN = sum(G['N'][n][k]['h'] for n in G['N'])
        line = f"  {rng_name[k]:16s}"
        for tag in 'PHN':
            ds = [dstar(G[tag][n][k]['h']) for n in G[tag]]
            dc = [dstar(G[tag][n][k]['h'], pooledN) for n in G[tag]]
            Ns = np.mean([G[tag][n][k]['N'] for n in G[tag]])
            mf = np.mean([G[tag][n][k]['mf'] for n in G[tag]])
            z = np.mean([G[tag][n][k]['z'] for n in G[tag]]); s1 = np.mean([G[tag][n][k]['s1'] for n in G[tag]]); sp = np.mean([G[tag][n][k]['sp'] for n in G[tag]])
            line += f" | {tag}: N={Ns:.3g} D*unif={np.mean(ds):.4f} D*vsCtrl={np.mean(dc):.4f} 1/sqrtN={1/np.sqrt(Ns):.1e} mean={mf:.4f} zeros={z:.1f} sum1/m={s1:.2f} sum1/phi={sp:.2f}"
        print(line)
