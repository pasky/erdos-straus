# Z3077: sub-route failure sets F_m = {p prime, 5 <= p <= X, p ∤ m : Type II count f_m(p) = 0} (counts from scripts/z32_ladder.c,
# run as z32_ladder m 2000000; binaries kept in /tmp/z32, too large for the repo: 8 MB each).
# Reciprocity fit: candidate conditions are Legendre symbols (d/p) = eps for squarefree d | 4m (with d = -1 and d = 2 included).
# For each m we search single and pairwise conditions Cond(p) := [(d1/p)=e1 and (d2/p)=e2] that contain ALL failures, and report
# the smallest residual (failures not covered -> none by construction; we report the number of primes covered and the rate ratio).
import sys, struct, itertools
import numpy as np
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
X = 2000000
primes = [p for p in L.primes_upto(X) if p >= 5]
def leg_all(d):
    return np.array([L.legendre(d, p) for p in primes], dtype=np.int8)
out = []
for m in (6, 8, 10, 12, 16):
    cnt = np.fromfile(f'/tmp/z32/z32_m{m}.bin', dtype=np.uint32)
    pr = np.array(primes); mask = np.array([(m % p) != 0 for p in primes])
    pr = pr[mask]
    f = cnt[pr]
    fail = (f == 0)
    nf = int(fail.sum())
    ds = sorted({d for d in range(-1, 4*m+1) if d not in (0, 1, -1) and False} | {-1, 2, -2} | {q for q in range(2, 4*m+1) if all(q % r for r in range(2, int(q**0.5)+1)) and (4*m) % q == 0} | {-q for q in range(2, 4*m+1) if all(q % r for r in range(2, int(q**0.5)+1)) and (4*m) % q == 0})
    chars = {}
    for d in ds:
        chars[d] = np.array([L.legendre(d, int(p)) for p in pr], dtype=np.int8)
    best1 = None
    for d, arr in chars.items():
        for e in (1, -1):
            cond = arr == e
            if not cond.any(): continue
            miss = int((fail & ~cond).sum())
            rate_in = fail[cond].mean(); rate_out = fail[~cond].mean() if (~cond).any() else 0
            score = (miss, -(rate_in - rate_out))
            if best1 is None or score < best1[0]: best1 = (score, d, e, rate_in, rate_out, int(cond.sum()))
    best2 = None
    keys = list(chars)
    for d1, d2 in itertools.combinations(keys, 2):
        for e1, e2 in itertools.product((1, -1), repeat=2):
            cond = (chars[d1] == e1) & (chars[d2] == e2)
            if not cond.any(): continue
            miss = int((fail & ~cond).sum())
            if best2 is None or miss < best2[0][0] or (miss == best2[0][0] and cond.sum() < best2[5]):
                best2 = ((miss,), d1, d2, e1, e2, int(cond.sum()), float(fail[cond].mean()))
    print(f"m={m}: primes p<={X} (p∤m) = {len(pr)}, failures = {nf}; first failures {pr[fail][:12].tolist()}")
    print(f"   best single (d/p)=e: d={best1[1]} e={best1[2]} misses {best1[0][0]} failures, cond size {best1[5]}, failure rate in/out {best1[3]:.4f}/{best1[4]:.4f}")
    if best2: print(f"   best pair: (d1={best2[1]},e1={best2[3]}) & (d2={best2[2]},e2={best2[4]}) misses {best2[0][0]} failures, cond size {best2[5]}, failure rate inside {best2[6]:.4f}")
