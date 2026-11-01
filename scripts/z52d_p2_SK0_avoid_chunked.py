"""Z0650 (pass 2, SK0): chunked (memory-bounded) version of scripts/z52b_dividing_avoid.py.
Same model: random 'prime-like' residues N in Mordell hard classes mod 840 (coprime to primes 11..199), tested against
Type I families N ≡ -f (mod 4ad), f | 4a^2 d+1 and Type II families N ≡ -e (mod 4ab), e | a+b, ordered by parameter product.
Survivor counts are accumulated over chunks, so the total sample size can be 1e8 with bounded memory.
Usage: python z52d_p2_SK0_avoid_chunked.py X_MAX TOTAL_SAMPLES CHUNK"""
import numpy as np, sys, math, time
from sympy import divisors, primerange
X_MAX, TOTAL, CHUNK = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        m = 4 * a * d
        fams.append((a * d, m, sorted({(-f) % m for f in divisors(4 * a * a * d + 1)})))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        m = 4 * a * b
        fams.append((a * b, m, sorted({(-e) % m for e in divisors(a + b)})))
fams.sort(key=lambda t: (t[0], t[1]))
cps = sorted({int(round(10 ** (k / 4))) for k in range(4, 20)} | {X_MAX})
cps = [c for c in cps if c <= X_MAX]
surv = np.zeros(len(cps), dtype=np.int64)     # survivors at checkpoint (measured just before families of size > cp)
n0_total = 0
t0 = time.time()
rng_seed = 1
done = 0
while done < TOTAL:
    rng = np.random.default_rng(1000 + rng_seed); rng_seed += 1
    N = 840 * rng.integers(2**50, 2**51, size=CHUNK * 3, dtype=np.int64) + rng.choice([1, 121, 169, 289, 361, 529], size=CHUNK * 3)
    for q in primerange(11, 200):
        N = N[N % q != 0]
    N = N[:CHUNK]
    n0_total += len(N); done += CHUNK
    ci = 0
    for size, m, res in fams:
        while ci < len(cps) and size > cps[ci]:
            surv[ci] += len(N); ci += 1
        if len(N) == 0:
            break
        tab = np.zeros(m, dtype=bool); tab[res] = True
        N = N[~tab[N % m]]
    while ci < len(cps):
        surv[ci] += len(N); ci += 1
    print(f"chunk done: total_samples={n0_total} elapsed={time.time()-t0:.1f}s", flush=True)
print(f"families={len(fams)} samples={n0_total}")
for c, s in zip(cps, surv):
    d = s / n0_total
    lnX = math.log(c)
    pred = math.exp(-0.028 * lnX ** 3)
    print(f"X={c:6d} survivors={int(s):7d} delta={d:.3e} expected_count_at_0.028model={pred*n0_total:.2f} ln(delta)/(lnX)^3={(math.log(d)/lnX**3) if s>0 else float('nan'):.4f}")
