"""O124 §8: numerics for the only rank-3 quadratic piece of ES, (Q_d): p = ef - 4 d a^2 with 4ad | f+1, b = ce-a >= 1
(Type II, ET (2.14),(2.18),(2.19)). For Mordell-hard primes p <= N (p mod 840 in {1,121,169,289,361,529}) record
  a_min(p) = least a such that some d <= DMAX gives a Type II solution via (Q_d),
and, for comparison, the number of all representations (e,f,a) of p by Q_d with a <= A (no side condition).
Usage: tern_qd.py N DMAX AMAX
"""
import sys, numpy as np
from collections import Counter
N, DMAX, AMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
LIM = N + 4*AMAX*AMAX*DMAX + 1
spf = np.zeros(LIM, dtype=np.int32)
for i in range(2, int(LIM**0.5)+1):
    if spf[i] == 0:
        blk = spf[i*i::i]; blk[blk == 0] = i
spf_l = spf  # 0 means prime
def factor(m):
    fs = {}
    while m > 1:
        q = int(spf_l[m]) or m
        fs[q] = fs.get(q, 0) + 1; m //= q
    return fs
def divisors(m):
    ds = [1]
    for q, k in factor(m).items():
        ds = [x*q**j for x in ds for j in range(k+1)]
    return ds
HARD = {1,121,169,289,361,529}
primes = [p for p in range(3, N+1) if spf[p] == 0 and p % 840 in HARD]
amin = Counter(); worst = []; tot_reps = 0; tot_side = 0
for p in primes:
    best = None
    for a in range(1, AMAX+1):
        for d in range(1, DMAX+1):
            m = p + 4*a*a*d; M = 4*a*d
            for f in divisors(m):
                if (f + 1) % M == 0:
                    c = (f+1)//M; e = m//f
                    if c*e - a >= 1:
                        best = a; break
            if best: break
        if best: break
    amin[best] += 1
    worst.append((best or 10**9, p))
# side-condition thinness on a sample: all reps with a <= 50, d = 1 vs those with 4a | f+1
SA = min(50, AMAX)
for p in primes[:2000]:
    for a in range(1, SA+1):
        ds = divisors(p + 4*a*a)
        tot_reps += len(ds); tot_side += sum(1 for f in ds if (f+1) % (4*a) == 0)
print(f"N={N} DMAX={DMAX} AMAX={AMAX}: {len(primes)} Mordell-hard primes")
print("a_min distribution:", sorted(amin.items(), key=lambda t: (t[0] is None, t[0] or 0)))
worst.sort(reverse=True); print("hardest:", worst[:10])
if tot_reps:
    print(f"sample {min(2000,len(primes))} primes, d=1, a<={SA}: all reps (e,f,a) = {tot_reps}, "
          f"with side condition 4a|f+1: {tot_side} (ratio {tot_side/tot_reps:.4f})")
