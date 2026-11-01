"""Z0666 (pass 2 fix, SK0): residue-avoidance model for m/n = 1/x+1/y+1/z with general m.
Families from Pomerance–Weingartner arXiv:2511.16817 Prop 2.1 (Type I) and Prop 2.3 (Type II):
  Type I : n ≡ -f (mod m a d),  f | m a^2 d + 1         (parameter size a*d)
  Type II: n ≡ -e (mod m a b),  e | a + b, a <= b       (parameter size a*b)
For m=4 these reduce to the moduli 4ad, 4ab of scripts/z52b_dividing_avoid.py (sanity check).
Model: random 'prime-like' n (coprime to primes 11..199) in the same residue classes mod 840 as the repo model.
Survivor fraction delta(X) after all families with parameter product <= X. Chunked, memory-bounded.
Usage: python z52d_p2_SK0_avoid_m.py m X_MAX TOTAL_SAMPLES CHUNK"""
import numpy as np, sys, math, time
from sympy import divisors, primerange
m, X_MAX, TOTAL, CHUNK = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        M = m * a * d
        fams.append((a * d, M, sorted({(-f) % M for f in divisors(m * a * a * d + 1)})))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        M = m * a * b
        fams.append((a * b, M, sorted({(-e) % M for e in divisors(a + b)})))
fams.sort(key=lambda t: (t[0], t[1]))
cps = sorted({int(round(10 ** (k / 4))) for k in range(4, 20)} | {X_MAX})
cps = [c for c in cps if c <= X_MAX]
surv = np.zeros(len(cps), dtype=np.int64)
n0_total = 0; seed = 0; done = 0; t0 = time.time()
while done < TOTAL:
    rng = np.random.default_rng(2000 + seed); seed += 1
    N = 840 * rng.integers(2**50, 2**51, size=CHUNK * 3, dtype=np.int64) + rng.choice([1, 121, 169, 289, 361, 529], size=CHUNK * 3)
    for q in primerange(11, 200):
        N = N[N % q != 0]
    N = N[:CHUNK]
    n0_total += len(N); done += CHUNK
    ci = 0
    for size, M, res in fams:
        while ci < len(cps) and size > cps[ci]:
            surv[ci] += len(N); ci += 1
        if len(N) == 0: break
        tab = np.zeros(M, dtype=bool); tab[res] = True
        N = N[~tab[N % M]]
    while ci < len(cps):
        surv[ci] += len(N); ci += 1
print(f"m={m} families={len(fams)} samples={n0_total} elapsed={time.time()-t0:.1f}s")
for c, s in zip(cps, surv):
    d = s / n0_total
    lnX = math.log(c)
    print(f"X={c:6d} survivors={int(s):8d} delta={d:.3e} ln(delta)/(lnX)^3={(math.log(d)/lnX**3) if s>0 else float('nan'):.4f}")
