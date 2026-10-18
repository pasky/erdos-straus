"""O262: per-m statistics of the Type II numerator-m lottery (counts from z32_ladder_run.py).
For each m: exceptions (count 0) and the largest one; per dyadic bin: #primes, mean, D = var/mean (within cells
p mod C, pooled), observed zeros, and NB-predicted zeros sum_cells n*D^(-mu/(D-1)) (cell mean mu, cell D),
plus the worst-cell safety ratio R = -log P0 / log p.  Cells: p mod C, C = lcm(840, 4m)."""
import sys, math, numpy as np
P = np.load('/tmp/z32/primes.npy').astype(np.int64)
ms = [int(t) for t in sys.argv[1].split(',')]
for m in ms:
    c = np.load(f'/tmp/z32/cnt_m{m}.npy').astype(np.int64)
    ok = (P > 3) & (m % P != 0); p, f = P[ok], c[ok]
    Z = p[f == 0]
    print(f'm={m}: #exc={len(Z)} largest={Z.max() if len(Z) else None} last5={list(Z[-5:])}')
    C = math.lcm(840, 4*m); cell = p % C
    for k in range(10, 27, 2):
        sel = (p >= 2**k) & (p < 2**(k+2))
        if not sel.any(): continue
        pp, ff, cc = p[sel], f[sel], cell[sel]
        L = np.log(pp.astype(float)); pred = 0.0; worstR = 1e9; Dl = []
        for r in np.unique(cc):
            s = cc == r; n = s.sum()
            if n < 20: continue
            mu = ff[s].mean(); var = ff[s].var(); D = max(var/mu, 1.0001) if mu > 0 else 1.0001
            Dl.append((D, n))
            if mu == 0: continue
            lp0 = -mu*math.log(D)/(D-1); pred += n*math.exp(lp0)
            worstR = min(worstR, -lp0/math.log(pp[s].mean()))
        Dm = sum(D*n for D, n in Dl)/max(1, sum(n for _, n in Dl))
        print(f'  [2^{k},2^{k+2}) n={sel.sum()} mean={ff.mean():.1f} mean/L^3={np.mean(ff/L**3):.4f} '
              f'cellD={Dm:.2f} zeros={int((ff==0).sum())} NBpred={pred:.2f} worstR={worstR:.2f} minf={ff.min()}')
