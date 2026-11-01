# Z3181: sporadic exceptions of the ternary form q0 = x^2+y^2+7z^2 (Ono–Soundararajan, GRH-conditional complete list),
# and their representability by all positive even ternary Gram matrices G of det <= DMAX (the form q_G(x) = x^T G x / 2).
# Exceptions computed numerically to NX (q0 values, exact via PARI qfrep).  For each exception n: number of classes of det<=DMAX
# representing n; whether any single class represents all exceptions.
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_ternary as T
pari = T.pari
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
NX = 3000
G0 = pari("[2,0,0;0,2,0;0,0,14]")
rep0 = [int(x) for x in pari(f"qfrep({G0},{NX},1)")]   # flag 1: entry i <-> norm i+1 (pairs ±x counted once)
exc = [n for n in range(1, NX+1) if rep0[n-1] == 0]
print("exceptions of x^2+y^2+7z^2 up to", NX, ":", exc)
allc = []
for det in range(8, DMAX+1, 2):
    allc += T.classes(det)
print("classes of even ternary forms with det <= %d: %d" % (DMAX, len(allc)), flush=True)
from collections import Counter
cnt = Counter()
universal = []
reps_cache = []
for G in allc:
    r = [int(x) for x in pari(f"qfrep({G},{NX},1)")]
    hit = [n for n in exc if r[n-1] > 0]
    for n in hit: cnt[n] += 1
    if len(hit) == len(exc): universal.append(G)
    reps_cache.append(len(hit))
print("number of classes representing each exception (exception: count):", {n: cnt[n] for n in exc})
print("classes representing ALL exceptions (up to NX):", len(universal))
print("classes representing exceptions at least once (max #exceptions represented by one class: %d of %d)" % (max(reps_cache), len(exc)))
