# z50 shifts: single-shift law. For random m uniform in (x/2, x], estimate
#   P(hit_v(m)) = P(m has a divisor d ≡ -1 (mod v))
# for v on a grid, at several scales x. Also records Omega(m) to compare with the
# few-prime-factor mechanism. EVIDENCE only.
# Usage: uv run --with sympy --with numpy python scripts/z50_shifts_single.py EXP SAMPLES SEED
import sys, random, math
import numpy as np
from sympy import factorint

E = int(sys.argv[1]); S = int(sys.argv[2]); seed = int(sys.argv[3])
random.seed(seed)
x = 10 ** E
VS = sorted(set([4, 8, 12, 24, 20, 28, 36, 40, 44, 48, 56, 60, 64, 72, 80, 96, 112, 128, 160, 192, 256, 320,
                 384, 512, 640, 768, 1024, 1280, 1536, 2048, 3072, 4096, 6144, 8192, 12288, 16384,
                 7, 15, 23, 31, 39, 47, 63, 79, 95, 127, 255, 511, 1023]))
hits = np.zeros(len(VS), dtype=np.int64)
omega_hist = {}
for _ in range(S):
    m = random.randrange(x // 2 + 1, x + 1)
    f = factorint(m)
    divs = np.array([1], dtype=object)
    for p, a in f.items():
        divs = np.concatenate([divs * (p ** k) for k in range(a + 1)])
    Om = sum(f.values()); omega_hist[Om] = omega_hist.get(Om, 0) + 1
    for i, v in enumerate(VS):
        r = (divs % v).astype(np.int64)
        if np.any(r == v - 1):
            hits[i] += 1
print(f"# x=1e{E} samples={S} seed={seed} loglogx={math.log(math.log(x)):.3f} logx={math.log(x):.3f}")
print("# v  P(hit_v)  phi(v)")
from sympy import totient
for v, h in zip(VS, hits):
    print(v, h / S, int(totient(v)))
print("# Omega histogram", sorted(omega_hist.items()))
