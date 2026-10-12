"""O155: do smooth witness moduli suffice for the (A)3 system?

p is covered by (A,C) iff p = -A (mod q), q = 4AC-1, p >= q - A  (so B = (p+A)/q >= 1).
Count primes p = 1 (mod 24), p <= N, covered by: all (A,C); only q with P+(q) <= N^beta.
Usage: PYTHONPATH=scripts uv run python scripts/bs_tech_smooth_level.py [N]
"""
import sys
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
lpf = np.zeros(N + 1, dtype=np.int64)  # largest prime factor
for i in range(2, N + 1):
    if lpf[i] == 0:
        lpf[i::i] = i
isp = lpf == np.arange(N + 1)
isp[:2] = False
targets = isp.copy()
targets[np.arange(N + 1) % 24 != 1] = False
betas = [None, 0.5, 0.4, 0.3, 0.25, 0.2]
cov = {b: np.zeros(N + 1, dtype=bool) for b in betas}
A = 1
while 4 * A - 1 <= N + A:
    C = 1
    while True:
        q = 4 * A * C - 1
        if q > N + A:
            break
        start = max(q - A, (-A) % q)
        if start <= N:
            P = lpf[q] if q <= N else q  # q > N only when q <= N + A: treat as rough
            for b in betas:
                if b is None or P <= N ** b:
                    cov[b][start::q] = True
        C += 1
    A += 1
T = targets.sum()
print(f"N={N}: primes p=1(24): {T}")
for b in betas:
    miss = int((targets & ~cov[b]).sum())
    print(f"  moduli q with P+(q) <= N^{b}: uncovered {miss} ({miss/T:.4f})")
