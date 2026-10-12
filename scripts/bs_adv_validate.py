"""O154: validate scripts/bs_adv_count.c (single-p exact f_II) against the full-range dump /tmp/fII_1e8.bin
(scripts/bs_prob_fII.c), random primes and random split parameters E."""
import numpy as np, subprocess, random
A = np.fromfile('/tmp/fII_1e8.bin', dtype=np.uint32).reshape(-1, 3)
random.seed(154)
idx = random.sample(range(len(A)), 400)
bad = 0
for i in idx:
    p, f = int(A[i, 0]), int(A[i, 1])
    E = random.choice([3, 50, 1000, int(2*p**0.5), p // 3])
    out = subprocess.run(['/tmp/bs_adv_count', str(p), str(max(E, 3))], capture_output=True, text=True).stdout.split()
    if int(out[1]) != f:
        bad += 1; print('MISMATCH', p, E, f, out[:4])
print('checked', len(idx), 'mismatches', bad)
