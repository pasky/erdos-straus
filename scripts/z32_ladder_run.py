"""O262: run z32_ladder for numerators m (Type II model of m/p) to X, keep counts on primes only.
Writes /tmp/z32/primes.npy (once) and /tmp/z32/cnt_m{m}.npy (uint32 counts at primes, aligned with primes.npy)."""
import sys, os, subprocess, numpy as np
X = int(float(sys.argv[1])); ms = [int(t) for t in sys.argv[2].split(',')]
pf = '/tmp/z32/primes.npy'
if not os.path.exists(pf):
    s = np.ones(X + 1, dtype=bool); s[:2] = False
    for i in range(2, int(X**0.5) + 1):
        if s[i]: s[i*i::i] = False
    np.save(pf, np.nonzero(s)[0].astype(np.uint32)); del s
P = np.load(pf)
for m in ms:
    out = f'/tmp/z32/cnt_m{m}.npy'
    if os.path.exists(out): continue
    b = f'/tmp/z32/L{m}.bin'
    if not os.path.exists(b): subprocess.run(['/tmp/z32/z32_ladder', str(m), str(X), b], check=True)
    c = np.fromfile(b, dtype=np.uint32); np.save(out, c[P]); os.remove(b); print('done', m, flush=True)
