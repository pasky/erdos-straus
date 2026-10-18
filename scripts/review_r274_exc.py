"""R274: exception lists (f_m(p) = 0, 3 < p <= X, p prime, p ∤ m) from review_r274_ladder.c output."""
import sys, numpy as np
X = int(sys.argv[1])
sieve = np.ones(X + 1, bool); sieve[:2] = False
for i in range(2, int(X**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
P = np.nonzero(sieve)[0]
for m in map(int, sys.argv[2:]):
    c = np.fromfile(f'/tmp/r274/m{m}_1e7.bin', dtype=np.uint32)[:X + 1]
    Q = P[(P > 3) & (m % P != 0)]
    z = Q[c[Q] == 0]
    print(f'm={m}: #exc={len(z)} last={z[-1] if len(z) else None} first10={z[:10].tolist()} last5={z[-5:].tolist()}')
    np.save(f'/tmp/r274/exc{m}.npy', z)
