"""O154: dyadic stats of f_II/L^3 for p = 1 mod 24 and p = 1 mod 24*5*7*11*13 (=360360*... ) from /tmp/fII_1e8.bin,
for comparison with the single-p exact counts at 1e12..1e16 (logs/bs_adv_*.jsonl)."""
import numpy as np
A = np.fromfile('/tmp/fII_1e8.bin', dtype=np.uint32).reshape(-1, 3).astype(np.int64)
p, f = A[:, 0], A[:, 1].astype(float); L = np.log(p.astype(float)); r = f / L**3
k = np.floor(np.log2(p)).astype(int)
for name, m0 in (('p=1 mod 24', p % 24 == 1), ('p=1 mod 120120', p % 120120 == 1), ('all primes', p > 3)):
    print(name)
    for kk in (18, 20, 22, 24, 26):
        m = m0 & (k == kk)
        if m.sum() < 5: continue
        x = r[m]; print(f"  2^{kk}: n={m.sum():7d} mean {x.mean():.4f} CV {x.std()/x.mean():.3f} min {x.min():.4f} min/mean {x.min()/x.mean():.2f} q01/mean {np.quantile(x,0.01)/x.mean():.2f}")
